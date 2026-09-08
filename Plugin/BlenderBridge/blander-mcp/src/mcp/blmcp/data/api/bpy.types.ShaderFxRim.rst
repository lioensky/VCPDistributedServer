ShaderFxRim(ShaderFx)
=====================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ShaderFx`

.. class:: ShaderFxRim(ShaderFx)

   Rim effect

   .. attribute:: blur

      Number of pixels for blurring rim (set to 0 to disable) (array of 2 items, in [0, 32767], default (0, 0))

      :type: :class:`bpy_prop_array`\ [int]

   .. attribute:: mask_color

      Color that must be kept (array of 3 items, in [0, 1], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. attribute:: mode

      Blend mode (default ``'NORMAL'``)

      :type: Literal['NORMAL', 'OVERLAY', 'ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE']

   .. attribute:: offset

      Offset of the rim (array of 2 items, in [-32768, 32767], default (0, 0))

      :type: :class:`bpy_prop_array`\ [int]

   .. attribute:: rim_color

      Color used for Rim (array of 3 items, in [0, 1], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. attribute:: samples

      Number of Blur Samples (zero, disable blur) (in [0, 32], default 4)

      :type: int

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
   - :class:`ShaderFx.name`
   - :class:`ShaderFx.type`
   - :class:`ShaderFx.show_viewport`
   - :class:`ShaderFx.show_render`
   - :class:`ShaderFx.show_in_editmode`
   - :class:`ShaderFx.show_expanded`

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
   - :class:`ShaderFx.bl_rna_get_subclass`
   - :class:`ShaderFx.bl_rna_get_subclass_py`

