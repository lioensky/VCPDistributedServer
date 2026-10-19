const test = require('node:test');
const assert = require('node:assert/strict');

const { formatKeenableResults, searchKeenable } = require('../KeenableSearch.js');

const PUBLIC_SEARCH_URL = 'https://api.keenable.ai/v1/search/public';
const KEYED_SEARCH_URL = 'https://api.keenable.ai/v1/search';
const FAKE_KEY = 'keenable-super-secret-test-key-should-never-leak';

function makeItem(overrides = {}) {
    return Object.assign({
        title: '示例标题',
        url: 'https://example.com/page',
        description: '',
        snippet: '这是一个示例摘要。'
    }, overrides);
}

/**
 * 构造一个假的 httpPost：记录每次调用，并按顺序返回预置结果。
 * 测试全程不发起真实网络请求。
 */
function makeHttpPost(responder) {
    const calls = [];
    const httpPost = async (url, body, config) => {
        calls.push({ url, body, config });
        return responder(url, body, config, calls.length - 1);
    };
    httpPost.calls = calls;
    return httpPost;
}

function okResponse(results) {
    return { data: { query: 'q', results } };
}

// ---------------------------------------------------------------------------
// formatKeenableResults - pure formatting
// ---------------------------------------------------------------------------

test('formatKeenableResults: formats results as a numbered markdown list', () => {
    const response = {
        results: [
            makeItem({ title: '第一条', url: 'https://a.example/1', snippet: '摘要一' }),
            makeItem({ title: '第二条', url: 'https://a.example/2', snippet: '摘要二' })
        ]
    };
    const md = formatKeenableResults(response);
    assert.match(md, /### 搜索结果/);
    assert.match(md, /1\. \*\*\[第一条\]\(https:\/\/a\.example\/1\)\*\*/);
    assert.match(md, /摘要一/);
    assert.match(md, /2\. \*\*\[第二条\]\(https:\/\/a\.example\/2\)\*\*/);
    assert.match(md, /摘要二/);
});

test('formatKeenableResults: reads snippet, falls back to description only when snippet is missing', () => {
    const fromSnippet = formatKeenableResults({ results: [makeItem({ snippet: '来自 snippet', description: '' })] });
    assert.match(fromSnippet, /来自 snippet/);

    const fromDescription = formatKeenableResults({ results: [makeItem({ snippet: undefined, description: '来自 description' })] });
    assert.match(fromDescription, /来自 description/);
});

test('formatKeenableResults: long snippets are collapsed onto one line and truncated', () => {
    const longSnippet = '第一段\n\n' + '字'.repeat(2000);
    const md = formatKeenableResults({ results: [makeItem({ snippet: longSnippet })] });
    const snippetLine = md.split('\n')[2];
    assert.ok(snippetLine.startsWith('   第一段 字'));
    assert.ok(snippetLine.endsWith('...'));
    assert.equal(snippetLine.trim().length, 600 + 3);
});

test('formatKeenableResults: renders published_at when present', () => {
    const md = formatKeenableResults({ results: [makeItem({ published_at: '2026-10-15T19:00:00Z' })] });
    assert.match(md, /- 发布时间: 2026-10-15T19:00:00Z/);
});

test('formatKeenableResults: missing published_at omits the published line', () => {
    const md = formatKeenableResults({ results: [makeItem()] });
    assert.doesNotMatch(md, /发布时间/);
});

test('formatKeenableResults: empty results array -> not-found message', () => {
    assert.equal(formatKeenableResults({ results: [] }), '未找到相关搜索结果。\n');
});

test('formatKeenableResults: missing results key -> not-found message', () => {
    assert.equal(formatKeenableResults({}), '未找到相关搜索结果。\n');
});

test('formatKeenableResults: null and undefined responses -> not-found message', () => {
    assert.equal(formatKeenableResults(null), '未找到相关搜索结果。\n');
    assert.equal(formatKeenableResults(undefined), '未找到相关搜索结果。\n');
});

test('formatKeenableResults: missing title falls back to placeholder, still renders link', () => {
    const md = formatKeenableResults({ results: [makeItem({ title: undefined })] });
    assert.match(md, /\*\*\[\(无标题\)\]\(https:\/\/example\.com\/page\)\*\*/);
});

test('formatKeenableResults: missing url renders an empty link without throwing', () => {
    const md = formatKeenableResults({ results: [makeItem({ url: undefined })] });
    assert.match(md, /\*\*\[示例标题\]\(\)\*\*/);
});

test('formatKeenableResults: missing snippet and description omits the snippet line', () => {
    const md = formatKeenableResults({ results: [makeItem({ snippet: undefined, description: undefined })] });
    assert.match(md, /\*\*\[示例标题\]/);
    assert.doesNotMatch(md, /这是一个示例摘要/);
});

// ---------------------------------------------------------------------------
// searchKeenable - key handling
// ---------------------------------------------------------------------------

test('searchKeenable: without a key it calls the public endpoint with X-Keenable-Title and no X-API-Key', async () => {
    const httpPost = makeHttpPost(() => okResponse([makeItem()]));
    const out = await searchKeenable('测试', {}, httpPost);
    assert.equal(out.status, 'success');
    assert.equal(httpPost.calls.length, 1);
    assert.equal(httpPost.calls[0].url, PUBLIC_SEARCH_URL);
    assert.equal(httpPost.calls[0].config.headers['X-Keenable-Title'], 'VCP');
    assert.equal(httpPost.calls[0].config.headers['X-API-Key'], undefined);
});

test('searchKeenable: a blank or comma-only key falls back to the public endpoint', async () => {
    for (const apiKey of ['', '   ', ' , , ']) {
        const httpPost = makeHttpPost(() => okResponse([makeItem()]));
        const out = await searchKeenable('测试', { apiKey }, httpPost);
        assert.equal(out.status, 'success');
        assert.equal(httpPost.calls[0].url, PUBLIC_SEARCH_URL, `apiKey=${JSON.stringify(apiKey)}`);
    }
});

test('searchKeenable: with a key it calls the keyed endpoint with X-API-Key', async () => {
    const httpPost = makeHttpPost(() => okResponse([makeItem()]));
    await searchKeenable('测试', { apiKey: FAKE_KEY }, httpPost);
    assert.equal(httpPost.calls[0].url, KEYED_SEARCH_URL);
    assert.equal(httpPost.calls[0].config.headers['X-API-Key'], FAKE_KEY);
    assert.equal(httpPost.calls[0].config.headers['X-Keenable-Title'], 'VCP');
});

test('searchKeenable: a comma-separated key list picks one of the supplied keys', async () => {
    const httpPost = makeHttpPost(() => okResponse([makeItem()]));
    const out = await searchKeenable('测试', { apiKey: 'key-a,key-b' }, httpPost);
    assert.equal(out.status, 'success');
    assert.ok(['key-a', 'key-b'].includes(httpPost.calls[0].config.headers['X-API-Key']));
});

test('searchKeenable: the api key never leaks into an error message', async () => {
    const httpPost = makeHttpPost(() => {
        throw new Error(`Request failed with X-API-Key: ${FAKE_KEY}`);
    });
    const out = await searchKeenable('测试', { apiKey: FAKE_KEY }, httpPost);
    assert.equal(out.status, 'error');
    assert.ok(!out.error.includes(FAKE_KEY));
    assert.match(out.error, /\[REDACTED\]/);
});

// ---------------------------------------------------------------------------
// searchKeenable - request construction
// ---------------------------------------------------------------------------

test('searchKeenable: sends the query in a JSON body', async () => {
    const httpPost = makeHttpPost(() => okResponse([makeItem()]));
    await searchKeenable('大语言模型', {}, httpPost);
    const call = httpPost.calls[0];
    assert.equal(call.body.query, '大语言模型');
    assert.equal(call.config.headers['Content-Type'], 'application/json');
});

test('searchKeenable: count defaults to 10 and is clamped to 20', async () => {
    const cases = [
        [undefined, 10],
        [5, 5],
        [50, 20],
        [0, 10],
        [-3, 10],
        ['abc', 10],
        ['7', 7]
    ];

    for (const [input, expected] of cases) {
        const httpPost = makeHttpPost(() => okResponse([makeItem()]));
        await searchKeenable('测试', { count: input }, httpPost);
        assert.equal(httpPost.calls[0].body.max_results, expected, `count=${input}`);
    }
});

test('searchKeenable: site is passed through, blank site is omitted', async () => {
    const withSite = makeHttpPost(() => okResponse([makeItem()]));
    await searchKeenable('测试', { site: ' github.com ' }, withSite);
    assert.equal(withSite.calls[0].body.site, 'github.com');

    const blank = makeHttpPost(() => okResponse([makeItem()]));
    await searchKeenable('测试', { site: '   ' }, blank);
    assert.equal(blank.calls[0].body.site, undefined);
});

test('searchKeenable: freshness maps onto a published_after date', async () => {
    const now = new Date('2026-10-19T12:00:00Z');
    const cases = [
        ['day', '2026-10-18'],
        ['week', '2026-10-12'],
        ['month', '2026-09-19'],
        ['year', '2025-10-19'],
        ['WEEK', '2026-10-12']
    ];

    for (const [input, expected] of cases) {
        const httpPost = makeHttpPost(() => okResponse([makeItem()]));
        await searchKeenable('测试', { freshness: input, now }, httpPost);
        assert.equal(httpPost.calls[0].body.published_after, expected, `freshness=${input}`);
    }
});

test('searchKeenable: freshness all or an unknown value sends no date filter', async () => {
    for (const freshness of ['all', 'decade', undefined]) {
        const httpPost = makeHttpPost(() => okResponse([makeItem()]));
        await searchKeenable('测试', { freshness }, httpPost);
        assert.equal(httpPost.calls[0].body.published_after, undefined, `freshness=${freshness}`);
    }
});

test('searchKeenable: explicit published_after wins over freshness, published_before is passed through', async () => {
    const httpPost = makeHttpPost(() => okResponse([makeItem()]));
    await searchKeenable('测试', {
        freshness: 'day',
        published_after: '2026-01-01',
        published_before: '2026-06-30',
        now: new Date('2026-10-19T12:00:00Z')
    }, httpPost);
    assert.equal(httpPost.calls[0].body.published_after, '2026-01-01');
    assert.equal(httpPost.calls[0].body.published_before, '2026-06-30');
});

test('searchKeenable: malformed dates are dropped rather than sent through', async () => {
    const httpPost = makeHttpPost(() => okResponse([makeItem()]));
    await searchKeenable('测试', { published_after: '2026/01/01', published_before: 'yesterday' }, httpPost);
    assert.equal(httpPost.calls[0].body.published_after, undefined);
    assert.equal(httpPost.calls[0].body.published_before, undefined);
});

// ---------------------------------------------------------------------------
// searchKeenable - the | separator
// ---------------------------------------------------------------------------

test('searchKeenable: a single query issues exactly one request', async () => {
    const httpPost = makeHttpPost(() => okResponse([makeItem()]));
    const out = await searchKeenable('单个查询', {}, httpPost);
    assert.equal(out.status, 'success');
    assert.equal(httpPost.calls.length, 1);
    assert.doesNotMatch(out.result, /## 🔍 查询:/);
});

test('searchKeenable: a | separated query fans out and labels each section', async () => {
    const httpPost = makeHttpPost((url, body) => okResponse([makeItem({ title: `命中-${body.query}` })]));
    const out = await searchKeenable('查询甲 | 查询乙 | 查询丙', {}, httpPost);

    assert.equal(out.status, 'success');
    assert.equal(httpPost.calls.length, 3);
    assert.deepEqual(httpPost.calls.map(c => c.body.query), ['查询甲', '查询乙', '查询丙']);
    assert.match(out.result, /## 🔍 查询: 查询甲/);
    assert.match(out.result, /## 🔍 查询: 查询乙/);
    assert.match(out.result, /## 🔍 查询: 查询丙/);
    assert.match(out.result, /命中-查询丙/);
});

test('searchKeenable: empty segments between separators are dropped', async () => {
    const httpPost = makeHttpPost(() => okResponse([makeItem()]));
    await searchKeenable('  甲 ||  | 乙  ', {}, httpPost);
    assert.deepEqual(httpPost.calls.map(c => c.body.query), ['甲', '乙']);
});

test('searchKeenable: a query of only separators returns an error', async () => {
    const httpPost = makeHttpPost(() => okResponse([makeItem()]));
    const out = await searchKeenable(' | | ', {}, httpPost);
    assert.equal(out.status, 'error');
    assert.match(out.error, /No valid search query/);
    assert.equal(httpPost.calls.length, 0);
});

test('searchKeenable: a non-string query returns an error rather than throwing', async () => {
    const httpPost = makeHttpPost(() => okResponse([makeItem()]));
    const out = await searchKeenable(undefined, {}, httpPost);
    assert.equal(out.status, 'error');
    assert.match(out.error, /No valid search query/);
});

// ---------------------------------------------------------------------------
// searchKeenable - failure handling
// ---------------------------------------------------------------------------

test('searchKeenable: a single failing query returns an error result', async () => {
    const httpPost = makeHttpPost(() => {
        throw new Error('Request failed with status code 429');
    });
    const out = await searchKeenable('测试', {}, httpPost);
    assert.equal(out.status, 'error');
    assert.match(out.error, /Keenable Search Error: Request failed with status code 429/);
});

test('searchKeenable: a partial failure still returns the successful sections', async () => {
    const httpPost = makeHttpPost((url, body) => {
        if (body.query === '会失败') {
            throw new Error('boom');
        }
        return okResponse([makeItem({ title: '成功结果' })]);
    });

    const out = await searchKeenable('会成功 | 会失败', {}, httpPost);
    assert.equal(out.status, 'success');
    assert.match(out.result, /## 🔍 查询: 会成功/);
    assert.match(out.result, /成功结果/);
    assert.match(out.result, /## ⚠️ 以下查询失败/);
    assert.match(out.result, /### 查询: 会失败/);
    assert.match(out.result, /错误: boom/);
});

test('searchKeenable: when every sub-query fails the whole call is an error', async () => {
    const httpPost = makeHttpPost(() => {
        throw new Error('all down');
    });
    const out = await searchKeenable('甲 | 乙', {}, httpPost);
    assert.equal(out.status, 'error');
    assert.match(out.error, /Keenable Search Error: all down/);
});

test('searchKeenable: the key is redacted inside a partial-failure section too', async () => {
    const httpPost = makeHttpPost((url, body) => {
        if (body.query === '会失败') {
            throw new Error(`upstream echoed ${FAKE_KEY}`);
        }
        return okResponse([makeItem()]);
    });

    const out = await searchKeenable('会成功 | 会失败', { apiKey: FAKE_KEY }, httpPost);
    assert.equal(out.status, 'success');
    assert.ok(!out.result.includes(FAKE_KEY));
    assert.match(out.result, /\[REDACTED\]/);
});

test('searchKeenable: an empty upstream body yields the not-found message, not a crash', async () => {
    const httpPost = makeHttpPost(() => ({ data: null }));
    const out = await searchKeenable('测试', {}, httpPost);
    assert.equal(out.status, 'success');
    assert.equal(out.result, '未找到相关搜索结果。\n');
});
