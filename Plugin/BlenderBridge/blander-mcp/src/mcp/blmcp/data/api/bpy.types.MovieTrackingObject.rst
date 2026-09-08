MovieTrackingObject(bpy_struct)
===============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MovieTrackingObject(bpy_struct)

   Match-moving object tracking and reconstruction data

   .. data:: is_camera

      Object is used for camera tracking (default False, readonly)

      :type: bool

   .. attribute:: keyframe_a

      First keyframe used for reconstruction initialization (in [-inf, inf], default 0)

      :type: int

   .. attribute:: keyframe_b

      Second keyframe used for reconstruction initialization (in [-inf, inf], default 0)

      :type: int

   .. attribute:: name

      Unique name of object (default "", never None)

      :type: str

   .. data:: plane_tracks

      Collection of plane tracks in this tracking data object (default None, readonly)

      :type: :class:`MovieTrackingObjectPlaneTracks`\ [:class:`MovieTrackingPlaneTrack`]

   .. data:: reconstruction

      (readonly)

      :type: :class:`MovieTrackingReconstruction` | None

   .. attribute:: scale

      Scale of object solution in camera space (in [0.0001, 10000], default 1.0)

      :type: float

   .. data:: tracks

      Collection of tracks in this tracking data object (default None, readonly)

      :type: :class:`MovieTrackingObjectTracks`\ [:class:`MovieTrackingTrack`]

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

   - :class:`MovieTracking.objects`
   - :class:`MovieTrackingObjects.active`
   - :class:`MovieTrackingObjects.new`
   - :class:`MovieTrackingObjects.remove`

