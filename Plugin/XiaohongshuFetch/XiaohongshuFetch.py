#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
XiaohongshuFetch - 小红书笔记解析插件 v4.0
策略：Cookie + xsec_token HTML降级解析（纯 requests，无外部签名依赖）
作者：Nova (2026-02-28)
"""

import sys
import json
import os
import re
import logging
import requests
from urllib.parse import urlencode

# --- 最优先：手动加载本插件目录下的 config.env ---
_PLUGIN_DIR = os.path.dirname(os.path.abspath(__file__))
_CONFIG_PATH = os.path.join(_PLUGIN_DIR, 'config.env')
if os.path.exists(_CONFIG_PATH):
    with open(_CONFIG_PATH, 'r', encoding='utf-8') as _f:
        for _line in _f:
            _line = _line.strip()
            if _line and not _line.startswith('#') and '=' in _line:
                _k, _v = _line.split('=', 1)
                os.environ.setdefault(_k.strip(), _v.strip())

# --- 日志配置 ---
class UTF8StreamHandler(logging.StreamHandler):
    def emit(self, record):
        try:
            msg = self.format(record)
            stream = self.stream
            if hasattr(stream, 'buffer'):
                stream.buffer.write((msg + self.terminator).encode('utf-8'))
                stream.buffer.flush()
            else:
                stream.write(msg + self.terminator)
                self.flush()
        except Exception:
            self.handleError(record)

handler = UTF8StreamHandler(sys.stderr)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logging.getLogger().addHandler(handler)
logging.getLogger().setLevel(logging.INFO)

TIMEOUT = int(os.environ.get('REQUEST_TIMEOUT', 20))

BASE_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Origin': 'https://www.xiaohongshu.com',
    'Referer': 'https://www.xiaohongshu.com/',
    'Connection': 'keep-alive',
}

# ───────────────────────────────────────────────
# 工具函数
# ───────────────────────────────────────────────

def extract_note_id(url):
    match = re.search(r'/(?:discovery/item|explore)/([a-f0-9]{24})', url)
    if match:
        return match.group(1)
    match = re.search(r'/(?:discovery/item|explore)/([a-f0-9]+)', url)
    if match:
        return match.group(1)
    match = re.search(r'[?&]source_note_id=([a-f0-9]+)', url)
    if match:
        return match.group(1)
    return None

def extract_xsec_token(url):
    match = re.search(r'[?&]xsec_token=([^&]+)', url)
    if match:
        return match.group(1)
    return ''

def resolve_short_url(url):
    if 'xhslink.com' not in url:
        return url
    try:
        resp = requests.get(url, allow_redirects=True, timeout=TIMEOUT,
                            headers={'User-Agent': BASE_HEADERS['User-Agent']})
        logging.info('短链解析: %s -> %s', url, resp.url)
        return resp.url
    except Exception as e:
        logging.error('短链解析失败: %s', e)
        return url

def build_cookies_dict(a1, web_session, web_id):
    full = os.environ.get('XHS_COOKIE_FULL', '').strip()
    if full:
        cookie_dict = {}
        for part in full.split(';'):
            part = part.strip()
            if '=' in part:
                k, v = part.split('=', 1)
                cookie_dict[k.strip()] = v.strip()
        return cookie_dict
    cookie_dict = {}
    if a1:
        cookie_dict['a1'] = a1
    if web_session:
        cookie_dict['web_session'] = web_session
    if web_id:
        cookie_dict['webId'] = web_id
    return cookie_dict

def bracket_balance_extract(html, marker):
    """
    从 html 中找到 marker 后的第一个完整 JSON 对象。
    正确处理转义字符：i+=2 跳过转义序列，避免 \" 误翻转 in_str。
    """
    idx = html.find(marker)
    if idx < 0:
        return None
    brace_start = html.find('{', idx)
    if brace_start < 0:
        return None
    depth = 0
    in_str = False
    i = brace_start
    limit = min(brace_start + 500000, len(html))
    while i < limit:
        ch = html[i]
        if in_str:
            if ch == '\\':
                i += 2
                continue
            if ch == '"':
                in_str = False
        else:
            if ch == '"':
                in_str = True
            elif ch == '{':
                depth += 1
            elif ch == '}':
                depth -= 1
                if depth == 0:
                    raw_json = html[brace_start:i + 1]
                    raw_json = re.sub(r'\bundefined\b', 'null', raw_json)
                    raw_json = re.sub(r'new Map\(\[.*?\]\)', '{}', raw_json)
                    raw_json = re.sub(r'new Set\(\[.*?\]\)', '[]', raw_json)
                    try:
                        state = json.loads(raw_json)
                        logging.info('bracket-balance OK, len=%d', len(raw_json))
                        return state
                    except json.JSONDecodeError as e:
                        logging.error('JSON parse fail: %s', str(e)[:100])
                        return None
        i += 1
    logging.error('bracket-balance: 未找到匹配闭合括号')
    return None

# ───────────────────────────────────────────────
# HTML 解析策略
# ───────────────────────────────────────────────

def fetch_html(url, cookies_dict):
    headers = dict(BASE_HEADERS)
    headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    headers['Upgrade-Insecure-Requests'] = '1'
    headers['Sec-Fetch-Dest'] = 'document'
    headers['Sec-Fetch-Mode'] = 'navigate'
    headers['Sec-Fetch-Site'] = 'none'
    cookie_str = '; '.join(f'{k}={v}' for k, v in cookies_dict.items())
    if cookie_str:
        headers['Cookie'] = cookie_str
    try:
        resp = requests.get(url, headers=headers, timeout=TIMEOUT, allow_redirects=True)
        resp.raise_for_status()
        logging.info('HTML GET %s -> %d, len=%d', url, resp.status_code, len(resp.text))
        return resp.text
    except Exception as e:
        logging.error('HTML 请求失败 %s: %s', url, e)
        return None

def parse_state_from_html(html):
    state = bracket_balance_extract(html, 'window.__INITIAL_STATE__')
    if state:
        return state
    fb_m = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', html, re.DOTALL)
    if fb_m:
        try:
            state = json.loads(fb_m.group(1))
            logging.info('NEXT_DATA fallback OK')
            return state
        except json.JSONDecodeError:
            pass
    return None

def extract_note_from_state(state, note_id):
    note = None
    note_map = state.get('note', {}).get('noteDetailMap', {})
    if note_id in note_map:
        note = note_map[note_id].get('note', note_map[note_id])
    if not note and note_map:
        first_key = list(note_map.keys())[0]
        first_val = note_map[first_key]
        if isinstance(first_val, dict):
            note = first_val.get('note', first_val)
            logging.info('NDM fallback: key=%s', first_key)
    if not note:
        for key in ['noteDetail', 'detail']:
            if state.get(key):
                note = state[key]
                break
    return note

def download_note_images(note, save_dir, cookies_dict):
    os.makedirs(save_dir, exist_ok=True)
    image_list = note.get('imageList', note.get('image_list', note.get('images', []))) or []
    downloaded_files = []
    headers = dict(BASE_HEADERS)
    cookie_str = '; '.join(f'{k}={v}' for k, v in cookies_dict.items())
    if cookie_str:
        headers['Cookie'] = cookie_str
    headers['Referer'] = 'https://www.xiaohongshu.com/'

    for idx, img in enumerate(image_list, 1):
        candidates = []
        if img.get('urlDefault'): candidates.append(img['urlDefault'])
        if img.get('url_default'): candidates.append(img['url_default'])
        trace_id = img.get('traceId') or img.get('trace_id') or ''
        if trace_id:
            candidates.append(f'https://ci.xiaohongshu.com/{trace_id}')
            candidates.append(f'http://sns-webpic-qc.xhscdn.com/{trace_id}')
        for info in img.get('info_list', img.get('infoList', [])):
            if info.get('url'): candidates.append(info['url'])

        saved = False
        for c_url in candidates:
            try:
                r = requests.get(c_url, headers=headers, timeout=15)
                if r.status_code == 200 and len(r.content) > 1000:
                    ext = 'jpg'
                    if r.content[:4] == b'RIFF' and b'WEBP' in r.content[:12]:
                        ext = 'webp'
                    elif r.content[:8] == b'\x89PNG\r\n\x1a\n':
                        ext = 'png'
                    fn = f'image_{idx:02d}.{ext}'
                    fp = os.path.join(save_dir, fn)
                    with open(fp, 'wb') as f:
                        f.write(r.content)
                    downloaded_files.append(fp)
                    saved = True
                    logging.info('图片 %d 下载成功: %s (%d bytes)', idx, fn, len(r.content))
                    break
            except Exception as e:
                logging.debug('尝试 url 失败 %s: %s', c_url, e)
        if not saved:
            logging.warning('图片 %d 所有候选链接下载失败', idx)
    return downloaded_files

def fetch_note(note_id, cookies_dict, original_url=None, xsec_token='', download_images=False, download_dir=''):
    """
    带 xsec_token 的 HTML 请求，优先用原始路径，fallback /discovery/item/。
    xsec_token 必须透传，否则小红书返回纯 JS 壳页面。
    """
    def build_url(base_path):
        params = {'xsec_source': 'pc_feed'}
        if xsec_token:
            params['xsec_token'] = xsec_token
        return base_path + '?' + urlencode(params)

    candidate_urls = []
    if original_url:
        q_idx = original_url.find('?')
        base = original_url[:q_idx] if q_idx >= 0 else original_url
        candidate_urls.append(build_url(base))
    candidate_urls.append(build_url('https://www.xiaohongshu.com/discovery/item/' + note_id))

    seen = set()
    unique_urls = []
    for u in candidate_urls:
        if u not in seen:
            seen.add(u)
            unique_urls.append(u)

    for url in unique_urls:
        logging.info('尝试: %s', url)
        html = fetch_html(url, cookies_dict)
        if not html:
            continue
        state = parse_state_from_html(html)
        if not state:
            logging.warning('state 解析失败: %s', url)
            continue
        note = extract_note_from_state(state, note_id)
        if note:
            downloaded = []
            if download_images:
                save_dir = download_dir if download_dir else os.path.join(_PLUGIN_DIR, 'downloads', note_id)
                downloaded = download_note_images(note, save_dir, cookies_dict)
            return format_note(note, note_id, downloaded=downloaded)
        logging.warning('state 中未找到笔记数据: %s', url)

    return '❌ 未能在页面数据中定位笔记，请确认链接有效或更新 Cookie。'

def resolve_browser_executable():
    """解析浏览器执行体路径：用户配置优先 -> 系统默认 Edge/Chrome 自动探测 -> 留空使用 Playwright 原生"""
    custom_path = (os.environ.get('XHS_BROWSER_EXECUTABLE_PATH') or '').strip()
    if custom_path and os.path.exists(custom_path):
        return custom_path

    # 通用系统路径自动发现（覆盖主流 Windows 10/11 与各版本机器）
    candidates = [
        r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
        r'C:\Program Files\Microsoft\Edge\Application\msedge.exe',
        os.path.expandvars(r'%LOCALAPPDATA%\Microsoft\Edge\Application\msedge.exe'),
        r'C:\Program Files\Google\Chrome\Application\chrome.exe',
        r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
        os.path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe'),
        r'D:\Software\chromium\chrome-win32\chrome.exe',
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    return None

def fetch_explore_feed(cookies_dict, limit=15):
    """通过真实浏览器上下文漫游发现页推荐流"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return '❌ 未安装 playwright，请先安装 playwright 依赖。'

    exe = resolve_browser_executable()

    cookies = []
    for k, v in cookies_dict.items():
        cookies.append({'name': k, 'value': v, 'domain': '.xiaohongshu.com', 'path': '/'})

    results = []
    try:
        with sync_playwright() as p:
            launch_kwargs = {'headless': True, 'args': ['--disable-blink-features=AutomationControlled']}
            if exe:
                launch_kwargs['executable_path'] = exe
            user_data_dir = os.path.join(_PLUGIN_DIR, 'browser_data')
            os.makedirs(user_data_dir, exist_ok=True)
            launch_args = ['--disable-blink-features=AutomationControlled', '--allow-running-insecure-content', '--ignore-certificate-errors']
            context = p.chromium.launch_persistent_context(
                user_data_dir,
                executable_path=exe if exe else None,
                headless=True,
                args=launch_args,
                user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
                viewport={'width': 1440, 'height': 900}
            )
            context.add_cookies(cookies)
            page = context.pages[0] if context.pages else context.new_page()
            page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined});")
            page.goto('https://www.xiaohongshu.com/explore', wait_until='commit', timeout=20000)
            page.wait_for_timeout(5000)
            page.mouse.wheel(0, 400)
            page.wait_for_timeout(2000)

            raw_cards = page.evaluate('''() => {
                const list = [];
                const sections = document.querySelectorAll("section.note-item, div.note-item, [class*='note-item']");
                for (const sec of sections) {
                    const link = sec.querySelector("a[href*='/explore/'], a[href*='/discovery/item/']");
                    const titleEl = sec.querySelector(".title, .footer .name, a.title, [class*='title']");
                    const authorEl = sec.querySelector(".author, .name, [class*='author']");
                    const likeEl = sec.querySelector(".like-wrapper, .count, [class*='like']");
                    if (link) {
                        const href = link.getAttribute("href") || "";
                        const m = href.match(/(?:explore|discovery\/item)\\/([a-zA-Z0-9]+)/);
                        list.push({
                            id: m ? m[1] : "",
                            href: href,
                            title: titleEl ? titleEl.textContent.trim() : "",
                            author: authorEl ? authorEl.textContent.trim() : "",
                            likes: likeEl ? likeEl.textContent.trim() : ""
                        });
                    }
                }
                return list;
            }''')
            context.close()

            results = raw_cards[:limit]
    except Exception as e:
        return f'❌ 漫游发现流失败: {e}'

    if not results:
        return '⚠️ 未能从发现页抓取到有效推荐卡片，请检查 Cookie 状态。'

    lines = ['### 🌸 小红书发现流推荐笔记（共 ' + str(len(results)) + ' 篇）\n']
    for idx, c in enumerate(results, 1):
        full_url = f'https://www.xiaohongshu.com{c["href"]}' if c['href'].startswith('/') else c['href']
        lines.append(f'{idx}. **{c["title"]}**')
        lines.append(f'   - 作者: {c["author"]} | ❤️ 点赞: {c["likes"]}')
        lines.append(f'   - 链接: {full_url}\n')

    lines.append('*提示：女仆可自主选择感兴趣的链接调用 fetch 命令进行精读或下载！*')
    return '\n'.join(lines)

