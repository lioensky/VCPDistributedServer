Graph Operators
===============

.. module:: bpy.ops.graph

.. function:: bake_keys()

   Add keyframes on every frame between the selected keyframes

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: blend_offset(*, factor=0.0)

   Shift selected keys to the value of the neighboring keys as a block

   :param factor: Offset Factor, Control which key to offset towards and how far (in [-inf, inf], optional)
   :type factor: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: blend_to_default(*, factor=0.0)

   Blend selected keys to their default value from their current position

   :param factor: Factor, How much to blend to the default value (in [-inf, inf], optional)
   :type factor: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: blend_to_ease(*, factor=0.0)

   Blends keyframes from current state to an ease-in or ease-out curve

   :param factor: Blend, Favor either original data or ease curve (in [-inf, inf], optional)
   :type factor: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: blend_to_neighbor(*, factor=0.0)

   Blend selected keyframes to their left or right neighbor

   :param factor: Blend, The blend factor with 0 being the current frame (in [-inf, inf], optional)
   :type factor: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: breakdown(*, factor=0.0)

   Move selected keyframes to an inbetween position relative to adjacent keys

   :param factor: Factor, Favor either the left or the right key (in [-inf, inf], optional)
   :type factor: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: butterworth_smooth(*, cutoff_frequency=3.0, filter_order=4, samples_per_frame=1, blend=1.0, blend_in_out=1)

   Smooth an F-Curve while maintaining the general shape of the curve

   :param cutoff_frequency: Frequency Cutoff (Hz), Lower values give a smoother curve (in [0, inf], optional)
   :type cutoff_frequency: float
   :param filter_order: Filter Order, Higher values produce a harder frequency cutoff (in [1, 32], optional)
   :type filter_order: int
   :param samples_per_frame: Samples per Frame, How many samples to calculate per frame, helps with subframe data (in [1, 64], optional)
   :type samples_per_frame: int
   :param blend: Blend, How much to blend to the smoothed curve (in [0, inf], optional)
   :type blend: float
   :param blend_in_out: Blend In/Out, Linearly blend the smooth data to the border frames of the selection (in [0, inf], optional)
   :type blend_in_out: int
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

