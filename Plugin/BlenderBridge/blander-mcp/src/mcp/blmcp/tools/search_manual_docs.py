# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

# pylint: disable=C0114  # See tool doc-string.

__all__ = (
    "register",
)

from blmcp.tools_helpers.rst_doc_search import (
    SEARCH_TOOL_DESCRIPTION,
    search,
    with_doc,
)
from mcp.server.fastmcp import FastMCP  # pylint: disable=import-error,no-name-in-module
from mcp.types import ToolAnnotations  # pylint: disable=import-error,no-name-in-module


def register(mcp: FastMCP) -> None:
    @mcp.tool(
        annotations=ToolAnnotations(
            title="Search User Manual",
            readOnlyHint=True,
        )
    )
    @with_doc(SEARCH_TOOL_DESCRIPTION.format(scope_name="user manual"))
    def search_manual_docs(
        query: str,
        max_results: int = 20,
        context: int = 0,
        index: int | None = None,
    ) -> dict[str, object]:
        return search(
            query=query,
            scope="manual",
            max_results=max_results,
            context=context,
            index=index,
        )
