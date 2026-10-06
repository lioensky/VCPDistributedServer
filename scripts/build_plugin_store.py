#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Build VCP official plugin store index and per-plugin zip packages.

Usage:
    python scripts/build_plugin_store.py
    python scripts/build_plugin_store.py --plugin XiaohongshuFetch
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List

SAFE_PLUGIN_NAME_RE = re.compile(r"^[A-Za-z0-9._-]+$")

DEFAULT_EXCLUDE_DIRS = {
    ".git",
    ".svn",
    ".hg",
    "node_modules",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    ".venv",
    "venv",
    "env",
    "dist",
    "build",
    "browser_data",
    "downloads",
}

DEFAULT_EXCLUDE_FILE_NAMES = {
    ".DS_Store",
    "Thumbs.db",
    "config.env",
    ".env",
    ".env.local",
    ".env.production",
    "package-lock.json",
    "yarn.lock",
    "pnpm-lock.yaml",
}

DEFAULT_EXCLUDE_SUFFIXES = {
    ".pyc",
    ".pyo",
    ".log",
    ".sqlite",
    ".sqlite3",
    ".db",
    ".tmp",
    ".bak",
    ".zip",
    ".tar",
    ".tgz",
    ".gz",
}

CATEGORY_BY_PLUGIN_TYPE = {
    "static": "data-provider",
    "service": "service",
    "hybridservice": "service",
}


def repo_root_from_script() -> Path:
    return Path(__file__).resolve().parents[1]


