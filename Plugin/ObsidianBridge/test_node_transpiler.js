'use strict';
// node_transpiler.js 单元测试 —— 纯函数层，不依赖 Obsidian
var T = require('./node_transpiler.js');
var M = T.MARK, DOT = T.DOT;
var pass = 0, fails = [];
function t(name, fn) {
    try { fn(); pass++; } catch (e) { fails.push(name + '\n      -> ' + e.message); }
}
function eq(a, b, m) { if (a !== b) throw new Error((m || '') + ' 期望[' + b + '] 实得[' + a + ']'); }
function ok(c, m) { if (!c) throw new Error(m || '断言失败'); }
function has(s, sub, m) { if (String(s).indexOf(sub) === -1) throw new Error((m || '') + ' 未包含[' + sub + '] 实得[' + String(s).slice(0, 160) + ']'); }
function isErr(r, sub) { ok(r.error, '应报错但未报错'); if (sub) has(r.error, sub, '错误信息'); }

// ---------- 白板落笔 ----------
t('01 基础配对 → Default1', function () {
    var r = T.transpileCreate(M + '你好' + M, '');
    eq(r.content, '<!--AUTO_Default1_BEGIN-->你好<!--AUTO_Default1_END-->');
    eq(r.nodes.length, 1); eq(r.pairCount, 1);
});
t('02 指定 tag', function () {
    var r = T.transpileCreate(M + '你好' + M, 'hello');
    eq(r.content, '<!--AUTO_hello_BEGIN-->你好<!--AUTO_hello_END-->');
});
t('03 Default 用全局序号补齐', function () {
    var r = T.transpileCreate(M + 'a' + M + 'x' + M + 'b' + M, 'hello');
    eq(r.nodes.length, 2);
    eq(r.nodes[0].tag, 'hello'); eq(r.nodes[1].tag, 'Default2');
});
t('04 tags 中间留空 → 该位 Default', function () {
    var r = T.transpileCreate(M + 'a' + M + '-' + M + 'b' + M + '-' + M + 'c' + M, 'x,,z');
    eq(r.nodes.map(function (n) { return n.tag; }).join('|'), 'x|Default2|z');
});
t('05 tags 末尾多打逗号不报错', function () {
    var r = T.transpileCreate(M + 'a' + M, 'hello,,');
    ok(!r.error, '不应报错: ' + r.error); eq(r.nodes[0].tag, 'hello');
});
t('06 tags 超量 → 唯一的报错条件', function () {
    isErr(T.transpileCreate(M + 'a' + M, 'x,y'), '超过节点对数量');
});
t('07 白板落笔: 落单的第三点原样保留', function () {
    var r = T.transpileCreate(M + '你好' + M + DOT, '');
    eq(r.pairCount, 1);
    eq(r.content, '<!--AUTO_Default1_BEGIN-->你好<!--AUTO_Default1_END-->' + DOT);
});
t('08 白板落笔: 落单的双点原样保留', function () {
    var r = T.transpileCreate(M + 'a' + M + 'b' + M, '');
    eq(r.pairCount, 1); has(r.content, 'b' + M, '尾部未配对的双点应保留');
});
t('09 人名号不被误切', function () {
    var src = '列夫' + DOT + '托尔斯泰与玛丽' + DOT + '居里';
    var r = T.transpileCreate(src, '');
    eq(r.content, src); eq(r.nodes.length, 0);
});
t('10 无节点时审计表给出自诊断提示', function () {
    var r = T.transpileCreate('普通文档', '');
    has(r.audit, '节点总数: 0'); has(r.audit, '双点');
});
t('11 围栏代码块内不转译', function () {
    var src = '正文\n```js\nvar a = "' + M + 'x' + M + '";\n```\n尾';
    var r = T.transpileCreate(src, '');
    eq(r.nodes.length, 0); eq(r.content, src);
});
t('12 行内代码不转译', function () {
    var src = '看 `' + M + 'x' + M + '` 这里';
    var r = T.transpileCreate(src, '');
    eq(r.nodes.length, 0);
});
t('13 空行保留（段落结构不被压扁）', function () {
    var r = T.transpileCreate('# 标题\n\n' + M + '正文' + M + '\n\n尾段', '');
    has(r.content, '# 标题\n\n<!--AUTO_Default1_BEGIN-->');
    has(r.content, '<!--AUTO_Default1_END-->\n\n尾段');
});
t('14 非法 tag 被拦截', function () {
    isErr(T.transpileCreate(M + 'a' + M, 'has space'), '非法字符');
    isErr(T.transpileCreate(M + 'a' + M, 'x-->y'), '撕破');
});
t('15 中文 tag 合法', function () {
    var r = T.transpileCreate(M + 'a' + M, '核心论点');
    ok(!r.error, r.error); eq(r.nodes[0].tag, '核心论点');
});

