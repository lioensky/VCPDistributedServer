# NovelAIGen v2.1.0

NovelAI 六端点、多渠道、全参数 VCP 网关。覆盖文生图、图生图、局部重绘、放大、Director 工具、Vibe 编码、标签建议与订阅查询，支持官方直连与第三方中转站。

## 1. 能力清单

| 命令                | 端点                              | 用途                      |
| ------------------- | --------------------------------- | ------------------------- |
| NovelAIGenerate     | `/ai/generate-image`              | 文生图                    |
| NovelAIImg2Img      | `/ai/generate-image`              | 图生图                    |
| NovelAIInpaint      | `/ai/generate-image`              | 局部重绘，action=`infill` |
| NovelAIUpscale      | `/ai/upscale`                     | 图片放大                  |
| NovelAIAugment      | `/ai/augment-image`               | Director 工具             |
| NovelAIEncodeVibe   | `/ai/encode-vibe`                 | Vibe 编码                 |
| NovelAISuggestTags  | `/ai/generate-image/suggest-tags` | 标签建议                  |
| NovelAISubscription | `/user/subscription`              | 订阅与额度查询            |

使用中转站时，上表端点会自动加上配置的路径前缀（见第 4 节）。

## 2. 快速开始

1. 取得 API token：官方为 NovelAI 账户的 Persistent API Token；中转站为该站签发的 token。
2. 复制 `config.env.example` 到 `config.env`，至少设置
   `NOVELAI_API_KEY`、`PROJECT_BASE_PATH`、`SERVER_PORT`、`IMAGESERVER_IMAGE_KEY`、`VarHttpUrl`。
3. 安装依赖并检查语法：

```bash
cd Plugin/NovelAIGen
npm install
node --check NovelAIGen.js
```

最小调用：

```text
tool_name: NovelAIGen
command: generate
prompt: 1girl, blue eyes, anime illustration
resolution: 832x1216
```

推荐先跑一次 `subscription` 命令——它是 GET 请求、不生成图片、不消耗额度，但能一次性验证
token 有效性、路径前缀是否正确、以及渠道遍历是否通畅。

## 3. 完整配置项

| 变量名                    | 类型    | 默认值                      | 说明                                                       |
| ------------------------- | ------- | --------------------------- | ---------------------------------------------------------- |
| NOVELAI_API_KEY           | string  | 空                          | 单渠道 Bearer token，多渠道时可空                          |
| NOVELAI_BASE_URL          | string  | `https://image.novelai.net` | 单渠道图像 API 基地址                                      |
| NOVELAI_PATH_PREFIX       | string  | 空                          | 单渠道原生协议路径前缀，中转站常用 `/native`；官方留空     |
| NOVELAI_ACCOUNT_URL       | string  | `https://api.novelai.net`   | 官方账户 API 域，仅在渠道无前缀时使用                      |
| MULTI_CHANNEL             | boolean | false                       | 启用多渠道                                                 |
| NOVELAI_CHANNELS          | string  | 空                          | `URL\|KEY\|MODELS\|CAPS\|PATH_PREFIX;...`                  |
| MODEL_ALIASES             | string  | 空                          | `alias=model;...` 覆盖内置别名表                           |
| INPAINT_MODELS            | string  | 空                          | `base=variant;...` 追加 inpainting 映射                    |
| INPAINT_FALLBACK_CHAIN    | string  | 空                          | `base>variant;...` 覆盖降级链                              |
| VIBE_UNSUPPORTED_PREFIXES | string  | 空                          | 本地拦截 Vibe 的模型前缀，逗号分隔；留空表示交给上游判断   |
| DEFAULT_MODEL             | string  | `v4.5`                      | 默认模型别名                                               |
| DEFAULT_STEPS             | number  | 23                          | 默认步数，范围 1–50                                        |
| DEFAULT_SCALE             | number  | 5                           | 默认引导系数                                               |
| DEFAULT_SAMPLER           | string  | `k_euler_ancestral`         | 默认采样器                                                 |
| DEFAULT_NOISE_SCHEDULE    | string  | `karras`                    | 默认噪声调度                                               |
| DEFAULT_UC                | string  | `lowres, artistic error, ...`（完整值见 config.env.example） | 默认负面提示词         |
| RESOLUTION_PRESETS        | string  | 内置白名单                  | 逗号分隔覆盖分辨率白名单                                   |
| MAX_RETRIES               | number  | 2                           | 429/5xx 最大重试次数                                       |
| RETRY_BASE_DELAY_MS       | number  | 2000                        | 指数退避基础毫秒数，实际延迟为 base × 3^attempt            |
| MAX_IMAGE_SIZE_MB         | number  | 8                           | 输入图片大小上限                                           |
| ENUM_PROBE                | boolean | true                        | 枚举候选链探测                                             |
| NovelAIProxy              | string  | 空                          | HTTP/HTTPS 代理，两种协议分别使用对应 agent                |
| DebugMode                 | boolean | false                       | 脱敏调试日志，base64 与密钥不会落入日志                    |
| PROJECT_BASE_PATH         | string  | 空                          | VCP 项目根目录，通常由框架注入                             |
| SERVER_PORT               | string  | 空                          | 图片服务器端口，通常由框架注入                             |
| IMAGESERVER_IMAGE_KEY     | string  | 空                          | 图片访问密钥，通常由框架注入                               |
| VarHttpUrl                | string  | 空                          | HTTP 图片服务地址                                          |
| VarHttpsUrl               | string  | 空                          | HTTPS 图片服务地址，设置时优先于 HTTP                      |

