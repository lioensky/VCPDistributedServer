Node Operators
==============

.. module:: bpy.ops.node

.. function:: activate_viewer()

   Activate selected viewer node in compositor and geometry nodes

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: add_closure_zone(*, settings=None, use_transform=False, offset=(150.0, 0.0))

   Add a Closure zone

   :param settings: Settings, Settings to be applied on the newly created node (optional)
   :type settings: :class:`bpy_prop_collection`\ [:class:`NodeSetting`] | None
   :param use_transform: Use Transform, Start transform operator after inserting the node (optional)
   :type use_transform: bool
   :param offset: Offset, Offset of nodes from the cursor when added (array of 2 items, in [-inf, inf], optional)
   :type offset: Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/node.py\:729 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/node.py#L729>`__


.. function:: add_collection(*, name="", session_uid=0)

   Add a collection info node to the current node editor

   :param name: Name, Name of the data-block to use by the operator (optional, never None)
   :type name: str
   :param session_uid: Session UID, Session UID of the data-block to use by the operator (in [-inf, inf], optional)
   :type session_uid: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: add_color(*, color=(0.0, 0.0, 0.0, 0.0), gamma=False, has_alpha=False)

   Add a color node to the current node editor

   :param color: Color, Source color (array of 4 items, in [0, inf], optional)
   :type color: Sequence[float]
   :param gamma: Gamma Corrected, The source color is gamma corrected (optional)
   :type gamma: bool
   :param has_alpha: Has Alpha, The source color contains an Alpha component (optional)
   :type has_alpha: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: add_empty_group(*, settings=None, use_transform=False)

   Add a group node with an empty group

   :param settings: Settings, Settings to be applied on the newly created node (optional)
   :type settings: :class:`bpy_prop_collection`\ [:class:`NodeSetting`] | None
   :param use_transform: Use Transform, Start transform operator after inserting the node (optional)
   :type use_transform: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/node.py\:630 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/node.py#L630>`__


.. function:: add_foreach_geometry_element_zone(*, settings=None, use_transform=False, offset=(150.0, 0.0))

   Add a For Each Geometry Element zone that allows executing nodes e.g. for each vertex separately

   :param settings: Settings, Settings to be applied on the newly created node (optional)
   :type settings: :class:`bpy_prop_collection`\ [:class:`NodeSetting`] | None
   :param use_transform: Use Transform, Start transform operator after inserting the node (optional)
   :type use_transform: bool
   :param offset: Offset, Offset of nodes from the cursor when added (array of 2 items, in [-inf, inf], optional)
   :type offset: Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/node.py\:729 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/node.py#L729>`__


