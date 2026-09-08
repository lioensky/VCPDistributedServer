UIList(bpy_struct)
==================

.. currentmodule:: bpy.types


Basic UIList Example
++++++++++++++++++++

This script is the UIList subclass used to show material slots, with a bunch of additional commentaries.

Notice the name of the class, this naming convention is similar as the one for panels or menus.

.. note::

   UIList subclasses must be registered for Blender to use them.

.. literalinclude:: ./examples/bpy.types.UIList.1.py
   :lines: 13-


Advanced UIList Example - Filtering and Reordering
++++++++++++++++++++++++++++++++++++++++++++++++++

This script is an extended version of the ``UIList`` subclass used to show vertex groups. It is not used 'as is',
because iterating over all vertices in a 'draw' function is a very bad idea for UI performance! However, it's a good
example of how to create/use filtering/reordering callbacks.

.. literalinclude:: ./examples/bpy.types.UIList.2.py
   :lines: 9-

base class --- :class:`bpy_struct`

subclasses --- 
:class:`ASSETBROWSER_UL_metadata_tags`, :class:`CLIP_UL_tracking_objects`, :class:`CURVES_UL_attributes`, :class:`DATA_UL_bone_collections`, :class:`FILEBROWSER_UL_dir`, :class:`GPENCIL_UL_annotation_layer`, :class:`GPENCIL_UL_matslots`, :class:`GREASE_PENCIL_UL_attributes`, :class:`GREASE_PENCIL_UL_masks`, :class:`IMAGE_UL_render_slots`, :class:`IMAGE_UL_udim_tiles`, :class:`MASK_UL_layers`, :class:`MATERIAL_UL_matslots`, :class:`MESH_UL_attributes`, :class:`MESH_UL_color_attributes`, :class:`MESH_UL_color_attributes_selector`, :class:`MESH_UL_uvmaps`, :class:`MESH_UL_vgroups`, :class:`PARTICLE_UL_particle_systems`, :class:`PHYSICS_UL_dynapaint_surfaces`, :class:`POINTCLOUD_UL_attributes`, :class:`POSE_UL_selection_set`, :class:`RENDER_UL_renderviews`, :class:`SCENE_UL_gltf2_filter_action`, :class:`SCENE_UL_keying_set_paths`, :class:`TEXTURE_UL_texpaintslots`, :class:`TEXTURE_UL_texslots`, :class:`UI_UL_list`, :class:`USERPREF_UL_asset_libraries`, :class:`USERPREF_UL_extension_repos`, :class:`VIEWLAYER_UL_aov`, :class:`VOLUME_UL_grids`, :class:`WORKSPACE_UL_addons_items`

.. class:: UIList(bpy_struct)

   UI list containing the elements of a collection

   .. data:: bitflag_filter_item

      The value of the reserved bitflag 'FILTER_ITEM' (in filter_flags values) (in [0, inf], default 0, readonly)

      :type: int

   .. data:: bitflag_item_never_show

      Skip the item from displaying in the list (in [0, inf], default 0, readonly)

      :type: int

   .. attribute:: bl_idname

      If this is set, the uilist gets a custom ID, otherwise it takes the name of the class used to define the uilist (for example, if the class name is "OBJECT_UL_vgroups", and bl_idname is not set by the script, then bl_idname = "OBJECT_UL_vgroups") (default "", never None)

      :type: str

   .. attribute:: filter_name

      Only show items matching this name (use '*' as wildcard) (default "", never None)

      :type: str

   .. data:: layout_type

      (default ``'DEFAULT'``, readonly)

      :type: Literal[:ref:`rna_enum_uilist_layout_type_items`]

   .. data:: list_id

      Identifier of the list, if any was passed to the "list_id" parameter of "template_list()" (default "", readonly, never None)

      :type: str

   .. attribute:: use_filter_invert

      Invert filtering (show hidden items, and vice versa) (default False)

      :type: bool

   .. attribute:: use_filter_show

      Show filtering options (default False)

      :type: bool

   .. attribute:: use_filter_sort_alpha

      Sort items by their name (default False)

      :type: bool

   .. attribute:: use_filter_sort_lock

      Lock the order of shown items (user cannot change it) (default False)

      :type: bool

   .. attribute:: use_filter_sort_reverse

      Reverse the order of shown items (default False)

      :type: bool

   .. method:: bl_system_properties_get(*, do_create=False)

      DEBUG ONLY. Internal access to runtime-defined RNA data storage, intended solely for testing and debugging purposes. Do not access it in regular scripting work, and in particular, do not assume that it contains writable data

      :param do_create: Ensure that system properties are created if they do not exist yet (optional)
      :type do_create: bool
      :return: The system properties root container, or None if there are no system properties stored in this data yet, and its creation was not requested
      :rtype: :class:`PropertyGroup`

   .. method:: draw_item(context, layout, data, item, icon, active_data, active_property, index, flt_flag)

      Draw an item in the list (NOTE: when you define your own draw_item function, you may want to check given 'item' is of the right type...)

      :type context: :class:`Context` | None
      :param layout: Layout to draw the item (never None)
      :type layout: :class:`UILayout` | None
      :param data: Data from which to take Collection property
      :type data: :class:`AnyType` | None
      :param item: Item of the collection property
      :type item: :class:`AnyType` | None
      :param icon: Icon of the item in the collection (in [0, inf])
      :type icon: int
      :param active_data: Data from which to take property for the active element (never None)
      :type active_data: :class:`AnyType` | None
      :param active_property: Identifier of property in active_data, for the active element (optional for registration, never None)
      :type active_property: str
      :param index: Index of the item in the collection (in [0, inf])
      :type index: int
      :param flt_flag: The filter-flag result for this item (in [0, inf])
      :type flt_flag: int

   .. method:: draw_filter(context, layout)

      Draw filtering options

      :type context: :class:`Context` | None
      :param layout: Layout to draw the item (never None)
      :type layout: :class:`UILayout` | None

   .. method:: filter_items(context, data, property)

      Filter and/or re-order items of the collection (output filter results in filter_flags, and reorder results in filter_neworder arrays)

      :type context: :class:`Context` | None
      :param data: Data from which to take Collection property
      :type data: :class:`AnyType` | None
      :param property: Identifier of property in data, for the collection (never None)
      :type property: str
      :return:
         ``filter_flags``, An array of filter flags, one for each item in the collection (NOTE: The upper 16 bits, including FILTER_ITEM, are reserved, only use the lower 16 bits for custom usages), :class:`bpy_prop_array`\ [int]

         ``filter_neworder``, An array of indices, one for each item in the collection, mapping the org index to the new one, :class:`bpy_prop_array`\ [int]

      :rtype: tuple[:class:`bpy_prop_array`\ [int], :class:`bpy_prop_array`\ [int]]

   .. classmethod:: append(draw_func)

      Append a draw function to this menu,
      takes the same arguments as the menus draw function

   .. classmethod:: is_extended()

   .. classmethod:: prepend(draw_func)

      Prepend a draw function to this menu, takes the same arguments as
      the menus draw function

   .. classmethod:: remove(draw_func)

      Remove a draw function that has been added to this menu.

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

