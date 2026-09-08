'use strict';
/*
 * GMR ex 模块 - 统一入口与命令分发
 *
 * 这是 BlenderBridge.js 主体唯一需要 require 的文件。主体侧只加一个
 * try-require 分支：模块存在则挂载 GMR 命令，不存在则原有 6 个子命令照常工作。
 * 这样 ex 模块可以整目录删除而不影响桥接本体。
 *
 * 命令分三组：
 *   模型仓库  import_model / list_models / update_model / remove_model
 *   训练任务  train / list_jobs / job_status / cancel_job
 *   推理服务  sidecar_start / sidecar_stop / sidecar_status / sidecar_load_model / infer
 *   总览      gmr_status / gmr_help
 */
const fs = require('fs');
const path = require('path');
const { CONFIG, ensureDirs } = require('./config');
const registry = require('./registry');
const jobs = require('./jobs');
const sidecar = require('./sidecar');

const NL = String.fromCharCode(10);
const VERSION = '0.1.0';

// 命令名 -> 处理函数。主体通过 has(command) 判断是否归本模块处理。
const HANDLERS = {
  // ---- 总览 ----
  gmr_status: async function () {
    ensureDirs();
    const models = registry.listModels();
    const jobList = jobs.listJobs();
    const sc = await sidecar.health().catch(function (e) { return { reachable: false, error: e.message }; });
    const running = jobList.jobs.filter(function (j) { return j.status === 'running'; }).length;
    const pyTrain = path.join(CONFIG.pythonDir, 'train.py');
    const pySide = path.join(CONFIG.pythonDir, 'sidecar.py');
    return {
      gmrVersion: VERSION,
      dataRoot: CONFIG.root,
      python: CONFIG.python,
      models: { count: models.count, byKind: countBy(models.models, 'kind') },
      jobs: { total: jobList.count, running: running },
      sidecar: { endpoint: CONFIG.sidecarUrl, reachable: !!sc.reachable, processAlive: !!sc.processAlive, loaded: sc.sidecar ? sc.sidecar.loaded : undefined },
      scripts: { train: fs.existsSync(pyTrain), sidecar: fs.existsSync(pySide) },
      note: 'GMR 是 BlenderBridge 的可选扩展模块（ex）。删除 gmr/ 目录不影响桥接本体的 6 个子命令。',
    };
  },

  gmr_help: async function () {
    return {
      gmrVersion: VERSION,
      架构: {
        慢回路: 'VCP -> BlenderBridge -> blender-mcp:6090 -> Blender Add-on（秒级，Agent 语义编排）',
        快回路: 'Blender GMR Add-on -> sidecar:6091（~100ms 拖拽推理，不经过 VCP）',
        管理回路: 'VCP -> BlenderBridge -> gmr ex -> sidecar:6091（起停、装载、试跑）',
        要点: '快回路必须绕开 blender-mcp。上游单并发(BLENDER_BUSY)+双跳延迟，交互推理塞进去必然请求堆积锁死。',
      },
      模型仓库: {
        import_model: '登记本地 checkpoint。参数 source(必需,绝对路径) name kind(betweener|poser|other) copy meta。拒绝 URL——pickle 反序列化等同任意代码执行。',
        list_models: '列出已注册模型。参数 kind(可选,过滤)。',
        update_model: '补齐骨架契约元数据。参数 model_id(必需) 及 joints/fps/window/up_axis/feature_dim/notes/name/kind。',
        remove_model: '注销登记。参数 model_id(必需) delete_file(可选)。原地登记的模型拒绝删文件，防误删原始资产。',
      },
      训练任务: {
        train: '启动训练。参数 dataset(必需) name kind script epochs batch_size lr window device seed resume_from extra_args。detached 启动后立即返回，不阻塞 70s 插件超时。',
        list_jobs: '列出任务。参数 status(可选)。',
        job_status: '查询任务与日志尾部。参数 job_id(必需) tail_bytes(可选)。',
        cancel_job: '发送 SIGTERM 终止。参数 job_id(必需)。已保存的 checkpoint 不删。',
      },
      推理服务: {
        sidecar_start: '启动推理进程。参数 model_id(可选,预载) device script。',
        sidecar_stop: '终止推理进程。无参数。',
        sidecar_status: '健康检查 + 已载模型 + 日志尾部。无参数。',
        sidecar_load_model: '热装载模型。参数 model_id(必需) device(可选)。',
        infer: '单次生成试跑（验证链路用，非交互回路）。参数 constraints(必需) window seed steps model_id base_motion。',
      },
      约束契约: {
        说明: '约束的单一真相源是 .blend 文件里的自定义属性，不在内存也不在 sidecar。',
        Empty上: 'gmr_type(sparse|fullbody) gmr_joint gmr_frame gmr_seed',
        Scene上: 'gmr_window(时间评估边界) gmr_base_action(编辑模式的 inpainting 底座)',
        好处: '随 .blend 存盘、seed 落盘即可复现变体、Agent 能读到完整创作意图而非仅结果动作。',
      },
      开源替代: {
        betweener: 'IBMM 未开源。论文原文明确写兼容其它生成引擎并引用 Cohan et al. 2024，即 CondMDI（开源）。',
        poser: 'ProtoRes 权重未公开。第一版建议直接用 Blender 原生 IK 顶替，省掉一整个模型。',
      },
      注意事项: [
        'bpy 非线程安全：推理结果必须经 bpy.app.timers.register() marshal 回主线程才能写 bpy.data，违反即随机 segfault。',
        'GMR_PYTHON 应指向装有 PyTorch 的独立 venv，勿用系统 Python。',
        'train.py 与 sidecar.py 是骨架，需按所选模型补全实际逻辑。',
      ],
    };
  },

  // ---- 模型仓库 ----
  import_model: async function (input) {
    return registry.importModel({
      source: input.source,
      name: input.name,
      kind: input.kind,
      copy: input.copy,
      meta: parseMaybeJson(input.meta, 'meta'),
    });
  },

  list_models: async function (input) {
    return registry.listModels(input.kind ? String(input.kind).trim() : null);
  },

  update_model: async function (input) {
    const id = input.model_id || input.id;
    const meta = parseMaybeJson(input.meta, 'meta') || {};
    // 也允许把字段直接平铺在参数里，省一层嵌套
    for (const k of ['joints', 'fps', 'window', 'up_axis', 'upAxis', 'feature_dim', 'featureDim', 'notes', 'name', 'kind']) {
      if (input[k] !== undefined && meta[k] === undefined) meta[k] = input[k];
    }
    if (meta.joints !== undefined) meta.joints = toNum(meta.joints);
    if (meta.fps !== undefined) meta.fps = toNum(meta.fps);
    if (meta.feature_dim !== undefined) meta.feature_dim = toNum(meta.feature_dim);
    if (meta.window !== undefined) meta.window = toNum(meta.window);
    return registry.updateModel(id, meta);
  },

  remove_model: async function (input) {
    return registry.removeModel(input.model_id || input.id, input.delete_file);
  },

  // ---- 训练任务 ----
  train: async function (input) {
    return jobs.startTraining(input);
  },

  list_jobs: async function (input) {
    return jobs.listJobs(input.status ? String(input.status).trim() : null);
  },

  job_status: async function (input) {
    return jobs.jobStatus(input.job_id || input.id, input.tail_bytes);
  },

  cancel_job: async function (input) {
    return jobs.cancelJob(input.job_id || input.id);
  },

  // ---- 推理服务 ----
  sidecar_start: async function (input) {
    return sidecar.start(input);
  },

  sidecar_stop: async function () {
    return sidecar.stop();
  },

  sidecar_status: async function () {
    return sidecar.health();
  },

  sidecar_load_model: async function (input) {
    return sidecar.loadModel(input);
  },

  infer: async function (input) {
    return sidecar.infer(input);
  },
};

function countBy(arr, key) {
  const out = {};
  for (const it of arr) {
    const k = it[key] || 'unknown';
    out[k] = (out[k] || 0) + 1;
  }
  return out;
}

function toNum(v) {
  const n = Number(v);
  return Number.isFinite(n) ? n : v;
}

function parseMaybeJson(v, label) {
  if (v === undefined || v === null) return undefined;
  if (typeof v === 'object') return v;
  const s = String(v).trim();
  if (!s) return undefined;
  try {
    return JSON.parse(s);
  } catch (e) {
    throw new Error('参数 ' + label + ' 不是合法 JSON: ' + e.message);
  }
}

function has(command) {
  return Object.prototype.hasOwnProperty.call(HANDLERS, String(command || '').trim());
}

async function handle(command, input) {
  const key = String(command || '').trim();
  if (!has(key)) {
    throw new Error('GMR 未知子命令 "' + key + '"。可用: ' + Object.keys(HANDLERS).join(' | ')
      + NL + '用 gmr_help 查看完整说明。');
  }
  return HANDLERS[key](input || {});
}

module.exports = { VERSION, has: has, handle: handle, commands: Object.keys(HANDLERS) };