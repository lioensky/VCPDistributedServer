Anim Operators
==============

.. module:: bpy.ops.anim

.. function:: change_frame(*, frame=0.0, snap=False, seq_solo_preview=False, pass_through_on_strip_handles=False)

   Interactively change the current frame number

   :param frame: Frame, (in [-1.04857e+06, 1.04857e+06], optional)
   :type frame: float
   :param snap: Snap, (optional)
   :type snap: bool
   :param seq_solo_preview: Strip Preview, (optional)
   :type seq_solo_preview: bool
   :param pass_through_on_strip_handles: Pass Through on Strip Handles, Allow another operator to operate on strip handles (optional)
   :type pass_through_on_strip_handles: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: channel_select_keys(*, extend=False)

   Select all keyframes of channel under mouse

   :param extend: Extend, Extend selection (optional)
   :type extend: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: channel_view_pick(*, include_handles=True, use_preview_range=True)

   Reset viewable area to show the channel under the cursor

   :param include_handles: Include Handles, Include handles of keyframes when calculating extents (optional)
   :type include_handles: bool
   :param use_preview_range: Use Preview Range, Ignore frames outside of the preview range (optional)
   :type use_preview_range: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: channels_bake(*, use_scene_range=True, range=(0, 0), step=1.0, remove_outside_range=False, interpolation_type='BEZIER', bake_modifiers=True)

   Create keyframes following the current shape of F-Curves of selected channels

   :param use_scene_range: Use Scene Range, If enabled, the scene start and end frame will be used to determine the bake range (optional)
   :type use_scene_range: bool
   :param range: Frame Range, The custom range in which to create new keys. Only used when not using the scene range (array of 2 items, in [-inf, inf], optional)
   :type range: Sequence[int]
   :param step: Frame Step, At which interval to add keys (in [0.01, inf], optional)
   :type step: float
   :param remove_outside_range: Remove Outside Range, Removes keys outside the given range, leaving only the newly baked (optional)
   :type remove_outside_range: bool
   :param interpolation_type: Interpolation Type, Choose the interpolation type with which new keys will be added (optional)

      - ``BEZIER``
        Bézier -- New keys will be Bézier.
      - ``LIN``
        Linear -- New keys will be linear.
      - ``CONST``
        Constant -- New keys will be constant.
   :type interpolation_type: Literal['BEZIER', 'LIN', 'CONST']
   :param bake_modifiers: Bake Modifiers, Bake Modifiers into keyframes and delete them after (optional)
   :type bake_modifiers: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: channels_clean_empty()

   Delete all empty animation data containers from visible data-blocks

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: channels_click(*, extend=False, extend_range=False, children_only=False)

   Handle mouse clicks over animation channels

   :param extend: Extend Select, (optional)
   :type extend: bool
   :param extend_range: Extend Range, Selection of active channel to clicked channel (optional)
   :type extend_range: bool
   :param children_only: Select Children Only, (optional)
   :type children_only: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: channels_collapse(*, all=True)

   Collapse (close) all selected expandable animation channels

   :param all: All, Collapse all channels (not just selected ones) (optional)
   :type all: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: channels_delete()

   Delete all selected animation channels

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: channels_editable_toggle(*, mode='TOGGLE', type='PROTECT')

   Toggle editability of selected channels

   :param mode: Mode, (optional)
   :type mode: Literal['TOGGLE', 'DISABLE', 'ENABLE', 'INVERT']
   :param type: Type, (optional)
   :type type: Literal['PROTECT', 'MUTE']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: channels_expand(*, all=True)

   Expand (open) all selected expandable animation channels

   :param all: All, Expand all channels (not just selected ones) (optional)
   :type all: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: channels_fcurves_enable()

   Clear 'disabled' tag from all F-Curves to get broken F-Curves working again

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: channels_group(*, name="")

   Add selected F-Curves to a new group

   :param name: Name, Name of newly created group (optional, never None)
   :type name: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: channels_move(*, direction='DOWN')

   Rearrange selected animation channels

   :param direction: Direction, (optional)
   :type direction: Literal['TOP', 'UP', 'DOWN', 'BOTTOM']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: channels_rename()

   Rename animation channel under mouse

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: channels_select_all(*, action='TOGGLE')

   Toggle selection of all animation channels

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

