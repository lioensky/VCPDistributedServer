SpaceView3D(Space)
==================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Space`

.. class:: SpaceView3D(Space)

   3D View space data

   .. attribute:: camera

      Active camera used in this view (when unlocked from the scene's active camera)

      :type: :class:`Object` | None

   .. attribute:: clip_end

      3D View far clipping distance (in [1e-06, inf], default 1000.0)

      :type: float

   .. attribute:: clip_start

      3D View near clipping distance (perspective view only) (in [1e-06, inf], default 0.01)

      :type: float

   .. data:: icon_from_show_object_viewport

      (in [-inf, inf], default 0, readonly)

      :type: int

   .. attribute:: lens

      Viewport lens angle (in [1, 250], default 50.0)

      :type: float

   .. data:: local_view

      Display an isolated subset of objects, apart from the scene visibility (readonly)

      :type: :class:`SpaceView3D` | None

   .. attribute:: lock_bone

      3D View center is locked to this bone's position (default "", never None)

      :type: str

   .. attribute:: lock_camera

      Enable view navigation within the camera view (default False)

      :type: bool

   .. attribute:: lock_cursor

      3D View center is locked to the cursor's position (default False)

      :type: bool

   .. attribute:: lock_object

      3D View center is locked to this object's position

      :type: :class:`Object` | None

   .. attribute:: mirror_xr_session

      Synchronize the viewer perspective of virtual reality sessions with this 3D viewport (default False)

      :type: bool

   .. data:: overlay

      Settings for display of overlays in the 3D viewport (readonly, never None)

      :type: :class:`View3DOverlay`

   .. data:: region_3d

      3D region for this space. When the space is in quad view, the camera region (readonly)

      :type: :class:`RegionView3D` | None

   .. data:: region_quadviews

      3D regions (the third one defines quad view settings, the fourth one is same as 'region_3d') (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`RegionView3D`]

   .. attribute:: render_border_max_x

      Maximum X value for the render region (in [0, 1], default 0.0)

      :type: float

   .. attribute:: render_border_max_y

      Maximum Y value for the render region (in [0, 1], default 0.0)

      :type: float

   .. attribute:: render_border_min_x

      Minimum X value for the render region (in [0, 1], default 0.0)

      :type: float

   .. attribute:: render_border_min_y

      Minimum Y value for the render region (in [0, 1], default 0.0)

      :type: float

   .. data:: shading

      Settings for shading in the 3D viewport (readonly, never None)

      :type: :class:`View3DShading`

   .. attribute:: show_bundle_names

      Show names for reconstructed tracks objects (default False)

      :type: bool

   .. attribute:: show_camera_path

      Show reconstructed camera path (default False)

      :type: bool

   .. attribute:: show_gizmo

      Show gizmos of all types (default True)

      :type: bool

   .. attribute:: show_gizmo_camera_dof_distance

      Gizmo to adjust camera focus distance (depends on limits display) (default False)

      :type: bool

   .. attribute:: show_gizmo_camera_lens

      Gizmo to adjust camera focal length or orthographic scale (default False)

      :type: bool

   .. attribute:: show_gizmo_context

      Context sensitive gizmos for the active item (default True)

      :type: bool

   .. attribute:: show_gizmo_empty_force_field

      Gizmo to adjust the force field (default False)

      :type: bool

   .. attribute:: show_gizmo_empty_image

      Gizmo to adjust image size and position (default False)

      :type: bool

   .. attribute:: show_gizmo_light_look_at

      Gizmo to adjust the direction of the light (default False)

      :type: bool

   .. attribute:: show_gizmo_light_size

      Gizmo to adjust spot and area size (default False)

      :type: bool

   .. attribute:: show_gizmo_modifier

      Gizmos for the active modifier (default True)

      :type: bool

   .. attribute:: show_gizmo_navigate

      Viewport navigation gizmo (default True)

      :type: bool

   .. attribute:: show_gizmo_object_rotate

      Gizmo to adjust rotation (default False)

      :type: bool

   .. attribute:: show_gizmo_object_scale

      Gizmo to adjust scale (default False)

      :type: bool

   .. attribute:: show_gizmo_object_translate

      Gizmo to adjust location (default False)

      :type: bool

   .. attribute:: show_gizmo_tool

      Active tool gizmo (default True)

      :type: bool

   .. attribute:: show_object_select_armature

      Allow selection of armatures (default True)

      :type: bool

   .. attribute:: show_object_select_camera

      Allow selection of cameras (default True)

      :type: bool

   .. attribute:: show_object_select_curve

      Allow selection of curves (default True)

      :type: bool

   .. attribute:: show_object_select_curves

      Allow selection of hair curves (default True)

      :type: bool

   .. attribute:: show_object_select_empty

      Allow selection of empties (default True)

      :type: bool

   .. attribute:: show_object_select_font

      Allow selection of text objects (default True)

      :type: bool

   .. attribute:: show_object_select_grease_pencil

      Allow selection of Grease Pencil objects (default True)

      :type: bool

   .. attribute:: show_object_select_lattice

      Allow selection of lattices (default True)

      :type: bool

   .. attribute:: show_object_select_light

      Allow selection of lights (default True)

      :type: bool

   .. attribute:: show_object_select_light_probe

      Allow selection of light probes (default True)

      :type: bool

   .. attribute:: show_object_select_mesh

      Allow selection of mesh objects (default True)

      :type: bool

   .. attribute:: show_object_select_meta

      Allow selection of metaballs (default True)

      :type: bool

   .. attribute:: show_object_select_pointcloud

      Allow selection of point clouds (default True)

      :type: bool

   .. attribute:: show_object_select_speaker

      Allow selection of speakers (default True)

      :type: bool

   .. attribute:: show_object_select_surf

      Allow selection of surfaces (default True)

      :type: bool

   .. attribute:: show_object_select_volume

      Allow selection of volumes (default True)

      :type: bool

   .. attribute:: show_object_viewport_armature

      Show armatures (default True)

      :type: bool

   .. attribute:: show_object_viewport_camera

      Show cameras (default True)

      :type: bool

   .. attribute:: show_object_viewport_curve

      Show curves (default True)

      :type: bool

   .. attribute:: show_object_viewport_curves

      Show hair curves (default True)

      :type: bool

   .. attribute:: show_object_viewport_empty

      Show empties (default True)

      :type: bool

   .. attribute:: show_object_viewport_font

      Show text objects (default True)

      :type: bool

   .. attribute:: show_object_viewport_grease_pencil

      Show Grease Pencil objects (default True)

      :type: bool

   .. attribute:: show_object_viewport_lattice

      Show lattices (default True)

      :type: bool

   .. attribute:: show_object_viewport_light

      Show lights (default True)

      :type: bool

   .. attribute:: show_object_viewport_light_probe

      Show light probes (default True)

      :type: bool

   .. attribute:: show_object_viewport_mesh

      Show mesh objects (default True)

      :type: bool

   .. attribute:: show_object_viewport_meta

      Show metaballs (default True)

      :type: bool

   .. attribute:: show_object_viewport_pointcloud

      Show point clouds (default True)

      :type: bool

   .. attribute:: show_object_viewport_speaker

      Show speakers (default True)

      :type: bool

   .. attribute:: show_object_viewport_surf

      Show surfaces (default True)

      :type: bool

   .. attribute:: show_object_viewport_volume

      Show volumes (default True)

      :type: bool

   .. attribute:: show_reconstruction

      Display reconstruction data from active movie clip (default True)

      :type: bool

   .. attribute:: show_region_asset_shelf

      Display a region with assets that may currently be relevant (such as brushes in paint modes, or poses in Pose Mode) (default False)

      :type: bool

   .. attribute:: show_region_hud

      (default False)

      :type: bool

   .. attribute:: show_region_tool_header

      (default False)

      :type: bool

   .. attribute:: show_region_toolbar

      (default False)

      :type: bool

   .. attribute:: show_region_ui

      (default False)

      :type: bool

   .. attribute:: show_stereo_3d_cameras

      Show the left and right cameras (default False)

      :type: bool

   .. attribute:: show_stereo_3d_convergence_plane

      Show the stereo 3D convergence plane (default True)

      :type: bool

   .. attribute:: show_stereo_3d_volume

      Show the stereo 3D frustum volume (default False)

      :type: bool

   .. attribute:: show_viewer

      Display non-final geometry from viewer nodes (default True)

      :type: bool

   .. attribute:: stereo_3d_camera

      (default ``'S3D'``)

      :type: Literal['LEFT', 'RIGHT', 'S3D']

   .. attribute:: stereo_3d_convergence_plane_alpha

      Opacity (alpha) of the convergence plane (in [0, 1], default 0.15)

      :type: float

   .. data:: stereo_3d_eye

      Current stereo eye being displayed (default ``'LEFT_EYE'``, readonly)

      :type: Literal['LEFT_EYE', 'RIGHT_EYE']

   .. attribute:: stereo_3d_volume_alpha

      Opacity (alpha) of the cameras' frustum volume (in [0, 1], default 0.05)

      :type: float

   .. attribute:: tracks_display_size

      Display size of tracks from reconstructed data (in [0, inf], default 0.2)

      :type: float

   .. attribute:: tracks_display_type

      Viewport display style for tracks (default ``'PLAIN_AXES'``)

      :type: Literal['PLAIN_AXES', 'ARROWS', 'SINGLE_ARROW', 'CIRCLE', 'CUBE', 'SPHERE', 'CONE']

   .. attribute:: use_local_camera

      Use a local camera in this view, rather than scene's active camera (default False)

      :type: bool

   .. attribute:: use_local_collections

      Display a different set of collections in this viewport (default False)

      :type: bool

   .. attribute:: use_render_border

      Use a region within the frame size for rendered viewport (when not viewing through the camera) (default False)

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


   .. classmethod:: draw_handler_add(callback, args, region_type, draw_type)
   
      Add a new draw handler to this space type.
      It will be called every time the specified region in the space type will be drawn.
      Note: All arguments are positional only for now.
   
      :param callback:
         A function that will be called when the region is drawn.
         It gets the specified arguments as input, it's return value is ignored.
      :type callback: Callable[..., Any]
      :param args: Arguments that will be passed to the callback.
      :type args: tuple[Any, ...]
      :param region_type: The region type the callback draws in; usually ``WINDOW``. (:class:`bpy.types.Region.type`)
      :type region_type: str
      :param draw_type: Usually ``POST_PIXEL`` for 2D drawing and ``POST_VIEW`` for 3D drawing. In some cases ``PRE_VIEW`` can be used. ``BACKDROP`` can be used for backdrops in the node editor.
      :type draw_type: str
      :return: Handler that can be removed later on.
      :rtype: object


   .. classmethod:: draw_handler_remove(handler, region_type)
   
      Remove a draw handler that was added previously.
   
      :param handler: The draw handler that should be removed.
      :type handler: object
      :param region_type: Region type the callback was added to.
      :type region_type: str


Inherited Properties
--------------------

.. hlist::
   :columns: 2

   - :class:`bpy_struct.id_data`
   - :class:`Space.type`
   - :class:`Space.show_locked_time`
   - :class:`Space.show_region_header`

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
   - :class:`Space.bl_rna_get_subclass`
   - :class:`Space.bl_rna_get_subclass_py`
   - :class:`Space.draw_handler_add`
   - :class:`Space.draw_handler_remove`

References
----------

.. hlist::
   :columns: 2

   - :class:`Object.local_view_get`
   - :class:`Object.local_view_set`
   - :class:`Object.visible_get`
   - :class:`Object.visible_in_viewport_get`
   - :class:`SpaceView3D.local_view`

