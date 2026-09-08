#!/usr/bin/env node
'use strict';
/*
 * BlenderBridge - VCP 插件
 * 打通 VCP <-> Blender 官方 MCP Server <-> Blender Add-on 的三端桥接。
 *
 * 架构（双跳）:
 *   VCP (stdio) <-> BlenderBridge <-> blender-mcp (Streamable HTTP :6090)
 *                                     <-> Blender Add-on (TCP :9876, null 分帧 JSON)
 *
 * 设计参照:
 *   - GodotBridge 的渐进式发现（Blender MCP 有 40+ 工具，不可一次性塞给模型）。
 *   - PenpotBridge 验证过的 MCP over Streamable HTTP 内核（SSE/JSON 双兼容 + session）。
 *
 * 依赖: 仅 Node.js 内置模块 (http/https)。
 */
const http = require('http');
const https = require('https');
const { URL } = require('url');

// 换行/回车常量。不写字面转义序列，避免本文件在经过会处理转义的写入工具时被破坏。
const NL = String.fromCharCode(10);
const CR = String.fromCharCode(13);

// ---------- GMR ex 模块（可选）----------
// 生成式动作绑定的模型仓库/训练/推理能力放在 gmr/ 子目录，与桥接本体解耦。
// 删除整个 gmr/ 目录不影响下方 6 个原生子命令，桥接照常工作。
// 快回路（Blender 拖拽推理）不经过本插件，由 Add-on 直连 sidecar:6091——
// 上游单并发(BLENDER_BUSY) + 双跳延迟，交互推理走这里必然请求堆积锁死。
let GMR = null;
let GMR_LOAD_ERROR = null;
try {
  GMR = require('./gmr');
} catch (e) {
  // MODULE_NOT_FOUND 属正常（模块未安装）；其它错误留痕便于诊断
  if (e && e.code !== 'MODULE_NOT_FOUND') GMR_LOAD_ERROR = e.message;
}

// ---------- 配置读取 ----------
const CONFIG = {
  url: process.env.BLENDER_MCP_URL || 'http://127.0.0.1:6090/',
  timeout: parseInt(process.env.REQUEST_TIMEOUT_MS || '60000', 10),
  protocolVersion: process.env.MCP_PROTOCOL_VERSION || '2025-06-18',
  debug: String(process.env.DebugMode) === 'true',
};

// ---------- MCP over Streamable HTTP 客户端 ----------
let _requestId = 0;
function nextId() { return ++_requestId; }
let _sessionId = null;

function postJsonRpc(method, params) {
  return new Promise((resolve, reject) => {
    let target;
    try {
      target = new URL(CONFIG.url);
    } catch (e) {
      return reject(new Error(`无效的 BLENDER_MCP_URL: ${CONFIG.url}`));
    }
    const payload = JSON.stringify({
      jsonrpc: '2.0',
      id: nextId(),
      method,
      params: params || {},
    });
    const headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json, text/event-stream',
      'Content-Length': Buffer.byteLength(payload),
    };
    if (_sessionId) headers['Mcp-Session-Id'] = _sessionId;
    const isHttps = target.protocol === 'https:';
    const lib = isHttps ? https : http;
    const options = {
      hostname: target.hostname,
      port: target.port || (isHttps ? 443 : 80),
      path: target.pathname + target.search,
      method: 'POST',
      headers,
      timeout: CONFIG.timeout,
    };
    const req = lib.request(options, (res) => {
      const sid = res.headers['mcp-session-id'];
      if (sid) _sessionId = sid;
      let raw = '';
      res.setEncoding('utf8');
      res.on('data', (chunk) => { raw += chunk; });
      res.on('end', () => {
        if (res.statusCode >= 400) {
          return reject(new Error(`HTTP ${res.statusCode}: ${raw.slice(0, 500)}`));
        }
        const parsed = parseMcpResponse(raw, res.headers['content-type'] || '');
        if (parsed == null) {
          return reject(new Error(`无法解析 MCP 响应: ${raw.slice(0, 500)}`));
        }
        if (parsed.error) {
          return reject(new Error(`MCP 错误 ${parsed.error.code}: ${parsed.error.message}`));
        }
        resolve(parsed.result);
      });
    });
    req.on('timeout', () => { req.destroy(new Error(`请求超时 (${CONFIG.timeout}ms)`)); });
    req.on('error', (err) => {
      if (err.code === 'ECONNREFUSED') {
        return reject(new Error(`无法连接 blender-mcp (${CONFIG.url})。请确认：1) blender-mcp 已启动 (uv run blender-mcp --transport http --port 6090)；2) Blender 正在运行且 MCP 插件已启用、面板显示 Server is running；3) 系统偏好已开启 Allow Online Access。`));
      }
      reject(err);
    });
    req.write(payload);
    req.end();
  });
}