.. function:: channels_select_box(*, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, deselect=False, extend=True)

   Select all animation channels within the specified region

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
   :param deselect: Deselect, Deselect rather than select items (optional)
   :type deselect: bool
   :param extend: Extend, Extend selection instead of deselecting everything first (optional)
   :type extend: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: channels_select_filter()

   Start entering text which filters the set of channels shown to only include those with matching names

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: channels_setting_disable(*, mode='DISABLE', type='PROTECT')

   Disable specified setting on all selected animation channels

   :param mode: Mode, (optional)
   :type mode: Literal['TOGGLE', 'DISABLE', 'ENABLE', 'INVERT']
   :param type: Type, (optional)
   :type type: Literal['PROTECT', 'MUTE']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: channels_setting_enable(*, mode='ENABLE', type='PROTECT')

   Enable specified setting on all selected animation channels

   :param mode: Mode, (optional)
   :type mode: Literal['TOGGLE', 'DISABLE', 'ENABLE', 'INVERT']
   :param type: Type, (optional)
   :type type: Literal['PROTECT', 'MUTE']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: channels_setting_toggle(*, mode='TOGGLE', type='PROTECT')

   Toggle specified setting on all selected animation channels

   :param mode: Mode, (optional)
   :type mode: Literal['TOGGLE', 'DISABLE', 'ENABLE', 'INVERT']
   :param type: Type, (optional)
   :type type: Literal['PROTECT', 'MUTE']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: channels_ungroup()

   Remove selected F-Curves from their current groups

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: channels_view_selected(*, include_handles=True, use_preview_range=True)

   Reset viewable area to show the selected channels

   :param include_handles: Include Handles, Include handles of keyframes when calculating extents (optional)
   :type include_handles: bool
   :param use_preview_range: Use Preview Range, Ignore frames outside of the preview range (optional)
   :type use_preview_range: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: clear_useless_actions(*, only_unused=True)

   Mark actions with no F-Curves for deletion after save and reload of file preserving "action libraries"

   :param only_unused: Only Unused, Only unused (Fake User only) actions get considered (optional)
   :type only_unused: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/anim.py\:365 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/anim.py#L365>`__


.. function:: copy_driver_button()

   Copy the driver for the highlighted button

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: debug_channel_list()

   Log the channel list info in the terminal. This operator is only available in debug builds of Blender

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: driver_button_add()

   Add driver for the property under the cursor

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: driver_button_edit()

   Edit the drivers for the connected property represented by the highlighted button

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: driver_button_remove(*, all=True)

   Remove the driver(s) for the connected property(s) represented by the highlighted button

   :param all: All, Delete drivers for all elements of the array (optional)
   :type all: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: end_frame_set()

   Set the current frame as the preview or scene end frame

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: keyframe_clear_button(*, all=True)

   Clear all keyframes on the currently active property

   :param all: All, Clear keyframes from all elements of the array (optional)
   :type all: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: keyframe_clear_v3d(*, confirm=True)

   Remove all keyframe animation for selected objects

   :param confirm: Confirm, Prompt for confirmation (optional)
   :type confirm: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: keyframe_clear_vse(*, confirm=True)

   Remove all keyframe animation for selected strips

   :param confirm: Confirm, Prompt for confirmation (optional)
   :type confirm: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: keyframe_delete(*, type='DEFAULT')

   Delete keyframes on the current frame for all properties in the specified Keying Set

   :param type: Keying Set, The Keying Set to use (optional)
   :type type: Literal['DEFAULT']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: keyframe_delete_button(*, all=True)

   Delete current keyframe of current UI-active property

   :param all: All, Delete keyframes from all elements of the array (optional)
   :type all: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: keyframe_delete_by_name(*, type="")

   Alternate access to 'Delete Keyframe' for keymaps to use

   :param type: Keying Set, The Keying Set to use (optional, never None)
   :type type: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: keyframe_delete_v3d(*, confirm=True)

   Remove keyframes on current frame for selected objects and bones

   :param confirm: Confirm, Prompt for confirmation (optional)
   :type confirm: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: keyframe_delete_vse(*, confirm=True)

   Remove keyframes on current frame for selected strips

   :param confirm: Confirm, Prompt for confirmation (optional)
   :type confirm: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: keyframe_insert(*, type='DEFAULT')

   Insert keyframes on the current frame using either the active keying set, or the user preferences if no keying set is active

   :param type: Keying Set, The Keying Set to use (optional)
   :type type: Literal['DEFAULT']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: keyframe_insert_button(*, all=True)

   Insert a keyframe for current UI-active property

   :param all: All, Insert a keyframe for all element of the array (optional)
   :type all: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: keyframe_insert_by_name(*, type="")

   Alternate access to 'Insert Keyframe' for keymaps to use

   :param type: Keying Set, The Keying Set to use (optional, never None)
   :type type: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: keyframe_insert_menu(*, type='DEFAULT', always_prompt=False)

   Insert Keyframes for specified Keying Set, with menu of available Keying Sets if undefined

   :param type: Keying Set, The Keying Set to use (optional)
   :type type: Literal['DEFAULT']
   :param always_prompt: Always Show Menu, (optional)
   :type always_prompt: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: keying_set_active_set(*, type='DEFAULT')

   Set a new active keying set

   :param type: Keying Set, The Keying Set to use (optional)
   :type type: Literal['DEFAULT']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: keying_set_add()

   Add a new (empty) keying set to the active Scene

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: keying_set_export(*, filepath="", filter_folder=True, filter_text=True, filter_python=True)

   Export Keying Set to a Python script

   :param filepath: filepath, (optional, never None)
   :type filepath: str
   :param filter_folder: Filter folders, (optional)
   :type filter_folder: bool
   :param filter_text: Filter text, (optional)
   :type filter_text: bool
   :param filter_python: Filter Python, (optional)
   :type filter_python: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/anim.py\:46 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/anim.py#L46>`__


