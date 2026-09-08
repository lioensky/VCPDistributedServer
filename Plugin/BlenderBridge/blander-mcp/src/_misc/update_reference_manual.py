# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Copy RST and Python files from a Blender manual checkout into ``data/manual/``.

Python files are included because the manual contains linked examples and templates.
"""

__all__ = (
    "main",
)

import argparse
import os
import shutil
import sys


def main() -> int:
    """
    Entry point for the update-manual script.
    """
    parser = argparse.ArgumentParser(
        description="Copy RST and Python files from a Blender manual source tree.",
    )
    parser.add_argument(
        "manual_dir",
        help="Path to the Blender manual repository root.",
    )
    args = parser.parse_args()

    src_dir = os.path.join(args.manual_dir, "manual")
    if not os.path.isdir(src_dir):
        print("Source directory not found: {:s}".format(src_dir))
        return 1

    # Resolve relative to the repository root (one level up from `scripts/`).
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dst_dir = os.path.join(repo_root, "mcp", "blmcp", "data", "manual")

    if os.path.isdir(dst_dir):
        shutil.rmtree(dst_dir)

    count = 0
    for dirpath, _dirnames, filenames in os.walk(src_dir):
        for filename in filenames:
            if not filename.endswith((".rst", ".py")):
                continue
            src_file = os.path.join(dirpath, filename)
            rel_path = os.path.relpath(src_file, src_dir)
            dst_file = os.path.join(dst_dir, rel_path)
            os.makedirs(os.path.dirname(dst_file), exist_ok=True)
            shutil.copy2(src_file, dst_file)
            count += 1

    print("Copied {:d} files to {:s}".format(count, dst_dir))
    return 0


if __name__ == "__main__":
    sys.exit(main())
