Nla Operators
=============

.. module:: bpy.ops.nla

.. function:: action_pushdown(*, track_index=-1)

   Push action down onto the top of the NLA stack as a new strip

   :param track_index: Track Index, Index of NLA action track to perform pushdown operation on (in [-1, inf], optional)
   :type track_index: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: action_sync_length(*, active=True)

   Synchronize the length of the referenced Action with the length used in the strip

   :param active: Active Strip Only, Only sync the active length for the active strip (optional)
   :type active: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: action_unlink(*, force_delete=False)

   Unlink this action from the active action slot (and/or exit Tweak Mode)

   :param force_delete: Force Delete, Clear Fake User and remove copy stashed in this data-block's NLA stack (optional)
   :type force_delete: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: actionclip_add(*, action='')

   Add an Action-Clip strip (i.e. an NLA Strip referencing an Action) to the active track

   :param action: Action, (optional)
   :type action: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: apply_scale()

   Apply scaling of selected strips to their referenced Actions

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: bake(*, frame_start=1, frame_end=250, step=1, only_selected=True, visual_keying=False, clear_constraints=False, clear_parents=False, use_current_action=False, clean_curves=False, bake_types={'POSE'}, channel_types={'BBONE', 'LOCATION', 'PROPS', 'ROTATION', 'SCALE'})

   Bake all selected objects location/scale/rotation animation to an action

   :param frame_start: Start Frame, Start frame for baking (in [0, 300000], optional)
   :type frame_start: int
   :param frame_end: End Frame, End frame for baking (in [1, 300000], optional)
   :type frame_end: int
   :param step: Frame Step, Number of frames to skip forward while baking each frame (in [1, 120], optional)
   :type step: int
   :param only_selected: Only Selected Bones, Only key selected bones (Pose baking only) (optional)
   :type only_selected: bool
   :param visual_keying: Visual Keying, Keyframe from the final transformations (with constraints applied) (optional)
   :type visual_keying: bool
   :param clear_constraints: Clear Local Constraints, Remove all constraints from keyed object/bones. To get a correct bake with this setting Visual Keying should be enabled (optional)
   :type clear_constraints: bool
   :param clear_parents: Clear Parents, Bake animation onto the object then clear parents (objects only) (optional)
   :type clear_parents: bool
   :param use_current_action: Overwrite Current Action, Bake animation into current action, instead of creating a new one (useful for baking only part of bones in an armature) (optional)
   :type use_current_action: bool
   :param clean_curves: Clean Curves, After baking curves, remove redundant keys (optional)
   :type clean_curves: bool
   :param bake_types: Bake Data, Which data's transformations to bake (optional)

      - ``POSE``
        Pose -- Bake bones transformations.
      - ``OBJECT``
        Object -- Bake object transformations.
   :type bake_types: set[Literal['POSE', 'OBJECT']]
   :param channel_types: Channels, Which channels to bake (optional)

      - ``LOCATION``
        Location -- Bake location channels.
      - ``ROTATION``
        Rotation -- Bake rotation channels.
      - ``SCALE``
        Scale -- Bake scale channels.
      - ``BBONE``
        B-Bone -- Bake B-Bone channels.
      - ``PROPS``
        Custom Properties -- Bake custom properties.
   :type channel_types: set[Literal['LOCATION', 'ROTATION', 'SCALE', 'BBONE', 'PROPS']]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/anim.py\:274 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/anim.py#L274>`__


