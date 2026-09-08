'use strict';
/*
 * GMR ex 模块 - 训练任务管理
 *
 * 核心约束：VCP 插件是 synchronous 类型，超时 70s；而训练是小时级任务。
 * 因此训练绝不能在插件进程内同步等待。做法：
 *   1. detached spawn 一个独立 Python 进程，stdio 重定向到日志文件；
 *   2. 立即 unref，让 VCP 插件进程能正常退出而训练继续；
 *   3. 全部状态落盘到 jobs/<id>.json，后续用 job_status 轮询。
 *
 * 因为父进程会先退出，我们拿不到子进程的 exit code。故约定 train.py 结束时
 * 必须写 <id>.done 文件（内含 exit code 与产物路径），这是状态机的唯一真相。
 */
const fs = require('fs');
const path = require('path');
const { spawn } = require('child_process');
const { CONFIG, ensureDirs } = require('./config');
const registry = require('./registry');

const NL = String.fromCharCode(10);

function jobPath(id) { return path.join(CONFIG.jobsDir, id + '.json'); }
function logPath(id) { return path.join(CONFIG.jobsDir, id + '.log'); }
function donePath(id) { return path.join(CONFIG.jobsDir, id + '.done'); }

function newJobId() {
  const d = new Date();
  const pad = (n) => String(n).padStart(2, '0');
  const stamp = d.getFullYear() + pad(d.getMonth() + 1) + pad(d.getDate())
    + '-' + pad(d.getHours()) + pad(d.getMinutes()) + pad(d.getSeconds());
  return 'job-' + stamp + '-' + Math.random().toString(36).slice(2, 6);
}

function readJob(id) {
  const p = jobPath(id);
  if (!fs.existsSync(p)) throw new Error('未找到任务 "' + id + '"。用 list_jobs 查看。');
  try {
    return JSON.parse(fs.readFileSync(p, 'utf8'));
  } catch (e) {
    throw new Error('任务状态文件损坏 ' + p + ': ' + e.message);
  }
}

function writeJob(job) {
  ensureDirs();
  const p = jobPath(job.id);
  const tmp = p + '.tmp';
  fs.writeFileSync(tmp, JSON.stringify(job, null, 2), 'utf8');
  fs.renameSync(tmp, p);
  return job;
}

// pid 是否仍存活。signal 0 只做权限与存在性检查，不实际发信号。
function isAlive(pid) {
  if (!pid) return false;
  try {
    process.kill(pid, 0);
    return true;
  } catch (e) {
    return e.code === 'EPERM';
  }
}

function tailFile(p, maxBytes) {
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
    const text = buf.toString('utf8');
    return start > 0 ? '...(前 ' + start + ' 字节已省略)' + NL + text : text;
  } finally {
    fs.closeSync(fd);
  }
}

/*
 * 状态收敛：把落盘状态与真实进程状态对齐。
 * 优先级 —— done 文件 > pid 存活性。
 * 这是必要的，因为 running 只是上次写入时的快照，进程可能早已结束。
 */
function reconcile(job) {
  if (['succeeded', 'failed', 'cancelled'].includes(job.status)) return job;

  const dp = donePath(job.id);
  if (fs.existsSync(dp)) {
    let done = {};
    try {
      done = JSON.parse(fs.readFileSync(dp, 'utf8'));
    } catch (e) {
      done = { exit_code: -1, error: 'done 文件解析失败: ' + e.message };
    }
    job.exitCode = done.exit_code !== undefined ? done.exit_code : -1;
    job.status = job.exitCode === 0 ? 'succeeded' : 'failed';
    job.finishedAt = done.finished_at || new Date().toISOString();
    if (done.error) job.error = done.error;
    if (done.metrics) job.metrics = done.metrics;

    // 训练成功且产出 checkpoint，自动登记进模型注册表
    if (job.status === 'succeeded' && done.checkpoint && !job.registeredModelId) {
      try {
        if (fs.existsSync(done.checkpoint)) {
          const res = registry.importModel({
            source: done.checkpoint,
            name: job.name || job.id,
            kind: job.kind || 'betweener',
            copy: false,
            meta: done.meta || {},
          });
          job.registeredModelId = res.imported.id;
        } else {
          job.warning = 'done 文件声明的 checkpoint 不存在: ' + done.checkpoint;
        }
      } catch (e) {
        job.warning = '自动登记模型失败（训练本身已成功）: ' + e.message;
      }
    }
    return writeJob(job);
  }

  if (job.pid && !isAlive(job.pid)) {
    // 进程没了却没留 done 文件：被 kill -9、OOM、或脚本崩在写 done 之前
    job.status = 'failed';
    job.error = '进程已消失但未写 done 文件。常见原因：被 SIGKILL、OOM，或脚本在收尾前崩溃。请查看日志尾部。';
    job.finishedAt = new Date().toISOString();
    return writeJob(job);
  }

  return job;
}

