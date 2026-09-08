MovieTrackingMarker(bpy_struct)
===============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MovieTrackingMarker(bpy_struct)

   Match-moving marker data for tracking

   .. attribute:: co

      Marker position at frame in normalized coordinates (array of 2 items, in [-inf, inf], default (0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: frame

      Frame number marker is keyframed on (in [-inf, inf], default 0)

      :type: int

   .. attribute:: is_keyed

      Whether the position of the marker is keyframed or tracked (default True)

      :type: bool

   .. attribute:: mute

      Is marker muted for current frame (default False)

      :type: bool

   .. data:: pattern_bound_box

      Pattern area bounding box in normalized coordinates (multi-dimensional array of 2 * 2 items, in [-inf, inf], default ((0.0, 0.0), (0.0, 0.0)), readonly)

      :type: :class:`bpy_prop_array`\ [float]

   .. attribute:: pattern_corners

      Array of coordinates which represents pattern's corners in normalized coordinates relative to marker position (multi-dimensional array of 4 * 2 items, in [-inf, inf], default ((0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0)))

      :type: :class:`bpy_prop_array`\ [float]

   .. attribute:: search_max

      Right-bottom corner of search area in normalized coordinates relative to marker position (array of 2 items, in [-inf, inf], default (0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: search_min

      Left-bottom corner of search area in normalized coordinates relative to marker position (array of 2 items, in [-inf, inf], default (0.0, 0.0))

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

   - :class:`MovieTrackingMarkers.find_frame`
   - :class:`MovieTrackingMarkers.insert_frame`
   - :class:`MovieTrackingTrack.markers`