.. function:: channels_click(*, extend=False)

   Handle clicks to select NLA tracks

   :param extend: Extend Select, (optional)
   :type extend: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: clear_scale()

   Reset scaling of selected strips

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: click_select(*, wait_to_deselect_others=False, use_select_on_click=False, mouse_x=0, mouse_y=0, extend=False, deselect_all=False)

   Handle clicks to select NLA Strips

   :param wait_to_deselect_others: Wait to Deselect Others, (optional)
   :type wait_to_deselect_others: bool
   :param use_select_on_click: Act on Click, Instead of selecting on mouse press, wait to see if there's drag event. Otherwise select on mouse release (optional)
   :type use_select_on_click: bool
   :param mouse_x: Mouse X, (in [-inf, inf], optional)
   :type mouse_x: int
   :param mouse_y: Mouse Y, (in [-inf, inf], optional)
   :type mouse_y: int
   :param extend: Extend Select, (optional)
   :type extend: bool
   :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor (optional)
   :type deselect_all: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: delete()

   Delete selected strips

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: duplicate(*, linked=False)

   Duplicate selected NLA-Strips, adding the new strips to new track(s)

   :param linked: Linked, When duplicating strips, assign new copies of the actions they use (optional)
   :type linked: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: duplicate_linked_move(*, NLA_OT_duplicate={}, TRANSFORM_OT_translate={})

   Duplicate Linked selected NLA-Strips, adding the new strips to new track(s)

   :param NLA_OT_duplicate: Duplicate Strips, Duplicate selected NLA-Strips, adding the new strips to new track(s) (optional, :func:`bpy.ops.nla.duplicate` keyword arguments)
   :type NLA_OT_duplicate: dict[str, Any]
   :param TRANSFORM_OT_translate: Move, Move selected items (optional, :func:`bpy.ops.transform.translate` keyword arguments)
   :type TRANSFORM_OT_translate: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: duplicate_move(*, NLA_OT_duplicate={}, TRANSFORM_OT_translate={})

   Duplicate selected NLA-Strips, adding the new strips to new track(s)

   :param NLA_OT_duplicate: Duplicate Strips, Duplicate selected NLA-Strips, adding the new strips to new track(s) (optional, :func:`bpy.ops.nla.duplicate` keyword arguments)
   :type NLA_OT_duplicate: dict[str, Any]
   :param TRANSFORM_OT_translate: Move, Move selected items (optional, :func:`bpy.ops.transform.translate` keyword arguments)
   :type TRANSFORM_OT_translate: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: fmodifier_add(*, type='NULL', only_active=True)

   Add F-Modifier to the active/selected NLA-Strips

   :param type: Type, (optional)
   :type type: Literal[:ref:`rna_enum_fmodifier_type_items`]
   :param only_active: Only Active, Only add a F-Modifier of the specified type to the active strip (optional)
   :type only_active: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: fmodifier_copy()

   Copy the F-Modifier(s) of the active NLA-Strip

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: fmodifier_paste(*, only_active=True, replace=False)

   Add copied F-Modifiers to the selected NLA-Strips

   :param only_active: Only Active, Only paste F-Modifiers on active strip (optional)
   :type only_active: bool
   :param replace: Replace Existing, Replace existing F-Modifiers, instead of just appending to the end of the existing list (optional)
   :type replace: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: make_single_user(*, confirm=True)

   Make linked action local to each strip

   :param confirm: Confirm, Prompt for confirmation (optional)
   :type confirm: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: meta_add()

   Add new meta-strips incorporating the selected strips

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: meta_remove()

   Separate out the strips held by the selected meta-strips

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: move_down()

   Move selected strips down a track if there's room

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: move_up()

   Move selected strips up a track if there's room

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: mute_toggle()

   Mute or un-mute selected strips

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: previewrange_set()

   Set Preview Range based on extents of selected strips

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select_all(*, action='TOGGLE')

   Select or deselect all NLA-Strips

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

.. function:: select_box(*, axis_range=False, tweak=False, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, mode='SET')

   Use box selection to grab NLA-Strips

   :param axis_range: Axis Range, (optional)
   :type axis_range: bool
   :param tweak: Tweak, Operator has been activated using a click-drag event (optional)
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

.. function:: select_leftright(*, mode='CHECK', extend=False)

   Select strips to the left or the right of the current frame

   :param mode: Mode, (optional)
   :type mode: Literal['CHECK', 'LEFT', 'RIGHT']
   :param extend: Extend Select, (optional)
   :type extend: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: selected_objects_add()

   Make selected objects appear in NLA Editor by adding Animation Data

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: snap(*, type='CFRA')

   Move start of strips to specified time

   :param type: Type, (optional)
   :type type: Literal['CFRA', 'NEAREST_FRAME', 'NEAREST_SECOND', 'NEAREST_MARKER']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: soundclip_add()

   Add a strip for controlling when speaker plays its sound clip

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: split()

   Split selected strips at their midpoints

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: swap()

   Swap order of selected strips within tracks

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: tracks_add(*, above_selected=False)

   Add NLA-Tracks above/after the selected tracks

   :param above_selected: Above Selected, Add a new NLA Track above every existing selected one (optional)
   :type above_selected: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: tracks_delete()

   Delete selected NLA-Tracks and the strips they contain

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: transition_add()

   Add a transition strip between two adjacent selected strips

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: tweakmode_enter(*, isolate_action=False, use_upper_stack_evaluation=False)

   Enter tweaking mode for the action referenced by the active strip to edit its keyframes

   :param isolate_action: Isolate Action, Enable 'solo' on the NLA Track containing the active strip, to edit it without seeing the effects of the NLA stack (optional)
   :type isolate_action: bool
   :param use_upper_stack_evaluation: Evaluate Upper Stack, In tweak mode, display the effects of the tracks above the tweak strip (optional)
   :type use_upper_stack_evaluation: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: tweakmode_exit(*, isolate_action=False)

   Exit tweaking mode for the action referenced by the active strip

   :param isolate_action: Isolate Action, Disable 'solo' on any of the NLA Tracks after exiting tweak mode to get things back to normal (optional)
   :type isolate_action: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: view_all()

   Reset viewable area to show full strips range

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: view_frame()

   Move the view to the current frame

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: view_selected()

   Reset viewable area to show selected strips range

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