## 4. 中转站支持

部分第三方站点在 NovelAI 原生协议路由前加一段路径前缀。以 YesNovelAI（nai.rinko.ai）为例，
其原生入口是 `/native/ai/generate-image` 而非 `/ai/generate-image`。

单渠道配置：

```env
NOVELAI_BASE_URL=https://nai.rinko.ai
NOVELAI_PATH_PREFIX=/native
NOVELAI_API_KEY=ynai-xxxxxxxx
```

请求会被拼接为 `baseUrl + prefix + endpoint`。前缀留空时拼接结果与不带前缀完全相同，
因此官方直连用户无需改动任何配置。

`subscription` 命令按渠道分流：配置了前缀的渠道走 `url + prefix + /user/subscription`
（中转站通常与图像 API 同域），未配置前缀的渠道走 `NOVELAI_ACCOUNT_URL`（官方账户 API
在独立域名 api.novelai.net）。

**中转站的能力边界**：站点可能只为部分端点配置了计费与路由。实测遇到过 Director（augment）
返回 `PRICE_NOT_CONFIGURED`——这表示请求已经到达站点计费层，路径与鉴权都正确，只是该端点
未开放。这类错误属于站点侧策略，不是插件问题。

## 5. 多渠道与能力位

```env
MULTI_CHANNEL=true
NOVELAI_CHANNELS=https://image.novelai.net|pst-xxxx|||;https://nai.rinko.ai|ynai-xxxx|||/native
```

五段依次为 URL、KEY、模型清单、能力清单、路径前缀。`MODELS` 为空表示接受任意模型，
`CAPS` 为空表示全能力，`PATH_PREFIX` 为空表示官方行为。
能力位取值：`gen`、`i2i`、`infill`、`vibe`、`augment`、`upscale`、`tags`。

分发流程：按能力位过滤渠道 → 按模型匹配收窄 → 洗牌 → 逐个尝试。任一渠道失败会继续尝试
下一个，全部失败时聚合报错并逐行列出各渠道原因（含 URL 与模型名，不含密钥）。
官方渠道与中转站渠道可以混合配置，一方不可用时自动落到另一方。

## 6. 模型别名与三维解析

