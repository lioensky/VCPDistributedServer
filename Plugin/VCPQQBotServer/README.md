# VCPQQBotServer

VCPQQBotServer 是一个 VCP `hybridservice` 插件，把腾讯 QQBot 的**单聊（C2C）和群聊（GROUP）**都接入 VCP 主服务器。

闭环流程（单聊与群聊共用同一条链路，只是触发条件不同）：

```text
QQ 用户单聊 / 群里@机器人（或在追问窗口内说话）
  -> QQBot Gateway WebSocket
  -> VCPQQBotServer
  -> VCP 主服务器 /v1/chat/completions 非流请求
  -> VCP 工具循环 / 记忆 / RAG / 预处理器
  -> AI 普通自然语言回复
  -> VCPQQBotServer 自动拆分文本与图片
  -> QQ 单聊/群聊文本 / 图片消息
```

AI 不需要通过工具调用来“回复 QQ”。AI 只要正常输出自然语言即可；插件会自动把非流式回复发送回 QQ 用户/群聊。

群里**主动发消息**（不是回复，而是 AI 自己发起，如早报/通知）才需要工具调用，见下方「群聊能力」一节的 `broadcast_to_groups` / `broadcast_draft_file`。

---

## 文件结构

```text
Plugin/VCPQQBotServer/
├── plugin-manifest.json      # VCP 插件声明
├── VCPQQBotServer.js         # 主实现：QQ Gateway + VCP Chat 桥接 + QQ 回复发送
├── config.env                # 本机真实配置（含密钥，勿公开）
├── config.env.example        # 可公开的配置模板
├── ws链接qqbot文档.md        # QQBot WebSocket 官方文档摘录
└── bot-node-sdk-main/        # 腾讯官方 Node SDK 源码参考
```

---

## 已实现能力

### 0. 群聊（GROUP_AT_MESSAGE_CREATE）—— 已实现，不是"未来计划"

群聊与单聊走同一条桥接链路，区别在于"什么时候唤醒 AI 回复"：

- **必须 @ 机器人才会回复**（QQ 群消息默认不会让 bot 接所有话，否则会刷屏）。
- @机器人后，插件会打开一个**"追问窗口"**：接下来 `QQBotGroupEngageWindow` 条群消息内（默认10条），不用再@也会继续接话；超过这个窗口数就关闭，要再@才会唤醒。
- 每次 bot 实际回复一次，追问窗口会重置（重新计数）。
- 其他机器人在欢迎语里用纯文字提到本机器人名字（没有走QQ平台结构化@）的情况，靠 `QQBotDisplayName` 识别。

**AI 主动给群发消息**（不是回复用户，是早报/通知场景）用以下两个工具命令：

| 命令 | 用途 |
|---|---|
| `broadcast_to_groups` | 直接传 `content` 文本，发给所有已知群（或 `QQBotBroadcastGroups` 指定的群） |
| `broadcast_draft_file` | 读取 `draft_morning_brief.txt` 文件内容发送，用于"先写文案再发送"的两步式早报流程（两步必须分两轮消息，详见下方说明） |

群推送目标群单：默认是"自动注册的群"——bot 收到过消息的任何群都会被自动记下来，不用手动配置；如果只想推送给指定几个群，才需要填 `QQBotBroadcastGroups`。

### 1. QQ 单聊 Gateway 接入

插件启动后会：

1. 读取 `QQAppID` 与 `QQAppSecret` / `QQBotToken`。
2. 请求 QQBot Gateway 地址。
3. 建立 WebSocket。
4. 处理 `Hello`、`Identify`、`Heartbeat`、`Heartbeat ACK`、`Reconnect`、`Invalid Session`。
5. 监听 `C2C_MESSAGE_CREATE`（单聊）与 `GROUP_AT_MESSAGE_CREATE`（群聊@）事件。

### 2. 直接调用 VCP 主服务器聊天入口

收到 QQ 单聊消息后，插件会直接访问本机 VCP 主服务器：

```text
POST http://127.0.0.1:${PORT}/v1/chat/completions
Authorization: Bearer ${Key}
```

其中 `PORT` 和 `Key` 由 VCP 插件系统自动注入，不需要在插件配置中重复填写。