.. function:: add_group(*, name="", session_uid=0, show_datablock_in_node=True)

   Add an existing node group to the current node editor

   :param name: Name, Name of the data-block to use by the operator (optional, never None)
   :type name: str
   :param session_uid: Session UID, Session UID of the data-block to use by the operator (in [-inf, inf], optional)
   :type session_uid: int
   :param show_datablock_in_node: Show the data-block selector in the node, (optional)
   :type show_datablock_in_node: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: add_group_asset(*, asset_library_type='LOCAL', asset_library_identifier="", relative_asset_identifier="")

   Add a node group asset to the active node tree

   :param asset_library_type: Asset Library Type, (optional)
   :type asset_library_type: Literal[:ref:`rna_enum_asset_library_type_items`]
   :param asset_library_identifier: Asset Library Identifier, (optional, never None)
   :type asset_library_identifier: str
   :param relative_asset_identifier: Relative Asset Identifier, (optional, never None)
   :type relative_asset_identifier: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: add_group_input_node(*, socket_identifier="", panel_identifier=0)

   Add a Group Input node with selected sockets to the current node editor

   :param socket_identifier: Socket Identifier, Socket to include in the added group input/output node (optional, never None)
   :type socket_identifier: str
   :param panel_identifier: Panel Identifier, Panel from which to add sockets to the added group input/output node (in [-inf, inf], optional)
   :type panel_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: add_image(*, filepath="", directory="", files=None, hide_props_region=True, check_existing=False, filter_blender=False, filter_backup=False, filter_image=True, filter_movie=True, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='', name="", session_uid=0)

   Add a image/movie file as node to the current node editor

   :param filepath: File Path, Path to file (optional, never None)
   :type filepath: str
   :param directory: Directory, Directory of the file (optional, never None)
   :type directory: str
   :param files: Files, (optional)
   :type files: :class:`bpy_prop_collection`\ [:class:`OperatorFileListElement`] | None
   :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings (optional)
   :type hide_props_region: bool
   :param check_existing: Check Existing, Check and warn on overwriting existing files (optional)
   :type check_existing: bool
   :param filter_blender: Filter .blend files, (optional)
   :type filter_blender: bool
   :param filter_backup: Filter backup .blend files, (optional)
   :type filter_backup: bool
   :param filter_image: Filter image files, (optional)
   :type filter_image: bool
   :param filter_movie: Filter movie files, (optional)
   :type filter_movie: bool
   :param filter_python: Filter Python files, (optional)
   :type filter_python: bool
   :param filter_font: Filter font files, (optional)
   :type filter_font: bool
   :param filter_sound: Filter sound files, (optional)
   :type filter_sound: bool
   :param filter_text: Filter text files, (optional)
   :type filter_text: bool
   :param filter_archive: Filter archive files, (optional)
   :type filter_archive: bool
   :param filter_btx: Filter btx files, (optional)
   :type filter_btx: bool
   :param filter_alembic: Filter Alembic files, (optional)
   :type filter_alembic: bool
   :param filter_usd: Filter USD files, (optional)
   :type filter_usd: bool
   :param filter_obj: Filter OBJ files, (optional)
   :type filter_obj: bool
   :param filter_volume: Filter OpenVDB volume files, (optional)
   :type filter_volume: bool
   :param filter_folder: Filter folders, (optional)
   :type filter_folder: bool
   :param filter_blenlib: Filter Blender IDs, (optional)
   :type filter_blenlib: bool
   :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file (in [1, 9], optional)
   :type filemode: int
   :param relative_path: Relative Path, Select the file relative to the blend file (optional)
   :type relative_path: bool
   :param show_multiview: Enable Multi-View, (optional)
   :type show_multiview: bool
   :param use_multiview: Use Multi-View, (optional)
   :type use_multiview: bool
   :param display_type: Display Type, (optional)

      - ``DEFAULT``
        Default -- Automatically determine display type for files.
      - ``LIST_VERTICAL``
        Short List -- Display files as short list.
      - ``LIST_HORIZONTAL``
        Long List -- Display files as a detailed list.
      - ``THUMBNAIL``
        Thumbnails -- Display files as thumbnails.
   :type display_type: Literal['DEFAULT', 'LIST_VERTICAL', 'LIST_HORIZONTAL', 'THUMBNAIL']
   :param sort_method: File sorting mode, (optional)

      - ``DEFAULT``
        Default -- Automatically determine sort method for files.
      - ``FILE_SORT_ALPHA``
        Name -- Sort the file list alphabetically.
      - ``FILE_SORT_EXTENSION``
        Extension -- Sort the file list by extension/type.
      - ``FILE_SORT_TIME``
        Modified Date -- Sort files by modification time.
      - ``FILE_SORT_SIZE``
        Size -- Sort files by size.
      - ``ASSET_CATALOG``
        Asset Catalog -- Sort the asset list so that assets in the same catalog are kept together. Within a single catalog, assets are ordered by name. The catalogs are in order of the flattened catalog hierarchy..
   :type sort_method: Literal['', 'DEFAULT', 'FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE', 'ASSET_CATALOG']
   :param name: Name, Name of the data-block to use by the operator (optional, never None)
   :type name: str
   :param session_uid: Session UID, Session UID of the data-block to use by the operator (in [-inf, inf], optional)
   :type session_uid: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: add_import_node(*, directory="", files=None)

   Add an import node to the node tree

   :param directory: Directory, Directory of the file (optional, never None)
   :type directory: str
   :param files: Files, (optional)
   :type files: :class:`bpy_prop_collection`\ [:class:`OperatorFileListElement`] | None
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: add_mask(*, name="", session_uid=0)

   Add a mask node to the current node editor

   :param name: Name, Name of the data-block to use by the operator (optional, never None)
   :type name: str
   :param session_uid: Session UID, Session UID of the data-block to use by the operator (in [-inf, inf], optional)
   :type session_uid: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: add_material(*, name="", session_uid=0)

   Add a material node to the current node editor

   :param name: Name, Name of the data-block to use by the operator (optional, never None)
   :type name: str
   :param session_uid: Session UID, Session UID of the data-block to use by the operator (in [-inf, inf], optional)
   :type session_uid: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: add_node(*, settings=None, use_transform=False, type="", visible_output="")

   Add a node to the active tree

   :param settings: Settings, Settings to be applied on the newly created node (optional)
   :type settings: :class:`bpy_prop_collection`\ [:class:`NodeSetting`] | None
   :param use_transform: Use Transform, Start transform operator after inserting the node (optional)
   :type use_transform: bool
   :param type: Node Type, Node type (optional, never None)
   :type type: str
   :param visible_output: Output Name, If provided, all outputs that are named differently will be hidden (optional, never None)
   :type visible_output: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/node.py\:490 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/node.py#L490>`__


.. function:: add_object(*, name="", session_uid=0)

   Add an object info node to the current node editor

   :param name: Name, Name of the data-block to use by the operator (optional, never None)
   :type name: str
   :param session_uid: Session UID, Session UID of the data-block to use by the operator (in [-inf, inf], optional)
   :type session_uid: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: add_repeat_zone(*, settings=None, use_transform=False, offset=(150.0, 0.0))

   Add a repeat zone that allows executing nodes a dynamic number of times

   :param settings: Settings, Settings to be applied on the newly created node (optional)
   :type settings: :class:`bpy_prop_collection`\ [:class:`NodeSetting`] | None
   :param use_transform: Use Transform, Start transform operator after inserting the node (optional)
   :type use_transform: bool
   :param offset: Offset, Offset of nodes from the cursor when added (array of 2 items, in [-inf, inf], optional)
   :type offset: Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/node.py\:729 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/node.py#L729>`__


.. function:: add_reroute(*, path=None, cursor=11)

   Add a reroute node

   :param path: Path, (optional)
   :type path: :class:`bpy_prop_collection`\ [:class:`OperatorMousePath`] | None
   :param cursor: Cursor, (in [0, inf], optional)
   :type cursor: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: add_simulation_zone(*, settings=None, use_transform=False, offset=(150.0, 0.0))

   Add simulation zone input and output nodes to the active tree

   :param settings: Settings, Settings to be applied on the newly created node (optional)
   :type settings: :class:`bpy_prop_collection`\ [:class:`NodeSetting`] | None
   :param use_transform: Use Transform, Start transform operator after inserting the node (optional)
   :type use_transform: bool
   :param offset: Offset, Offset of nodes from the cursor when added (array of 2 items, in [-inf, inf], optional)
   :type offset: Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/node.py\:729 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/node.py#L729>`__


