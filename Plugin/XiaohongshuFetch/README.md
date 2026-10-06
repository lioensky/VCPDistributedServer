# XiaohongshuFetch 🍠

小红书全能生态解析插件。现已进化为具备**定向笔记精读、无水印图片批量下载、发现流自主漫游、关键词精准搜索**的一体化专精工具，兼具轻量静态解析与无头浏览器真实渲染上下文双引擎。

---

## 🌟 功能特性

- 📷 **定向笔记精读 (`fetch`)**：
  - 自动解析图文笔记与视频笔记，提取标题、正文、作者、互动数据（赞/藏/评）与话题标签。
  - 支持直接提取无水印最高画质（WB_DFT）图片直链与高清 MP4 视频直链。
  - **原生落盘支持**：传入 `download_images: true` 即可带防盗链鉴权头将全套原图下载至本地指定目录。
- 🌸 **发现流自主漫游 (`feed`)**：
  - 无需任何外部链接，女仆/用户可直接调用漫游指令，实时抓取小红书首页热门推荐卡片流。
  - 为 AI 女仆自主探索外部世界、汲取灵感并在社区发帖提供数字眼睛与双脚。
- 🔍 **关键词精准搜索 (`search`)**：
  - 传入任意搜索词，自动激活搜索流并拦截最新的 `so.xiaohongshu.com` 接口数据。
  - 自动为每篇笔记绑定合法直达凭据（`xsec_token`），支持无缝二次精读。
- 🛡️ **高鲁棒性反爬与跨环境架构**：
  - **ES6 SSR 脱水清洗**：彻底解决小红书脱水数据中 `new Map` / `new Set` 引发的反序列化崩溃。
  - **多级自适应内核嗅探**：支持用户在配置文件中指定浏览器，或自动扫描 Windows 标准 Edge / Chrome 路径，免去跨机硬编码痛点。
  - **持久化用户数据目录**：挂载 `browser_data` 保存环境特征与指纹，大幅降低风控扫码验证频率。

---

## 🛠️ 安装依赖

插件核心运行依赖 `requests`，若需启用漫游发现流（`feed`）与精准搜索（`search`），请安装 `playwright`：

```bash
pip install requests playwright
```

> **提示**：插件默认会优先探测您系统中已安装的 **Microsoft Edge** 或 **Google Chrome**。只要机器上存在任一现代浏览器，**无需额外下载庞大的 Chromium 驱动包即可开箱即用**！

---

## ⚙️ 配置文件向导 (`config.env`)

