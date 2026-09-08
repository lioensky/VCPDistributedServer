Action Operators
================

.. module:: bpy.ops.action

.. function:: bake_keys()

   Add keyframes on every frame between the selected keyframes

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: clean(*, threshold=0.001, channels=False)

   Simplify F-Curves by removing closely spaced keyframes

   :param threshold: Threshold, (in [0, inf], optional)
   :type threshold: float
   :param channels: Channels, (optional)
   :type channels: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: clickselect(*, wait_to_deselect_others=False, use_select_on_click=False, mouse_x=0, mouse_y=0, extend=False, deselect_all=False, column=False, channel=False)

   Select keyframes by clicking on them

   :param wait_to_deselect_others: Wait to Deselect Others, (optional)
   :type wait_to_deselect_others: bool
   :param use_select_on_click: Act on Click, Instead of selecting on mouse press, wait to see if there's drag event. Otherwise select on mouse release (optional)
   :type use_select_on_click: bool
   :param mouse_x: Mouse X, (in [-inf, inf], optional)
   :type mouse_x: int
   :param mouse_y: Mouse Y, (in [-inf, inf], optional)
   :type mouse_y: int
   :param extend: Extend Select, Toggle keyframe selection instead of leaving newly selected keyframes only (optional)
   :type extend: bool
   :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor (optional)
   :type deselect_all: bool
   :param column: Column Select, Select all keyframes that occur on the same frame as the one under the mouse (optional)
   :type column: bool
   :param channel: Only Channel, Select all the keyframes in the channel under the mouse (optional)
   :type channel: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: copy()

   Copy selected keyframes to the internal clipboard

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: delete(*, confirm=True)

   Remove all selected keyframes

   :param confirm: Confirm, Prompt for confirmation (optional)
   :type confirm: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: duplicate()

   Make a copy of all selected keyframes

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: duplicate_move(*, ACTION_OT_duplicate={}, TRANSFORM_OT_transform={})

   Make a copy of all selected keyframes and move them

   :param ACTION_OT_duplicate: Duplicate Keyframes, Make a copy of all selected keyframes (optional, :func:`bpy.ops.action.duplicate` keyword arguments)
   :type ACTION_OT_duplicate: dict[str, Any]
   :param TRANSFORM_OT_transform: Transform, Transform selected items by mode type (optional, :func:`bpy.ops.transform.transform` keyword arguments)
   :type TRANSFORM_OT_transform: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: easing_type(*, type='AUTO')

   Set easing type for the F-Curve segments starting from the selected keyframes

   :param type: Type, (optional)
   :type type: Literal[:ref:`rna_enum_beztriple_interpolation_easing_items`]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: extrapolation_type(*, type='CONSTANT')

   Set extrapolation mode for selected F-Curves

   :param type: Type, (optional)

      - ``CONSTANT``
        Constant Extrapolation -- Values on endpoint keyframes are held.
      - ``LINEAR``
        Linear Extrapolation -- Straight-line slope of end segments are extended past the endpoint keyframes.
      - ``MAKE_CYCLIC``
        Make Cyclic (F-Modifier) -- Add Cycles F-Modifier if one does not exist already.
      - ``CLEAR_CYCLIC``
        Clear Cyclic (F-Modifier) -- Remove Cycles F-Modifier if not needed anymore.
   :type type: Literal['CONSTANT', 'LINEAR', 'MAKE_CYCLIC', 'CLEAR_CYCLIC']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: frame_jump()

   Set the current frame to the average frame value of selected keyframes

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: handle_type(*, type='FREE')

   Set type of handle for selected keyframes

   :param type: Type, (optional)
   :type type: Literal[:ref:`rna_enum_keyframe_handle_type_items`]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: interpolation_type(*, type='CONSTANT')

   Set interpolation mode for the F-Curve segments starting from the selected keyframes

   :param type: Type, (optional)
   :type type: Literal[:ref:`rna_enum_beztriple_interpolation_mode_items`]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: keyframe_insert(*, type='ALL')

   Insert keyframes for the specified channels

   :param type: Type, (optional)
   :type type: Literal['ALL', 'SEL', 'GROUP']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: keyframe_type(*, type='KEYFRAME')

   Set type of keyframe for the selected keyframes

   :param type: Type, (optional)
   :type type: Literal[:ref:`rna_enum_beztriple_keyframe_type_items`]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: markers_make_local()

   Move selected scene markers to the active Action as local 'pose' markers

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: mirror(*, type='CFRA')

   Flip selected keyframes over the selected mirror line

   :param type: Type, (optional)

      - ``CFRA``
        By Times Over Current Frame -- Flip times of selected keyframes using the current frame as the mirror line.
      - ``XAXIS``
        By Values Over Zero Value -- Flip values of selected keyframes (i.e. negative values become positive, and vice versa).
      - ``MARKER``
        By Times Over First Selected Marker -- Flip times of selected keyframes using the first selected marker as the reference point.
   :type type: Literal['CFRA', 'XAXIS', 'MARKER']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: new()

   Create new action

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: paste(*, offset='START', merge='MIX', flipped=False)

   Paste keyframes from the internal clipboard for the selected channels, starting on the current frame

   :param offset: Offset, Paste time offset of keys (optional)
   :type offset: Literal[:ref:`rna_enum_keyframe_paste_offset_items`]
   :param merge: Type, Method of merging pasted keys and existing (optional)
   :type merge: Literal[:ref:`rna_enum_keyframe_paste_merge_items`]
   :param flipped: Flipped, Paste keyframes from mirrored bones if they exist (optional)
   :type flipped: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: previewrange_set()

   Set Preview Range based on extents of selected Keyframes

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: push_down()

   Push action down on to the NLA stack as a new strip

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select_all(*, action='TOGGLE')

   Toggle selection of all keyframes

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