// Streamable HTTP 可能返回 application/json 或 text/event-stream(SSE)
function parseMcpResponse(raw, contentType) {
  const text = String(raw || '').trim();
  if (!text) return null;
  const looksLikeSse = contentType.includes('text/event-stream')
    || text.startsWith('event:')
    || text.startsWith('data:')
    || text.indexOf(NL + 'data:') >= 0;
  if (looksLikeSse) {
    // 先剥掉 CR 再按 LF 切分，兼容 CRLF 与 LF 两种行尾
    const lines = text.split(CR).join('').split(NL).filter((l) => l.startsWith('data:'));
    for (let i = lines.length - 1; i >= 0; i--) {
      const jsonStr = lines[i].slice(5).trim();
      try {
        const obj = JSON.parse(jsonStr);
        if (obj && (obj.result !== undefined || obj.error !== undefined)) return obj;
      } catch (e) { /* 跳过非 JSON 行 */ }
    }
    return null;
  }
  try {
    return JSON.parse(text);
  } catch (e) {
    return null;
  }
}

let _initialized = false;
async function ensureInitialized() {
  if (_initialized) return;
  await postJsonRpc('initialize', {
    protocolVersion: CONFIG.protocolVersion,
    capabilities: {},
    clientInfo: { name: 'VCP-BlenderBridge', version: '1.1.0' },
  });
  try {
    await postJsonRpc('notifications/initialized', {});
  } catch (e) { /* 忽略 */ }
  _initialized = true;
}

async function listTools() {
  await ensureInitialized();
  const result = await postJsonRpc('tools/list', {});
  return (result && Array.isArray(result.tools)) ? result.tools : [];
}

async function callMcpTool(name, args) {
  await ensureInitialized();
  return await postJsonRpc('tools/call', { name, arguments: args || {} });
}

// ---------- 领域归类（按工具名前缀，不硬编码工具清单）----------
function classifyDomain(toolName) {
  const n = toolName || '';
  if (n.startsWith('get_blendfile_summary')) return 'blendfile';
  if (n.startsWith('geonodes')) return 'geonodes';
  if (n.startsWith('gp_')) return 'greasepencil';
  if (n.startsWith('render')) return 'render';
  if (n.startsWith('get_screenshot')) return 'screenshot';
  if (n.startsWith('jump_to')) return 'navigation';
  if (n.startsWith('object_') || n === 'get_object_detail_summary' || n === 'get_objects_summary') return 'object';
  if (n.includes('material')) return 'material';
  if (n.startsWith('mesh_')) return 'mesh';
  if (n.startsWith('armature') || n.startsWith('action') || n === 'camera_target_track') return 'animation';
  if (n.startsWith('asset') || n.startsWith('blend_library')) return 'asset';
  if (n.includes('api_docs') || n.includes('manual_docs') || n === 'get_python_api_docs') return 'docs';
  if (n === 'get_scene_state') return 'scene';
  if (n.startsWith('execute_blender_code')) return 'exec';
  return 'other';
}