| 别名   | 标识符                        |
| ------ | ----------------------------- |
| v5     | `nai-diffusion-5-full`        |
| v5c    | `nai-diffusion-5-curated`     |
| v4.5   | `nai-diffusion-4-5-full`      |
| v4.5c  | `nai-diffusion-4-5-curated`   |
| v4     | `nai-diffusion-4-full`        |
| v4c    | `nai-diffusion-4-curated`     |
| v3     | `nai-diffusion-3`             |
| furry  | `nai-diffusion-furry-3`       |
| furry3 | `nai-diffusion-3-furry`       |

V5 标识符来源为中转站 `/v1/models` 实证。官方直连是否接受同一组 ID 未经验证；
若遇拒绝，用 `MODEL_ALIASES` 覆盖。`furry` 与 `furry3` 是同一模型的两种写法，
分别来自 SDK 枚举与中转站接口，按渠道选用。

也可以直接传原始标识符（以 `nai-` 或 `safe-` 开头时跳过别名表）。

模型按 `version` × `tier` × `purpose` 三维解析。inpaint 的 purpose 不是普通模型上的开关，
而是独立训练的 `-inpainting` checkpoint。内置映射覆盖 V3、V4、V4.5-curated 与 furry；
未命中时沿降级链选择并在返回文本中显式告知实际使用的模型。

出于保守，`nai-diffusion-4-5-full-inpainting` 与 V5 系的 inpainting 变体未全部内置——
它们只在部分中转站的模型列表中出现。需要时通过 `INPAINT_MODELS` 添加：

```env
INPAINT_MODELS=nai-diffusion-4-5-full=nai-diffusion-4-5-full-inpainting
```

## 7. 协议要点

- inpaint 的 action 字面值是 `infill`（SDK 枚举成员名为 INPAINTING，但序列化值不同）
- 图片与 mask 写入 payload 前必须剥离 data URI 前缀，只留裸 base64
- `params_version` 当前为 3
- 多角色由 `v4_prompt.caption.char_captions[]` 三层结构表达，每个角色带 `centers` 坐标数组
- Vibe 在生成请求中由三个平行数组表达，上限 16 个参考图

## 8. 各命令示例

### 8.1 generate

```text
tool_name: NovelAIGen
command: generate
prompt: 1girl, blue eyes, long hair
resolution: 832x1216
model: v4.5
steps: 23
```

多角色（V4 起支持，最多 6 个）：

```text
char_1: 1girl, silver hair, blue eyes, reading a book
char_1_x: 0.3
char_1_y: 0.5
char_1_uc: red hair
char_2: 1girl, colorful hair, yellow eyes, smiling
char_2_x: 0.7
char_2_y: 0.5
```

或用 JSON 数组形态的 `characters` 参数。角色 prompt 内可写
`source#动作` / `target#动作` / `mutual#动作` 表达角色间交互。

### 8.2 img2img

```text
command: img2img
image: path/to/input.png
prompt: change the background to night sky
strength: 0.65
noise: 0.05
```

### 8.3 inpaint

```text
command: inpaint
image: path/to/input.png
mask: path/to/mask.png
prompt: replace the masked area
```

遮罩图白色区域重绘，黑色区域保留。

### 8.4 upscale

```text
command: upscale
image: path/to/input.png
scale: 2
```

### 8.5 augment

```text
command: augment
req_type: colorize
image: path/to/input.png
```

`req_type` 可选：`emotion`（可配 emotion 与 prompt）、`colorize`（可配 defry）、
`lineart`、`sketch`、`declutter`、`bg-removal`。

### 8.6 encode_vibe

```text
command: encode_vibe
image: path/to/input.png
information_extracted: 1
```

编码消耗 2 Anlas。相同图片与相同 `information_extracted` 会命中本地 JSON 缓存
（落盘于 `image/novelaigen/vibes/`，键为内容与参数的哈希），不重复消耗。

在生成中应用：

```text
vibe: [{"image":"ref1.png","informationExtracted":1,"strength":0.6}]
```

### 8.7 suggest_tags

```text
command: suggest_tags
prompt: blue eyes, school uniform
```

### 8.8 subscription

