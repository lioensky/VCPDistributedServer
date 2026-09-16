const test = require('node:test');
const assert = require('node:assert/strict');

const { formatSerplyResults, searchSerply } = require('../SerplySearch.js');

const SERPLY_SEARCH_URL = 'https://api.serply.io/v1/search';
const FAKE_KEY = 'serply-super-secret-test-key-should-never-leak';

function makeItem(overrides = {}) {
    return Object.assign({
        title: '示例标题',
        link: 'https://example.com/page',
        description: '这是一个示例描述。',
        position: 1,
        realPosition: 1,
        result_type: 'organic',
        metadata: { display_url: 'example.com' }
    }, overrides);
}

/**
 * 构造一个假的 httpGet：记录每次调用，并按顺序返回预置结果。
 * 测试全程不发起真实网络请求。
 */
function makeHttpGet(responder) {
    const calls = [];
    const httpGet = async (url, config) => {
        calls.push({ url, config });
        return responder(url, config, calls.length - 1);
    };
    httpGet.calls = calls;
    return httpGet;
}

function okResponse(results) {
    return { data: { results } };
}

// ---------------------------------------------------------------------------
// formatSerplyResults - pure formatting
// ---------------------------------------------------------------------------

test('formatSerplyResults: formats results as a numbered markdown list', () => {
    const response = {
        results: [
            makeItem({ title: '第一条', link: 'https://a.example/1', description: '描述一' }),
            makeItem({ title: '第二条', link: 'https://a.example/2', description: '描述二' })
        ]
    };
    const md = formatSerplyResults(response, false);
    assert.match(md, /### 搜索结果/);
    assert.match(md, /1\. \*\*\[第一条\]\(https:\/\/a\.example\/1\)\*\*/);
    assert.match(md, /描述一/);
    assert.match(md, /2\. \*\*\[第二条\]\(https:\/\/a\.example\/2\)\*\*/);
    assert.match(md, /描述二/);
});

test('formatSerplyResults: news mode switches the section heading', () => {
    const md = formatSerplyResults({ results: [makeItem()] }, true);
    assert.match(md, /### 新闻结果/);
    assert.doesNotMatch(md, /### 搜索结果/);
});

test('formatSerplyResults: renders published_time when metadata carries it', () => {
    const response = { results: [makeItem({ metadata: { published_time: '8 hours ago' } })] };
    const md = formatSerplyResults(response, true);
    assert.match(md, /- 发布时间: 8 hours ago/);
});

test('formatSerplyResults: falls back to metadata.attributes for the published time', () => {
    // 部分区域的新闻结果不返回 published_time，而是返回 attributes 数组。
    const response = { results: [makeItem({ metadata: { attributes: ['Il y a 2 jours', 'il y a 3 heures'] } })] };
    const md = formatSerplyResults(response, true);
    assert.match(md, /- 发布时间: Il y a 2 jours/);
});

test('formatSerplyResults: metadata without a time field omits the published line', () => {
    const md = formatSerplyResults({ results: [makeItem()] }, false);
    assert.doesNotMatch(md, /发布时间/);
});

test('formatSerplyResults: empty results array -> not-found message', () => {
    assert.equal(formatSerplyResults({ results: [] }, false), '未找到相关搜索结果。\n');
});

test('formatSerplyResults: missing results key -> not-found message', () => {
    assert.equal(formatSerplyResults({}, false), '未找到相关搜索结果。\n');
});

test('formatSerplyResults: null and undefined responses -> not-found message', () => {
    assert.equal(formatSerplyResults(null, false), '未找到相关搜索结果。\n');
    assert.equal(formatSerplyResults(undefined, false), '未找到相关搜索结果。\n');
});

test('formatSerplyResults: missing title falls back to placeholder, still renders link', () => {
    const md = formatSerplyResults({ results: [makeItem({ title: undefined })] }, false);
    assert.match(md, /\*\*\[\(无标题\)\]\(https:\/\/example\.com\/page\)\*\*/);
});

test('formatSerplyResults: missing link renders an empty link without throwing', () => {
    const md = formatSerplyResults({ results: [makeItem({ link: undefined })] }, false);
    assert.match(md, /\*\*\[示例标题\]\(\)\*\*/);
});

test('formatSerplyResults: missing description omits the description line', () => {
    const md = formatSerplyResults({ results: [makeItem({ description: undefined })] }, false);
    assert.match(md, /\*\*\[示例标题\]/);
    assert.doesNotMatch(md, /这是一个示例描述/);
});

// ---------------------------------------------------------------------------
// searchSerply - key handling
// ---------------------------------------------------------------------------

test('searchSerply: missing api key returns an error without calling the network', async () => {
    const httpGet = makeHttpGet(() => okResponse([makeItem()]));
    const out = await searchSerply('测试', {}, httpGet);
    assert.equal(out.status, 'error');
    assert.match(out.error, /SerplyKey environment variable not set/);
    assert.equal(httpGet.calls.length, 0);
});

test('searchSerply: a comma-only key is rejected', async () => {
    const httpGet = makeHttpGet(() => okResponse([makeItem()]));
    const out = await searchSerply('测试', { apiKey: ' , , ' }, httpGet);
    assert.equal(out.status, 'error');
    assert.match(out.error, /empty or contains only commas/);
    assert.equal(httpGet.calls.length, 0);
});

test('searchSerply: a comma-separated key list picks one of the supplied keys', async () => {
    const httpGet = makeHttpGet(() => okResponse([makeItem()]));
    const out = await searchSerply('测试', { apiKey: 'key-a,key-b' }, httpGet);
    assert.equal(out.status, 'success');
    assert.ok(['key-a', 'key-b'].includes(httpGet.calls[0].config.headers['X-Api-Key']));
});

test('searchSerply: the api key never leaks into an error message', async () => {
    const httpGet = makeHttpGet(() => {
        throw new Error(`Request failed with X-Api-Key: ${FAKE_KEY}`);
    });
    const out = await searchSerply('测试', { apiKey: FAKE_KEY }, httpGet);
    assert.equal(out.status, 'error');
    assert.ok(!out.error.includes(FAKE_KEY));
    assert.match(out.error, /\[REDACTED\]/);
});

// ---------------------------------------------------------------------------
// searchSerply - request construction
// ---------------------------------------------------------------------------

test('searchSerply: sends the query, the key header and an explicit User-Agent', async () => {
    const httpGet = makeHttpGet(() => okResponse([makeItem()]));
    await searchSerply('大语言模型', { apiKey: FAKE_KEY }, httpGet);

    const call = httpGet.calls[0];
    assert.equal(call.url, SERPLY_SEARCH_URL);
    assert.equal(call.config.params.q, '大语言模型');
    assert.equal(call.config.headers['X-Api-Key'], FAKE_KEY);
    // Serply 在 Cloudflare 之后，缺少 User-Agent 会被拦截返回 error 1010。
    assert.ok(call.config.headers['User-Agent']);
});

test('searchSerply: count defaults to 10 and is clamped to the Serply ceiling of 10', async () => {
    const cases = [
        [undefined, 10],
        [5, 5],
        [20, 10],
        [0, 10],
        [-3, 10],
        ['abc', 10],
        ['7', 7]
    ];

    for (const [input, expected] of cases) {
        const httpGet = makeHttpGet(() => okResponse([makeItem()]));
        await searchSerply('测试', { apiKey: FAKE_KEY, count: input }, httpGet);
        assert.equal(httpGet.calls[0].config.params.num, expected, `count=${input}`);
    }
});

test('searchSerply: topic news sets tbm=nws, general leaves it unset', async () => {
    const news = makeHttpGet(() => okResponse([makeItem()]));
    await searchSerply('测试', { apiKey: FAKE_KEY, topic: 'news' }, news);
    assert.equal(news.calls[0].config.params.tbm, 'nws');

    const general = makeHttpGet(() => okResponse([makeItem()]));
    await searchSerply('测试', { apiKey: FAKE_KEY, topic: 'general' }, general);
    assert.equal(general.calls[0].config.params.tbm, undefined);
});

test('searchSerply: time_range maps onto tbs=qdr:*, including the short aliases', async () => {
    const cases = [
        ['day', 'qdr:d'],
        ['week', 'qdr:w'],
        ['month', 'qdr:m'],
        ['year', 'qdr:y'],
        ['d', 'qdr:d'],
        ['w', 'qdr:w'],
        ['m', 'qdr:m'],
        ['y', 'qdr:y'],
        ['WEEK', 'qdr:w']
    ];

    for (const [input, expected] of cases) {
        const httpGet = makeHttpGet(() => okResponse([makeItem()]));
        await searchSerply('测试', { apiKey: FAKE_KEY, time_range: input }, httpGet);
        assert.equal(httpGet.calls[0].config.params.tbs, expected, `time_range=${input}`);
    }
});

test('searchSerply: an unknown time_range is dropped rather than sent through', async () => {
    const httpGet = makeHttpGet(() => okResponse([makeItem()]));
    await searchSerply('测试', { apiKey: FAKE_KEY, time_range: 'decade' }, httpGet);
    assert.equal(httpGet.calls[0].config.params.tbs, undefined);
});

test('searchSerply: country and language map onto gl and hl', async () => {
    const httpGet = makeHttpGet(() => okResponse([makeItem()]));
    await searchSerply('测试', { apiKey: FAKE_KEY, country: 'US', language: 'EN' }, httpGet);
    assert.equal(httpGet.calls[0].config.params.gl, 'us');
    assert.equal(httpGet.calls[0].config.params.hl, 'en');
});

test('searchSerply: blank country and language are omitted', async () => {
    const httpGet = makeHttpGet(() => okResponse([makeItem()]));
    await searchSerply('测试', { apiKey: FAKE_KEY, country: '   ', language: '' }, httpGet);
    assert.equal(httpGet.calls[0].config.params.gl, undefined);
    assert.equal(httpGet.calls[0].config.params.hl, undefined);
});

// ---------------------------------------------------------------------------
// searchSerply - the | separator
// ---------------------------------------------------------------------------

test('searchSerply: a single query issues exactly one request', async () => {
    const httpGet = makeHttpGet(() => okResponse([makeItem()]));
    const out = await searchSerply('单个查询', { apiKey: FAKE_KEY }, httpGet);
    assert.equal(out.status, 'success');
    assert.equal(httpGet.calls.length, 1);
    assert.doesNotMatch(out.result, /## 🔍 查询:/);
});

test('searchSerply: a | separated query fans out and labels each section', async () => {
    const httpGet = makeHttpGet((url, config) => okResponse([makeItem({ title: `命中-${config.params.q}` })]));
    const out = await searchSerply('查询甲 | 查询乙 | 查询丙', { apiKey: FAKE_KEY }, httpGet);

    assert.equal(out.status, 'success');
    assert.equal(httpGet.calls.length, 3);
    assert.deepEqual(httpGet.calls.map(c => c.config.params.q), ['查询甲', '查询乙', '查询丙']);
    assert.match(out.result, /## 🔍 查询: 查询甲/);
    assert.match(out.result, /## 🔍 查询: 查询乙/);
    assert.match(out.result, /## 🔍 查询: 查询丙/);
    assert.match(out.result, /命中-查询丙/);
});

test('searchSerply: empty segments between separators are dropped', async () => {
    const httpGet = makeHttpGet(() => okResponse([makeItem()]));
    await searchSerply('  甲 ||  | 乙  ', { apiKey: FAKE_KEY }, httpGet);
    assert.deepEqual(httpGet.calls.map(c => c.config.params.q), ['甲', '乙']);
});

test('searchSerply: a query of only separators returns an error', async () => {
    const httpGet = makeHttpGet(() => okResponse([makeItem()]));
    const out = await searchSerply(' | | ', { apiKey: FAKE_KEY }, httpGet);
    assert.equal(out.status, 'error');
    assert.match(out.error, /No valid search query/);
    assert.equal(httpGet.calls.length, 0);
});

test('searchSerply: a non-string query returns an error rather than throwing', async () => {
    const httpGet = makeHttpGet(() => okResponse([makeItem()]));
    const out = await searchSerply(undefined, { apiKey: FAKE_KEY }, httpGet);
    assert.equal(out.status, 'error');
    assert.match(out.error, /No valid search query/);
});

// ---------------------------------------------------------------------------
// searchSerply - failure handling
// ---------------------------------------------------------------------------

test('searchSerply: a single failing query returns an error result', async () => {
    const httpGet = makeHttpGet(() => {
        throw new Error('Request failed with status code 401');
    });
    const out = await searchSerply('测试', { apiKey: FAKE_KEY }, httpGet);
    assert.equal(out.status, 'error');
    assert.match(out.error, /Serply Search Error: Request failed with status code 401/);
});

test('searchSerply: a partial failure still returns the successful sections', async () => {
    const httpGet = makeHttpGet((url, config) => {
        if (config.params.q === '会失败') {
            throw new Error('boom');
        }
        return okResponse([makeItem({ title: '成功结果' })]);
    });

    const out = await searchSerply('会成功 | 会失败', { apiKey: FAKE_KEY }, httpGet);
    assert.equal(out.status, 'success');
    assert.match(out.result, /## 🔍 查询: 会成功/);
    assert.match(out.result, /成功结果/);
    assert.match(out.result, /## ⚠️ 以下查询失败/);
    assert.match(out.result, /### 查询: 会失败/);
    assert.match(out.result, /错误: boom/);
});

test('searchSerply: when every sub-query fails the whole call is an error', async () => {
    const httpGet = makeHttpGet(() => {
        throw new Error('all down');
    });
    const out = await searchSerply('甲 | 乙', { apiKey: FAKE_KEY }, httpGet);
    assert.equal(out.status, 'error');
    assert.match(out.error, /Serply Search Error: all down/);
});

test('searchSerply: the key is redacted inside a partial-failure section too', async () => {
    const httpGet = makeHttpGet((url, config) => {
        if (config.params.q === '会失败') {
            throw new Error(`upstream echoed ${FAKE_KEY}`);
        }
        return okResponse([makeItem()]);
    });

    const out = await searchSerply('会成功 | 会失败', { apiKey: FAKE_KEY }, httpGet);
    assert.equal(out.status, 'success');
    assert.ok(!out.result.includes(FAKE_KEY));
    assert.match(out.result, /\[REDACTED\]/);
});

test('searchSerply: an empty upstream body yields the not-found message, not a crash', async () => {
    const httpGet = makeHttpGet(() => ({ data: null }));
    const out = await searchSerply('测试', { apiKey: FAKE_KEY }, httpGet);
    assert.equal(out.status, 'success');
    assert.equal(out.result, '未找到相关搜索结果。\n');
});