.. function:: select_box(*, axis_range=False, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, mode='SET', tweak=False)

   Select all keyframes within the specified region

   :param axis_range: Axis Range, (optional)
   :type axis_range: bool
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
   :param tweak: Tweak, Operator has been activated using a click-drag event (optional)
   :type tweak: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_circle(*, x=0, y=0, radius=25, wait_for_input=True, mode='SET')

   Select keyframe points using circle selection

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

.. function:: select_column(*, mode='KEYS')

   Select all keyframes on the specified frame(s)

   :param mode: Mode, (optional)
   :type mode: Literal['KEYS', 'CFRA', 'MARKERS_COLUMN', 'MARKERS_BETWEEN']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_lasso(*, path=None, use_smooth_stroke=False, smooth_stroke_factor=0.75, smooth_stroke_radius=35, mode='SET')

   Select keyframe points using lasso selection

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

.. function:: select_leftright(*, mode='CHECK', extend=False)

   Select keyframes to the left or the right of the current frame

   :param mode: Mode, (optional)
   :type mode: Literal['CHECK', 'LEFT', 'RIGHT']
   :param extend: Extend Select, (optional)
   :type extend: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_less()

   Deselect keyframes on ends of selection islands

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select_linked()

   Select keyframes occurring in the same F-Curves as selected ones

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select_more()

   Select keyframes beside already selected ones

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: snap(*, type='CFRA')

   Snap selected keyframes to the times specified

   :param type: Type, (optional)

      - ``CFRA``
        Selection to Current Frame -- Snap selected keyframes to the current frame.
      - ``NEAREST_FRAME``
        Selection to Nearest Frame -- Snap selected keyframes to the nearest (whole) frame (use to fix accidental subframe offsets).
      - ``NEAREST_SECOND``
        Selection to Nearest Second -- Snap selected keyframes to the nearest second.
      - ``NEAREST_MARKER``
        Selection to Nearest Marker -- Snap selected keyframes to the nearest marker.
   :type type: Literal['CFRA', 'NEAREST_FRAME', 'NEAREST_SECOND', 'NEAREST_MARKER']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: stash(*, create_new=True)

   Store this action in the NLA stack as a non-contributing strip for later use

   :param create_new: Create New Action, Create a new action once the existing one has been safely stored (optional)
   :type create_new: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: stash_and_create()

   Store this action in the NLA stack as a non-contributing strip for later use, and create a new action

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: unlink(*, force_delete=False)

   Unlink this action from the active action slot (and/or exit Tweak Mode)

   :param force_delete: Force Delete, Clear Fake User and remove copy stashed in this data-block's NLA stack (optional)
   :type force_delete: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: view_all()

   Reset viewable area to show full keyframe range

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: view_frame()

   Move the view to the current frame

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: view_selected()

   Reset viewable area to show selected keyframes range

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
