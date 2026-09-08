MovieTrackingStabilization(bpy_struct)
======================================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MovieTrackingStabilization(bpy_struct)

   2D stabilization based on tracking markers

   .. attribute:: active_rotation_track_index

      Index of active track in rotation stabilization tracks list (in [-inf, inf], default 0)

      :type: int

   .. attribute:: active_track_index

      Index of active track in translation stabilization tracks list (in [-inf, inf], default 0)

      :type: int

   .. attribute:: anchor_frame

      Reference point to anchor stabilization (other frames will be adjusted relative to this frame's position) (in [0, 1048574], default 0)

      :type: int

   .. attribute:: filter_type

      Interpolation to use for sub-pixel shifts and rotations due to stabilization (default ``'NEAREST'``)

      - ``NEAREST``
        Nearest -- No interpolation, use nearest neighbor pixel.
      - ``BILINEAR``
        Bilinear -- Simple interpolation between adjacent pixels.
      - ``BICUBIC``
        Bicubic -- High quality pixel interpolation.

      :type: Literal['NEAREST', 'BILINEAR', 'BICUBIC']

   .. attribute:: influence_location

      Influence of stabilization algorithm on footage location (in [0, 1], default 0.0)

      :type: float

   .. attribute:: influence_rotation

      Influence of stabilization algorithm on footage rotation (in [0, 1], default 0.0)

      :type: float

   .. attribute:: influence_scale

      Influence of stabilization algorithm on footage scale (in [0, 1], default 0.0)

      :type: float

   .. data:: rotation_tracks

      Collection of tracks used for 2D stabilization (translation) (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`MovieTrackingTrack`]

   .. attribute:: scale_max

      Limit the amount of automatic scaling (in [0, 10], default 0.0)

      :type: float

   .. attribute:: show_tracks_expanded

      Show UI list of tracks participating in stabilization (default False)

      :type: bool

   .. attribute:: target_position

      Known relative offset of original shot, will be subtracted (e.g. for panning shot, can be animated) (array of 2 items, in [-inf, inf], default (0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: target_rotation

      Rotation present on original shot, will be compensated (e.g. for deliberate tilting) (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: target_scale

      Explicitly scale resulting frame to compensate zoom of original shot (in [1.192e-07, inf], default 0.0)

      :type: float

   .. data:: tracks

      Collection of tracks used for 2D stabilization (translation) (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`MovieTrackingTrack`]

   .. attribute:: use_2d_stabilization

      Use 2D stabilization for footage (default False)

      :type: bool

   .. attribute:: use_autoscale

      Automatically scale footage to cover unfilled areas when stabilizing (default False)

      :type: bool

   .. attribute:: use_stabilize_rotation

      Stabilize detected rotation around center of frame (default False)

      :type: bool

   .. attribute:: use_stabilize_scale

      Compensate any scale changes relative to center of rotation (default False)

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

   - :class:`MovieTracking.stabilization`