def search_notes(keyword, cookies_dict, limit=10):
    """通过真实浏览器上下文模拟点击放大镜执行关键词搜索并截包"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return '❌ 未安装 playwright，请先安装 playwright 依赖。'

    exe = resolve_browser_executable()

    import urllib.parse
    encoded_kw = urllib.parse.quote(keyword)
    search_url = f'https://www.xiaohongshu.com/search_result?keyword={encoded_kw}&search_type=note'

    cookies = []
    for k, v in cookies_dict.items():
        cookies.append({'name': k, 'value': v, 'domain': '.xiaohongshu.com', 'path': '/'})

    captured = []
    try:
        with sync_playwright() as p:
            launch_kwargs = {
                'headless': True,
                'args': ['--disable-blink-features=AutomationControlled', '--allow-running-insecure-content', '--ignore-certificate-errors']
            }
            if exe:
                launch_kwargs['executable_path'] = exe
            browser = p.chromium.launch(**launch_kwargs)
            context = browser.new_context(
                user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
                viewport={'width': 1280, 'height': 800}
            )
            context.add_cookies(cookies)
            page = context.new_page()

            def on_resp(resp):
                if 'search/notes' in resp.url:
                    try:
                        data = resp.json()
                        items = data.get('data', {}).get('items', [])
                        if items:
                            captured.extend(items)
                    except Exception:
                        pass

            page.on('response', on_resp)
            page.goto(search_url, wait_until='commit', timeout=20000)
            page.wait_for_timeout(3000)

            # 点击放大镜触发搜索接口发包
            page.mouse.click(668, 25)

            for _ in range(8):
                if captured:
                    break
                page.wait_for_timeout(1000)

            browser.close()
    except Exception as e:
        return f'❌ 搜索失败: {e}'

    if not captured:
        return f'⚠️ 未能搜索到关于“{keyword}”的相关笔记，请确认 Cookie 是否有效。'

    items = captured[:limit]
    lines = [f'### 🔍 小红书关键词搜索结果：【{keyword}】（共 {len(items)} 篇）\n']
    for idx, it in enumerate(items, 1):
        nc = it.get('note_card', it)
        title = nc.get('display_title') or nc.get('title') or '无标题'
        user = nc.get('user', {}).get('nickname') or '未知作者'
        nid = it.get('id')
        token = it.get('xsec_token', '')
        link = f'https://www.xiaohongshu.com/discovery/item/{nid}?xsec_token={token}&xsec_source=pc_search' if token else f'https://www.xiaohongshu.com/discovery/item/{nid}'
        likes = (nc.get('interact_info') or {}).get('liked_count', '')
        like_str = f' | ❤️ 点赞: {likes}' if likes else ''
        lines.append(f'{idx}. **{title}**')
        lines.append(f'   - 作者: {user}{like_str}')
        lines.append(f'   - 链接: {link}\n')

    lines.append('*提示：可直接复制上方链接调用 fetch 命令进行精读或原图下载！*')
    return '\n'.join(lines)

# ───────────────────────────────────────────────
# 统一格式化输出
# ───────────────────────────────────────────────

def format_note(note, note_id, downloaded=None):
    title = (note.get('display_title') or note.get('title') or '').strip()
    desc = (note.get('desc') or note.get('description') or note.get('note_text') or '').strip()
    if not title:
        title = desc[:30] + ('…' if len(desc) > 30 else '')
    note_type = note.get('type', 'normal')

    user = note.get('user', note.get('author', {})) or {}
    author = (user.get('nickname') or user.get('nick_name') or '未知作者').strip()
    author_id = (user.get('user_id') or user.get('userId') or user.get('userid') or '').strip()

    interact = note.get('interact_info', note.get('interactInfo', {})) or {}
    likes = str(interact.get('liked_count') or interact.get('likedCount') or '0')
    collects = str(interact.get('collected_count') or interact.get('collectedCount') or interact.get('collect_count') or '0')
    comments = str(interact.get('comment_count') or interact.get('commentCount') or '0')

    lines = []
    lines.append('### 📕 ' + (title or '（无标题）'))
    lines.append('**作者**: ' + author + '（ID: ' + str(author_id) + '）')
    lines.append('**互动**: ❤️ ' + likes + ' ⭐ ' + collects + ' 💬 ' + comments)
    lines.append('\n**正文**:\n' + desc + '\n')

    if note_type == 'video':
        video = note.get('video', {}) or {}
        video_url = None
        try:
            h264_list = video.get('media', {}).get('stream', {}).get('h264', [])
            if h264_list:
                video_url = h264_list[0].get('masterUrl') or h264_list[0].get('master_url')
        except Exception:
            pass
        if not video_url:
            video_url = (video.get('consumer', {}) or {}).get('originVideoKey') or video.get('url')
        if video_url:
            lines.append('#### 🎬 无水印视频:')
            lines.append('<video src="' + video_url + '" controls style="max-width:100%;border-radius:8px;"></video>')
            lines.append('\n[📥 视频直链](' + video_url + ')')
        else:
            lines.append('⚠️ 视频直链获取失败（请更新 Cookie）')

    image_list = note.get('imageList', note.get('image_list', note.get('images', []))) or []
    if image_list:
        lines.append('#### 🖼️ 无水印图片（共 ' + str(len(image_list)) + ' 张）:')
        for idx, img in enumerate(image_list):
            info_list = img.get('info_list', [])
            img_url = ''
            for info in info_list:
                if info.get('image_scene') == 'WB_DFT':
                    img_url = info.get('url', '')
                    break
            if not img_url and info_list:
                img_url = info_list[0].get('url', '')
            if not img_url:
                img_url = img.get('urlDefault') or img.get('url_default') or img.get('url', '')
            clean_url = img_url.split('?')[0] if img_url else ''
            if clean_url:
                lines.append('<img src="' + clean_url + '" alt="图片' + str(idx + 1) + '" style="max-width:100%;margin:4px 0;border-radius:8px;">')

    tag_list = note.get('tagList', note.get('tag_list', note.get('tags', []))) or []
    if tag_list:
        tags = ' '.join(['#' + t.get('name', t.get('tag', '')) for t in tag_list if t])
        if tags.strip():
            lines.append('\n**标签**: ' + tags)

    if downloaded:
        lines.append('\n#### 💾 本地已下载图片（共 ' + str(len(downloaded)) + ' 张）:')
        for f in downloaded:
            lines.append('- `' + f + '`')

    lines.append('\n---\n*数据来源：小红书 | 笔记ID: ' + note_id + '*')
    return '\n'.join(lines)

# ───────────────────────────────────────────────
# 主入口
# ───────────────────────────────────────────────

def main():
    output = {}
    try:
        raw = sys.stdin.read()
        if not raw.strip():
            raise ValueError('没有接收到标准输入数据')

        input_data = json.loads(raw)
        cmd = input_data.get('command', 'fetch')

        a1 = os.environ.get('XHS_COOKIE_A1', '') or input_data.get('a1', '')
        web_session = os.environ.get('XHS_COOKIE_WEB_SESSION', '') or input_data.get('web_session', '')
        web_id = os.environ.get('XHS_COOKIE_WEB_ID', '') or input_data.get('web_id', '')
        cookies_dict = build_cookies_dict(a1, web_session, web_id)

        if cmd == 'feed':
            limit = int(input_data.get('limit', 15))
            result_text = fetch_explore_feed(cookies_dict, limit=limit)
            output = {'status': 'success', 'result': result_text}
            sys.stdout.buffer.write(json.dumps(output, ensure_ascii=False).encode('utf-8'))
            sys.stdout.buffer.write(b'\n')
            sys.stdout.buffer.flush()
            return

        if cmd == 'search':
            keyword = input_data.get('keyword', '').strip()
            if not keyword:
                raise ValueError('缺少必需参数: keyword')
            limit = int(input_data.get('limit', 10))
            result_text = search_notes(keyword, cookies_dict, limit=limit)
            output = {'status': 'success', 'result': result_text}
            sys.stdout.buffer.write(json.dumps(output, ensure_ascii=False).encode('utf-8'))
            sys.stdout.buffer.write(b'\n')
            sys.stdout.buffer.flush()
            return

        raw_url = input_data.get('url', '').strip()
        if not raw_url:
            raise ValueError('缺少必需参数: url')

        logging.info('原始 URL: %s', raw_url)
        logging.info('Cookie a1:%s web_session:%s webId:%s',
                     '已配置' if a1 else '未配置',
                     '已配置' if web_session else '未配置',
                     '已配置' if web_id else '未配置')

        resolved_url = resolve_short_url(raw_url)
        note_id = extract_note_id(resolved_url)
        if not note_id:
            raise ValueError('无法从链接中提取笔记 ID: ' + resolved_url)

        xsec_token = extract_xsec_token(resolved_url)
        logging.info('笔记 ID: %s', note_id)
        logging.info('xsec_token: %s', xsec_token[:20] + '...' if len(xsec_token) > 20 else xsec_token)

        download_images = input_data.get('download_images', False)
        download_dir = input_data.get('download_dir', '') or input_data.get('downloadDir', '')
        result_text = fetch_note(note_id, cookies_dict, original_url=resolved_url, xsec_token=xsec_token,
                                 download_images=download_images, download_dir=download_dir)
        output = {'status': 'success', 'result': result_text}

    except Exception as e:
        logging.error('主流程异常: %s', e)
        output = {'status': 'error', 'error': str(e)}

    sys.stdout.buffer.write(json.dumps(output, ensure_ascii=False).encode('utf-8'))
    sys.stdout.buffer.write(b'\n')
    sys.stdout.buffer.flush()


if __name__ == '__main__':
    main()