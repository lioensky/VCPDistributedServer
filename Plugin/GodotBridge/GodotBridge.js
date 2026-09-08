#!/usr/bin/env node
'use strict';

/*
 * GodotBridge - VCP 插件
 * 作为标准 MCP Client 连接 Godot MCP Native 插件，
 * 通过渐进式工具发现让 VCP Agent 操作 Godot 项目。
 *
 * 协议: stdio (VCP) <-> Streamable HTTP (Godot MCP)
 * 依赖: 仅 Node.js 内置模块 (http/https)
 */

const http = require('http');
const https = require('https');
const { URL } = require('url');

// ---------- 配置读取 ----------
const CONFIG = {
  url: process.env.GODOT_MCP_URL || 'http://127.0.0.1:9080/mcp',
  token: process.env.GODOT_MCP_TOKEN || '',
  timeout: parseInt(process.env.REQUEST_TIMEOUT_MS || '30000', 10),
  protocolVersion: process.env.MCP_PROTOCOL_VERSION || '2025-06-18',
};

// ---------- 工具领域分类 ----------
// 依据 Godot MCP Native 的命名前缀归类，供 list_domains / discover_tools 使用。
function classifyDomain(toolName) {
  const n = String(toolName || '').toLowerCase();
  if (/(^|-)runtime(-|$)|runtime-/.test(n)) return 'runtime';
  if (/node/.test(n)) return 'node';
  if (/script|symbol/.test(n)) return 'script';
  if (/scene/.test(n)) return 'scene';
  if (/debug|breakpoint|stack|profiler|debugger/.test(n)) return 'debug';
  if (/editor|inspector|screenshot|export/.test(n)) return 'editor';
  if (/project|resource|input-action|autoload|test|uid|dependency|tileset/.test(n)) return 'project';
  return 'other';
}

// ---------- MCP over Streamable HTTP 客户端 ----------
let _requestId = 0;
function nextId() { return ++_requestId; }

// 会话状态：Streamable HTTP 首次 initialize 后可能返回 Mcp-Session-Id
let _sessionId = null;

