gpu_extras submodule (gpu_extras.presets)
=========================================

.. module:: gpu_extras.presets

.. function:: draw_circle_2d(position, color, radius, *, segments=None)

   Draw a circle.
   
   :param position: 2D position where the circle will be drawn.
   :type position: Sequence[float]
   :param color: Color of the circle (RGBA).
      To use transparency blend must be set to ``ALPHA``, see: :func:`gpu.state.blend_set`.
   :type color: Sequence[float]
   :param radius: Radius of the circle.
   :type radius: float
   :param segments: How many segments will be used to draw the circle.
       Higher values give better results but the drawing will take longer.
       If None or not specified, an automatic value will be calculated.
   :type segments: int | None

.. function:: draw_texture_2d(texture, position, width, height, is_scene_linear_with_rec709_srgb_target=False)

   Draw a 2d texture.
   
   :param texture: GPUTexture to draw (e.g. gpu.texture.from_image(image) for :class:`bpy.types.Image`).
   :type texture: :class:`gpu.types.GPUTexture`
   :param position: 2D position of the lower left corner.
   :type position: Sequence[float]
   :param width: Width of the image when drawn (not necessarily
       the original width of the texture).
   :type width: float
   :param height: Height of the image when drawn.
   :type height: float
   :param is_scene_linear_with_rec709_srgb_target:
       True if the `texture` is stored in scene linear color space and
       the destination frame-buffer uses the Rec.709 sRGB color space
       (which is true when drawing textures acquired from :class:`bpy.types.Image` inside a
       'PRE_VIEW', 'POST_VIEW' or 'POST_PIXEL' draw handler).
       Otherwise the color space is assumed to match the one of the frame-buffer. (default=False)
   :type is_scene_linear_with_rec709_srgb_target: bool