.. function:: add_zone(*, settings=None, use_transform=False, offset=(150.0, 0.0), input_node_type="", output_node_type="", add_default_geometry_link=False)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :param settings: Settings, Settings to be applied on the newly created node (optional)
   :type settings: :class:`bpy_prop_collection`\ [:class:`NodeSetting`] | None
   :param use_transform: Use Transform, Start transform operator after inserting the node (optional)
   :type use_transform: bool
   :param offset: Offset, Offset of nodes from the cursor when added (array of 2 items, in [-inf, inf], optional)
   :type offset: Sequence[float]
   :param input_node_type: Input Node, Specifies the input node used by the created zone (optional, never None)
   :type input_node_type: str
   :param output_node_type: Output Node, Specifies the output node used by the created zone (optional, never None)
   :type output_node_type: str
   :param add_default_geometry_link: Add Geometry Link, When enabled, create a link between geometry sockets in this zone (optional)
   :type add_default_geometry_link: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/node.py\:729 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/node.py#L729>`__


.. function:: attach()

   Attach active node to a frame

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: backimage_fit()

   Fit the background image to the view

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: backimage_move()

   Move node backdrop

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: backimage_sample()

   Use mouse to sample background image

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: backimage_zoom(*, factor=1.2)

   Zoom in/out the background image

   :param factor: Factor, (in [0, 10], optional)
   :type factor: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: bake_node_item_add(*, node_identifier=0)

   Add item below active item

   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: bake_node_item_move(*, direction='UP', node_identifier=0)

   Move active item

   :param direction: Direction, Move direction (optional)
   :type direction: Literal['UP', 'DOWN']
   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: bake_node_item_remove(*, node_identifier=0)

   Remove active item

   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: capture_attribute_item_add(*, node_identifier=0)

   Add item below active item

   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: capture_attribute_item_move(*, direction='UP', node_identifier=0)

   Move active item

   :param direction: Direction, Move direction (optional)
   :type direction: Literal['UP', 'DOWN']
   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: capture_attribute_item_remove(*, node_identifier=0)

   Remove active item

   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: clear_viewer_border()

   Clear the boundaries for viewer operations

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: clipboard_copy()

   Copy the selected nodes to the internal clipboard

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: clipboard_paste(*, offset=(0.0, 0.0))

   Paste nodes from the internal clipboard to the active node tree

   :param offset: Location, The 2D view location for the center of the new nodes, or unchanged if not set (array of 2 items, in [-inf, inf], optional)
   :type offset: Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: closure_input_item_add(*, node_identifier=0)

   Add item below active item

   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: closure_input_item_move(*, direction='UP', node_identifier=0)

   Move active item

   :param direction: Direction, Move direction (optional)
   :type direction: Literal['UP', 'DOWN']
   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: closure_input_item_remove(*, node_identifier=0)

   Remove active item

   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: closure_output_item_add(*, node_identifier=0)

   Add item below active item

   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: closure_output_item_move(*, direction='UP', node_identifier=0)

   Move active item

   :param direction: Direction, Move direction (optional)
   :type direction: Literal['UP', 'DOWN']
   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: closure_output_item_remove(*, node_identifier=0)

   Remove active item

   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: collapse_hide_unused_toggle()

   Toggle collapsed nodes and hide unused sockets

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/node.py\:995 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/node.py#L995>`__

.. function:: combine_bundle_item_add(*, node_identifier=0)

   Add item below active item

   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: combine_bundle_item_move(*, direction='UP', node_identifier=0)

   Move active item

   :param direction: Direction, Move direction (optional)
   :type direction: Literal['UP', 'DOWN']
   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: combine_bundle_item_remove(*, node_identifier=0)

   Remove active item

   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: connect_to_output(*, run_in_geometry_nodes=True)

   Connect active node to the active output node of the node tree

   :param run_in_geometry_nodes: Run in Geometry Nodes Editor, (optional)
   :type run_in_geometry_nodes: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/connect_to_output.py\:251 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/connect_to_output.py#L251>`__


