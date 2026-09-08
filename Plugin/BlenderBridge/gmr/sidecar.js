'use strict';
/*
 * GMR ex 模块 - 推理 sidecar 客户端与生命周期管理
 *
 * 架构定位（重要）：sidecar 与 blender-mcp 是【并列】关系，不是串联。
 *
 *   慢回路(秒级):   VCP -> BlenderBridge -> blender-mcp:6090 -> Blender Add-on
 *   快回路(~100ms): Blender GMR Add-on -> sidecar:6091        [不经过 VCP]
 *   管理回路:       VCP -> BlenderBridge -> gmr ex -> sidecar:6091
 *
 * 交互期的拖拽推理必须由 Blender Add-on 直连 6091。理由已写在 README：
 * blender-mcp 上游单并发(BLENDER_BUSY) + 双跳延迟，塞进去必然请求堆积锁死。
 * 本模块只负责“管理”——起停、健康检查、装载模型、以及慢回路的单次试跑。
 */
const http = require('http');
const fs = require('fs');
const path = require('path');
const { spawn } = require('child_process');
const { CONFIG, ensureDirs } = require('./config');
const registry = require('./registry');

const NL = String.fromCharCode(10);
const PID_FILE = () => path.join(CONFIG.root, 'sidecar.pid');
const SIDECAR_LOG = () => path.join(CONFIG.root, 'sidecar.log');

function httpJson(method, urlPath, body, timeoutMs) {
  return new Promise((resolve, reject) => {
    const payload = body === undefined ? null : JSON.stringify(body);
    const headers = { 'Accept': 'application/json' };
    if (payload) {
      headers['Content-Type'] = 'application/json';
      headers['Content-Length'] = Buffer.byteLength(payload);
    }
    const req = http.request({
      host: CONFIG.sidecarHost,
      port: CONFIG.sidecarPort,
      path: urlPath,
      method: method,
      headers: headers,
      timeout: timeoutMs || CONFIG.inferTimeoutMs,
    }, (res) => {
      let raw = '';
      res.setEncoding('utf8');
      res.on('data', (c) => { raw += c; });
      res.on('end', () => {
        let parsed = null;
        try {
          parsed = raw.trim() ? JSON.parse(raw) : {};
        } catch (e) {
          parsed = { raw: raw.slice(0, 500) };
        }
        if (res.statusCode >= 400) {
          const msg = (parsed && parsed.error) ? parsed.error : raw.slice(0, 300);
          return reject(new Error('sidecar HTTP ' + res.statusCode + ': ' + msg));
        }
        resolve(parsed);
      });
    });
    req.on('timeout', () => {
      req.destroy(new Error('sidecar 请求超时 (' + (timeoutMs || CONFIG.inferTimeoutMs) + 'ms)'));
    });
    req.on('error', (err) => {
      if (err.code === 'ECONNREFUSED') {
        return reject(new Error('无法连接推理 sidecar (' + CONFIG.sidecarUrl + ')。'
          + NL + '请先用 sidecar_start 启动，或确认 GMR_SIDECAR_PORT 配置一致。'
          + NL + '注意 sidecar 需要装有 PyTorch 的独立 Python 环境（用 GMR_PYTHON 指定）。'));
      }
      reject(err);
    });
    if (payload) req.write(payload);
    req.end();
  });
}

function isAlive(pid) {
  if (!pid) return false;
  try {
    process.kill(pid, 0);
    return true;
  } catch (e) {
    return e.code === 'EPERM';
  }
}

function readPidFile() {
  const p = PID_FILE();
  if (!fs.existsSync(p)) return null;
  const n = parseInt(fs.readFileSync(p, 'utf8').trim(), 10);
  return Number.isFinite(n) ? n : null;
}

function tail(p, maxBytes) {
  if (!fs.existsSync(p)) return '';
  const size = fs.statSync(p).size;
  const limit = maxBytes || CONFIG.logTailBytes;
  const start = Math.max(0, size - limit);
  const fd = fs.openSync(p, 'r');
  try {
    const len = size - start;
    if (len <= 0) return '';
    const buf = Buffer.alloc(len);
    fs.readSync(fd, buf, 0, len, start);
    return buf.toString('utf8');
  } finally {
    fs.closeSync(fd);
  }
}

async function health() {
  ensureDirs();
  const pid = readPidFile();
  const out = {
    endpoint: CONFIG.sidecarUrl,
    pidFile: PID_FILE(),
    recordedPid: pid,
    processAlive: isAlive(pid),
    logFile: SIDECAR_LOG(),
  };
  try {
    const res = await httpJson('GET', '/health', undefined, CONFIG.healthTimeoutMs);
    out.reachable = true;
    out.sidecar = res;
  } catch (e) {
    out.reachable = false;
    out.error = e.message;
    if (out.processAlive) {
      out.hint = '进程存活但 HTTP 不通：可能仍在加载模型（大 checkpoint 需要时间），或端口不一致。查看日志尾部。';
    }
    out.logTail = tail(SIDECAR_LOG(), 1500);
  }
  return out;
}

