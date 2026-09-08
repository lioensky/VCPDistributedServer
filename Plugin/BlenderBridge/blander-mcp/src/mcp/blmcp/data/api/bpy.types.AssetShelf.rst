AssetShelf(bpy_struct)
======================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

subclasses --- 
:class:`IMAGE_AST_brush_paint`, :class:`NODE_AST_compositor`, :class:`VIEW3D_AST_brush_gpencil_paint`, :class:`VIEW3D_AST_brush_gpencil_sculpt`, :class:`VIEW3D_AST_brush_gpencil_vertex`, :class:`VIEW3D_AST_brush_gpencil_weight`, :class:`VIEW3D_AST_brush_sculpt`, :class:`VIEW3D_AST_brush_sculpt_curves`, :class:`VIEW3D_AST_brush_texture_paint`, :class:`VIEW3D_AST_brush_vertex_paint`, :class:`VIEW3D_AST_brush_weight_paint`, :class:`VIEW3D_AST_pose_library`

.. class:: AssetShelf(bpy_struct)

   Regions for quick access to assets

   .. attribute:: asset_library_reference

      Choose the asset library to display assets from (default ``'ALL'``)

      - ``ALL``
        All Libraries -- Show assets from all of the listed asset libraries.
      - ``LOCAL``
        Current File -- Show the assets currently available in this Blender session.
      - ``ESSENTIALS``
        Essentials -- Show the basic building blocks and utilities coming with Blender.
      - ``CUSTOM``
        Custom -- Show assets from the asset libraries configured in the Preferences.

      :type: Literal['ALL', 'LOCAL', 'ESSENTIALS', 'CUSTOM']

   .. attribute:: bl_activate_operator

      Operator to call when activating an item with asset reference properties (default "", never None)

      :type: str

   .. attribute:: bl_default_preview_size

      Default size of the asset preview thumbnails in pixels (in [32, 256], default 0)

      :type: int

   .. attribute:: bl_drag_operator

      Operator to call when dragging an item with asset reference properties (default "", never None)

      :type: str

   .. attribute:: bl_idname

      If this is set, the asset gets a custom ID, otherwise it takes the name of the class used to define the asset (for example, if the class name is "OBJECT_AST_hello", and bl_idname is not set by the script, then bl_idname = "OBJECT_AST_hello") (default "", never None)

      :type: str

   .. attribute:: bl_options

      Options for this asset shelf type (default set())

      - ``NO_ASSET_DRAG``
        No Asset Dragging -- Disable the default asset dragging on drag events. Useful for implementing custom dragging via custom key-map items..
      - ``DEFAULT_VISIBLE``
        Visible by Default -- Unhide the asset shelf when it's available for the first time, otherwise it will be hidden.
      - ``STORE_ENABLED_CATALOGS_IN_PREFERENCES``
        Store Enabled Catalogs in Preferences -- Store the shelf's enabled catalogs in the preferences rather than the local asset shelf settings.
      - ``ACTIVATE_FOR_CONTEXT_MENU``
        When spawning a context menu for an asset, activate the asset and call \`bl_activate_operator\` if present, rather than just highlighting the asset.

      :type: set[Literal['NO_ASSET_DRAG', 'DEFAULT_VISIBLE', 'STORE_ENABLED_CATALOGS_IN_PREFERENCES', 'ACTIVATE_FOR_CONTEXT_MENU']]

   .. attribute:: bl_space_type

      The space where the asset shelf will show up in. Ignored for popup asset shelves which can be displayed in any space. (default ``'EMPTY'``)

      :type: Literal[:ref:`rna_enum_space_type_items`]

   .. attribute:: filter_action

      Show Action data-blocks (default False)

      :type: bool

   .. attribute:: filter_annotations

      Show Annotation data-blocks (default False)

      :type: bool

   .. attribute:: filter_armature

      Show Armature data-blocks (default False)

      :type: bool

   .. attribute:: filter_brush

      Show Brushes data-blocks (default False)

      :type: bool

   .. attribute:: filter_cachefile

      Show Cache File data-blocks (default False)

      :type: bool

   .. attribute:: filter_camera

      Show Camera data-blocks (default False)

      :type: bool

   .. attribute:: filter_curve

      Show Curve data-blocks (default False)

      :type: bool

   .. attribute:: filter_curves

      Show/hide Curves data-blocks (default False)

      :type: bool

   .. attribute:: filter_font

      Show Font data-blocks (default False)

      :type: bool

   .. attribute:: filter_grease_pencil

      Show Grease Pencil data-blocks (default False)

      :type: bool

   .. attribute:: filter_group

      Show Collection data-blocks (default False)

      :type: bool

   .. attribute:: filter_image

      Show Image data-blocks (default False)

      :type: bool

   .. attribute:: filter_lattice

      Show Lattice data-blocks (default False)

      :type: bool

   .. attribute:: filter_light

      Show Light data-blocks (default False)

      :type: bool

   .. attribute:: filter_light_probe

      Show Light Probe data-blocks (default False)

      :type: bool

   .. attribute:: filter_linestyle

      Show Freestyle's Line Style data-blocks (default False)

      :type: bool

   .. attribute:: filter_mask

      Show Mask data-blocks (default False)

      :type: bool

   .. attribute:: filter_material

      Show Material data-blocks (default False)

      :type: bool

   .. attribute:: filter_mesh

      Show Mesh data-blocks (default False)

      :type: bool

   .. attribute:: filter_metaball

      Show Metaball data-blocks (default False)

      :type: bool

   .. attribute:: filter_movie_clip

      Show Movie Clip data-blocks (default False)

      :type: bool

   .. attribute:: filter_node_tree

      Show Node Tree data-blocks (default False)

      :type: bool

   .. attribute:: filter_object

      Show Object data-blocks (default False)

      :type: bool

   .. attribute:: filter_paint_curve

      Show Paint Curve data-blocks (default False)

      :type: bool

   .. attribute:: filter_palette

      Show Palette data-blocks (default False)

      :type: bool

   .. attribute:: filter_particle_settings

      Show Particle Settings data-blocks (default False)

      :type: bool

   .. attribute:: filter_pointcloud

      Show/hide Point Cloud data-blocks (default False)

      :type: bool

   .. attribute:: filter_scene

      Show Scene data-blocks (default False)

      :type: bool

   .. attribute:: filter_sound

      Show Sound data-blocks (default False)

      :type: bool

   .. attribute:: filter_speaker

      Show Speaker data-blocks (default False)

      :type: bool

   .. attribute:: filter_text

      Show Text data-blocks (default False)

      :type: bool

   .. attribute:: filter_texture

      Show Texture data-blocks (default False)

      :type: bool

   .. attribute:: filter_volume

      Show/hide Volume data-blocks (default False)

      :type: bool

   .. attribute:: filter_work_space

      Show workspace data-blocks (default False)

      :type: bool

   .. attribute:: filter_world

      Show World data-blocks (default False)

      :type: bool

   .. attribute:: preview_size

      Size of the asset preview thumbnails in pixels (in [24, 256], default 0)

      :type: int

   .. attribute:: search_filter

      Filter assets by name (default "", never None)

      :type: str

   .. attribute:: show_names

      Show the asset name together with the preview. Otherwise only the preview will be visible. (default False)

      :type: bool

   .. classmethod:: poll(context)

      If this method returns a non-null output, the asset shelf will be visible

      :type context: :class:`Context` | None
      :rtype: bool

   .. classmethod:: asset_poll(asset)

      Determine if an asset should be visible in the asset shelf. If this method returns a non-null output, the asset will be visible.

      :type asset: :class:`AssetRepresentation` | None
      :rtype: bool

   .. classmethod:: get_active_asset()

      Return a reference to the asset that should be highlighted as active in the asset shelf

      :return: The weak reference to the asset to be highlighted as active, or None
      :rtype: :class:`AssetWeakReference`

   .. classmethod:: draw_context_menu(context, asset, layout)

      Draw UI elements into the context menu UI layout displayed on right click

      :type context: :class:`Context` | None
      :type asset: :class:`AssetRepresentation` | None
      :type layout: :class:`UILayout` | None

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