/*
 * 启动训练任务。
 *   dataset  必需，数据集路径（目录或文件）
 *   name     可选，任务/模型名
 *   kind     可选，betweener | poser
 *   script   可选，训练脚本路径，默认 gmr/python/train.py
 *   epochs / batch_size / lr / window / device / seed / resume_from 透传
 *   extra_args 可选，字符串数组或空格分隔字符串
 */
function startTraining(input) {
  ensureDirs();

  const dataset = String(input.dataset || '').trim();
  if (!dataset) throw new Error('train 需要参数 dataset（数据集目录或文件的路径）。');
  const datasetAbs = path.resolve(dataset);
  if (!fs.existsSync(datasetAbs)) {
    throw new Error('数据集不存在: ' + datasetAbs + NL + '提示：默认数据集根目录为 ' + CONFIG.datasetsDir);
  }

  const script = path.resolve(String(input.script || path.join(CONFIG.pythonDir, 'train.py')));
  if (!fs.existsSync(script)) {
    throw new Error('训练脚本不存在: ' + script + NL + '这是骨架脚本，需按所选模型（CondMDI / MDM 等）补全实际训练逻辑。');
  }

  const kind = String(input.kind || 'betweener').trim();
  if (!Object.prototype.hasOwnProperty.call(registry.KINDS, kind)) {
    throw new Error('未知 kind "' + kind + '"。可用: ' + Object.keys(registry.KINDS).join(' | '));
  }

  const id = newJobId();
  const name = String(input.name || ('gmr-' + kind + '-' + id.slice(4, 17))).trim();
  const outDir = path.join(CONFIG.modelsDir, id);
  fs.mkdirSync(outDir, { recursive: true });

  // 全部走数组参数，不用 shell:true，避免命令注入
  const args = [
    script,
    '--dataset', datasetAbs,
    '--out-dir', outDir,
    '--job-id', id,
    '--done-file', donePath(id),
    '--kind', kind,
  ];

  const passthrough = [
    ['epochs', '--epochs'],
    ['batch_size', '--batch-size'],
    ['lr', '--lr'],
    ['window', '--window'],
    ['device', '--device'],
    ['resume_from', '--resume-from'],
    ['seed', '--seed'],
  ];
  for (const pair of passthrough) {
    const key = pair[0];
    const flag = pair[1];
    if (input[key] !== undefined && String(input[key]).trim() !== '') {
      args.push(flag, String(input[key]).trim());
    }
  }

  if (Array.isArray(input.extra_args)) {
    for (const a of input.extra_args) args.push(String(a));
  } else if (typeof input.extra_args === 'string' && input.extra_args.trim()) {
    // 按空格切分。含空格的复杂参数请用数组形式传入。
    const parts = input.extra_args.trim().split(' ').filter(function (s) { return s.length > 0; });
    for (const a of parts) args.push(a);
  }

  const lp = logPath(id);
  const logFd = fs.openSync(lp, 'a');
  let child;
  try {
    child = spawn(CONFIG.python, args, {
      cwd: CONFIG.pythonDir,
      detached: true,
      stdio: ['ignore', logFd, logFd],
      env: Object.assign({}, process.env, {
        PYTHONUNBUFFERED: '1',
        GMR_JOB_ID: id,
        GMR_MODELS_DIR: CONFIG.modelsDir,
      }),
    });
  } catch (e) {
    fs.closeSync(logFd);
    throw new Error('无法启动训练进程（Python 解释器 "' + CONFIG.python + '" 是否存在？可用 GMR_PYTHON 指定 venv 内的 python）: ' + e.message);
  }

  let spawnError = null;
  child.on('error', function (err) { spawnError = err.message; });

  const pid = child.pid;
  // 与子进程彻底解绑，插件进程退出后训练继续
  child.unref();
  fs.closeSync(logFd);

  const job = {
    id: id,
    name: name,
    kind: kind,
    status: 'running',
    pid: pid,
    python: CONFIG.python,
    script: script,
    dataset: datasetAbs,
    outDir: outDir,
    logFile: lp,
    doneFile: donePath(id),
    args: args,
    startedAt: new Date().toISOString(),
    finishedAt: null,
    exitCode: null,
    registeredModelId: null,
  };
  if (spawnError) {
    job.status = 'failed';
    job.error = 'spawn 失败: ' + spawnError;
  }
  writeJob(job);

  return {
    job: {
      id: job.id,
      name: job.name,
      kind: job.kind,
      status: job.status,
      pid: job.pid,
      outDir: job.outDir,
      logFile: job.logFile,
    },
    hint: '训练已在独立进程中启动，插件不会等待。用 job_status(job_id="' + id + '") 查询进度，用 cancel_job 终止。'
      + NL + '训练成功后 checkpoint 会自动登记进模型注册表，无需再手动 import_model。',
  };
}

