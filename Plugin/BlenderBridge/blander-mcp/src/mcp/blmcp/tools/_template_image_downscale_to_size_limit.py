# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Inline `_image_downscale_to_size_limit`.

__all__ = ()


def _image_downscale_to_size_limit(
        tmpdir: str, filepath: str,
        size_limit_in_bytes: int,
        size_tolerance_in_bytes: int = 0,
) -> bytes:
    """
    Downscale *filepath* for HiDPI and to stay under *size_limit_in_bytes*.

    *size_tolerance_in_bytes* defines an acceptable margin below the limit.
    Once a result fits within ``size_limit - tolerance``, the search stops
    instead of continuing to find the least-downscaled option.

    Returns the image file contents as bytes.
    """
    import os

    # Early out: if the file already fits, no processing needed.
    if os.path.getsize(filepath) <= size_limit_in_bytes:
        with open(filepath, "rb") as fh:
            return fh.read()

    import imbuf  # type: ignore[import-not-found]  # pylint: disable=import-error,no-name-in-module
    from bpy import context  # pylint: disable=import-error,no-name-in-module

    filepath_out = os.path.join(tmpdir, "downscaled.png")
    im = imbuf.load(filepath)

    # Downscale HiDPI images to logical pixel size.
    pixel_size = context.preferences.system.pixel_size
    if pixel_size > 1.0:
        w, h = im.size
        im.resize((round(w / pixel_size), round(h / pixel_size)), method='BILINEAR')

    def _write_and_read(im_buf: "imbuf.types.ImBuf") -> bytes:
        imbuf.write(im_buf, filepath=filepath_out)
        with open(filepath_out, "rb") as fh:
            return fh.read()

    def _encode_at_divisor(divisor: int) -> bytes | None:
        new_w = orig_w // divisor
        new_h = orig_h // divisor
        if new_w <= 64 or new_h <= 64:
            return None
        im_copy = im.copy()
        im_copy.resize((new_w, new_h), method='BILINEAR')
        result = _write_and_read(im_copy)
        im_copy.free()
        return result

    try:
        # Re-encode after HiDPI downscale (if applied) and check size.
        data = _write_and_read(im)
        if len(data) <= size_limit_in_bytes:
            return data

        # Dimension divisors: powers of 2 interleaved with 3x powers of 2.
        # Gives: 1/2, 1/3, 1/4, 1/6, 1/8, 1/12, ... of the original.
        divisors = (2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 64)

        orig_w, orig_h = im.size

        # Trim divisors that would push dimensions below 64px.
        max_idx = -1
        for i, d in enumerate(divisors):
            if orig_w // d > 64 and orig_h // d > 64:
                max_idx = i
            else:
                break

        if max_idx < 0:
            return data

        # Binary search for the lowest divisor whose output fits.
        # Each probe estimates the next midpoint from the actual encoded size.
        # PNG size scales roughly with pixel count (1/divisor^2),
        # so: needed_divisor ~= current_divisor * sqrt(current_size / limit).
        # Falls back to standard bisection when the range is too small.
        import math
        lo, hi = 0, max_idx
        # Initial estimate uses divisor=1 (the full-size encode above).
        estimated = math.sqrt(len(data) / size_limit_in_bytes)
        while lo <= hi:
            if hi - lo >= 2:
                mid = min(hi - 1, max(lo + 1, min(
                    range(lo, hi + 1),
                    key=lambda i: abs(divisors[i] - estimated),
                )))
            else:
                mid = (lo + hi) // 2
            test_filedata_as_bytes = _encode_at_divisor(divisors[mid])
            if test_filedata_as_bytes is not None and len(test_filedata_as_bytes) <= size_limit_in_bytes:
                data = test_filedata_as_bytes
                if len(test_filedata_as_bytes) == size_limit_in_bytes:
                    break  # Exact fit, no better option possible.
                if size_tolerance_in_bytes > 0:
                    if len(test_filedata_as_bytes) < size_limit_in_bytes:
                        if len(test_filedata_as_bytes) >= size_limit_in_bytes - size_tolerance_in_bytes:
                            break  # Smaller but not by much, good enough.
                hi = mid - 1
                # Re-estimate: this divisor was enough, maybe a smaller one works.
                estimated = divisors[mid] * math.sqrt(len(test_filedata_as_bytes) / size_limit_in_bytes)
            else:
                lo = mid + 1
                # Re-estimate: need more scaling.
                if test_filedata_as_bytes is not None:
                    estimated = divisors[mid] * math.sqrt(len(test_filedata_as_bytes) / size_limit_in_bytes)

    finally:
        im.free()

    return data