.. function:: cryptomatte_layer_add()

   Add a new input layer to a Cryptomatte node

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: cryptomatte_layer_remove()

   Remove layer from a Cryptomatte node

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: deactivate_viewer()

   Deactivate selected viewer node in geometry nodes

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: default_group_width_set()

   Set the width based on the parent group node in the current context

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: delete()

   Remove selected nodes

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: delete_copy_reconnect(*, NODE_OT_clipboard_copy={}, NODE_OT_delete_reconnect={})

   Copy nodes to clipboard, remove and reconnect them.

   :param NODE_OT_clipboard_copy: Copy to Clipboard, Copy the selected nodes to the internal clipboard (optional, :func:`bpy.ops.node.clipboard_copy` keyword arguments)
   :type NODE_OT_clipboard_copy: dict[str, Any]
   :param NODE_OT_delete_reconnect: Delete with Reconnect, Remove nodes and reconnect nodes as if deletion was muted (optional, :func:`bpy.ops.node.delete_reconnect` keyword arguments)
   :type NODE_OT_delete_reconnect: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: delete_reconnect()

   Remove nodes and reconnect nodes as if deletion was muted

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: detach()

   Detach selected nodes from parents

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: detach_translate_attach(*, NODE_OT_detach={}, TRANSFORM_OT_translate={}, NODE_OT_attach={})

   Detach nodes, move and attach to frame

   :param NODE_OT_detach: Detach Nodes, Detach selected nodes from parents (optional, :func:`bpy.ops.node.detach` keyword arguments)
   :type NODE_OT_detach: dict[str, Any]
   :param TRANSFORM_OT_translate: Move, Move selected items (optional, :func:`bpy.ops.transform.translate` keyword arguments)
   :type TRANSFORM_OT_translate: dict[str, Any]
   :param NODE_OT_attach: Attach Nodes, Attach active node to a frame (optional, :func:`bpy.ops.node.attach` keyword arguments)
   :type NODE_OT_attach: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: duplicate(*, keep_inputs=False, linked=True)

   Duplicate selected nodes

   :param keep_inputs: Keep Inputs, Keep the input links to duplicated nodes (optional)
   :type keep_inputs: bool
   :param linked: Linked, Duplicate node but not node trees, linking to the original data (optional)
   :type linked: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: duplicate_compositing_modifier_node_group()

   Duplicate the currently assigned compositing node group.

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: duplicate_compositing_node_group()

   Duplicate the currently assigned compositing node group.

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: duplicate_move(*, NODE_OT_duplicate={}, NODE_OT_translate_attach={})

   Duplicate selected nodes and move them

   :param NODE_OT_duplicate: Duplicate Nodes, Duplicate selected nodes (optional, :func:`bpy.ops.node.duplicate` keyword arguments)
   :type NODE_OT_duplicate: dict[str, Any]
   :param NODE_OT_translate_attach: Move and Attach, Move nodes and attach to frame (optional, :func:`bpy.ops.node.translate_attach` keyword arguments)
   :type NODE_OT_translate_attach: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: duplicate_move_keep_inputs(*, NODE_OT_duplicate={}, NODE_OT_translate_attach={})

   Duplicate selected nodes keeping input links and move them

   :param NODE_OT_duplicate: Duplicate Nodes, Duplicate selected nodes (optional, :func:`bpy.ops.node.duplicate` keyword arguments)
   :type NODE_OT_duplicate: dict[str, Any]
   :param NODE_OT_translate_attach: Move and Attach, Move nodes and attach to frame (optional, :func:`bpy.ops.node.translate_attach` keyword arguments)
   :type NODE_OT_translate_attach: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: duplicate_move_linked(*, NODE_OT_duplicate={}, NODE_OT_translate_attach={})

   Duplicate selected nodes, but not their node trees, and move them

   :param NODE_OT_duplicate: Duplicate Nodes, Duplicate selected nodes (optional, :func:`bpy.ops.node.duplicate` keyword arguments)
   :type NODE_OT_duplicate: dict[str, Any]
   :param NODE_OT_translate_attach: Move and Attach, Move nodes and attach to frame (optional, :func:`bpy.ops.node.translate_attach` keyword arguments)
   :type NODE_OT_translate_attach: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: enum_definition_item_add(*, node_identifier=0)

   Add item below active item

   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: enum_definition_item_move(*, direction='UP', node_identifier=0)

   Move active item

   :param direction: Direction, Move direction (optional)
   :type direction: Literal['UP', 'DOWN']
   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: enum_definition_item_remove(*, node_identifier=0)

   Remove active item

   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: evaluate_closure_input_item_add(*, node_identifier=0)

   Add item below active item

   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: evaluate_closure_input_item_move(*, direction='UP', node_identifier=0)

   Move active item

   :param direction: Direction, Move direction (optional)
   :type direction: Literal['UP', 'DOWN']
   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: evaluate_closure_input_item_remove(*, node_identifier=0)

   Remove active item

   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: evaluate_closure_output_item_add(*, node_identifier=0)

   Add item below active item

   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: evaluate_closure_output_item_move(*, direction='UP', node_identifier=0)

   Move active item

   :param direction: Direction, Move direction (optional)
   :type direction: Literal['UP', 'DOWN']
   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: evaluate_closure_output_item_remove(*, node_identifier=0)

   Remove active item

   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: field_to_grid_item_add(*, node_identifier=0)

   Add item below active item

   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: field_to_grid_item_move(*, direction='UP', node_identifier=0)

   Move active item

   :param direction: Direction, Move direction (optional)
   :type direction: Literal['UP', 'DOWN']
   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: field_to_grid_item_remove(*, node_identifier=0)

   Remove active item

   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: field_to_list_item_add(*, node_identifier=0)

   Add item below active item

   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: field_to_list_item_move(*, direction='UP', node_identifier=0)

   Move active item

   :param direction: Direction, Move direction (optional)
   :type direction: Literal['UP', 'DOWN']
   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: field_to_list_item_remove(*, node_identifier=0)

   Remove active item

   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: file_output_item_add(*, node_identifier=0)

   Add item below active item

   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: file_output_item_move(*, direction='UP', node_identifier=0)

   Move active item

   :param direction: Direction, Move direction (optional)
   :type direction: Literal['UP', 'DOWN']
   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: file_output_item_remove(*, node_identifier=0)

   Remove active item

   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: find_node()

   Search for a node by name and focus and select it

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: foreach_geometry_element_zone_generation_item_add(*, node_identifier=0)

   Add item below active item

   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: foreach_geometry_element_zone_generation_item_move(*, direction='UP', node_identifier=0)

   Move active item

   :param direction: Direction, Move direction (optional)
   :type direction: Literal['UP', 'DOWN']
   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: foreach_geometry_element_zone_generation_item_remove(*, node_identifier=0)

   Remove active item

   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: foreach_geometry_element_zone_input_item_add(*, node_identifier=0)

   Add item below active item

   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: foreach_geometry_element_zone_input_item_move(*, direction='UP', node_identifier=0)

   Move active item

   :param direction: Direction, Move direction (optional)
   :type direction: Literal['UP', 'DOWN']
   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: foreach_geometry_element_zone_input_item_remove(*, node_identifier=0)

   Remove active item

   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: foreach_geometry_element_zone_main_item_add(*, node_identifier=0)

   Add item below active item

   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: foreach_geometry_element_zone_main_item_move(*, direction='UP', node_identifier=0)

   Move active item

   :param direction: Direction, Move direction (optional)
   :type direction: Literal['UP', 'DOWN']
   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: foreach_geometry_element_zone_main_item_remove(*, node_identifier=0)

   Remove active item

   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: format_string_item_add(*, node_identifier=0)

   Add item below active item

   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: format_string_item_move(*, direction='UP', node_identifier=0)

   Move active item

   :param direction: Direction, Move direction (optional)
   :type direction: Literal['UP', 'DOWN']
   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: format_string_item_remove(*, node_identifier=0)

   Remove active item

   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: geometry_nodes_viewer_item_add(*, node_identifier=0)

   Add item below active item

   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: geometry_nodes_viewer_item_move(*, direction='UP', node_identifier=0)

   Move active item

   :param direction: Direction, Move direction (optional)
   :type direction: Literal['UP', 'DOWN']
   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: geometry_nodes_viewer_item_remove(*, node_identifier=0)

   Remove active item

   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: gltf_settings_node_operator()

   Add a node to the active tree for glTF export

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `addons_core/io_scene_gltf2/blender/com/gltf2_blender_ui.py\:35 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/io_scene_gltf2/blender/com/gltf2_blender_ui.py#L35>`__

