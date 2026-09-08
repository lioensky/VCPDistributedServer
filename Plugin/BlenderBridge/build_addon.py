#!/usr/bin/env python3
"""
Blender Add-on 打包脚本。

把 blander-mcp/src/addon/blender_mcp_addon/ 打成可被 Blender 直接安装的 zip。

【为什么不用 blender --command extension build】
那条命令要求本机已装 Blender 且在 PATH 里。而打包这件事本身只是"按规则压缩文件"，
不需要 Blender 参与。用标准库实现后，任何有 Python 3 的机器都能打包，
CI 环境也不必装一个几百 MB 的 Blender。

【产出的 zip 结构】
Blender 扩展要求 blender_manifest.toml 位于 zip 根目录，而非嵌套在子目录里。
本脚本严格遵守这一点：

    mcp-1.0.1.zip
    ├── blender_manifest.toml     ← 必须在根
    ├── __init__.py
    ├── mcp_to_blender_server.py
    └── ...

【用法】
    python3 build_addon.py                    # 用默认路径，输出到插件目录
    python3 build_addon.py --output /tmp      # 指定输出目录
    python3 build_addon.py --name addon.zip   # 指定文件名
    python3 build_addon.py --check            # 只校验不打包

【产物命名】
默认按扩展规范取 <id>-<version>.zip（读 blender_manifest.toml 得到）。
若需固定名 blender_mcp_addon.zip 以兼容旧 README，加 --legacy-name。
"""

import argparse
import os
import re
import sys
import zipfile

# 相对本脚本所在目录（即插件根）的 addon 源码路径
DEFAULT_ADDON_SRC = os.path.join("blander-mcp", "src", "addon", "blender_mcp_addon")

# 不打进 zip 的目录名与文件后缀
EXCLUDE_DIRS = {"__pycache__", ".git", ".mypy_cache", ".pytest_cache", ".ruff_cache"}
EXCLUDE_SUFFIXES = (".pyc", ".pyo", ".pyd", ".swp", ".orig", ".rej")
EXCLUDE_NAMES = {".DS_Store", "Thumbs.db"}

# Blender 扩展的必需文件
REQUIRED_FILES = ("blender_manifest.toml", "__init__.py")


def plugin_root():
    return os.path.dirname(os.path.abspath(__file__))


def read_manifest_field(manifest_path, field):
    """
    从 blender_manifest.toml 读一个顶层字符串字段。

    这里刻意不用 tomllib——它要 Python 3.11+，而 addon 声明的是 >=3.10。
    manifest 的顶层字段都是简单的 key = "value" 形式，正则足够且更兼容。
    """
    try:
        with open(manifest_path, "r", encoding="utf-8") as f:
            text = f.read()
    except OSError as e:
        raise RuntimeError("无法读取 " + manifest_path + ": " + str(e))

    # 只匹配顶层（行首无缩进）的 key = "value"，避免误取 [permissions] 等表内字段
    pattern = r'^' + re.escape(field) + r'\s*=\s*"([^"]*)"'
    m = re.search(pattern, text, re.MULTILINE)
    return m.group(1) if m else None


def should_skip(rel_path, filename):
    if filename in EXCLUDE_NAMES:
        return True
    if filename.endswith(EXCLUDE_SUFFIXES):
        return True
    parts = rel_path.replace(os.sep, "/").split("/")
    for p in parts:
        if p in EXCLUDE_DIRS:
            return True
    return False


def collect_files(src_dir):
    """遍历源目录，返回 [(绝对路径, zip 内相对路径)]，已排除无关文件。"""
    collected = []
    for dirpath, dirnames, filenames in os.walk(src_dir):
        # 原地修改 dirnames 可阻止 os.walk 进入这些目录
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
        for fn in sorted(filenames):
            abs_path = os.path.join(dirpath, fn)
            rel_path = os.path.relpath(abs_path, src_dir)
            if should_skip(rel_path, fn):
                continue
            collected.append((abs_path, rel_path))
    collected.sort(key=lambda x: x[1])
    return collected


