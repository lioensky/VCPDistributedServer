# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Verify that all Python files contain an SPDX license header on the first line.
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
    os.path.join("mcp", "blmcp", "data", "api"),
)


def main() -> int:
    """
    Entry point for the check-license script.
    """
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    fail = 0
    count = 0
    for scan_dir in _SCAN_DIRS:
        scan_dir_abs = os.path.join(repo_root, scan_dir)
        for dirpath, _dirnames, filenames in os.walk(scan_dir_abs):
            dirpath_rel = os.path.relpath(dirpath, repo_root)
            if any(dirpath_rel == d or dirpath_rel.startswith(d + os.sep) for d in _SKIP_DIRS):
                continue
            for filename in filenames:
                if not filename.endswith(".py"):
                    continue
                filepath = os.path.join(dirpath, filename)
                with open(filepath, "r", encoding="utf-8") as fh:
                    first_line = fh.readline()
                if "SPDX" not in first_line:
                    print("Missing SPDX in: {:s}".format(os.path.relpath(filepath, repo_root)))
                    fail = 1
                else:
                    count += 1

    print("Found {:d} files with SPDX headers.".format(count))
    return fail


if __name__ == "__main__":
    sys.exit(main())
