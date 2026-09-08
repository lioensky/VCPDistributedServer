ImagePaint(Paint)
=================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Paint`

.. class:: ImagePaint(Paint)

   Properties of image and texture painting mode

   .. attribute:: canvas

      Image used as canvas

      :type: :class:`Image` | None

   .. attribute:: clone_alpha

      Opacity of clone image display (in [0, 1], default 0.5)

      :type: float

   .. attribute:: clone_image

      Image used as clone source

      :type: :class:`Image` | None

   .. attribute:: clone_offset

      (array of 2 items, in [-inf, inf], default (0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: dither

      Amount of dithering when painting on byte images (in [0, 2], default 0.0)

      :type: float

   .. attribute:: interpolation

      Texture filtering type (default ``'LINEAR'``)

      - ``LINEAR``
        Linear -- Linear interpolation.
      - ``CLOSEST``
        Closest -- No interpolation (sample closest texel).

      :type: Literal['LINEAR', 'CLOSEST']

   .. attribute:: invert_stencil

      Invert the stencil layer (default False)

      :type: bool

   .. data:: missing_materials

      The mesh is missing materials (default False, readonly)

      :type: bool

   .. data:: missing_stencil

      Image Painting does not have a stencil (default False, readonly)

      :type: bool

   .. data:: missing_texture

      Image Painting does not have a texture to paint on (default False, readonly)

      :type: bool

   .. data:: missing_uvs

      A UV layer is missing on the mesh (default False, readonly)

      :type: bool

   .. attribute:: mode

      Mode of operation for projection painting (default ``'MATERIAL'``)

      - ``MATERIAL``
        Material -- Detect image slots from the material.
      - ``IMAGE``
        Single Image -- Set image for texture painting directly.

      :type: Literal['MATERIAL', 'IMAGE']

   .. attribute:: normal_angle

      Paint most on faces pointing towards the view according to this angle (in [0, 90], default 80)

      :type: int

   .. attribute:: screen_grab_size

      Size to capture the image for re-projecting (array of 2 items, in [512, 16384], default (0, 0))

      :type: :class:`bpy_prop_array`\ [int]

   .. attribute:: seam_bleed

      Extend paint beyond the faces' UVs to reduce seams (in pixels, slower) (in [-32768, 32767], default 2)

      :type: int

   .. attribute:: stencil_color

      Stencil color in the viewport (array of 3 items, in [0, 1], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. attribute:: stencil_image

      Image used as stencil

      :type: :class:`Image` | None

   .. attribute:: use_backface_culling

      Ignore faces pointing away from the view (faster) (default True)

      :type: bool

   .. attribute:: use_clone_layer

      Use another UV map as clone source, otherwise use the 3D cursor as the source (default False)

      :type: bool

   .. attribute:: use_normal_falloff

      Paint most on faces pointing towards the view (default True)

      :type: bool

   .. attribute:: use_occlude

      Only paint onto the faces directly under the brush (slower) (default True)

      :type: bool

   .. attribute:: use_stencil_layer

      Set the mask layer from the UV map buttons (default False)

      :type: bool

   .. method:: detect_data()

      Check if required texpaint data exist

      :rtype: bool

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
   - :class:`Paint.brush`
   - :class:`Paint.brush_asset_reference`
   - :class:`Paint.eraser_brush`
   - :class:`Paint.eraser_brush_asset_reference`
   - :class:`Paint.palette`
   - :class:`Paint.show_brush`
   - :class:`Paint.show_brush_on_surface`
   - :class:`Paint.show_low_resolution`
   - :class:`Paint.use_sculpt_delay_updates`
   - :class:`Paint.show_bvh_nodes`
   - :class:`Paint.use_symmetry_x`
   - :class:`Paint.use_symmetry_y`
   - :class:`Paint.use_symmetry_z`
   - :class:`Paint.use_symmetry_feather`
   - :class:`Paint.cavity_curve`
   - :class:`Paint.use_cavity`
   - :class:`Paint.tile_offset`
   - :class:`Paint.tile_x`
   - :class:`Paint.tile_y`
   - :class:`Paint.tile_z`
   - :class:`Paint.show_strength_curve`
   - :class:`Paint.show_size_curve`
   - :class:`Paint.show_jitter_curve`
   - :class:`Paint.unified_paint_settings`

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
   - :class:`Paint.bl_rna_get_subclass`
   - :class:`Paint.bl_rna_get_subclass_py`

References
----------

.. hlist::
   :columns: 2

   - :class:`ToolSettings.image_paint`

