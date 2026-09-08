Outliner Operators
==================

.. module:: bpy.ops.outliner

.. function:: action_set(*, action='')

   Change the active action used

   :param action: Action, (optional)
   :type action: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: animdata_operation(*, type='CLEAR_ANIMDATA')

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :param type: Animation Operation, (optional)

      - ``CLEAR_ANIMDATA``
        Clear Animation Data -- Remove this animation data container.
      - ``SET_ACT``
        Set Action.
      - ``CLEAR_ACT``
        Unlink Action.
      - ``REFRESH_DRIVERS``
        Refresh Drivers.
      - ``CLEAR_DRIVERS``
        Clear Drivers.
   :type type: Literal['CLEAR_ANIMDATA', 'SET_ACT', 'CLEAR_ACT', 'REFRESH_DRIVERS', 'CLEAR_DRIVERS']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: clear_filter()

   Clear the search filter

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: collection_color_tag_set(*, color='NONE')

   Set a color tag for the selected collections

   :param color: Color Tag, (optional)
   :type color: Literal[:ref:`rna_enum_collection_color_items`]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: collection_disable()

   Disable viewport display in the view layers

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: collection_disable_render()

   Do not render this collection

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: collection_drop()

   Drag to move to collection in Outliner

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: collection_duplicate()

   Recursively duplicate the collection, all its children, objects and object data

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: collection_duplicate_linked()

   Recursively duplicate the collection, all its children and objects, with linked object data

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: collection_enable()

   Enable viewport display in the view layers

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: collection_enable_render()

   Render the collection

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: collection_exclude_clear()

   Include collection in the active view layer

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: collection_exclude_set()

   Exclude collection from the active view layer

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: collection_hide()

   Hide the collection in this view layer

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: collection_hide_inside()

   Hide all the objects and collections inside the collection

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: collection_hierarchy_delete()

   Delete selected collection hierarchies

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: collection_holdout_clear()

   Clear masking of collection in the active view layer

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: collection_holdout_set()

   Mask collection in the active view layer

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: collection_indirect_only_clear()

   Clear collection contributing only indirectly in the view layer

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: collection_indirect_only_set()

   Set collection to only contribute indirectly (through shadows and reflections) in the view layer

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: collection_instance()

   Instance selected collections to active scene

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: collection_isolate(*, extend=False)

   Hide all but this collection and its parents

   :param extend: Extend, Extend current visible collections (optional)
   :type extend: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: collection_link()

   Link selected collections to active scene

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: collection_new(*, nested=True)

   Add a new collection inside selected collection

   :param nested: Nested, Add as child of selected collection (optional)
   :type nested: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: collection_objects_deselect()

   Deselect objects in collection

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: collection_objects_select()

   Select objects in collection

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: collection_show()

   Show the collection in this view layer

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: collection_show_inside()

   Show all the objects and collections inside the collection

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: constraint_operation(*, type='ENABLE')

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :param type: Constraint Operation, (optional)
   :type type: Literal['ENABLE', 'DISABLE', 'DELETE']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: data_operation(*, type='DEFAULT')

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :param type: Data Operation, (optional)
   :type type: Literal['DEFAULT']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: datastack_drop()

   Copy or reorder modifiers, constraints, and effects

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: delete(*, hierarchy=False)

   Delete selected objects and collections

   :param hierarchy: Hierarchy, Delete child objects and collections (optional)
   :type hierarchy: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: drivers_add_selected()

   Add drivers to selected items

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: drivers_delete_selected()

   Delete drivers assigned to selected items

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: expanded_toggle()

   Expand/Collapse all items

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: hide()

   Hide selected objects and collections

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: highlight_update()

   Update the item highlight based on the current mouse position

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: id_copy()

   Copy the selected data-blocks to the internal clipboard

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: id_delete()

   Delete the ID under cursor

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: id_linked_relocate()

   Replace the active linked ID (and its dependencies if any) by another one, from the same or a different library

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: id_operation(*, type='UNLINK')

   General data-block management operations

   :param type: ID Data Operation, (optional)

      - ``UNLINK``
        Unlink.
      - ``LOCAL``
        Make Local.
      - ``SINGLE``
        Make Single User.
      - ``DELETE``
        Delete.
      - ``REMAP``
        Remap Users -- Make all users of selected data-blocks to use instead current (clicked) one.
      - ``COPY``
        Copy.
      - ``PASTE``
        Paste.
      - ``ADD_FAKE``
        Add Fake User -- Ensure data-block gets saved even if it isn't in use (e.g. for motion and material libraries).
      - ``CLEAR_FAKE``
        Clear Fake User.
      - ``RENAME``
        Rename.
      - ``SELECT_LINKED``
        Select Linked.
   :type type: Literal['UNLINK', 'LOCAL', 'SINGLE', 'DELETE', 'REMAP', 'COPY', 'PASTE', 'ADD_FAKE', 'CLEAR_FAKE', 'RENAME', 'SELECT_LINKED']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: id_paste()

   Paste data-blocks from the internal clipboard

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: id_remap(*, id_type='OBJECT', old_id=0, new_id=0)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :param id_type: ID Type, (optional)
   :type id_type: Literal[:ref:`rna_enum_id_type_items`]
   :param old_id: Old ID, Old ID's session uid to remap data from (in [-inf, inf], optional)
   :type old_id: int
   :param new_id: New ID, New ID's session uid to remap all selected IDs' users to (in [-inf, inf], optional)
   :type new_id: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: item_activate(*, extend=False, extend_range=False, deselect_all=False, recurse=False)

   Handle mouse clicks to select and activate items

   :param extend: Extend, Extend selection for activation (optional)
   :type extend: bool
   :param extend_range: Extend Range, Select a range from active element (optional)
   :type extend_range: bool
   :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor (optional)
   :type deselect_all: bool
   :param recurse: Recurse, Select objects recursively from active element (optional)
   :type recurse: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: item_drag_drop()

   Drag and drop element to another place

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: item_openclose(*, all=False)

   Toggle whether item under cursor is open or closed

   :param all: All, Close or open all items (optional)
   :type all: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: item_rename(*, use_active=False)

   Rename the active element

   :param use_active: Use Active, Rename the active item, rather than the one the mouse is over (optional)
   :type use_active: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: keyingset_add_selected()

   Add selected items (blue-gray rows) to active Keying Set

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: keyingset_remove_selected()

   Remove selected items (blue-gray rows) from active Keying Set

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: lib_operation(*, type='DELETE')

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :param type: Library Operation, (optional)

      - ``DELETE``
        Delete -- Delete this library and all its items.
      - ``RELOCATE``
        Relocate -- Select a new path for this library, and reload all its data.
      - ``RELOAD``
        Reload -- Reload all data from this library.
   :type type: Literal['DELETE', 'RELOCATE', 'RELOAD']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: lib_relocate()

   Relocate the library under cursor

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: liboverride_operation(*, type='OVERRIDE_LIBRARY_CREATE_HIERARCHY', selection_set='SELECTED')

   Create, reset or clear library override hierarchies

   :param type: Library Override Operation, (optional)

      - ``OVERRIDE_LIBRARY_CREATE_HIERARCHY``
        Make -- Create a local override of the selected linked data-blocks, and their hierarchy of dependencies.
      - ``OVERRIDE_LIBRARY_RESET``
        Reset -- Reset the selected local overrides to their linked references values.
      - ``OVERRIDE_LIBRARY_CLEAR_SINGLE``
        Clear -- Delete the selected local overrides and relink their usages to the linked data-blocks if possible, else reset them and mark them as non editable.
   :type type: Literal['OVERRIDE_LIBRARY_CREATE_HIERARCHY', 'OVERRIDE_LIBRARY_RESET', 'OVERRIDE_LIBRARY_CLEAR_SINGLE']
   :param selection_set: Selection Set, Over which part of the tree items to apply the operation (optional)

      - ``SELECTED``
        Selected -- Apply the operation over selected data-blocks only.
      - ``CONTENT``
        Content -- Apply the operation over content of the selected items only (the data-blocks in their sub-tree).
      - ``SELECTED_AND_CONTENT``
        Selected & Content -- Apply the operation over selected data-blocks and all their dependencies.
   :type selection_set: Literal['SELECTED', 'CONTENT', 'SELECTED_AND_CONTENT']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: liboverride_troubleshoot_operation(*, type='OVERRIDE_LIBRARY_RESYNC_HIERARCHY', selection_set='SELECTED')

   Advanced operations over library override to help fix broken hierarchies

   :param type: Library Override Troubleshoot Operation, (optional)

      - ``OVERRIDE_LIBRARY_RESYNC_HIERARCHY``
        Resync -- Rebuild the selected local overrides from their linked references, as well as their hierarchies of dependencies.
      - ``OVERRIDE_LIBRARY_RESYNC_HIERARCHY_ENFORCE``
        Resync Enforce -- Rebuild the selected local overrides from their linked references, as well as their hierarchies of dependencies, enforcing these hierarchies to match the linked data (i.e. ignoring existing overrides on data-blocks pointer properties).
      - ``OVERRIDE_LIBRARY_DELETE_HIERARCHY``
        Delete -- Delete the selected local overrides (including their hierarchies of override dependencies) and relink their usages to the linked data-blocks.
   :type type: Literal['OVERRIDE_LIBRARY_RESYNC_HIERARCHY', 'OVERRIDE_LIBRARY_RESYNC_HIERARCHY_ENFORCE', 'OVERRIDE_LIBRARY_DELETE_HIERARCHY']
   :param selection_set: Selection Set, Over which part of the tree items to apply the operation (optional)

      - ``SELECTED``
        Selected -- Apply the operation over selected data-blocks only.
      - ``CONTENT``
        Content -- Apply the operation over content of the selected items only (the data-blocks in their sub-tree).
      - ``SELECTED_AND_CONTENT``
        Selected & Content -- Apply the operation over selected data-blocks and all their dependencies.
   :type selection_set: Literal['SELECTED', 'CONTENT', 'SELECTED_AND_CONTENT']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: material_drop()

   Drag material to object in Outliner

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: modifier_operation(*, type='APPLY')

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :param type: Modifier Operation, (optional)
   :type type: Literal['APPLY', 'DELETE', 'TOGVIS', 'TOGREN']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: object_operation(*, type='SELECT')

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :param type: Object Operation, (optional)

      - ``SELECT``
        Select.
      - ``DESELECT``
        Deselect.
      - ``SELECT_HIERARCHY``
        Select Hierarchy.
      - ``REMAP``
        Remap Users -- Make all users of selected data-blocks to use instead a new chosen one.
      - ``RENAME``
        Rename.
   :type type: Literal['SELECT', 'DESELECT', 'SELECT_HIERARCHY', 'REMAP', 'RENAME']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: operation()

   Context menu for item operations

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: orphans_manage()

   Open a window to manage unused data

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: orphans_purge(*, do_local_ids=True, do_linked_ids=True, do_recursive=True)

   Clear all orphaned data-blocks without any users from the file

   :param do_local_ids: Local Data-blocks, Include unused local data-blocks into deletion (optional)
   :type do_local_ids: bool
   :param do_linked_ids: Linked Data-blocks, Include unused linked data-blocks into deletion (optional)
   :type do_linked_ids: bool
   :param do_recursive: Recursive Delete, Recursively check for indirectly unused data-blocks, ensuring that no orphaned data-blocks remain after execution (optional)
   :type do_recursive: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: parent_clear()

   Drag to clear parent in Outliner

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: parent_drop()

   Drag to parent in Outliner

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: scene_drop()

   Drag object to scene in Outliner

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: scene_operation(*, type='DELETE')

   Context menu for scene operations

   :param type: Scene Operation, (optional)
   :type type: Literal['DELETE']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: scroll_page(*, up=False)

   Scroll page up or down

   :param up: Up, Scroll up one page (optional)
   :type up: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_all(*, action='TOGGLE')

   Toggle the Outliner selection of items

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

   Use box selection to select tree elements

   :param tweak: Tweak, Tweak gesture from empty space for box selection (optional)
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

.. function:: select_walk(*, direction='UP', extend=False, toggle_all=False)

   Use walk navigation to select tree elements

   :param direction: Walk Direction, Select/Deselect element in this direction (optional)
   :type direction: Literal['UP', 'DOWN', 'LEFT', 'RIGHT']
   :param extend: Extend, Extend selection on walk (optional)
   :type extend: bool
   :param toggle_all: Toggle All, Toggle open/close hierarchy (optional)
   :type toggle_all: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: show_active()

   Open up the tree and adjust the view so that the active object is shown centered

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: show_hierarchy()

   Open all object entries and close all others

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: show_one_level(*, open=True)

   Expand/collapse all entries by one level

   :param open: Open, Expand all entries one level deep (optional)
   :type open: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: start_filter()

   Start entering filter text

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: unhide_all()

   Unhide all objects and collections

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
