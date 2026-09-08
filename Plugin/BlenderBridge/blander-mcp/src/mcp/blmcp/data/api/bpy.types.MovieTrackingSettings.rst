MovieTrackingSettings(bpy_struct)
=================================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MovieTrackingSettings(bpy_struct)

   Match moving settings

   .. attribute:: clean_action

      Cleanup action to execute (default ``'SELECT'``)

      - ``SELECT``
        Select -- Select unclean tracks.
      - ``DELETE_TRACK``
        Delete Track -- Delete unclean tracks.
      - ``DELETE_SEGMENTS``
        Delete Segments -- Delete unclean segments of tracks.

      :type: Literal['SELECT', 'DELETE_TRACK', 'DELETE_SEGMENTS']

   .. attribute:: clean_error

      Effect on tracks which have a larger re-projection error (in [0, inf], default 0.0)

      :type: float

   .. attribute:: clean_frames

      Effect on tracks which are tracked less than the specified amount of frames (in [0, inf], default 0)

      :type: int

   .. attribute:: default_correlation_min

      Default minimum value of correlation between matched pattern and reference that is still treated as successful tracking (in [0, 1], default 0.0)

      :type: float

   .. attribute:: default_frames_limit

      Every tracking cycle, this number of frames are tracked (in [0, 32767], default 0)

      :type: int

   .. attribute:: default_margin

      Default distance from image boundary at which marker stops tracking (in [0, 300], default 0)

      :type: int

   .. attribute:: default_motion_model

      Default motion model to use for tracking (default ``'Loc'``)

      - ``Perspective``
        Perspective -- Search for markers that are perspectively deformed (homography) between frames.
      - ``Affine``
        Affine -- Search for markers that are affine-deformed (t, r, k, and skew) between frames.
      - ``LocRotScale``
        Location, Rotation & Scale -- Search for markers that are translated, rotated, and scaled between frames.
      - ``LocScale``
        Location & Scale -- Search for markers that are translated and scaled between frames.
      - ``LocRot``
        Location & Rotation -- Search for markers that are translated and rotated between frames.
      - ``Loc``
        Location -- Search for markers that are translated between frames.

      :type: Literal['Perspective', 'Affine', 'LocRotScale', 'LocScale', 'LocRot', 'Loc']

   .. attribute:: default_pattern_match

      Track pattern from given frame when tracking marker to next frame (default ``'KEYFRAME'``)

      - ``KEYFRAME``
        Keyframe -- Track pattern from keyframe to next frame.
      - ``PREV_FRAME``
        Previous frame -- Track pattern from current frame to next frame.

      :type: Literal['KEYFRAME', 'PREV_FRAME']

   .. attribute:: default_pattern_size

      Size of pattern area for newly created tracks (in [5, 1000], default 0)

      :type: int

   .. attribute:: default_search_size

      Size of search area for newly created tracks (in [5, 1000], default 0)

      :type: int

   .. attribute:: default_weight

      Influence of newly created track on a final solution (in [0, 1], default 0.0)

      :type: float

   .. attribute:: distance

      Distance between two bundles used for scene scaling (in [-inf, inf], default 1.0)

      :type: float

   .. attribute:: object_distance

      Distance between two bundles used for object scaling (in [0.001, 10000], default 1.0)

      :type: float

   .. attribute:: refine_intrinsics_focal_length

      Refine focal length during camera solving (default False)

      :type: bool

   .. attribute:: refine_intrinsics_principal_point

      Refine principal point during camera solving (default False)

      :type: bool

   .. attribute:: refine_intrinsics_radial_distortion

      Refine radial coefficients of distortion model during camera solving (default False)

      :type: bool

   .. attribute:: refine_intrinsics_tangential_distortion

      Refine tangential coefficients of distortion model during camera solving (default False)

      :type: bool

   .. attribute:: speed

      Limit speed of tracking to make visual feedback easier (this does not affect the tracking quality) (default ``'FASTEST'``)

      - ``FASTEST``
        Fastest -- Track as fast as possible.
      - ``DOUBLE``
        Double -- Track with double speed.
      - ``REALTIME``
        Realtime -- Track with realtime speed.
      - ``HALF``
        Half -- Track with half of realtime speed.
      - ``QUARTER``
        Quarter -- Track with quarter of realtime speed.

      :type: Literal['FASTEST', 'DOUBLE', 'REALTIME', 'HALF', 'QUARTER']

   .. attribute:: use_default_blue_channel

      Use blue channel from footage for tracking (default True)

      :type: bool

   .. attribute:: use_default_brute

      Use a brute-force translation-only initialization when tracking (default False)

      :type: bool

   .. attribute:: use_default_green_channel

      Use green channel from footage for tracking (default True)

      :type: bool

   .. attribute:: use_default_mask

      Use a Grease Pencil data-block as a mask to use only specified areas of pattern when tracking (default False)

      :type: bool

   .. attribute:: use_default_normalization

      Normalize light intensities while tracking (slower) (default False)

      :type: bool

   .. attribute:: use_default_red_channel

      Use red channel from footage for tracking (default True)

      :type: bool

   .. attribute:: use_keyframe_selection

      Automatically select keyframes when solving camera/object motion (default False)

      :type: bool

   .. attribute:: use_tripod_solver

      Use special solver to track a stable camera position, such as a tripod (default False)

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

   - :class:`MovieTracking.settings`

