'use strict';
/*
 * GMR ex 模块 - 统一配置解析
 *
 * 设计原则：
 *   1. 所有路径默认落在 BlenderBridge 插件目录内，便于整体迁移/删除。
 *   2. 只依赖 Node 内置模块，与 BlenderBridge.js 主体保持同样的零依赖约束。
 *   3. 每次 VCP 调用都是新进程，任何状态必须落盘，不能驻留内存。
 */
const path = require('path');
const fs = require('fs');

// gmr/ 的父目录，即 BlenderBridge 插件根
const PLUGIN_ROOT = path.resolve(__dirname, '..');

function envStr(key, fallback) {
  const v = process.env[key];
  return (v === undefined || v === null || String(v).trim() === '') ? fallback : String(v).trim();
}

function envInt(key, fallback) {
  const n = parseInt(process.env[key], 10);
  return Number.isFinite(n) ? n : fallback;
}

function envBool(key, fallback) {
  const v = process.env[key];
  if (v === undefined || v === null || String(v).trim() === '') return fallback;
  return ['true', '1', 'yes', 'on'].includes(String(v).trim().toLowerCase());
}

const GMR_ROOT = path.resolve(envStr('GMR_ROOT', path.join(PLUGIN_ROOT, 'gmr_data')));

const CONFIG = {
  pluginRoot: PLUGIN_ROOT,
  root: GMR_ROOT,

  // 模型仓库：存放 checkpoint 与 registry.json
  modelsDir: path.resolve(envStr('GMR_MODELS_DIR', path.join(GMR_ROOT, 'models'))),
  // 任务目录：存放 <jobId>.json 状态与 <jobId>.log 日志
  jobsDir: path.resolve(envStr('GMR_JOBS_DIR', path.join(GMR_ROOT, 'jobs'))),
  // 数据集根目录
  datasetsDir: path.resolve(envStr('GMR_DATASETS_DIR', path.join(GMR_ROOT, 'datasets'))),

  // Python 解释器。强烈建议指向独立 venv，避免污染系统 Python。
  python: envStr('GMR_PYTHON', 'python3'),
  pythonDir: path.join(__dirname, 'python'),

  // 推理 sidecar。与 blender-mcp 的 6090 并列而非串联。
  sidecarUrl: envStr('GMR_SIDECAR_URL', 'http://127.0.0.1:6091/'),
  sidecarHost: envStr('GMR_SIDECAR_HOST', '127.0.0.1'),
  sidecarPort: envInt('GMR_SIDECAR_PORT', 6091),

  // 安全开关：默认禁止从 URL 下载模型（pickle 反序列化存在 RCE 风险）
  allowDownload: envBool('GMR_ALLOW_DOWNLOAD', false),
  // 导入模型时是否强制要求 safetensors 等安全格式
  requireSafeFormat: envBool('GMR_REQUIRE_SAFE_FORMAT', false),

  // 日志尾部返回的最大字节数，防止污染上下文
  logTailBytes: envInt('GMR_LOG_TAIL_BYTES', 4096),
  // sidecar 健康检查超时
  healthTimeoutMs: envInt('GMR_HEALTH_TIMEOUT_MS', 3000),
  // 单次推理请求超时
  inferTimeoutMs: envInt('GMR_INFER_TIMEOUT_MS', 30000),

  debug: envBool('DebugMode', false),
};

// 惰性建目录，避免只读操作也产生副作用
function ensureDirs() {
  for (const d of [CONFIG.root, CONFIG.modelsDir, CONFIG.jobsDir, CONFIG.datasetsDir]) {
    try {
      fs.mkdirSync(d, { recursive: true });
    } catch (e) {
      throw new Error('无法创建 GMR 目录 ' + d + ': ' + e.message);
    }
  }
}

module.exports = { CONFIG, ensureDirs };