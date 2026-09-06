'use strict';
// ============================================================
// node_transpiler.js  --  ObsidianBridge 节点写作模式 · 纯函数层
// 零 IO、零依赖。所有字符串变换集中于此，可脱离 Obsidian 单测。
// ============================================================

// 中文间隔号 U+00B7。源码内不写字面量，避免任何环节的编码风险。
var DOT = String.fromCharCode(0x00B7);
var MARK = DOT + DOT;

var TAG_CHARS = 'A-Za-z0-9_\\u4e00-\\u9fa5\\-';
var TAG_RE = new RegExp('^[' + TAG_CHARS + ']+$');

function beginOf(tag) { return '<!--AUTO_' + tag + '_BEGIN-->'; }
function endOf(tag) { return '<!--AUTO_' + tag + '_END-->'; }
function anchorRe() { return new RegExp('<!--AUTO_([' + TAG_CHARS + ']+)_(BEGIN|END)-->', 'g'); }

// ---------- 通用小工具 ----------

// 文档侧只做 CRLF 归一，绝不改动其它字符（改了就会写回污染原文）
function normDoc(s) {
    return String(s == null ? '' : s).replace(/\r\n/g, '\n').replace(/\r/g, '\n');
}

// 匹配目标侧做完整归一：Agent 可能写字面量 \n，而文档里是真换行
function normTarget(s) {
    return normDoc(s).replace(/\\n/g, '\n').replace(/\\t/g, '\t');
}

