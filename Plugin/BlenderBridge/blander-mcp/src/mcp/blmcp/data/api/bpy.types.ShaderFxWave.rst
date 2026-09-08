ShaderFxWave(ShaderFx)
======================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ShaderFx`

.. class:: ShaderFxWave(ShaderFx)

   Wave Deformation effect

   .. attribute:: amplitude

      Amplitude of Wave (in [0, inf], default 0.0)

      :type: float

   .. attribute:: orientation

      Direction of the wave (default ``'HORIZONTAL'``)

      :type: Literal['HORIZONTAL', 'VERTICAL']

   .. attribute:: period

      Period of Wave (in [0, inf], default 0.0)

      :type: float

   .. attribute:: phase

      Phase Shift of Wave (in [-inf, inf], default 0.0)

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