.. function:: group_edit(*, exit=False)

   Edit node group

   :param exit: Exit, (optional)
   :type exit: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: group_enter_exit()

   Enter or exit node group based on cursor location

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: group_insert()

   Insert selected nodes into a node group

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: group_make()

   Make group from selected nodes

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: group_separate(*, type='COPY')

   Separate selected nodes from the node group

   :param type: Type, (optional)

      - ``COPY``
        Copy -- Copy to parent node tree, keep group intact.
      - ``MOVE``
        Move -- Move to parent node tree, remove from group.
   :type type: Literal['COPY', 'MOVE']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: group_ungroup()

   Ungroup selected nodes

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: hide_socket_toggle()

   Toggle unused node socket display

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: hide_toggle()

   Toggle collapsing of selected nodes

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: index_switch_item_add(*, node_identifier=0)

   Add an item to the index switch

   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: index_switch_item_remove(*, index=0)

   Remove an item from the index switch

   :param index: Index, Index to remove (in [0, inf], optional)
   :type index: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: insert_offset()

   Automatically offset nodes on insertion

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: interface_item_duplicate()

   Add a copy of the active item to the interface

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/node.py\:1181 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/node.py#L1181>`__

.. function:: interface_item_make_panel_toggle()

   Make the active boolean socket a toggle for its parent panel

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/node.py\:1260 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/node.py#L1260>`__

.. function:: interface_item_new(*, item_type='INPUT')

   Add a new item to the interface

   :param item_type: Item Type, Type of the item to create (optional)
   :type item_type: Literal['INPUT', 'OUTPUT', 'PANEL']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/node.py\:1087 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/node.py#L1087>`__


.. function:: interface_item_new_panel_toggle()

   Add a checkbox to the currently selected panel

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/node.py\:1152 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/node.py#L1152>`__

.. function:: interface_item_remove()

   Remove selected items from the interface

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/node.py\:1200 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/node.py#L1200>`__

.. function:: interface_item_unlink_panel_toggle()

   Make the panel toggle a stand-alone socket

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/node.py\:1308 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/node.py#L1308>`__