// 剥掉 Markdown 标题语法，保留标题文字
function stripHeading(s) {
    return String(s == null ? '' : s).replace(/^[ \t]*#{1,6}[ \t]*/gm, '');
}

// Markdown 表格单元格转义
function cell(s) {
    return String(s == null ? '' : s)
        .replace(/\|/g, '\\|')
        .replace(/\n/g, '\u23CE')
        .replace(/<!--/g, '<!-')
        .replace(/-->/g, '- >');
}

function countOccur(hay, needle) {
    if (!needle) return 0;
    var n = 0, i = 0;
    for (;;) {
        var k = hay.indexOf(needle, i);
        if (k === -1) return n;
        n++; i = k + 1;
    }
}

// 逗号分隔的 tag 位置列表；末尾空位先剔除，不因手滑多打逗号触发报错
function parseTags(csv) {
    if (csv === undefined || csv === null || csv === '') return [];
    var arr = String(csv).split(',').map(function (s) { return s.trim(); });
    while (arr.length && arr[arr.length - 1] === '') arr.pop();
    return arr;
}

function validateTag(tag) {
    if (!tag) return 'tag 不可为空';
    if (String(tag).indexOf('-->') !== -1) return 'tag 含 --> 片段，会撕破注释锚点';
    if (!TAG_RE.test(tag)) return 'tag "' + tag + '" 含非法字符，仅允许 字母/数字/下划线/连字符/中文';
    return null;
}

// ---------- 代码区间（扫 MARK 及 锚点 时跳过） ----------

function codeRanges(text) {
    var ranges = [];
    var lines = text.split('\n');
    var pos = 0, fenceCh = null, fenceLen = 0, fenceStart = 0;
    for (var i = 0; i < lines.length; i++) {
        var lineStart = pos;
        pos += lines[i].length + 1; // 包含 \n
        var m = lines[i].match(/^[ \t]*(`{3,}|~{3,})/);
        if (!m) continue;
        var ch = m[1].charAt(0);
        var len = m[1].length;
        if (fenceCh === null) {
            fenceCh = ch; fenceLen = len; fenceStart = lineStart;
        } else if (ch === fenceCh && len >= fenceLen) {
            ranges.push([fenceStart, pos]);
            fenceCh = null; fenceLen = 0;
        }
    }
    if (fenceCh !== null) ranges.push([fenceStart, text.length]);

    var inFence = function (idx) {
        for (var k = 0; k < ranges.length; k++) if (idx >= ranges[k][0] && idx < ranges[k][1]) return true;
        return false;
    };

    // 匹配任意长度的反引号 inline code
    var inlineRe = /(`+)([\s\S]*?)\1/g, mm;
    while ((mm = inlineRe.exec(text)) !== null) {
        if (!inFence(mm.index)) {
            ranges.push([mm.index, mm.index + mm[0].length]);
        }
    }
    return ranges;
}

function makeSkipTest(ranges) {
    return function (idx) {
        for (var k = 0; k < ranges.length; k++) if (idx >= ranges[k][0] && idx < ranges[k][1]) return true;
        return false;
    };
}

module.exports = {
    DOT: DOT, MARK: MARK,
    beginOf: beginOf, endOf: endOf, anchorRe: anchorRe,
    normDoc: normDoc, normTarget: normTarget,
    stripHeading: stripHeading, cell: cell, countOccur: countOccur,
    parseTags: parseTags, validateTag: validateTag,
    codeRanges: codeRanges, makeSkipTest: makeSkipTest
};

// ============================================================
// 扫描 / 审计 / 呈现
// ============================================================

// 取首尾 n 个码点。剥标题语法保留文字，trim 但不折叠内部空白。
function edge(body, n) {
    var s = stripHeading(normDoc(body)).trim();
    var cps = Array.from(s);
    if (cps.length === 0) return { head: '\u2205', tail: '\u2205', len: 0 };
    return {
        head: cps.slice(0, n).join(''),
        tail: cps.slice(Math.max(0, cps.length - n)).join(''),
        len: cps.length
    };
}

// 扫出全部锚点对。返回 { nodes, errors }
// 自动忽略 Markdown 代码块及 inline code 里的伪锚点
function scanNodes(text) {
    var t = normDoc(text);
    var skip = makeSkipTest(codeRanges(t));
    var re = anchorRe();
    var toks = [], m;
    while ((m = re.exec(t)) !== null) {
        if (!skip(m.index)) {
            toks.push({ tag: m[1], kind: m[2], start: m.index, end: m.index + m[0].length });
        }
    }
    var nodes = [], errors = [], pending = null;
    for (var i = 0; i < toks.length; i++) {
        var tk = toks[i];
        if (tk.kind === 'BEGIN') {
            if (pending) errors.push('锚点 "' + pending.tag + '" 的 BEGIN 尚未闭合便遇到新的 BEGIN "' + tk.tag + '"（不支持嵌套）');
            pending = tk;
        } else {
            if (!pending) { errors.push('孤立的 END 锚点 "' + tk.tag + '"'); continue; }
            if (pending.tag !== tk.tag) { errors.push('锚点不配对: BEGIN "' + pending.tag + '" 对上 END "' + tk.tag + '"'); pending = null; continue; }
            nodes.push({
                tag: tk.tag, index: nodes.length + 1,
                beginStart: pending.start, bodyStart: pending.end,
                bodyEnd: tk.start, endEnd: tk.end,
                body: t.slice(pending.end, tk.start)
            });
            pending = null;
        }
    }
    if (pending) errors.push('锚点 "' + pending.tag + '" 缺少 END');

    var seen = {};
    for (var j = 0; j < nodes.length; j++) {
        var k = 'k' + nodes[j].tag;
        if (seen[k] !== undefined) {
            errors.push('tag 重名: "' + nodes[j].tag + '" 同时出现在第 ' + seen[k] + ' 和第 ' + nodes[j].index + ' 个节点。tag 必须唯一，否则寻址失效');
        } else seen[k] = nodes[j].index;
    }
    return { nodes: nodes, errors: errors };
}

// 审计表。写入类命令操作完毕后一律返回，作为 Agent 的地图与反馈通道。
function buildAudit(nodes, note) {
    var out = [];
    out.push('节点总数: ' + nodes.length + (note ? '  |  ' + note : ''));
    if (nodes.length === 0) {
        out.push('');
        out.push('（本文档无节点。若期望有节点却显示 0，请检查是否用了双点 ' + MARK + ' 且成对）');
        return out.join('\n');
    }
    out.push('');
    out.push('| # | tag | 首5 | 尾5 | 长度 |');
    out.push('|---|-----|-----|-----|------|');
    for (var i = 0; i < nodes.length; i++) {
        var e = edge(nodes[i].body, 5);
        out.push('| ' + nodes[i].index + ' | ' + cell(nodes[i].tag) + ' | ' + cell(e.head) + ' | ' + cell(e.tail) + ' | ' + e.len + ' |');
    }
    return out.join('\n');
}

// 锚点 → Agent 可读形式。跳过代码块内部的示例锚点。
function toReadable(text) {
    var t = normDoc(text);
    var skip = makeSkipTest(codeRanges(t));
    var re = new RegExp('<!--AUTO_([' + TAG_CHARS + ']+)_(BEGIN|END)-->', 'g');
    var out = '', lastIdx = 0, m;
    while ((m = re.exec(t)) !== null) {
        if (!skip(m.index)) {
            out += t.slice(lastIdx, m.index);
            out += (m[2] === 'BEGIN' ? '[node-tag:' + m[1] + ']' : '[/node-tag:' + m[1] + ']');
            lastIdx = m.index + m[0].length;
        }
    }
    out += t.slice(lastIdx);
    return out;
}

// ============================================================
// 白板落笔: ·· → 锚点
// ============================================================
function transpileCreate(text, tagsCsv) {
    var t = normDoc(text);
    var skip = makeSkipTest(codeRanges(t));

    var pos = [], i = 0;
    for (;;) {
        var k = t.indexOf(MARK, i);
        if (k === -1) break;
        if (!skip(k)) pos.push(k);
        i = k + MARK.length;
    }

    var pairs = [];
    for (var p = 0; p + 1 < pos.length; p += 2) pairs.push([pos[p], pos[p + 1]]);
    var N = pairs.length;

    var tags = parseTags(tagsCsv);
    if (tags.length > N) {
        return { error: 'tags 数量(' + tags.length + ') 超过节点对数量(' + N + ')。请核对正文里成对的双点标记数量；未命名的位置会自动补 Default{i}，无需占位。' };
    }

    var assigned = [];
    for (var j = 0; j < N; j++) {
        var tg = (tags[j] !== undefined && tags[j] !== '') ? tags[j] : 'Default' + (j + 1);
        var ve = validateTag(tg);
        if (ve) return { error: '第 ' + (j + 1) + ' 个节点: ' + ve };
        assigned.push(tg);
    }

    var out = t;
    for (var q = N - 1; q >= 0; q--) {
        var a = pairs[q][0], b = pairs[q][1];
        var body = out.slice(a + MARK.length, b);
        out = out.slice(0, a) + beginOf(assigned[q]) + body + endOf(assigned[q]) + out.slice(b + MARK.length);
    }

    var sc = scanNodes(out);
    if (sc.errors.length) return { error: '转译后自检失败: ' + sc.errors.join('; ') };

    return {
        content: out,
        nodes: sc.nodes,
        pairCount: N,
        strayDots: pos.length - N * 2,
        audit: buildAudit(sc.nodes, '本次转译 ' + N + ' 对' + (pos.length % 2 ? '，另有 1 处双点未配对已按字面量保留' : ''))
    };
}

Object.assign(module.exports, {
    edge: edge, scanNodes: scanNodes, buildAudit: buildAudit,
    toReadable: toReadable, transpileCreate: transpileCreate
});

// ============================================================
// 五片切分 —— 一切 tag 操作的唯一寻址入口
//   head | BEGIN | body | END | tail
// 寻址逻辑只写一次，四个 tag 操作都是它的薄壳。
// ============================================================
function splitByTag(text, tag) {
    var t = normDoc(text);
    var sc = scanNodes(t);
    if (sc.errors.length) return { error: '文档锚点结构异常，请先修复: ' + sc.errors.join('; ') };

    var hit = null;
    for (var i = 0; i < sc.nodes.length; i++) if (sc.nodes[i].tag === tag) { hit = sc.nodes[i]; break; }
    if (!hit) {
        var avail = sc.nodes.map(function (n) { return n.tag; });
        return {
            error: 'tag "' + tag + '" 不存在。' +
                (avail.length ? '可用 tag: ' + avail.join(', ') : '本文档没有任何节点，请先用 node_add 添加。')
        };
    }
    return {
        head: t.slice(0, hit.beginStart),
        begin: t.slice(hit.beginStart, hit.bodyStart),
        body: hit.body,
        end: t.slice(hit.bodyEnd, hit.endEnd),
        tail: t.slice(hit.endEnd),
        node: hit, all: sc.nodes
    };
}

function _reassembled(newText, note) {
    var sc = scanNodes(newText);
    if (sc.errors.length) return { error: '操作后自检失败: ' + sc.errors.join('; ') };
    return { content: newText, nodes: sc.nodes, audit: buildAudit(sc.nodes, note) };
}

// ============================================================
// node_add —— 唯一的模糊操作，从「文本空间」跨到「锚点空间」的渡口
//
// 顺序处理策略（旅友/夕弦 2026-09-02 定调）:
// 总是取最先出现的第一个匹配项包裹节点。若 target 在文档中有重复，
// 按顺序取最靠前的那个，不抛重叠/多次匹配的阻断报错。
// ============================================================
function wrapTarget(text, target, tag) {
    var t = normDoc(text);
    var raw = normDoc(target);
    if (!raw) return { error: '缺少必需参数: target（要包成节点的原文）' };
    var tgt = raw;

    var ve = validateTag(tag);
    if (ve) return { error: ve };

    var sc0 = scanNodes(t);
    if (sc0.errors.length) return { error: '文档锚点结构异常，请先修复: ' + sc0.errors.join('; ') };
    for (var i = 0; i < sc0.nodes.length; i++) {
        if (sc0.nodes[i].tag === tag) return { error: 'tag "' + tag + '" 已存在（第 ' + sc0.nodes[i].index + ' 个节点）。tag 必须唯一，请换一个名字。' };
    }

    // 按顺序搜索首个匹配位置 (字面量优先)
    var a = t.indexOf(tgt);
    if (a === -1) {
        var alt = normTarget(target);
        if (alt !== raw) {
            a = t.indexOf(alt);
            if (a !== -1) tgt = alt;
        }
    }
    if (a === -1) return { error: '未在文档中找到该 target。请确认原文（可先用 node_read mode=full 取得当前全文）。' };

    var b = a + tgt.length;

    // 与已有锚点重叠 → 会切出交叉嵌套，污染寻址能力本身
    for (var j = 0; j < sc0.nodes.length; j++) {
        var nd = sc0.nodes[j];
        var overlap = a < nd.endEnd && b > nd.beginStart;
        if (!overlap) continue;
        var contained = a >= nd.bodyStart && b <= nd.bodyEnd;
        return {
            error: 'target ' + (contained ? '位于' : '与') + '已有节点 "' + nd.tag + '" ' +
                (contained ? '内部' : '范围交叉') + '，当前版本不支持嵌套或交叉锚点。'
        };
    }

    var out = t.slice(0, a) + beginOf(tag) + tgt + endOf(tag) + t.slice(b);
    return _reassembled(out, '已添加节点 "' + tag + '"');
}

// ============================================================
// tag 操作 —— 全部无歧义，只是「选哪几片重新拼起来」
// ============================================================
function replaceBody(text, tag, content) {
    if (content === undefined || content === null) return { error: '缺少必需参数: content' };
    var s = splitByTag(text, tag);
    if (s.error) return s;
    var body = normDoc(content);
    return _reassembled(s.head + s.begin + body + s.end + s.tail, '已替换节点 "' + tag + '" 的正文');
}

function clearBody(text, tag) {
    var s = splitByTag(text, tag);
    if (s.error) return s;
    if (s.body.trim() === '') return { error: '节点 "' + tag + '" 的正文已为空，无需清空。若要拆除锚点请用 node_delete。' };
    return _reassembled(s.head + s.begin + s.end + s.tail, '已清空节点 "' + tag + '" 的正文（锚点保留，可继续 node_delete 拆除）');
}

// 拆壳。前置条件: 正文必须已为空（两步删除法，确保有可审计的中间态）
function unwrapNode(text, tag) {
    var s = splitByTag(text, tag);
    if (s.error) return s;
    if (s.body.trim() !== '') {
        var e = edge(s.body, 5);
        return {
            error: '节点 "' + tag + '" 仍有正文（' + e.len + ' 字符: "' + e.head + '…' + e.tail + '"）。' +
                '请先 node_text_delete 清空，再 node_delete 拆除锚点。此两步设计用于避免误删正文。'
        };
    }
    return _reassembled(s.head + s.tail, '已拆除节点 "' + tag + '" 的锚点');
}

// ============================================================
// node_read 三模式
// ============================================================
function readView(text, mode, tag) {
    var t = normDoc(text);
    if (mode === 'full') {
        var sc = scanNodes(t);
        return { text: toReadable(t), nodeCount: sc.nodes.length };
    }
    if (mode === 'tags') {
        var s2 = scanNodes(t);
        if (s2.errors.length) return { error: '文档锚点结构异常: ' + s2.errors.join('; ') };
        return { text: buildAudit(s2.nodes, null), nodeCount: s2.nodes.length };
    }
    if (mode === 'node') {
        if (!tag) return { error: 'mode=node 时必须提供 tag 参数。可先用 mode=tags 查看可用 tag。' };
        var s3 = splitByTag(t, tag);
        if (s3.error) return s3;
        return { text: s3.body, nodeCount: s3.all.length, tag: tag };
    }
    return { error: 'mode 无效: "' + mode + '"。必须为 full / tags / node 之一。' };
}

Object.assign(module.exports, {
    splitByTag: splitByTag, wrapTarget: wrapTarget,
    replaceBody: replaceBody, clearBody: clearBody, unwrapNode: unwrapNode,
    readView: readView
});
