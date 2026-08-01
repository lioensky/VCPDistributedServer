# GodotBridge — VCP × Godot MCP 桥接插件

作为标准 **MCP Client** 连接 [Godot MCP Native](https://github.com/yurineko73/Godot-MCP-Native) 插件，让 VCP Agent 通过渐进式工具发现来读写 Godot 项目的场景、脚本、节点、资源，并控制编辑器与运行时调试。

## 架构定位

```
VCP Agent ──stdio──> GodotBridge (本插件) ──Streamable HTTP──> Godot MCP Native ──> Godot Editor / Runtime
```

- **本插件只做协议适配**：MCP 初始化、会话管理、工具发现、参数校验、结果规范化。
- **不修改 Godot 侧**：Godot MCP Native 的 155 个工具原样复用。
- **零第三方依赖**：仅使用 Node.js 内置 `http/https` 实现 MCP 客户端。

## 前置条件

1. 目标 Godot 项目已复制 `addons/godot_mcp` 并在「项目设置 → 插件」中启用。
2. MCP 面板配置为 HTTP 模式，默认端口 `9080`。
3. Godot 编辑器保持运行（桥接依赖其在线）。

## 配置

复制 `config.env.example` 为 `config.env`：

| 变量 | 说明 | 默认 |
|---|---|---|
| `GODOT_MCP_URL` | Godot MCP 的 HTTP 端点 | `http://127.0.0.1:9080/mcp` |
| `GODOT_MCP_TOKEN` | 可选，Godot 启用认证时的 Bearer Token | 空 |
| `REQUEST_TIMEOUT_MS` | 单次请求超时 | `30000` |
| `MCP_PROTOCOL_VERSION` | MCP 协议版本 | `2025-06-18` |

> Token 不要提交到版本控制。

## 子命令（渐进式发现）

为节约上下文，不把 155 个工具 Schema 一次性塞给模型，而是分层查询：

| command | 作用 | 参数 |
|---|---|---|
| `status` | 检查连接与工具总数 | — |
| `list_domains` | 列出所有工具领域及数量 | — |
| `discover_tools` | 列出某领域的工具清单 | `domain` |
| `get_tool_schema` | 查看单个工具完整参数 | `tool` |
| `call_tool` | 调用任意 Godot MCP 工具 | `tool`, `arguments` |

领域分类：`node` / `script` / `scene` / `editor` / `debug` / `runtime` / `project` / `other`。

## 调用示例

检查连接：
```
<<<[TOOL_REQUEST]>>>
tool_name:「始」GodotBridge「末」,
command:「始」status「末」
<<<[END_TOOL_REQUEST]>>>
```

查看某领域工具：
```
<<<[TOOL_REQUEST]>>>
tool_name:「始」GodotBridge「末」,
command:「始」discover_tools「末」,
domain:「始」scene「末」
<<<[END_TOOL_REQUEST]>>>
```

调用工具（获取场景树）：
```
<<<[TOOL_REQUEST]>>>
tool_name:「始」GodotBridge「末」,
command:「始」call_tool「末」,
tool:「始」get-scene-tree「末」,
arguments:「始」{}「末」
<<<[END_TOOL_REQUEST]>>>
```

## 实现要点

- **Streamable HTTP**：`Accept: application/json, text/event-stream`，自动解析 JSON 与 SSE 两种响应。
- **会话保持**：捕获 `Mcp-Session-Id` 响应头并在后续请求携带。
- **初始化握手**：进程内首次调用时执行 `initialize` + `notifications/initialized`。
- **分页拉取**：`tools/list` 跟随 `nextCursor` 直到取完。
- **结果适配**：文本合并、图片仅保留元信息（避免大段 base64 污染文本）、`structuredContent` 单独返回。

## 后续扩展（可选）

当前为「请求—响应」型 MVP。若需 Godot **主动推送**运行时事件（崩溃、断点命中、场景切换），需：
- Godot 侧新增 `addons/godot_mcp/vcp_bridge/`（事件通道）；
- 本插件新增独立事件接收器，与请求通道隔离。

## 作者

ATRI —— 我是高性能的嘛！