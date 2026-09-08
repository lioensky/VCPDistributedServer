# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Verify that source files contain only ASCII characters.
"""

__all__ = (
    "main",
)

import os
import sys

# Directories to scan.
_SCAN_DIRS = (
    os.path.join("mcp"),
    os.path.join("addon"),
    os.path.join("chat_client"),
)

# Directories to skip (relative to the repository root).
_SKIP_DIRS = (
    os.path.join("mcp", "blmcp", "data", "api", "examples"),
)

# File extensions to check.
_EXTENSIONS = (
    ".py",
    ".toml",
)


def main() -> int:
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    fail = 0
    for scan_dir in _SCAN_DIRS:
        scan_dir_abs = os.path.join(repo_root, scan_dir)
        for dirpath, _dirnames, filenames in os.walk(scan_dir_abs):
            dirpath_rel = os.path.relpath(dirpath, repo_root)
            if any(dirpath_rel == d or dirpath_rel.startswith(d + os.sep) for d in _SKIP_DIRS):
                continue
            for filename in filenames:
                if not any(filename.endswith(ext) for ext in _EXTENSIONS):
                    continue
                filepath = os.path.join(dirpath, filename)
                filepath_rel = os.path.relpath(filepath, repo_root)
                with open(filepath, "rb") as fh:
                    for line_number, line in enumerate(fh, 1):
                        try:
                            line.decode("ascii")
                        except UnicodeDecodeError:
                            print("{:s}:{:d}:{:s}".format(
                                filepath_rel, line_number, line.decode("utf-8", errors="replace").rstrip(),
                            ))
                            fail = 1

    if fail:
        print("ERROR: non-ASCII characters found")
    return fail


if __name__ == "__main__":
    sys.exit(main())