function listJobs(statusFilter) {
  ensureDirs();
  const files = fs.readdirSync(CONFIG.jobsDir).filter(function (f) {
    return f.endsWith('.json') && !f.endsWith('.tmp');
  });
  const out = [];
  for (const f of files) {
    try {
      let job = JSON.parse(fs.readFileSync(path.join(CONFIG.jobsDir, f), 'utf8'));
      job = reconcile(job);
      if (statusFilter && job.status !== statusFilter) continue;
      out.push({
        id: job.id,
        name: job.name,
        kind: job.kind,
        status: job.status,
        pid: job.pid,
        startedAt: job.startedAt,
        finishedAt: job.finishedAt,
        registeredModelId: job.registeredModelId,
      });
    } catch (e) { /* 跳过损坏的状态文件 */ }
  }
  out.sort(function (a, b) { return String(b.startedAt).localeCompare(String(a.startedAt)); });
  return { count: out.length, jobsDir: CONFIG.jobsDir, jobs: out };
}

function jobStatus(id, tailBytes) {
  const job = reconcile(readJob(String(id || '').trim()));
  return {
    job: {
      id: job.id,
      name: job.name,
      kind: job.kind,
      status: job.status,
      pid: job.pid,
      alive: job.status === 'running' ? isAlive(job.pid) : false,
      startedAt: job.startedAt,
      finishedAt: job.finishedAt,
      exitCode: job.exitCode,
      outDir: job.outDir,
      registeredModelId: job.registeredModelId,
      error: job.error || null,
      warning: job.warning || null,
      metrics: job.metrics || null,
    },
    logTail: tailFile(job.logFile, tailBytes ? parseInt(tailBytes, 10) : undefined),
  };
}

function cancelJob(id) {
  const key = String(id || '').trim();
  const job = reconcile(readJob(key));
  if (job.status !== 'running') {
    return { id: key, status: job.status, note: '任务已是终态，无需取消。' };
  }
  if (!isAlive(job.pid)) {
    job.status = 'failed';
    job.error = '取消时发现进程已不存在。';
    job.finishedAt = new Date().toISOString();
    writeJob(job);
    return { id: key, status: job.status, note: '进程已不存在，状态已更新。' };
  }
  try {
    // 先温和终止，让 Python 有机会保存 checkpoint 与写 done 文件
    process.kill(job.pid, 'SIGTERM');
  } catch (e) {
    throw new Error('发送 SIGTERM 失败: ' + e.message);
  }
  job.status = 'cancelled';
  job.finishedAt = new Date().toISOString();
  writeJob(job);
  return {
    id: key,
    status: 'cancelled',
    note: '已发送 SIGTERM。若进程无响应，需手动 kill -9 ' + job.pid + '。已保存的 checkpoint 不会被删除。',
  };
}

module.exports = { startTraining, listJobs, jobStatus, cancelJob, tailFile };