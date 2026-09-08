'use strict';
// ============================================================
// node_io.js  --  节点写作模式的 IO 层
//
// 读: fs 直读（定位仍借 CLI 的 file 命令解析 wikilink -> relPath）
//     不用 CLI read 取内容, 因 execCLI 对输出做 .trim(), 会削掉文件首尾空白;
//     整篇覆写场景下那是会累积的损耗。
// 写: CLI create path=... content=... overwrite
//     与插件原有 22 命令同一条通道, 不偏离原架构。
//
// 已知代价（旅友 2026-09-02 决策）: CLI 无条件还原 content= 里的 \n \t 转义序列,
// 故以 \t / \n 起头的 LaTeX 命令（\theta \times \nabla \neq ...）与 Windows 路径
// 会在写入时被改写。实测该 vault 25 篇笔记中仅 1 处命中, 暴露面极小,
// 且 Obsidian 自带 history 可恢复, 因此不为此偏离原架构。
//     不设前置拦截; 改为写后落盘比对, 若不一致则在返回中附警示并指明首个差异行。
// ============================================================

const fs = require('fs');
const path = require('path');

// argv 单条上限 MAX_ARG_STRLEN = 128KB。escapeValue 会把每个换行/制表符
// 膨胀为两字节字面量, 故预估时按此计入, 阈值取保守值。
const ARGV_SAFE = 110 * 1024;

// ---------- vault 路径解析(动态取, 不硬编码) ----------
let _vaultCache = null;

function vaultRoot(execCLI, buildCommand, vaultName) {
    const key = vaultName || '__active__';
    if (_vaultCache && _vaultCache.key === key) return _vaultCache.root;
    const r = execCLI(buildCommand('vault', {}, [], vaultName));
    if (!r.success) throw new Error('无法获取 vault 路径: ' + r.output);
    let root = null;
    for (const line of String(r.output).split(/\r?\n/)) {
        const m = line.match(/^path\s+(.+)$/);
        if (m) { root = m[1].trim(); break; }
    }
    if (!root) throw new Error('vault 输出中未找到 path 字段: ' + r.output);
    _vaultCache = { key, root };
    return root;
}

function absOf(execCLI, buildCommand, args, relPath) {
    const root = vaultRoot(execCLI, buildCommand, args.vault);
    const rootAbs = path.resolve(root);
    const abs = path.resolve(path.join(root, relPath));
    if (abs !== rootAbs && !abs.startsWith(rootAbs + path.sep)) {
        throw new Error('目标路径逃逸出 vault: ' + relPath);
    }
    return abs;
}

// ---------- file info ----------
function fileInfo(execCLI, buildCommand, args) {
    const params = {};
    if (args.file) params.file = args.file;
    if (args.path) params.path = args.path;
    const r = execCLI(buildCommand('file', params, [], args.vault));
    if (!r.success) return { success: false, output: r.output };
    const info = {};
    for (const line of String(r.output).split(/\r?\n/)) {
        const m = line.match(/^(\w+)\s+(.*)$/);
        if (m) info[m[1]] = m[2].trim();
    }
    if (!info.path) return { success: false, output: '未能解析 file 输出: ' + r.output };
    return {
        success: true,
        relPath: info.path,
        size: parseInt(info.size, 10) || 0,
        modified: parseInt(info.modified, 10) || 0
    };
}

// ---------- 读 ----------
function readNote(execCLI, buildCommand, args) {
    const params = {};
    if (args.file) params.file = args.file;
    if (args.path) params.path = args.path;
    // 裸调用: 不经 read handler, 避免其 '笔记内容 [xxx]:' 装饰前缀污染写回内容
    const r = execCLI(buildCommand('read', params, [], args.vault));
    if (!r.success) return { success: false, output: r.output };
    return { success: true, text: r.output };
}

function readFs(execCLI, buildCommand, args, relPath) {
    let abs;
    try { abs = absOf(execCLI, buildCommand, args, relPath); }
    catch (e) { return { success: false, output: e.message }; }
    try {
        return { success: true, text: fs.readFileSync(abs, 'utf8'), absPath: abs };
    } catch (e) {
        return { success: false, output: '磁盘读取失败: ' + e.message };
    }
}

// ---------- 写: 与原有 22 命令同一条通道 ----------

// 预估 escapeValue 后的 argv 长度（换行/制表符各膨胀为两字节字面量）
function estimateArgLen(text) {
    const escaped = String(text).replace(/\n/g, '\\n').replace(/\t/g, '\\t');
    return Buffer.byteLength(escaped, 'utf8');
}