.. function:: keying_set_path_add()

   Add empty path to active keying set

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: keying_set_path_remove()

   Remove active Path from active keying set

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: keying_set_remove()

   Remove the active keying set

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: keyingset_button_add(*, all=True)

   Add current UI-active property to current keying set

   :param all: All, Add all elements of the array to a Keying Set (optional)
   :type all: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: keyingset_button_remove()

   Remove current UI-active property from current keying set

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: merge_animation()

   Merge the animation of the selected objects into the action of the active object. Actions are not deleted by this, but might end up with zero users

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: paste_driver_button()

   Paste the driver in the internal clipboard to the highlighted button

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: previewrange_clear()

   Clear preview range

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: previewrange_set(*, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True)

   Interactively define frame range used for playback

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

.. function:: replace_action(*, old_session_uid=0, new_session_uid=0)

   Swap all users of one action to another one. The normal action slot assignment rules apply. This ignores the NLA and Action Constraints

   :param old_session_uid: Old Action, Old Action's session uid to replace (in [-inf, inf], optional)
   :type old_session_uid: int
   :param new_session_uid: Replacement Action, The replacement Action's session uid to remap all selected Action's users to (in [-inf, inf], optional)
   :type new_session_uid: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: replace_action_new(*, old_session_uid=0)

   Swap all users of one action to a new action. This ignores the NLA and Action Constraints

   :param old_session_uid: Old Action, Old Action's session uid to replace (in [-inf, inf], optional)
   :type old_session_uid: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: scene_range_frame()

   Reset the horizontal view to the current scene frame range, taking the preview range into account if it is active

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: separate_slots()

   Move all slots of the action on the active object into newly created, separate actions. All users of those slots will be reassigned to the new actions. The current action won't be deleted but will be empty and might end up having zero users

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: slot_channels_move_to_new_action()

   Move the selected slots into a newly created action

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: slot_new_for_id()

   Create a new action slot for this data-block, to hold its animation

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/anim.py\:721 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/anim.py#L721>`__

.. function:: slot_unassign_from_constraint()

   Un-assign the action slot from this constraint

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/anim.py\:779 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/anim.py#L779>`__

.. function:: slot_unassign_from_id()

   Un-assign the action slot, effectively making this data-block non-animated

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/anim.py\:758 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/anim.py#L758>`__

.. function:: slot_unassign_from_nla_strip()

   Un-assign the action slot from this NLA strip, effectively making it non-animated

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/anim.py\:779 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/anim.py#L779>`__

.. function:: start_frame_set()

   Set the current frame as the preview or scene start frame

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: update_animated_transform_constraints(*, use_convert_to_radians=True)

   Update f-curves/drivers affecting Transform constraints (use it with files from 2.70 and earlier)

   :param use_convert_to_radians: Convert to Radians, Convert f-curves/drivers affecting rotations to radians.Warning: Use this only once(optional)
   :type use_convert_to_radians: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/anim.py\:402 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/anim.py#L402>`__


.. function:: version_bone_hide_property()

   Moves any F-Curves for the `hide` property of selected armatures into the action of the object. This will only operate on the first layer and strip of the action

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/anim.py\:842 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/anim.py#L842>`__

.. function:: view_curve_in_graph_editor(*, all=False, isolate=False)

   Frame the property under the cursor in the Graph Editor

   :param all: Show All, Frame the whole array property instead of only the index under the cursor (optional)
   :type all: bool
   :param isolate: Isolate, Hides all F-Curves other than the ones being framed (optional)
   :type isolate: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