请求固定为非流式：

```json
{
  "messages": [],
  "stream": false,
  "user": "qq_c2c_${openid}"
}
```

这意味着 QQ 单聊可以直接使用 VCP 原有能力，包括：

- VCP 工具协议文本解析
- 同步 / 异步工具调用
- 记忆与 RAG
- 消息预处理器
- 占位符系统
- 模型路由与主服务器配置

### 3. AI 普通回复自动转 QQ 消息

AI 正常输出文本即可，例如：

```text
已经完成了，这是生成结果：

![图片](http://127.0.0.1:5890/pw=xxx/images/demo.png)

如果还需要修改风格，我可以继续处理。
```

插件会自动切成：

1. QQ 文本消息：`已经完成了，这是生成结果：`
2. QQ 图片消息：`demo.png`
3. QQ 文本消息：`如果还需要修改风格，我可以继续处理。`

### 4. 图片 URL 自动识别

非流式 AI 回复中会识别三类图片写法：

#### 裸 URL

```text
http://127.0.0.1:5890/pw=xxx/images/a.png
```

#### Markdown 图片

```markdown
![图](http://127.0.0.1:5890/pw=xxx/images/a.png)
```

#### HTML 图片

```html
<img src="http://127.0.0.1:5890/pw=xxx/images/a.png">
```

支持的图片扩展名：

- `.png`
- `.jpg`
- `.jpeg`
- `.gif`
- `.webp`
- `.bmp`

默认策略是尽量发送真正的 QQ 图片消息，而不是把图片地址当文字发出去。

图片发送优先级：

1. 如果 URL 是 VCP 本地图床地址（形如 `/pw=.../images/...`），插件会解析到服务器本地文件，直接用 QQ `/files` 的 `file_data` base64 上传。
2. 如果原图直传失败，会用 `sharp` 在内存里压缩到约 150KB 再直传。GIF 会跳过压缩，避免动图丢帧。
3. 如果不是本地图床图片，或本地直传与压缩都失败，才回退到 QQ `/files` 的 URL 上传模式。
4. 如果最终仍失败，插件只记录日志并静默跳过图片，**不会**向群里或单聊发送 `[图片: URL]` / `图片：URL` 这类纯文本链接。

⚠️ VCP 内部生成的图片 URL 通常带鉴权参数（如 `pw=xxx`）。配置 `QQBotPublicBaseUrl`（如 `https://yourdomain.com`）后，插件在 URL 上传兜底时会把这种内部 URL 转换成公开的 `/stickers/` 路径，避免把鉴权参数交给 QQ 侧抓取。

### 5. 文本分段

QQ 文本回复会按 `QQBotMaxReplyChars` 自动分段。

切分优先级：

1. 双换行段落
2. 单换行
3. 中文 / 英文句号、问号、感叹号
4. 硬切字符

连续发送会按 `QQBotSendDelayMs` 间隔等待，降低触发 QQ 频控的概率。

---

## 配置方法

复制配置模板：

```bash
cp Plugin/VCPQQBotServer/config.env.example Plugin/VCPQQBotServer/config.env
```

然后编辑：

```env
QQAppID=
QQAppSecret=
QQBotToken=
QQBotAuthMode=bot_app_token
QQBotSandbox=false
QQBotIntents=GROUP_AND_C2C_EVENT
QQBotModel=
QQBotSystemPrompt=你是接入 QQ 单聊的 VCPQQBot。你正在通过 VCP 主服务器与 QQ 用户聊天。你可以自然聊天，也可以使用 VCP 工具协议完成任务。若回复中包含图片 URL、Markdown 图片或 HTML img 标签，系统会自动转成 QQ 图片发送。回复应适合 QQ 聊天场景，避免一次性输出过长文本。
QQBotAllowList=
QQBotHistoryTurns=8
QQBotMaxReplyChars=1200
QQBotSendDelayMs=800
QQBotRequestTimeoutMs=300000
QQBotImageMode=upload
QQBotUploadImages=true
DebugMode=false
QQBotGroupEngageWindow=10
QQBotDisplayName=
QQBotBroadcastGroups=
QQBotPublicBaseUrl=
```

