ToolSettings(bpy_struct)
========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ToolSettings(bpy_struct)


   .. attribute:: anim_fix_to_cam_use_loc

      Create location keys when fixing to the scene camera (default True)

      :type: bool

   .. attribute:: anim_fix_to_cam_use_rot

      Create rotation keys when fixing to the scene camera (default True)

      :type: bool

   .. attribute:: anim_fix_to_cam_use_scale

      Create scale keys when fixing to the scene camera (default True)

      :type: bool

   .. attribute:: anim_mirror_bone

      Bone to use for the mirroring (default "", never None)

      :type: str

   .. attribute:: anim_mirror_object

      Object to mirror over. Leave empty and name a bone to always mirror over that bone of the active armature

      :type: :class:`Object` | None

   .. attribute:: anim_relative_object

      Object to which matrices are made relative

      :type: :class:`Object` | None

   .. attribute:: annotation_stroke_placement_view2d

      (default ``'IMAGE'``)

      - ``IMAGE``
        Image -- Stick stroke to the image.
      - ``VIEW``
        View -- Stick stroke to the view.

      :type: Literal['IMAGE', 'VIEW']

   .. attribute:: annotation_stroke_placement_view3d

      How annotation strokes are orientated in 3D space (default ``'CURSOR'``)

      - ``CURSOR``
        3D Cursor -- Draw stroke at 3D cursor location.
      - ``VIEW``
        View -- Stick stroke to the view.
      - ``SURFACE``
        Surface -- Stick stroke to surfaces.

      :type: Literal['CURSOR', 'VIEW', 'SURFACE']

   .. attribute:: annotation_thickness

      Thickness of annotation strokes (in [1, 10], default 3)

      :type: int

   .. attribute:: auto_keying_mode

      Mode of automatic keyframe insertion for objects, bones and masks (default ``'ADD_REPLACE_KEYS'``)

      :type: Literal['ADD_REPLACE_KEYS', 'REPLACE_KEYS']

   .. data:: curve_paint_settings

      (readonly, never None)

      :type: :class:`CurvePaintSettings`

   .. data:: curves_sculpt

      (readonly)

      :type: :class:`CurvesSculpt` | None

   .. data:: custom_bevel_profile_preset

      Used for defining a profile's path (readonly)

      :type: :class:`CurveProfile` | None

   .. attribute:: double_threshold

      Threshold distance for Auto Merge (in [0, 1], default 0.001)

      :type: float

   .. data:: gpencil_interpolate

      Settings for Grease Pencil interpolation tools (readonly)

      :type: :class:`GPencilInterpolateSettings` | None

   .. data:: gpencil_paint

      (readonly)

      :type: :class:`GpPaint` | None

   .. data:: gpencil_sculpt

      Settings for stroke sculpting tools and brushes (readonly)

      :type: :class:`GPencilSculptSettings` | None

   .. data:: gpencil_sculpt_paint

      (readonly)

      :type: :class:`GpSculptPaint` | None

   .. attribute:: gpencil_selectmode_edit

      (default ``'POINT'``)

      :type: Literal[:ref:`rna_enum_grease_pencil_selectmode_items`]

   .. attribute:: gpencil_stroke_placement_view3d

      (default ``'ORIGIN'``)

      - ``ORIGIN``
        Origin -- Draw stroke at Object origin.
      - ``CURSOR``
        3D Cursor -- Draw stroke at 3D cursor location.
      - ``SURFACE``
        Surface -- Stick stroke to surfaces.
      - ``STROKE``
        Stroke -- Stick stroke to other strokes.

      :type: Literal['ORIGIN', 'CURSOR', 'SURFACE', 'STROKE']

   .. attribute:: gpencil_stroke_snap_mode

      (default ``'NONE'``)

      - ``NONE``
        All Points -- Snap to all points.
      - ``ENDS``
        End Points -- Snap to first and last points and interpolate.
      - ``FIRST``
        First Point -- Snap to first point.

      :type: Literal['NONE', 'ENDS', 'FIRST']

   .. attribute:: gpencil_surface_offset

      Offset along the normal when drawing on surfaces (in [-inf, inf], default 0.15)

      :type: float

   .. data:: gpencil_vertex_paint

      (readonly)

      :type: :class:`GpVertexPaint` | None

   .. data:: gpencil_weight_paint

      (readonly)

      :type: :class:`GpWeightPaint` | None

   .. data:: image_paint

      (readonly)

      :type: :class:`ImagePaint` | None

   .. attribute:: keyframe_type

      Type of keyframes to create when inserting keyframes (default ``'KEYFRAME'``)

      :type: Literal[:ref:`rna_enum_beztriple_keyframe_type_items`]

   .. attribute:: lock_markers

      Prevent marker editing (default False)

      :type: bool

   .. attribute:: lock_object_mode

      Restrict selection to objects using the same mode as the active object, to prevent accidental mode switch when selecting (default True)

      :type: bool

   .. attribute:: mesh_select_mode

      Which mesh elements selection works on (array of 3 items, default (False, False, False))

      :type: :class:`bpy_prop_array`\ [bool]

   .. attribute:: normal_vector

      Normal vector used to copy, add or multiply (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. data:: paint_mode

      (readonly)

      :type: :class:`PaintModeSettings` | None

   .. data:: particle_edit

      (readonly)

      :type: :class:`ParticleEdit` | None

   .. attribute:: plane_axis

      The axis used for placing the base region (default ``'Z'``)

      :type: Literal[:ref:`rna_enum_axis_xyz_items`]

   .. attribute:: plane_axis_auto

      Select the closest axis when placing objects (surface overrides) (default True)

      :type: bool

   .. attribute:: plane_depth

      The initial depth used when placing the cursor (default ``'SURFACE'``)

      - ``SURFACE``
        Surface -- Start placing on the surface, using the 3D cursor position as a fallback.
      - ``CURSOR_PLANE``
        Cursor Plane -- Start placement using a point projected onto the orientation axis at the 3D cursor position.
      - ``CURSOR_VIEW``
        Cursor View -- Start placement using a point projected onto the view plane at the 3D cursor position.

      :type: Literal['SURFACE', 'CURSOR_PLANE', 'CURSOR_VIEW']

   .. attribute:: plane_orientation

      The initial depth used when placing the cursor (default ``'SURFACE'``)

      - ``SURFACE``
        Surface -- Use the surface normal (using the transform orientation as a fallback).
      - ``DEFAULT``
        Default -- Use the current transform orientation.

      :type: Literal['SURFACE', 'DEFAULT']

   .. attribute:: playhead_snap_distance

      Maximum distance for snapping in pixels (in [-inf, inf], default 20)

      :type: int

   .. attribute:: proportional_distance

      Display size for proportional editing circle (in [1e-05, 5000], default 1.0)

      :type: float

   .. attribute:: proportional_edit_falloff

      Falloff type for proportional editing mode (default ``'SMOOTH'``)

      :type: Literal[:ref:`rna_enum_proportional_falloff_items`]

   .. attribute:: proportional_size

      Display size for proportional editing circle (in [1e-05, 5000], default 1.0)

      :type: float

   .. data:: sculpt

      (readonly)

      :type: :class:`Sculpt` | None

   .. data:: sequencer_tool_settings

      (readonly, never None)

      :type: :class:`SequencerToolSettings`

   .. attribute:: show_uv_local_view

      Display only faces with the currently displayed image assigned (default False)

      :type: bool

   .. attribute:: snap_angle_increment_2d

      Angle used for rotation increments in 2D editors (in [0, 3.14159], default 0.0872665)

      :type: float

   .. attribute:: snap_angle_increment_2d_precision

      Precision angle used for rotation increments in 2D editors (in [0, 3.14159], default 0.0174533)

      :type: float

   .. attribute:: snap_angle_increment_3d

      Angle used for rotation increments in 3D editors (in [0, 3.14159], default 0.0872665)

      :type: float

   .. attribute:: snap_angle_increment_3d_precision

      Precision angle used for rotation increments in 3D editors (in [0, 3.14159], default 0.0174533)

      :type: float

   .. attribute:: snap_anim_element

      Type of element to snap to (default ``'FRAME'``)

      :type: Literal[:ref:`rna_enum_snap_animation_element_items`]

   .. attribute:: snap_elements

      Type of element to snap to (default {``'INCREMENT'``})

      :type: set[Literal[:ref:`rna_enum_snap_element_items`]]

   .. attribute:: snap_elements_base

      Type of element for the "Snap Base" to snap to (default {``'INCREMENT'``})

      - ``INCREMENT``
        Increment -- Snap to increments.
      - ``GRID``
        Grid -- Snap to grid.
      - ``VERTEX``
        Vertex -- Snap to vertices.
      - ``EDGE``
        Edge -- Snap to edges.
      - ``FACE``
        Face -- Snap by projecting onto faces.
      - ``VOLUME``
        Volume -- Snap to volume.
      - ``EDGE_MIDPOINT``
        Edge Center -- Snap to the middle of edges.
      - ``EDGE_PERPENDICULAR``
        Edge Perpendicular -- Snap to the nearest point on an edge.
      - ``FACE_MIDPOINT``
        Face Center -- Snap to the middle of faces.

      :type: set[Literal['INCREMENT', 'GRID', 'VERTEX', 'EDGE', 'FACE', 'VOLUME', 'EDGE_MIDPOINT', 'EDGE_PERPENDICULAR', 'FACE_MIDPOINT']]

   .. attribute:: snap_elements_individual

      Type of element for individual transformed elements to snap to (default set())

      - ``FACE_PROJECT``
        Face Project -- Snap by projecting onto faces.
      - ``FACE_NEAREST``
        Face Nearest -- Snap to nearest point on faces.

      :type: set[Literal['FACE_PROJECT', 'FACE_NEAREST']]

   .. attribute:: snap_elements_tool

      The target to use while snapping (default ``'GEOMETRY'``)

      - ``GEOMETRY``
        Geometry -- Snap to all geometry.
      - ``DEFAULT``
        Default -- Use the current snap settings.

      :type: Literal['GEOMETRY', 'DEFAULT']

   .. attribute:: snap_face_nearest_steps

      Number of steps to break transformation into for face nearest snapping (in [1, 100], default 1)

      :type: int

   .. attribute:: snap_playhead_element

      Type of element to snap to (default {``'KEY'``, ``'Strip'``})

      - ``FRAME``
        Frames -- Snap to frame increments.
      - ``SECOND``
        Seconds -- Snap to second increments.
      - ``MARKER``
        Markers -- Snap to markers.
      - ``KEY``
        Keyframes -- Snap to keyframes.
      - ``Strip``
        Strips -- Snap to Strips.

      :type: set[Literal['FRAME', 'SECOND', 'MARKER', 'KEY', 'Strip']]

   .. attribute:: snap_playhead_frame_step

      At which interval to snap to frames (in [1, 32768], default 2)

      :type: int

   .. attribute:: snap_playhead_second_step

      At which interval to snap to seconds (in [1, 32768], default 1)

      :type: int

   .. attribute:: snap_target

      Which part to snap onto the target (default ``'CLOSEST'``)

      :type: Literal[:ref:`rna_enum_snap_source_items`]

   .. attribute:: snap_uv_element

      Type of element to snap to (default {``'INCREMENT'``})

      - ``INCREMENT``
        Increment -- Snap to increments of grid.
      - ``GRID``
        Grid -- Snap to grid.
      - ``VERTEX``
        Vertex -- Snap to vertices.

      :type: set[Literal['INCREMENT', 'GRID', 'VERTEX']]

   .. data:: statvis

      (readonly, never None)

      :type: :class:`MeshStatVis`

   .. attribute:: transform_pivot_point

      Pivot center for rotation/scaling (default ``'MEDIAN_POINT'``)

      - ``BOUNDING_BOX_CENTER``
        Bounding Box Center -- Pivot around bounding box center of selected object(s).
      - ``CURSOR``
        3D Cursor -- Pivot around the 3D cursor.
      - ``INDIVIDUAL_ORIGINS``
        Individual Origins -- Pivot around each object's own origin.
      - ``MEDIAN_POINT``
        Median Point -- Pivot around the median point of selected objects.
      - ``ACTIVE_ELEMENT``
        Active Element -- Pivot around active object.

      :type: Literal['BOUNDING_BOX_CENTER', 'CURSOR', 'INDIVIDUAL_ORIGINS', 'MEDIAN_POINT', 'ACTIVE_ELEMENT']

   .. attribute:: use_annotation_project_only_selected

      Project the strokes only onto selected objects (default False)

      :type: bool

   .. attribute:: use_annotation_stroke_endpoints

      Only use the first and last parts of the stroke for snapping (default False)

      :type: bool

   .. attribute:: use_auto_normalize

      Ensure all bone-deforming vertex groups add up to 1.0 while weight painting or assigning to vertices (default False)

      :type: bool

   .. attribute:: use_edge_path_live_unwrap

      Changing edge seams recalculates UV unwrap (default False)

      :type: bool

   .. attribute:: use_gpencil_automerge_strokes

      Join the last drawn stroke with previous strokes in the active layer by distance (default False)

      :type: bool

   .. attribute:: use_gpencil_draw_additive

      When creating new frames, the strokes from the previous/active frame are included as the basis for the new one (default False)

      :type: bool

   .. attribute:: use_gpencil_draw_onback

      New strokes are drawn below of all strokes in the layer (default False)

      :type: bool

   .. attribute:: use_gpencil_project_only_selected

      Project the strokes only onto selected objects (default False)

      :type: bool

   .. attribute:: use_gpencil_select_mask_point

      Only sculpt selected stroke points (default False)

      :type: bool

   .. attribute:: use_gpencil_select_mask_segment

      Only sculpt selected stroke points between other strokes (default False)

      :type: bool

   .. attribute:: use_gpencil_select_mask_stroke

      Only sculpt selected strokes (default False)

      :type: bool

   .. attribute:: use_gpencil_thumbnail_list

      Show compact list of colors instead of thumbnails (default True)

      :type: bool

   .. attribute:: use_gpencil_vertex_select_mask_point

      Only paint selected stroke points (default False)

      :type: bool

   .. attribute:: use_gpencil_vertex_select_mask_segment

      Only paint selected stroke points between other strokes (default False)

      :type: bool

   .. attribute:: use_gpencil_vertex_select_mask_stroke

      Only paint selected strokes (default False)

      :type: bool

   .. attribute:: use_gpencil_weight_data_add

      Weight data for new strokes is added according to the current vertex group and weight. If no vertex group selected, weight is not added. (default False)

      :type: bool

   .. attribute:: use_grease_pencil_multi_frame_editing

      Enable multi-frame editing (default False)

      :type: bool

   .. attribute:: use_keyframe_cycle_aware

      For channels with cyclic extrapolation, keyframe insertion is automatically remapped inside the cycle time range, and keeps ends in sync. Curves newly added to actions with a Manual Frame Range and Cyclic Animation are automatically made cyclic. (default False)

      :type: bool

   .. attribute:: use_keyframe_insert_auto

      Automatic keyframe insertion for objects, bones and masks (default True)

      :type: bool

   .. attribute:: use_keyframe_insert_keyingset

      Automatic keyframe insertion using active Keying Set only (default False)

      :type: bool

   .. attribute:: use_lock_relative

      Display bone-deforming groups as if all locked deform groups were deleted, and the remaining ones were re-normalized (default False)

      :type: bool

   .. attribute:: use_mesh_automerge

      Automatically merge vertices moved to the same location (default False)

      :type: bool

   .. attribute:: use_mesh_automerge_and_split

      Automatically split edges and faces (default False)

      :type: bool

   .. attribute:: use_multipaint

      Paint across the weights of all selected bones, maintaining their relative influence (default False)

      :type: bool

   .. attribute:: use_proportional_action

      Proportional editing in action editor (default False)

      :type: bool

   .. attribute:: use_proportional_connected

      Proportional Editing using connected geometry only (default False)

      :type: bool

   .. attribute:: use_proportional_edit

      Proportional edit mode (default False)

      :type: bool

   .. attribute:: use_proportional_edit_mask

      Proportional editing mask mode (default False)

      :type: bool

   .. attribute:: use_proportional_edit_objects

      Proportional editing object mode (default False)

      :type: bool

   .. attribute:: use_proportional_fcurve

      Proportional editing in F-Curve editor (default False)

      :type: bool

   .. attribute:: use_proportional_projected

      Proportional Editing using screen space locations (default False)

      :type: bool

   .. attribute:: use_record_with_nla

      Add a new NLA Track + Strip for every loop/pass made over the animation to allow non-destructive tweaking (default False)

      :type: bool

   .. attribute:: use_snap

      Snap during transform (default False)

      :type: bool

   .. attribute:: use_snap_align_rotation

      Align rotation with the snapping target (default False)

      :type: bool

   .. attribute:: use_snap_anim

      Enable snapping when transforming keyframes (default True)

      :type: bool

   .. attribute:: use_snap_backface_culling

      Exclude back facing geometry from snapping (default False)

      :type: bool

   .. attribute:: use_snap_driver

      Enable snapping when transforming keys in the Driver Editor (default False)

      :type: bool

   .. attribute:: use_snap_driver_absolute

      Snap to full values (default False)

      :type: bool

   .. attribute:: use_snap_edit

      Snap onto non-active objects in edit mode (edit mode only) (default True)

      :type: bool

   .. attribute:: use_snap_grid_absolute

      Absolute grid alignment while translating (based on the pivot center) (default False)

      :type: bool

   .. attribute:: use_snap_node

      Snap Node during transform (default False)

      :type: bool

   .. attribute:: use_snap_nonedit

      Snap onto objects not in edit mode (edit mode only) (default True)

      :type: bool

   .. attribute:: use_snap_peel_object

      Consider objects as whole when finding volume center (default False)

      :type: bool

   .. attribute:: use_snap_playhead

      Snap playhead when scrubbing (default False)

      :type: bool

   .. attribute:: use_snap_rotate

      Rotate is affected by the snapping settings (default False)

      :type: bool

   .. attribute:: use_snap_scale

      Scale is affected by snapping settings (default False)

      :type: bool

   .. attribute:: use_snap_selectable

      Snap only onto objects that are selectable (default False)

      :type: bool

   .. attribute:: use_snap_self

      Snap onto itself only if enabled (edit mode only) (default True)

      :type: bool

   .. attribute:: use_snap_sequencer

      Snap strips during transform (default True)

      :type: bool

   .. attribute:: use_snap_time_absolute

      Absolute time alignment when transforming keyframes (default False)

      :type: bool

   .. attribute:: use_snap_to_same_target

      Snap only to target that source was initially near ("Face Nearest" only) (default False)

      :type: bool

   .. attribute:: use_snap_translate

      Move is affected by snapping settings (default True)

      :type: bool

   .. attribute:: use_snap_uv

      Snap UV during transform (default False)

      :type: bool

   .. attribute:: use_transform_correct_face_attributes

      Correct data such as UVs and color attributes when transforming (default False)

      :type: bool

   .. attribute:: use_transform_correct_keep_connected

      During the Face Attributes correction, merge attributes connected to the same vertex (default False)

      :type: bool

   .. attribute:: use_transform_data_origin

      Transform object origins, while leaving the shape in place (default False)

      :type: bool

   .. attribute:: use_transform_pivot_point_align

      Only transform object locations, without affecting rotation or scaling (default False)

      :type: bool

   .. attribute:: use_transform_skip_children

      Transform the parents, leaving the children in place (default False)

      :type: bool

   .. attribute:: use_uv_custom_region

      Custom defined region (default False)

      :type: bool

   .. attribute:: use_uv_select_island

      Island selection (default False)

      :type: bool

   .. attribute:: use_uv_select_sync

      Keep UV and edit mode mesh selection in sync (default True)

      :type: bool

   .. data:: uv_sculpt

      (readonly)

      :type: :class:`UvSculpt` | None

   .. attribute:: uv_sculpt_all_islands

      Brush operates on all islands (default False)

      :type: bool

   .. attribute:: uv_sculpt_lock_borders

      Disable editing of boundary edges (default False)

      :type: bool

   .. attribute:: uv_select_mode

      UV selection and display mode (default ``'VERTEX'``)

      :type: Literal[:ref:`rna_enum_mesh_select_mode_uv_items`]

   .. attribute:: uv_sticky_select_mode

      Method for extending UV vertex selection (default ``'SHARED_LOCATION'``)

      - ``DISABLED``
        Disabled -- Sticky vertex selection disabled.
      - ``SHARED_LOCATION``
        Shared Location -- Select UVs that are at the same location and share a mesh vertex.
      - ``SHARED_VERTEX``
        Shared Vertex -- Select UVs that share a mesh vertex, whether or not they are at the same location.

      :type: Literal['DISABLED', 'SHARED_LOCATION', 'SHARED_VERTEX']

   .. attribute:: vertex_group_subset

      Filter Vertex groups for Display (default ``'ALL'``)

      - ``ALL``
        All -- All Vertex Groups.
      - ``BONE_DEFORM``
        Deform -- Vertex Groups assigned to Deform Bones.
      - ``OTHER_DEFORM``
        Other -- Vertex Groups assigned to non Deform Bones.

      :type: Literal['ALL', 'BONE_DEFORM', 'OTHER_DEFORM']

   .. attribute:: vertex_group_user

      Display unweighted vertices (default ``'ACTIVE'``)

      - ``NONE``
        None.
      - ``ACTIVE``
        Active -- Show vertices with no weights in the active group.
      - ``ALL``
        All -- Show vertices with no weights in any group.

      :type: Literal['NONE', 'ACTIVE', 'ALL']

   .. attribute:: vertex_group_weight

      Weight to assign in vertex groups (in [0, 1], default 1.0)

      :type: float

   .. data:: vertex_paint

      (readonly)

      :type: :class:`VertexPaint` | None

   .. data:: weight_paint

      (readonly)

      :type: :class:`VertexPaint` | None

   .. attribute:: workspace_tool_type

      Action when dragging in the viewport (default ``'FALLBACK'``)

      :type: Literal['DEFAULT', 'FALLBACK']

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

   - :mod:`bpy.context.tool_settings`
   - :class:`Context.tool_settings`
   - :class:`Scene.tool_settings`