// ---------- 结果适配 ----------
// 图像不在本插件内解码或落盘，而是原样交给 VCP 的多模态通道，
// 由 VCP 统一处理图像文件——这样 Agent 能真正看见截图与渲染结果，
// 且不必在此重复实现一套路径管理与清理策略。
//
// 上游另有 render_thumbnail_to_path / render_viewport_to_path 两个自带落盘语义的工具，
// 它们直接返回路径而不产生 image 内容项。需要规避大图占用上下文时优先用那两个。
function adaptResult(toolName, result) {
  if (!result) return { tool: toolName, text: '(空响应)' };
  const out = { tool: toolName };
  if (result.isError) out.isError = true;
  if (result.structuredContent !== undefined) out.structured = result.structuredContent;
  if (Array.isArray(result.content)) {
    const texts = [];
    const images = [];
    for (const item of result.content) {
      if (!item || typeof item !== 'object') continue;
      if (item.type === 'text') {
        texts.push(item.text);
      } else if (item.type === 'image') {
        const mime = item.mimeType || 'image/png';
        if (item.data) {
          images.push({ mimeType: mime, base64: String(item.data) });
        } else {
          texts.push(`(上游返回了 ${mime} 图像项，但缺少 data 字段)`);
        }
      } else {
        texts.push(JSON.stringify(item).slice(0, 400));
      }
    }
    if (texts.length) out.text = texts.join(NL);
    if (images.length) out.images = images;
  }
  if (out.text === undefined && out.images === undefined && out.structured === undefined) out.raw = result;
  return out;
}

// 把含图像的结果转成 VCP 多模态 content 数组。
// 纯文本结果不走这里，仍按原有的字符串通路返回，避免改变既有行为。
function toMultimodalContent(adapted) {
  const parts = [];
  const textLines = [];
  if (adapted.tool) textLines.push(`工具: ${adapted.tool}`);
  if (adapted.isError) textLines.push('（上游标记为错误）');
  if (adapted.text) textLines.push(adapted.text);
  if (adapted.structured !== undefined) {
    textLines.push('structured: ' + JSON.stringify(adapted.structured, null, 2));
  }
  const imgs = adapted.images || [];
  let totalBytes = 0;
  for (const im of imgs) totalBytes += im.base64.length;
  if (imgs.length) {
    textLines.push(`附带 ${imgs.length} 张图像（base64 合计约 ${Math.round(totalBytes / 1024)} KB）。`);
    if (totalBytes > 2 * 1024 * 1024) {
      textLines.push('提示：本次图像较大。若只需确认构图，改用 render_thumbnail_to_path 或 render_viewport_to_path，它们返回文件路径而非内联图像。');
    }
  }
  parts.push({ type: 'text', text: textLines.join(NL) });
  for (const im of imgs) {
    parts.push({
      type: 'image_url',
      image_url: { url: `data:${im.mimeType};base64,${im.base64}` },
    });
  }
  return parts;
}

// ---------- 子命令处理 ----------
async function handleStatus() {
  const tools = await listTools();
  const domains = {};
  for (const t of tools) {
    const d = classifyDomain(t.name);
    domains[d] = (domains[d] || 0) + 1;
  }
  return {
    connected: true,
    endpoint: CONFIG.url,
    protocolVersion: CONFIG.protocolVersion,
    totalTools: tools.length,
    domains,
    hint: '渐进式发现: list_domains -> discover_tools -> get_tool_schema -> call_tool。程序化建模用 create_model。',
  };
}

async function handleListDomains() {
  const tools = await listTools();
  const domains = {};
  for (const t of tools) {
    const d = classifyDomain(t.name);
    domains[d] = (domains[d] || 0) + 1;
  }
  return { totalTools: tools.length, domains };
}

async function handleDiscoverTools(input) {
  const domain = (input.domain || '').trim();
  if (!domain) throw new Error('discover_tools 需要参数 domain。先用 list_domains 查看可用领域。');
  const tools = await listTools();
  const matched = tools
    .filter((t) => classifyDomain(t.name) === domain)
    .map((t) => ({ name: t.name, description: (t.description || '').split(NL)[0].slice(0, 160) }));
  if (!matched.length) throw new Error(`领域 "${domain}" 下无工具，或领域名有误。用 list_domains 核对。`);
  return { domain, count: matched.length, tools: matched };
}

async function handleGetToolSchema(input) {
  const tool = (input.tool || '').trim();
  if (!tool) throw new Error('get_tool_schema 需要参数 tool（工具名）。');
  const tools = await listTools();
  const found = tools.find((t) => t.name === tool);
  if (!found) throw new Error(`未找到工具 "${tool}"。用 discover_tools 查看某领域的工具名。`);
  return {
    name: found.name,
    description: found.description || '',
    inputSchema: found.inputSchema || {},
  };
}

