GPU State Utilities (gpu.state)
===============================

.. module:: gpu.state

This module provides access to the gpu state.

.. function:: active_framebuffer_get()

   Return the active frame-buffer in context.

   :return: The active framebuffer.
   :rtype: :class:`gpu.types.GPUFrameBuffer`


.. function:: blend_get()

   Current blending equation.

   :return: The current blend mode.
   :rtype: str


.. function:: blend_set(mode)

   Defines the fixed pipeline blending equation.

   :param mode: The type of blend mode.

      * ``NONE`` No blending.
      * ``ALPHA`` The original color channels are interpolated according to the alpha value.
      * ``ALPHA_PREMULT`` The original color channels are interpolated according to the alpha value with the new colors pre-multiplied by this value.
      * ``ADDITIVE`` The original color channels are added by the corresponding ones.
      * ``ADDITIVE_PREMULT`` The original color channels are added by the corresponding ones that are pre-multiplied by the alpha value.
      * ``MULTIPLY`` The original color channels are multiplied by the corresponding ones.
      * ``SUBTRACT`` The original color channels are subtracted by the corresponding ones.
      * ``INVERT`` The original color channels are replaced by its complementary color.
   :type mode: Literal['NONE', 'ALPHA', 'ALPHA_PREMULT', 'ADDITIVE', 'ADDITIVE_PREMULT', 'MULTIPLY', 'SUBTRACT', 'INVERT']


.. function:: clip_distances_set(distances_enabled)

   Sets the number of ``gl_ClipDistance`` planes used for clip geometry.

   :param distances_enabled: Number of clip distances enabled.
   :type distances_enabled: int


.. function:: color_mask_set(r, g, b, a)

   Enable or disable writing of frame buffer color components.

   :param r: Red component.
   :type r: bool
   :param g: Green component.
   :type g: bool
   :param b: Blue component.
   :type b: bool
   :param a: Alpha component.
   :type a: bool


.. function:: depth_mask_get()

   Writing status in the depth component.

   :return: True if writing to the depth component is enabled.
   :rtype: bool


.. function:: depth_mask_set(value)

   Write to depth component.

   :param value: True for writing to the depth component.
   :type value: bool


.. function:: depth_test_get()

   Current depth_test equation.

   :return: The current depth test mode.
   :rtype: str


.. function:: depth_test_set(mode)

   Defines the depth_test equation.

   :param mode: The depth test equation name.
   :type mode: Literal['NONE', 'ALWAYS', 'LESS', 'LESS_EQUAL', 'EQUAL', 'GREATER', 'GREATER_EQUAL']


.. function:: face_culling_set(culling)

   Specify whether none, front-facing or back-facing facets can be culled.

   :param culling: The face culling mode.
   :type culling: Literal['NONE', 'FRONT', 'BACK']


.. function:: front_facing_set(invert)

   Specifies the orientation of front-facing polygons.

   :param invert: True for clockwise polygons as front-facing.
   :type invert: bool


.. function:: line_width_get()

   Current width of rasterized lines.

   :return: The current line width.
   :rtype: float


.. function:: line_width_set(width)

   Specify the width of rasterized lines.

   :param width: New width.
   :type width: float


.. function:: point_size_set(size)

   Specify the diameter of rasterized points.

   :param size: New diameter.
   :type size: float


.. function:: program_point_size_set(enable)

   If enabled, the derived point size is taken from the (potentially clipped) shader builtin gl_PointSize.

   :param enable: True for shader builtin gl_PointSize.
   :type enable: bool


.. function:: scissor_get()

   Retrieve the scissors of the active framebuffer.
   Note: Only valid between 'scissor_set' and a framebuffer rebind.

   :return: The scissor of the active framebuffer as a tuple
        (x, y, xsize, ysize).
        x, y: lower left corner of the scissor rectangle, in pixels.
        xsize, ysize: width and height of the scissor rectangle.
   :rtype: tuple[int, int, int, int]


.. function:: scissor_set(x, y, xsize, ysize)

   Specifies the scissor area of the active framebuffer.
   Note: The scissor state is not saved upon framebuffer rebind.

   :param x: Lower left corner x coordinate, in pixels.
   :type x: int
   :param y: Lower left corner y coordinate, in pixels.
   :type y: int
   :param xsize: Width of the scissor rectangle.
   :type xsize: int
   :param ysize: Height of the scissor rectangle.
   :type ysize: int


.. function:: scissor_test_set(enable)

   Enable/disable scissor testing on the active framebuffer.

   :param enable:
        True - enable scissor testing.
        False - disable scissor testing.
   :type enable: bool


.. function:: viewport_get()

   Viewport of the active framebuffer.

   :return: The viewport as a tuple (x, y, xsize, ysize).
   :rtype: tuple[int, int, int, int]


.. function:: viewport_set(x, y, xsize, ysize)

   Specifies the viewport of the active framebuffer.
   Note: The viewport state is not saved upon framebuffer rebind.

   :param x: Lower left corner x coordinate, in pixels.
   :type x: int
   :param y: Lower left corner y coordinate, in pixels.
   :type y: int
   :param xsize: Width of the viewport.
   :type xsize: int
   :param ysize: Height of the viewport.
   :type ysize: int


