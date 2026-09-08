# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Copy RST files and examples from a Blender API reference build into ``data/api/``.

Examples are copied from ``API_DIR/../examples`` into ``data/api/examples/``.
"""

__all__ = (
    "main",
)

import argparse
import os
import shutil
import sys


def _rst_transform(dst_dir: str) -> None:
    """
    Post-process RST files in *dst_dir*, rewriting paths so
    ``literalinclude`` directives point to the co-located examples.
    """
    old = ".. literalinclude:: ../examples/"
    new = ".. literalinclude:: ./examples/"
    for dirpath, _dirnames, filenames in os.walk(dst_dir):
        for filename in filenames:
            if not filename.endswith(".rst"):
                continue
            filepath = os.path.join(dirpath, filename)
            with open(filepath, "r", encoding="utf-8") as fh:
                data = fh.read()
            data_replaced = data.replace(old, new)
            if data_replaced != data:
                with open(filepath, "w", encoding="utf-8") as fh:
                    fh.write(data_replaced)


def main() -> int:
    """
    Entry point for the update-reference-api script.
    """
    parser = argparse.ArgumentParser(
        description="Copy RST files from a Blender API reference build.",
    )
    parser.add_argument(
        "api_dir",
        help="Path to the directory containing generated API RST files.",
    )
    args = parser.parse_args()

    src_dir = args.api_dir
    if not os.path.isfile(os.path.join(src_dir, "bpy.app.rst")):
        print("Source directory does not look like an API reference build: {:s}".format(src_dir))
        return 1

    examples_dir = os.path.join(os.path.dirname(src_dir), "examples")
    if not os.path.isdir(examples_dir):
        print("Examples directory not found: {:s}".format(examples_dir))
        return 1

    # Resolve relative to the repository root (one level up from `scripts/`).
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dst_dir = os.path.join(repo_root, "mcp", "blmcp", "data", "api")

    if os.path.isdir(dst_dir):
        shutil.rmtree(dst_dir)

    count = 0

    # Copy RST files.
    for dirpath, _dirnames, filenames in os.walk(src_dir):
        for filename in filenames:
            if not filename.endswith(".rst"):
                continue
            src_file = os.path.join(dirpath, filename)
            rel_path = os.path.relpath(src_file, src_dir)
            dst_file = os.path.join(dst_dir, rel_path)
            os.makedirs(os.path.dirname(dst_file), exist_ok=True)
            shutil.copy2(src_file, dst_file)
            count += 1

    # Copy examples from the sibling `examples/` directory.
    dst_examples_dir = os.path.join(dst_dir, "examples")
    for dirpath, _dirnames, filenames in os.walk(examples_dir):
        for filename in filenames:
            src_file = os.path.join(dirpath, filename)
            rel_path = os.path.relpath(src_file, examples_dir)
            dst_file = os.path.join(dst_examples_dir, rel_path)
            os.makedirs(os.path.dirname(dst_file), exist_ok=True)
            shutil.copy2(src_file, dst_file)
            count += 1

    _rst_transform(dst_dir)

    print("Copied {:d} files to {:s}".format(count, dst_dir))
    return 0


if __name__ == "__main__":
    sys.exit(main())
