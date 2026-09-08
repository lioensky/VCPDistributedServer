# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Inline `_deferred_tool_check_for_file_output`.

__all__ = ()

import os
from collections.abc import Callable


def _deferred_tool_check_for_file_output(
        job_type: str,
        output_path: str,
        restore_attrs: list[tuple[object, str, object]] | None = None,
) -> Callable[[], dict[str, object] | None]:
    """
    Return a deferred checker for a background job that writes a file.

    The returned callable follows the deferred tool convention
    (see ``deferred_tool.py``): returns ``None`` while the job is
    running, or a result ``dict`` once it completes.

    When *restore_attrs* is provided, each ``(obj, attr, value)`` tuple
    is restored via ``setattr`` after the job completes.
    """
    import bpy  # pylint: disable=import-error,no-name-in-module

    def check_is_finished() -> dict[str, object] | None:
        if bpy.app.is_job_running(job_type):
            return None
        if restore_attrs is not None:
            for obj, attr, value in restore_attrs:
                setattr(obj, attr, value)
        if os.path.exists(output_path):
            return {"status": "ok", "filepath": output_path}
        return {"status": "error", "message": "Job completed but output file was not created"}

    return check_is_finished
