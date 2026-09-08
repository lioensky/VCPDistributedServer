ThemeClipEditor(bpy_struct)
===========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ThemeClipEditor(bpy_struct)

   Theme settings for the Movie Clip Editor

   .. attribute:: active_marker

      Color of active marker (array of 3 items, in [0, 1], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. attribute:: disabled_marker

      Color of disabled marker (array of 3 items, in [0, 1], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. attribute:: grid

      (array of 4 items, in [0, 1], default (0.0, 0.0, 0.0, 0.0))

      :type: :class:`bpy_prop_array`\ [float]

   .. attribute:: locked_marker

      Color of locked marker (array of 3 items, in [0, 1], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. attribute:: marker

      Color of marker (array of 3 items, in [0, 1], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. attribute:: marker_outline

      Color of marker's outline (array of 3 items, in [0, 1], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. attribute:: metadatabg

      (array of 3 items, in [0, 1], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. attribute:: metadatatext

      (array of 3 items, in [0, 1], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. attribute:: path_after

      Color of path after current frame (array of 3 items, in [0, 1], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. attribute:: path_before

      Color of path before current frame (array of 3 items, in [0, 1], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. attribute:: path_keyframe_after

      Color of keyframes on a path after current frame (array of 3 items, in [0, 1], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. attribute:: path_keyframe_before

      Color of keyframes on a path before current frame (array of 3 items, in [0, 1], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. attribute:: selected_marker

      Color of selected marker (array of 3 items, in [0, 1], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. data:: space

      Settings for space (readonly, never None)

      :type: :class:`ThemeSpaceGeneric`

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

   - :class:`Theme.clip_editor`

