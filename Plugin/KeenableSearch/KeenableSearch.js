#!/usr/bin/env node
'use strict';

const fs = require('fs');
const path = require('path');
const stdin = require('process').stdin;

// 未配置 KeenableKey 时走免密钥公共端点；配置后走带密钥端点，仅用于提升速率限制。
const KEENABLE_PUBLIC_SEARCH_URL = 'https://api.keenable.ai/v1/search/public';
const KEENABLE_SEARCH_URL = 'https://api.keenable.ai/v1/search';
// 免密钥调用必须携带 X-Keenable-Title 标识调用方应用，否则接口返回 400。
const KEENABLE_TITLE = 'VCP';
const DEFAULT_COUNT = 10;
const MAX_COUNT = 20;
// Keenable 的 snippet 是页面正文摘录，单条可能长达数千字符，这里截断以控制上下文长度。
const MAX_SNIPPET_LENGTH = 600;
const FRESHNESS_DAYS = { day: 1, week: 7, month: 30, year: 365 };
const DATE_PATTERN = /^\d{4}-\d{2}-\d{2}$/;

/**
 * 取出单条结果的摘要文本：合并空白并截断。
 * Keenable 的 description 字段恒为空，正文摘录在 snippet 中；仅在 snippet 缺失时兜底读取 description。
 */
function extractSnippet(item) {
    const raw = [item.snippet, item.description].find(s => typeof s === 'string' && s.trim());
    if (!raw) {
        return '';
    }
    const text = raw.replace(/\s+/g, ' ').trim();
    return text.length > MAX_SNIPPET_LENGTH ? `${text.slice(0, MAX_SNIPPET_LENGTH)}...` : text;
}

/**
 * 格式化单条搜索结果为 Markdown 列表项。
 * 对缺失字段进行防御处理，永不抛出异常。
 */
function formatOneResult(index, item) {
    item = item || {};
    const title = (typeof item.title === 'string' && item.title.trim()) ? item.title.trim() : '(无标题)';
    const url = (typeof item.url === 'string') ? item.url : '';

    let md = `${index}. **[${title}](${url})**\n`;

    const snippet = extractSnippet(item);
    if (snippet) {
        md += `   ${snippet}\n`;
    }

    if (typeof item.published_at === 'string' && item.published_at.trim()) {
        md += `   - 发布时间: ${item.published_at.trim()}\n`;
    }

    md += '\n';
    return md;
}

/**
 * 将 Keenable 搜索响应格式化为 Markdown。
 * 纯函数：不发起任何网络请求，对 null/undefined/畸形结构进行防御处理。
 */
function formatKeenableResults(response) {
    const results = (response && typeof response === 'object' && Array.isArray(response.results))
        ? response.results
        : [];

    if (results.length === 0) {
        return '未找到相关搜索结果。\n';
    }

    let md = '### 搜索结果\n';
    results.forEach((item, idx) => {
        md += formatOneResult(idx + 1, item);
    });

    return md;
}

/**
 * 解析 KeenableKey：可选配置，未设置时返回 { key: null } 走免密钥端点。
 * 支持逗号分隔的多个 Key，随机挑选一个使用（与 TavilyKey 逻辑一致）。
 * allKeys 包含所有候选 Key（用于后续对错误消息做防泄露脱敏），不仅仅是被选中的那一个。
 */
function resolveApiKey(rawKey) {
    if (!rawKey || typeof rawKey !== 'string' || !rawKey.trim()) {
        return { key: null, allKeys: [] };
    }

    const keys = rawKey.split(',').map(k => k.trim()).filter(k => k.length > 0);
    if (keys.length === 0) {
        return { key: null, allKeys: [] };
    }
    return { key: keys[Math.floor(Math.random() * keys.length)], allKeys: keys };
}

/**
 * 对外部错误消息中可能出现的 API Key 原文进行脱敏替换，防止密钥通过底层 HTTP 库的
 * 错误信息意外泄露到插件输出中。
 */
function redactSecrets(message, secrets) {
    if (typeof message !== 'string' || !Array.isArray(secrets)) {
        return message;
    }
    let sanitized = message;
    for (const secret of secrets) {
        if (typeof secret === 'string' && secret.length > 0 && sanitized.includes(secret)) {
            sanitized = sanitized.split(secret).join('[REDACTED]');
        }
    }
    return sanitized;
}

