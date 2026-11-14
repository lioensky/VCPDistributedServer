'use strict';

/**
 * Plugin/VCPKnowledge/VCPKnowledge.js
 *
 * 🧭 VCP 全域冷知识库雷达与按需查阅插件 v2.6.0 (Flagship Universal Edition / RiverMemo CSR Topology)
 *
 * 核心特性：
 * 1. 单一占位符联通全部 TriviumDB 冷知识库；
 * 2. 全链路七大变量免疫架构：
 *    - 向量分布自适应（Z-Score + MAD/IQR 鲁棒校准 + 小样本库 N<15 先验退火 + 维度切换自愈）；
 *    - 双引擎路由卡片生成（.epub/Markdown 章节骨架 + 全文五段等距采样 + 可选轻量模型高密度语义提炼）；
 *    - 查询词长亚线性饱和归一化 + 元对话泛词过滤（根治长句/泛技术词累加误触）；
 *    - 跨语种文档自适应放行（中文提问查英文原版书免受中文词法门槛误拦）；
 *    - L0（静默省流）/ L1（章节坐标）/ L2（高置信焦点原文限长直通）三级自适应门控；
 * 3. 上下双路融合路由（Top-Down 目录路由 + Bottom-Up TriviumDB 深层 Chunk 探针反哺）；
 * 4. 零主程序侵入自挂载（_ensureRuntimeHooks）+ 查询向量缓存 Key 对齐 + 群聊整轮 LRU 缓存。
 */

const fsp = require('fs').promises;
const path = require('path');
const crypto = require('crypto');
const { chunkText } = require('../../TextChunker');
const { getEmbeddingsBatch } = require('../../EmbeddingUtils');
const { readTextFile, loadChapters } = require('../../modules/knowledgeBase/ingestionPipeline');

const UNIFIED_PLACEHOLDER_REGEX = new RegExp(
    '(?:\\[\\[(?:VCP|全域)?知识库([^\\]]*)\\]\\]|<<(?:VCP|全域)?知识库([^>]*)>>|\\{\\{(?:VCP|全域)?知识库([^}]*)\\}\\})',
    'g'
);

const TRIVIAL_QUERY_REGEX = /^(你好|您好|嗨|hello|hi|谢谢|多谢|晚安|早安|早上好|中午好|下午好|晚上好|在吗|好的|嗯|哦|ok|okay|继续|明白|收到|原来如此|哈哈|哈哈哈)[\s!！。.？?~～]*$/i;

// 仅过滤通用现代汉语语法虚词、人称/指示代词、疑问词与连词，绝不屏蔽任何技术或领域实义名词
const CJK_GRAMMAR_STOPWORDS_RAW =
    '我们|你们|他们|它们|什么|怎么|如何|为什么|为什|可以|能够|应该|需要|有没有|有没|没有|是不是|是不|' +
    '一个|一些|一下|一样|一直|一起|这个|那个|这些|那些|这样|那样|这里|那里|现在|时候|因为|所以|如果|' +
    '但是|而且|或者|虽然|然后|就是|还是|只是|不是|已经|开始|继续|进行|使用|通过|关于|对于|根据|问题|' +
    '情况|东西|事情|地方|部分|内容|方式|方法|结果|觉得|知道|看到|告诉|帮我|请问|能不能|能不|好吗|行的|' +
    '的话|其他|再来|看看|刚才|之前|之后|里面|记得|都能|相似|类似|还有|多少|影响|也是|一种|各种|已有|' +
    '完成|最后|一次|再做|说错|重新|回答|检查';
const CJK_STOP_BIGRAMS = new Set(CJK_GRAMMAR_STOPWORDS_RAW.split('|'));

// 默认保持零硬编码业务词表；特定书名/专名统一由路由卡片自动提取或用户在 config.env 的 CUSTOM_LIBRARY_ALIASES 中配置
const DEFAULT_LIBRARY_ALIASES = {};

function toNormalizedFloat32(vec) {
    if (!Array.isArray(vec) && !ArrayBuffer.isView(vec)) return null;
    const len = vec.length;
    if (!len) return null;
    const out = new Float32Array(len);
    let sumSq = 0;
    for (let i = 0; i < len; i++) {
        const v = Number(vec[i]) || 0;
        out[i] = v;
        sumSq += v * v;
    }
    const norm = Math.sqrt(sumSq);
    if (norm > 1e-12) {
        const inv = 1 / norm;
        for (let i = 0; i < len; i++) out[i] *= inv;
    }
    return out;
}

function dotProductUnit(a, b) {
    if (!a || !b || a.length !== b.length) return 0;
    let s = 0;
    const len = a.length;
    for (let i = 0; i < len; i++) s += a[i] * b[i];
    return s;
}

function parseFiniteInt(val, fallback) {
    const n = parseInt(val, 10);
    return Number.isFinite(n) && n > 0 ? n : fallback;
}

function parseFiniteFloat(val, fallback) {
    const n = parseFloat(val);
    return Number.isFinite(n) && n >= 0 ? n : fallback;
}

class VCPKnowledgePlugin {
    constructor() {
        this.config = {
            RADAR_TOP_DOCS: 5,
            RADAR_PINPOINT_CHUNKS: 2,
            RADAR_SNIPPET_CHARS: 110,
            RADAR_MIN_SCORE: 0.48,
            RADAR_INLINE_SCORE: 0.65,
            AUTO_SYNC_BATCH_SIZE: 12,
            AUTO_LLM_SUMMARY: true,
            ROUTER_SUMMARY_MODEL: '',
            CUSTOM_LIBRARY_ALIASES: '',
            TOPOLOGY_PROPAGATION: true,
            TOPOLOGY_PATH_BONUS_MAX: 0.08,
            TOPOLOGY_HEADING_TF_BOOST: 2,
            TOPOLOGY_MAX_CONCEPTS: 24,
            TOPOLOGY_MAX_OUTFLOW: 32,
            TOPOLOGY_SPARSE_TOP_SCORE: 0.60,
            TOPOLOGY_SPARSE_MIN_HITS: 2,
            TOPOLOGY_MAX_OUTFLOW: 32,
            TOPOLOGY_MIN_DF_CAP: 16
        };
        this.tdbKnowledgeManager = null;
        this.pluginManager = null;
        this.vcpLogFunctions = null;

        this._metaCache = { mtimeMs: 0, checkedAt: 0, data: {} };
        this._catalogCache = { mtimeMs: 0, checkedAt: 0, items: {}, unitVectors: new Map(), dim: 0 };
        this._bm25IndexCache = { sig: '', df: new Map(), titleSegDf: new Map(), avgdl: 1, docMap: new Map() };
        this._topologyCache = null;
        this._queryVecCache = new Map();
        this._radarResultCache = new Map();
        this._docChunksCache = new Map();
        this._customAliasesMap = {};
        this._syncingNewDocs = false;
    }

    async initialize(config = {}, dependencies = {}) {
        this.config = {
            ...this.config,
            ...config,
            RADAR_TOP_DOCS: parseFiniteInt(config.RADAR_TOP_DOCS, 5),
            RADAR_PINPOINT_CHUNKS: parseFiniteInt(config.RADAR_PINPOINT_CHUNKS, 2),
            RADAR_SNIPPET_CHARS: parseFiniteInt(config.RADAR_SNIPPET_CHARS, 110),
            RADAR_MIN_SCORE: parseFiniteFloat(config.RADAR_MIN_SCORE, 0.48),
            RADAR_INLINE_SCORE: parseFiniteFloat(config.RADAR_INLINE_SCORE, 0.65),
            AUTO_SYNC_BATCH_SIZE: parseFiniteInt(config.AUTO_SYNC_BATCH_SIZE, 12),
            AUTO_LLM_SUMMARY: String(config.AUTO_LLM_SUMMARY ?? 'true').toLowerCase() !== 'false',
            ROUTER_SUMMARY_MODEL: String(config.ROUTER_SUMMARY_MODEL || process.env.JEV_MODEL || process.env.JevModel || '').trim(),
            CUSTOM_LIBRARY_ALIASES: String(config.CUSTOM_LIBRARY_ALIASES || '').trim(),
            TOPOLOGY_PROPAGATION: String(config.TOPOLOGY_PROPAGATION ?? 'true').toLowerCase() !== 'false',
            TOPOLOGY_PATH_BONUS_MAX: parseFiniteFloat(config.TOPOLOGY_PATH_BONUS_MAX, 0.08),
            TOPOLOGY_HEADING_TF_BOOST: parseFiniteInt(config.TOPOLOGY_HEADING_TF_BOOST, 2),
            TOPOLOGY_MAX_CONCEPTS: parseFiniteInt(config.TOPOLOGY_MAX_CONCEPTS, 24),
            TOPOLOGY_MAX_OUTFLOW: parseFiniteInt(config.TOPOLOGY_MAX_OUTFLOW, 32),
            TOPOLOGY_SPARSE_TOP_SCORE: parseFiniteFloat(config.TOPOLOGY_SPARSE_TOP_SCORE, 0.60),
            TOPOLOGY_SPARSE_MIN_HITS: parseFiniteInt(config.TOPOLOGY_SPARSE_MIN_HITS, 2),
            TOPOLOGY_MAX_OUTFLOW: parseFiniteInt(config.TOPOLOGY_MAX_OUTFLOW, 32),
            TOPOLOGY_MIN_DF_CAP: parseFiniteInt(config.TOPOLOGY_MIN_DF_CAP, 16)
        };
        this._customAliasesMap = this._parseCustomAliases(this.config.CUSTOM_LIBRARY_ALIASES);
        this._radarResultCache.clear();
        this.setDependencies(dependencies);
        this._ensureRuntimeHooks();
        const hookTimer = setImmediate(() => this._ensureRuntimeHooks());
        if (typeof hookTimer?.unref === 'function') hookTimer.unref();
        const tagSample = '[' + '[VCP知识库]' + '] / {' + '{VCP知识库}' + '}';
        console.log(`[VCPKnowledge] 🧭 全域冷知识库雷达 v2.6.0-csr 已就绪 (Unified Placeholder: ${tagSample}, Topology: ${this.config.TOPOLOGY_PROPAGATION ? 'ON' : 'OFF'})`);
    }

    setDependencies(dependencies = {}) {
        if (dependencies.pluginManager) this.pluginManager = dependencies.pluginManager;
        if (dependencies.tdbKnowledgeManager) {
            this.tdbKnowledgeManager = dependencies.tdbKnowledgeManager;
        } else if (this.pluginManager?.tdbKnowledgeManager) {
            this.tdbKnowledgeManager = this.pluginManager.tdbKnowledgeManager;
        }
        if (dependencies.vcpLogFunctions) {
            this.vcpLogFunctions = dependencies.vcpLogFunctions;
        } else if (this.pluginManager?.getVCPLogFunctions) {
            this.vcpLogFunctions = this.pluginManager.getVCPLogFunctions();
        }
    }

    _ensureRuntimeHooks() {
        try {
            const pm = this.pluginManager;
            if (pm) {
                if (Array.isArray(pm.preprocessorOrder)) {
                    const ragIdx = pm.preprocessorOrder.indexOf('RAGDiaryPlugin');
                    const myIdx = pm.preprocessorOrder.indexOf('VCPKnowledge');
                    if (ragIdx !== -1 && (myIdx === -1 || myIdx > ragIdx)) {
                        if (myIdx !== -1) pm.preprocessorOrder.splice(myIdx, 1);
                        const newRagIdx = pm.preprocessorOrder.indexOf('RAGDiaryPlugin');
                        pm.preprocessorOrder.splice(newRagIdx, 0, 'VCPKnowledge');
                    }
                }
                if (pm.messagePreprocessors instanceof Map && pm.messagePreprocessors.has('RAGDiaryPlugin') && pm.messagePreprocessors.has('VCPKnowledge')) {
                    const keys = Array.from(pm.messagePreprocessors.keys());
                    const ragIdx = keys.indexOf('RAGDiaryPlugin');
                    const myIdx = keys.indexOf('VCPKnowledge');
                    if (myIdx > ragIdx) {
                        const entries = Array.from(pm.messagePreprocessors.entries());
                        const [myEntry] = entries.splice(myIdx, 1);
                        const targetIdx = entries.findIndex(([k]) => k === 'RAGDiaryPlugin');
                        entries.splice(targetIdx, 0, myEntry);
                        pm.messagePreprocessors.clear();
                        for (const [k, v] of entries) pm.messagePreprocessors.set(k, v);
                    }
                }
            }

            const patchProcessorProto = (proto) => {
                if (!proto || proto._vcpKnowledgeHooked) return;
                const origFn = proto.isDiaryPlaceholderAmbiguity;
                proto.isDiaryPlaceholderAmbiguity = function (rawName, modifiers) {
                    const nameTrimmed = String(rawName || '').trim();
                    if (!nameTrimmed || /^(?:VCP|全域)$/i.test(nameTrimmed)) return true;
                    return typeof origFn === 'function' ? origFn.call(this, rawName, modifiers) : false;
                };
                proto._vcpKnowledgeHooked = true;
            };

            const ragPlugin = this._getRagPlugin();
            if (ragPlugin?.tdbProcessor) {
                patchProcessorProto(Object.getPrototypeOf(ragPlugin.tdbProcessor));
            } else {
                try {
                    const TDBPlaceholderProcessor = require('../RAGDiaryPlugin/TDBPlaceholderProcessor');
                    if (TDBPlaceholderProcessor?.prototype) patchProcessorProto(TDBPlaceholderProcessor.prototype);
                } catch (_) {}
            }
        } catch (_) {}
    }

