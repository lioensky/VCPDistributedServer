# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Inline `_backup_attrs_multi`.

__all__ = ()

import contextlib
from typing import Generator


@contextlib.contextmanager
def _backup_attrs_multi(
        *obj_attrs: tuple[object, tuple[str, ...]],
) -> Generator[list[dict[str, object]], None, None]:
    """
    Context manager that saves named attributes on multiple objects
    and restores them on exit.

    Each argument is a ``(obj, (attr, ...))`` pair. Yields a list of
    dicts (one per pair) containing the saved values.
    """
    saved: list[tuple[object, dict[str, object]]] = []
    result: list[dict[str, object]] = []
    for obj, attrs in obj_attrs:
        d = {attr: getattr(obj, attr) for attr in attrs}
        saved.append((obj, d))
        result.append(d)
    try:
        yield result
    finally:
        for obj, d in saved:
            for attr, value in d.items():
                setattr(obj, attr, value)
