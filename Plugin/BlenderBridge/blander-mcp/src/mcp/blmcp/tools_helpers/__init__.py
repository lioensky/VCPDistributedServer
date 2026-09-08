# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Shared helpers for tool modules.
"""

__all__ = (
    "toolcode_format_call",
    "toolcode_load_from_filepath",
    "toolcode_wrap_with_calling_convention",
)

import os

_PARAMS_PLACEHOLDER = "__BLMCP_PARAMS__"


def toolcode_format_call(toolcode_template: str, params: object) -> str:
    """
    Substitute the parameter placeholder in *toolcode_template* with *params*.
    """
    return toolcode_template.replace(_PARAMS_PLACEHOLDER, repr(params))


def toolcode_load_from_filepath(filepath: str) -> str:
    """
    Read the ``*_toolcode.py`` file that corresponds to *filepath*.

    Given ``/path/to/tools/my_tool.py``, returns the contents of
    ``/path/to/tools/my_tool_toolcode.py``.

    Simple templating is supported:
    Blocks delimited by
    ``# @include_begin: _template_foo.py`` and
    ``# @include_end`` are replaced with the contents of the referenced file
    (resolved relative to the tool-code file's directory).
    """
    base, ext = os.path.splitext(filepath)
    toolcode_path = base + "_toolcode" + ext
    return _toolcode_expand_includes(toolcode_path)


_INCLUDE_BEGIN_PREFIX = "# @include_begin: "
_INCLUDE_END = "# @include_end"


def _toolcode_expand_includes(toolcode_path: str) -> str:
    with open(toolcode_path, "r", encoding="utf-8") as fh:
        lines = fh.read().splitlines(True)
    toolcode_dir = os.path.dirname(toolcode_path)
    result: list[str] = []
    skip = False
    include_name = ""
    for line in lines:
        if line.startswith(_INCLUDE_BEGIN_PREFIX):
            if skip:
                raise ValueError(
                    "Nested {:s} for {:s} in {:s}".format(_INCLUDE_BEGIN_PREFIX.rstrip(), include_name, toolcode_path)
                )
            include_name = line[len(_INCLUDE_BEGIN_PREFIX):].rstrip()
            include_path = os.path.join(toolcode_dir, include_name)
            if not os.path.exists(include_path):
                raise FileNotFoundError(
                    "Include file {:s} not found (from {:s})".format(include_path, toolcode_path)
                )
            with open(include_path, "r", encoding="utf-8") as fh:
                result.append(fh.read())
            if result[-1] and not result[-1].endswith("\n"):
                result.append("\n")
            skip = True
        elif skip:
            if line.startswith(_INCLUDE_END):
                skip = False
        else:
            result.append(line)
    if skip:
        raise ValueError(
            "Missing {:s} for {:s} in {:s}".format(_INCLUDE_END, include_name, toolcode_path)
        )
    return "".join(result)


def toolcode_wrap_with_calling_convention(
    toolcode: str,
    use_result: bool = True,
) -> str:
    """
    Append the calling convention footer to *toolcode*.

    The footer inserts a placeholder that is later replaced by
    ``toolcode_format_call`` with the ``repr`` of the ``Params``
    named-tuple (or ``None`` for parameter-less tools).
    When *use_result* is True the return value is converted via ``._asdict()``.
    """
    call = "main({:s})".format(_PARAMS_PLACEHOLDER)

    if use_result:
        # When main() returns a callable, store it as `check_is_finished`
        # for the addon's deferred response system (see `deferred_tool.py`).
        # When it returns a NamedTuple, convert to dict as usual.
        footer = (
            "\n_rv = {:s}\n"
            "if callable(_rv):\n"
            "    check_is_finished = _rv\n"
            "    result = {{}}\n"
            "else:\n"
            "    result = _rv._asdict()\n"
        ).format(call)
    else:
        footer = "\nresult = {:s}\n".format(call)

    return toolcode + footer
