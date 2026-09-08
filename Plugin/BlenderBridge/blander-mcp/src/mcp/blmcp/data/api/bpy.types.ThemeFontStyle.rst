ThemeFontStyle(bpy_struct)
==========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ThemeFontStyle(bpy_struct)

   Theme settings for Font

   .. attribute:: character_weight

      Weight of the characters. 100-900, 400 is normal. (in [100, 900], default 400)

      :type: int

   .. attribute:: points

      Font size in points (in [6, 32], default 0.0)

      :type: float

   .. attribute:: shadow

      Shadow type (0 none, 3, 5 blur, 6 outline) (in [0, 6], default 0)

      :type: int

   .. attribute:: shadow_alpha

      (in [0, 1], default 0.0)

      :type: float

   .. attribute:: shadow_offset_x

      Shadow offset in pixels (in [-10, 10], default 0)

      :type: int

   .. attribute:: shadow_offset_y

      Shadow offset in pixels (in [-10, 10], default 0)

      :type: int

   .. attribute:: shadow_value

      Shadow color in gray value (in [0, 1], default 0.0)

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

   - :class:`ThemeStyle.panel_title`
   - :class:`ThemeStyle.tooltip`
   - :class:`ThemeStyle.widget`

