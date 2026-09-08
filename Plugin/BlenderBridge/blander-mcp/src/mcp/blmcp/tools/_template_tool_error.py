# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Inline `ErrorResult`.

__all__ = ()

from typing import NamedTuple


class ErrorResult(NamedTuple):
    """
    Structured error returned by tool-code (REQ-01).

    - ``status``        always ``"error"``
    - ``error_code``    machine-readable string constant
    - ``message``       human-readable description
    - ``current_state`` dict snapshot of what is currently available,
                        so the AI knows what it can use next
    - ``hint``          what the AI should try next
    """

    status: str
    error_code: str
    message: str
    current_state: dict
    hint: str