// ---------- 扫描 ----------
t('16 tag 重名 → 硬报错', function () {
    var s = T.scanNodes('<!--AUTO_x_BEGIN-->a<!--AUTO_x_END--><!--AUTO_x_BEGIN-->b<!--AUTO_x_END-->');
    ok(s.errors.length > 0); has(s.errors.join(';'), '重名');
});
t('17 缺 END → 报错', function () {
    has(T.scanNodes('<!--AUTO_x_BEGIN-->a').errors.join(';'), '缺少 END');
});
t('18 孤立 END → 报错', function () {
    has(T.scanNodes('a<!--AUTO_x_END-->').errors.join(';'), '孤立');
});
t('19 嵌套 → 报错', function () {
    has(T.scanNodes('<!--AUTO_a_BEGIN-->1<!--AUTO_b_BEGIN-->2<!--AUTO_b_END-->3<!--AUTO_a_END-->').errors.join(';'), '嵌套');
});

// ---------- 五片切分 ----------
var DOC = '开头段\n\n<!--AUTO_mid_BEGIN-->中间正文<!--AUTO_mid_END-->\n\n结尾段';
t('20 五片可无损还原原文', function () {
    var s = T.splitByTag(DOC, 'mid');
    ok(!s.error, s.error);
    eq(s.head + s.begin + s.body + s.end + s.tail, DOC);
    eq(s.body, '中间正文');
});
t('21 tag 不存在 → 列出可用 tag', function () {
    isErr(T.splitByTag(DOC, 'nope'), '可用 tag: mid');
});
t('22 空文档 tag 不存在 → 引导 node_add', function () {
    isErr(T.splitByTag('纯文本', 'x'), 'node_add');
});

// ---------- node_add 渡口 ----------
t('23 成功包裹句中短语（不劈开段落）', function () {
    var r = T.wrapTarget('这是一句话里的关键短语在中间。', '关键短语', 'k');
    ok(!r.error, r.error);
    eq(r.content, '这是一句话里的<!--AUTO_k_BEGIN-->关键短语<!--AUTO_k_END-->在中间。');
    eq(r.nodes.length, 1);
});
t('24 0 处匹配 → 报错并引导 node_read', function () {
    isErr(T.wrapTarget('abc', 'xyz', 'k'), '未在文档中找到');
});
t('25 N 处匹配 → 顺序包裹首个匹配项', function () {
    var r = T.wrapTarget('xxxaaayyy', 'aa', 'k');
    eq(r.content, 'xxx<!--AUTO_k_BEGIN-->aa<!--AUTO_k_END-->ayyy');
});
t('26 tag 已存在 → 拒绝', function () {
    isErr(T.wrapTarget(DOC, '开头段', 'mid'), '已存在');
});
t('27 target 落在已有节点内部 → 拒绝', function () {
    isErr(T.wrapTarget(DOC, '中间正文', 'k2'), '内部');
});
t('28 target 与锚点范围交叉 → 拒绝', function () {
    isErr(T.wrapTarget(DOC, '正文<!--AUTO_mid_END-->\n\n结尾', 'k3'), '交叉');
});
t('29 target 支持字面量 \\n 归一', function () {
    var r = T.wrapTarget('第一行\n第二行', '第一行\\n第二行', 'k');
    ok(!r.error, r.error); eq(r.nodes[0].body, '第一行\n第二行');
});

