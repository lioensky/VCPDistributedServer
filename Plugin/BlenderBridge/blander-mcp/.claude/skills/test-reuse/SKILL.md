---
name: test-reuse
description: 连接到已开启的 Blender 运行集成测试（TestReuseServer 模式）。适合日常开发调试，跳过构建/安装/启动 Blender 的开销，秒级反馈。
---

# 快速测试（复用已运行的 Blender）

连接到用户**正在开着的** Blender MCP 插件，直接运行测试，无需重新构建或启动 Blender。

## 前提

Blender 必须已开启，且 MCP 插件已启动（默认监听 9876 端口）。

## 执行步骤

1. 设置环境变量并运行 pytest：

```powershell
cd D:\data\projects\blander-mcp\src
$env:BLENDER_BIN  = "C:\Program Files\Blender Foundation\Blender 5.1\blender.exe"
$env:BLENDER_MCP  = "D:/data/projects/blander-mcp/.venv/Scripts/blender-mcp.EXE"
$env:PYTHONPATH   = "D:\data\projects\blander-mcp"
$env:BLENDER_MCP_REUSE = "1"
```

2. 根据用户的意图选择运行范围：

- **运行所有 Reuse 测试**（无参数时）：
  ```powershell
  python -m pytest tests/test_blender_mcp_with_blender.py -k TestReuseServer -v
  ```

- **运行指定测试**（用户提供了测试名或关键词时）：
  ```powershell
  python -m pytest "tests/test_blender_mcp_with_blender.py::TestReuseServer::<测试名>" -v
  ```
  或用关键词过滤：
  ```powershell
  python -m pytest tests/test_blender_mcp_with_blender.py -k "TestReuseServer and <关键词>" -v
  ```

## 结果处理

- 若端口不可达（Blender 未开或插件未启动），会看到 `RuntimeError: BLENDER_MCP_REUSE=1 but port 9876 is not reachable`，提示用户先启动 Blender 并开启 MCP 插件。
- 测试失败时，显示错误详情，根据需要修复代码后重新运行单个失败用例。
- 不要在每次修复后重跑全套，先用 `-k` 精确复现失败用例，确认修复后再跑更大范围。
