FModifierSmooth(FModifier)
==========================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`FModifier`

.. class:: FModifierSmooth(FModifier)

   Smooth curve using Gaussian smoothing

   .. attribute:: filter_width

      The number of frames to average around each keyframe. Higher values allow more smoothing, but will decrease performance. (in [1, 32], default 0)

      :type: int

   .. attribute:: sigma

      The shape of the Gaussian distribution in frames. Lower values will increase sharpness across the Filter Width. (in [0.1, 100], default 0.0)

      :type: float

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
   - :class:`FModifier.name`
   - :class:`FModifier.type`
   - :class:`FModifier.show_expanded`
   - :class:`FModifier.mute`
   - :class:`FModifier.is_valid`
   - :class:`FModifier.active`
   - :class:`FModifier.use_restricted_range`
   - :class:`FModifier.frame_start`
   - :class:`FModifier.frame_end`
   - :class:`FModifier.blend_in`
   - :class:`FModifier.blend_out`
   - :class:`FModifier.use_influence`
   - :class:`FModifier.influence`

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
   - :class:`FModifier.bl_rna_get_subclass`
   - :class:`FModifier.bl_rna_get_subclass_py`