.. function:: join()

   Attach selected nodes to a new common frame

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: join_named(*, NODE_OT_join={}, WM_OT_call_panel={})

   Create a new frame node around the selected nodes and name it immediately

   :param NODE_OT_join: Join Nodes in Frame, Attach selected nodes to a new common frame (optional, :func:`bpy.ops.node.join` keyword arguments)
   :type NODE_OT_join: dict[str, Any]
   :param WM_OT_call_panel: Call Panel, Open a predefined panel (optional, :func:`bpy.ops.wm.call_panel` keyword arguments)
   :type WM_OT_call_panel: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: join_nodes()

   Merge selected group input nodes into one if possible

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: link(*, detach=False, drag_start=(0.0, 0.0), inside_padding=2.0, outside_padding=0.0, speed_ramp=1.0, max_speed=26.0, delay=0.5, zoom_influence=0.5)

   Use the mouse to create a link between two nodes

   :param detach: Detach, Detach and redirect existing links (optional)
   :type detach: bool
   :param drag_start: Drag Start, The position of the mouse cursor at the start of the operation (array of 2 items, in [-6, 6], optional)
   :type drag_start: Sequence[float]
   :param inside_padding: Inside Padding, Inside distance in UI units from the edge of the region within which to start panning (in [0, 100], optional)
   :type inside_padding: float
   :param outside_padding: Outside Padding, Outside distance in UI units from the edge of the region at which to stop panning (in [0, 100], optional)
   :type outside_padding: float
   :param speed_ramp: Speed Ramp, Width of the zone in UI units where speed increases with distance from the edge (in [0, 100], optional)
   :type speed_ramp: float
   :param max_speed: Max Speed, Maximum speed in UI units per second (in [0, 10000], optional)
   :type max_speed: float
   :param delay: Delay, Delay in seconds before maximum speed is reached (in [0, 10], optional)
   :type delay: float
   :param zoom_influence: Zoom Influence, Influence of the zoom factor on scroll speed (in [0, 1], optional)
   :type zoom_influence: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: link_drag_operation_test(*, find_link_operations=False, link_operation_index=-1)

   Run a node link-drag operation for testing

   :param find_link_operations: Find Link Operations, Write link operation names for the context socket the "link_operation_names" property of the node tree (optional)
   :type find_link_operations: bool
   :param link_operation_index: Link Operation Index, Link operation to execute on the context socket (in [-1, inf], optional)
   :type link_operation_index: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: link_make(*, replace=False)

   Make a link between selected output and input sockets

   :param replace: Replace, Replace socket connections with the new links (optional)
   :type replace: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: link_viewer()

   Link to viewer node

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: links_cut(*, path=None, cursor=15)

   Use the mouse to cut (remove) some links

   :param path: Path, (optional)
   :type path: :class:`bpy_prop_collection`\ [:class:`OperatorMousePath`] | None
   :param cursor: Cursor, (in [0, inf], optional)
   :type cursor: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: links_detach()

   Remove all links to selected nodes, and try to connect neighbor nodes together

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: links_mute(*, path=None, cursor=39)

   Use the mouse to mute links

   :param path: Path, (optional)
   :type path: :class:`bpy_prop_collection`\ [:class:`OperatorMousePath`] | None
   :param cursor: Cursor, (in [0, inf], optional)
   :type cursor: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: move_detach_links(*, NODE_OT_links_detach={}, TRANSFORM_OT_translate={})

   Move a node to detach links

   :param NODE_OT_links_detach: Detach Links, Remove all links to selected nodes, and try to connect neighbor nodes together (optional, :func:`bpy.ops.node.links_detach` keyword arguments)
   :type NODE_OT_links_detach: dict[str, Any]
   :param TRANSFORM_OT_translate: Move, Move selected items (optional, :func:`bpy.ops.transform.translate` keyword arguments)
   :type TRANSFORM_OT_translate: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: move_detach_links_release(*, NODE_OT_links_detach={}, NODE_OT_translate_attach={})

   Move a node to detach links

   :param NODE_OT_links_detach: Detach Links, Remove all links to selected nodes, and try to connect neighbor nodes together (optional, :func:`bpy.ops.node.links_detach` keyword arguments)
   :type NODE_OT_links_detach: dict[str, Any]
   :param NODE_OT_translate_attach: Move and Attach, Move nodes and attach to frame (optional, :func:`bpy.ops.node.translate_attach` keyword arguments)
   :type NODE_OT_translate_attach: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: mute_toggle()

   Toggle muting of selected nodes

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: new_compositing_node_group(*, name="")

   Create a new compositing node group and initialize it with default nodes

   :param name: Name, (optional, never None)
   :type name: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: new_compositor_sequencer_node_group(*, name="Sequencer Compositor Nodes")

   Create a new compositor node group for sequencer

   :param name: Name, (optional, never None)
   :type name: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: new_geometry_node_group_assign()

   Create a new geometry node group and assign it to the active modifier

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/geometry_nodes.py\:345 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/geometry_nodes.py#L345>`__

.. function:: new_geometry_node_group_tool()

   Create a new geometry node group for a tool

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/geometry_nodes.py\:366 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/geometry_nodes.py#L366>`__

.. function:: new_geometry_nodes_modifier()

   Create a new modifier with a new geometry node group

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/geometry_nodes.py\:322 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/geometry_nodes.py#L322>`__

.. function:: new_node_tree(*, type='', name="NodeTree")

   Create a new node tree

   :param type: Tree Type, (optional)
   :type type: str
   :param name: Name, (optional, never None)
   :type name: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: node_color_preset_add(*, name="", remove_name=False, remove_active=False)

   Add or remove a Node Color Preset

   :param name: Name, Name of the preset, used to make the path name (optional, never None)
   :type name: str
   :param remove_name: remove_name, (optional)
   :type remove_name: bool
   :param remove_active: remove_active, (optional)
   :type remove_active: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/presets.py\:119 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/presets.py#L119>`__