async function start(input) {
  ensureDirs();
  const existing = readPidFile();
  if (isAlive(existing)) {
    return {
      started: false,
      pid: existing,
      note: 'sidecar 已在运行（pid ' + existing + '）。如需重启请先 sidecar_stop。',
    };
  }

  const script = path.resolve(String((input && input.script) || path.join(CONFIG.pythonDir, 'sidecar.py')));
  if (!fs.existsSync(script)) {
    throw new Error('sidecar 脚本不存在: ' + script);
  }

  const args = [script, '--host', CONFIG.sidecarHost, '--port', String(CONFIG.sidecarPort)];

  // 可选：启动时预载某个已注册模型
  if (input && input.model_id) {
    const m = registry.getModel(input.model_id);
    args.push('--model', m.path, '--model-kind', m.kind, '--model-id', m.id);
    if (m.joints) args.push('--joints', String(m.joints));
    if (m.fps) args.push('--fps', String(m.fps));
    if (m.upAxis) args.push('--up-axis', String(m.upAxis));
  }
  if (input && input.device) args.push('--device', String(input.device));

  const logFd = fs.openSync(SIDECAR_LOG(), 'a');
  let child;
  try {
    child = spawn(CONFIG.python, args, {
      cwd: CONFIG.pythonDir,
      detached: true,
      stdio: ['ignore', logFd, logFd],
      env: Object.assign({}, process.env, { PYTHONUNBUFFERED: '1' }),
    });
  } catch (e) {
    fs.closeSync(logFd);
    throw new Error('无法启动 sidecar（检查 GMR_PYTHON="' + CONFIG.python + '" 是否为装有 PyTorch 的解释器）: ' + e.message);
  }
  let spawnError = null;
  child.on('error', function (err) { spawnError = err.message; });
  const pid = child.pid;
  child.unref();
  fs.closeSync(logFd);
  fs.writeFileSync(PID_FILE(), String(pid), 'utf8');

  if (spawnError) {
    throw new Error('spawn sidecar 失败: ' + spawnError);
  }

  return {
    started: true,
    pid: pid,
    endpoint: CONFIG.sidecarUrl,
    logFile: SIDECAR_LOG(),
    note: '已在独立进程启动，插件不等待其就绪。模型加载可能需数十秒，请稍后用 sidecar_status 确认 reachable=true。',
  };
}

function stop() {
  const pid = readPidFile();
  if (!pid) return { stopped: false, note: '无 pid 记录，sidecar 可能未通过本插件启动。' };
  if (!isAlive(pid)) {
    try { fs.unlinkSync(PID_FILE()); } catch (e) { /* 忽略 */ }
    return { stopped: false, pid: pid, note: '进程已不存在，已清理 pid 文件。' };
  }
  try {
    process.kill(pid, 'SIGTERM');
  } catch (e) {
    throw new Error('发送 SIGTERM 失败: ' + e.message);
  }
  try { fs.unlinkSync(PID_FILE()); } catch (e) { /* 忽略 */ }
  return { stopped: true, pid: pid, note: '已发送 SIGTERM。若无响应需手动 kill -9 ' + pid + '。' };
}

async function loadModel(input) {
  const id = String((input && input.model_id) || '').trim();
  if (!id) throw new Error('sidecar_load_model 需要参数 model_id。用 list_models 查看。');
  const m = registry.getModel(id);
  if (!fs.existsSync(m.path)) {
    throw new Error('模型文件缺失: ' + m.path + '（注册项仍在，但文件已被移动或删除）');
  }
  const res = await httpJson('POST', '/load_model', {
    model_id: m.id,
    path: m.path,
    kind: m.kind,
    format: m.format,
    joints: m.joints,
    fps: m.fps,
    window: m.window,
    up_axis: m.upAxis,
    feature_dim: m.featureDim,
    device: (input && input.device) || undefined,
  }, 120000);
  return { loaded: m.id, kind: m.kind, sidecar: res };
}

/*
 * 慢回路的单次生成试跑。用途是验证链路与调参，不是交互回路。
 * 真正的拖拽实时生成由 Blender GMR Add-on 直连 6091，不经过这里。
 */
async function infer(input) {
  const body = {};
  if (input.constraints !== undefined) {
    body.constraints = typeof input.constraints === 'string' ? JSON.parse(input.constraints) : input.constraints;
  }
  if (input.window !== undefined) {
    body.window = typeof input.window === 'string' ? JSON.parse(input.window) : input.window;
  }
  if (input.seed !== undefined) body.seed = parseInt(input.seed, 10);
  if (input.steps !== undefined) body.steps = parseInt(input.steps, 10);
  if (input.base_motion !== undefined) body.base_motion = input.base_motion;
  if (input.model_id !== undefined) body.model_id = String(input.model_id);

  if (!body.constraints) {
    throw new Error('infer 需要参数 constraints。格式示例：'
      + NL + '[{"type":"sparse","joint":"foot_L","frame":30,"loc":[0.4,0,0.05]},'
      + NL + ' {"type":"fullbody","frame":0,"pose":[...]}]'
      + NL + '这与 Blender 侧挂在 Empty 上的 gmr_* 自定义属性是同一套契约。');
  }

  const t0 = Date.now();
  const res = await httpJson('POST', '/infer', body, CONFIG.inferTimeoutMs);
  const ms = Date.now() - t0;

  // 动作数据可能很大，不能整份塞进上下文
  const out = {
    latencyMs: ms,
    modelId: res.model_id,
    frames: res.frames,
    joints: res.joints,
    seed: res.seed,
  };
  if (res.output_file) out.outputFile = res.output_file;
  if (res.motion && Array.isArray(res.motion)) {
    out.motionPreview = {
      totalFrames: res.motion.length,
      firstFrame: res.motion[0],
      note: '完整动作数据已省略以免污染上下文。请让 sidecar 写文件并用 output_file 取回。',
    };
  }
  if (ms > 300) {
    out.perfWarning = '单次推理 ' + ms + 'ms。交互式拖拽需 ~100-150ms，超出会失去 rig 手感。'
      + '优化方向：减少采样步数（DDIM/LCM）、缩短窗口、或改用蒸馏模型。';
  }
  return out;
}

module.exports = { health: health, start: start, stop: stop, loadModel: loadModel, infer: infer, tail: tail };