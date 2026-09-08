# BlenderBridge

VCP 与 Blender 的三端桥接插件。让 Agent 能直接读写正在运行的 Blender 场景。

## 架构（双跳）

```
VCP (stdio)
  ⇕
BlenderBridge.js          ← 本插件，MCP Client 适配层
  ⇕  Streamable HTTP :6090
blender-mcp               ← Blender 官方 MCP Server（独立 Python 进程）
  ⇕  TCP socket :9876（null 分帧 JSON）
Blender Add-on            ← 运行在 Blender 进程内
```

两跳都必须活着。任一跳断开，工具调用即失败。

## 端口说明

| 跳 | 端口 | 默认值 | 如何修改 |
|---|---|---|---|
| ① VCP ⇄ blender-mcp | HTTP | **6090** | 本插件 `config.env` 的 `BLENDER_MCP_URL`，同时 blender-mcp 启动时 `--port` 要一致 |
| ② blender-mcp ⇄ Add-on | TCP | **9876** | Blender 插件偏好面板的 Port 字段；blender-mcp 侧读环境变量 `BLENDER_MCP_PORT` |

**注意上游的端口配置特性：**

- 第二跳（TCP 9876）：`blender-mcp` 运行时直读环境变量 `BLENDER_MCP_HOST` / `BLENDER_MCP_PORT`，原生可配。
- 第一跳（HTTP 6090）：**不读环境变量**，只认命令行 `--port` 参数。上游源码 `blmcp/__init__.py` 里 argparse 的 default 是 8000，没有 `os.environ` 兜底。
- 上游 `.gitignore` 虽预留了 `src/.env`，但那个文件只被 `Makefile` 的 `-include .env` 加载。直接 spawn `blender-mcp` 时不走 make，`.env` 不生效。

因此本插件的做法是：**HTTP 端口走 CLI 参数，TCP 端口走环境变量注入**，上游仓库不需要打任何补丁，`git pull` 永不冲突。

默认使用 6090 而非上游的 8000，因为 8000 是极易被抢占的公共默认端口。6090 紧邻 VCP 自家的 6005/6006，语义归拢便于运维识别。

## 安装与启动

上游 `blender_mcp` 本体已随插件放在 `blander-mcp/` 目录下，**不需要 git clone**。

整个准备过程就是三条命令：

```bash
cd /path/to/VCPToolBox/Plugin/BlenderBridge

# ① 打包 Blender Add-on（纯标准库，无需装 Blender）
python3 build_addon.py

# ② 安装 Python 环境（自动按 .python-version 拉 3.13.x）
cd blander-mcp && uv sync && cd ..

# ③ 启动 MCP 服务器
cd blander-mcp/src && BLENDER_MCP_HOST=localhost BLENDER_MCP_PORT=9876 \
  ../.venv/bin/blender-mcp --transport http --host 127.0.0.1 --port 6090
```

需要先装 `uv`（Arch: `sudo pacman -S uv`）。依赖 `mcp[cli]` / `docutils` / `pyyaml` 全由 uv 管理，不污染系统 Python。

下面是每步的细节与注意事项。

### 1. 打包 Blender Add-on

```bash
python3 build_addon.py
```

产出 `mcp-1.0.1.zip`（按扩展规范命名为 `<id>-<version>.zip`）。加 `--legacy-name` 可固定输出 `blender_mcp_addon.zip`。

**为什么不用 `blender --command extension build`**：那条命令要求本机已装 Blender 且在 PATH 里。而打包本身只是「按规则压缩文件」，不需要 Blender 参与。改用标准库实现后，任何有 Python 3 的机器都能打包，CI 环境也不必装一个几百 MB 的 Blender。

脚本会做打包前校验（`blender_manifest.toml` 必须在 zip 根目录、必需文件齐全），并自动排除 `__pycache__` 与 `.pyc`。其它可用参数：

```bash
python3 build_addon.py --check          # 只校验不打包
python3 build_addon.py --output /tmp    # 指定输出目录
```

### 2. 在 Blender 里安装 Add-on

`Preferences → Add-ons → ▾ → Install from Disk` → 选上一步产出的 zip → 勾选启用。

Add-on 是**零 pip 依赖**的（只用 `bpy` + 标准库），装上即可用。

也可以走官方扩展仓库（添加 `https://lab.blender.org/` 后搜 MCP），但那样装的是线上版而非本地这份。

### 3. 开启 Allow Online Access（最易踩的坑）

`Preferences → System → Allow Online Access` **必须勾上**。

Add-on 启动时强制检查 `bpy.app.online_access`，未开启会直接拒启并报
`Online access must be enabled in the system preferences`。即使只连 localhost 也照拦。

### 4. 确认 Add-on 服务已启动

Add-on 偏好面板里应显示 `Server is running`。默认 `use_autostart` 为 true，Blender 启动 1 秒后自动起。若显示 stopped，手动点 Start。

