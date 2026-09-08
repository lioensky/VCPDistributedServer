# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Context manager to capture STDOUT/STDERR while also forwarding to the real output.

Useful so the LLM may use print(..) style debugging and receive the results as part of the response.
"""

__all__ = (
    "CaptureOutput",
)

import io
import sys
from typing import IO, Self


class _Tee(io.TextIOBase):
    """Write to both a :class:`io.StringIO` buffer and the original stream."""
    __slots__ = (
        "_buffer",
        "_original",
    )

    def __init__(self, original: IO[str]) -> None:
        self._buffer = io.StringIO()
        self._original = original

    def write(self, s: str) -> int:
        self._original.write(s)
        return self._buffer.write(s)

    def flush(self) -> None:
        self._original.flush()
        self._buffer.flush()

    def getvalue(self) -> str:
        return self._buffer.getvalue()


class CaptureOutput:
    """
    Context manager that captures STDOUT & STDERR.

    Output is forwarded to the original streams in real time
    and also stored for retrieval via :meth:`stdout` and :meth:`stderr`.
    """
    __slots__ = (
        "_tee_out",
        "_tee_err",
        "_original_out",
        "_original_err",
    )

    def __enter__(self) -> Self:
        self._original_out = sys.stdout
        self._original_err = sys.stderr
        self._tee_out = _Tee(self._original_out)
        self._tee_err = _Tee(self._original_err)
        sys.stdout = self._tee_out
        sys.stderr = self._tee_err
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: object,
    ) -> None:
        del exc_type, exc_val, exc_tb
        sys.stdout = self._original_out
        sys.stderr = self._original_err

    @property
    def stdout(self) -> str:
        return self._tee_out.getvalue()

    @property
    def stderr(self) -> str:
        return self._tee_err.getvalue()