.. function:: click_insert(*, frame=1.0, value=1.0, extend=False)

   Insert new keyframe at the cursor position for the active F-Curve

   :param frame: Frame Number, Frame to insert keyframe on (in [-inf, inf], optional)
   :type frame: float
   :param value: Value, Value for keyframe on (in [-inf, inf], optional)
   :type value: float
   :param extend: Extend, Extend selection instead of deselecting everything first (optional)
   :type extend: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: clickselect(*, wait_to_deselect_others=False, use_select_on_click=False, mouse_x=0, mouse_y=0, extend=False, deselect_all=False, column=False, curves=False)

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
   :param curves: Only Curves, Select all the keyframes in the curve (optional)
   :type curves: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: copy()

   Copy selected keyframes to the internal clipboard

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: cursor_set(*, frame=0.0, value=0.0)

   Interactively set the current frame and value cursor

   :param frame: Frame, (in [-1.04857e+06, 1.04857e+06], optional)
   :type frame: float
   :param value: Value, (in [-inf, inf], optional)
   :type value: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: decimate(*, mode='RATIO', factor=0.333333, remove_error_margin=0.0)

   Decimate F-Curves by removing keyframes that influence the curve shape the least

   :param mode: Mode, Which mode to use for decimation (optional)

      - ``RATIO``
        Ratio -- Use a percentage to specify how many keyframes you want to remove.
      - ``ERROR``
        Error Margin -- Use an error margin to specify how much the curve is allowed to deviate from the original path.
   :type mode: Literal['RATIO', 'ERROR']
   :param factor: Factor, The ratio of keyframes to remove (in [0, 1], optional)
   :type factor: float
   :param remove_error_margin: Max Error Margin, How much the new decimated curve is allowed to deviate from the original (in [0, inf], optional)
   :type remove_error_margin: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: delete(*, confirm=True)

   Remove all selected keyframes

   :param confirm: Confirm, Prompt for confirmation (optional)
   :type confirm: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: driver_delete_invalid()

   Delete all visible drivers considered invalid

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: driver_variables_copy()

   Copy the driver variables of the active driver

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: driver_variables_paste(*, replace=False)

   Add copied driver variables to the active driver

   :param replace: Replace Existing, Replace existing driver variables, instead of just appending to the end of the existing list (optional)
   :type replace: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: duplicate(*, mode='TRANSLATION')

   Make a copy of all selected keyframes

   :param mode: Mode, (optional)
   :type mode: Literal[:ref:`rna_enum_transform_mode_type_items`]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: duplicate_move(*, GRAPH_OT_duplicate={}, TRANSFORM_OT_translate={})

   Make a copy of all selected keyframes and move them

   :param GRAPH_OT_duplicate: Duplicate Keyframes, Make a copy of all selected keyframes (optional, :func:`bpy.ops.graph.duplicate` keyword arguments)
   :type GRAPH_OT_duplicate: dict[str, Any]
   :param TRANSFORM_OT_translate: Move, Move selected items (optional, :func:`bpy.ops.transform.translate` keyword arguments)
   :type TRANSFORM_OT_translate: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: ease(*, factor=0.0, sharpness=2.0)

   Align keyframes on a ease-in or ease-out curve

   :param factor: Curve Bend, Defines if the keys should be aligned on an ease-in or ease-out curve (in [-inf, inf], optional)
   :type factor: float
   :param sharpness: Sharpness, Higher values make the change more abrupt (in [0.001, inf], optional)
   :type sharpness: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: easing_type(*, type='AUTO')

   Set easing type for the F-Curve segments starting from the selected keyframes

   :param type: Type, (optional)
   :type type: Literal[:ref:`rna_enum_beztriple_interpolation_easing_items`]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: equalize_handles(*, side='LEFT', handle_length=5.0, flatten=False)

   Ensure selected keyframes' handles have equal length, optionally making them horizontal. Automatic, Automatic Clamped, or Vector handle types will be converted to Aligned

   :param side: Side, Side of the keyframes' Bézier handles to affect (optional)

      - ``LEFT``
        Left -- Equalize selected keyframes' left handles.
      - ``RIGHT``
        Right -- Equalize selected keyframes' right handles.
      - ``BOTH``
        Both -- Equalize both of a keyframe's handles.
   :type side: Literal['LEFT', 'RIGHT', 'BOTH']
   :param handle_length: Handle Length, Length to make selected keyframes' Bézier handles (in [0.1, inf], optional)
   :type handle_length: float
   :param flatten: Flatten, Make the values of the selected keyframes' handles the same as their respective keyframes (optional)
   :type flatten: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: euler_filter()

   Fix large jumps and flips in the selected Euler Rotation F-Curves arising from rotation values being clipped when baking physics

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