---

## 关键配置说明

| 配置项 | 说明 |
|---|---|
| `QQAppID` | QQBot AppID |
| `QQAppSecret` | QQBot Secret 或 Token，默认会参与 `Bot {QQAppID}.{Token}` 鉴权 |
| `QQBotToken` | 可选，填写后优先于 `QQAppSecret` |
| `QQBotAuthMode` | `bot_app_token` 或 `access_token` |
| `QQBotSandbox` | 是否使用沙箱 Gateway 与 API |
| `QQBotIntents` | 单聊至少需要 `GROUP_AND_C2C_EVENT` |
| `QQBotModel` | 发送到 VCP 主服务器的模型名，留空则使用主服务器默认策略 |
| `QQBotSystemPrompt` | QQ 单聊入口专用系统提示词 |
| `QQBotAllowList` | 允许自动聊天的 QQ 用户 openid，逗号分隔；留空允许全部 |
| `QQBotHistoryTurns` | 每个 QQ 单聊会话保留最近多少轮上下文 |
| `QQBotMaxReplyChars` | QQ 文本消息最大分段字符数 |
| `QQBotSendDelayMs` | 连续发送文本 / 图片之间的延迟 |
| `QQBotRequestTimeoutMs` | 调用 VCP 主服务器非流聊天的超时时间 |
| `QQBotImageMode` | `upload` 为尝试转 QQ 图片；`text` 为只发送 URL 文本 |
| `DebugMode` | 输出调试日志 |
| `QQBotGroupEngageWindow` | 群里@后，继续免@接话的消息条数；0=每次都要@ |
| `QQBotDisplayName` | bot 在群里显示的昵称（识别"被纯文字提及但非结构化@"的边界情况用） |
| `QQBotBroadcastGroups` | 主动推送限定的目标群 openid，逗号分隔；留空则推给自动注册的所有群 |
| `QQBotPublicBaseUrl` | 把内部带鉴权参数的图片 URL 转成公开 `/stickers/` 路径，避免群聊裂图 |

---

## 鉴权模式说明

### bot_app_token

默认模式：

```text
Authorization: Bot {QQAppID}.{QQBotToken或QQAppSecret}
Identify token: Bot {QQAppID}.{QQBotToken或QQAppSecret}
```

适用于当前本地官方 SDK 参考实现。

### access_token

```text
Authorization: QQBot {QQBotToken或QQAppSecret}
Identify token: QQBot {QQBotToken或QQAppSecret}
```

如果 QQ 开放平台当前应用要求 AccessToken 模式，可以切换为：

```env
QQBotAuthMode=access_token
QQBotToken=你的AccessToken
```

---

## QQ 开放平台权限

单聊能力依赖：

```text
GROUP_AND_C2C_EVENT
```

对应 intent：

```text
1 << 25
```

如果应用没有该权限，Gateway 可能返回无权限 intent 或直接断开。遇到连接失败时，请先减少 `QQBotIntents`，确认开放平台已开通对应事件订阅权限。

---

## 图片发送说明

当前实现使用新版 QQ 群聊/C2C 富媒体接口：

```text
POST /v2/groups/{group_openid}/files
POST /v2/groups/{group_openid}/messages
POST /v2/users/{openid}/files
POST /v2/users/{openid}/messages
```

图片发送流程：

1. 从 AI 回复中识别图片 URL。
2. 如果是 VCP 本地图床图片，读取本地文件并调用 `/files`，传入 `file_type=1`、`file_data=<base64>`、`srv_send_msg=false`。
3. 如果原图直传失败，尝试用 `sharp` 压缩后再次用 `file_data` 上传。
4. 如果无法定位本地文件或 `file_data` 路径全失败，使用 URL 上传兜底：`file_type=1`、`url=<publicUrl>`、`srv_send_msg=false`。
5. 从返回中读取 `file_info`。
6. 调用 `/messages`，使用 `msg_type=7` 和 `media.file_info` 发送真正的 QQ 图片消息。
7. 如全部失败，静默跳过图片，只记日志，绝不发送图片 URL 文本。