    _parseCustomAliases(rawConfig) {
        const str = String(rawConfig || '').trim();
        if (!str) return {};
        if (str.startsWith('{')) {
            try {
                const parsed = JSON.parse(str);
                if (parsed && typeof parsed === 'object') return parsed;
            } catch (_) {}
        }
        const result = {};
        for (const entry of str.split(/[;\n]+/).map(s => s.trim()).filter(Boolean)) {
            const sepIdx = entry.search(/[:：]/);
            if (sepIdx <= 0) continue;
            const libName = entry.slice(0, sepIdx).trim();
            const words = entry.slice(sepIdx + 1).split(/[,，|]+/).map(w => w.trim().toLowerCase()).filter(Boolean);
            if (libName && words.length > 0) result[libName] = words;
        }
        return result;
    }

    _buildEffectiveAliases(libraryNames = []) {
        const merged = {};
        for (const [lib, words] of Object.entries(DEFAULT_LIBRARY_ALIASES)) {
            merged[lib] = [...words];
        }
        for (const [lib, words] of Object.entries(this._customAliasesMap || {})) {
            merged[lib] = [...new Set([...(merged[lib] || []), ...words.map(w => String(w).toLowerCase())])];
        }
        for (const libName of libraryNames) {
            const lower = String(libName || '').trim().toLowerCase();
            if (!lower) continue;
            const autoWords = [lower];
            const stripped = lower.replace(/(?:个人)?(?:知识库|资料库|设定集|百科全书|百科|文库|手册|方法论)$/g, '').trim();
            if (stripped.length >= 2 && stripped !== lower && !/^(?:vcp|ai|db|kb)$/i.test(stripped)) autoWords.push(stripped);
            merged[libName] = [...new Set([...(merged[libName] || []), ...autoWords])];
        }
        return merged;
    }

    _getTdbManager() {
        if (this.tdbKnowledgeManager?.initialized) return this.tdbKnowledgeManager;
        if (this.pluginManager?.tdbKnowledgeManager?.initialized) {
            this.tdbKnowledgeManager = this.pluginManager.tdbKnowledgeManager;
            return this.tdbKnowledgeManager;
        }
        try {
            const singleton = require('../../TDBKnowledge.js');
            if (singleton && singleton.initialized) {
                this.tdbKnowledgeManager = singleton;
                return singleton;
            }
        } catch (_) {}
        return null;
    }

    _getRagPlugin() {
        return this.pluginManager?.messagePreprocessors?.get?.('RAGDiaryPlugin') || null;
    }

    async _getRouterMeta(storePath) {
        if (!storePath) return {};
        const now = Date.now();
        if (this._metaCache.mtimeMs > 0 && (now - this._metaCache.checkedAt < 5000)) {
            return this._metaCache.data;
        }
        const file = path.join(storePath, 'tdb_router_meta.json');
        try {
            const st = await fsp.stat(file);
            this._metaCache.checkedAt = now;
            if (st.mtimeMs === this._metaCache.mtimeMs && this._metaCache.data) {
                return this._metaCache.data;
            }
            const data = JSON.parse(await fsp.readFile(file, 'utf8'));
            this._metaCache = { mtimeMs: st.mtimeMs, checkedAt: now, data };
            return data;
        } catch (_) {
            return this._metaCache.data || {};
        }
    }

    async _getRouterCatalog(storePath) {
        if (!storePath) return { items: {}, unitVectors: new Map(), dim: 0 };
        const now = Date.now();
        if (this._catalogCache.mtimeMs > 0 && (now - this._catalogCache.checkedAt < 5000)) {
            return this._catalogCache;
        }
        const file = path.join(storePath, 'tdb_router_catalog.json');
        try {
            const st = await fsp.stat(file);
            this._catalogCache.checkedAt = now;
            if (st.mtimeMs === this._catalogCache.mtimeMs && this._catalogCache.unitVectors.size > 0) {
                return this._catalogCache;
            }
            const parsed = JSON.parse(await fsp.readFile(file, 'utf8'));
            const items = (parsed && parsed.items && typeof parsed.items === 'object') ? parsed.items : {};
            const unitVectors = new Map();
            let detectedDim = 0;
            for (const [k, v] of Object.entries(items)) {
                if (Array.isArray(v?.vector) && v.vector.length > 0) {
                    const u = toNormalizedFloat32(v.vector);
                    if (u) {
                        unitVectors.set(k, u);
                        detectedDim = u.length;
                    }
                }
            }
            this._catalogCache = { mtimeMs: st.mtimeMs, checkedAt: now, items, unitVectors, dim: detectedDim };
            return this._catalogCache;
        } catch (_) {
            return this._catalogCache;
        }
    }

    _buildTopologyCSR(indexSig, bm25) {
        // 扩库三步合一：①分库共现分片 ②自适应概念粒度+固定出流预算 ③CSR 压缩（RiverMemo 规模化纪律）
        const t0 = Date.now();
        const N = bm25.docMap.size || 1;
        const minDf = Math.max(2, Math.min(this.config.TOPOLOGY_MIN_DF_CAP || 16, Math.floor(Math.sqrt(N / 50))));
        const maxDf = Math.max(minDf + 1, Math.ceil(N * 0.35));
        const maxIdf = Math.log(1 + N / minDf) || 1;
        const topConcepts = Math.max(4, this.config.TOPOLOGY_MAX_CONCEPTS || 24);
        const outflow = Math.max(4, this.config.TOPOLOGY_MAX_OUTFLOW || 32);

        // 1) 每篇文档概念集：全局 df 窗口 + IDF Top-N（与 v2.5 同口径）
        const conceptIndex = new Map();
        const conceptNames = [];
        const docConcepts = new Map();
        for (const [key, d] of bm25.docMap) {
            const candArr = [];
            for (const t of d.tf.keys()) {
                const dfT = bm25.df.get(t) || 0;
                if (t.length < 2 || dfT < minDf || dfT > maxDf) continue;
                candArr.push([t, Math.log(1 + N / dfT)]);
            }
            candArr.sort((a, b) => b[1] - a[1]);
            const ids = [];
            for (let i = 0; i < candArr.length && ids.length < topConcepts; i++) {
                let id = conceptIndex.get(candArr[i][0]);
                if (id === undefined) { id = conceptNames.length; conceptIndex.set(candArr[i][0], id); conceptNames.push(candArr[i][0]); }
                ids.push(id);
            }
            if (ids.length > 0) docConcepts.set(key, ids);
        }
        const C = conceptNames.length;

        // 2) 分库共现分片：库内配对计数；权重 = 库内共现 / 概念全局df（有界[0,1]，跨库求和=全局权重）
        const libIds = new Map();
        const libPairCo = [];
        for (const [key, ids] of docConcepts) {
            const libName = key.slice(0, key.indexOf('\u0000'));
            let libId = libIds.get(libName);
            if (libId === undefined) { libId = libIds.size; libIds.set(libName, libId); libPairCo.push(new Map()); }
            const co = libPairCo[libId];
            const uniq = [...new Set(ids)];
            for (let i = 0; i < uniq.length; i++) {
                for (let j = i + 1; j < uniq.length; j++) {
                    const a = Math.min(uniq[i], uniq[j]), b = Math.max(uniq[i], uniq[j]);
                    const pid = a * C + b;
                    co.set(pid, (co.get(pid) || 0) + 1);
                }
            }
        }

        // 3) 出流预算归并：每概念仅保留权重 Top-K 邻居（内存硬上限 = C × K）
        const adj = new Array(C);
        for (let libId = 0; libId < libPairCo.length; libId++) {
            for (const [pid, co] of libPairCo[libId]) {
                const a = Math.floor(pid / C), b = pid - a * C;
                const dfA = Math.max(1, bm25.df.get(conceptNames[a]) || 1);
                const dfB = Math.max(1, bm25.df.get(conceptNames[b]) || 1);
                (adj[a] || (adj[a] = [])).push([b, Math.min(1, co / dfA)]);
                (adj[b] || (adj[b] = [])).push([a, Math.min(1, co / dfB)]);
            }
        }
        const offsets = new Uint32Array(C + 1);
        const kept = new Array(C);
        let totalEdges = 0;
        for (let c = 0; c < C; c++) {
            const list = adj[c];
            if (list && list.length > outflow) {
                list.sort((x, y) => y[1] - x[1]);
                kept[c] = list.slice(0, outflow);
            } else {
                kept[c] = list || null;
            }
            totalEdges += kept[c] ? kept[c].length : 0;
            offsets[c + 1] = totalEdges;
        }
        const neighborIdx = new Uint32Array(totalEdges);
        const edgeW = new Float32Array(totalEdges);
        let p = 0;
        for (let c = 0; c < C; c++) {
            const list = kept[c];
            if (list) for (const [n, w] of list) { neighborIdx[p] = n; edgeW[p] = w; p++; }
            adj[c] = null; kept[c] = null;
        }

        // 4) conceptDocs CSR：概念 → 文档索引（全域，跨库桥接不受分库限制）
        const docKeys = [...bm25.docMap.keys()];
        const docKeyIdx = new Map();
        docKeys.forEach((k, i) => docKeyIdx.set(k, i));
        const cDocLists = new Array(C);
        for (const [key, ids] of docConcepts) {
            const di = docKeyIdx.get(key);
            for (const id of new Set(ids)) (cDocLists[id] || (cDocLists[id] = [])).push(di);
        }
        const docOffsets = new Uint32Array(C + 1);
        let totalCD = 0;
        for (let c = 0; c < C; c++) { totalCD += cDocLists[c] ? cDocLists[c].length : 0; docOffsets[c + 1] = totalCD; }
        const docIdxArr = new Uint32Array(totalCD);
        p = 0;
        for (let c = 0; c < C; c++) {
            const list = cDocLists[c];
            if (list) for (const di of list) docIdxArr[p++] = di;
            cDocLists[c] = null;
        }

        // 5) IDF 向量（全局 df 口径，与 v2.5 一致）
        const idfArr = new Float32Array(C);
        for (let c = 0; c < C; c++) idfArr[c] = Math.log(1 + N / Math.max(1, bm25.df.get(conceptNames[c]) || 1));

        const stats = { N, C, totalEdges, conceptDocEntries: totalCD, libs: libIds.size, minDf, maxDf, outflow, libEdgeCounts: libPairCo.map(m => m.size), buildMs: Date.now() - t0 };
        console.log(`[VCPKnowledge] 🗺️ 拓扑CSR重建: docs=${N} libs=${stats.libs} concepts=${C} edges=${totalEdges} (出流≤${outflow}, df∈[${minDf},${maxDf}]) ${stats.buildMs}ms`);
        return { sig: indexSig, conceptIndex, conceptNames, docKeys, docKeyIdx, offsets, neighborIdx, edgeW, docOffsets, docIdxArr, idfArr, maxIdf, stats };
    }

    _lookupDocMeta(meta, doc) {
        if (!meta || !doc) return {};
        const fullPath = String(doc.path || '');
        const libPrefixBs = `${doc.library}\\`;
        const libPrefixFs = `${doc.library}/`;
        const shortPath = fullPath.startsWith(libPrefixBs)
            ? fullPath.slice(libPrefixBs.length)
            : (fullPath.startsWith(libPrefixFs) ? fullPath.slice(libPrefixFs.length) : fullPath);
        const normFull = fullPath.split(path.sep).join('/');
        const normShort = shortPath.split(path.sep).join('/');

        return (
            meta[`${doc.library}\u0000${fullPath}`] ||
            meta[`${doc.library}\u0000${shortPath}`] ||
            meta[fullPath] ||
            meta[shortPath] ||
            meta[normFull] ||
            meta[normShort] ||
            meta[`${doc.library}/${normShort}`] ||
            {}
        );
    }

