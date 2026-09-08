# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Verify that every Python module defines ``__all__``.

Usage::

    python _misc/check_namespace.py mcp/ addon/
"""

__all__ = (
    "main",
)

import argparse
import ast
import os
import sys


def _extract_all(tree: ast.Module) -> tuple[str, ...] | None:
    """Return the value of ``__all__`` if it is a simple tuple/list of strings.

    Returns ``None`` when no ``__all__`` assignment exists or when
    the value cannot be statically evaluated.
    """
    for node in ast.iter_child_nodes(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "__all__":
                    if isinstance(node.value, (ast.Tuple, ast.List)):
                        names: list[str] = []
                        for elt in node.value.elts:
                            if isinstance(elt, ast.Constant) and isinstance(elt.value, str):
                                names.append(elt.value)
                            else:
                                return None
                        return tuple(names)
                    return None
    return None


def _has_all_assignment(tree: ast.Module) -> bool:
    """Return whether an ``__all__`` assignment exists at module level."""
    for node in ast.iter_child_nodes(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "__all__":
                    return True
    return False


def _extract_names(tree: ast.Module) -> tuple[list[str], set[str]]:
    """Return ``(definitions, all_names)`` at module level.

    *definitions* are functions, classes, and assignments (order preserved).
    *all_names* includes definitions plus imported names.
    """
    defs: list[str] = []
    all_names: set[str] = set()
    for node in ast.iter_child_nodes(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            defs.append(node.name)
            all_names.add(node.name)
        elif isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    defs.append(target.id)
                    all_names.add(target.id)
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            defs.append(node.target.id)
            all_names.add(node.target.id)
        elif isinstance(node, ast.Import):
            for alias in node.names:
                all_names.add(alias.asname if alias.asname else alias.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            for alias in node.names:
                all_names.add(alias.asname if alias.asname else alias.name)
    return defs, all_names


def _create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Verify that every Python module defines ``__all__``.",
    )
    parser.add_argument(
        "--skip",
        action="append",
        default=[],
        dest="skip_dirs",
        metavar="DIR",
        help="Directory to skip (may be repeated).",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Print files without errors too.",
    )
    parser.add_argument(
        "paths",
        nargs="+",
        metavar="PATH",
        help="Files or directories to check.",
    )
    return parser


def main() -> int:
    args = _create_parser().parse_args()
    errors = 0
    count = 0

    skip_dirs: list[str] = args.skip_dirs
    verbose: bool = args.verbose
    paths: list[str] = args.paths

    for path in paths:
        if os.path.isfile(path):
            if any(path == d or path.startswith(d + os.sep) for d in skip_dirs):
                files = []
            else:
                files = [path] if path.endswith(".py") else []
        else:
            files = []
            for dirpath, _dirnames, filenames in os.walk(path):
                if any(dirpath == d or dirpath.startswith(d + os.sep) for d in skip_dirs):
                    continue
                for filename in sorted(filenames):
                    if filename.endswith(".py"):
                        files.append(os.path.join(dirpath, filename))

        for filepath in files:
            filename = os.path.basename(filepath)

            with open(filepath, "r", encoding="utf-8") as fh:
                source = fh.read()

            try:
                tree = ast.parse(source, filename=filepath)
            except SyntaxError as ex:
                print("Syntax error: {:s}: {:s}".format(filepath, str(ex)))
                errors += 1
                count += 1
                continue

            if not _has_all_assignment(tree):
                print("Missing __all__: {:s}".format(filepath))
                errors += 1
                count += 1
                continue

            all_names = _extract_all(tree)
            if all_names is None:
                print("{:s}: (could not parse __all__)".format(filepath))
                count += 1
                continue

            if verbose:
                print("{:s}: {:s}".format(filepath, ", ".join(all_names) if all_names else "(empty)"))

            all_set = set(all_names)
            defs, module_names = _extract_names(tree)
            for name in defs:
                if name.startswith("_"):
                    continue
                if name in all_set:
                    continue
                print("  Not in __all__ and missing '_' prefix: {:s}".format(name))
                errors += 1
            # For package init files, subpackage directories and sibling
            # modules count as implicitly defined names.
            if filename == "__init__.py":
                pkg_dir = os.path.dirname(filepath)
                for entry in os.scandir(pkg_dir):
                    if entry.is_dir() and os.path.isfile(os.path.join(entry.path, filename)):
                        module_names.add(entry.name)
                    elif entry.is_file() and entry.name.endswith(".py") and entry.name != filename:
                        module_names.add(entry.name[:-3])

            for name in all_names:
                if name in module_names:
                    continue
                print("  In __all__ but not defined: {:s}".format(name))
                errors += 1
            count += 1

    print("Checked {:d} file(s), {:d} error(s).".format(count, errors))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
