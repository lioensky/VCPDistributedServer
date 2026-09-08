# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Run tool-code via ``blender --background``.
"""

__all__ = (
    "run_blender_cli",
    "synced_blend_for_cli",
)

import contextlib
import json
import logging
import os
import subprocess
import sys
from collections.abc import Generator

from blmcp.tools_helpers.connection import send_code

_log = logging.getLogger(__name__)

_RESULT_PREFIX = "__BLMCP_RESULT__"
_ERROR_PREFIX = "__BLMCP_ERROR__"
_CLI_TIMEOUT = 120.0
_MAX_NUMBERED_PATHS = 10000


def _get_blender_path() -> str:
    return os.environ.get("BLENDER_PATH", "blender")


def run_blender_cli(
    blend_file: str,
    code: str,
    timeout: float = _CLI_TIMEOUT,
) -> dict[str, object]:
    """
    Run Python code inside ``blender --background``.

    *blend_file* is the path to the ``.blend`` file to open.
    *code* is executed via ``exec()`` and should assign to ``result``.

    Returns the JSON-de-serialized ``result`` value.
    """
    blender = _get_blender_path()

    wrapper = (
        "import json\n"
        "try:\n"
        "    _ns = {{'result': {{}}}}\n"
        "    exec({!r}, _ns)\n"
        "    _result = _ns['result']\n"
        "    if not isinstance(_result, dict):\n"
        "        raise TypeError(\n"
        "            'The `result` variable must be a dict, not ' +\n"
        "            type(_result).__name__ +\n"
        "            '. Wrap your return value: `result = {{\"key\": value}}`')\n"
        # This only executes arbitrary (LLM-generated) code, not regular tools,
        # so use `default=repr` (equivalent to `strict_json=False`).
        '    print("{:s}" + json.dumps(_result, default=repr))\n'
        "except Exception as ex:\n"
        '    print("{:s}" + json.dumps(str(ex)))\n'
    ).format(code, _RESULT_PREFIX, _ERROR_PREFIX)

    # On Windows, asyncio's ProactorEventLoop (IOCP) can cause pipe
    # handles created by subprocess to deadlock when called from a
    # thread pool.  Explicit DEVNULL for stdin and CREATE_NO_WINDOW
    # keep Blender's handles isolated from the event loop's IOCP.
    extra_kwargs: dict[str, object] = {}
    if sys.platform == "win32":
        extra_kwargs["creationflags"] = subprocess.CREATE_NO_WINDOW
    try:
        proc = subprocess.run(
            [blender, "--factory-startup", "--background",
             blend_file, "--python-expr", wrapper],
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=timeout,
            check=False,
            **extra_kwargs,
        )
    except subprocess.TimeoutExpired as ex:
        raise RuntimeError("Blender CLI timed out after {:.0f}s".format(timeout)) from ex
    except FileNotFoundError as ex:
        raise RuntimeError(
            "Blender executable not found at '{:s}'. "
            "Set the BLENDER_PATH environment variable to the correct path.".format(blender)
        ) from ex

    for line in proc.stdout.splitlines():
        if line.startswith(_RESULT_PREFIX):
            result = json.loads(line[len(_RESULT_PREFIX):])
            if not isinstance(result, dict):
                raise TypeError("Expected dict from Blender CLI, got {!r}".format(type(result)))
            return result
        if line.startswith(_ERROR_PREFIX):
            raise RuntimeError("Blender error: {:s}".format(json.loads(line[len(_ERROR_PREFIX):])))

    raise RuntimeError(
        "No result marker in Blender output.\nstdout: {:s}\nstderr: {:s}".format(proc.stdout, proc.stderr)
    )


def _numbered_blend_path(filepath: str) -> str:
    """
    Return an unused path like ``/path/to/file_mcp_0001.blend``.
    """
    base, ext = os.path.splitext(filepath)
    for i in range(1, _MAX_NUMBERED_PATHS):
        candidate = "{:s}_mcp_{:04d}{:s}".format(base, i, ext)
        if not os.path.exists(candidate):
            return candidate
    raise RuntimeError("Could not find an unused numbered path for '{:s}'".format(filepath))


@contextlib.contextmanager
def synced_blend_for_cli(blend_file: str) -> Generator[str, None, None]:
    """
    Context manager that ensures *blend_file* reflects unsaved changes.

    When a running Blender instance has the same file open with unsaved
    modifications, a numbered copy is saved and yielded. The copy is
    deleted on exit. When no instance is reachable or the file is clean,
    *blend_file* is yielded unchanged.
    """
    temp_path: str | None = None
    try:
        try:
            response = send_code(
                "import bpy, os\n"
                "result = {\"is_dirty\": bpy.data.is_dirty, \"filepath\": bpy.data.filepath}\n",
                strict_json=True,
            )
        except ConnectionError:
            # No running Blender instance, use the on-disk file as-is.
            yield blend_file
            return

        if response.get("status") != "ok":
            raise RuntimeError(str(response.get("message", "Unknown error")))
        result = response["result"]
        assert isinstance(result, dict)
        is_dirty = result.get("is_dirty", False)
        blender_filepath = str(result.get("filepath", ""))

        # Compare normalized paths to see if this is the same file.
        if (
            not blender_filepath
            or os.path.realpath(blend_file) != os.path.realpath(blender_filepath)
        ):
            yield blend_file
            return

        if not is_dirty:
            yield blend_file
            return

        # Dirty file, save a numbered copy.
        temp_path = _numbered_blend_path(blend_file)
        save_response = send_code(
            "import bpy\n"
            "bpy.ops.wm.save_as_mainfile(filepath={!r}, copy=True)\n".format(temp_path),
            strict_json=True,
        )
        if save_response.get("status") != "ok":
            raise RuntimeError(str(save_response.get("message", "Unknown error")))
        yield temp_path
    finally:
        if temp_path is not None:
            try:
                os.remove(temp_path)
            except OSError as ex:
                _log.warning("Failed to remove temporary file '{:s}': {:s}".format(temp_path, str(ex)))
