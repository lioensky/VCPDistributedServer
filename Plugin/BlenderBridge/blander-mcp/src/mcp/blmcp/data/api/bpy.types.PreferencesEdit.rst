PreferencesEdit(bpy_struct)
===========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: PreferencesEdit(bpy_struct)

   Settings for interacting with Blender data

   .. attribute:: auto_keying_mode

      Mode of automatic keyframe insertion for Objects and Bones (default setting used for new Scenes) (default ``'ADD_REPLACE_KEYS'``)

      :type: Literal['ADD_REPLACE_KEYS', 'REPLACE_KEYS']

   .. attribute:: collection_instance_empty_size

      Display size of the empty when new collection instances are created (in [0.001, inf], default 1.0)

      :type: float

   .. attribute:: connect_strips_by_default

      Connect newly added movie strips by default if they have multiple channels (default True)

      :type: bool

   .. attribute:: fcurve_new_auto_smoothing

      Auto Handle Smoothing mode used for newly added F-Curves (default ``'CONT_ACCEL'``)

      :type: Literal[:ref:`rna_enum_fcurve_auto_smoothing_items`]

   .. attribute:: fcurve_unselected_alpha

      The opacity of unselected F-Curves against the background of the Graph Editor (in [0.001, 1], default 0.25)

      :type: float

   .. attribute:: grease_pencil_default_color

      Color of new annotation layers (array of 4 items, in [0, inf], default (0.38, 0.61, 0.78, 0.9))

      :type: :class:`bpy_prop_array`\ [float]

   .. attribute:: grease_pencil_eraser_radius

      Radius of eraser 'brush' (in [1, 500], default 25)

      :type: int

   .. attribute:: grease_pencil_euclidean_distance

      Distance moved by mouse when drawing stroke to include (in [0, 100], default 2)

      :type: int

   .. attribute:: grease_pencil_manhattan_distance

      Pixels moved by mouse per axis when drawing stroke (in [0, 100], default 1)

      :type: int

   .. attribute:: key_insert_channels

      Which channels to insert keys at when no keying set is active (default {``'CUSTOM_PROPS'``, ``'LOCATION'``, ``'ROTATION'``, ``'SCALE'``})

      :type: set[Literal['LOCATION', 'ROTATION', 'SCALE', 'ROTATE_MODE', 'CUSTOM_PROPS']]

   .. attribute:: keyframe_new_handle_type

      Handle type for handles of new keyframes (default ``'AUTO_CLAMPED'``)

      :type: Literal[:ref:`rna_enum_keyframe_handle_type_items`]

   .. attribute:: keyframe_new_interpolation_type

      Interpolation mode used for first keyframe on newly added F-Curves (subsequent keyframes take interpolation from preceding keyframe) (default ``'BEZIER'``)

      :type: Literal[:ref:`rna_enum_beztriple_interpolation_mode_items`]

   .. attribute:: material_link

      Toggle whether the material is linked to object data or the object block (default ``'OBDATA'``)

      - ``OBDATA``
        Object Data -- Toggle whether the material is linked to object data or the object block.
      - ``OBJECT``
        Object -- Toggle whether the material is linked to object data or the object block.

      :type: Literal['OBDATA', 'OBJECT']

   .. attribute:: node_margin

      Minimum distance between nodes for Auto-offsetting nodes (in [0, 255], default 40)

      :type: int

   .. attribute:: node_preview_resolution

      Resolution used for Shader node previews (should be changed for performance convenience) (in [50, 250], default 120)

      :type: int

   .. attribute:: node_use_insert_offset

      Automatically offset the following or previous nodes in a chain when inserting a new node (default True)

      :type: bool

   .. attribute:: object_align

      The default alignment for objects added from a 3D viewport menu (default ``'WORLD'``)

      - ``WORLD``
        World -- Align newly added objects to the world coordinate system.
      - ``VIEW``
        View -- Align newly added objects to the active 3D view orientation.
      - ``CURSOR``
        3D Cursor -- Align newly added objects to the 3D Cursor's rotation.

      :type: Literal['WORLD', 'VIEW', 'CURSOR']

   .. attribute:: sculpt_paint_overlay_color

      Color of texture overlay (array of 3 items, in [0, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. attribute:: show_only_selected_curve_keyframes

      Only keyframes of selected F-Curves are visible and editable (default False)

      :type: bool

   .. attribute:: undo_memory_limit

      Maximum memory usage in megabytes (0 means unlimited) (in [0, inf], default 0)

      :type: int

   .. attribute:: undo_steps

      Number of undo steps available (smaller values conserve memory) (in [0, 256], default 32)

      :type: int

   .. attribute:: use_anim_channel_group_colors

      Use animation channel group colors; generally this is used to show bone group colors (default False)

      :type: bool

   .. attribute:: use_auto_keyframe_insert_needed

      Auto-Keying will skip inserting keys that don't affect the animation (default True)

      :type: bool

   .. attribute:: use_auto_keying

      Automatic keyframe insertion for Objects and Bones (default setting used for new Scenes) (default False)

      :type: bool

   .. attribute:: use_auto_keying_warning

      Show warning indicators when transforming objects and bones if auto keying is enabled (default True)

      :type: bool

   .. attribute:: use_cursor_lock_adjust

      Place the cursor without 'jumping' to the new location (when lock-to-cursor is used) (default True)

      :type: bool

   .. attribute:: use_duplicate_action

      Causes actions to be duplicated with the data-blocks (default True)

      :type: bool

   .. attribute:: use_duplicate_armature

      Causes armature data to be duplicated with the object (default True)

      :type: bool

   .. attribute:: use_duplicate_camera

      Causes camera data to be duplicated with the object (default True)

      :type: bool

   .. attribute:: use_duplicate_curve

      Causes curve data to be duplicated with the object (default True)

      :type: bool

   .. attribute:: use_duplicate_curves

      Causes curves data to be duplicated with the object (default True)

      :type: bool

   .. attribute:: use_duplicate_grease_pencil

      Causes Grease Pencil data to be duplicated with the object (default True)

      :type: bool

   .. attribute:: use_duplicate_lattice

      Causes lattice data to be duplicated with the object (default True)

      :type: bool

   .. attribute:: use_duplicate_light

      Causes light data to be duplicated with the object (default True)

      :type: bool

   .. attribute:: use_duplicate_lightprobe

      Causes light probe data to be duplicated with the object (default True)

      :type: bool

   .. attribute:: use_duplicate_material

      Causes material data to be duplicated with the object (default False)

      :type: bool

   .. attribute:: use_duplicate_mesh

      Causes mesh data to be duplicated with the object (default True)

      :type: bool

   .. attribute:: use_duplicate_metaball

      Causes metaball data to be duplicated with the object (default True)

      :type: bool

   .. attribute:: use_duplicate_node_tree

      Make copies of node groups when duplicating nodes in the node editor (default False)

      :type: bool

   .. attribute:: use_duplicate_particle

      Causes particle systems to be duplicated with the object (default False)

      :type: bool

   .. attribute:: use_duplicate_pointcloud

      Causes point cloud data to be duplicated with the object (default True)

      :type: bool

   .. attribute:: use_duplicate_speaker

      Causes speaker data to be duplicated with the object (default True)

      :type: bool

   .. attribute:: use_duplicate_surface

      Causes surface data to be duplicated with the object (default True)

      :type: bool

   .. attribute:: use_duplicate_text

      Causes text data to be duplicated with the object (default True)

      :type: bool

   .. attribute:: use_duplicate_volume

      Causes volume data to be duplicated with the object (default False)

      :type: bool

   .. attribute:: use_enter_edit_mode

      Enter edit mode automatically after adding a new object (default False)

      :type: bool

   .. attribute:: use_fcurve_high_quality_drawing

      Draw F-Curves using Anti-Aliasing (disable for better performance) (default True)

      :type: bool

   .. attribute:: use_global_undo

      Global undo works by keeping a full copy of the file itself in memory, so takes extra memory (default True)

      :type: bool

   .. attribute:: use_insertkey_xyz_to_rgb

      Color for newly added transformation F-Curves (Location, Rotation, Scale) and also Color is based on the transform axis (default True)

      :type: bool

   .. attribute:: use_keyframe_insert_available

      Insert Keyframes only for properties that are already animated (default False)

      :type: bool

   .. attribute:: use_keyframe_insert_needed

      When keying manually, skip inserting keys that don't affect the animation (default False)

      :type: bool

   .. attribute:: use_mouse_depth_cursor

      Use the surface depth for cursor placement (default True)

      :type: bool

   .. attribute:: use_negative_frames

      Current frame number can be manually set to a negative value (default False)

      :type: bool

   .. attribute:: use_text_edit_auto_close

      Automatically close relevant character pairs when typing in the text editor (default False)

      :type: bool

   .. attribute:: use_visual_keying

      Use Visual keying automatically for constrained objects (default False)

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

   - :class:`Preferences.edit`