// ---------- tag 操作 ----------
t('30 replace: 换正文，锚点留存', function () {
    var r = T.replaceBody(DOC, 'mid', '新的内容');
    ok(!r.error, r.error);
    eq(r.content, '开头段\n\n<!--AUTO_mid_BEGIN-->新的内容<!--AUTO_mid_END-->\n\n结尾段');
});
t('31 replace: 缺 content 报错', function () { isErr(T.replaceBody(DOC, 'mid', undefined), 'content'); });
t('32 clear: 清空正文，锚点留存', function () {
    var r = T.clearBody(DOC, 'mid');
    ok(!r.error, r.error);
    eq(r.content, '开头段\n\n<!--AUTO_mid_BEGIN--><!--AUTO_mid_END-->\n\n结尾段');
    has(r.audit, 'node_delete', '应引导下一步');
});
t('33 clear: 已空则拒绝重复清空', function () {
    var empty = T.clearBody(DOC, 'mid').content;
    isErr(T.clearBody(empty, 'mid'), '已为空');
});
t('34 两步删除法: 有正文时拒绝拆壳', function () {
    var r = T.unwrapNode(DOC, 'mid');
    isErr(r, 'node_text_delete'); has(r.error, '仍有正文');
});
t('35 两步删除法: 清空后可拆壳且无缝', function () {
    var empty = T.clearBody(DOC, 'mid').content;
    var r = T.unwrapNode(empty, 'mid');
    ok(!r.error, r.error);
    eq(r.content, '开头段\n\n\n\n结尾段');
    eq(r.nodes.length, 0);
});
t('36 空节点审计表显示 ∅ 与长度 0', function () {
    var empty = T.clearBody(DOC, 'mid').content;
    var a = T.buildAudit(T.scanNodes(empty).nodes, null);
    has(a, '\u2205'); has(a, '| 0 |');
});

// ---------- node_read ----------
t('37 mode=full 转成可读式，无 HTML', function () {
    var v = T.readView(DOC, 'full');
    has(v.text, '[node-tag:mid]'); has(v.text, '[/node-tag:mid]');
    ok(v.text.indexOf('<!--') === -1, '不应残留 HTML');
    eq(v.nodeCount, 1);
});
t('38 mode=tags 返回审计表', function () {
    var v = T.readView(DOC, 'tags');
    has(v.text, '| # | tag |'); has(v.text, 'mid');
});
t('39 mode=node 仅返回正文', function () {
    eq(T.readView(DOC, 'node', 'mid').text, '中间正文');
});
t('40 mode=node 缺 tag → 引导 mode=tags', function () {
    isErr(T.readView(DOC, 'node'), 'mode=tags');
});
t('41 mode 无效 → 报错列出合法值', function () {
    isErr(T.readView(DOC, 'xxx'), 'full / tags / node');
});
t('42 无节点文档 mode=full 原样返回', function () {
    var v = T.readView('干净文本', 'full'); eq(v.text, '干净文本'); eq(v.nodeCount, 0);
});

// ---------- edge / 审计细节 ----------
t('43 edge 剥标题语法保留文字', function () {
    eq(T.edge('### 标题文字后续', 5).head, '标题文字后');
});
t('44 edge 按 Unicode 码点计数（emoji 不被切半）', function () {
    var e = T.edge('\u{1F44D}abcdefg', 5);
    eq(e.len, 8); eq(e.head, '\u{1F44D}abcd');
});
t('45 edge 短块首尾窗口重叠时原样输出', function () {
    var e = T.edge('abc', 5); eq(e.head, 'abc'); eq(e.tail, 'abc'); eq(e.len, 3);
});
t('46 审计表转义竖线与换行不破表', function () {
    var a = T.buildAudit(T.scanNodes('<!--AUTO_p_BEGIN-->a|b\nc<!--AUTO_p_END-->').nodes, null);
    has(a, '\\|'); ok(a.split('\n').length === 5, '表应为 5 行，实得 ' + a.split('\n').length);
});
t('47 CRLF 归一', function () {
    eq(T.normDoc('a\r\nb'), 'a\nb');
});

