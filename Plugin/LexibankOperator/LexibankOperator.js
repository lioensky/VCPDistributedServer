const fs = require('fs');
const path = require('path');
const { spawn } = require('child_process');

function loadEnv() {
  const envPath = path.join(__dirname, 'config.env');
  if (fs.existsSync(envPath)) {
    const lines = fs.readFileSync(envPath, 'utf8').split('\n');
    for (const line of lines) {
      const trimmed = line.trim();
      if (!trimmed || trimmed.startsWith('#')) continue;
      const idx = trimmed.indexOf('=');
      if (idx !== -1) {
        const k = trimmed.slice(0, idx).trim();
        const v = trimmed.slice(idx + 1).trim();
        process.env[k] = v;
      }
    }
  }
}

function runPythonQuery(inputPayload) {
  return new Promise((resolve) => {
    loadEnv();
    const queryScript = path.join(__dirname, 'engine', 'query.py');
    const pyBin = process.env.PYTHON_BIN || 'python3';
    const child = spawn(pyBin, [queryScript], {
      cwd: __dirname,
      env: process.env,
      stdio: ['pipe', 'pipe', 'pipe']
    });

    let stdoutData = '';
    let stderrData = '';
    child.stdout.setEncoding('utf8');
    child.stdout.on('data', d => { stdoutData += d; });

    child.stderr.setEncoding('utf8');
    child.stderr.on('data', d => { stderrData += d; });

    child.on('close', code => {
      if (code !== 0 && !stdoutData.trim()) {
        resolve({ error: `Engine exited with code ${code}`, stderr: stderrData.trim() });
      } else {
        try {
          resolve(JSON.parse(stdoutData.trim()));
        } catch (e) {
          resolve({ raw_output: stdoutData.trim(), stderr: stderrData.trim() });
        }
      }
    });

    child.on('error', err => {
      resolve({ error: `Failed to spawn python process: ${err.message}` });
    });

    const jsonStr = typeof inputPayload === 'string' ? inputPayload : JSON.stringify(inputPayload || {});
    child.stdin.write(jsonStr);
    child.stdin.end();
  });
}

// 终极兼容：捕获 VCP 传入的所有形参，彻底解决传参形式多义性
async function processToolCall(...rawArgs) {
  let merged = {};

  for (const item of rawArgs) {
    if (!item) continue;
    if (typeof item === 'string') {
      try {
        const parsed = JSON.parse(item);
        if (parsed && typeof parsed === 'object') {
          Object.assign(merged, parsed);
        } else {
          merged.command = merged.command || item;
        }
      } catch (e) {
        merged.command = merged.command || item;
      }
    } else if (typeof item === 'object') {
      Object.assign(merged, item);
    }
  }

  // 二次深层提取 command 字段
  if (merged.args && typeof merged.args === 'object') {
    Object.assign(merged, merged.args);
  }

  return await runPythonQuery(merged);
}

// 兼容 CLI 管道执行
if (require.main === module) {
  let raw = '';
  process.stdin.setEncoding('utf8');
  process.stdin.on('data', chunk => { raw += chunk; });
  process.stdin.on('end', async () => {
    try {
      const parsed = raw.trim() ? JSON.parse(raw) : {};
      const res = await runPythonQuery(parsed);
      process.stdout.write(JSON.stringify(res));
    } catch (e) {
      process.stdout.write(JSON.stringify({ error: e.message }));
    }
  });
}

module.exports = {
  processToolCall
};