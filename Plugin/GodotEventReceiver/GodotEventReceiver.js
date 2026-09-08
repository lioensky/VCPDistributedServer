'use strict';

/*
 * GodotEventReceiver - VCP service 插件（二期反向通道）
 * 作为 WebSocket 服务端，接收 Godot 侧 godot_vcp_bridge 主动推送的事件。
 *
 * 方向: Godot (WS client) --> 本插件 (WS server)
 * 与一期 GodotBridge (VCP 请求 -> Godot 响应) 方向相反、通道隔离。
 *
 * 依赖: ws（VCPToolBox 已内置）
 */

const path = require('path');
const fs = require('fs').promises;
const WebSocket = require('ws');

const LOG_DIR_NAME = 'log';
const LOG_FILE_NAME = 'godot_events.txt';

let wss = null;
let logFilePath = null;
let pluginConfig = {};
let broadcastVCPInfoFunction = null; // 由 server.js 注入（同 VCPLog 范式）

function debugLog(...args) {
  if (pluginConfig && pluginConfig.DebugMode) console.log('[GodotEventReceiver]', ...args);
}

async function ensureLogFile(basePath) {
  const dir = path.join(basePath, LOG_DIR_NAME);
  try {
    await fs.mkdir(dir, { recursive: true });
    logFilePath = path.join(dir, LOG_FILE_NAME);
    await fs.access(logFilePath).catch(async () => {
      await fs.writeFile(logFilePath, `Godot event log initialized at ${new Date().toISOString()}\n`, 'utf-8');
    });
  } catch (e) {
    console.error('[GodotEventReceiver] 无法创建日志目录/文件:', e.message);
  }
}

async function writeLog(line) {
  if (!logFilePath) return;
  try {
    await fs.appendFile(logFilePath, `${new Date().toISOString()} - ${line}\n`, 'utf-8');
  } catch (e) {
    console.error('[GodotEventReceiver] 写日志失败:', e.message);
  }
}

// 校验连接令牌：优先 Authorization: Bearer，其次 ?token=
function checkAuth(req) {
  const token = String(pluginConfig.GODOT_EVENT_TOKEN || '').trim();
  if (!token) return true; // 未配置令牌则放行
  const auth = req.headers['authorization'] || '';
  const m = auth.match(/^Bearer\s+(.+)$/i);
  if (m && m[1].trim() === token) return true;
  try {
    const url = new URL(req.url, 'http://localhost');
    if (url.searchParams.get('token') === token) return true;
  } catch (e) { /* ignore */ }
  return false;
}

// 统一事件信封 -> VCP 前端广播 payload
function toVcpInfo(evt) {
  return {
    type: 'godot_event',
    source: 'GodotEventReceiver',
    event_type: evt.event_type || 'unknown',
    project_id: evt.project_id || null,
    session_id: evt.session_id || null,
    timestamp: evt.timestamp || new Date().toISOString(),
    payload: evt.payload !== undefined ? evt.payload : evt,
  };
}

function handleMessage(raw, ws) {
  let evt;
  try {
    evt = JSON.parse(raw.toString());
  } catch (e) {
    debugLog('收到非 JSON 消息，忽略:', raw.toString().slice(0, 120));
    return;
  }

  // 心跳
  if (evt.event_type === 'ping' || evt.type === 'ping') {
    try { ws.send(JSON.stringify({ event_type: 'pong', timestamp: new Date().toISOString() })); } catch (e) { /* ignore */ }
    return;
  }

  writeLog(`[${evt.event_type || 'unknown'}] ${JSON.stringify(evt)}`);
  debugLog('事件:', evt.event_type, '| project:', evt.project_id);

  const shouldBroadcast = pluginConfig.GODOT_EVENT_BROADCAST !== false
    && String(pluginConfig.GODOT_EVENT_BROADCAST) !== 'false';
  if (shouldBroadcast && broadcastVCPInfoFunction) {
    try { broadcastVCPInfoFunction(toVcpInfo(evt)); }
    catch (e) { debugLog('广播失败:', e.message); }
  }
}

function startWebSocketServer() {
  const port = parseInt(pluginConfig.GODOT_EVENT_PORT || '5090', 10);

  wss = new WebSocket.Server({ port }, () => {
    console.log(`[GodotEventReceiver] 监听 Godot 事件于 ws://127.0.0.1:${port}`);
  });

  wss.on('connection', (ws, req) => {
    if (!checkAuth(req)) {
      debugLog('连接令牌校验失败，拒绝');
      try { ws.close(4001, 'unauthorized'); } catch (e) { /* ignore */ }
      return;
    }
    const peer = req.socket.remoteAddress;
    console.log(`[GodotEventReceiver] Godot 客户端已连接: ${peer}`);
    writeLog(`connection opened from ${peer}`);

    ws.on('message', (data) => handleMessage(data, ws));
    ws.on('close', () => {
      debugLog('Godot 客户端断开:', peer);
      writeLog(`connection closed from ${peer}`);
    });
    ws.on('error', (err) => debugLog('连接错误:', err.message));

    // 握手确认
    try { ws.send(JSON.stringify({ event_type: 'welcome', server: 'VCP-GodotEventReceiver', timestamp: new Date().toISOString() })); } catch (e) { /* ignore */ }
  });

  wss.on('error', (err) => {
    console.error('[GodotEventReceiver] WebSocket 服务器错误:', err.message);
  });
}

// ---------- VCP 插件生命周期 ----------
function initialize(config) {
  pluginConfig = config || {};
  const basePath = path.join(pluginConfig.PROJECT_BASE_PATH || __dirname, 'Plugin', 'GodotEventReceiver');
  // 若未提供 PROJECT_BASE_PATH，退回到插件自身目录
  ensureLogFile(pluginConfig.PROJECT_BASE_PATH ? basePath : __dirname);
  startWebSocketServer();
  console.log(`[GodotEventReceiver] 初始化完成。端口: ${pluginConfig.GODOT_EVENT_PORT || 5090}，令牌校验: ${pluginConfig.GODOT_EVENT_TOKEN ? '开启' : '关闭'}`);
}

// server.js 注入中央 WebSocketServer 广播函数（同 VCPLog）
function setBroadcastFunctions(broadcastInfoFunc) {
  broadcastVCPInfoFunction = broadcastInfoFunc;
  debugLog('broadcastVCPInfoFunction 已注入');
}

async function shutdown() {
  debugLog('关闭中...');
  if (wss) {
    for (const client of wss.clients) {
      try { client.close(1001, 'server shutdown'); } catch (e) { /* ignore */ }
    }
    wss.close();
    wss = null;
  }
  await writeLog('GodotEventReceiver shutdown.');
}

module.exports = {
  initialize,
  shutdown,
  setBroadcastFunctions,
};