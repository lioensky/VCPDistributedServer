#!/usr/bin/env node
'use strict';

/*
 * PenpotBridge - VCP 插件（原生内接层）
 *
 * 设计要害（区别于 GodotBridge 的裸透传）：
 * Penpot MCP 只有 5 个工具，且核心是 execute_code —— 要 LLM 先啃 API 文档再手写 JS。
 * 太原始。本桥在中间放一层"语义收敛"：把常用设计操作预写成 Plugin API 代码片段，
 * 包装成高层 VCP 命令（overview / api_info / list_pages / get_selection / get_page_tree /
 * create_rect / create_text / export / exec）。exec 作为逃生舱，仍可执行任意代码。
 *
 * 协议: stdio (VCP) <-> Streamable HTTP (Penpot MCP :4401/mcp)
 * 依赖: 仅 Node.js 内置模块 (http/https)
 */

const http = require('http');
const https = require('https');
const { URL } = require('url');

// ---------- 配置读取 ----------
const CONFIG = {
  url: process.env.PENPOT_MCP_URL || 'http://[::1]:4401/mcp',
  userToken: process.env.PENPOT_MCP_USER_TOKEN || '',
  timeout: parseInt(process.env.REQUEST_TIMEOUT_MS || '60000', 10),
  protocolVersion: process.env.MCP_PROTOCOL_VERSION || '2025-06-18',
  debug: String(process.env.DebugMode) === 'true',
};

// ---------- MCP over Streamable HTTP 客户端（复用 GodotBridge 验证过的内核）----------
let _requestId = 0;
function nextId() { return ++_requestId; }
let _sessionId = null;

