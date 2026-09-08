XrSessionSettings(bpy_struct)
=============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: XrSessionSettings(bpy_struct)


   .. attribute:: base_pose_angle

      Rotation angle around the Z-Axis to apply the rotation deltas from the VR headset to (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: base_pose_location

      Coordinates to apply translation deltas from the VR headset to (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: base_pose_object

      Object to take the location and rotation to which translation and rotation deltas from the VR headset will be applied to

      :type: :class:`Object` | None

   .. attribute:: base_pose_type

      Define where the location and rotation for the VR view come from, to which translation and rotation deltas from the VR headset will be applied to (default ``'SCENE_CAMERA'``)

      - ``SCENE_CAMERA``
        Scene Camera -- Follow the active scene camera to define the VR view's base pose.
      - ``OBJECT``
        Object -- Follow the transformation of an object to define the VR view's base pose.
      - ``CUSTOM``
        Custom -- Follow a custom transformation to define the VR view's base pose.

      :type: Literal['SCENE_CAMERA', 'OBJECT', 'CUSTOM']

   .. attribute:: base_scale

      Uniform scale to apply to VR view (in [1e-06, inf], default 1.0)

      :type: float

   .. attribute:: clip_end

      VR viewport far clipping distance (in [1e-06, inf], default 0.0)

      :type: float

   .. attribute:: clip_start

      VR viewport near clipping distance (in [1e-06, inf], default 0.0)

      :type: float

   .. attribute:: controller_draw_style

      Style to use when drawing VR controllers (default ``'DARK'``)

      - ``DARK``
        Dark -- Draw dark controller.
      - ``LIGHT``
        Light -- Draw light controller.
      - ``DARK_RAY``
        Dark + Ray -- Draw dark controller with aiming axis ray.
      - ``LIGHT_RAY``
        Light + Ray -- Draw light controller with aiming axis ray.

      :type: Literal['DARK', 'LIGHT', 'DARK_RAY', 'LIGHT_RAY']

   .. attribute:: fly_speed

      Fly speed in meters per second (in [1e-06, inf], default 0.0)

      :type: float

   .. data:: icon_from_show_object_viewport

      (in [-inf, inf], default 0, readonly)

      :type: int

   .. data:: shading

      (readonly, never None)

      :type: :class:`View3DShading`

   .. attribute:: show_annotation

      Show annotations for this view (default False)

      :type: bool

   .. attribute:: show_controllers

      Show VR controllers (requires VR actions for controller poses) (default False)

      :type: bool

   .. attribute:: show_custom_overlays

      Show custom VR overlays (default False)

      :type: bool

   .. attribute:: show_floor

      Show the ground plane grid (default False)

      :type: bool

   .. attribute:: show_object_extras

      Show object extras, including empties, lights, and cameras (default False)

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

   .. attribute:: show_passthrough

      Show the passthrough view (default False)

      :type: bool

   .. attribute:: show_selection

      Show selection outlines (default False)

      :type: bool

   .. attribute:: use_absolute_tracking

      Allow the VR tracking origin to be defined independently of the headset location (default False)

      :type: bool

   .. attribute:: use_positional_tracking

      Allow VR headsets to affect the location in virtual space, in addition to the rotation (default False)

      :type: bool

   .. attribute:: view_scale

      Scaling factor applied on top of scene scale for adjustments to the VR view. When possible, prefer modifying the scene scale instead (in [1e-06, inf], default 1.0)

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

   - :class:`WindowManager.xr_session_settings`