    _extractStructuralSkeleton(rawText, epubHeadings = []) {
        const cleanedText = String(rawText || '')
            .replace(/^\[20\d{2}-\d{2}-\d{2}\]\s*-\s*[^\r\n]+\r?\n?/gm, '')
            .trim();

        let allHeadings = (epubHeadings || [])
            .map(h => String(h || '').trim())
            .filter(h => h.length >= 2 && h.length <= 72 && !/^(?:目录|封面|版权|扉页|contents|cover|copyright)$/i.test(h));

        if (allHeadings.length === 0) {
            const majorHeadings = [];
            const minorHeadings = [];
            for (const line of cleanedText.split(/\r?\n/)) {
                const trimmed = line.trim();
                if (!trimmed || trimmed.length > 80) continue;
                const isMajor = /^(#{1,2}\s+.+|第[一二三四五六七八九十百千万0-9]+[章节篇部卷回]\s*.+|[一二三四五六七八九十]+、\s*.+|\d+\.\s+[^\d].{2,50})$/.test(trimmed);
                const isMinor = !isMajor && /^(#{3,4}\s+.+|\d+\.\d+\s+[^\d].{2,50})$/.test(trimmed);
                if (isMajor || isMinor) {
                    const cleanH = trimmed.replace(/^#+\s*/, '').trim();
                    if (/^\d+(?:\.\d+)?\s*(?:gb|mb|kb|gib|mib|tb|%|px|ms|s)$/i.test(cleanH)) continue;
                    if (cleanH.length >= 2 && cleanH.length <= 68) {
                        if (isMajor && !majorHeadings.includes(cleanH)) majorHeadings.push(cleanH);
                        else if (isMinor && !minorHeadings.includes(cleanH)) minorHeadings.push(cleanH);
                    }
                }
            }
            const maxMajor = 14;
            const sampledMajor = majorHeadings.length <= maxMajor
                ? majorHeadings
                : Array.from({ length: maxMajor }, (_, i) => majorHeadings[Math.min(majorHeadings.length - 1, Math.round((i * (majorHeadings.length - 1)) / (maxMajor - 1)))]);
            const remainingSlots = Math.max(0, 28 - sampledMajor.length);
            const sampledMinor = minorHeadings.length <= remainingSlots
                ? minorHeadings
                : Array.from({ length: remainingSlots }, (_, i) => minorHeadings[Math.min(minorHeadings.length - 1, Math.round((i * (minorHeadings.length - 1)) / Math.max(1, remainingSlots - 1)))]);
            allHeadings = [...new Set([...sampledMajor, ...sampledMinor])];
        }

        const maxHeadings = 28;
        let headings = [];
        if (allHeadings.length <= maxHeadings) {
            headings = allHeadings;
        } else {
            for (let i = 0; i < maxHeadings; i++) {
                const idx = Math.min(allHeadings.length - 1, Math.round((i * (allHeadings.length - 1)) / (maxHeadings - 1)));
                if (!headings.includes(allHeadings[idx])) headings.push(allHeadings[idx]);
            }
        }

        const flat = cleanedText.replace(/\s+/g, ' ').trim();
        let multiSample = '';
        if (flat.length <= 1800) {
            multiSample = flat;
        } else {
            const positions = [0.02, 0.15, 0.28, 0.41, 0.54, 0.67, 0.80, 0.92];
            const segLen = 82;
            multiSample = positions.map(p => {
                const start = Math.floor(flat.length * p);
                return flat.slice(start, start + segLen);
            }).join(' … ');
        }

        return { headings, multiSample, firstSnippet: flat.slice(0, 420) };
    }

    async _distillSummaryViaLLM(manager, doc, headings, multiSample) {
        const model = this.config.ROUTER_SUMMARY_MODEL || process.env.JEV_MODEL || process.env.JevModel || '';
        if (!this.config.AUTO_LLM_SUMMARY || !model || !manager?.config?.apiUrl || !manager?.config?.apiKey) {
            return null;
        }
        try {
            const prompt = [
                '你是一个专业知识库路由索引提炼器。请根据以下文档的标题、章节目录和五段等距采样，输出一个高信息密度的 JSON 路由卡片。',
                '要求：',
                '1. "summary": 100~160字的高浓度中文语义提要（直接陈述核心概念、关键实体、解决的问题与方法论；若是英文书籍请用中文提炼核心理论并保留关键英文术语）。',
                '2. "tags": 8~12个高区分度检索标签数组。',
                '只输出合法 JSON 对象：{"summary":"...","tags":["..."]}',
                `【所属知识库】：${doc.library}`,
                `【文档标题】：${doc.title}`,
                `【章节目录】：${headings.join(' | ') || '无显式章节标题'}`,
                `【全文五段采样】：${multiSample.slice(0, 2000)}`
            ].join('\n');

            const res = await fetch(`${manager.config.apiUrl}/v1/chat/completions`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${manager.config.apiKey}`
                },
                body: JSON.stringify({
                    model,
                    messages: [{ role: 'user', content: prompt }],
                    temperature: 0.1,
                    max_tokens: 600,
                    enable_thinking: false
                })
            });
            if (!res.ok) return null;
            const data = await res.json();
            const content = String(data.choices?.[0]?.message?.content || '').trim();
            const m = content.match(/\{[\s\S]*\}/);
            if (!m) return null;
            const parsed = JSON.parse(m[0]);
            if (!parsed.summary) return null;
            return {
                summary: String(parsed.summary).trim(),
                tags: Array.isArray(parsed.tags) ? parsed.tags.map(t => String(t).trim()).filter(Boolean) : []
            };
        } catch (_) {
            return null;
        }
    }

    _stripLibraryPrefix(library, rawPath) {
        const p = String(rawPath || '');
        const pBs = `${library}\\`;
        const pFs = `${library}/`;
        if (p.startsWith(pBs)) return p.slice(pBs.length);
        if (p.startsWith(pFs)) return p.slice(pFs.length);
        return p;
    }

    _lookupCatalogUnitVec(catalogCache, doc) {
        if (!catalogCache?.unitVectors || !doc) return null;
        const shortPath = this._stripLibraryPrefix(doc.library, doc.path);
        return (
            catalogCache.unitVectors.get(`${doc.library}\u0000${shortPath}`) ||
            catalogCache.unitVectors.get(`${doc.library}\u0000${doc.path}`) ||
            catalogCache.unitVectors.get(`${doc.library}\u0000${doc.library}\\${shortPath}`) ||
            null
        );
    }

    async _autoSyncNewDocuments(manager, allDocs, meta, catalogCache, storePath, activeQueryDim = 0) {
        if (!storePath || !Array.isArray(allDocs) || allDocs.length === 0) return;
        if (this._syncingNewDocs) return;

        const catalogItems = catalogCache.items || {};
        const expectedDim = activeQueryDim || manager.config?.dimension || 0;

        const missing = allDocs.filter(doc => {
            const shortPath = this._stripLibraryPrefix(doc.library, doc.path);
            const metaEntry = this._lookupDocMeta(meta, doc);
            const hasMeta = Boolean(metaEntry?.description);
            const catEntry = catalogItems[`${doc.library}\u0000${shortPath}`]
                || catalogItems[`${doc.library}\u0000${doc.path}`]
                || catalogItems[`${doc.library}\u0000${doc.library}\\${shortPath}`];
            const vec = catEntry?.vector;
            const hasValidVec = Array.isArray(vec) && vec.length > 0 && (!expectedDim || vec.length === expectedDim);
            const cardTimeMs = Number(catEntry?.docMtime || metaEntry?.docMtime || catEntry?.updatedAt || (metaEntry?.updatedAt ? Date.parse(metaEntry.updatedAt) : 0)) || 0;
            const isStaleMtime = Boolean(doc.mtime && cardTimeMs > 0 && doc.mtime > cardTimeMs + 2000);
            return !hasMeta || !hasValidVec || isStaleMtime;
        });

        if (missing.length === 0) return;

        this._syncingNewDocs = true;
        try {
            const batchSize = Math.max(1, this.config.AUTO_SYNC_BATCH_SIZE || 12);
            const batch = missing.slice(0, batchSize);
            const textsToEmbed = [];
            const batchRecords = [];
            let metaChanged = false;

            for (const doc of batch) {
                const shortPath = this._stripLibraryPrefix(doc.library, doc.path);
                const key = `${doc.library}\u0000${shortPath}`;
                const metaEntry = this._lookupDocMeta(meta, doc);
                const catEntry = catalogItems[key] || catalogItems[`${doc.library}\u0000${doc.path}`] || catalogItems[`${doc.library}\u0000${doc.library}\\${shortPath}`];
                const cardTimeMs = Number(catEntry?.docMtime || metaEntry?.docMtime || catEntry?.updatedAt || (metaEntry?.updatedAt ? Date.parse(metaEntry.updatedAt) : 0)) || 0;
                const isStaleMtime = Boolean(doc.mtime && cardTimeMs > 0 && doc.mtime > cardTimeMs + 2000);
                let existingDesc = isStaleMtime ? '' : String(metaEntry.description || '').trim();
                let existingTags = (!isStaleMtime && Array.isArray(metaEntry.tags) && metaEntry.tags.length > 0)
                    ? metaEntry.tags
                    : [doc.library, doc.title];

                if (!existingDesc) {
                    try {
                        const absPath = path.join(manager.config.rootPath, doc.library, shortPath);
                        const chaps = typeof loadChapters === 'function' ? await loadChapters(absPath).catch(() => []) : [];
                        const epubHeadings = Array.isArray(chaps) && chaps.length > 0
                            ? chaps.map(c => c.title).filter(Boolean)
                            : [];
                        const rawText = await readTextFile(absPath);
                        const { headings, multiSample, firstSnippet } = this._extractStructuralSkeleton(rawText, epubHeadings);
                        const distilled = await this._distillSummaryViaLLM(manager, doc, headings, multiSample);
                        const tocPart = headings.length > 0 ? `[核心目录] ${headings.slice(0, 20).join(' | ')}\n` : '';
                        const summaryPart = distilled?.summary
                            ? `[语义提要] ${distilled.summary}\n[路由摘要] ${multiSample.slice(0, 560) || firstSnippet}`
                            : `[路由摘要] ${multiSample.slice(0, 650) || firstSnippet}`;
                        existingDesc = `${tocPart}${summaryPart}`.trim();
                        existingTags = [...new Set([
                            doc.library,
                            doc.title,
                            ...(distilled?.tags || []),
                            ...headings.slice(0, 18)
                        ])].filter(Boolean).slice(0, 24);

                        const rec = {
                            library: doc.library,
                            path: shortPath,
                            title: doc.title,
                            tags: existingTags,
                            description: existingDesc,
                            docMtime: doc.mtime || Date.now(),
                            updatedAt: new Date().toISOString()
                        };
                        meta[key] = rec;
                        meta[`${doc.library}\u0000${doc.library}\\${shortPath}`] = rec;
                        metaChanged = true;
                    } catch (_) {
                        existingDesc = `${doc.library} ${doc.title}`;
                    }
                }

                const embedInput = `知识库:${doc.library}\n标题:${doc.title}\n路径:${shortPath}\n标签:${(existingTags || []).join(', ')}\n${existingDesc}`.slice(0, 1350);
                textsToEmbed.push(embedInput);
                batchRecords.push({ doc, shortPath, key, tags: existingTags, description: existingDesc });
            }

            if (metaChanged) {
                await fsp.writeFile(path.join(storePath, 'tdb_router_meta.json'), JSON.stringify(meta, null, 2), 'utf8');
                this._metaCache.checkedAt = 0;
            }

            if (textsToEmbed.length > 0 && manager.config?.apiUrl) {
                const vectors = await getEmbeddingsBatch(textsToEmbed, {
                    apiKey: manager.config.apiKey,
                    apiUrl: manager.config.apiUrl,
                    model: manager.config.model
                });
                let updatedCatalog = false;
                for (let i = 0; i < batchRecords.length; i++) {
                    const vec = vectors?.[i];
                    if (Array.isArray(vec) && vec.length > 0) {
                        const rec = batchRecords[i];
                        const catRecord = {
                            library: rec.doc.library,
                            path: rec.shortPath,
                            title: rec.doc.title,
                            tags: rec.tags,
                            description: rec.description,
                            vector: vec,
                            docMtime: rec.doc.mtime || Date.now(),
                            updatedAt: Date.now()
                        };
                        catalogItems[rec.key] = catRecord;
                        catalogItems[`${rec.doc.library}\u0000${rec.doc.library}\\${rec.shortPath}`] = catRecord;
                        const u = toNormalizedFloat32(vec);
                        if (u) {
                            catalogCache.unitVectors.set(rec.key, u);
                            catalogCache.unitVectors.set(`${rec.doc.library}\u0000${rec.doc.library}\\${rec.shortPath}`, u);
                        }
                        updatedCatalog = true;
                    }
                }

                if (updatedCatalog) {
                    const catFile = path.join(storePath, 'tdb_router_catalog.json');
                    const rawCat = { version: 3, updatedAt: new Date().toISOString(), items: catalogItems };
                    await fsp.writeFile(catFile, JSON.stringify(rawCat), 'utf8');
                    this._catalogCache.checkedAt = 0;
                    if (missing.length > batchSize) {
                        setTimeout(() => {
                            this._autoSyncNewDocuments(manager, allDocs, meta, catalogCache, storePath, expectedDim).catch(() => {});
                        }, 60);
                    }
                }
            }
        } catch (err) {
            console.warn('[VCPKnowledge] 自动增量路由同步跳过:', err.message);
        } finally {
            this._syncingNewDocs = false;
        }
    }

    async _getQueryVector(queryText, manager, embedKeyText = null) {
        const clean = String(embedKeyText || queryText || '').trim();
        if (!clean) return null;

        const ragPlugin = this._getRagPlugin();
        const tdbModel = String(manager?.config?.model || '').trim();
        const ragModel = String(process.env.WhitelistEmbeddingModel || '').trim();
        const canShareRagCache = Boolean(
            ragPlugin &&
            typeof ragPlugin.getSingleEmbeddingCached === 'function' &&
            (!tdbModel || !ragModel || tdbModel === ragModel) &&
            !process.env.WhitelistEmbeddingUrl
        );
        if (canShareRagCache) {
            try {
                const alignedText = typeof ragPlugin.sanitizeForEmbedding === 'function'
                    ? (ragPlugin.sanitizeForEmbedding(clean, 'user') || clean)
                    : clean;
                const vec = await ragPlugin.getSingleEmbeddingCached(alignedText);
                if (Array.isArray(vec) && vec.length > 0) return vec;
            } catch (_) {}
        }

        const hash = crypto.createHash('sha256').update(clean, 'utf8').digest('hex');
        const cached = this._queryVecCache.get(hash);
        if (cached && (Date.now() - cached.at < 15 * 60 * 1000)) {
            return cached.vector;
        }

        if (!manager?.config?.apiUrl) return null;
        try {
            const [vec] = await getEmbeddingsBatch([clean], {
                apiKey: manager.config.apiKey,
                apiUrl: manager.config.apiUrl,
                model: manager.config.model
            });
            if (Array.isArray(vec) && vec.length > 0) {
                this._queryVecCache.set(hash, { vector: vec, at: Date.now() });
                if (this._queryVecCache.size > 256) {
                    this._queryVecCache.delete(this._queryVecCache.keys().next().value);
                }
                return vec;
            }
        } catch (e) {
            console.warn('[VCPKnowledge] Query embedding fallback to lexical-only:', e.message);
        }
        return null;
    }

    _isToolPayloadText(raw) {
        const s = String(raw || '').trim();
        if (!s) return false;
        return (
            s.startsWith('<!-- VCP_TOOL_PAYLOAD -->') ||
            s.includes('<<<[VCP_TOOL_BATCH_START') ||
            s.includes('【工具返回批次开始｜时间：') ||
            s.includes('[[VCP调用结果信息汇总:') ||
            s.startsWith('[系统提示:] 过程结论已记录')
        );
    }

    _isContextCompactionMessage(m, raw = '') {
        if (!m) return false;
        if (m.contextCompaction) return true;
        const s = String(raw || '').trim();
        return s.includes('[VCHAT上下文智能压缩块]') && !s.includes('当前环境时间与天气：');
    }

    _sanitizeQueryText(raw) {
        return String(raw || '')
            .replace(/\[系统提示:\]\s*\[VCHAT上下文智能压缩块\][\s\S]*?\[系统提示:\]/g, ' ')
            .replace(/\[VCHAT上下文智能压缩块\][\s\S]*?<\/context_checkpoint>/g, ' ')
            .replace(/<context_checkpoint>[\s\S]*?<\/context_checkpoint>/g, ' ')
            .replace(/##\s*宿主保留：最新版本日记原文[\s\S]*?\[系统提示:\]/g, ' ')
            .replace(/<!--\s*VCP_TOOL_PAYLOAD\s*-->[\s\S]*$/g, ' ')
            .replace(/<<<\[VCP_TOOL_BATCH_START[^\]]*\]>>>[\s\S]*?<<<\[VCP_TOOL_BATCH_END\]>>>/g, ' ')
            .replace(/\[\[VCP调用结果信息汇总:[\s\S]*?VCP调用结果结束\]\]/g, ' ')
            .replace(/<!--\s*VCP_RAG_BLOCK_START[\s\S]*?VCP_RAG_BLOCK_END\s*-->/g, ' ')
            .replace(/<!--\s*VCP_KNOWLEDGE_RADAR_START[\s\S]*?VCP_KNOWLEDGE_RADAR_END\s*-->/g, ' ')
            .replace(/\[---\s*VCP元思考链[\s\S]*?\[---\s*元思考链结束\s*---\]/g, ' ')
            .replace(/\[系统提示:\]\s*过程结论已记录[^\n]*/g, ' ')
            .replace(/\[系统提示:\]/g, ' ')
            .replace(/\[系统邀请指令:\][^\n]*/g, ' ')
            .replace(/\[系统记忆上下文[^\]]*\][\s\S]*?(?=\n(?:当前环境时间与天气：|[^\n]{2,})|$)/g, ' ')
            .replace(/(?:^|\n)\s*[^\n:：]{0,28}日记本和[^\n:：]{0,28}日记本[:：]\s*/g, '\n')
            .replace(/(?:^|\n)\s*这里是[^\n:：]{0,28}日记本[:：]\s*/g, '\n')
            .replace(/(?:^|\n)\s*这是VCP全域冷知识库雷达[:：]?\s*/g, '\n')
            .replace(/当前环境时间与天气：[^\n]*?现在是\d{1,2}:\d{2}(?::\d{2})?[。.\s]*/g, ' ')
            .replace(/当前环境时间与天气：.*?(\n|$)/g, ' ')
            .replace(/\[附加(?:图片|文件|音频|视频)[:：][^\]]*\]/g, ' ')
            .replace(/\{\{.*?\}\}|\[\[.*?\]\]|<<.*?>>|《《.*?》》/g, ' ')
            .replace(/^[\s。.，,、；;：:！!？?]+/, '')
            .replace(/\s+/g, ' ')
            .trim();
    }

    _extractConversationQuery(messages) {
        if (!Array.isArray(messages)) return { query: '', primaryText: '' };
        const userTexts = [];
        for (let i = messages.length - 1; i >= 0 && userTexts.length < 2; i--) {
            const m = messages[i];
            if (!m || m.role !== 'user') continue;
            let raw = '';
            if (typeof m.content === 'string') {
                raw = m.content;
            } else if (Array.isArray(m.content)) {
                raw = m.content.filter(p => p && p.type === 'text').map(p => p.text).join('\n');
            }
            if (this._isToolPayloadText(raw) || this._isContextCompactionMessage(m, raw)) continue;
            const clean = this._sanitizeQueryText(raw);
            if (clean) userTexts.push(clean);
        }
        if (userTexts.length === 0) return { query: '', primaryText: '' };
        const primaryText = userTexts[0].slice(0, 400);
        const query = (userTexts[0].length < 18 && userTexts[1])
            ? `${userTexts[0]} ${userTexts[1].slice(0, 90)}`.trim()
            : primaryText;
        return { query, primaryText };
    }

    _normalize(text) {
        return String(text || '')
            .toLowerCase()
            .normalize('NFKC')
            .replace(/[_\\\-—–:：,，.。!！?？/()（）【】\[\]「」『』《》"']+/g, ' ')
            .replace(/\s+/g, ' ')
            .trim();
    }

    _tokenize(text, isQuery = false) {
        const val = this._normalize(text);
        const latin = (val.match(/[a-z0-9][a-z0-9_./:#@+-]{1,}/g) || [])
            .filter(w => !isQuery || (w !== 'vcp' && w !== 'api' && w !== 'ai'));
        const cjkRuns = val.match(/[\u4e00-\u9fff]+/g) || [];
        const cjk = [];
        const boundaryParticles = /^[的了呢吗吧啊呀哦嗯着过地得之与及和或把被让给在从向到上下里外内中前后都也就还再又很太更最每各不没无非我你他她它您请]|^[一二三四五六七八九十百千万]|[的了呢吗吧啊呀哦嗯着过地得之与及和或把被让给在从向到上下里外内中前后都也就还再又我你他她它您]$/;
        for (const run of cjkRuns) {
            const cleanedRun = isQuery ? run.replace(/一下|一点|一些|一会儿/g, ' ') : run;
            const segments = isQuery
                ? cleanedRun.split(/[\s的了呢吗吧啊呀哦嗯着过地得之与及和或把被让给在从向到上下里外内中前后都也就还再又很太更最每各我你他她它您请]+/).filter(s => s.length >= 2)
                : [cleanedRun];
            for (const seg of segments) {
                if (seg.length === 1) {
                    if (!isQuery) cjk.push(seg);
                } else {
                    for (let i = 0; i < seg.length - 1; i++) {
                        const bg = seg.slice(i, i + 2);
                        if (isQuery && (CJK_STOP_BIGRAMS.has(bg) || boundaryParticles.test(bg))) continue;
                        cjk.push(bg);
                    }
                    if (seg.length >= 3 && seg.length <= 6 && (!isQuery || !CJK_STOP_BIGRAMS.has(seg))) {
                        cjk.push(seg);
                    }
                }
            }
        }
        return [...new Set(latin.concat(cjk))];
    }

    _calibrateVectorScores(rawScores) {
        const valid = rawScores.filter(s => s > 0);
        if (valid.length === 0) return rawScores;

        const sorted = [...valid].sort((a, b) => a - b);
        const n = sorted.length;
        const empMedian = sorted[Math.floor(n * 0.5)];
        const q75 = sorted[Math.floor(n * 0.75)];
        const q25 = sorted[Math.floor(n * 0.25)];
        const absDevs = sorted.map(v => Math.abs(v - empMedian)).sort((a, b) => a - b);
        const mad = absDevs[Math.floor(absDevs.length * 0.5)] * 1.4826;
        const iqrStd = (q75 - q25) / 1.349;
        const empSpread = Math.max(mad, iqrStd, 0.042);

        const sampleCount = n;
        const priorWeight = sampleCount < 16 ? Math.max(0.15, (16 - sampleCount) / 16) : 0;
        const alpha = 1.0 - priorWeight;
        const median = alpha * empMedian + (1 - alpha) * 0.26;
        const spread = Math.max(0.045, alpha * empSpread + (1 - alpha) * 0.075);
        const minEffectiveRaw = empMedian < 0.18
            ? Math.max(0.18, empMedian + 0.045)
            : Math.max(0.24, median + 0.35 * spread);
        const maxBoostRatio = empMedian < 0.18 ? 2.45 : 1.85;

        return rawScores.map(raw => {
            if (raw <= 0) return 0;
            if (raw < minEffectiveRaw) {
                return Math.max(0, Math.min(0.36, raw * 0.92));
            }
            const z = (raw - median) / spread;
            const relativeCalibrated = Math.max(0, Math.min(0.98, 0.24 + z * 0.115));
            const isSkewedModel = median > 0.42 || median < 0.17;
            const blended = isSkewedModel
                ? (0.22 * raw + 0.78 * relativeCalibrated)
                : (0.52 * raw + 0.48 * relativeCalibrated);
            const capped = Math.min(blended, raw * maxBoostRatio);
            return Math.max(0, Math.min(0.99, capped));
        });
    }

    async routeAndHighlight(queryText, options = {}) {
        const manager = this._getTdbManager();
        if (!manager) return { enabled: false, mode: 'L0', libraries: [], highlights: [] };

        const allDocs = manager.listDocuments();
        if (!allDocs || allDocs.length === 0) {
            return { enabled: true, mode: 'L0', libraries: [], highlights: [] };
        }

        const libCounts = new Map();
        for (const d of allDocs) libCounts.set(d.library, (libCounts.get(d.library) || 0) + 1);
        const libraryOverview = [...libCounts.entries()].map(([name, count]) => ({ name, count }));

        const cleanQuery = String(queryText || '').trim();
        if (!cleanQuery || cleanQuery.length < 2 || TRIVIAL_QUERY_REGEX.test(cleanQuery)) {
            return { enabled: true, mode: 'L0', libraries: libraryOverview, highlights: [], trivial: true };
        }

        const topK = Math.max(1, options.topK || this.config.RADAR_TOP_DOCS);
        const minScore = options.minScore ?? this.config.RADAR_MIN_SCORE;
        const allowedLibs = Array.isArray(options.libraries) && options.libraries.length > 0
            ? new Set(options.libraries)
            : null;

        const storePath = manager.config?.storePath;
        const [meta, catalogCache] = await Promise.all([
            this._getRouterMeta(storePath),
            this._getRouterCatalog(storePath)
        ]);

        const indexSig = `${allDocs.length}:${this._metaCache.mtimeMs}:${catalogCache.mtimeMs}`;
        const cacheKey = `${cleanQuery}|${allowedLibs ? [...allowedLibs].join(',') : 'ALL'}|${topK}|${minScore}|${indexSig}`;
        const cachedRadar = this._radarResultCache.get(cacheKey);
        if (cachedRadar && (Date.now() - cachedRadar.at < 60 * 1000)) {
            return cachedRadar.result;
        }

        const queryVectorRaw = await this._getQueryVector(cleanQuery, manager, options.primaryText || cleanQuery);
        const queryUnitVec = queryVectorRaw ? toNormalizedFloat32(queryVectorRaw) : null;
        const activeQueryDim = queryUnitVec ? queryUnitVec.length : 0;

        this._autoSyncNewDocuments(manager, allDocs, meta, catalogCache, storePath, activeQueryDim).catch(() => {});

        if (this._bm25IndexCache.sig !== indexSig) {
            const df = new Map();
            const titleSegDf = new Map();
            const docMap = new Map();
            let totalTerms = 0;
            for (const doc of allDocs) {
                const key = `${doc.library}\u0000${doc.path}`;
                const shortPath = this._stripLibraryPrefix(doc.library, doc.path);
                const metaEntry = this._lookupDocMeta(meta, doc);
                const rawTags = Array.isArray(metaEntry.tags) ? metaEntry.tags : [];
                const libLower = String(doc.library || '').toLowerCase();
                const titleLower = String(doc.title || '').toLowerCase();
                const tags = rawTags.filter(t => {
                    const tl = String(t || '').trim().toLowerCase();
                    return tl && tl !== libLower && tl !== titleLower;
                });
                const description = String(metaEntry.description || '').trim();
                const routerText = `${doc.title} ${shortPath} ${tags.join(' ')} ${description}`;
                const terms = this._tokenize(routerText, false);
                const tf = new Map();
                for (const t of terms) tf.set(t, (tf.get(t) || 0) + 1);
                for (const t of new Set(terms)) df.set(t, (df.get(t) || 0) + 1);
                totalTerms += terms.length;
                // V1 章节层级加权：[核心目录] 行独立分词，TF 加成提升章节概念权重
                const tocLine = description.match(/^\[核心目录\]\s*(.+)$/m);
                if (tocLine) {
                    const headingTerms = this._tokenize(tocLine[1], false);
                    const hBoost = this.config.TOPOLOGY_HEADING_TF_BOOST;
                    for (const t of headingTerms) {
                        if (!tf.has(t)) df.set(t, (df.get(t) || 0) + 1);
                        tf.set(t, (tf.get(t) || 0) + hBoost);
                    }
                    totalTerms += headingTerms.length * hBoost;
                }
                const isLatinTitle = /^[a-z0-9_\-\s.()]+$/i.test(doc.title);
                const titleNorm = this._normalize(doc.title);
                const rawTitleSegs = titleNorm
                    .replace(/^\d+\s*/, '')
                    .split(/[\s_—\-]+/)
                    .filter(s => s.length >= 2 && !CJK_STOP_BIGRAMS.has(s));
                for (const seg of new Set(rawTitleSegs)) {
                    titleSegDf.set(seg, (titleSegDf.get(seg) || 0) + 1);
                }
                docMap.set(key, {
                    ...doc,
                    key,
                    isLatinTitle,
                    titleNorm,
                    rawTitleSegs,
                    tags,
                    tagsLower: tags.filter(t => t && t.length >= 4).map(t => String(t).toLowerCase()),
                    description,
                    termsLen: terms.length,
                    tf
                });
            }
            const avgdl = totalTerms / (allDocs.length || 1) || 1;
            this._bm25IndexCache = { sig: indexSig, df, titleSegDf, avgdl, docMap };
        }

        // ===== V2 河道传播底座 v2.6：分库共现分片 + 自适应粒度 + 出流预算 + CSR（仅索引变化时重建） =====
        if (this.config.TOPOLOGY_PROPAGATION && this._topologyCache?.sig !== indexSig) {
            this._topologyCache = this._buildTopologyCSR(indexSig, this._bm25IndexCache);
        }

        const candidateDocs = allowedLibs ? allDocs.filter(d => allowedLibs.has(d.library)) : allDocs;
        const queryLower = cleanQuery.toLowerCase();
        const queryNorm = this._normalize(cleanQuery);
        const effectiveAliases = this._buildEffectiveAliases([...libCounts.keys()]);
        const mentionedLibraries = new Set();
        for (const [libName, aliases] of Object.entries(effectiveAliases)) {
            if (!libCounts.has(libName)) continue;
            if (queryLower.includes(libName.toLowerCase()) || aliases.some(a => a && queryLower.includes(a))) {
                mentionedLibraries.add(libName);
            }
        }

        const queryTerms = this._tokenize(cleanQuery, true);
        const { df, titleSegDf, avgdl, docMap } = this._bm25IndexCache;
        const maxGenericTitleSegDf = Math.max(3, Math.ceil(allDocs.length * 0.05));
        const k1 = 1.2;
        const b = 0.75;
        const bm25HalfSat = 5.2 + 0.45 * Math.max(0, queryTerms.length - 3);

        const docInfos = candidateDocs.map(doc => {
            const key = `${doc.library}\u0000${doc.path}`;
            const cachedDoc = docMap.get(key) || doc;
            let bm25 = 0;
            let matchedTermCount = 0;
            let specificTermCount = 0;
            if (cachedDoc.tf) {
                for (const term of queryTerms) {
                    const freq = cachedDoc.tf.get(term) || 0;
                    if (!freq) continue;
                    const docFreq = df.get(term) || 0;
                    if (docFreq <= Math.max(3, allDocs.length * 0.35)) {
                        matchedTermCount++;
                    }
                    if (docFreq <= Math.max(2, Math.floor(allDocs.length * 0.12))) {
                        specificTermCount++;
                    }
                    const idf = Math.log(1 + (allDocs.length - docFreq + 0.5) / (docFreq + 0.5));
                    bm25 += idf * ((freq * (k1 + 1)) / (freq + k1 * (1 - b + b * (cachedDoc.termsLen / avgdl))));
                }
            }
            const bm25Norm = bm25 > 0 ? (bm25 / (bm25 + bm25HalfSat)) : 0;
            const docUnitVec = this._lookupCatalogUnitVec(catalogCache, doc);
            const hasDocVec = Boolean(queryUnitVec && docUnitVec && queryUnitVec.length === docUnitVec.length);
            const rawVecScore = hasDocVec
                ? Math.max(0, dotProductUnit(queryUnitVec, docUnitVec))
                : 0;

            return {
                ...cachedDoc,
                key,
                bm25,
                bm25Norm,
                hasDocVec,
                rawVecScore,
                matchedTermCount,
                specificTermCount
            };
        });

        const hasValidVectors = Boolean(queryUnitVec && docInfos.some(d => d.rawVecScore > 0));
        const calibratedVecs = hasValidVectors
            ? this._calibrateVectorScores(docInfos.map(d => d.rawVecScore))
            : docInfos.map(() => 0);

        const scored = docInfos.map((d, idx) => {
            const vecScore = calibratedVecs[idx];
            const hasHighLexicalSpecificity = (
                (d.specificTermCount >= 2 && d.matchedTermCount >= 3 && d.bm25Norm >= 0.45 && d.rawVecScore >= 0.45) ||
                (d.specificTermCount >= 1 && d.matchedTermCount >= 2 && d.bm25Norm >= 0.35 && d.rawVecScore >= 0.48)
            );
            const effectiveVecForBlend = hasHighLexicalSpecificity ? Math.max(vecScore, d.rawVecScore * 0.90) : vecScore;
            let score = (hasValidVectors && d.hasDocVec)
                ? (0.38 * d.bm25Norm + 0.62 * effectiveVecForBlend)
                : d.bm25Norm;

            const titleNorm = d.titleNorm || this._normalize(d.title);
            const rawSegs = d.rawTitleSegs || titleNorm.replace(/^\d+\s*/, '').split(/[\s_—\-]+/).filter(Boolean);
            const specificTitleSegs = rawSegs.filter(s =>
                s.length >= 4 &&
                !CJK_STOP_BIGRAMS.has(s) &&
                (!titleSegDf || (titleSegDf.get(s) || 0) <= maxGenericTitleSegDf)
            );
            let exactMatch = false;
            let titleCoreHit = false;
            if (titleNorm && titleNorm.length >= 2 && (queryNorm.includes(titleNorm) || (queryNorm.length >= 4 && titleNorm.includes(queryNorm)))) {
                score += 0.38;
                exactMatch = true;
            } else {
                if (specificTitleSegs.some(seg => queryNorm.includes(seg))) {
                    score += 0.16;
                    titleCoreHit = true;
                } else if ((d.tagsLower || []).some(t => t.length >= 4 && !CJK_STOP_BIGRAMS.has(t) && (!titleSegDf || (titleSegDf.get(t) || 0) <= maxGenericTitleSegDf) && queryLower.includes(t))) {
                    score += 0.14;
                }
            }

            if (mentionedLibraries.has(d.library)) {
                const wantsIndex = /索引|目录|注册表|有哪些|列表|全部|总览|总纲/.test(cleanQuery);
                const isIndexDoc = /^00_|索引|注册表|总纲|总览/.test(d.title);
                if (d.matchedTermCount >= 1 || vecScore >= 0.44 || (wantsIndex && isIndexDoc) || (libCounts.get(d.library) === 1)) {
                    score += 0.15;
                }
                if ((wantsIndex && isIndexDoc) || (libCounts.get(d.library) === 1)) {
                    score += 0.10;
                }
            }

            return { ...d, vectorScore: vecScore, score, exactMatch, titleCoreHit };
        });

        // ===== V2 河道传播（CSR）：严格稀疏门控 + tie-breaker 路径奖励（上限 TOPOLOGY_PATH_BONUS_MAX） =====
        const topo = this.config.TOPOLOGY_PROPAGATION ? this._topologyCache : null;
        if (topo?.conceptIndex && queryTerms.length > 0) {
            const maxBaseScore = scored.reduce((m, s) => Math.max(m, s.score), 0);
            if (maxBaseScore < this.config.TOPOLOGY_SPARSE_TOP_SCORE) {
                const entryIds = [];
                for (const t of queryTerms) {
                    const cid = topo.conceptIndex.get(t);
                    if (cid !== undefined) entryIds.push(cid);
                }
                if (entryIds.length >= Math.max(1, this.config.TOPOLOGY_SPARSE_MIN_HITS) && entryIds.length <= this.config.TOPOLOGY_MAX_CONCEPTS) {
                    const qIdSet = new Set(entryIds);
                    const propagated = new Map();
                    for (const e of entryIds) {
                        const eW = topo.idfArr[e] / topo.maxIdf;
                        for (let j = topo.offsets[e]; j < topo.offsets[e + 1]; j++) {
                            const n = topo.neighborIdx[j];
                            if (qIdSet.has(n)) continue;
                            const s = topo.edgeW[j] * eW * (topo.idfArr[n] / topo.maxIdf);
                            if (s > (propagated.get(n) || 0)) propagated.set(n, s);
                        }
                    }
                    if (propagated.size > 0) {
                        const cap = this.config.TOPOLOGY_PATH_BONUS_MAX;
                        const docBonus = new Map();
                        for (const [n, s] of propagated) {
                            const b = cap * Math.min(1, s);
                            for (let j = topo.docOffsets[n]; j < topo.docOffsets[n + 1]; j++) {
                                const di = topo.docIdxArr[j];
                                if (b > (docBonus.get(di) || 0)) docBonus.set(di, b);
                            }
                        }
                        let boosted = 0;
                        for (const item of scored) {
                            const di = topo.docKeyIdx.get(item.key);
                            if (di === undefined) continue;
                            const b = docBonus.get(di);
                            if (b > 0) { item.score += b; item._pathBonus = b; boosted++; }
                        }
                        if (boosted > 0) {
                            console.log(`[VCPKnowledge] 🌊 河道传播生效: 入口概念=${entryIds.length}, 传播概念=${propagated.size}, 加权文档=${boosted} (maxBase=${maxBaseScore.toFixed(3)})`);
                        }
                    }
                }
            }
        }

        const pinpointMap = new Map();
        const canonicalKeyMap = new Map();
        for (const d of scored) {
            canonicalKeyMap.set(d.key, d);
            canonicalKeyMap.set(`${d.library}\u0000${d.library}\\${d.path}`, d);
            canonicalKeyMap.set(`${d.library}\u0000${d.library}/${d.path}`, d);
            const base = path.basename(d.path);
            if (!canonicalKeyMap.has(`${d.library}\u0000${base}`)) {
                canonicalKeyMap.set(`${d.library}\u0000${base}`, d);
            }
        }

        if (queryVectorRaw && typeof manager.searchLibrary === 'function') {
            const allLibNames = allowedLibs ? [...allowedLibs] : [...libCounts.keys()];
            try {
                const perLibResults = await Promise.all(
                    allLibNames.map(lib => {
                        const docCnt = libCounts.get(lib) || 1;
                        const k = docCnt > 50 ? 6 : (docCnt > 15 ? 3 : 2);
                        return manager.searchLibrary(lib, '', queryVectorRaw, {
                            topK: k,
                            expandDepth: 0,
                            minScore: 0.38,
                            hybridAlpha: 1.0
                        }).catch(() => []);
                    })
                );
                const deepHits = perLibResults.flat().sort((a, b) => (b.score || 0) - (a.score || 0));

                for (const h of deepHits) {
                    if (h.payload?.type === 'document' || (h.chunkIndex === undefined && !h.text)) continue;
                    const rawSource = String(h.sourcePath || h.sourceFile || '');
                    const strippedSource = rawSource.startsWith(`${h.library}\\`) || rawSource.startsWith(`${h.library}/`)
                        ? rawSource.slice(h.library.length + 1)
                        : rawSource;
                    const matchedDoc = canonicalKeyMap.get(`${h.library}\u0000${strippedSource}`)
                        || canonicalKeyMap.get(`${h.library}\u0000${rawSource}`)
                        || canonicalKeyMap.get(`${h.library}\u0000${path.basename(rawSource)}`);
                    if (!matchedDoc) continue;

                    const cIdx = Number.isFinite(Number(h.chunkIndex)) ? Number(h.chunkIndex) : 0;
                    if (!pinpointMap.has(matchedDoc.key)) pinpointMap.set(matchedDoc.key, []);
                    const arr = pinpointMap.get(matchedDoc.key);
                    const maxPinpoints = Math.max(1, this.config.RADAR_PINPOINT_CHUNKS || 2);

                    let chunkLexHits = 0;
                    let chunkSpecificHits = 0;
                    const chunkTextNorm = this._normalize(h.text || '');
                    for (const term of queryTerms) {
                        if (term.length >= 2 && chunkTextNorm.includes(term)) {
                            const docFreq = df.get(term) || 0;
                            if (docFreq <= Math.max(4, allDocs.length * 0.30)) chunkLexHits++;
                            if (docFreq <= Math.max(2, Math.floor(allDocs.length * 0.12))) chunkSpecificHits++;
                        }
                    }

                    if (arr.length < maxPinpoints && !arr.some(x => x.chunkIndex === cIdx)) {
                        arr.push({
                            chunkIndex: cIdx,
                            score: h.score || 0,
                            snippet: this._makeSnippet(h.text, this.config.RADAR_SNIPPET_CHARS),
                            inlineText: this._makeSnippet(h.text, 520)
                        });
                    }
                    const chunkVecCosine = Number(h.score) || 0;
                    if (!matchedDoc._bestChunkVec || chunkVecCosine > matchedDoc._bestChunkVec) {
                        matchedDoc._bestChunkVec = chunkVecCosine;
                    }
                    if (!matchedDoc._bestChunkLexHits || chunkLexHits > matchedDoc._bestChunkLexHits) {
                        matchedDoc._bestChunkLexHits = chunkLexHits;
                    }
                    if (!matchedDoc._bestChunkSpecificHits || chunkSpecificHits > matchedDoc._bestChunkSpecificHits) {
                        matchedDoc._bestChunkSpecificHits = chunkSpecificHits;
                    }

                    const isShortQuery = queryTerms.length <= 6;
                    const isDeepAnchorHit = (
                        (isShortQuery && chunkVecCosine >= 0.55 && (chunkSpecificHits >= 1 || chunkLexHits >= 2)) ||
                        (chunkVecCosine >= 0.48 && chunkSpecificHits >= 2 && chunkLexHits >= 3) ||
                        (chunkVecCosine >= 0.58 && chunkLexHits >= 2 && chunkSpecificHits >= 1 && matchedDoc.rawVecScore >= 0.37) ||
                        (chunkVecCosine >= 0.54 && matchedDoc.rawVecScore >= 0.42 && chunkLexHits >= 2 && (chunkSpecificHits >= 1 || matchedDoc.specificTermCount >= 1))
                    );
                    const eligibleForChunkBoost = (
                        mentionedLibraries.has(matchedDoc.library) ||
                        (matchedDoc.titleCoreHit && matchedDoc.rawVecScore >= 0.46) ||
                        isDeepAnchorHit ||
                        (matchedDoc.isLatinTitle && matchedDoc.vectorScore >= 0.48) ||
                        (matchedDoc.specificTermCount >= 1 && matchedDoc.matchedTermCount >= 2 && matchedDoc.vectorScore >= 0.45) ||
                        (matchedDoc.specificTermCount >= 1 && matchedDoc.vectorScore >= 0.58 && matchedDoc.rawVecScore >= 0.48)
                    );
                    if (chunkVecCosine >= 0.48 && eligibleForChunkBoost) {
                        const qualityRatio = Math.min(1.0, Math.max(0.20, (chunkVecCosine - 0.46) / 0.24));
                        const boost = 0.20 * qualityRatio;
                        if (!matchedDoc._chunkBoost || boost > matchedDoc._chunkBoost) {
                            matchedDoc.score += boost - (matchedDoc._chunkBoost || 0);
                            matchedDoc._chunkBoost = boost;
                        }
                        if (isDeepAnchorHit) {
                            matchedDoc._chunkPromoted = true;
                            const promotedFloor = minScore + 0.03 + 0.12 * qualityRatio;
                            if (matchedDoc.score < promotedFloor) {
                                matchedDoc.score = promotedFloor;
                            }
                        }
                    }
                }
            } catch (_) {}
        }

        scored.sort((a, b) => b.score - a.score || a.path.localeCompare(b.path));

        const selected = [];
        const perLibCount = new Map();
        const maxPerLib = mentionedLibraries.size > 1 ? 2 : 3;

        if (mentionedLibraries.size > 0) {
            for (const libName of mentionedLibraries) {
                const bestInLib = scored.find(d => d.library === libName && d.score >= minScore * 0.85);
                if (bestInLib && selected.length < topK) {
                    selected.push(bestInLib);
                    perLibCount.set(libName, 1);
                }
            }
        }

        for (const item of scored) {
            if (selected.length >= topK) break;
            const docUsesVec = hasValidVectors && item.hasDocVec;
            const effectiveMinScore = docUsesVec ? minScore : Math.min(minScore, 0.30);
            if (item.score < effectiveMinScore && !item.exactMatch) continue;
            if (!item.exactMatch && !mentionedLibraries.has(item.library)) {
                if (!docUsesVec) {
                    if (item.matchedTermCount < 2 && !item.titleCoreHit) continue;
                } else {
                    const hasStrongChunk = Boolean(item._chunkPromoted) || ((item._chunkBoost || 0) >= 0.12 && item.rawVecScore >= 0.46 && (item._bestChunkVec || 0) >= 0.52);
                    const hasStrongLexicalAnchor = (
                        (item.specificTermCount >= 2 && item.matchedTermCount >= 2 && item.bm25Norm >= 0.42 && item.rawVecScore >= 0.48) ||
                        (item.specificTermCount >= 1 && item.matchedTermCount >= 2 && item.bm25Norm >= 0.35 && item.rawVecScore >= 0.50) ||
                        (item.specificTermCount >= 1 && item.bm25Norm >= 0.30 && item.rawVecScore >= 0.51)
                    );
                    const totalSpecificHits = Math.max(item.specificTermCount || 0, item._bestChunkSpecificHits || 0);
                    const highVecSingleAnchor = (item.vectorScore >= 0.60 || hasStrongLexicalAnchor) && item.rawVecScore >= 0.51 && totalSpecificHits >= 1 && (queryTerms.length <= 8 || item.matchedTermCount >= 2 || (item._bestChunkLexHits || 0) >= 2);
                    const minTermsRequired = (
                        (item.isLatinTitle && item.vectorScore >= 0.50) ||
                        (item.titleCoreHit && item.rawVecScore >= 0.50) ||
                        hasStrongChunk ||
                        hasStrongLexicalAnchor ||
                        highVecSingleAnchor ||
                        (item.vectorScore >= 0.76 && item.rawVecScore >= 0.55)
                    ) ? 1 : 2;
                    const effectiveTermHits = Math.max(item.matchedTermCount, item._bestChunkLexHits || 0, (item.isLatinTitle && item.vectorScore >= 0.50) ? 1 : 0);
                    if ((item.vectorScore < 0.44 && !hasStrongChunk && !hasStrongLexicalAnchor) || effectiveTermHits < minTermsRequired) continue;
                    if (totalSpecificHits === 0 && !item.isLatinTitle && (item._bestChunkVec || 0) < 0.58 && item.rawVecScore < 0.54) continue;
                }
            }
            if (selected.some(s => s.key === item.key)) continue;
            const curLibCnt = perLibCount.get(item.library) || 0;
            if (curLibCnt >= maxPerLib && scored.length > topK) continue;
            selected.push(item);
            perLibCount.set(item.library, curLibCnt + 1);
        }

        // V2 河道提名通道：topK 有空位时，pathBonus 文档以半门槛提名（不抢主证据位置，标记 _riverNominated）
        if (topo?.conceptIndex && selected.length < topK) {
            const nomThreshold = Math.min(minScore * 0.5, this.config.TOPOLOGY_PATH_BONUS_MAX * 0.5);
            for (const item of scored) {
                if (selected.length >= topK) break;
                if ((item._pathBonus || 0) <= 0) continue;
                if (selected.some(s => s.key === item.key)) continue;
                if (item.score < nomThreshold) continue;
                const curLibCnt2 = perLibCount.get(item.library) || 0;
                if (curLibCnt2 >= maxPerLib && scored.length > topK) continue;
                selected.push(item);
                item._riverNominated = true;
                perLibCount.set(item.library, curLibCnt2 + 1);
            }
        }

        const missingPinpointDocs = selected.filter(d => !pinpointMap.has(d.key));
        if (missingPinpointDocs.length > 0 && queryVectorRaw) {
            const targetLibs = [...new Set(missingPinpointDocs.map(s => s.library))];
            const targetPaths = [];
            for (const d of missingPinpointDocs) {
                targetPaths.push(d.path, `${d.library}\\${d.path}`, `${d.library}/${d.path}`);
            }
            try {
                const chunkHits = await manager.searchWithVector(queryVectorRaw, cleanQuery, {
                    libraries: targetLibs,
                    topK: Math.max(6, missingPinpointDocs.length * 2),
                    expandDepth: 0,
                    minScore: 0.05,
                    hybridAlpha: 0.72,
                    payloadFilter: { source_path: { $in: [...new Set(targetPaths)] } }
                });
                for (const h of (chunkHits || [])) {
                    if (h.payload?.type === 'document' || (h.chunkIndex === undefined && !h.text)) continue;
                    const rawSource = String(h.sourcePath || h.sourceFile || '');
                    const strippedSource = rawSource.startsWith(`${h.library}\\`) || rawSource.startsWith(`${h.library}/`)
                        ? rawSource.slice(h.library.length + 1)
                        : rawSource;
                    const matchedDoc = canonicalKeyMap.get(`${h.library}\u0000${strippedSource}`)
                        || canonicalKeyMap.get(`${h.library}\u0000${rawSource}`)
                        || canonicalKeyMap.get(`${h.library}\u0000${path.basename(rawSource)}`);
                    if (!matchedDoc) continue;
                    const cIdx = Number.isFinite(Number(h.chunkIndex)) ? Number(h.chunkIndex) : 0;
                    if (!pinpointMap.has(matchedDoc.key)) pinpointMap.set(matchedDoc.key, []);
                    const arr = pinpointMap.get(matchedDoc.key);
                    const maxPinpoints = Math.max(1, this.config.RADAR_PINPOINT_CHUNKS || 2);
                    if (arr.length < maxPinpoints && !arr.some(x => x.chunkIndex === cIdx)) {
                        arr.push({
                            chunkIndex: cIdx,
                            score: h.score || 0,
                            snippet: this._makeSnippet(h.text, this.config.RADAR_SNIPPET_CHARS),
                            inlineText: this._makeSnippet(h.text, 520)
                        });
                    }
                }
            } catch (_) {}
        }

        const chunkCountStmt = manager.metaDb?.prepare?.('SELECT COUNT(*) as c FROM chunks WHERE library = ? AND (path = ? OR path = ?)');
        const highlights = selected.map(doc => {
            const shortPath = this._stripLibraryPrefix(doc.library, doc.path);
            const fullPath = `${doc.library}\\${shortPath}`;
            const totalChunks = chunkCountStmt ? (chunkCountStmt.get(doc.library, shortPath, fullPath)?.c || 1) : 1;
            const pinpoints = pinpointMap.get(doc.key) || [];
            const tocLine = this._extractTocSummary(doc.description, doc.tags);
            return {
                library: doc.library,
                path: shortPath,
                title: doc.title,
                score: Math.min(0.999, doc.score),
                vectorScore: doc.vectorScore,
                bm25Norm: doc.bm25Norm,
                matchedTermCount: doc.matchedTermCount,
                exactMatch: Boolean(doc.exactMatch),
                totalChunks,
                tocSummary: tocLine,
                pinpoints
            };
        });

        const maxPinpointsCfg = Math.max(1, this.config.RADAR_PINPOINT_CHUNKS || 2);
        for (const h of highlights) {
            if (h.pinpoints.length === 0) {
                try {
                    const loaded = await this._loadDocChunks(manager, h);
                    if (loaded?.chunks?.length > 0) {
                        const rankedChunks = loaded.chunks.map((ch, idx) => {
                            const norm = this._normalize(ch);
                            let uniq = 0;
                            let tfSum = 0;
                            for (const t of queryTerms) {
                                if (t.length >= 2 && norm.includes(t)) {
                                    uniq++;
                                    tfSum += (norm.split(t).length - 1);
                                }
                            }
                            return { idx, ch, score: uniq * 10 + Math.min(9, tfSum) };
                        }).sort((a, b) => b.score - a.score || a.idx - b.idx);
                        for (const rc of rankedChunks.slice(0, maxPinpointsCfg)) {
                            h.pinpoints.push({
                                chunkIndex: rc.idx,
                                score: h.score,
                                snippet: this._makeSnippet(rc.ch, this.config.RADAR_SNIPPET_CHARS),
                                inlineText: this._makeSnippet(rc.ch, 520)
                            });
                        }
                    }
                } catch (_) {}
            } else if (!h.pinpoints[0].inlineText) {
                try {
                    const loaded = await this._loadDocChunks(manager, h);
                    const textChunk = loaded?.chunks?.[h.pinpoints[0].chunkIndex];
                    if (textChunk) h.pinpoints[0].inlineText = this._makeSnippet(textChunk, 520);
                } catch (_) {}
            }
        }

        const mode = highlights.length === 0
            ? 'L0'
            : ((highlights[0].score >= this.config.RADAR_INLINE_SCORE || highlights[0].exactMatch) ? 'L2' : 'L1');

        const result = {
            enabled: true,
            mode,
            query: cleanQuery,
            libraries: libraryOverview,
            highlights
        };

        this._radarResultCache.set(cacheKey, { result, at: Date.now() });
        if (this._radarResultCache.size > 128) {
            this._radarResultCache.delete(this._radarResultCache.keys().next().value);
        }
        return result;
    }

    _extractTocSummary(description, tags = []) {
        const desc = String(description || '')
            .replace(/^\[20\d{2}-\d{2}-\d{2}\]\s*-\s*[^\r\n]+\r?\n?/gm, '')
            .trim();
        if (desc) {
            const lines = desc.split(/\r?\n/).map(s => s.trim()).filter(Boolean);
            const tocLine = lines.find(l => l.startsWith('[核心目录]'))?.replace(/^\[核心目录\]\s*/, '') || '';
            const sumLine = lines.find(l => l.startsWith('[语义提要]') || l.startsWith('[路由摘要]'))?.replace(/^\[(?:语义提要|路由摘要)\]\s*/, '') || lines[0] || '';
            if (tocLine && sumLine && tocLine !== sumLine) {
                return `${tocLine.slice(0, 75)} — ${sumLine.slice(0, 75)}`;
            }
            return (sumLine || tocLine).slice(0, 145);
        }
        if (Array.isArray(tags) && tags.length > 0) {
            return tags.slice(0, 8).join(' | ');
        }
        return '';
    }

    _makeSnippet(text, maxChars = 110) {
        const clean = String(text || '')
            .replace(/^\[20\d{2}-\d{2}-\d{2}\]\s*-\s*[^\r\n]+\r?\n?/gm, '')
            .replace(/\r?\n+/g, ' ')
            .replace(/\s+/g, ' ')
            .trim();
        return clean.length > maxChars ? `${clean.slice(0, maxChars)}…` : clean;
    }

    formatRadarBlock(radar) {
        if (!radar || !radar.enabled) {
            return '[🧭 VCP 全域冷知识库雷达：当前未启用]';
        }
        const totalDocs = radar.libraries.reduce((s, l) => s + l.count, 0);
        const libStr = radar.libraries.map(l => `${l.name}(${l.count}篇)`).join(' | ');

        if (!radar.highlights || radar.highlights.length === 0) {
            return [
                '<!-- VCP_KNOWLEDGE_RADAR_START -->',
                `[🧭 VCP 全域知识库雷达 (L0 静默就绪) | 已联通 ${radar.libraries.length} 库 ${totalDocs} 篇: ${libStr} | 如需查书/设定/规范请调 VCPKnowledge]`,
                '<!-- VCP_KNOWLEDGE_RADAR_END -->'
            ].join('\n');
        }

        const lines = [
            '<!-- VCP_KNOWLEDGE_RADAR_START -->',
            `[🧭 VCP 全域知识库雷达 (${radar.mode || 'L1'}) | 已联通 ${radar.libraries.length} 大知识库 / 共 ${totalDocs} 篇文档]`,
            `📚 全域库表: ${libStr}`,
            `🎯 【本轮高亮知识位置】（已按当前话题自动路由定位 ${radar.highlights.length} 处高相关知识坐标）：`
        ];

        radar.highlights.forEach((h, idx) => {
            const pct = `${(h.score * 100).toFixed(1)}%`;
            const chunkHint = h.pinpoints.length > 0
                ? `📍焦点位置: 第 ${h.pinpoints.map(p => `#${p.chunkIndex}`).join(', ')} 节`
                : `共 ${h.totalChunks} 节`;
            lines.push(`${idx + 1}. 🔥 [${h.library}] ${h.path} (匹配度: ${pct} | 共${h.totalChunks}节 | ${chunkHint})`);
            if (h.tocSummary) {
                lines.push(`   ├─ 目录/提要: ${h.tocSummary}`);
            }
            if (idx === 0 && radar.mode === 'L2' && h.pinpoints[0]?.inlineText) {
                lines.push(`   ├─ ⚡ 高置信焦点直通(#${h.pinpoints[0].chunkIndex}): "${h.pinpoints[0].inlineText}"`);
            } else if (h.pinpoints.length > 0 && h.pinpoints[0].snippet) {
                lines.push(`   ├─ 位置预览(#${h.pinpoints[0].chunkIndex}): "${h.pinpoints[0].snippet}"`);
            }
            const targetChunk = h.pinpoints.length > 0 ? String(h.pinpoints[0].chunkIndex) : '0';
            lines.push(`   └─ 🔍 按需直读: VCPKnowledge(command="read", doc=${JSON.stringify(h.path)}, chunk=${JSON.stringify(targetChunk)})`);
        });

        lines.push('💡 [按需查找指南]: 上方仅提供坐标定位与微预览。回答具体内容前，请务必调用 `VCPKnowledge(command="read", doc=..., chunk=...)` 读取完整原文，切勿仅凭微预览脑补细节。');
        lines.push('<!-- VCP_KNOWLEDGE_RADAR_END -->');
        return lines.join('\n');
    }

    _broadcastRadar(radar) {
        const pushFn = this.vcpLogFunctions?.pushVcpInfo || this._getRagPlugin()?.pushVcpInfo;
        if (typeof pushFn !== 'function' || !radar?.highlights?.length) return;
        try {
            pushFn({
                type: 'RAG_RETRIEVAL_DETAILS',
                dbName: `🧭 VCP全域知识库雷达 (${radar.mode || 'L1'})`,
                query: radar.query || '',
                k: radar.highlights.length,
                sourceType: 'VCPKnowledgeRadar',
                libraries: radar.libraries.map(l => l.name),
                results: radar.highlights.map(h => ({
                    text: `[${h.library}] ${h.path}\n目录/提要: ${h.tocSummary || '无'}\n${h.pinpoints[0]?.snippet ? `位置预览(#${h.pinpoints[0].chunkIndex}): ${h.pinpoints[0].snippet}` : ''}`,
                    score: h.score,
                    source: 'tdb-radar',
                    matchedTags: [h.library, h.title, `共${h.totalChunks}节`]
                }))
            });
        } catch (_) {}
    }

    _isEligibleCarrierMessage(m, allowMaskedCompaction = false, hasSystemCarrier = false) {
        if (!m || (m.role !== 'system' && m.role !== 'user')) return false;
        if (m.contextCompaction && !allowMaskedCompaction) return false;
        const text = typeof m.content === 'string'
            ? m.content
            : (Array.isArray(m.content) ? m.content.map(p => p?.text || '').join('\n') : '');
        if (!text || this._isToolPayloadText(text)) return false;
        if (!allowMaskedCompaction && this._isContextCompactionMessage(m, text)) return false;
        if (m.role === 'user' && hasSystemCarrier && !/\[系统提示:\]|这是VCP全域冷知识库雷达/.test(text)) {
            return false;
        }
        return true;
    }

    _stripCompressedCheckpointSegments(text) {
        const s = String(text || '');
        if (!s.includes('context_checkpoint') && !s.includes('VCHAT上下文智能压缩块')) {
            return { masked: s, restore: (out) => out };
        }
        const saved = [];
        const masked = s.replace(
            /\[系统提示:\]\s*\[VCHAT上下文智能压缩块\][\s\S]*?\[系统提示:\]|<context_checkpoint>[\s\S]*?<\/context_checkpoint>/g,
            (match) => {
                const token = `__VCP_CK_MASK_${saved.length}__`;
                saved.push({ token, match });
                return token;
            }
        );
        return {
            masked,
            restore: (out) => {
                let res = String(out || '');
                for (const item of saved) {
                    res = res.replace(item.token, () => item.match);
                }
                return res;
            }
        };
    }

    async processMessages(messages) {
        this._ensureRuntimeHooks();
        if (!Array.isArray(messages) || messages.length === 0) return messages;

        const hasSystemCarrier = messages.some(m => {
            if (!m || m.role !== 'system') return false;
            const rawText = typeof m.content === 'string'
                ? m.content
                : (Array.isArray(m.content) ? m.content.map(p => p?.text || '').join('\n') : '');
            UNIFIED_PLACEHOLDER_REGEX.lastIndex = 0;
            return UNIFIED_PLACEHOLDER_REGEX.test(rawText);
        });

        let hasPlaceholder = hasSystemCarrier;
        if (!hasPlaceholder) {
            for (const m of messages) {
                if (!this._isEligibleCarrierMessage(m, true, false)) continue;
                const rawText = typeof m.content === 'string'
                    ? m.content
                    : (Array.isArray(m.content) ? m.content.map(p => p?.text || '').join('\n') : '');
                const { masked: text } = this._stripCompressedCheckpointSegments(rawText);
                UNIFIED_PLACEHOLDER_REGEX.lastIndex = 0;
                if (UNIFIED_PLACEHOLDER_REGEX.test(text)) {
                    hasPlaceholder = true;
                    break;
                }
            }
        }
        if (!hasPlaceholder) return messages;

        const { query: queryText, primaryText } = this._extractConversationQuery(messages);
        let defaultRadarCache = null;

        const resolveModifierRadar = async (rawMod = '') => {
            const mod = String(rawMod || '').trim();
            let topK = this.config.RADAR_TOP_DOCS;
            let libraries = null;

            const kMatch = mod.match(/(?:^|:)(\d+)/);
            if (kMatch) topK = Math.max(1, Math.min(12, parseInt(kMatch[1], 10)));

            const libPart = mod.replace(/(?:^|:)\d+/g, '').replace(/^:+/, '').trim();
            if (libPart) {
                libraries = libPart.split(/[|,，]/).map(s => s.trim()).filter(Boolean);
            }

            if (!libraries && topK === this.config.RADAR_TOP_DOCS) {
                if (!defaultRadarCache) {
                    defaultRadarCache = await this.routeAndHighlight(queryText, { topK, primaryText });
                    this._broadcastRadar(defaultRadarCache);
                }
                return this.formatRadarBlock(defaultRadarCache);
            }

            const customRadar = await this.routeAndHighlight(queryText, { topK, libraries, primaryText });
            this._broadcastRadar(customRadar);
            return this.formatRadarBlock(customRadar);
        };

        for (const m of messages) {
            if (!this._isEligibleCarrierMessage(m, true, hasSystemCarrier)) continue;
            if (typeof m.content === 'string') {
                const { masked, restore } = this._stripCompressedCheckpointSegments(m.content);
                UNIFIED_PLACEHOLDER_REGEX.lastIndex = 0;
                const matches = [...masked.matchAll(UNIFIED_PLACEHOLDER_REGEX)];
                if (matches.length > 0) {
                    let updated = masked;
                    for (const match of matches) {
                        const full = match[0];
                        const mod = match[1] || match[2] || match[3] || '';
                        const block = await resolveModifierRadar(mod);
                        updated = updated.replace(full, () => block);
                    }
                    m.content = restore(updated);
                }
            } else if (Array.isArray(m.content)) {
                for (const part of m.content) {
                    if (!part || part.type !== 'text' || typeof part.text !== 'string') continue;
                    if (this._isToolPayloadText(part.text)) continue;
                    const { masked, restore } = this._stripCompressedCheckpointSegments(part.text);
                    UNIFIED_PLACEHOLDER_REGEX.lastIndex = 0;
                    const matches = [...masked.matchAll(UNIFIED_PLACEHOLDER_REGEX)];
                    if (matches.length > 0) {
                        let updated = masked;
                        for (const match of matches) {
                            const full = match[0];
                            const mod = match[1] || match[2] || match[3] || '';
                            const block = await resolveModifierRadar(mod);
                            updated = updated.replace(full, () => block);
                        }
                        part.text = restore(updated);
                    }
                }
            }
        }

        return messages;
    }

    async _loadDocChunks(manager, docRecord) {
        const shortPath = this._stripLibraryPrefix(docRecord.library, docRecord.path);
        const absPath = path.join(manager.config.rootPath, docRecord.library, shortPath);
        const st = await fsp.stat(absPath);
        const cached = this._docChunksCache.get(absPath);
        if (cached && cached.mtimeMs === st.mtimeMs) return cached;
        const fullText = await readTextFile(absPath);
        const chunks = chunkText(fullText).map(c => c.trim()).filter(Boolean);
        const entry = { mtimeMs: st.mtimeMs, chunks, fullText };
        this._docChunksCache.set(absPath, entry);
        if (this._docChunksCache.size > 32) {
            this._docChunksCache.delete(this._docChunksCache.keys().next().value);
        }
        return entry;
    }

    _resolveTargetDoc(manager, docQuery, library = null) {
        const libs = library ? String(library).split(/[|,，]/).map(s => s.trim()).filter(Boolean) : null;
        const allDocs = manager.listDocuments(libs);
        const qRaw = String(docQuery || '').trim();
        if (!qRaw) return null;

        const qNorm = qRaw.replace(/\//g, '\\').toLowerCase();
        let hit = allDocs.find(d =>
            d.path.toLowerCase() === qNorm ||
            `${d.library}\\${d.path}`.toLowerCase() === qNorm ||
            path.basename(d.path).toLowerCase() === qNorm
        );
        if (hit) return hit;

        const qClean = this._normalize(qRaw);
        hit = allDocs.find(d => d.path.toLowerCase().includes(qNorm) || this._normalize(d.title).includes(qClean));
        return hit || null;
    }

    _parseChunkSpec(spec, totalChunks) {
        if (spec === undefined || spec === null || String(spec).trim() === '') {
            return [0, 1].filter(i => i < totalChunks);
        }
        const raw = String(spec).trim().replace(/#/g, '');
        if (/^all$/i.test(raw)) {
            return Array.from({ length: Math.min(totalChunks, 10) }, (_, i) => i);
        }
        const indices = new Set();
        let hasExplicitNumber = false;
        for (const part of raw.split(/[,，\s]+/).filter(Boolean)) {
            const range = part.match(/^(\d+)\s*-\s*(\d+)$/);
            if (range) {
                hasExplicitNumber = true;
                const start = Math.max(0, parseInt(range[1], 10));
                const end = Math.min(totalChunks - 1, parseInt(range[2], 10));
                for (let i = start; i <= end && indices.size < 10; i++) indices.add(i);
            } else if (/^\d+$/.test(part)) {
                hasExplicitNumber = true;
                const idx = parseInt(part, 10);
                if (idx >= 0 && idx < totalChunks) indices.add(idx);
            }
        }
        if (indices.size > 0) return [...indices].sort((a, b) => a - b);
        return hasExplicitNumber ? [] : [0];
    }

    async processToolCall(args = {}) {
        const manager = this._getTdbManager();
        if (!manager) {
            return { content: [{ type: 'text', text: '冷知识库（TDBKnowledge）尚未初始化。' }] };
        }

        const cmd = String(args.command || args.action || '').trim().toLowerCase();
        const docArg = args.doc || args.document || args.path || args.file || '';
        const libArg = args.library || args.knowledge_base || args.knowledgeBase || args.folder || '';
        const queryArg = args.query || args.q || args.keyword || '';
        const chunkArg = args.chunk ?? args.section ?? args.chunks ?? null;

        if (cmd === 'radar' || cmd === 'route') {
            const q = String(queryArg || docArg || '').trim();
            const libs = libArg ? String(libArg).split(/[|,，]/).map(s => s.trim()).filter(Boolean) : null;
            const kVal = Math.max(1, Math.min(12, parseInt(args.k ?? args.top_k ?? this.config.RADAR_TOP_DOCS, 10) || this.config.RADAR_TOP_DOCS));
            const radar = await this.routeAndHighlight(q, { topK: kVal, libraries: libs });
            return { content: [{ type: 'text', text: this.formatRadarBlock(radar) }] };
        }

        if (cmd === 'toc' || cmd === 'list') {
            if (docArg) {
                const target = this._resolveTargetDoc(manager, docArg, libArg);
                if (!target) return { content: [{ type: 'text', text: `未找到文档 "${docArg}"。` }] };
                const shortTargetPath = this._stripLibraryPrefix(target.library, target.path);
                const { chunks } = await this._loadDocChunks(manager, target);
                const tocLines = chunks.map((c, idx) => `  #${idx}: ${this._makeSnippet(c, 90)}`);
                const report = [
                    `## 📖 文档分节目录：[${target.library}] ${shortTargetPath} (共 ${chunks.length} 节)`,
                    ...tocLines,
                    `\n💡 调用 VCPKnowledge(command="read", doc=${JSON.stringify(shortTargetPath)}, chunk="节号如 0-2") 即可读取对应节完整正文。`
                ].join('\n');
                return { content: [{ type: 'text', text: report }] };
            }

            const libs = libArg ? String(libArg).split(/[|,，]/).map(s => s.trim()).filter(Boolean) : null;
            const docs = manager.listDocuments(libs);
            const grouped = {};
            for (const d of docs) {
                const shortP = this._stripLibraryPrefix(d.library, d.path);
                (grouped[d.library] = grouped[d.library] || []).push(shortP);
            }
            const lines = ['## 📚 VCP 全域冷知识库文档清单'];
            for (const [lib, paths] of Object.entries(grouped)) {
                lines.push(`\n### [${lib}] (${paths.length} 篇)`);
                paths.slice(0, 40).forEach(p => lines.push(`- ${p}`));
                if (paths.length > 40) lines.push(`- ... 其余 ${paths.length - 40} 篇（请用 search 检索）`);
            }
            return { content: [{ type: 'text', text: lines.join('\n') }] };
        }

        if (cmd === 'read' || (docArg && (!queryArg || chunkArg !== null))) {
            const target = this._resolveTargetDoc(manager, docArg, libArg);
            if (!target) {
                return {
                    content: [{
                        type: 'text',
                        text: `未找到文档 "${docArg}"。请检查路径或使用 VCPKnowledge(command="search", query="${docArg}") 检索。`
                    }]
                };
            }

            const shortTargetPath = this._stripLibraryPrefix(target.library, target.path);
            const { chunks } = await this._loadDocChunks(manager, target);
            const indices = this._parseChunkSpec(chunkArg, chunks.length);
            if (!indices || indices.length === 0) {
                return {
                    content: [{
                        type: 'text',
                        text: `⚠️ 节号越界：文档 "[${target.library}] ${shortTargetPath}" 共 ${chunks.length} 节（有效节号范围: 0 - ${Math.max(0, chunks.length - 1)}），请求的 chunk="${chunkArg}" 超出范围。`
                    }]
                };
            }
            const out = [
                `## 📄 知识库原文直读：[${target.library}] ${shortTargetPath}`,
                `> 全文共 ${chunks.length} 节 (#0 ~ #${chunks.length - 1})，当前读取第 ${indices.map(i => `#${i}`).join(', ')} 节：\n`
            ];

            for (const idx of indices) {
                out.push(`### [第 #${idx} 节 / 共 ${chunks.length} 节]`);
                out.push(chunks[idx]);
                out.push('');
            }

            const maxRead = Math.max(...indices);
            if (maxRead + 1 < chunks.length) {
                out.push(`---`);
                out.push(`💡 **后续节预览**: 第 #${maxRead + 1} 节开头为 *"${this._makeSnippet(chunks[maxRead + 1], 80)}"* —— 如需继续阅读，请调用 \`VCPKnowledge(command="read", doc=${JSON.stringify(shortTargetPath)}, chunk="${maxRead + 1}-${Math.min(chunks.length - 1, maxRead + 3)}")\`。`);
            }

            return { content: [{ type: 'text', text: out.join('\n') }] };
        }

        const query = String(queryArg || docArg || '').trim();
        if (!query) {
            return { content: [{ type: 'text', text: '请提供 query（检索词）或 doc（文档路径）参数。' }] };
        }

        const k = Math.max(1, Math.min(15, parseInt(args.k ?? args.top_k ?? 4, 10) || 4));
        const libraries = libArg
            ? String(libArg).split(/[|,，]/).map(s => s.trim()).filter(Boolean)
            : null;

        let explicitDocFilter = null;
        if (docArg && queryArg) {
            const target = this._resolveTargetDoc(manager, docArg, libArg);
            if (target) {
                const shortP = this._stripLibraryPrefix(target.library, target.path);
                explicitDocFilter = {
                    source_path: {
                        $in: [shortP, target.path, `${target.library}\\${shortP}`, `${target.library}/${shortP}`]
                    }
                };
            }
        }

        const queryVector = await this._getQueryVector(query, manager);
        const radar = !explicitDocFilter
            ? await this.routeAndHighlight(query, { topK: 8, libraries, minScore: 0.22 })
            : null;

        const queryTerms = this._tokenize(query, true);
        const radarDocBonus = new Map();
        const candidatePool = [];
        if (radar?.highlights?.length) {
            for (const h of radar.highlights) {
                const shortP = this._stripLibraryPrefix(h.library, h.path);
                radarDocBonus.set(`${h.library}\u0000${shortP}`, h.score);
                if (h.pinpoints?.length) {
                    for (const p of h.pinpoints) {
                        candidatePool.push({
                            library: h.library,
                            sourceFile: shortP,
                            chunkIndex: p.chunkIndex,
                            score: Math.max(p.score || 0, h.score * 0.92),
                            text: p.inlineText || p.snippet || ''
                        });
                    }
                } else {
                    try {
                        const loaded = await this._loadDocChunks(manager, { library: h.library, path: shortP });
                        if (loaded?.chunks?.length) {
                            const ranked = loaded.chunks.map((ch, idx) => {
                                const norm = this._normalize(ch);
                                let uniq = 0;
                                let tfSum = 0;
                                for (const t of queryTerms) {
                                    if (t.length >= 2 && norm.includes(t)) {
                                        uniq++;
                                        tfSum += (norm.split(t).length - 1);
                                    }
                                }
                                return { idx, ch, rankScore: uniq * 10 + Math.min(9, tfSum) };
                            }).sort((a, b) => b.rankScore - a.rankScore || a.idx - b.idx);
                            for (const rc of ranked.slice(0, 3)) {
                                candidatePool.push({
                                    library: h.library,
                                    sourceFile: shortP,
                                    chunkIndex: rc.idx,
                                    score: h.score * 0.92 + Math.min(0.06, rc.rankScore * 0.0005),
                                    text: rc.ch
                                });
                            }
                        }
                    } catch (_) {}
                }
            }
        }

        const searchOpts = {
            libraries: libraries && libraries.length > 0 ? libraries : undefined,
            topK: Math.max(k * 4, 16),
            expandDepth: 0,
            minScore: 0.08,
            hybridAlpha: 0.68,
            ...(explicitDocFilter ? { payloadFilter: explicitDocFilter } : {})
        };

        let rawHits = [];
        try {
            rawHits = queryVector
                ? await manager.searchWithVector(queryVector, query, searchOpts)
                : await manager.search(query, searchOpts);
        } catch (_) {
            rawHits = [];
        }

        for (const h of (rawHits || [])) {
            if (h.payload?.type === 'document' || (h.chunkIndex === undefined && !h.text)) continue;
            candidatePool.push(h);
        }

        const dedupedMap = new Map();
        for (const h of candidatePool) {
            const docPath = this._stripLibraryPrefix(h.library, h.sourcePath || h.sourceFile || '');
            if (!docPath) continue;
            const cIdx = Number.isFinite(Number(h.chunkIndex)) ? Number(h.chunkIndex) : 0;
            const uid = `${h.library}\u0000${docPath}#${cIdx}`;

            const rawScore = Number(h.vectorScore ?? h.score) || 0;
            let baseNorm = rawScore > 1.0 ? (rawScore / (rawScore + 1.15)) : Math.max(0, Math.min(0.98, rawScore));
            const docBonus = radarDocBonus.get(`${h.library}\u0000${docPath}`) || 0;
            if (docBonus > 0) {
                baseNorm = Math.min(0.99, baseNorm * 0.72 + docBonus * 0.34);
            }
            const textNorm = this._normalize(`${docPath} ${h.text || ''}`);
            let lexHits = 0;
            for (const term of queryTerms) {
                if (term.length >= 2 && textNorm.includes(term)) lexHits++;
            }
            if (queryTerms.length > 0 && lexHits > 0) {
                baseNorm = Math.min(0.995, baseNorm + Math.min(0.18, lexHits * 0.045));
            }

            const prev = dedupedMap.get(uid);
            if (!prev || baseNorm > prev.finalScore) {
                dedupedMap.set(uid, {
                    library: h.library,
                    docPath,
                    chunkIndex: cIdx,
                    finalScore: baseNorm,
                    previewText: String(h.text || '').trim()
                });
            }
        }

        const finalHits = [...dedupedMap.values()]
            .sort((a, b) => b.finalScore - a.finalScore)
            .slice(0, k);

        if (finalHits.length === 0) {
            return {
                content: [{
                    type: 'text',
                    text: `[VCPKnowledge 检索] 在范围 [${libraries ? libraries.join(', ') : '全部知识库'}] 中未找到与 "${query}" 匹配的片段。`
                }]
            };
        }

        const lines = [
            `## 🔍 VCPKnowledge 检索结果（查询: "${query}" | 命中 ${finalHits.length} 处）\n`
        ];
        for (let i = 0; i < finalHits.length; i++) {
            const h = finalHits[i];
            const pct = `${(h.finalScore * 100).toFixed(1)}%`;
            let bodyText = h.previewText;
            let totalChunks = 0;
            try {
                const loaded = await this._loadDocChunks(manager, { library: h.library, path: h.docPath });
                if (loaded?.chunks?.length) {
                    totalChunks = loaded.chunks.length;
                    const fullChunk = loaded.chunks[h.chunkIndex];
                    if (fullChunk) {
                        bodyText = fullChunk.length > 1800 ? `${fullChunk.slice(0, 1800)}\n…[本节剩余 ${fullChunk.length - 1800} 字可调 read 读取]` : fullChunk;
                    }
                }
            } catch (_) {}
            const totalHint = totalChunks > 0 ? ` / 共 ${totalChunks} 节` : '';
            lines.push(`### ${i + 1}. [${h.library}] ${h.docPath} (第 #${h.chunkIndex} 节${totalHint} | 相关度: ${pct})`);
            lines.push(bodyText || '(无正文预览)');
            lines.push(`> 📍 *如需连读上下文，可调用: \`VCPKnowledge(command="read", doc=${JSON.stringify(h.docPath)}, chunk="${Math.max(0, h.chunkIndex - 1)}-${h.chunkIndex + 1}")\`*\n`);
        }

        return { content: [{ type: 'text', text: lines.join('\n') }] };
    }
}

module.exports = new VCPKnowledgePlugin();