function postJsonRpc(method, params) {
  return new Promise((resolve, reject) => {
    let target;
    try {
      target = new URL(CONFIG.url);
    } catch (e) {
      return reject(new Error(`无效的 PENPOT_MCP_URL: ${CONFIG.url}`));
    }
    // 多用户模式：userToken 通过 query 传递（见 PenpotMcpServer.setupHttpEndpoints）
    if (CONFIG.userToken && !target.searchParams.has('userToken')) {
      target.searchParams.set('userToken', CONFIG.userToken);
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
        return reject(new Error(`无法连接 Penpot MCP (${CONFIG.url})。请确认：1) mcp-server 已启动(npm run bootstrap)；2) 浏览器已打开 Penpot 并加载插件，点击了 "Connect to MCP server"，且插件 UI 未关闭。`));
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

let _initialized = false;
async function ensureInitialized() {
  if (_initialized) return;
  await postJsonRpc('initialize', {
    protocolVersion: CONFIG.protocolVersion,
    capabilities: {},
    clientInfo: { name: 'VCP-PenpotBridge', version: '1.0.0' },
  });
  try {
    await postJsonRpc('notifications/initialized', {});
  } catch (e) { /* 忽略 */ }
  _initialized = true;
}

// 调用底层 MCP 工具
async function callMcpTool(name, args) {
  await ensureInitialized();
  const result = await postJsonRpc('tools/call', { name, arguments: args || {} });
  return result;
}

// 从 MCP content 数组提取纯文本
function extractText(result) {
  if (!result) return '';
  if (Array.isArray(result.content)) {
    return result.content
      .filter((i) => i && i.type === 'text')
      .map((i) => i.text)
      .join('\n');
  }
  return '';
}

// ============================================================
// 语义收敛层：预置 Plugin API 代码片段
// 把常用设计操作固化为经过验证的 JS 片段，Agent 无需先啃 API 文档手写代码。
// 每个片段都是 execute_code 的 body（"想象成一个函数体，return 即工具返回值"）。
// ============================================================

const SNIPPETS = {
  // 列出当前文件所有页面及其顶层结构
  list_pages: () => `
    const file = penpot.currentFile;
    const pages = (file.pages || []).map(p => ({
      id: p.id,
      name: p.name,
      rootChildren: (p.root && p.root.children ? p.root.children : []).map(c => ({
        id: c.id, name: c.name, type: c.type
      }))
    }));
    return { fileName: file.name, pageCount: pages.length, pages };
  `,

  // 读取当前选中的图形
  get_selection: () => `
    const sel = penpot.selection || [];
    return sel.map(s => ({
      id: s.id, name: s.name, type: s.type,
      x: s.x, y: s.y, width: s.width, height: s.height
    }));
  `,

  // 读取当前页面的浅层结构树（深度 3）
  get_page_tree: () => `
    const page = penpot.currentPage;
    function walk(node, depth) {
      const info = { id: node.id, name: node.name, type: node.type };
      if (depth > 0 && node.children && node.children.length) {
        info.children = node.children.map(c => walk(c, depth - 1));
      }
      return info;
    }
    const root = page.root;
    return { pageName: page.name, tree: (root.children || []).map(c => walk(c, 3)) };
  `,

  // 创建矩形
  create_rect: (a) => `
    const rect = penpot.createRectangle();
    rect.x = ${Number(a.x) || 0};
    rect.y = ${Number(a.y) || 0};
    rect.resize(${Number(a.width) || 100}, ${Number(a.height) || 100});
    ${a.name ? `rect.name = ${JSON.stringify(String(a.name))};` : ''}
    ${a.fill ? `rect.fills = [{ fillColor: ${JSON.stringify(String(a.fill))} }];` : ''}
    return { id: rect.id, name: rect.name, type: rect.type };
  `,

  // 创建文本
  create_text: (a) => `
    const text = penpot.createText(${JSON.stringify(String(a.text || 'Text'))});
    text.x = ${Number(a.x) || 0};
    text.y = ${Number(a.y) || 0};
    ${a.fontSize ? `text.fontSize = ${JSON.stringify(String(a.fontSize))};` : ''}
    ${a.fill ? `text.fills = [{ fillColor: ${JSON.stringify(String(a.fill))} }];` : ''}
    return { id: text.id, name: text.name, type: text.type };
  `,
};

// ---------- 高层命令处理 ----------

// 读使用说明（一次性；Agent 读过后不应重复调用）
async function handleOverview() {
  const result = await callMcpTool('high_level_overview', {});
  return { overview: extractText(result) };
}

// 查 Penpot API 文档
async function handleApiInfo(input) {
  const type = (input.type || '').trim();
  if (!type) throw new Error('api_info 需要参数 type（Penpot API 类型名，如 Penpot / Shape / Board）。可选 member 查具体成员。');
  const args = { type };
  if (input.member) args.member = String(input.member).trim();
  const result = await callMcpTool('penpot_api_info', args);
  return { type, member: args.member || null, doc: extractText(result) };
}

// 执行预置片段
async function runSnippet(name, args) {
  const builder = SNIPPETS[name];
  if (!builder) throw new Error(`未知预置片段: ${name}`);
  const code = builder(args || {});
  const result = await callMcpTool('execute_code', { code });
  return extractText(result);
}

// 逃生舱：执行任意代码
async function handleExec(input) {
  const code = input.code;
  if (!code || !String(code).trim()) {
    throw new Error('exec 需要参数 code（在 Penpot 插件上下文执行的 JS，可用 penpot / penpotUtils / storage 对象；想象成函数体，return 即返回值）。');
  }
  const result = await callMcpTool('execute_code', { code: String(code) });
  return { result: extractText(result) || '(无返回值)' };
}

// 导出图形
async function handleExport(input) {
  const args = {};
  if (input.shapeId) args.shapeId = String(input.shapeId);
  if (input.format) args.format = String(input.format);
  if (input.scale) args.scale = input.scale;
  const result = await callMcpTool('export_shape', args);
  return adaptResult('export_shape', result);
}

// ---------- 结果适配（图片仅留元信息，避免 base64 污染文本）----------
function adaptResult(toolName, result) {
  if (!result) return { tool: toolName, content: '(空响应)' };
  const out = { tool: toolName };
  if (result.isError) out.isError = true;
  if (Array.isArray(result.content)) {
    const texts = [];
    const media = [];
    for (const item of result.content) {
      if (!item || typeof item !== 'object') continue;
      if (item.type === 'text') texts.push(item.text);
      else if (item.type === 'image') media.push({ type: 'image', mimeType: item.mimeType || 'image/png', bytes: item.data ? item.data.length : 0 });
      else texts.push(JSON.stringify(item).slice(0, 400));
    }
    if (texts.length) out.text = texts.join('\n');
    if (media.length) out.media = media;
  }
  if (out.text === undefined && out.media === undefined) out.raw = result;
  return out;
}

// ---------- 输入读取与分发 ----------
function readStdin() {
  return new Promise((resolve) => {
    let data = '';
    process.stdin.setEncoding('utf8');
    process.stdin.on('data', (c) => { data += c; });
    process.stdin.on('end', () => resolve(data));
    setTimeout(() => { if (!data) resolve(''); }, CONFIG.timeout + 5000);
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
  const command = (input.command || 'overview').trim();

  try {
    let data;
    switch (command) {
      case 'overview':
        data = await handleOverview();
        break;
      case 'api_info':
        data = await handleApiInfo(input);
        break;
      case 'list_pages':
        data = { pages: await runSnippet('list_pages', input) };
        break;
      case 'get_selection':
        data = { selection: await runSnippet('get_selection', input) };
        break;
      case 'get_page_tree':
        data = { tree: await runSnippet('get_page_tree', input) };
        break;
      case 'create_rect':
        data = { created: await runSnippet('create_rect', input) };
        break;
      case 'create_text':
        data = { created: await runSnippet('create_text', input) };
        break;
      case 'export':
        data = await handleExport(input);
        break;
      case 'exec':
        data = await handleExec(input);
        break;
      default:
        throw new Error(`未知 command "${command}"。可用: overview | api_info | list_pages | get_selection | get_page_tree | create_rect | create_text | export | exec`);
    }
    process.stdout.write(JSON.stringify({
      status: 'success',
      result: typeof data === 'string' ? data : JSON.stringify(data, null, 2),
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