.. function:: fmodifier_add(*, type='NULL', only_active=False)

   Add F-Modifier to the active/selected F-Curves

   :param type: Type, (optional)
   :type type: Literal[:ref:`rna_enum_fmodifier_type_items`]
   :param only_active: Only Active, Only add F-Modifier to active F-Curve (optional)
   :type only_active: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: fmodifier_copy()

   Copy the F-Modifier(s) of the active F-Curve

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: fmodifier_paste(*, only_active=False, replace=False)

   Add copied F-Modifiers to the selected F-Curves

   :param only_active: Only Active, Only paste F-Modifiers on active F-Curve (optional)
   :type only_active: bool
   :param replace: Replace Existing, Replace existing F-Modifiers, instead of just appending to the end of the existing list (optional)
   :type replace: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: frame_jump()

   Place the cursor on the midpoint of selected keyframes

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: gaussian_smooth(*, factor=1.0, sigma=0.33, filter_width=6)

   Smooth the curve using a Gaussian filter

   :param factor: Factor, How much to blend to the default value (in [0, inf], optional)
   :type factor: float
   :param sigma: Sigma, The shape of the gaussian distribution, lower values make it sharper (in [0.001, inf], optional)
   :type sigma: float
   :param filter_width: Filter Width, How far to each side the operator will average the key values (in [1, 64], optional)
   :type filter_width: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: ghost_curves_clear()

   Clear F-Curve snapshots (Ghosts) for active Graph Editor

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: ghost_curves_create()

   Create snapshot (Ghosts) of selected F-Curves as background aid for active Graph Editor

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: handle_type(*, type='FREE')

   Set type of handle for selected keyframes

   :param type: Type, (optional)
   :type type: Literal[:ref:`rna_enum_keyframe_handle_type_items`]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: hide(*, unselected=False)

   Hide selected curves from Graph Editor view

   :param unselected: Unselected, Hide unselected rather than selected curves (optional)
   :type unselected: bool
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

      - ``ALL``
        All Channels -- Insert a keyframe on all visible and editable F-Curves using each curve's current value.
      - ``SEL``
        Only Selected Channels -- Insert a keyframe on selected F-Curves using each curve's current value.
      - ``ACTIVE``
        Only Active F-Curve -- Insert a keyframe on the active F-Curve using the curve's current value.
      - ``CURSOR_ACTIVE``
        Active Channels at Cursor -- Insert a keyframe for the active F-Curve at the cursor point.
      - ``CURSOR_SEL``
        Selected Channels at Cursor -- Insert a keyframe for selected F-Curves at the cursor point.
   :type type: Literal['ALL', 'SEL', 'ACTIVE', 'CURSOR_ACTIVE', 'CURSOR_SEL']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: keyframe_jump(*, next=True)

   Jump to previous/next keyframe

   :param next: Next Keyframe, (optional)
   :type next: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: keys_to_samples()

   Convert selected channels to an uneditable set of samples to save storage space

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: match_slope(*, factor=0.0)

   Blend selected keys to the slope of neighboring ones

   :param factor: Factor, Defines which keys to use as slope and how much to blend towards them (in [-inf, inf], optional)
   :type factor: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: mirror(*, type='CFRA')

   Flip selected keyframes over the selected mirror line

   :param type: Type, (optional)

      - ``CFRA``
        By Times Over Current Frame -- Flip times of selected keyframes using the current frame as the mirror line.
      - ``VALUE``
        By Values Over Cursor Value -- Flip values of selected keyframes using the cursor value (Y/Horizontal component) as the mirror line.
      - ``YAXIS``
        By Times Over Zero Time -- Flip times of selected keyframes, effectively reversing the order they appear in.
      - ``XAXIS``
        By Values Over Zero Value -- Flip values of selected keyframes (i.e. negative values become positive, and vice versa).
      - ``MARKER``
        By Times Over First Selected Marker -- Flip times of selected keyframes using the first selected marker as the reference point.
   :type type: Literal['CFRA', 'VALUE', 'YAXIS', 'XAXIS', 'MARKER']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: paste(*, offset='START', value_offset='NONE', merge='MIX', flipped=False)

   Paste keyframes from the internal clipboard for the selected channels, starting on the current frame

   :param offset: Frame Offset, Paste time offset of keys (optional)
   :type offset: Literal[:ref:`rna_enum_keyframe_paste_offset_items`]
   :param value_offset: Value Offset, Paste keys with a value offset (optional)
   :type value_offset: Literal[:ref:`rna_enum_keyframe_paste_offset_value_items`]
   :param merge: Type, Method of merging pasted keys and existing (optional)
   :type merge: Literal[:ref:`rna_enum_keyframe_paste_merge_items`]
   :param flipped: Flipped, Paste keyframes from mirrored bones if they exist (optional)
   :type flipped: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: previewrange_set()

   Set Preview Range based on range of selected keyframes

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: push_pull(*, factor=1.0)

   Exaggerate or minimize the value of the selected keys

   :param factor: Factor, Control how far to push or pull the keys (in [-inf, inf], optional)
   :type factor: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: reveal(*, select=True)

   Make previously hidden curves visible again in Graph Editor view

   :param select: Select, (optional)
   :type select: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: samples_to_keys()

   Convert selected channels from samples to keyframes

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: scale_average(*, factor=1.0)

   Scale selected key values by their combined average

   :param factor: Scale Factor, The scale factor applied to the curve segments (in [-inf, inf], optional)
   :type factor: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: scale_from_neighbor(*, factor=0.0, anchor='LEFT')

   Increase or decrease the value of selected keys in relationship to the neighboring one

   :param factor: Factor, The factor to scale keys with (in [-inf, inf], optional)
   :type factor: float
   :param anchor: Reference Key, Which end of the segment to use as a reference to scale from (optional)
   :type anchor: Literal['LEFT', 'RIGHT']
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