.. function:: node_copy_color()

   Copy color to all selected nodes

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: options_toggle()

   Toggle option buttons display for selected nodes

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: parent_set()

   Attach selected nodes

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: preview_toggle()

   Toggle preview display for selected nodes

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: read_viewlayers()

   Read all render layers of all used scenes

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: render_changed()

   Render current scene, when input node's layer has been changed

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: repeat_zone_item_add(*, node_identifier=0)

   Add item below active item

   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: repeat_zone_item_move(*, direction='UP', node_identifier=0)

   Move active item

   :param direction: Direction, Move direction (optional)
   :type direction: Literal['UP', 'DOWN']
   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: repeat_zone_item_remove(*, node_identifier=0)

   Remove active item

   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: resize()

   Resize a node

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select(*, extend=False, deselect=False, toggle=False, deselect_all=False, select_passthrough=False, location=(0, 0), socket_select=False, clear_viewer=False)

   Select the node under the cursor

   :param extend: Extend, Extend selection instead of deselecting everything first (optional)
   :type extend: bool
   :param deselect: Deselect, Remove from selection (optional)
   :type deselect: bool
   :param toggle: Toggle Selection, Toggle the selection (optional)
   :type toggle: bool
   :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor (optional)
   :type deselect_all: bool
   :param select_passthrough: Only Select Unselected, Ignore the select action when the element is already selected (optional)
   :type select_passthrough: bool
   :param location: Location, Mouse location (array of 2 items, in [-inf, inf], optional)
   :type location: Sequence[int]
   :param socket_select: Socket Select, (optional)
   :type socket_select: bool
   :param clear_viewer: Clear Viewer, Deactivate geometry nodes viewer when clicking in empty space (optional)
   :type clear_viewer: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_all(*, action='TOGGLE')

   (De)select all nodes

   :param action: Action, Selection action to execute (optional)

      - ``TOGGLE``
        Toggle -- Toggle selection for all elements.
      - ``SELECT``
        Select -- Select all elements.
      - ``DESELECT``
        Deselect -- Deselect all elements.
      - ``INVERT``
        Invert -- Invert selection of all elements.
   :type action: Literal['TOGGLE', 'SELECT', 'DESELECT', 'INVERT']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_box(*, tweak=False, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, mode='SET')

   Use box selection to select nodes

   :param tweak: Tweak, Only activate when mouse is not over a node (useful for tweak gesture) (optional)
   :type tweak: bool
   :param xmin: X Min, (in [-inf, inf], optional)
   :type xmin: int
   :param xmax: X Max, (in [-inf, inf], optional)
   :type xmax: int
   :param ymin: Y Min, (in [-inf, inf], optional)
   :type ymin: int
   :param ymax: Y Max, (in [-inf, inf], optional)
   :type ymax: int
   :param wait_for_input: Wait for Input, (optional)
   :type wait_for_input: bool
   :param mode: Mode, (optional)

      - ``SET``
        Set -- Set a new selection.
      - ``ADD``
        Extend -- Extend existing selection.
      - ``SUB``
        Subtract -- Subtract existing selection.
   :type mode: Literal['SET', 'ADD', 'SUB']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_circle(*, x=0, y=0, radius=25, wait_for_input=True, mode='SET')

   Use circle selection to select nodes

   :param x: X, (in [-inf, inf], optional)
   :type x: int
   :param y: Y, (in [-inf, inf], optional)
   :type y: int
   :param radius: Radius, (in [1, inf], optional)
   :type radius: int
   :param wait_for_input: Wait for Input, (optional)
   :type wait_for_input: bool
   :param mode: Mode, (optional)

      - ``SET``
        Set -- Set a new selection.
      - ``ADD``
        Extend -- Extend existing selection.
      - ``SUB``
        Subtract -- Subtract existing selection.
   :type mode: Literal['SET', 'ADD', 'SUB']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_grouped(*, extend=False, type='TYPE')

   Select nodes with similar properties

   :param extend: Extend, Extend selection instead of deselecting everything first (optional)
   :type extend: bool
   :param type: Type, (optional)
   :type type: Literal['TYPE', 'COLOR', 'PREFIX', 'SUFFIX']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_lasso(*, tweak=False, path=None, use_smooth_stroke=False, smooth_stroke_factor=0.75, smooth_stroke_radius=35, mode='SET')

   Select nodes using lasso selection

   :param tweak: Tweak, Only activate when mouse is not over a node (useful for tweak gesture) (optional)
   :type tweak: bool
   :param path: Path, (optional)
   :type path: :class:`bpy_prop_collection`\ [:class:`OperatorMousePath`] | None
   :param use_smooth_stroke: Stabilize Stroke, Selection lags behind mouse and follows a smoother path (optional)
   :type use_smooth_stroke: bool
   :param smooth_stroke_factor: Smooth Stroke Factor, Higher values give a smoother stroke (in [0.5, 0.99], optional)
   :type smooth_stroke_factor: float
   :param smooth_stroke_radius: Smooth Stroke Radius, Minimum distance from last point before selection continues (in [10, 200], optional)
   :type smooth_stroke_radius: int
   :param mode: Mode, (optional)

      - ``SET``
        Set -- Set a new selection.
      - ``ADD``
        Extend -- Extend existing selection.
      - ``SUB``
        Subtract -- Subtract existing selection.
   :type mode: Literal['SET', 'ADD', 'SUB']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_link_viewer(*, NODE_OT_select={}, NODE_OT_link_viewer={})

   Select node and link it to a viewer node

   :param NODE_OT_select: Select, Select the node under the cursor (optional, :func:`bpy.ops.node.select` keyword arguments)
   :type NODE_OT_select: dict[str, Any]
   :param NODE_OT_link_viewer: Link to Viewer Node, Link to viewer node (optional, :func:`bpy.ops.node.link_viewer` keyword arguments)
   :type NODE_OT_link_viewer: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_linked_from()

   Select nodes linked from the selected ones

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select_linked_to()

   Select nodes linked to the selected ones

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select_same_type_step(*, prev=False)

   Activate and view same node type, step by step

   :param prev: Previous, (optional)
   :type prev: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: separate_bundle_item_add(*, node_identifier=0)

   Add item below active item

   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: separate_bundle_item_move(*, direction='UP', node_identifier=0)

   Move active item

   :param direction: Direction, Move direction (optional)
   :type direction: Literal['UP', 'DOWN']
   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: separate_bundle_item_remove(*, node_identifier=0)

   Remove active item

   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: shader_script_update()

   Update shader script node with new sockets and options from the script

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: simulation_zone_item_add(*, node_identifier=0)

   Add item below active item

   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: simulation_zone_item_move(*, direction='UP', node_identifier=0)

   Move active item

   :param direction: Direction, Move direction (optional)
   :type direction: Literal['UP', 'DOWN']
   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: simulation_zone_item_remove(*, node_identifier=0)

   Remove active item

   :param node_identifier: Node Identifier, Optional identifier of the node to operate on (in [0, inf], optional)
   :type node_identifier: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: sockets_sync(*, node_name="")

   Update sockets to match what is actually used

   :param node_name: Node Name, (optional, never None)
   :type node_name: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: swap_empty_group(*, settings=None)

   Replace active node with an empty group

   :param settings: Settings, Settings to be applied on the newly created node (optional)
   :type settings: :class:`bpy_prop_collection`\ [:class:`NodeSetting`] | None
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/node.py\:666 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/node.py#L666>`__