// ---------- 全链路 ----------
t('48 全链路: create → add → replace → clear → delete', function () {
    var c = T.transpileCreate('# 文档\n\n' + M + '第一节' + M + '\n\n普通段落收尾', 'sec1');
    ok(!c.error, c.error); eq(c.nodes.length, 1);
    var a = T.wrapTarget(c.content, '普通段落', 'sec2');
    ok(!a.error, a.error); eq(a.nodes.length, 2);
    var rp = T.replaceBody(a.content, 'sec1', '改写后的第一节');
    ok(!rp.error, rp.error); eq(T.readView(rp.content, 'node', 'sec1').text, '改写后的第一节');
    var cl = T.clearBody(rp.content, 'sec2');
    ok(!cl.error, cl.error);
    var dl = T.unwrapNode(cl.content, 'sec2');
    ok(!dl.error, dl.error); eq(dl.nodes.length, 1);
    has(dl.content, '# 文档\n\n<!--AUTO_sec1_BEGIN-->改写后的第一节<!--AUTO_sec1_END-->');
    ok(dl.content.indexOf('sec2') === -1, 'sec2 锚点应已拆除');
});

// ---------- LaTeX 回归: 与 Obsidian CLI 同类缺陷的防护 ----------
var BS = String.fromCharCode(92);
t('49 wrapTarget: \\theta 不被 \\t 转义摧毁', function () {
    var doc = 'X ' + BS + 'theta 与 ' + BS + 'times Y';
    var r = T.wrapTarget(doc, BS + 'theta 与 ' + BS + 'times', 'f');
    ok(!r.error, r.error);
    eq(r.nodes[0].body, BS + 'theta 与 ' + BS + 'times');
    ok(r.content.indexOf(String.fromCharCode(9)) === -1, '不应出现制表符');
});
t('50 wrapTarget: \\nabla \\neq 不被 \\n 转义摧毁', function () {
    var doc = 'A' + BS + 'nabla B' + BS + 'neq C';
    var r = T.wrapTarget(doc, BS + 'nabla B' + BS + 'neq', 'g');
    ok(!r.error, r.error);
    eq(r.nodes[0].body, BS + 'nabla B' + BS + 'neq');
});
t('51 wrapTarget: 字面量 \\n 零匹配时回退仍生效', function () {
    var r = T.wrapTarget('第一行\n第二行'.replace('\\n', String.fromCharCode(10)), '第一行' + BS + 'n第二行', 'k');
    ok(!r.error, r.error);
    eq(r.nodes[0].body, '第一行' + String.fromCharCode(10) + '第二行');
});
t('52 replaceBody: content 里的 \\theta 原样写入', function () {
    var r = T.replaceBody(DOC, 'mid', 'X' + BS + 'theta' + BS + 'times Y');
    ok(!r.error, r.error);
    eq(T.readView(r.content, 'node', 'mid').text, 'X' + BS + 'theta' + BS + 'times Y');
    ok(r.content.indexOf(String.fromCharCode(9)) === -1, '不应出现制表符');
});
t('53 Windows 路径不被摧毁', function () {
    var doc = 'path C:' + BS + 'temp' + BS + 'new';
    var r = T.wrapTarget(doc, 'C:' + BS + 'temp' + BS + 'new', 'p');
    ok(!r.error, r.error);
    eq(r.nodes[0].body, 'C:' + BS + 'temp' + BS + 'new');
});

console.log('==========================================');
console.log('  PASS ' + pass + '   FAIL ' + fails.length + '   TOTAL ' + (pass + fails.length));
console.log('==========================================');
if (fails.length) { fails.forEach(function (f) { console.log('  FAIL  ' + f); }); process.exit(1); }
console.log('  ALL_GREEN');