登录小红书网页版 (https://www.xiaohongshu.com) 后，打开浏览器开发者工具：
`F12 → Application → Cookies → www.xiaohongshu.com`

复制对应字段填入插件根目录的 `config.env`：

| 配置字段 | 默认/必需 | 说明 |
|----------|-----------|------|
| `XHS_COOKIE_A1` | 必需 | 设备指纹 Cookie（约 52 位） |
| `XHS_COOKIE_WEB_SESSION` | 必需 | 登录态 Session（以 `040069` 开头，核心鉴权凭据） |
| `XHS_COOKIE_WEB_ID` | 可选 | Web 设备 ID |
| `XHS_COOKIE_FULL` | 推荐 | 浏览器中的整串 Cookie（配置后将优先使用此字段） |
| `REQUEST_TIMEOUT` | 默认 `20` | HTTP 请求超时时间（秒） |
| `XHS_BROWSER_EXECUTABLE_PATH` | 可选 | 自定义浏览器路径（如本地便携版 Chromium，留空则全自动探测） |

### `config.env` 示例

```env
# 核心认证 Cookie
XHS_COOKIE_A1=19992fdd1d66y4k59wukr7v0018n4w13v3478j7ea70000187841
XHS_COOKIE_WEB_SESSION=040069796e622b75a18a996c56364a66a15db1
XHS_COOKIE_WEB_ID=2f4a13f6ebec647f3b8b1b0179976371

# 完整 Cookie（推荐直接整串填入）
XHS_COOKIE_FULL=a1=19992fdd...; web_session=040069...; webBuild=5.13.0

# 浏览器内核执行体路径（可选配置）
# 留空时自动顺序探测：系统预装 Edge -> Google Chrome -> 常见便携路径
XHS_BROWSER_EXECUTABLE_PATH=D:\Software\chromium\chrome-win32\chrome.exe
```

---

## 📖 指令与调用方式

插件已向 VCP 网关注册三大标准调用接口：

### 1. 抓取与精读单笔记 (`fetch`)

在聊天中直接发送小红书链接，或通过工具调用：

```json
{
  "command": "fetch",
  "url": "https://www.xiaohongshu.com/discovery/item/6ac07d3b000000001500a333?xsec_token=...",
  "download_images": false
}
```

- **参数说明**：
  - `url` *(string, 必需)*：小红书笔记链接（支持 `explore/<id>`、`discovery/item/<id>` 及 `xhslink.com` 短链接）。
  - `download_images` *(bool, 可选)*：设为 `true` 时，插件将自动在本地下载全部无水印原图。默认 `false` 仅作内存解析与富文本展示。
  - `download_dir` *(string, 可选)*：自定义图片下载保存目录（如 `D:\VCP\downloads\我的壁纸`）。

---

### 2. 漫游首页发现流 (`feed`)

无需任何 URL，自动获取小红书发现页最新热门推荐：

```json
{
  "command": "feed",
  "limit": 10
}
```

- **参数说明**：
  - `limit` *(int, 可选, 默认 15)*：返回的热门笔记数量。

---

### 3. 关键词精准搜索 (`search`)

按指定关键词检索笔记库：

```json
{
  "command": "search",
  "keyword": "四姑娘山",
  "limit": 6
}
```

- **参数说明**：
  - `keyword` *(string, 必需)*：搜索关键词。
  - `limit` *(int, 可选, 默认 10)*：返回的笔记结果数量。

---

## 🏗️ 架构演进路线

```
[模式 1: 静态流清洗 (fetch 默认)]
输入链接 ──► 提取 ID/Token ──► 带凭据 GET ──► 消除 ES6 脱水语法 ──► 反序列化 noteDetailMap ──► 极速直出

[模式 2: 原生资产落盘 (download_images=true)]
解析完成 ──► 读取 urlDefault / traceId ──► 伪装 Referer + Cookie ──► 批量无损下载至本地

[模式 3: 真实上下文渲染 (feed / search)]
指令下发 ──► resolve_browser_executable 嗅探内核 ──► 挂载持久化 browser_data ──► 拦截真实交互与 API ──► 结构化输出
```

---

## 📝 版本更新历史 (CHANGELOG)

| 版本 | 日期 | 核心变更与里程碑 |
|------|------|------------------|
| **v5.0** | 2026-10-06 | 🚀 **重大架构跃迁：三大指令矩阵与通用跨平台重构**<br>• **指令矩阵扩展**：正式支持 `command: "feed"`（发现流自主漫游）与 `command: "search"`（关键词精准搜索），插件从单一解析器进化为全生态数据管道。<br>• **原生资产下载**：新增 `download_images` 与 `download_dir` 参数，支持带伪装头与防盗链直连下载无水印原图。<br>• **ES6 脱水反序列化补丁**：解决小红书新版 SSR 中 `new Map([])` 与 `new Set([])` 引发的反序列化抛崩问题，状态还原率达 100%。<br>• **多级自适应内核嗅探**：新增 `XHS_BROWSER_EXECUTABLE_PATH` 配置项；支持自动发现 Win10/11 系统预装 Edge 与 Chrome 标准路径，告别死路径硬编码。<br>• **持久化防风控上下文**：引入 `browser_data` 持久化上下文，显著降低设备验证触发概率。 |
| **v4.2** | 2026-10-05 | 修复单笔记提取中 `bracket_balance_extract` 状态机在遇到嵌套多层脚本时的跨标签匹配溢出缺陷。 |
| **v4.0** | 2026-02-28 | 移除历史遗留的 xhshow 外部签名依赖，精简收敛为标准脱水解析策略。 |
| **v3.2** | 2026-02-28 | 修复请求未透传 `xsec_token` 导致服务端返回空壳 JS 页面的问题。 |
| **v3.1** | 2026-02-28 | 修复括号平衡解析器转义状态机中 `\\\"` 误翻转字符串标记的 bug。 |
| **v3.0** | 2026-02-28 | 确立基于 HTML 脱水状态树提取的基础架构。 |

---

## 👩‍💻 维护者

无渡&Nova · VCP AI Maid Team · 2026-10-06