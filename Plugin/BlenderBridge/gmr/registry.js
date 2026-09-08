'use strict';
/*
 * GMR ex 模块 - 模型注册表
 *
 * 职责：把散落的 checkpoint 收敛成可查询清单，并记录 GMR 推理必需的骨架契约
 * 元数据（关节数、fps、窗口长度、up 轴）。这些不是装饰——缺了它们 Blender 侧
 * 无法正确 retarget，up_axis 弄错会直接得到躺平的角色。
 *
 * registry.json 结构：
 *   { "version": 1, "models": { "<id>": { ...record } } }
 */
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const { CONFIG, ensureDirs } = require('./config');

const REGISTRY_PATH = () => path.join(CONFIG.modelsDir, 'registry.json');

// safetensors / onnx / npz 无 pickle 风险，优先推荐
const SAFE_FORMATS = ['safetensors', 'onnx', 'npz'];
const KNOWN_FORMATS = SAFE_FORMATS.concat(['pt', 'pth', 'ckpt', 'bin']);

// 模型用途分类，对应论文服务端的两个模块
const KINDS = {
  betweener: 'ML-Betweener 类：稀疏关键帧之间生成/补全动作（IBMM / CondMDI / MDM）',
  poser: 'ML-Poser 类：从稀疏关节约束解算全身姿态（神经 IK / ProtoRes）',
  other: '其它辅助模型',
};

function readRegistry() {
  const p = REGISTRY_PATH();
  if (!fs.existsSync(p)) return { version: 1, models: {} };
  try {
    const obj = JSON.parse(fs.readFileSync(p, 'utf8'));
    if (!obj || typeof obj !== 'object') return { version: 1, models: {} };
    if (!obj.models || typeof obj.models !== 'object') obj.models = {};
    return obj;
  } catch (e) {
    throw new Error('registry.json 解析失败（文件可能损坏）: ' + e.message);
  }
}

function writeRegistry(reg) {
  ensureDirs();
  const p = REGISTRY_PATH();
  // 先写临时文件再 rename，避免写入中断损坏注册表
  const tmp = p + '.tmp';
  fs.writeFileSync(tmp, JSON.stringify(reg, null, 2), 'utf8');
  fs.renameSync(tmp, p);
}

function slugify(name) {
  return String(name)
    .trim()
    .toLowerCase()
    .replace(/[^a-z0-9._-]+/g, '-')
    .replace(/^[-]+/, '')
    .replace(/[-]+$/, '')
    .slice(0, 64) || 'model';
}

function isRemoteSource(s) {
  const lower = String(s).trim().toLowerCase();
  return lower.startsWith('http://') || lower.startsWith('https://') || lower.startsWith('ftp://');
}

function sha256File(filePath, maxBytes) {
  // 大 checkpoint 全量哈希很慢。只哈希前 8MB + 文件大小，
  // 目的是完整性/重复性识别，非密码学证明。
  const limit = maxBytes || 8 * 1024 * 1024;
  const h = crypto.createHash('sha256');
  const fd = fs.openSync(filePath, 'r');
  try {
    const buf = Buffer.alloc(Math.min(limit, 1024 * 1024));
    let read = 0;
    while (read < limit) {
      const n = fs.readSync(fd, buf, 0, buf.length, read);
      if (n <= 0) break;
      h.update(buf.slice(0, n));
      read += n;
    }
  } finally {
    fs.closeSync(fd);
  }
  const size = fs.statSync(filePath).size;
  h.update('|size:' + size);
  return h.digest('hex');
}

function detectFormat(filePath) {
  const ext = path.extname(filePath).replace('.', '').toLowerCase();
  return KNOWN_FORMATS.includes(ext) ? ext : (ext || 'unknown');
}

/*
 * 导入模型。
 *   source 必需，本地文件绝对路径（拒绝 URL，理由见下）
 *   name   可选，人类可读名，默认取文件名
 *   kind   可选，betweener | poser | other，默认 betweener
 *   copy   可选，true 复制进仓库，false 原地登记（默认 false，省磁盘）
 *   meta   可选，骨架契约 { joints, fps, window, up_axis, feature_dim, notes }
 */
