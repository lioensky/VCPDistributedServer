MaterialGPencilStyle(bpy_struct)
================================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MaterialGPencilStyle(bpy_struct)


   .. attribute:: alignment_mode

      Defines how align Dots and Boxes with drawing path and object rotation (default ``'PATH'``)

      - ``PATH``
        Path -- Follow stroke drawing path and object rotation.
      - ``OBJECT``
        Object -- Follow object rotation only.
      - ``FIXED``
        Fixed -- Do not follow drawing path or object rotation and keeps aligned with viewport.

      :type: Literal['PATH', 'OBJECT', 'FIXED']

   .. attribute:: alignment_rotation

      Additional rotation applied to dots and square texture of strokes. Only applies in texture shading mode. (in [-1.5708, 1.5708], default 0.0)

      :type: float

   .. attribute:: color

      (array of 4 items, in [0, 1], default (0.0, 0.0, 0.0, 0.0))

      :type: :class:`bpy_prop_array`\ [float]

   .. attribute:: fill_color

      Color for filling region bounded by each stroke (array of 4 items, in [0, 1], default (0.0, 0.0, 0.0, 0.0))

      :type: :class:`bpy_prop_array`\ [float]

   .. attribute:: fill_image

      :type: :class:`Image` | None

   .. attribute:: fill_style

      Select style used to fill strokes (default ``'SOLID'``)

      - ``SOLID``
        Solid -- Fill area with solid color.
      - ``GRADIENT``
        Gradient -- Fill area with gradient color.
      - ``TEXTURE``
        Texture -- Fill area with image texture.

      :type: Literal['SOLID', 'GRADIENT', 'TEXTURE']

   .. attribute:: flip

      Flip filling colors (default False)

      :type: bool

   .. attribute:: ghost

      Display strokes using this color when showing onion skins (default False)

      :type: bool

   .. attribute:: gradient_type

      Select type of gradient used to fill strokes (default ``'LINEAR'``)

      - ``LINEAR``
        Linear -- Fill area with gradient color.
      - ``RADIAL``
        Radial -- Fill area with radial gradient.

      :type: Literal['LINEAR', 'RADIAL']

   .. attribute:: hide

      Set color Visibility (default False)

      :type: bool

   .. data:: is_fill_visible

      True when opacity of fill is set high enough to be visible (default False, readonly)

      :type: bool

   .. data:: is_stroke_visible

      True when opacity of stroke is set high enough to be visible (default False, readonly)

      :type: bool

   .. attribute:: lock

      Protect color from further editing and/or frame changes (default False)

      :type: bool

   .. attribute:: mix_color

      Color for mixing with primary filling color (array of 4 items, in [0, 1], default (0.0, 0.0, 0.0, 0.0))

      :type: :class:`bpy_prop_array`\ [float]

   .. attribute:: mix_factor

      Mix Factor (in [0, 1], default 0.0)

      :type: float

   .. attribute:: mix_stroke_factor

      Mix Stroke Factor (in [0, 1], default 0.0)

      :type: float

   .. attribute:: mode

      Select line type for strokes (default ``'LINE'``)

      - ``LINE``
        Line -- Draw strokes using a continuous line.
      - ``DOTS``
        Dots -- Draw strokes using separated dots.
      - ``BOX``
        Squares -- Draw strokes using separated squares.

      :type: Literal['LINE', 'DOTS', 'BOX']

   .. attribute:: pass_index

      Index number for the "Color Index" pass (in [0, 32767], default 0)

      :type: int

   .. attribute:: pixel_size

      Texture Pixel Size factor along the stroke (in [1, 5000], default 0.0)

      :type: float

   .. attribute:: show_fill

      Show stroke fills of this material (default False)

      .. deprecated:: 5.10 removal planned in version 6.0

         Unused but kept for compatibility with older versions of Blender.

      :type: bool

   .. attribute:: show_stroke

      Show stroke lines of this material (default False)

      .. deprecated:: 5.10 removal planned in version 6.0

         Unused but kept for compatibility with older versions of Blender.

      :type: bool

   .. attribute:: stroke_image

      :type: :class:`Image` | None

   .. attribute:: stroke_style

      Select style used to draw strokes (default ``'SOLID'``)

      - ``SOLID``
        Solid -- Draw strokes with solid color.
      - ``TEXTURE``
        Texture -- Draw strokes using texture.

      :type: Literal['SOLID', 'TEXTURE']

   .. attribute:: texture_angle

      Texture Orientation Angle (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: texture_clamp

      Do not repeat texture and clamp to one instance only (default False)

      :type: bool

   .. attribute:: texture_offset

      Shift Texture in 2d Space (array of 2 items, in [-inf, inf], default (0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: texture_scale

      Scale Factor for Texture (array of 2 items, in [-inf, inf], default (0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: use_fill_holdout

      Remove the color from underneath this stroke by using it as a mask (default False)

      :type: bool

   .. attribute:: use_overlap_strokes

      Disable stencil and overlap self intersections with alpha materials (default False)

      :type: bool

   .. attribute:: use_stroke_holdout

      Remove the color from underneath this stroke by using it as a mask (default False)

      :type: bool

   .. classmethod:: bl_rna_get_subclass(id, default=None, /)
   
      :param id: The RNA type identifier.
      :type id: str
      :param default: The value to return when not found.
      :type default: :class:`bpy.types.Struct` | None
      :return: The RNA type or default when not found.
      :rtype: :class:`bpy.types.Struct`


   .. classmethod:: bl_rna_get_subclass_py(id, default=None, /)
   
      :param id: The RNA type identifier.
      :type id: str
      :param default: The value to return when not found.
      :type default: type | None
      :return: The class or default when not found.
      :rtype: type


Inherited Properties
--------------------

.. hlist::
   :columns: 2

   - :class:`bpy_struct.id_data`

Inherited Functions
-------------------

.. hlist::
   :columns: 2

   - :class:`bpy_struct.as_pointer`
   - :class:`bpy_struct.driver_add`
   - :class:`bpy_struct.driver_remove`
   - :class:`bpy_struct.get`
   - :class:`bpy_struct.id_properties_clear`
   - :class:`bpy_struct.id_properties_ensure`
   - :class:`bpy_struct.id_properties_ui`
   - :class:`bpy_struct.is_property_hidden`
   - :class:`bpy_struct.is_property_overridable_library`
   - :class:`bpy_struct.is_property_readonly`
   - :class:`bpy_struct.is_property_set`
   - :class:`bpy_struct.items`
   - :class:`bpy_struct.keyframe_delete`
   - :class:`bpy_struct.keyframe_insert`
   - :class:`bpy_struct.keys`
   - :class:`bpy_struct.path_from_id`
   - :class:`bpy_struct.path_from_module`
   - :class:`bpy_struct.path_resolve`
   - :class:`bpy_struct.pop`
   - :class:`bpy_struct.property_overridable_library_set`
   - :class:`bpy_struct.property_unset`
   - :class:`bpy_struct.rna_ancestors`
   - :class:`bpy_struct.type_recast`
   - :class:`bpy_struct.values`

References
----------

.. hlist::
   :columns: 2

   - :class:`Material.grease_pencil`