def read_json(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return data


def write_json(path: Path, data: Dict[str, Any]) -> None:
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def is_safe_plugin_name(name: str) -> bool:
    return bool(name and SAFE_PLUGIN_NAME_RE.fullmatch(name) and not name.startswith("."))


def normalize_category(manifest: Dict[str, Any]) -> str:
    raw = str(manifest.get("category") or "").strip()
    if raw:
        return raw

    plugin_type = str(manifest.get("pluginType") or manifest.get("type") or "").strip().lower()
    if plugin_type in CATEGORY_BY_PLUGIN_TYPE:
        return CATEGORY_BY_PLUGIN_TYPE[plugin_type]

    name = str(manifest.get("name") or "").lower()
    if any(k in name for k in ["image", "gen", "draw", "flux", "doubao", "zimage", "comfy", "novelai"]):
        return "image-generation"
    if any(k in name for k in ["video", "suno", "music"]):
        return "media-generation"
    if any(k in name for k in ["search", "fetch", "crawl", "wiki", "serp", "arxiv", "paper"]):
        return "information-retrieval"
    if any(k in name for k in ["shell", "executor", "file", "backup", "operator"]):
        return "system-integration"
    if any(k in name for k in ["agent", "message", "assistant", "dream", "task"]):
        return "agent-collab"
    if any(k in name for k in ["forum", "bilibili"]):
        return "social"
    if any(k in name for k in ["chrome", "bridge", "capture", "screenshot"]):
        return "browser"
    return "tool"


def should_exclude(path: Path, plugin_dir: Path) -> bool:
    rel_parts = path.relative_to(plugin_dir).parts

    for part in rel_parts:
        if part in DEFAULT_EXCLUDE_DIRS:
            return True

    name = path.name
    if name in DEFAULT_EXCLUDE_FILE_NAMES:
        return True

    lower = name.lower()
    if any(lower.endswith(suffix) for suffix in DEFAULT_EXCLUDE_SUFFIXES):
        return True

    return False


def iter_plugin_files(plugin_dir: Path) -> Iterable[Path]:
    for path in plugin_dir.rglob("*"):
        if path.is_dir():
            continue
        if should_exclude(path, plugin_dir):
            continue
        yield path


def build_plugin_zip(plugin_dir: Path, plugin_name: str) -> Path:
    zip_path = plugin_dir / f"{plugin_name}.zip"
    if zip_path.exists():
        zip_path.unlink()

    parent_dir_name = plugin_dir.name

    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for file_path in iter_plugin_files(plugin_dir):
            arcname = Path(parent_dir_name) / file_path.relative_to(plugin_dir)
            zf.write(file_path, arcname.as_posix())

    return zip_path


def to_raw_download_url(repo: str, branch: str, zip_path: Path, root: Path) -> str:
    rel = zip_path.relative_to(root).as_posix()
    return f"https://raw.githubusercontent.com/{repo}/{branch}/{rel}"


def make_plugin_entry(
    manifest: Dict[str, Any],
    plugin_name: str,
    zip_url: str,
) -> Dict[str, Any]:
    display_name = str(manifest.get("displayName") or plugin_name).strip()
    description = str(manifest.get("description") or "").strip()
    version = str(manifest.get("version") or "").strip()
    author = str(manifest.get("author") or "VCP Team").strip()
    icon = str(manifest.get("icon") or "extension").strip()

    entry: Dict[str, Any] = {
        "name": plugin_name,
        "displayName": display_name,
        "description": description,
        "version": version,
        "author": author,
        "icon": icon,
        "category": normalize_category(manifest),
        "downloadUrl": zip_url,
    }

    for optional_key in ["homepage", "repository", "license", "minVcpVersion"]:
        value = manifest.get(optional_key)
        if isinstance(value, str) and value.strip():
            entry[optional_key] = value.strip()

    return entry


def package_single_plugin(plugin_dir: Path, repo: str, branch: str, root: Path) -> Dict[str, Any]:
    manifest_path = plugin_dir / "plugin-manifest.json"
    if not manifest_path.exists():
        raise FileNotFoundError(f"Missing plugin-manifest.json in {plugin_dir}")

    manifest = read_json(manifest_path)
    raw_name = str(manifest.get("name") or "").strip()
    if not is_safe_plugin_name(raw_name):
        raise ValueError(f"Unsafe plugin name: {raw_name}")

    zip_path = build_plugin_zip(plugin_dir, raw_name)
    zip_url = to_raw_download_url(repo, branch, zip_path, root)
    entry = make_plugin_entry(manifest, raw_name, zip_url)
    return {
        "entry": entry,
        "zipPath": zip_path,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build VCP plugin store registry and zip packages.")
    parser.add_argument("--repo", default="lioensky/VCPDistributedServer", help="GitHub repo in owner/name format.")
    parser.add_argument("--branch", default="main", help="GitHub branch for raw download URLs.")
    parser.add_argument("--root", default="", help="Repository root. Defaults to script parent parent.")
    parser.add_argument("--plugin", default="", help="Package single plugin directory name.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve() if args.root else repo_root_from_script()

    if args.plugin:
        plugin_dir = root / "Plugin" / args.plugin
        if not plugin_dir.is_dir():
            print(f"Plugin directory not found: {plugin_dir}", file=sys.stderr)
            return 1
        res = package_single_plugin(plugin_dir, args.repo, args.branch, root)
        print(f"[OK] {args.plugin} packaged successfully.")
        print(f"Zip: {res['zipPath']}")
        print("Registry Entry:")
        print(json.dumps(res["entry"], ensure_ascii=False, indent=2))
        return 0

    plugin_root = root / "Plugin"
    if not plugin_root.is_dir():
        print(f"Plugin directory not found: {plugin_root}", file=sys.stderr)
        return 1

    entries: List[Dict[str, Any]] = []
    for pdir in sorted(plugin_root.iterdir(), key=lambda p: p.name.lower()):
        if not pdir.is_dir():
            continue
        mpath = pdir / "plugin-manifest.json"
        if not mpath.exists():
            continue
        try:
            res = package_single_plugin(pdir, args.repo, args.branch, root)
            entries.append(res["entry"])
            print(f"[OK] {pdir.name} -> {res['zipPath'].relative_to(root).as_posix()}")
        except Exception as e:
            print(f"[SKIP] {pdir.name}: {e}")

    registry = {
        "schemaVersion": 1,
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "source": {
            "name": "VCP 官方插件商店",
            "repository": f"https://github.com/{args.repo}",
            "branch": args.branch,
        },
        "plugins": entries,
    }
    write_json(root / "plugins.json", registry)
    print(f"\nGenerated plugins.json with {len(entries)} plugin(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())