def validate(src_dir, files):
    """打包前校验，尽量在压缩前就把问题暴露出来。"""
    errors = []
    names = set(rel for _, rel in files)

    for req in REQUIRED_FILES:
        if req not in names:
            errors.append("缺少必需文件: " + req + "（Blender 扩展要求它位于 addon 根目录）")

    manifest_path = os.path.join(src_dir, "blender_manifest.toml")
    info = {}
    if os.path.exists(manifest_path):
        for field in ("id", "version", "name", "blender_version_min", "type"):
            info[field] = read_manifest_field(manifest_path, field)
        if not info.get("id"):
            errors.append("blender_manifest.toml 缺 id 字段")
        if not info.get("version"):
            errors.append("blender_manifest.toml 缺 version 字段")
        if info.get("type") and info["type"] != "add-on":
            errors.append('blender_manifest.toml 的 type 应为 "add-on"，当前为 "' + str(info["type"]) + '"')

    return errors, info


def build(src_dir, out_path, files):
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    # ZIP_DEFLATED 是 Blender 扩展的标准压缩方式
    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for abs_path, rel_path in files:
            # arcname 用正斜杠，保证在 Windows 上打的包在 Linux/macOS 也能正确解出
            zf.write(abs_path, rel_path.replace(os.sep, "/"))
    return out_path


def human_size(n):
    if n < 1024:
        return str(n) + " B"
    if n < 1024 * 1024:
        return "{:.2f} KB".format(n / 1024.0)
    return "{:.2f} MB".format(n / (1024.0 * 1024.0))


def main():
    root = plugin_root()
    p = argparse.ArgumentParser(
        description="把 blender_mcp_addon 打包成 Blender 可安装的 zip（纯标准库，无需安装 Blender）"
    )
    p.add_argument("--src", default=None,
                   help="addon 源码目录，默认 " + DEFAULT_ADDON_SRC)
    p.add_argument("--output", default=None,
                   help="输出目录，默认为本脚本所在目录（插件根）")
    p.add_argument("--name", default=None,
                   help="输出文件名，默认 <id>-<version>.zip")
    p.add_argument("--legacy-name", action="store_true",
                   help="固定用 blender_mcp_addon.zip 作为文件名")
    p.add_argument("--check", action="store_true",
                   help="只校验源码结构，不实际打包")
    p.add_argument("--quiet", action="store_true", help="只输出结果路径")
    args = p.parse_args()

    src_dir = args.src if args.src else os.path.join(root, DEFAULT_ADDON_SRC)
    src_dir = os.path.abspath(src_dir)

    if not os.path.isdir(src_dir):
        print("错误：addon 源码目录不存在", file=sys.stderr)
        print("  查找路径: " + src_dir, file=sys.stderr)
        print("", file=sys.stderr)
        print("这个目录来自 Blender 官方 blender_mcp 项目。请确认：", file=sys.stderr)
        print("  1) blander-mcp/ 目录存在于插件根目录下；", file=sys.stderr)
        print("  2) 其内含 src/addon/blender_mcp_addon/；", file=sys.stderr)
        print("  3) 或用 --src 显式指定路径。", file=sys.stderr)
        return 2

    files = collect_files(src_dir)
    if not files:
        print("错误：源目录下没有可打包的文件: " + src_dir, file=sys.stderr)
        return 2

    errors, info = validate(src_dir, files)
    if errors:
        print("校验失败：", file=sys.stderr)
        for e in errors:
            print("  - " + e, file=sys.stderr)
        return 1

    if not args.quiet:
        print("源目录  : " + src_dir)
        print("扩展 ID : " + str(info.get("id")))
        print("名称    : " + str(info.get("name")))
        print("版本    : " + str(info.get("version")))
        print("最低要求: Blender " + str(info.get("blender_version_min")))
        print("文件数  : " + str(len(files)))

    if args.check:
        if not args.quiet:
            print("")
            print("校验通过（--check 模式，未打包）。")
        return 0

    if args.name:
        zip_name = args.name
    elif args.legacy_name:
        zip_name = "blender_mcp_addon.zip"
    else:
        zip_name = str(info.get("id")) + "-" + str(info.get("version")) + ".zip"

    out_dir = os.path.abspath(args.output) if args.output else root
    out_path = os.path.join(out_dir, zip_name)

    build(src_dir, out_path, files)
    size = os.path.getsize(out_path)

    if args.quiet:
        print(out_path)
    else:
        print("")
        print("打包完成: " + out_path)
        print("大小    : " + human_size(size))
        print("")
        print("下一步：在 Blender 里 Preferences -> Add-ons -> 右上角下拉 -> Install from Disk")
        print("        选择上面这个 zip，然后勾选启用。")
        print("提醒  ：还需在 Preferences -> System 勾选 Allow Online Access，")
        print("        否则 add-on 会拒绝启动（即使只连 localhost 也照拦）。")
    return 0


if __name__ == "__main__":
    sys.exit(main())