如果腾讯接口字段变化，需要重点检查 `uploadGroupImageByFileData()`、`uploadC2CImageByFileData()`、`uploadGroupImageSmart()`、`uploadC2CImageSmart()`、`sendGroupImage()` 和 `sendC2CImage()`。

---


## 入站图片识别（用户发图给机器人）

机器人不仅能发图，还能**识别用户发来的图片**。用户在单聊或群里发图片/截图，插件会下载图片转成多模态 `image_url` 格式传给 AI 模型识别（需模型支持视觉，如 agnes-2.0-flash / gemini-2.5-flash 等）。

### 识图链路

1. 收到带图片附件的 QQ 消息（`attachments` 含 `content_type: image/*` 或文件类型）。
2. 下载图片（QQ 附件 URL，公网可直接下载，无需鉴权），转 base64 data URL。
3. 组装成 OpenAI 多模态格式 `[{type:'text',text:...}, {type:'image_url',image_url:{url:dataUrl}}]` 传给 VCP 主服务器。
4. VCP 转发给视觉模型，模型识别图内容并回复。

### 图片质量与高清识图（重要）

QQ 机器人 API 对**普通图片消息**会给压缩缩略图（通常 9-70KB），细小文字 AI 可能看不清。要获得高清识别，**用文件方式发送图片**：

| 发送方式 | 附件 content_type | 图片大小 | 识别效果 |
|---------|------------------|---------|---------|
| 普通图片消息 | `image/png` 等 | 9-70KB 缩略图 | 看个大体，细小文字模糊 |
| **文件发送** | `file` | 原图（实测 444KB） | **完整识别细节** |

实测：同一张 VCP 架构图，普通图片发送 AI 只能看个轮廓；文件发送 444KB 原图，AI 能完整列出图中所有组件和文字。

### 低清图片的确定性提示

当收到的是低清缩略图时（按像素/最长边/字节三者判断，阈值见 `IMAGE_QUALITY_THRESHOLD`），插件会**确定性追加**提示，告诉用户：

> 我已收到图片，但 QQ 提供的是压缩预览图，细小文字无法可靠辨认。请勾选原图发送，或将截图作为文件发送。

这样用户一定知道要发文件/原图才能获得高清识别，不依赖模型是否输出提示。

### 历史脱敏（避免上下文爆炸）

当前请求保留完整 `image_url` 让模型识图；写入会话历史时，图片部分替换为简短文本（如 `[本轮已接收并处理 1 张图片]`），**避免 8 轮历史每轮都重传 base64** 导致上下文膨胀。后续请求不会重传图片数据。

### 安全校验

- **host 白名单**：只下载 `*.qq.com` / `*.qq.com.cn` 域名的图片（QQ 官方域名），拒绝外部 host。
- **MIME 魔数校验**：下载后校验文件头魔数（PNG/JPEG/GIF/WEBP），防止伪造 content-type。
- **禁用重定向**：QQ 直链不需要跳转，禁用重定向防 SSRF。
- **资源边界**：单图上限 12MiB、单次最多 3 张、总字节预算 16MiB，超限静默跳过并提示。

### 图源探测（研究用，默认关闭）

`QQBotImageVariantProbe` 开启后，会对每张入站图片试不同 `spec` 候选（`QQBotImageVariantSpecs`），选字节最大的有效图。**实测 QQ 不支持 spec 变体（spec=1/2 返回 400），普通图片就是缩略图**，所以默认关闭。仅在研究 QQ 是否有高清变体时临时开启。

### 入站事件审计（研究用，默认关闭）

`QQBotInboundEventAudit` 开启后，记录每个入站 QQ 事件的类型/附件结构（脱敏，不记 openid/URL/rkey/正文），用于判断文件消息等是否到达机器人。仅在排查"发图无响应"等问题时临时开启。

---

## 与 VCP 工具调用的关系

QQBot 插件不把“回复 QQ”暴露成必须调用的 VCP 工具。

正确行为：

```text
QQ 用户：帮我生成一张猫猫图
AI：好的，我来生成。
AI：<<<[TOOL_REQUEST]>>> ... 调用生图工具 ...
AI：生成好了：![图](http://...)
插件：自动把文本和图片发回 QQ
```

也就是说：