async function handleCallTool(input) {
  const tool = (input.tool || '').trim();
  if (!tool) throw new Error('call_tool 需要参数 tool（工具名）。');
  let args = input.arguments;
  if (typeof args === 'string') {
    try { args = JSON.parse(args); } catch (e) { throw new Error(`arguments 不是合法 JSON: ${e.message}`); }
  }
  const result = await callMcpTool(tool, args || {});
  return adaptResult(tool, result);
}

// 模型自制逃生舱：execute_blender_code 的语义别名。
// 通过 bpy 在 Blender 内程序化建模；也是未来接入文生 3D / 生成式建模插件的注入点。
// 详见同目录「模型自制说明.md」。
async function handleCreateModel(input) {
  const code = input.code;
  if (!code || !String(code).trim()) {
    throw new Error('create_model 需要参数 code（在 Blender 内执行的 Python，通过 bpy 程序化建模；代码中 result 变量须为 dict 且 JSON 可序列化）。详见「模型自制说明.md」。');
  }
  const result = await callMcpTool('execute_blender_code', { code: String(code) });
  return adaptResult('execute_blender_code(create_model)', result);
}

// ---------- 输入读取与分发 ----------
function readStdin() {
  return new Promise((resolve) => {
    let data = '';
    let settled = false;
    const finish = (val) => {
      if (settled) return;
      settled = true;
      clearTimeout(guard);
      resolve(val);
    };
    process.stdin.setEncoding('utf8');
    process.stdin.on('data', (c) => { data += c; });
    process.stdin.on('end', () => finish(data));
    // 兜底：stdin 迟迟不关闭时的保护。unref() 确保它不会阻止进程正常退出，
    // 避免正常 EOF 后仍有幽灵计时器挂在 event loop 里（曾导致 PTY 环境误判超时）。
    const guard = setTimeout(() => finish(data), CONFIG.timeout + 5000);
    if (guard.unref) guard.unref();
  });
}

function parseInput(raw) {
  const text = String(raw || '').trim();
  if (!text) return {};
  try { return JSON.parse(text); } catch (e) { return {}; }
}

async function main() {
  const raw = await readStdin();
  const input = parseInput(raw);
  const command = (input.command || 'status').trim();
  try {
    let data;
    switch (command) {
      case 'status':
        data = await handleStatus();
        break;
      case 'list_domains':
        data = await handleListDomains();
        break;
      case 'discover_tools':
        data = await handleDiscoverTools(input);
        break;
      case 'get_tool_schema':
        data = await handleGetToolSchema(input);
        break;
      case 'call_tool':
        data = await handleCallTool(input);
        break;
      case 'create_model':
        data = await handleCreateModel(input);
        break;
      default:
        // 未命中原生子命令时，尝试交给 GMR ex 模块处理
        if (GMR && GMR.has(command)) {
          data = await GMR.handle(command, input);
          break;
        }
        {
          const native = 'status | list_domains | discover_tools | get_tool_schema | call_tool | create_model';
          let msg = `未知 command "${command}"。`;
          if (GMR) {
            msg += NL + `桥接本体: ${native}`;
            msg += NL + `GMR 扩展: ${GMR.commands.join(' | ')}`;
            msg += NL + '用 gmr_help 查看 GMR 各命令的完整参数说明。';
          } else {
            msg += `可用: ${native}`;
            msg += NL + (GMR_LOAD_ERROR
              ? `（GMR ex 模块加载失败，故其命令不可用: ${GMR_LOAD_ERROR}）`
              : '（GMR ex 模块未安装。若需模型训练/导入与推理管理，请补全 gmr/ 目录。）');
          }
          throw new Error(msg);
        }
    }

    // 含图像时返回多模态 content 数组，交由 VCP 处理图像；
    // 其余情况保持原有的字符串结果，行为不变。
    let payload;
    if (data && typeof data === 'object' && Array.isArray(data.images) && data.images.length) {
      payload = toMultimodalContent(data);
    } else if (typeof data === 'string') {
      payload = data;
    } else {
      payload = JSON.stringify(data, null, 2);
    }

    process.stdout.write(JSON.stringify({
      status: 'success',
      result: payload,
    }));
  } catch (err) {
    process.stdout.write(JSON.stringify({
      status: 'error',
      error: err && err.message ? err.message : String(err),
    }));
    process.exitCode = 1;
  }
}

main();