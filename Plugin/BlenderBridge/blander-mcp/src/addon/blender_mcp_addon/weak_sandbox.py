# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Weak sandbox for LLM-generated code execution.

Note that this isn't really a sandbox,
more guidance that some things should not be done.

Notes:

- The reason *not* to use the prompt is that it tends not to be reliable,
  sometimes initial requests leave the context window (or are ignored for whatever reason),
  so we are better off with a simple way to prevent some things from happening.

- If the LLM (or its user) is motivated these can be worked around.
  This is more of a slap on the wrist not to try some things.
"""

__all__ = (
    "WeakSandboxForLLM",
)

import sys
from typing import Any, Self


def _blocked_exit(*args: object, **kwargs: object) -> None:  # noqa: ARG001
    raise RuntimeError("sys.exit() is not allowed in LLM-generated code")


# Each entry is `(object, attr_name, replacement)`.
_OVERRIDES: tuple[tuple[object, str, object], ...] = (
    (sys, "exit", _blocked_exit),
)

# Operators that LLM-generated code must not access.
# Each entry is `("module.func", "reason")`.
#
# Use this sparingly.
# The rule of thumb for inclusion is:
#
#    The operator is guaranteed to cause problems and/or failure.
#
# There are lots of operations that are fairly questionable:
# - `bpy.ops.screen.spacedata_cleanup`.
# - `bpy.ops.wm.previews_clear`
#
# but it's not the purpose of this weak sandbox to disallow
# things the LLM probably shouldn't be doing.
#
# NOTE(@ideasman42): The scope of this may change over time,
# the statement above is a rule of thumb - to apply for now.
#
_BLOCKED_OPS: tuple[tuple[str, str], ...] = (
    ("wm.quit_blender", "Terminates the Blender process, use bpy.app.quit() if you must"),
    (
        "wm.read_factory_settings",
        "Resets all user preferences and startup file, "
        "use bpy.ops.wm.read_homefile() or "
        "bpy.ops.wm.read_homefile(use_empty=True, use_factory_startup=True) instead",
    ),
    (
        "wm.read_factory_userpref",
        "Resets all user preferences, "
        "use bpy.ops.wm.read_homefile() or "
        "bpy.ops.wm.read_homefile(use_empty=True, use_factory_startup=True) instead",
    ),
    ("wm.read_userpref", "May reset user preferences disabling this add-on, avoid calling"),
)

_BLOCKED_OPS_SET: frozenset[str] = frozenset(op for op, _reason in _BLOCKED_OPS)


class WeakSandboxForLLM:
    """Context manager wrapping ``exec()`` of LLM-generated code."""
    __slots__ = (
        "_store_attrs",
        "_store_ops",
    )

    # -------------------------------------------------------------------------
    # Attribute overrides

    @staticmethod
    def override_store() -> list[tuple[object, str, object]]:
        """Save current values listed in ``_OVERRIDES`` and apply replacements."""
        saved: list[tuple[object, str, object]] = []
        for obj, attr, replacement in _OVERRIDES:
            saved.append((obj, attr, getattr(obj, attr)))
            setattr(obj, attr, replacement)
        return saved

    @staticmethod
    def override_restore(saved: list[tuple[object, str, object]]) -> None:
        """Restore values previously captured by :meth:`override_store`."""
        for obj, attr, original in saved:
            setattr(obj, attr, original)

    # -------------------------------------------------------------------------
    # Operator blocking

    @staticmethod
    def ops_blocked_store() -> tuple[Any, Any]:
        """Replace ``bpy.ops._op_create_function`` with a filtered wrapper.

        Returns ``(bpy_ops_module, original_function)`` for later restore.
        """
        import bpy.ops as _bpy_ops  # noqa: WPS433

        original = _bpy_ops._op_create_function

        def _filtered_op_create_function(module: str, func: str) -> Any:
            key = "{:s}.{:s}".format(module, func)
            if key in _BLOCKED_OPS_SET:
                reason = next(r for op, r in _BLOCKED_OPS if op == key)

                def _blocked(
                        *args: tuple[object, ...],
                        **kwargs: dict[str, object],
                ) -> None:
                    # Include the arguments as they may help the LLM pin-point the cause of the error.
                    args_str = ", ".join(
                        [repr(a) for a in args] + ["{:s}={!r}".format(k, v) for k, v in kwargs.items()]
                    )
                    raise RuntimeError(
                        "Operator 'bpy.ops.{:s}({:s})' is not allowed in LLM-generated code: {:s}".format(
                            key, args_str, reason,
                        )
                    )

                return _blocked
            return original(module, func)

        _bpy_ops._op_create_function = _filtered_op_create_function
        return (_bpy_ops, original)

    @staticmethod
    def ops_blocked_restore(saved: tuple[Any, Any]) -> None:
        """Restore the original ``_op_create_function``."""
        bpy_ops_module, original = saved
        bpy_ops_module._op_create_function = original

    # -------------------------------------------------------------------------
    # Context manager

    def __enter__(self) -> Self:
        self._store_attrs = self.override_store()
        self._store_ops = self.ops_blocked_store()
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: object,
    ) -> None:
        del exc_type, exc_val, exc_tb
        self.ops_blocked_restore(self._store_ops)
        self.override_restore(self._store_attrs)
