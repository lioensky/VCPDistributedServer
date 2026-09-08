# 测试指南

本文档说明如何在 Linux / macOS / Windows 上运行本项目的测试。

测试分三类：

1. **单元测试** — 不需要 Blender，跨平台命令一致。
2. **Blender 集成测试**（`src/tests/test_blender_mcp_with_blender.py`）—
   需要本地安装 Blender，验证 MCP Server ↔ Blender 插件的真实通信。
3. **LLM 集成测试**（`src/tests/integration/test_blender_mcp_with_llm.py`）—
   额外需要 Blender + LLM（Claude API 或本地 `llama-server`）。

---

## 0. 环境准备

项目用 [uv](https://docs.astral.sh/uv/) 管理虚拟环境和依赖，三平台命令相同：

```bash
cd blander-mcp
uv sync              # 创建 .venv 并安装依赖（含 dev 组：pytest、autopep8）
```

`.venv` 中可执行文件的路径因平台而异，后面配置环境变量时会用到：

| 平台    | `blender-mcp` 可执行文件路径          |
|---------|----------------------------------------|
| Linux   | `.venv/bin/blender-mcp`                |
| macOS   | `.venv/bin/blender-mcp`                |
| Windows | `.venv\Scripts\blender-mcp.exe`        |

---

## 1. 单元测试（无需 Blender）

覆盖 MCP Server 配置、工具清单、RST 文档解析/检索等，三平台命令一致。

```bash
cd src
python tests/test_tool_listing.py
python tests/test_rst_parse.py
python tests/test_rst_search.py
python tests/test_mcp_server.py
```

在有 `make` 的平台（Linux / macOS，或 Windows 下的 Git Bash + make / WSL）可以直接：

```bash
cd src
make test
```

也可以用 `pytest` 统一跑：

```bash
cd src
python -m pytest tests/test_mcp_server.py tests/test_rst_parse.py tests/test_rst_search.py tests/test_tool_listing.py -v
```

---

## 2. Blender 集成测试

文件：`src/tests/test_blender_mcp_with_blender.py`，包含四个测试类：

- `TestBackgroundServer` — 完全隔离环境：构建插件 zip → 装到临时 HOME →
  启动后台（`--background`）Blender → 测试 → 清理。三平台均可用，**推荐用于
  CI / 首次验证**。
- `TestReuseServer` — 连接一个**用户已经手动打开、并启用了 MCP 插件**的
  Blender，跳过构建/启动开销，秒级反馈，适合日常开发调试。
- `TestForegroundServer` / `TestInteractiveServer` — 需要真实/虚拟显示环境
  （通过 Weston 提供 Wayland），**仅 Linux 支持**；Windows / macOS 上会失败，
  可忽略（对应 skill 文件 `test-full` 的说明）。

### 公共环境变量

| 变量                 | 作用                                   | 默认值        |
|----------------------|----------------------------------------|---------------|
| `BLENDER_BIN`        | Blender 可执行文件路径                 | `blender`（取自 PATH） |
| `BLENDER_MCP`        | `blender-mcp` 可执行文件路径           | `blender-mcp`（取自 PATH） |
| `BLENDER_MCP_REUSE`  | 设为 `1` 时连接已运行的 Blender（Reuse 模式） | 未设置    |
| `BLENDER_MCP_PORT`   | 插件监听端口                           | `9876`        |
| `BLENDER_MCP_TIMEOUT`| 启动超时（秒）                         | `10`          |
| `GLOBAL_TIMEOUT_SCALE`| 所有超时的放大系数（机器较慢时调大）  | `1`           |
| `WESTON_BIN`         | Weston 可执行文件（仅 Foreground 测试用，Linux） | `weston` |

### 2.1 隔离环境（`TestBackgroundServer`）

**Linux / macOS（bash/zsh）**

```bash
cd src
export BLENDER_BIN=/path/to/blender          # 见下方各平台默认安装路径
export BLENDER_MCP="$(pwd)/../.venv/bin/blender-mcp"
export PYTHONPATH="$(pwd)/.."
unset BLENDER_MCP_REUSE

python -m pytest tests/test_blender_mcp_with_blender.py -k TestBackgroundServer -v
```

**Windows（PowerShell）**

```powershell
cd D:\data\projects\blander-mcp\src
$env:BLENDER_BIN = "C:\Program Files\Blender Foundation\Blender 5.1\blender.exe"
$env:BLENDER_MCP = "D:/data/projects/blander-mcp/.venv/Scripts/blender-mcp.EXE"
$env:PYTHONPATH  = "D:\data\projects\blander-mcp"
Remove-Item Env:BLENDER_MCP_REUSE -ErrorAction SilentlyContinue

python -m pytest tests/test_blender_mcp_with_blender.py -k TestBackgroundServer -v
```

`setUpClass` 会启动 Blender 三次（构建、安装、服务器），初次约需 30–60 秒；
同一测试类内的用例共用一个 Blender 进程，单个用例本身很快。

只跑某个用例：

```bash
python -m pytest "tests/test_blender_mcp_with_blender.py::TestBackgroundServer::<测试名>" -v
```

### 2.2 复用已运行的 Blender（`TestReuseServer`）

前提：Blender 已手动打开，且 MCP 插件已启动（默认监听 9876 端口）。

**Linux / macOS**

```bash
cd src
export BLENDER_BIN=/path/to/blender
export BLENDER_MCP="$(pwd)/../.venv/bin/blender-mcp"
export PYTHONPATH="$(pwd)/.."
export BLENDER_MCP_REUSE=1

python -m pytest tests/test_blender_mcp_with_blender.py -k TestReuseServer -v
```

**Windows（PowerShell）**

```powershell
cd D:\data\projects\blander-mcp\src
$env:BLENDER_BIN = "C:\Program Files\Blender Foundation\Blender 5.1\blender.exe"
$env:BLENDER_MCP = "D:/data/projects/blander-mcp/.venv/Scripts/blender-mcp.EXE"
$env:PYTHONPATH  = "D:\data\projects\blander-mcp"
$env:BLENDER_MCP_REUSE = "1"

python -m pytest tests/test_blender_mcp_with_blender.py -k TestReuseServer -v
```

若端口不可达，会报 `RuntimeError: BLENDER_MCP_REUSE=1 but port 9876 is not reachable`
——先确认 Blender 已开且插件已启动。

### 2.3 Foreground / Interactive（仅 Linux）

需要安装 Weston（例如 `apt install weston`），无需额外设置显示环境变量，
测试会自建一个 headless Wayland socket。若想用真实显示，设置
`BLENDER_MCP_FOREGROUND=1`。

```bash
sudo apt install weston   # 或对应发行版的包管理器
cd src
export BLENDER_BIN=/path/to/blender
export BLENDER_MCP="$(pwd)/../.venv/bin/blender-mcp"
export PYTHONPATH="$(pwd)/.."

python -m pytest tests/test_blender_mcp_with_blender.py -k "TestForegroundServer or TestInteractiveServer" -v
```

macOS / Windows 上没有 Wayland，这两个测试类会失败，直接忽略即可。

### 各平台 Blender 默认安装路径参考

| 平台    | 常见路径示例                                              |
|---------|-------------------------------------------------------------|
| Linux   | `/usr/bin/blender`、`/opt/blender-5.1/blender`，或 snap 版 `/snap/blender/current/blender` |
| macOS   | `/Applications/Blender.app/Contents/MacOS/Blender`           |
| Windows | `C:\Program Files\Blender Foundation\Blender 5.1\blender.exe`|

若 Blender 已在 PATH 中，可省略 `BLENDER_BIN` / `BLENDER_MCP`，使用默认值
（`blender` / `blender-mcp`）。

---

## 3. LLM 集成测试（可选）

文件：`src/tests/integration/test_blender_mcp_with_llm.py`，通过
`make test_integration` 驱动，需要 `BLENDER_BIN` 且额外配置模型来源：

- Claude：设置 `ANTHROPIC_API_KEY`（可选 `ANTHROPIC_MODEL`，默认
  `claude-sonnet-4-20250514`）。
- 本地模型：设置 `USE_LLAMA_CXX=1`，并提供 `LLAMA_SERVER_BIN`、
  `LLAMA_SERVER_ARGS`（不要包含 `--port`，由测试框架分配）。两者二选一，
  不可同时使用。

这些变量可写入 `src/.env`（已在 `.gitignore` 中，不会被提交），`make` 会自动加载。

```bash
cd src
make test_integration                       # 跑全部
make test_integration TESTS_LIST=1          # 仅列出所有可跑的用例
make test_integration TESTS=TestChatClient.test_name   # 跑单个用例
```

该命令依赖 GNU Make；Windows 下建议在 Git Bash / WSL 中执行，或参考
`test_blender_mcp_with_llm.py` 顶部的用法说明直接用 `python` 调用。

---

## 4. 常见问题

- **`'blender' not found in PATH`**：设置 `BLENDER_BIN` 为完整可执行文件路径。
- **`'blender-mcp' not found in PATH`**：设置 `BLENDER_MCP` 为 `.venv` 内可执行
  文件的完整路径（见第 0 节表格）。
- **`BLENDER_MCP_REUSE=1 but port 9876 is not reachable`**：Reuse 模式下 Blender
  未打开或插件未启动/监听端口不一致。
- **机器较慢导致超时**：设置 `GLOBAL_TIMEOUT_SCALE=2`（或更大）放宽所有超时。
