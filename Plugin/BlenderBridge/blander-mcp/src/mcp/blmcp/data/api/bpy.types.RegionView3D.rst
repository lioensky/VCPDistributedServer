RegionView3D(bpy_struct)
========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: RegionView3D(bpy_struct)

   3D View region data

   .. attribute:: clip_planes

      (multi-dimensional array of 6 * 4 items, in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)))

      :type: :class:`bpy_prop_array`\ [float]

   .. attribute:: is_orthographic_side_view

      Whether the current view is aligned to an axis (does not check whether the view is orthographic, use "is_perspective" for that). Setting this will rotate the view to the closest axis (default False)

      :type: bool

   .. attribute:: is_perspective

      (default False)

      :type: bool

   .. attribute:: lock_rotation

      Lock view rotation of side views to Top/Front/Right (default False)

      :type: bool

   .. data:: perspective_matrix

      Current perspective matrix (``window_matrix * view_matrix``) (multi-dimensional array of 4 * 4 items, in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)), readonly)

      :type: :class:`mathutils.Matrix`

   .. attribute:: show_sync_view

      Sync view position between side views (default False)

      :type: bool

   .. attribute:: use_box_clip

      Clip view contents based on what is visible in other side views (default False)

      :type: bool

   .. attribute:: use_clip_planes

      (default False)

      :type: bool

   .. attribute:: view_camera_offset

      View shift in camera view (array of 2 items, in [-inf, inf], default (0.0, 0.0))

      :type: :class:`bpy_prop_array`\ [float]

   .. attribute:: view_camera_zoom

      Zoom factor in camera view (in [-30, 600], default 0.0)

      :type: float

   .. attribute:: view_distance

      Distance to the view location (in [0, inf], default 0.0)

      :type: float

   .. attribute:: view_location

      View pivot location (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: view_matrix

      Current view matrix (multi-dimensional array of 4 * 4 items, in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)))

      :type: :class:`mathutils.Matrix`

   .. attribute:: view_perspective

      View Perspective (default ``'ORTHO'``)

      :type: Literal['PERSP', 'ORTHO', 'CAMERA']

   .. attribute:: view_rotation

      Rotation in quaternions (keep normalized) (array of 4 items, in [-inf, inf], default (0.0, 0.0, 0.0, 0.0))

      :type: :class:`mathutils.Quaternion`

   .. data:: window_matrix

      Current window matrix (multi-dimensional array of 4 * 4 items, in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)), readonly)

      :type: :class:`mathutils.Matrix`

   .. method:: update()

      Recalculate the view matrices


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

   - :class:`Context.region_data`
   - :class:`SpaceView3D.region_3d`
   - :class:`SpaceView3D.region_quadviews`