.. function:: swap_group_asset(*, asset_library_type='LOCAL', asset_library_identifier="", relative_asset_identifier="")

   Swap selected nodes with the specified node group asset

   :param asset_library_type: Asset Library Type, (optional)
   :type asset_library_type: Literal[:ref:`rna_enum_asset_library_type_items`]
   :param asset_library_identifier: Asset Library Identifier, (optional, never None)
   :type asset_library_identifier: str
   :param relative_asset_identifier: Relative Asset Identifier, (optional, never None)
   :type relative_asset_identifier: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: swap_node(*, settings=None, type="", visible_output="")

   Replace the selected nodes with the specified type

   :param settings: Settings, Settings to be applied on the newly created node (optional)
   :type settings: :class:`bpy_prop_collection`\ [:class:`NodeSetting`] | None
   :param type: Node Type, Node type (optional, never None)
   :type type: str
   :param visible_output: Output Name, If provided, all outputs that are named differently will be hidden (optional, never None)
   :type visible_output: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/node.py\:555 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/node.py#L555>`__


.. function:: swap_zone(*, settings=None, offset=(150.0, 0.0), input_node_type="", output_node_type="", add_default_geometry_link=False)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :param settings: Settings, Settings to be applied on the newly created node (optional)
   :type settings: :class:`bpy_prop_collection`\ [:class:`NodeSetting`] | None
   :param offset: Offset, Offset of nodes from the cursor when added (array of 2 items, in [-inf, inf], optional)
   :type offset: Sequence[float]
   :param input_node_type: Input Node, Specifies the input node used by the created zone (optional, never None)
   :type input_node_type: str
   :param output_node_type: Output Node, Specifies the output node used by the created zone (optional, never None)
   :type output_node_type: str
   :param add_default_geometry_link: Add Geometry Link, When enabled, create a link between geometry sockets in this zone (optional)
   :type add_default_geometry_link: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/node.py\:847 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/node.py#L847>`__


.. function:: test_inlining_shader_nodes()

   Create a new inlined shader node tree as is consumed by renderers

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: toggle_viewer()

   Toggle selected viewer node in compositor and geometry nodes

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: translate_attach(*, TRANSFORM_OT_translate={}, NODE_OT_attach={})

   Move nodes and attach to frame

   :param TRANSFORM_OT_translate: Move, Move selected items (optional, :func:`bpy.ops.transform.translate` keyword arguments)
   :type TRANSFORM_OT_translate: dict[str, Any]
   :param NODE_OT_attach: Attach Nodes, Attach active node to a frame (optional, :func:`bpy.ops.node.attach` keyword arguments)
   :type NODE_OT_attach: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: translate_attach_remove_on_cancel(*, TRANSFORM_OT_translate={}, NODE_OT_attach={})

   Move nodes and attach to frame

   :param TRANSFORM_OT_translate: Move, Move selected items (optional, :func:`bpy.ops.transform.translate` keyword arguments)
   :type TRANSFORM_OT_translate: dict[str, Any]
   :param NODE_OT_attach: Attach Nodes, Attach active node to a frame (optional, :func:`bpy.ops.node.attach` keyword arguments)
   :type NODE_OT_attach: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: tree_path_parent(*, parent_tree_index=0)

   Go to parent node tree

   :param parent_tree_index: Parent Index, Parent index in context path (in [-inf, inf], optional)
   :type parent_tree_index: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/node.py\:1031 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/node.py#L1031>`__


.. function:: view_all()

   Resize view so you can see all nodes

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: view_selected()

   Resize view so you can see selected nodes

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: viewer_border(*, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True)

   Set the boundaries for viewer operations (Not implemented)

   :param xmin: X Min, (in [-inf, inf], optional)
   :type xmin: int
   :param xmax: X Max, (in [-inf, inf], optional)
   :type xmax: int
   :param ymin: Y Min, (in [-inf, inf], optional)
   :type ymin: int
   :param ymax: Y Max, (in [-inf, inf], optional)
   :type ymax: int
   :param wait_for_input: Wait for Input, (optional)
   :type wait_for_input: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: viewer_shortcut_get(*, viewer_index=0)

   Toggle a specific viewer node using 1,2,..,9 keys

   :param viewer_index: Viewer Index, Index corresponding to the shortcut, e.g. number key 1 corresponds to index 1 etc.. (in [-inf, inf], optional)
   :type viewer_index: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/node.py\:1422 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/node.py#L1422>`__


.. function:: viewer_shortcut_set(*, viewer_index=0)

   Create a viewer shortcut for the selected node by pressing ctrl+1,2,..9

   :param viewer_index: Viewer Index, Index corresponding to the shortcut, e.g. number key 1 corresponds to index 1 etc.. (in [-inf, inf], optional)
   :type viewer_index: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/node.py\:1362 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/node.py#L1362>`__


