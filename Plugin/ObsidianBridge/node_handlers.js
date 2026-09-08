'use strict';
// ============================================================
// node_handlers.js  --  节点写作模式的 6 个命令
//
// 编排层: 只做 IO 顺序与错误包装, 全部字符串变换委托 node_transpiler(纯函数)。
// 五个写入命令共用同一条流水线, 唯一差异是中间那个纯函数。
// ============================================================

const T = require('./node_transpiler.js');
const L = require('./node_lock.js');
const IO = require('./node_io.js');

function register(HANDLERS, deps) {
    const buildCommand = deps.buildCommand;
    const execCLI = deps.execCLI;
    const success = deps.success;
    const error = deps.error;

    // ---------- 统一写入流水线 ----------
    // lock -> file(定位+乐观锁基线) -> fs读 -> 纯函数变换 -> fs写(二次校验) -> unlock
    function pipeline(args, label, transform) {
        if (!args.file && !args.path) return error('缺少必需参数: file 或 path');

        const info = IO.fileInfo(execCLI, buildCommand, args);
        if (!info.success) {
            return error('无法定位笔记: ' + info.output +
                '\n提示: file= 按笔记名解析(类似 wikilink), path= 为精确相对路径。');
        }

        let handle;
        try { handle = L.acquire(info.relPath); }
        catch (e) { return error(e.message); }

        try {
            const rd = IO.readFs(execCLI, buildCommand, args, info.relPath);
            if (!rd.success) return error('读取笔记失败: ' + rd.output);

            const res = transform(rd.text);
            if (res.error) return error(res.error);

            const wr = IO.writeBack(execCLI, buildCommand, args, info.relPath, info.modified, res.content);
            if (!wr.success) {
                return error(wr.output +
                    '\n如需查看历史版本: obsidian history path=' + info.relPath);
            }

            // 写入类命令不返回审计表: Agent 刚刚指定了 tag, 知道自己改了什么;
            // 需要全图时可随时 node_read mode=tags 兜底。
            return success(label + '  |  ' + info.relPath + '  |  ' + wr.bytes + ' 字节'
                + (wr.warn || ''));
        } finally {
            L.release(handle);
        }
    }

    Object.assign(HANDLERS, {

        // ===== 1. 白板落笔 =====
        node_create: function (args) {
            if (!args.name && !args.path) return error('缺少必需参数: name 或 path');
            if (args.template) {
                return error('node_create 暂不支持 template 参数(模板内容与节点转译的合并顺序尚未定义)。' +
                    '如需模板, 请先用 create 命令建立笔记, 再用 node_add 添加节点。');
            }

            // 纯函数先行: 转译失败则完全不碰文件系统
            const tr = T.transpileCreate(args.content === undefined ? '' : String(args.content), args.tags);
            if (tr.error) return error(tr.error);

            let relPath;
            if (args.path) {
                relPath = String(args.path).replace(/\.md$/i, '') + '.md';
            } else {
                const base = String(args.name).replace(/\.md$/i, '');
                relPath = args.folder
                    ? String(args.folder).replace(/[\/\\]+$/, '') + '/' + base + '.md'
                    : base + '.md';
            }

            // 建档与写正文合为一次 CLI 调用，与原有 create 命令同一通道
            let handle;
            try { handle = L.acquire(relPath); }
            catch (e) { return error(e.message); }
            try {
                const wr = IO.writeNew(execCLI, buildCommand, args, relPath, tr.content, !!args.overwrite);
                if (!wr.success) return error('创建笔记失败: ' + wr.output);
                // 审计表基于落盘实际内容, 而非预期内容
                const post = T.scanNodes(wr.actual || tr.content);
                const audit = post.errors.length
                    ? tr.audit + '\n\n[警示] 落盘后锚点结构异常: ' + post.errors.join('; ')
                    : T.buildAudit(post.nodes, '本次转译 ' + tr.pairCount + ' 对');
                return success('笔记 "' + relPath + '" 创建成功  |  ' + wr.bytes + ' 字节\n\n'
                    + audit + (wr.warn || ''));
            } finally {
                L.release(handle);
            }
        },

        // ===== 2. 唯一的模糊操作: 文本空间 -> 锚点空间的渡口 =====
        node_add: function (args) {
            if (!args.target) return error('缺少必需参数: target(要包成节点的原文, 需逐字复制)');
            if (!args.tag) return error('缺少必需参数: tag');
            return pipeline(args, '已添加节点 "' + args.tag + '"', function (text) {
                return T.wrapTarget(text, args.target, args.tag);
            });
        },

        // ===== 3-5. tag 寻址, 全部无歧义 =====
        node_text_replace: function (args) {
            if (!args.tag) return error('缺少必需参数: tag');
            if (args.content === undefined || args.content === null) return error('缺少必需参数: content');
            return pipeline(args, '已替换节点 "' + args.tag + '" 的正文', function (text) {
                return T.replaceBody(text, args.tag, args.content);
            });
        },

        node_text_delete: function (args) {
            if (!args.tag) return error('缺少必需参数: tag');
            return pipeline(args, '已清空节点 "' + args.tag + '" 的正文（锚点保留，可继续 node_delete 拆除）', function (text) {
                return T.clearBody(text, args.tag);
            });
        },

        node_delete: function (args) {
            if (!args.tag) return error('缺少必需参数: tag');
            return pipeline(args, '已拆除节点 "' + args.tag + '" 的锚点', function (text) {
                return T.unwrapNode(text, args.tag);
            });
        },

        // ===== 6. 三模式读取 =====
        node_read: function (args) {
            if (!args.file && !args.path) return error('缺少必需参数: file 或 path');
            if (!args.mode) {
                return error('缺少必需参数: mode。必须为 full / tags / node 之一。' +
                    '\n  full = 整篇正文(锚点转为 [node-tag:xxx] 可读形式)' +
                    '\n  tags = 仅节点清单(审计表)' +
                    '\n  node = 指定 tag 的节点正文(需同时给 tag 参数)');
            }

            const info = IO.fileInfo(execCLI, buildCommand, args);
            if (!info.success) return error('无法定位笔记: ' + info.output);

            const rd = IO.readFs(execCLI, buildCommand, args, info.relPath);
            if (!rd.success) return error('读取笔记失败: ' + rd.output);

            const v = T.readView(rd.text, args.mode, args.tag);
            if (v.error) return error(v.error);

            let head;
            if (args.mode === 'full') head = '笔记全文 [' + info.relPath + ']  节点数 ' + v.nodeCount;
            else if (args.mode === 'tags') head = '节点清单 [' + info.relPath + ']';
            else head = '节点正文 [' + info.relPath + ' :: ' + args.tag + ']';

            return success(head + '\n\n' + v.text);
        }
    });

    // 连字符别名: 指向同一 handler, 兼容 node-add 一类写法
    const aliases = ['node_create', 'node_add', 'node_text_replace', 'node_text_delete', 'node_delete', 'node_read'];
    aliases.forEach(function (k) {
        HANDLERS[k.replace(/_/g, '-')] = HANDLERS[k];
    });
}

module.exports = { register };
