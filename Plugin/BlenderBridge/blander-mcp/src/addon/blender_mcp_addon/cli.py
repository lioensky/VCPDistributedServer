# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
CLI command handler for running the MCP server in background mode.

Started via ``blender --background file.blend --command blender_mcp``.
"""

__all__ = (
    "cli_execute",
)

import argparse

from . import execute_blocking
from . import mcp_to_blender_server


def cli_execute(argv: list[str]) -> int:
    """
    Block and serve MCP requests until interrupted.
    """
    parser = argparse.ArgumentParser(
        prog="blender_mcp",
        description=(
            "Start the Blender MCP server. "
            "Deferred responses are not supported in background mode; "
            "each request must complete before returning."
        ),
    )
    parser.add_argument(
        "--host",
        default=mcp_to_blender_server.DEFAULT_HOST,
        help="Host to bind to.",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=mcp_to_blender_server.DEFAULT_PORT,
        help="Port to listen on.",
    )
    args = parser.parse_args(argv)

    try:
        mcp_to_blender_server.start(args.host, args.port)
    except Exception as ex:  # pylint: disable=broad-exception-caught
        print("Error: {:s}".format(str(ex)))
        return 1

    print("MCP server started on {:s}:{:d}, press Ctrl+C to exit.".format(args.host, args.port))

    try:
        execute_blocking.run()
    finally:
        mcp_to_blender_server.stop()
    return 0