// 落盘比对: 不一致则定位首个差异行, 供返回中附带警示
function diffReport(expect, actual) {
    if (expect === actual) return null;
    const a = expect.split('\n'), b = actual.split('\n');
    const n = Math.max(a.length, b.length);
    for (let i = 0; i < n; i++) {
        if (a[i] !== b[i]) {
            const clip = (s) => s === undefined ? '(无此行)'
                : (s.length > 90 ? s.slice(0, 90) + '…' : s).replace(/\t/g, '<TAB>');
            return {
                line: i + 1,
                expect: clip(a[i]),
                actual: clip(b[i])
            };
        }
    }
    return { line: 0, expect: '(长度差异)', actual: '' };
}

function WARN(d) {
    return '\n\n[警示] 落盘内容与预期不一致，首个差异在第 ' + d.line + ' 行:'
        + '\n  预期: ' + d.expect
        + '\n  实际: ' + d.actual
        + '\n原因: Obsidian CLI 会还原 content= 中的 \\n \\t 转义序列，'
        + '以 \\t / \\n 起头的序列（如 \\theta \\times \\nabla \\neq 或 C:\\temp）会被改写。'
        + '\n如需恢复: obsidian history path=<笔记路径>';
}

// 经 CLI create 写入。overwrite 由 flags 控制:
//   已有文件的整篇覆写 -> ['overwrite']
//   新建且不允许覆盖   -> []
function writeViaCli(execCLI, buildCommand, args, relPath, newText, flags) {
    const est = estimateArgLen(newText);
    if (est > ARGV_SAFE) {
        return {
            success: false,
            output: '内容经转义后约 ' + est + ' 字节，超过命令行单参数安全上限 '
                + ARGV_SAFE + ' 字节，已中止且未写入任何内容。'
                + '（系统硬上限 131072 字节，超出会抛 E2BIG）'
        };
    }

    const r = execCLI(buildCommand('create', { path: relPath, content: newText }, flags || [], args.vault));
    if (!r.success) return { success: false, output: '写入失败: ' + r.output };

    // 落盘校验（读磁盘, 不经 CLI read 以免 trim 干扰比对）
    // actual 回传给调用方: 审计表必须基于磁盘实际内容计算,
    // 否则若 CLI 改写了 \\t \\n 序列, 审计表会报告一个不存在的状态。
    let warn = null, actual = newText;
    try {
        const abs = absOf(execCLI, buildCommand, args, relPath);
        actual = fs.readFileSync(abs, 'utf8');
        const d = diffReport(newText, actual);
        if (d) warn = WARN(d);
    } catch (e) {
        warn = '\n\n[警示] 无法完成落盘校验: ' + e.message;
    }

    return { success: true, bytes: Buffer.byteLength(actual, 'utf8'), warn: warn, actual: actual };
}

// 五个写入命令的回写入口: 乐观锁 + 整篇覆写
function writeBack(execCLI, buildCommand, args, relPath, expectModified, newText) {
    let abs;
    try { abs = absOf(execCLI, buildCommand, args, relPath); }
    catch (e) { return { success: false, output: e.message }; }

    if (!fs.existsSync(abs)) {
        return { success: false, output: '目标文件不存在于磁盘: ' + abs };
    }

    // 乐观锁: 防止读改写期间该文件被 Obsidian 内编辑改动
    if (expectModified) {
        let curMs = 0;
        try { curMs = Math.floor(fs.statSync(abs).mtimeMs); } catch (_) { }
        if (curMs && Math.abs(curMs - expectModified) > 1) {
            return {
                success: false,
                output: '文件在本次操作期间被改动（读取时 modified=' + expectModified
                    + '，当前=' + curMs + '）。为避免覆盖他人编辑已中止，未写入任何内容。请重新读取后再试。'
            };
        }
    }

    return writeViaCli(execCLI, buildCommand, args, relPath, newText, ['overwrite']);
}

// node_create 专用: 一次调用完成建档 + 写正文
function writeNew(execCLI, buildCommand, args, relPath, newText, allowOverwrite) {
    return writeViaCli(execCLI, buildCommand, args, relPath, newText,
        allowOverwrite ? ['overwrite'] : []);
}

module.exports = {
    vaultRoot, fileInfo, readNote, readFs,
    writeBack, writeNew, estimateArgLen, ARGV_SAFE
};
