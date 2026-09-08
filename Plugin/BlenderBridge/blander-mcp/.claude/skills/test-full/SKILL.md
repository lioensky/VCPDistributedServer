---
name: test-full
description: 完整集成测试（TestBackgroundServer 模式）。自动构建插件、安装到隔离环境、启动 Blender 后台进程再测试。适合 CI 验证或需要完全隔离环境时使用。
---

# 完整集成测试（隔离 Blender 环境）

自动完成：构建插件 zip → 安装到临时 HOME → 启动后台 Blender → 运行测试 → 清理。
每次测试都使用最新插件代码，环境完全隔离，不影响用户本地的 Blender 配置。

## 执行步骤

1. 设置环境变量并运行 pytest：

```powershell
cd D:\data\projects\blander-mcp\src
$env:BLENDER_BIN  = "C:\Program Files\Blender Foundation\Blender 5.1\blender.exe"
$env:BLENDER_MCP  = "D:/data/projects/blander-mcp/.venv/Scripts/blender-mcp.EXE"
$env:PYTHONPATH   = "D:\data\projects\blander-mcp"
Remove-Item Env:BLENDER_MCP_REUSE -ErrorAction SilentlyContinue
```

2. 根据用户的意图选择运行范围：

- **运行所有后台模式测试**（无参数时）：
  ```powershell
  python -m pytest tests/test_blender_mcp_with_blender.py -k TestBackgroundServer -v
  ```

- **运行指定测试**（用户提供了测试名或关键词时）：
  ```powershell
  python -m pytest "tests/test_blender_mcp_with_blender.py::TestBackgroundServer::<测试名>" -v
  ```
  或用关键词过滤：
  ```powershell
  python -m pytest tests/test_blender_mcp_with_blender.py -k "TestBackgroundServer and <关键词>" -v
  ```

## 耗时说明

每次 `setUpClass` 要启动 Blender 三次（构建、安装、服务器），约需 30–60 秒的初始化时间。
类内所有测试共用同一个 Blender 进程，单个用例执行很快。

## 结果处理

- 测试失败时，显示错误详情，根据需要修复代码后重新运行失败用例。
- 若只想验证某几个用例，用 `-k "TestBackgroundServer and <关键词>"` 过滤，避免每次都等全套初始化。
- `TestForegroundServer` 和 `TestInteractiveServer` 在 Windows 上会失败（需要 Linux Wayland），忽略即可。