```text
command: subscription
```

逐渠道查询并汇总。返回订阅等级、额度余额与配额状态；未知字段原样输出 JSON。

生成类命令返回图片 URL 后，应使用 `<img src="返回URL" width="300">` 展示。

## 9. 已实测与未实测

以下能力经真实 API 调用验证（渠道为 YesNovelAI / nai.rinko.ai，走 `/native` 前缀）：

- 文生图：v3、v4、v4.5、v5 四代模型均出图成功
- 图生图：strength 0.65 下姿态保真与风格注入均正常
- 多角色坐标：2 角色与 3 角色场景，坐标分离生效，角色特征无交叉污染
- 角色交互语法：`source#` / `target#` 标注下攻防姿态正确呈现
- 分辨率：512x768、768x512、832x1216、1216x832、1536x1024 均通过
- 路径前缀拼接、模型三维解析、ZIP 响应解包、图片落盘与 URL 构造
- 订阅查询（含中转站同域前缀分流）
- 错误路径：400、402、504 三种状态码的语义化提示与聚合报错
- 多渠道 failover 的聚合错误格式

以下尚未验证：

- 官方直连路径。前缀机制设计为空前缀时与旧版行为等价（`url + "" + endpoint`
  与原拼接逐字相同），但未做真实调用确认
- inpaint 命令与 inpainting 模型降级链
- Vibe 编码与缓存命中
- upscale、suggest_tags 端点
- MessagePack 响应分支（未遇到该响应类型）
- V5 标识符在官方直连下是否可用

## 10. 已知限制

- 未实现 `/ai/generate-image-stream` 流式端点
- 不解析或生成 `.naiv4vibe` 文件
- 不做本地额度消耗预估——服务端是价格与余额的最终权威
- 不提供 GUI，不做图片后处理链
- upscale 与 augment 的部分字段名基于官方 schema 名推定，仍待实测确认
- 部分中转站未为非核心端点（augment / vibe / upscale / tags）配置计费，
  调用会返回 `PRICE_NOT_CONFIGURED` 或 405

## 11. 故障排查

按以下顺序排查：

1. **405，且响应 Content-Type 是 text/html**
   请求未进入应用层，通常是路径不对。中转站需检查 `NOVELAI_PATH_PREFIX`
   或渠道第五段是否填了正确前缀。判别技巧：返回 `application/json` 说明进了 API 层，
   返回 `text/html` 且长度接近站点首页说明被前端路由接管了。

2. **401 / 403**
   检查 token 拼写与前缀（部分站点要求完整前缀如 `ynai-`）、渠道 URL 与 KEY 的绑定关系。
   403 也可能是该 token 没有请求模型的权限。

3. **400**
   核对分辨率是否在白名单内、模型标识符是否被渠道支持、steps 是否在 1–50。
   inpaint 报 400 时先确认 inpainting 模型是否可用。

4. **402 额度不足**
   调用 `subscription` 查询余额。注意中转站可能对下游用户设虚拟限额——
   即使账户显示 Opus，`unlimitedImageGeneration` 也可能为 false。

5. **429 / 502 / 503 / 504**
   瞬时故障，插件会按 `MAX_RETRIES` 与指数退避自动重试。持续出现说明上游过载。

6. **全渠道失败**
   读聚合错误的每一行——它列出了每个渠道的独立失败原因。检查能力位过滤是否把
   唯一支持该命令的渠道排除了。

7. **图片无法展示**
   检查 `PROJECT_BASE_PATH`、`SERVER_PORT`、`IMAGESERVER_IMAGE_KEY`、
   `VarHttpUrl` / `VarHttpsUrl`，以及 `image/novelaigen/` 目录写权限。

## 12. 依赖与检查

依赖版本全部固定，详见 `package.json`。

```bash
node --check NovelAIGen.js
```

`DebugMode=true` 会输出脱敏后的请求体——base64 会被替换为长度标记，
含 token / key / authorization 的字段会被替换为 `<redacted>`。