function postJsonRpc(method, params) {
  return new Promise((resolve, reject) => {
    let target;
    try {
      target = new URL(CONFIG.url);
    } catch (e) {
      return reject(new Error(`无效的 GODOT_MCP_URL: ${CONFIG.url}`));
    }

    const payload = JSON.stringify({
      jsonrpc: '2.0',
      id: nextId(),
      method,
      params: params || {},
    });

    const headers = {
      'Content-Type': 'application/json',
      // Streamable HTTP 要求客户端声明可接受 json 与 event-stream
      'Accept': 'application/json, text/event-stream',
      'Content-Length': Buffer.byteLength(payload),
    };
    if (CONFIG.token) headers['Authorization'] = `Bearer ${CONFIG.token}`;
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
      // 捕获会话 ID
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
        return reject(new Error(`无法连接 Godot MCP (${CONFIG.url})。请确认 Godot 编辑器已启动并启用了 MCP Native 插件的 HTTP 模式。`));
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

  if (contentType.includes('text/event-stream') || text.startsWith('event:') || text.includes('\ndata:') || text.startsWith('data:')) {
    // 逐行提取 data: 负载，取最后一个可解析为带 id 的 JSON-RPC 对象
    const dataLines = text.split(/\r?\n/).filter((l) => l.startsWith('data:'));
    for (let i = dataLines.length - 1; i >= 0; i--) {
      const jsonStr = dataLines[i].slice(5).trim();
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

// initialize 握手 —— 每个进程生命周期执行一次
let _initialized = false;
async function ensureInitialized() {
  if (_initialized) return;
  await postJsonRpc('initialize', {
    protocolVersion: CONFIG.protocolVersion,
    capabilities: {},
    clientInfo: { name: 'VCP-GodotBridge', version: '1.0.0' },
  });
  // 通知服务器初始化完成（notification 无需等待结果，容错处理）
  try {
    await postJsonRpc('notifications/initialized', {});
  } catch (e) { /* 部分实现不要求此通知，忽略 */ }
  _initialized = true;
}

// 拉取全部工具（支持分页 cursor）
async function fetchAllTools() {
  await ensureInitialized();
  const tools = [];
  let cursor;
  do {
    const params = cursor ? { cursor } : {};
    const result = await postJsonRpc('tools/list', params);
    if (result && Array.isArray(result.tools)) tools.push(...result.tools);
    cursor = result ? result.nextCursor : undefined;
  } while (cursor);
  return tools;
}

// ---------- 子命令处理 ----------
async function handleStatus() {
  const tools = await fetchAllTools();
  const domains = {};
  for (const t of tools) {
    const d = classifyDomain(t.name);
    domains[d] = (domains[d] || 0) + 1;
  }
  return {
    connected: true,
    endpoint: CONFIG.url,
    sessionId: _sessionId || null,
    protocolVersion: CONFIG.protocolVersion,
    totalTools: tools.length,
    domains,
  };
}

async function handleListDomains() {
  const tools = await fetchAllTools();
  const domains = {};
  for (const t of tools) {
    const d = classifyDomain(t.name);
    domains[d] = (domains[d] || 0) + 1;
  }
  return {
    totalTools: tools.length,
    domains,
    hint: '使用 discover_tools 并传入 domain 查看某领域的工具清单。',
  };
}

async function handleDiscoverTools(args) {
  const domain = (args.domain || '').trim().toLowerCase();
  if (!domain) throw new Error('discover_tools 需要参数 domain。可先用 list_domains 查看可用领域。');
  const tools = await fetchAllTools();
  const filtered = tools
    .filter((t) => classifyDomain(t.name) === domain)
    .map((t) => ({
      name: t.name,
      description: firstLine(t.description),
    }));
  if (filtered.length === 0) {
    return { domain, count: 0, tools: [], hint: '该领域无工具或领域名有误，请用 list_domains 核对。' };
  }
  return {
    domain,
    count: filtered.length,
    tools: filtered,
    hint: '使用 get_tool_schema 传入 tool 查看某工具完整参数。',
  };
}

async function handleGetToolSchema(args) {
  const toolName = (args.tool || '').trim();
  if (!toolName) throw new Error('get_tool_schema 需要参数 tool。');
  const tools = await fetchAllTools();
  const found = tools.find((t) => t.name === toolName);
  if (!found) {
    const suggestions = tools
      .filter((t) => t.name.includes(toolName) || toolName.includes(t.name))
      .slice(0, 5)
      .map((t) => t.name);
    throw new Error(`未找到工具 "${toolName}"。${suggestions.length ? '相近工具: ' + suggestions.join(', ') : '请用 discover_tools 核对名称。'}`);
  }
  return {
    name: found.name,
    description: found.description,
    inputSchema: found.inputSchema || {},
  };
}

async function handleCallTool(args) {
  const toolName = (args.tool || '').trim();
  if (!toolName) throw new Error('call_tool 需要参数 tool。');

  let toolArgs = args.arguments;
  if (typeof toolArgs === 'string') {
    const s = toolArgs.trim();
    if (s === '' ) {
      toolArgs = {};
    } else {
      try {
        toolArgs = JSON.parse(s);
      } catch (e) {
        throw new Error(`arguments 不是合法 JSON: ${e.message}`);
      }
    }
  }
  if (toolArgs == null) toolArgs = {};
  if (typeof toolArgs !== 'object' || Array.isArray(toolArgs)) {
    throw new Error('arguments 必须是一个 JSON 对象。');
  }

  await ensureInitialized();
  const result = await postJsonRpc('tools/call', {
    name: toolName,
    arguments: toolArgs,
  });

  return adaptToolResult(toolName, result);
}

// ---------- 结果适配 ----------
function adaptToolResult(toolName, result) {
  if (!result) return { tool: toolName, content: '(空响应)' };

  const out = { tool: toolName };
  if (result.isError) out.isError = true;

  if (Array.isArray(result.content)) {
    const texts = [];
    const media = [];
    for (const item of result.content) {
      if (!item || typeof item !== 'object') continue;
      if (item.type === 'text') {
        texts.push(item.text);
      } else if (item.type === 'image') {
        // 避免把大段 base64 直接塞进文本结果，只保留元信息
        media.push({ type: 'image', mimeType: item.mimeType || 'image/png', bytes: item.data ? item.data.length : 0 });
      } else if (item.type === 'resource') {
        texts.push(`[resource] ${JSON.stringify(item.resource || {}).slice(0, 400)}`);
      } else {
        texts.push(JSON.stringify(item).slice(0, 400));
      }
    }
    if (texts.length) out.text = texts.join('\n');
    if (media.length) out.media = media;
  }

  if (result.structuredContent !== undefined) {
    out.structured = result.structuredContent;
  }

  if (out.text === undefined && out.structured === undefined && out.media === undefined) {
    out.raw = result;
  }
  return out;
}

function firstLine(str) {
  if (!str) return '';
  const s = String(str).trim();
  const idx = s.indexOf('\n');
  return idx === -1 ? s : s.slice(0, idx);
}

// ---------- 输入读取与分发 ----------
function readStdin() {
  return new Promise((resolve) => {
    let data = '';
    process.stdin.setEncoding('utf8');
    process.stdin.on('data', (c) => { data += c; });
    process.stdin.on('end', () => resolve(data));
    // 若无 stdin（超时保护）
    setTimeout(() => { if (!data) resolve(''); }, CONFIG.timeout + 5000);
  });
}

function parseInput(raw) {
  const text = String(raw || '').trim();
  if (!text) return {};
  try {
    return JSON.parse(text);
  } catch (e) {
    // 兼容极简 key=value 情况（一般 VCP 传 JSON，此处兜底）
    return {};
  }
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
      default:
        throw new Error(`未知 command "${command}"。可用: status | list_domains | discover_tools | get_tool_schema | call_tool`);
    }
    process.stdout.write(JSON.stringify({
      status: 'success',
      result: JSON.stringify(data, null, 2),
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