function importModel(opts) {
  ensureDirs();
  const source = String(opts.source || '').trim();
  if (!source) throw new Error('import_model 需要参数 source（模型文件的绝对路径）。');
  if (isRemoteSource(source)) {
    throw new Error('检测到远程 URL。本命令只接受本地路径：请先手动下载并核验来源，再用本地路径导入。理由——PyTorch checkpoint 走 pickle 反序列化，加载不受信任的文件等同于任意代码执行。');
  }
  const abs = path.resolve(source);
  if (!fs.existsSync(abs)) throw new Error('模型文件不存在: ' + abs);
  const st = fs.statSync(abs);
  if (!st.isFile()) throw new Error('source 必须是文件而非目录: ' + abs);

  const format = detectFormat(abs);
  if (CONFIG.requireSafeFormat && !SAFE_FORMATS.includes(format)) {
    throw new Error('GMR_REQUIRE_SAFE_FORMAT 已开启，只允许 ' + SAFE_FORMATS.join('/') + ' 格式，当前为 ' + format + '。');
  }

  const kind = String(opts.kind || 'betweener').trim();
  if (!Object.prototype.hasOwnProperty.call(KINDS, kind)) {
    throw new Error('未知 kind "' + kind + '"。可用: ' + Object.keys(KINDS).join(' | '));
  }

  const name = String(opts.name || path.basename(abs, path.extname(abs))).trim();
  const reg = readRegistry();
  const base = slugify(name);
  let id = base;
  let suffix = 1;
  while (reg.models[id]) { id = base + '-' + (++suffix); }

  let storedPath = abs;
  let copied = false;
  if (opts.copy === true || String(opts.copy) === 'true') {
    const destDir = path.join(CONFIG.modelsDir, id);
    fs.mkdirSync(destDir, { recursive: true });
    storedPath = path.join(destDir, path.basename(abs));
    fs.copyFileSync(abs, storedPath);
    copied = true;
  }

  const meta = (opts.meta && typeof opts.meta === 'object') ? opts.meta : {};
  const record = {
    id,
    name,
    kind,
    format,
    path: storedPath,
    copied,
    sizeBytes: st.size,
    fingerprint: sha256File(abs),
    importedAt: new Date().toISOString(),
    // 骨架契约。留空不阻止导入，但 Blender 侧 retarget 会缺依据。
    joints: meta.joints !== undefined ? meta.joints : null,
    fps: meta.fps !== undefined ? meta.fps : null,
    window: meta.window !== undefined ? meta.window : null,
    upAxis: meta.up_axis || meta.upAxis || null,
    featureDim: meta.feature_dim !== undefined ? meta.feature_dim : (meta.featureDim !== undefined ? meta.featureDim : null),
    notes: meta.notes || '',
  };

  reg.models[id] = record;
  writeRegistry(reg);

  const warnings = [];
  if (!SAFE_FORMATS.includes(format)) {
    warnings.push('格式 ' + format + ' 依赖 pickle 反序列化。sidecar 加载时会强制 weights_only=True，但仍请确认文件来源可信。');
  }
  if (record.joints === null || record.upAxis === null) {
    warnings.push('缺少骨架契约（joints / up_axis）。建议用 update_model 补齐——up_axis 弄错会导致角色躺平。');
  }
  return { imported: record, warnings };
}

function listModels(filterKind) {
  const reg = readRegistry();
  let arr = Object.values(reg.models);
  if (filterKind) arr = arr.filter((m) => m.kind === filterKind);
  arr.sort((a, b) => String(b.importedAt).localeCompare(String(a.importedAt)));
  return {
    count: arr.length,
    modelsDir: CONFIG.modelsDir,
    models: arr.map((m) => ({
      id: m.id,
      name: m.name,
      kind: m.kind,
      format: m.format,
      sizeMB: +(m.sizeBytes / 1048576).toFixed(2),
      joints: m.joints,
      fps: m.fps,
      upAxis: m.upAxis,
      exists: fs.existsSync(m.path),
      path: m.path,
    })),
  };
}

function getModel(id) {
  const reg = readRegistry();
  const m = reg.models[String(id || '').trim()];
  if (!m) throw new Error('未找到模型 "' + id + '"。用 list_models 查看已注册模型。');
  return m;
}

function updateModel(id, meta) {
  const reg = readRegistry();
  const key = String(id || '').trim();
  const m = reg.models[key];
  if (!m) throw new Error('未找到模型 "' + key + '"。');
  const patch = Object.assign({}, meta || {});
  if (patch.up_axis !== undefined) patch.upAxis = patch.up_axis;
  if (patch.feature_dim !== undefined) patch.featureDim = patch.feature_dim;
  const allowed = ['joints', 'fps', 'window', 'upAxis', 'featureDim', 'notes', 'name', 'kind'];
  const changed = {};
  for (const k of allowed) {
    if (patch[k] !== undefined) {
      if (k === 'kind' && !Object.prototype.hasOwnProperty.call(KINDS, patch[k])) {
        throw new Error('未知 kind "' + patch[k] + '"。');
      }
      m[k] = patch[k];
      changed[k] = patch[k];
    }
  }
  if (!Object.keys(changed).length) {
    throw new Error('update_model 未提供可更新字段。可更新: ' + allowed.join(', '));
  }
  writeRegistry(reg);
  return { id: key, changed, model: m };
}

function removeModel(id, deleteFile) {
  const reg = readRegistry();
  const key = String(id || '').trim();
  const m = reg.models[key];
  if (!m) throw new Error('未找到模型 "' + key + '"。');
  let fileDeleted = false;
  const wantDelete = (deleteFile === true || String(deleteFile) === 'true');
  if (wantDelete) {
    if (!m.copied) {
      throw new Error('模型 "' + key + '" 是原地登记（copied=false），文件位于你自有目录 ' + m.path + '。为避免误删原始资产，本命令拒绝删除；请手动处理，或不传 delete_file 仅注销登记。');
    }
    try {
      fs.rmSync(path.dirname(m.path), { recursive: true, force: true });
      fileDeleted = true;
    } catch (e) {
      throw new Error('注册项未删除，因为文件删除失败: ' + e.message);
    }
  }
  delete reg.models[key];
  writeRegistry(reg);
  return { removed: key, fileDeleted, path: m.path };
}

module.exports = {
  KINDS, SAFE_FORMATS, KNOWN_FORMATS,
  readRegistry, importModel, listModels, getModel, updateModel, removeModel,
};