NDOFMotionEventData(bpy_struct)
===============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: NDOFMotionEventData(bpy_struct)

   NDOF motion data for window manager events

   .. data:: progress

      Indicates the gesture phase (default ``'STARTING'``, readonly)

      :type: Literal['STARTING', 'IN_PROGRESS', 'FINISHING']

   .. data:: rotation

      Axis-angle rotation of this motion event. The vector magnitude is the angle where 1.0 represents 360 degrees. The angle is typically scaled by the time-delta before use. (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0), readonly)

      :type: :class:`mathutils.Vector`

   .. data:: time_delta

      Time since previous motion event (in seconds) (in [-inf, inf], default 0.0, readonly)

      :type: float

   .. data:: translation

      The translation of this motion event. The range on each axis is [-1 to 1], before being multiplied by the sensitivity preference. This is typically scaled by the time-delta before use. (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0), readonly)

      :type: :class:`mathutils.Vector`

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

   - :class:`Event.ndof_motion`

