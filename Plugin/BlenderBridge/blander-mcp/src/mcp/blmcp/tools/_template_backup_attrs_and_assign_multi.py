# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Inline `_backup_attrs_and_assign_multi`.

__all__ = ()

import contextlib
from typing import Generator


@contextlib.contextmanager
def _backup_attrs_and_assign_multi(
        *obj_attrs: tuple[object, dict[str, object]],
) -> Generator[None, None, None]:
    """
    Context manager that saves and assigns attributes on multiple objects,
    restoring all originals on exit.

    Each argument is a ``(obj, {attr: value, ...})`` pair.
    """
    saved: list[tuple[object, dict[str, object]]] = []
    try:
        for obj, attrs in obj_attrs:
            saved.append((obj, {attr: getattr(obj, attr) for attr in attrs}))
            for attr, value in attrs.items():
                setattr(obj, attr, value)
        yield
    finally:
        for obj, attrs in saved:
            for attr, value in attrs.items():
                setattr(obj, attr, value)
