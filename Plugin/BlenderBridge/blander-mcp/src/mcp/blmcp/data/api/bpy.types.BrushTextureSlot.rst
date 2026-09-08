BrushTextureSlot(TextureSlot)
=============================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`TextureSlot`

.. class:: BrushTextureSlot(TextureSlot)

   Texture slot for textures in a Brush data-block

   .. attribute:: angle

      Brush texture rotation (in [0, 6.28319], default 0.0)

      :type: float

   .. data:: has_random_texture_angle

      (default False, readonly)

      :type: bool

   .. data:: has_texture_angle

      (default False, readonly)

      :type: bool

   .. data:: has_texture_angle_source

      (default False, readonly)

      :type: bool

   .. attribute:: map_mode

      (default ``'VIEW_PLANE'``)

      :type: Literal['VIEW_PLANE', 'AREA_PLANE', 'TILED', '3D', 'RANDOM', 'STENCIL']

   .. attribute:: mask_map_mode

      (default ``'VIEW_PLANE'``)

      :type: Literal['VIEW_PLANE', 'TILED', 'RANDOM', 'STENCIL']

   .. attribute:: random_angle

      Brush texture random angle (in [0, 6.28319], default 6.28319)

      :type: float

   .. attribute:: use_rake

      (default False)

      :type: bool

   .. attribute:: use_random

      (default False)

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
   - :class:`TextureSlot.texture`
   - :class:`TextureSlot.name`
   - :class:`TextureSlot.offset`
   - :class:`TextureSlot.scale`
   - :class:`TextureSlot.color`
   - :class:`TextureSlot.blend_type`
   - :class:`TextureSlot.default_value`
   - :class:`TextureSlot.output_node`

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
   - :class:`TextureSlot.bl_rna_get_subclass`
   - :class:`TextureSlot.bl_rna_get_subclass_py`

References
----------

.. hlist::
   :columns: 2

   - :class:`Brush.mask_texture_slot`
   - :class:`Brush.texture_slot`