/**
 * 归一化 count 参数：非数字/负数/零 -> 默认值 10；超过上限 -> 截断为 20。
 */
function normalizeCount(count) {
    let n = parseInt(count, 10);
    if (isNaN(n) || n <= 0) {
        n = DEFAULT_COUNT;
    }
    if (n > MAX_COUNT) {
        n = MAX_COUNT;
    }
    return n;
}

function normalizeDate(value) {
    return (typeof value === 'string' && DATE_PATTERN.test(value.trim())) ? value.trim() : null;
}

/**
 * 计算 published_after：显式日期优先，否则把 freshness（day/week/month/year）换算为
 * 当前 UTC 日期往前推的 YYYY-MM-DD。无法识别时返回 null，不做时间过滤。
 */
function resolvePublishedAfter(freshness, publishedAfter, now) {
    const explicit = normalizeDate(publishedAfter);
    if (explicit) {
        return explicit;
    }
    const days = (typeof freshness === 'string') ? FRESHNESS_DAYS[freshness.trim().toLowerCase()] : undefined;
    if (!days) {
        return null;
    }
    const base = (now instanceof Date) ? now : new Date();
    return new Date(base.getTime() - days * 24 * 60 * 60 * 1000).toISOString().slice(0, 10);
}

/**
 * 默认的 HTTP POST 实现（生产环境使用，基于 Node.js 18+ 内置 fetch，无需额外依赖）。
 * 测试中会注入替身函数，不发起真实网络请求。
 */
async function defaultHttpPost(url, body, config) {
    const response = await fetch(url, {
        method: 'POST',
        headers: config.headers,
        body: JSON.stringify(body),
        signal: AbortSignal.timeout(config.timeout)
    });
    const text = await response.text();
    if (!response.ok) {
        const detail = text ? `: ${text.substring(0, 200)}` : '';
        throw new Error(`Request failed with status code ${response.status}${detail}`);
    }
    return { data: text ? JSON.parse(text) : null };
}

/**
 * 对单个子查询发起 Keenable 搜索请求，返回响应体（response.data）。
 * 可能抛出异常（网络错误/HTTP 错误），由调用方通过 Promise.allSettled 或 try/catch 处理。
 */
async function fetchSubQuery(subQuery, apiKey, extraBody, httpPost) {
    const headers = {
        'Content-Type': 'application/json',
        'X-Keenable-Title': KEENABLE_TITLE
    };
    if (apiKey) {
        headers['X-API-Key'] = apiKey;
    }
    const response = await httpPost(
        apiKey ? KEENABLE_SEARCH_URL : KEENABLE_PUBLIC_SEARCH_URL,
        Object.assign({ query: subQuery }, extraBody),
        { headers, timeout: 25000 }
    );
    return (response && response.data) ? response.data : null;
}

/**
 * Keenable 搜索核心逻辑。接受可注入的 httpPost（用于测试，避免真实网络请求）。
 * 支持使用 | 分隔的多个查询并发搜索。
 * 契约：永不抛出异常，永远返回 {status:"success", result} 或 {status:"error", error}。
 * 契约：任何输出字符串中都不得包含 apiKey 原文。
 */