.. function:: select_box(*, axis_range=False, include_handles=True, tweak=False, use_curve_selection=True, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, mode='SET')

   Select all keyframes within the specified region

   :param axis_range: Axis Range, (optional)
   :type axis_range: bool
   :param include_handles: Include Handles, Are handles tested individually against the selection criteria, independently from their keys. When unchecked, handles are (de)selected in unison with their keys (optional)
   :type include_handles: bool
   :param tweak: Tweak, Operator has been activated using a click-drag event (optional)
   :type tweak: bool
   :param use_curve_selection: Select Curves, Allow selecting all the keyframes of a curve by selecting the calculated F-curve (optional)
   :type use_curve_selection: bool
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

.. function:: select_circle(*, x=0, y=0, radius=25, wait_for_input=True, mode='SET', include_handles=True, use_curve_selection=True)

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
   :param include_handles: Include Handles, Are handles tested individually against the selection criteria, independently from their keys. When unchecked, handles are (de)selected in unison with their keys (optional)
   :type include_handles: bool
   :param use_curve_selection: Select Curves, Allow selecting all the keyframes of a curve by selecting the curve itself (optional)
   :type use_curve_selection: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_column(*, mode='KEYS')

   Select all keyframes on the specified frame(s)

   :param mode: Mode, (optional)
   :type mode: Literal['KEYS', 'CFRA', 'MARKERS_COLUMN', 'MARKERS_BETWEEN']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_key_handles(*, left_handle_action='SELECT', right_handle_action='SELECT', key_action='KEEP')

   For selected keyframes, select/deselect any combination of the key itself and its handles

   :param left_handle_action: Left Handle, Effect on the left handle (optional)

      - ``SELECT``
        Select.
      - ``DESELECT``
        Deselect.
      - ``KEEP``
        Keep -- Leave as is.
   :type left_handle_action: Literal['SELECT', 'DESELECT', 'KEEP']
   :param right_handle_action: Right Handle, Effect on the right handle (optional)

      - ``SELECT``
        Select.
      - ``DESELECT``
        Deselect.
      - ``KEEP``
        Keep -- Leave as is.
   :type right_handle_action: Literal['SELECT', 'DESELECT', 'KEEP']
   :param key_action: Key, Effect on the key itself (optional)

      - ``SELECT``
        Select.
      - ``DESELECT``
        Deselect.
      - ``KEEP``
        Keep -- Leave as is.
   :type key_action: Literal['SELECT', 'DESELECT', 'KEEP']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_lasso(*, path=None, use_smooth_stroke=False, smooth_stroke_factor=0.75, smooth_stroke_radius=35, mode='SET', include_handles=True, use_curve_selection=True)

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
   :param include_handles: Include Handles, Are handles tested individually against the selection criteria, independently from their keys. When unchecked, handles are (de)selected in unison with their keys (optional)
   :type include_handles: bool
   :param use_curve_selection: Select Curves, Allow selecting all the keyframes of a curve by selecting the curve itself (optional)
   :type use_curve_selection: bool
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
.. function:: shear(*, factor=0.0, direction='FROM_LEFT')

   Affect the value of the keys linearly, keeping the same relationship between them using either the left or the right key as reference

   :param factor: Shear Factor, The amount of shear to apply (in [-inf, inf], optional)
   :type factor: float
   :param direction: Direction, Which end of the segment to use as a reference to shear from (optional)

      - ``FROM_LEFT``
        From Left -- Shear the keys using the left key as reference.
      - ``FROM_RIGHT``
        From Right -- Shear the keys using the right key as reference.
   :type direction: Literal['FROM_LEFT', 'FROM_RIGHT']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: smooth()

   Apply weighted moving means to make selected F-Curves less bumpy

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: snap(*, type='CFRA')

   Snap selected keyframes to the chosen times/values

   :param type: Type, (optional)

      - ``CFRA``
        Selection to Current Frame -- Snap selected keyframes to the current frame.
      - ``VALUE``
        Selection to Cursor Value -- Set values of selected keyframes to the cursor value (Y/Horizontal component).
      - ``NEAREST_FRAME``
        Selection to Nearest Frame -- Snap selected keyframes to the nearest (whole) frame (use to fix accidental subframe offsets).
      - ``NEAREST_SECOND``
        Selection to Nearest Second -- Snap selected keyframes to the nearest second.
      - ``NEAREST_MARKER``
        Selection to Nearest Marker -- Snap selected keyframes to the nearest marker.
      - ``HORIZONTAL``
        Flatten Handles -- Flatten handles for a smoother transition.
   :type type: Literal['CFRA', 'VALUE', 'NEAREST_FRAME', 'NEAREST_SECOND', 'NEAREST_MARKER', 'HORIZONTAL']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: snap_cursor_value()

   Place the cursor value on the average value of selected keyframes

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: sound_to_samples(*, filepath="", check_existing=False, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=True, filter_python=False, filter_font=False, filter_sound=True, filter_text=False, filter_archive=False, filter_btx=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='', low=0.0, high=100000.0, attack=0.005, release=0.2, threshold=0.0, use_accumulate=False, use_additive=False, use_square=False, sthreshold=0.1)

   Bakes a sound wave to samples on selected channels

   :param filepath: File Path, Path to file (optional, never None)
   :type filepath: str
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
   :type sort_method: str
   :param low: Lowest Frequency, Cutoff frequency of a high-pass filter that is applied to the audio data (in [0, 100000], optional)
   :type low: float
   :param high: Highest Frequency, Cutoff frequency of a low-pass filter that is applied to the audio data (in [0, 100000], optional)
   :type high: float
   :param attack: Attack Time, Value for the envelope calculation that tells how fast the envelope can rise (the lower the value the steeper it can rise) (in [0, 2], optional)
   :type attack: float
   :param release: Release Time, Value for the envelope calculation that tells how fast the envelope can fall (the lower the value the steeper it can fall) (in [0, 5], optional)
   :type release: float
   :param threshold: Threshold, Minimum amplitude value needed to influence the envelope (in [0, 1], optional)
   :type threshold: float
   :param use_accumulate: Accumulate, Only the positive differences of the envelope amplitudes are summarized to produce the output (optional)
   :type use_accumulate: bool
   :param use_additive: Additive, The amplitudes of the envelope are summarized (or, when Accumulate is enabled, both positive and negative differences are accumulated) (optional)
   :type use_additive: bool
   :param use_square: Square, The output is a square curve (negative values always result in -1, and positive ones in 1) (optional)
   :type use_square: bool
   :param sthreshold: Square Threshold, Square only: all values with an absolute amplitude lower than that result in 0 (in [0, 1], optional)
   :type sthreshold: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: time_offset(*, frame_offset=0.0)

   Shifts the value of selected keys in time

   :param frame_offset: Frame Offset, How far in frames to offset the animation (in [-inf, inf], optional)
   :type frame_offset: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: view_all(*, include_handles=True)

   Reset viewable area to show full keyframe range

   :param include_handles: Include Handles, Include handles of keyframes when calculating extents (optional)
   :type include_handles: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: view_frame()

   Move the view to the current frame

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: view_selected(*, include_handles=True)

   Reset viewable area to show selected keyframe range

   :param include_handles: Include Handles, Include handles of keyframes when calculating extents (optional)
   :type include_handles: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