- 工具调用仍然由 VCP 主服务器文本协议处理。
- QQ 回复由插件在非流式最终结果阶段自动完成。
- AI 不需要显式调用 `VCPQQBotServer` 来发消息。

---

## 状态查看

插件提供动态占位符：

```text
{{VCPQQBotStatus}}
{{VCPQQRecentMessages}}
```

也提供一个只读状态工具：

```text
<<<[TOOL_REQUEST]>>>
tool_name:「始」VCPQQBotServer「末」,
command:「始」status「末」
<<<[END_TOOL_REQUEST]>>>
```

这个工具仅用于排障查看状态，不用于正常聊天回复。

## 群聊主动推送（早报/通知）

AI 想**主动**给群发消息（不是回复用户的提问，是自己发起，比如定时早报）时用这两个命令：

**直接发文本**：

```text
<<<[TOOL_REQUEST]>>>
tool_name:「始」VCPQQBotServer「末」,
command:「始」broadcast_to_groups「末」,
content:「始」早上好！今天是2026年6月27日，祝大家工作顺利～「末」
<<<[END_TOOL_REQUEST]>>>
```

**两步式早报（先写文案到草稿文件，再发送）**：

第一步，把文案写进绝对路径 `<VCP根目录>/Plugin/VCPQQBotServer/draft_morning_brief.txt`（用 ServerFileOperator/DevFileOperator 的写文件命令，**填绝对路径，不要写相对路径**）。

第二步，发送草稿文件内容：

```text
<<<[TOOL_REQUEST]>>>
tool_name:「始」VCPQQBotServer「末」,
command:「始」broadcast_draft_file「末」
<<<[END_TOOL_REQUEST]>>>
```

⚠️ **这两步必须分在两轮不同的 AI 消息里**：第一轮只发 WriteFile，等结果真正返回确认写入成功；第二轮再单独发 broadcast_draft_file。**千万不要把这两个 TOOL_REQUEST 写在同一轮消息里一起发出**——VCP 对同一轮消息里的多个工具调用是用 `Promise.all` 并发执行的（见 `modules/vcpLoop/toolExecutor.js`），写文件（要启动新进程，有一定耗时）和读文件（常驻服务，几乎瞬间响应）会赛跑，读操作很可能先于写操作完成而报 `ENOENT`（2026-06-27 实测踩过这个坑）。

两步式的意义：撰写和发送可以分给不同 agent/不同时机做，避免一个长任务里既要想文案又要管发送状态——但前提是真的分两轮，不是写在一轮里假装两步。

---

## 常见问题

### 1. 插件启动但不连接 Gateway

检查：

- `QQAppID` 是否填写。
- `QQAppSecret` 或 `QQBotToken` 是否填写。
- `QQBotAuthMode` 是否符合当前开放平台鉴权方式。
- `QQBotSandbox` 是否和应用环境一致。

### 2. Gateway 报 invalid intents 或断开

检查：

- `QQBotIntents` 是否只保留已授权事件。
- 单聊是否已开通 `GROUP_AND_C2C_EVENT`。
- 可先只配置：

```env
QQBotIntents=GROUP_AND_C2C_EVENT
```

### 3. QQ 用户发消息后没有 AI 回复

检查：

- VCP 主服务器是否已启动。
- 插件状态中 `VCP 端口` 是否存在。
- 插件状态中 `VCP Key` 是否为 `FOUND`。
- `QQBotAllowList` 是否限制了当前用户 openid。
- VCP 主服务器 `/v1/chat/completions` 是否能正常非流响应。

### 4. AI 回复了图片 URL，但 QQ 没发图

检查：

- `QQBotImageMode` 是否为 `upload`。
- 如果是 VCP 图床 URL，确认 `/pw=.../images/...` 后面的本地文件真实存在。
- 如果文件名是模型编出来的，确认 `resolveEmojiFile()` 是否能模糊匹配到真实文件名。
- `sharp` 是否安装；未安装时仍会尝试原图直传和 URL 上传，但没有压缩兜底。
- QQ 群聊/C2C 文件接口是否返回 `file_info`。
- `QQBotPublicBaseUrl` 是否填写；它只影响 URL 上传兜底，本地 `file_data` 直传不依赖它。
- 腾讯接口是否变更了字段或路径。

