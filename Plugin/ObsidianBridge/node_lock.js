'use strict';
// ============================================================
// node_lock.js  --  按笔记路径的跨进程 FIFO 目录队列锁 (Ticket Queue Lock)
//
// 为什么必须是文件锁: VCPToolBox 以 pluginType=synchronous + stdio 调用本插件,
// 每次工具调用都 fork 一个新的 node 进程。进程一死内存状态即消失,
// 任何 let locked = true 之类的内存锁完全无效。
//
// 方案 C 机制原理 (Ticket Queue):
// 1. 取票落盘: 任何进程在笔记专属锁目录下写入 [高精时间戳]_[PID]_[随机].ticket
// 2. 检查位次: 读目录按自然字典序排序。队首 (index 0) 是自己则成功取得锁！
// 3. 顺序叫号: 自己执行完后删除自己的 ticket。下一个进程轮询时升格为 index 0。
// 4. 死锁自愈: 轮询中若发现队首进程 PID 已死亡，顺手帮其清理 ticket，自动叫号。
// ============================================================

const fs = require('fs');
const os = require('os');
const path = require('path');
const crypto = require('crypto');

const LOCK_BASE_DIR = path.join(os.tmpdir(), 'vcp-obsidian-node-locks');
const STALE_MS = 30000;   // 最长挂起容忍时间
const WAIT_MS = 15000;    // 最长排队等待时间
const POLL_MS = 50;       // 轮询时间间隔

function lockDirFor(notePath) {
    const h = crypto.createHash('sha1').update(String(notePath)).digest('hex').slice(0, 16);
    return path.join(LOCK_BASE_DIR, h);
}

function ensureDir(dirPath) {
    try { fs.mkdirSync(dirPath, { recursive: true }); } catch (_) { /* 已存在 */ }
}

function alive(pid) {
    if (!pid) return false;
    try { process.kill(pid, 0); return true; }
    catch (e) { return e.code === 'EPERM'; }
}

function sleepSync(ms) {
    try {
        Atomics.wait(new Int32Array(new SharedArrayBuffer(4)), 0, 0, ms);
    } catch (_) {
        const t = Date.now() + ms;
        while (Date.now() < t) { /* 退化忙等 */ }
    }
}

function readTicketMeta(ticketPath) {
    try { return JSON.parse(fs.readFileSync(ticketPath, 'utf8')); } catch (_) { return null; }
}

function acquire(notePath) {
    const qDir = lockDirFor(notePath);
    ensureDir(qDir);

    // 高精时间戳(微秒级模拟) + PID + 随机串 确保全系统唯一且绝对按时间正序
    const now = Date.now().toString().padStart(15, '0');
    const nonce = Math.random().toString(36).slice(2, 8);
    const ticketName = `${now}_${process.pid}_${nonce}.ticket`;
    const ticketPath = path.join(qDir, ticketName);

    // 1. 落盘排队票据 (写入 PID 和时间)
    try {
        fs.writeFileSync(ticketPath, JSON.stringify({ pid: process.pid, at: Date.now(), note: notePath }));
    } catch (e) {
        throw new Error('无法创建锁票据文件: ' + e.message);
    }

    const deadline = Date.now() + WAIT_MS;

    // 2. 轮询队列，严格按 FIFO 顺序排队
    for (;;) {
        let files = [];
        try {
            files = fs.readdirSync(qDir).filter(f => f.endsWith('.ticket')).sort();
        } catch (_) { }

        // 如果队列为空或找不到自己，说明出错了
        if (files.length === 0 || !files.includes(ticketName)) {
            // 尝试重新写入票据
            try { fs.writeFileSync(ticketPath, JSON.stringify({ pid: process.pid, at: Date.now(), note: notePath })); } catch (_) { }
        } else {
            // 检查队首 (0号)
            const headTicket = files[0];
            if (headTicket === ticketName) {
                // 成功获得锁！
                return { ticketPath, qDir, note: notePath };
            }

            // 自己不是队首，检查 0 号是否已经死掉或超时 (死锁自愈)
            const headPath = path.join(qDir, headTicket);
            const meta = readTicketMeta(headPath);
            const isDead = meta && !alive(meta.pid);
            const isStale = meta && (Date.now() - (meta.at || 0) > STALE_MS);

            if (isDead || isStale || !meta) {
                // 队首已死或损坏，帮其清理出队
                try { fs.unlinkSync(headPath); } catch (_) { }
                continue; // 立即下一轮重新检查
            }
        }

        // 超时退队
        if (Date.now() >= deadline) {
            try { fs.unlinkSync(ticketPath); } catch (_) { }
            const e = new Error(
                '获取写锁超时(' + (WAIT_MS / 1000) + 's): "' + notePath + '" 排队超时。请稍后重试。'
            );
            e.isLockTimeout = true;
            throw e;
        }

        sleepSync(POLL_MS);
    }
}

function release(handle) {
    if (!handle || !handle.ticketPath) return;
    try {
        fs.unlinkSync(handle.ticketPath);
    } catch (_) { /* 已释放 */ }
}

function withLock(notePath, fn) {
    const handle = acquire(notePath);
    try { return fn(); }
    finally { release(handle); }
}

module.exports = { acquire, release, withLock, LOCK_BASE_DIR, STALE_MS, WAIT_MS };
