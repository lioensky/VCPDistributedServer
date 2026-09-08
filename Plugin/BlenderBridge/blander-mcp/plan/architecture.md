# blender-animation-mcp — 架构设计

> 本文档描述系统架构和技术选型，不规定工具命名或调用风格。

---

## 一、架构概览

```
自然语言输入
     ↓
AI Agent（Claude）
     ↓  MCP Protocol (stdio)
MCP Server（blmcp 包，src/mcp/）
     ↓  JSON over TCP (localhost)
Blender Addon（src/addon/）
     ↓  bpy Python API
Blender Engine
     ↓
动画输出（视频 / 图片）
```

---

## 二、技术选型

### MCP Server

| 技术 | 选择 | 理由 |
|------|------|------|
| 语言 | Python 3.10+ | 与 Blender 生态一致，MCP SDK 原生支持 |
| MCP 框架 | FastMCP（mcp[cli]） | 官方 SDK，工具自动注册 |
| 传输方式 | stdio（主）/ HTTP（备） | 本地开发用 stdio；HTTP 支持 llama.cpp 等本地 LLM |
| 包管理 | uv | 速度快，lockfile 可靠 |
| 包名 | blmcp | 对应 `src/mcp/blmcp/` |

### Blender Addon

| 技术 | 选择 | 理由 |
|------|------|------|
| 通信 | JSON over TCP Socket（null byte 分隔） | 进程间通信，双向可靠 |
| 执行调度 | `bpy.app.timers` | 保证所有 bpy 调用在 Blender 主线程 |
| Blender 版本 | 4.0+ | Geometry Nodes 和 Grease Pencil 3 趋于稳定 |

---

## 三、项目目录结构

```
blander-mcp/
├── src/
│   ├── mcp/                         # MCP Server
│   │   └── blmcp/
│   │       ├── __init__.py          # 入口，工具自动注册
│   │       ├── __main__.py
│   │       ├── data/
│   │       │   ├── prompts.yml      # System Prompt
│   │       │   ├── api/             # Blender API RST 文档
│   │       │   └── manual/          # Blender 用户手册 RST 文档
│   │       ├── tools/               # 每个能力一对文件
│   │       │   ├── xxx.py           # 工具注册（@mcp.tool）
│   │       │   └── xxx_toolcode.py  # 发送给 Blender 执行的 Python 代码
│   │       └── tools_helpers/       # 通信、文档搜索等共享工具
│   ├── addon/                       # Blender Addon
│   │   └── blender_mcp_addon/
│   │       ├── __init__.py          # Addon 注册入口
│   │       ├── mcp_to_blender_server.py  # TCP Server + 主线程调度
│   │       └── execute_*.py         # 代码执行机制
│   └── tests/                       # 测试套件
├── plan/                            # 计划文档
├── pyproject.toml                   # 项目配置
└── uv.lock
```

---

## 四、工具组织原则

MCP Server 中每个工具对应 `tools/` 下的一对文件：

- `capability_name.py` — 注册 `@mcp.tool()`，校验参数，调用 `send_code`
- `capability_name_toolcode.py` — 纯 Python/bpy 代码模板，在 Blender 侧执行

工具按能力命名，不按命名空间分组。文件通过 `pkgutil.iter_modules` 自动发现和注册，
无需手动维护列表。

---

## 五、错误信息规范

所有工具调用返回统一结构：

```json
// 成功
{
  "status": "ok",
  "result": { ... }
}

// 失败
{
  "status": "error",
  "message": "对象 'robot' 不存在",
  "hint": "可用对象：['Camera', 'Light', 'Cube']"
}
```

错误信息必须对 AI 友好：告知当前可用状态，让 AI 能自我纠正。

---

## 六、连接配置

MCP Server 通过环境变量配置 Blender 连接：

| 环境变量 | 默认值 | 说明 |
|----------|--------|------|
| `BLENDER_MCP_HOST` | `127.0.0.1` | Blender Addon 地址 |
| `BLENDER_MCP_PORT` | `6789` | Blender Addon 端口 |

---

## 七、Claude Desktop 配置

```json
{
  "mcpServers": {
    "blender-mcp": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "D:/data/projects/blander-mcp",
        "blender-mcp"
      ]
    }
  }
}
```