端口保持 9876 即可；若要改，面板改完记得同步下一步的环境变量。

### 5. 启动 blender-mcp

```bash
cd blander-mcp/src
BLENDER_MCP_HOST=localhost BLENDER_MCP_PORT=9876 \
  ../.venv/bin/blender-mcp --transport http --host 127.0.0.1 --port 6090
```

默认传输是 stdio，**必须显式指定 `--transport http`**。

### 6. 配置本插件

`config.env`：

```
BLENDER_MCP_URL=http://127.0.0.1:6090/
REQUEST_TIMEOUT_MS=60000
MCP_PROTOCOL_VERSION=2025-06-18
DebugMode=false
```

## 子命令

采用渐进式发现，避免 59 个工具的 Schema 一次性冲垮上下文。

| 子命令 | 参数 | 说明 |
|---|---|---|
| `status` | — | 连接状态、工具总数、领域分布 |
| `list_domains` | — | 所有领域及工具数 |
| `discover_tools` | `domain` | 列出该领域的工具名与简介 |
| `get_tool_schema` | `tool` | 单个工具的完整参数 Schema |
| `call_tool` | `tool`, `arguments` | 调用任意 Blender MCP 工具 |
| `create_model` | `code` | 程序化建模逃生舱，详见「模型自制说明.md」 |

**推荐流程**：`list_domains` → `discover_tools` → `get_tool_schema` → `call_tool`。

不要凭记忆猜参数名。实测教训：`mesh_primitive_add` 的参数是 `primitive_type` 而非 `primitive`，只有查 Schema 才知道。

### 领域划分（共 59 工具）

按工具名前缀自动归类，不硬编码清单，上游新增工具会自动落位：

| 领域 | 数量 | 内容 |
|---|---|---|
| `scene` | 1 | 场景状态总览 |
| `object` | 10 | 物体详情、修改器、材质、驱动器、F 曲线、关键帧 |
| `mesh` | 1 | 图元创建 |
| `material` | 1 | 材质列表 |
| `geonodes` | 4 | 几何节点查询、赋值、预设、关键帧 |
| `greasepencil` | 10 | 蜡笔图层、材质、笔画、形状 |
| `animation` | 3 | 骨骼动作、动作列表、相机追踪 |
| `asset` | 2 | 资产导入、库链接 |
| `blendfile` | 10 | 数据块统计、缺失文件、链接库、路径信息、用途推测 |
| `render` | 4 | 帧渲染、动画渲染、缩略图、视口输出 |
| `screenshot` | 3 | 窗口/区域截图、窗口布局 JSON |
| `navigation` | 4 | 切换工作区标签、聚焦物体 |
| `docs` | 3 | Python API 文档、用户手册检索 |
| `exec` | 2 | 任意 Python 执行（含 CLI 后台版） |

## 安全须知

Add-on 侧的 `weak_sandbox.py` **不是真沙箱**。上游注释原话：

> this isn't really a sandbox, more guidance that some things should not be done
> ... This is more of a slap on the wrist not to try some things.

它只拦：

- `sys.exit()`
- 4 个毁灭级算子：`wm.quit_blender`、`wm.read_factory_settings`、`wm.read_factory_userpref`、`wm.read_userpref`

**这意味着 `execute_blender_code` / `create_model` 在 Blender 进程内近乎全权限执行 Python**——可读写文件系统、可调用完整 `bpy` API。

建议：

1. 优先使用 59 个结构化工具，`create_model` 仅作覆盖不到时的逃生舱。
2. 破坏性操作（删除物体、批量改数据块）前向用户确权。
3. 不要在不受信任的 .blend 文件或不受信任的提示词下开放本插件。

## 故障排查

| 现象 | 原因与处理 |
|---|---|
| `ECONNREFUSED` | blender-mcp 未启动，或端口与 `BLENDER_MCP_URL` 不一致 |
| `Cannot connect to Blender at localhost:9876` | Blender 未运行 / Add-on 未启用 / 面板显示 stopped |
| `Online access must be enabled` | 去 Preferences → System 勾选 Allow Online Access |
| `BLENDER_BUSY` | 上游只支持单并发。等当前调用结束再重试，顺序调用完全正常 |
| 工具报参数错误 | 先 `get_tool_schema` 查真实参数名，勿凭记忆 |
| `result` 不是 dict | `create_model` 的代码里 `result` 必须是 JSON 可序列化的 dict |

## 已验证环境

- Blender 5.2.0 LTS（Add-on 要求 ≥ 5.1.0）
- blender-mcp 1.28.0
- MCP 协议 2025-06-18
- Python 3.13.13（由 uv 管理）

上游原生开启 `stateless_http=True`，重复 `initialize` 不会报 500——这与 PenpotBridge 早期踩过的单例 transport 坑不同，无需额外改造。