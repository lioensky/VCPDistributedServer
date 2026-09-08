Font Drawing (blf)
==================

.. module:: blf

This module provides access to Blender's text drawing functions.


Hello World Text Example
++++++++++++++++++++++++

Example of using the blf module. For this module to work we
need to use the GPU module :mod:`gpu` as well.

.. literalinclude:: ./examples/blf.0.py
   :lines: 8-


Drawing Text to an Image
++++++++++++++++++++++++

Example showing how text can be drawn into an image.
This can be done by binding an image buffer (:mod:`imbuf`) to the font's ID.

.. literalinclude:: ./examples/blf.1.py
   :lines: 9-

.. function:: aspect(fontid, aspect)

   Set the aspect for drawing text.

   :param fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
   :type fontid: int
   :param aspect: The aspect ratio for non-uniform scaling of text.
   :type aspect: float


.. function:: bind_imbuf(fontid, imbuf, *, display_name=None)

   Context manager to draw text into an image buffer instead of the GPU's context.

   :param fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
   :type fontid: int
   :param imbuf: The image to draw into.
   :type imbuf: :class:`imbuf.types.ImBuf`
   :param display_name: Ignored (formerly a color-space transform name), kept for backwards compatibility.
   :type display_name: str | None
   :return: The BLF ImBuf context manager.
   :rtype: BLFImBufContext


.. function:: clipping(fontid, xmin, ymin, xmax, ymax)

   Set the clipping, enable/disable using :data:`CLIPPING`.

   :param fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
   :type fontid: int
   :param xmin: Left edge of the clipping rectangle.
   :type xmin: float
   :param ymin: Bottom edge of the clipping rectangle.
   :type ymin: float
   :param xmax: Right edge of the clipping rectangle.
   :type xmax: float
   :param ymax: Top edge of the clipping rectangle.
   :type ymax: float


.. function:: color(fontid, r, g, b, a)

   Set the color for drawing text.

   :param fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
   :type fontid: int
   :param r: Red channel 0.0 - 1.0.
   :type r: float
   :param g: Green channel 0.0 - 1.0.
   :type g: float
   :param b: Blue channel 0.0 - 1.0.
   :type b: float
   :param a: Alpha channel 0.0 - 1.0.
   :type a: float


.. function:: dimensions(fontid, text)

   Return the width and height of the text.

   :param fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
   :type fontid: int
   :param text: The text to measure.
   :type text: str
   :return: The width and height of the text.
   :rtype: tuple[float, float]


.. function:: disable(fontid, option)

   Disable a font drawing option.

   :param fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
   :type fontid: int
   :param option: One of :data:`ROTATION`, :data:`CLIPPING`, :data:`SHADOW`, :data:`MONOCHROME` or :data:`WORD_WRAP`.
   :type option: int


.. function:: draw(fontid, text)

   Draw text in the current context.

   :param fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
   :type fontid: int
   :param text: The text to draw.
   :type text: str


.. function:: draw_buffer(fontid, text)

   Draw text into the image buffer bound via :func:`blf.bind_imbuf`.

   :param fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
   :type fontid: int
   :param text: The text to draw into the bound image buffer.
   :type text: str


.. function:: enable(fontid, option)

   Enable a font drawing option.

   :param fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
   :type fontid: int
   :param option: One of :data:`ROTATION`, :data:`CLIPPING`, :data:`SHADOW`, :data:`MONOCHROME` or :data:`WORD_WRAP`.
   :type option: int


.. function:: load(filepath)

   Load a new font.

   :param filepath: The filepath of the font.
   :type filepath: str | bytes
   :return: The new font's fontid or -1 if there was an error.
   :rtype: int


.. function:: position(fontid, x, y, z)

   Set the position for drawing text.

   :param fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
   :type fontid: int
   :param x: X axis position to draw the text.
   :type x: float
   :param y: Y axis position to draw the text.
   :type y: float
   :param z: Z axis position to draw the text (typically 0).
   :type z: float


.. function:: rotation(fontid, angle)

   Set the text rotation angle, enable/disable using :data:`ROTATION`.

   :param fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
   :type fontid: int
   :param angle: The angle for text drawing to use (in radians).
   :type angle: float


.. function:: shadow(fontid, level, r, g, b, a)

   Shadow options, enable/disable using :data:`SHADOW`.

   :param fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
   :type fontid: int
   :param level: The shadow type: 0 for none, 3 for 3x3 blur, 5 for 5x5 blur or 6 for outline. Other values raise a :exc:`TypeError`.
   :type level: int
   :param r: Shadow color (red channel 0.0 - 1.0).
   :type r: float
   :param g: Shadow color (green channel 0.0 - 1.0).
   :type g: float
   :param b: Shadow color (blue channel 0.0 - 1.0).
   :type b: float
   :param a: Shadow color (alpha channel 0.0 - 1.0).
   :type a: float


.. function:: shadow_offset(fontid, x, y)

   Set the offset for shadow text, enable/disable using :data:`SHADOW`.

   :param fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
   :type fontid: int
   :param x: Horizontal shadow offset value in pixels.
   :type x: int
   :param y: Vertical shadow offset value in pixels.
   :type y: int


.. function:: size(fontid, size)

   Set the size for drawing text.

   :param fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
   :type fontid: int
   :param size: Point size of the font.
   :type size: float


.. function:: unload(filepath)

   Unload an existing font.

   :param filepath: The filepath of the font.
   :type filepath: str | bytes


.. function:: word_wrap(fontid, wrap_width)

   Set the wrap width, enable/disable using :data:`WORD_WRAP`.

   :param fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
   :type fontid: int
   :param wrap_width: The width (in pixels) to wrap words at.
   :type wrap_width: int


.. data:: CLIPPING

   Constant value 2

.. data:: MONOCHROME

   Constant value 128

.. data:: ROTATION

   Constant value 1

.. data:: SHADOW

   Constant value 4

.. data:: WORD_WRAP

   Constant value 64