async function searchKeenable(query, options = {}, httpPost = defaultHttpPost) {
    // 声明在 try 之外，以便 catch 块也能用它对错误消息脱敏（即使异常发生在解析 Key 之后）。
    let secretsToRedact = [];
    try {
        const {
            apiKey: rawApiKey,
            count,
            site,
            freshness,
            published_after: publishedAfter,
            published_before: publishedBefore,
            now
        } = options || {};

        const resolvedKey = resolveApiKey(rawApiKey);
        const apiKey = resolvedKey.key;
        secretsToRedact = resolvedKey.allKeys;

        const rawQuery = (typeof query === 'string') ? query : '';
        const subQueries = rawQuery.split('|').map(q => q.trim()).filter(q => q.length > 0);

        if (subQueries.length === 0) {
            return { status: 'error', error: "No valid search query after splitting by '|'" };
        }

        const extraBody = { max_results: normalizeCount(count) };
        if (typeof site === 'string' && site.trim()) {
            extraBody.site = site.trim();
        }
        const after = resolvePublishedAfter(freshness, publishedAfter, now);
        if (after) {
            extraBody.published_after = after;
        }
        const before = normalizeDate(publishedBefore);
        if (before) {
            extraBody.published_before = before;
        }

        if (subQueries.length === 1) {
            const data = await fetchSubQuery(subQueries[0], apiKey, extraBody, httpPost);
            return { status: 'success', result: formatKeenableResults(data) };
        }

        // 多个子查询 => 并发搜索
        const settled = await Promise.allSettled(
            subQueries.map(subQuery =>
                fetchSubQuery(subQuery, apiKey, extraBody, httpPost).then(data => ({ subQuery, data }))
            )
        );

        let markdownResult = '';
        const failedResults = [];
        let hasAnySuccess = false;

        settled.forEach((result, idx) => {
            if (result.status === 'fulfilled') {
                hasAnySuccess = true;
                const { subQuery, data } = result.value;
                markdownResult += `## 🔍 查询: ${subQuery}\n\n`;
                markdownResult += formatKeenableResults(data);
                markdownResult += '\n\n---\n\n';
            } else {
                const rawReasonMessage = (result.reason && result.reason.message) ? result.reason.message : '未知错误';
                const reasonMessage = redactSecrets(rawReasonMessage, secretsToRedact);
                failedResults.push({ subQuery: subQueries[idx], error: reasonMessage });
            }
        });

        if (failedResults.length > 0) {
            markdownResult += `## ⚠️ 以下查询失败\n\n`;
            for (const fail of failedResults) {
                markdownResult += `### 查询: ${fail.subQuery}\n`;
                markdownResult += `错误: ${fail.error}\n\n`;
            }
        }

        if (!hasAnySuccess) {
            const firstError = failedResults.length > 0 ? failedResults[0].error : '未知错误';
            return { status: 'error', error: `Keenable Search Error: ${firstError}` };
        }

        return { status: 'success', result: markdownResult };
    } catch (e) {
        const rawMessage = (e && e.message) ? e.message : 'An unknown error occurred.';
        const message = redactSecrets(rawMessage, secretsToRedact);
        return { status: 'error', error: `Keenable Search Error: ${message}` };
    }
}

function loadLocalEnvIfNeeded() {
    if (process.env.KeenableKey) {
        return;
    }

    const envPath = path.join(__dirname, 'config.env');
    if (!fs.existsSync(envPath)) {
        return;
    }

    const envContent = fs.readFileSync(envPath, 'utf8');
    for (const line of envContent.split(/\r?\n/)) {
        const trimmed = line.trim();
        if (!trimmed || trimmed.startsWith('#')) {
            continue;
        }

        const separatorIndex = trimmed.indexOf('=');
        if (separatorIndex <= 0) {
            continue;
        }

        const key = trimmed.slice(0, separatorIndex).trim();
        let value = trimmed.slice(separatorIndex + 1).trim();
        if ((value.startsWith('"') && value.endsWith('"')) || (value.startsWith("'") && value.endsWith("'"))) {
            value = value.slice(1, -1);
        }

        if (key && process.env[key] === undefined) {
            process.env[key] = value;
        }
    }
}

async function main() {
    loadLocalEnvIfNeeded();
    let inputData = '';
    stdin.setEncoding('utf8');

    stdin.on('data', function (chunk) {
        inputData += chunk;
    });

    stdin.on('end', async function () {
        let output;

        try {
            if (!inputData.trim()) {
                throw new Error('No input data received from stdin.');
            }

            const data = JSON.parse(inputData);

            output = await searchKeenable(data.query, {
                apiKey: process.env.KeenableKey,
                count: data.count,
                site: data.site,
                freshness: data.freshness,
                published_after: data.published_after,
                published_before: data.published_before
            });
        } catch (e) {
            let errorMessage;
            if (e instanceof SyntaxError) {
                errorMessage = 'Invalid JSON input.';
            } else if (e instanceof Error) {
                errorMessage = e.message;
            } else {
                errorMessage = 'An unknown error occurred.';
            }
            output = { status: 'error', error: `Keenable Search Error: ${errorMessage}` };
        }

        // Output JSON to stdout
        process.stdout.write(JSON.stringify(output, null, 2));
    });
}

if (require.main === module) {
    main().catch(error => {
        // Catch any unhandled promise rejections from main
        process.stdout.write(JSON.stringify({ status: 'error', error: `Unhandled Plugin Error: ${error.message || error}` }));
        process.exit(1); // Indicate failure
    });
}

module.exports = {
    formatKeenableResults,
    searchKeenable
};