失败时插件会静默跳过图片，不会回退发送图片 URL 文本。群里看到文字部分但没有图时，先看 VCP 日志里的 `发送群图片失败(静默跳过,不发文本链接)` 或 `发送 QQ 图片失败(静默跳过,不发文本链接)`。

### 5. `broadcast_draft_file` 报 ENOENT 找不到草稿文件，但文件确实存在

几乎一定是**两步发在了同一轮 AI 消息里**（见上方「群聊主动推送」一节的警告）：VCP 并发执行同一轮内的多个工具调用，WriteFile 还没写完，broadcast_draft_file 已经在读了。解法：把 WriteFile 和 broadcast_draft_file 拆成两轮分别发送，确认第一轮的写入结果真正返回后才发第二轮。

### 6. `broadcast_to_groups` / `broadcast_draft_file` 对某个群返回 400/其他错误码

插件会把 QQ API 返回的真实错误码和消息体一起报出来（如 `HTTP 400 {"code":xxx,"message":"..."}`），照着这个真实错误信息判断，而不要凭空猜测。常见原因包括：bot 已被移出该群、bot 在该群被禁言、消息内容触发频控/敏感词过滤、群 openid 已失效（很久没收到该群消息）。先看插件返回的具体错误码再排查，不要跳过这一步直接猜。

### 7. 为什么不是流式回复

当前单聊优先稳定闭环，使用非流式是为了：

- 等 VCP 工具循环完整结束。
- 一次性拿到最终 AI 回复。
- 统一解析文本、Markdown 图片、HTML 图片和裸 URL。
- 按 QQ 消息类型有序发送文本与图片。

后续如果需要“边生成边发 QQ”，可以另做流式适配，但图片解析与工具循环完成时机要更谨慎。

---

## 开发与校验

语法检查：

```bash
node --check Plugin/VCPQQBotServer/VCPQQBotServer.js
```

Manifest 校验：

```bash
node -e "JSON.parse(require('fs').readFileSync('Plugin/VCPQQBotServer/plugin-manifest.json','utf8')); console.log('manifest ok')"
```

重启 VCP 主服务器后，插件会自动被加载。

---

## 当前边界

- ✅ 已实现 `C2C_MESSAGE_CREATE`（单聊自动回复）。
- ✅ 已实现 `GROUP_AT_MESSAGE_CREATE`（群聊@唤醒 + 追问窗口免@接话，见上方「群聊能力」一节）。
- ✅ 已实现群聊主动推送（`broadcast_to_groups` / `broadcast_draft_file`）。
- 暂未实现频道 `AT_MESSAGE_CREATE` 自动回复（频道≠群，QQ频道是另一套场景，目前没接）。
- 暂未实现用户发来的 QQ 图片转 VCP 多模态输入，仅会把附件元数据写入用户消息。
- QQ 图片发送接口按当前新版 C2C 文档经验实现，如平台字段变动需按真实返回调整。

> ⚠️ 这份文档曾经长期写着"群聊未实现"，但实际群聊早就在线上跑着。维护这份文档时务必先去服务器核对 `config.env` 和真实日志，而不是凭旧文档的记忆去判断功能边界。

---

## 推荐上线步骤

1. 填写 `config.env`。
2. 确认 QQ 开放平台启用单聊与群聊事件（`GROUP_AND_C2C_EVENT`）。
3. 先设置 `DebugMode=true`。
4. 重启 VCP 主服务器。
5. 通过状态工具或占位符确认 Gateway 已连接。
6. 用白名单 openid 单聊测试纯文本。
7. 把 bot 拉进测试群，@它测试群聊回复，确认 `QQBotGroupEngageWindow` 的免@追问窗口生效。
8. 测试 VCP 工具调用，例如搜索、文件、图片生成。
9. 测试 AI 回复中的裸图片 URL、Markdown 图片、HTML 图片；本地图床表情包应走 `file_data` 直传，外部图片或直传失败时才依赖 `QQBotPublicBaseUrl` 的 URL 兜底。
10. 测试群聊主动推送 `broadcast_to_groups`。
11. 稳定后设置 `DebugMode=false`。
