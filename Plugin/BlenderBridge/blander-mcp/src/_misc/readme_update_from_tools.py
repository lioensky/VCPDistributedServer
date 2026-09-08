# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Update the tools listing in ``readme.rst`` from tool module docstrings.

Scans ``mcp/blmcp/tools/`` for ``@mcp.tool()`` decorated functions,
extracts their names and docstrings, and replaces the content between
the ``BEGIN TOOL LISTING`` / ``END TOOL LISTING`` sentinels in the readme.
"""

__all__ = (
    "main",
)

import ast
import os
import sys
import textwrap


def _extract_tools(tools_dir: str) -> list[tuple[str, str]]:
    """
    Return a sorted list of ``(name, description)`` pairs for every
    ``@mcp.tool()`` decorated function found in *tools_dir*.
    """
    tools: list[tuple[str, str]] = []
    for filename in sorted(os.listdir(tools_dir)):
        if not filename.endswith(".py"):
            continue
        if filename.endswith("_toolcode.py"):
            continue
        if filename == "__init__.py":
            continue

        filepath = os.path.join(tools_dir, filename)
        with open(filepath, "r", encoding="utf-8") as fh:
            tree = ast.parse(fh.read(), filename=filepath)

        for node in ast.walk(tree):
            if not isinstance(node, ast.FunctionDef):
                continue
            # Check for the `@mcp.tool()` decorator.
            has_decorator = False
            for dec in node.decorator_list:
                if isinstance(dec, ast.Call) and isinstance(dec.func, ast.Attribute):
                    if dec.func.attr == "tool":
                        has_decorator = True
                        break
            if not has_decorator:
                continue

            docstring = ast.get_docstring(node) or ""
            # Use only the first paragraph of the docstring.
            first_para = docstring.split("\n\n")[0].strip()
            # Collapse to a single line.
            description = " ".join(first_para.split())
            tools.append((node.name, description))

    return tools


def _format_tools_rst(tools: list[tuple[str, str]]) -> str:
    """
    Format the tool list as RST definition list items.
    """
    lines: list[str] = []
    for name, description in tools:
        lines.append("``{:s}``".format(name))
        wrapped = textwrap.wrap(description, width=72)
        for line in wrapped:
            lines.append("   {:s}".format(line))
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    """
    Entry point for the update-readme-tools script.
    """
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    tools_dir = os.path.join(repo_root, "mcp", "blmcp", "tools")
    readme_path = os.path.join(repo_root, "readme.rst")

    tools = _extract_tools(tools_dir)
    if not tools:
        print("No tools found in {:s}".format(tools_dir))
        return 1

    tools_rst = _format_tools_rst(tools)

    begin_sentinel = ".. BEGIN TOOL LISTING"
    end_sentinel = ".. END TOOL LISTING"

    with open(readme_path, "r", encoding="utf-8") as fh:
        content = fh.read()

    begin_idx = content.find(begin_sentinel)
    end_idx = content.find(end_sentinel)
    if begin_idx == -1 or end_idx == -1:
        print("Could not find {:s} / {:s} sentinels in {:s}".format(
            begin_sentinel, end_sentinel, readme_path,
        ))
        return 1

    new_content = (
        content[:begin_idx + len(begin_sentinel)]
        + "\n\n"
        + tools_rst
        + "\n"
        + content[end_idx:]
    )

    with open(readme_path, "w", encoding="utf-8") as fh:
        fh.write(new_content)

    print("Updated {:s} with {:d} tools.".format(readme_path, len(tools)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
