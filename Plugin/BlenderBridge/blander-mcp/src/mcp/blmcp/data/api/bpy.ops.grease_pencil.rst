Grease Pencil Operators
=======================

.. module:: bpy.ops.grease_pencil

.. function:: active_frame_delete(*, all=False)

   Delete the active Grease Pencil frame(s)

   :param all: Delete all, Delete active keyframes of all layers (optional)
   :type all: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: bake_grease_pencil_animation(*, frame_start=1, frame_end=250, step=1, only_selected=False, frame_target=1, project_type='KEEP')

   Bake Grease Pencil object transform to Grease Pencil keyframes

   :param frame_start: Start Frame, The start frame (in [1, 100000], optional)
   :type frame_start: int
   :param frame_end: End Frame, The end frame of animation (in [1, 100000], optional)
   :type frame_end: int
   :param step: Step, Step between generated frames (in [1, 100], optional)
   :type step: int
   :param only_selected: Only Selected Keyframes, Convert only selected keyframes (optional)
   :type only_selected: bool
   :param frame_target: Target Frame, Destination frame (in [1, 100000], optional)
   :type frame_target: int
   :param project_type: Projection Type, (optional)

      - ``KEEP``
        No Reproject.
      - ``FRONT``
        Front -- Reproject the strokes using the X-Z plane.
      - ``SIDE``
        Side -- Reproject the strokes using the Y-Z plane.
      - ``TOP``
        Top -- Reproject the strokes using the X-Y plane.
      - ``VIEW``
        View -- Reproject the strokes to end up on the same plane, as if drawn from the current viewpoint using 'Cursor' Stroke Placement.
      - ``CURSOR``
        Cursor -- Reproject the strokes using the orientation of 3D cursor.
   :type project_type: Literal['KEEP', 'FRONT', 'SIDE', 'TOP', 'VIEW', 'CURSOR']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: brush_stroke(*, stroke=None, mode='NORMAL', brush_toggle='None', pen_flip=False)

   Draw a new stroke in the active Grease Pencil object

   :param stroke: Stroke, (optional)
   :type stroke: :class:`bpy_prop_collection`\ [:class:`OperatorStrokeElement`] | None
   :param mode: Stroke Mode, Action taken when a paint stroke is made (optional)

      - ``NORMAL``
        Regular -- Apply brush normally.
      - ``INVERT``
        Invert -- Invert action of brush for duration of stroke.
   :type mode: Literal['NORMAL', 'INVERT']
   :param brush_toggle: Temporary Brush Toggle Type, Brush to use for duration of stroke (optional)

      - ``None``
        None -- Apply brush normally.
      - ``SMOOTH``
        Smooth -- Switch to smooth brush for duration of stroke.
      - ``ERASE``
        Erase -- Switch to erase brush for duration of stroke.
      - ``MASK``
        Mask -- Switch to mask brush for duration of stroke.
   :type brush_toggle: Literal['None', 'SMOOTH', 'ERASE', 'MASK']
   :param pen_flip: Pen Flip, Whether a tablet's eraser mode is being used (optional)
   :type pen_flip: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: caps_set(*, type='ROUND')

   Change curve caps mode (rounded or flat)

   :param type: Type, (optional)

      - ``ROUND``
        Rounded -- Set as default rounded.
      - ``FLAT``
        Flat.
      - ``START``
        Toggle Start.
      - ``END``
        Toggle End.
   :type type: Literal['ROUND', 'FLAT', 'START', 'END']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: clean_loose(*, limit=1)

   Remove loose points

   :param limit: Limit, Number of points to consider stroke as loose (in [1, inf], optional)
   :type limit: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: convert_curve_type(*, type='POLY', threshold=0.01)

   Convert type of selected curves

   :param type: Type, (optional)
   :type type: Literal[:ref:`rna_enum_curves_type_items`]
   :param threshold: Threshold, The distance that the resulting points are allowed to be within (in [0, 100], optional)
   :type threshold: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: copy()

   Copy the selected Grease Pencil points or strokes to the internal clipboard

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: cyclical_set(*, type='TOGGLE', subdivide_cyclic_segment=True)

   Close or open the selected stroke adding a segment from last to first point

   :param type: Type, (optional)
   :type type: Literal['CLOSE', 'OPEN', 'TOGGLE']
   :param subdivide_cyclic_segment: Match Point Density, Add point in the new segment to keep the same density (optional)
   :type subdivide_cyclic_segment: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: delete(*, mode='ALL')

   Delete selected strokes or points

   :param mode: Mode, The kind of strokes or fills to delete (optional)

      - ``ALL``
        All -- Delete all selected strokes or points.
      - ``STROKES``
        Only Strokes -- Delete only strokes and not fills.
      - ``FILLS``
        Only Fills -- Delete only fills and not strokes.
   :type mode: Literal['ALL', 'STROKES', 'FILLS']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: delete_breakdown()

   Remove breakdown frames generated by interpolating between two Grease Pencil frames

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: delete_frame(*, type='ACTIVE_FRAME')

   Delete Grease Pencil Frame(s)

   :param type: Type, Method used for deleting Grease Pencil frames (optional)

      - ``ACTIVE_FRAME``
        Active Frame -- Deletes current frame in the active layer.
      - ``ALL_FRAMES``
        All Active Frames -- Delete active frames for all layers.
   :type type: Literal['ACTIVE_FRAME', 'ALL_FRAMES']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: dissolve(*, type='POINTS')

   Delete selected points without splitting strokes

   :param type: Type, Method used for dissolving stroke points (optional)

      - ``POINTS``
        Dissolve -- Dissolve selected points.
      - ``BETWEEN``
        Dissolve Between -- Dissolve points between selected points.
      - ``UNSELECT``
        Dissolve Unselect -- Dissolve all unselected points.
   :type type: Literal['POINTS', 'BETWEEN', 'UNSELECT']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: duplicate()

   Duplicate the selected points

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: duplicate_move(*, GREASE_PENCIL_OT_duplicate={}, TRANSFORM_OT_translate={})

   Make copies of the selected Grease Pencil strokes and move them

   :param GREASE_PENCIL_OT_duplicate: Duplicate, Duplicate the selected points (optional, :func:`bpy.ops.grease_pencil.duplicate` keyword arguments)
   :type GREASE_PENCIL_OT_duplicate: dict[str, Any]
   :param TRANSFORM_OT_translate: Move, Move selected items (optional, :func:`bpy.ops.transform.translate` keyword arguments)
   :type TRANSFORM_OT_translate: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: erase_box(*, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True)

   Erase points in the box region

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

.. function:: erase_lasso(*, path=None, use_smooth_stroke=False, smooth_stroke_factor=0.75, smooth_stroke_radius=35)

   Erase points in the lasso region

   :param path: Path, (optional)
   :type path: :class:`bpy_prop_collection`\ [:class:`OperatorMousePath`] | None
   :param use_smooth_stroke: Stabilize Stroke, Selection lags behind mouse and follows a smoother path (optional)
   :type use_smooth_stroke: bool
   :param smooth_stroke_factor: Smooth Stroke Factor, Higher values give a smoother stroke (in [0.5, 0.99], optional)
   :type smooth_stroke_factor: float
   :param smooth_stroke_radius: Smooth Stroke Radius, Minimum distance from last point before selection continues (in [10, 200], optional)
   :type smooth_stroke_radius: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: extrude()

   Extrude the selected points

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: extrude_move(*, GREASE_PENCIL_OT_extrude={}, TRANSFORM_OT_translate={})

   Extrude selected points and move them

   :param GREASE_PENCIL_OT_extrude: Extrude Stroke Points, Extrude the selected points (optional, :func:`bpy.ops.grease_pencil.extrude` keyword arguments)
   :type GREASE_PENCIL_OT_extrude: dict[str, Any]
   :param TRANSFORM_OT_translate: Move, Move selected items (optional, :func:`bpy.ops.transform.translate` keyword arguments)
   :type TRANSFORM_OT_translate: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: fill(*, invert=False, precision=False)

   Fill with color the shape formed by strokes

   :param invert: Invert, Find boundary of unfilled instead of filled regions (optional)
   :type invert: bool
   :param precision: Precision, Use precision movement for extension lines (optional)
   :type precision: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: frame_clean_duplicate(*, selected=False)

   Remove any keyframe that is a duplicate of the previous one

   :param selected: Selected, Only delete selected keyframes (optional)
   :type selected: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: frame_duplicate(*, all=False)

   Make a copy of the active Grease Pencil frame(s)

   :param all: Duplicate all, Duplicate active keyframes of all layer (optional)
   :type all: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: insert_blank_frame(*, all_layers=False, duration=0)

   Insert a blank frame on the current scene frame

   :param all_layers: All Layers, Insert a blank frame in all editable layers (optional)
   :type all_layers: bool
   :param duration: Duration, (in [0, 1048574], optional)
   :type duration: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: interpolate(*, shift=0.0, layers='ACTIVE', exclude_breakdowns=False, use_selection=False, flip='AUTO', smooth_steps=1, smooth_factor=0.0)

   Interpolate Grease Pencil strokes between frames

   :param shift: Shift, Bias factor for which frame has more influence on the interpolated strokes (in [-1, 1], optional)
   :type shift: float
   :param layers: Layer, Layers included in the interpolation (optional)
   :type layers: Literal['ACTIVE', 'ALL']
   :param exclude_breakdowns: Exclude Breakdowns, Exclude existing Breakdowns keyframes as interpolation extremes (optional)
   :type exclude_breakdowns: bool
   :param use_selection: Use Selection, Use only selected strokes for interpolating (optional)
   :type use_selection: bool
   :param flip: Flip Mode, Invert destination stroke to match start and end with source stroke (optional)
   :type flip: Literal['NONE', 'FLIP', 'AUTO']
   :param smooth_steps: Iterations, Number of times to smooth newly created strokes (in [1, 3], optional)
   :type smooth_steps: int
   :param smooth_factor: Smooth, Amount of smoothing to apply to interpolated strokes, to reduce jitter/noise (in [0, 2], optional)
   :type smooth_factor: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: interpolate_sequence(*, step=1, layers='ACTIVE', exclude_breakdowns=False, use_selection=False, flip='AUTO', smooth_steps=1, smooth_factor=0.0, type='LINEAR', easing='EASE_IN', back=1.702, amplitude=0.15, period=0.15)

   Generate 'in-betweens' to smoothly interpolate between Grease Pencil frames

   :param step: Step, Number of frames between generated interpolated frames (in [1, 1048574], optional)
   :type step: int
   :param layers: Layer, Layers included in the interpolation (optional)
   :type layers: Literal['ACTIVE', 'ALL']
   :param exclude_breakdowns: Exclude Breakdowns, Exclude existing Breakdowns keyframes as interpolation extremes (optional)
   :type exclude_breakdowns: bool
   :param use_selection: Use Selection, Use only selected strokes for interpolating (optional)
   :type use_selection: bool
   :param flip: Flip Mode, Invert destination stroke to match start and end with source stroke (optional)
   :type flip: Literal['NONE', 'FLIP', 'AUTO']
   :param smooth_steps: Iterations, Number of times to smooth newly created strokes (in [1, 3], optional)
   :type smooth_steps: int
   :param smooth_factor: Smooth, Amount of smoothing to apply to interpolated strokes, to reduce jitter/noise (in [0, 2], optional)
   :type smooth_factor: float
   :param type: Type, Interpolation method to use the next time 'Interpolate Sequence' is run (optional)

      - ``LINEAR``
        Linear -- Straight-line interpolation between A and B (i.e. no ease in/out).
      - ``CUSTOM``
        Custom -- Custom interpolation defined using a curve map.
      - ``SINE``
        Sinusoidal -- Sinusoidal easing (weakest, almost linear but with a slight curvature).
      - ``QUAD``
        Quadratic -- Quadratic easing.
      - ``CUBIC``
        Cubic -- Cubic easing.
      - ``QUART``
        Quartic -- Quartic easing.
      - ``QUINT``
        Quintic -- Quintic easing.
      - ``EXPO``
        Exponential -- Exponential easing (dramatic).
      - ``CIRC``
        Circular -- Circular easing (strongest and most dynamic).
      - ``BACK``
        Back -- Cubic easing with overshoot and settle.
      - ``BOUNCE``
        Bounce -- Exponentially decaying parabolic bounce, like when objects collide.
      - ``ELASTIC``
        Elastic -- Exponentially decaying sine wave, like an elastic band.
   :type type: Literal['LINEAR', 'CUSTOM', 'SINE', 'QUAD', 'CUBIC', 'QUART', 'QUINT', 'EXPO', 'CIRC', 'BACK', 'BOUNCE', 'ELASTIC']
   :param easing: Easing, Which ends of the segment between the preceding and following Grease Pencil frames easing interpolation is applied to (optional)
   :type easing: Literal[:ref:`rna_enum_beztriple_interpolation_easing_items`]
   :param back: Back, Amount of overshoot for 'back' easing (in [0, inf], optional)
   :type back: float
   :param amplitude: Amplitude, Amount to boost elastic bounces for 'elastic' easing (in [0, inf], optional)
   :type amplitude: float
   :param period: Period, Time between bounces for elastic easing (in [-inf, inf], optional)
   :type period: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: join_fills()

   Join selected strokes into one fill to create holes

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: join_selection(*, type='JOINSTROKES')

   New stroke from selected points/strokes

   :param type: Type, Defines how the operator will behave on the selection in the active layer (optional)

      - ``JOINSTROKES``
        Join Strokes -- Join the selected strokes into one stroke.
      - ``SPLITCOPY``
        Split and Copy -- Copy the selected points to a new stroke.
      - ``SPLIT``
        Split -- Split the selected point to a new stroke.
   :type type: Literal['JOINSTROKES', 'SPLITCOPY', 'SPLIT']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: layer_active(*, layer=0)

   Set the active Grease Pencil layer

   :param layer: Grease Pencil Layer, (in [0, inf], optional)
   :type layer: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: layer_add(*, new_layer_name="Layer")

   Add a new Grease Pencil layer in the active object

   :param new_layer_name: Name, Name of the new layer (optional, never None)
   :type new_layer_name: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: layer_duplicate(*, empty_keyframes=False)

   Make a copy of the active Grease Pencil layer

   :param empty_keyframes: Empty Keyframes, Add Empty Keyframes (optional)
   :type empty_keyframes: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: layer_duplicate_object(*, only_active=True, mode='ALL')

   Make a copy of the active Grease Pencil layer to selected object

   :param only_active: Only Active, Copy only active Layer, uncheck to append all layers (optional)
   :type only_active: bool
   :param mode: Mode, (optional)
   :type mode: Literal['ALL', 'ACTIVE']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: layer_group_add(*, new_layer_group_name="")

   Add a new Grease Pencil layer group in the active object

   :param new_layer_group_name: Name, Name of the new layer group (optional, never None)
   :type new_layer_group_name: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: layer_group_color_tag(*, color_tag='COLOR1')

   Change layer group icon

   :param color_tag: Color Tag, (optional)
   :type color_tag: Literal['NONE', 'COLOR1', 'COLOR2', 'COLOR3', 'COLOR4', 'COLOR5', 'COLOR6', 'COLOR7', 'COLOR8']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: layer_group_remove(*, keep_children=False)

   Remove Grease Pencil layer group in the active object

   :param keep_children: Keep children nodes, Keep the children nodes of the group and only delete the group itself (optional)
   :type keep_children: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: layer_hide(*, unselected=False)

   Hide selected/unselected Grease Pencil layers

   :param unselected: Unselected, Hide unselected rather than selected layers (optional)
   :type unselected: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: layer_isolate(*, affect_visibility=False)

   Make only active layer visible/editable

   :param affect_visibility: Affect Visibility, Also affect the visibility (optional)
   :type affect_visibility: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: layer_lock_all(*, lock=True)

   Lock all Grease Pencil layers to prevent them from being accidentally modified

   :param lock: Lock Value, Lock/Unlock all layers (optional)
   :type lock: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: layer_mask_add(*, name="")

   Add new layer as masking

   :param name: Layer, Name of the layer (optional, never None)
   :type name: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: layer_mask_remove()

   Remove Layer Mask

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: layer_mask_reorder(*, direction='UP')

   Reorder the active Grease Pencil mask layer up/down in the list

   :param direction: Direction, (optional)
   :type direction: Literal['UP', 'DOWN']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: layer_merge(*, mode='ACTIVE')

   Combine layers based on the mode into one layer

   :param mode: Mode, (optional)

      - ``ACTIVE``
        Active -- Combine the active layer with the layer just below (if it exists).
      - ``GROUP``
        Group -- Combine layers in the active group into a single layer.
      - ``ALL``
        All -- Combine all layers into a single layer.
   :type mode: Literal['ACTIVE', 'GROUP', 'ALL']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: layer_move(*, direction='UP')

   Move the active Grease Pencil layer or Group

   :param direction: Direction, (optional)
   :type direction: Literal['UP', 'DOWN']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: layer_remove()

   Remove the active Grease Pencil layer

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: layer_reveal()

   Show all Grease Pencil layers

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: material_copy_to_object(*, only_active=True)

   Append Materials of the active Grease Pencil to other object

   :param only_active: Only Active, Append only active material, uncheck to append all materials (optional)
   :type only_active: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: material_hide(*, invert=False)

   Hide active/inactive Grease Pencil material(s)

   :param invert: Invert, Hide inactive materials instead of the active one (optional)
   :type invert: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: material_isolate(*, affect_visibility=False)

   Toggle whether the active material is the only one that is editable and/or visible

   :param affect_visibility: Affect Visibility, In addition to toggling the editability, also affect the visibility (optional)
   :type affect_visibility: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: material_lock_all()

   Lock all Grease Pencil materials to prevent them from being accidentally modified

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: material_lock_unselected()

   Lock any material not used in any selected stroke

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: material_lock_unused()

   Lock and hide any material not used

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: material_reveal()

   Unhide all hidden Grease Pencil materials

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: material_select(*, deselect=False)

   Select/Deselect all Grease Pencil strokes using current material

   :param deselect: Deselect, Unselect strokes (optional)
   :type deselect: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: material_unlock_all()

   Unlock all Grease Pencil materials so that they can be edited

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: move_to_layer(*, target_layer_name="", add_new_layer=False)

   Move selected strokes to another layer

   :param target_layer_name: Name, Target Grease Pencil Layer (optional, never None)
   :type target_layer_name: str
   :param add_new_layer: New Layer, Move selection to a new layer (optional)
   :type add_new_layer: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: outline(*, type='VIEW', radius=0.01, offset_factor=-1.0, corner_subdivisions=2)

   Convert selected strokes to perimeter

   :param type: Projection Mode, (optional)
   :type type: Literal['VIEW', 'FRONT', 'SIDE', 'TOP', 'CURSOR', 'CAMERA']
   :param radius: Radius, (in [0, 10], optional)
   :type radius: float
   :param offset_factor: Offset Factor, (in [-1, 1], optional)
   :type offset_factor: float
   :param corner_subdivisions: Corner Subdivisions, (in [0, 10], optional)
   :type corner_subdivisions: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: paintmode_toggle(*, back=False)

   Enter/Exit paint mode for Grease Pencil strokes

   :param back: Return to Previous Mode, Return to previous mode (optional)
   :type back: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: paste(*, type='ACTIVE', paste_back=False, keep_world_transform=False)

   Paste Grease Pencil points or strokes from the internal clipboard to the active layer

   :param type: Type, (optional)
   :type type: Literal['ACTIVE', 'LAYER']
   :param paste_back: Paste on Back, Add pasted strokes behind all strokes (optional)
   :type paste_back: bool
   :param keep_world_transform: Keep World Transform, Keep the world transform of strokes from the clipboard unchanged (optional)
   :type keep_world_transform: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: pen(*, extend=False, deselect=False, toggle=False, deselect_all=False, select_passthrough=False, extrude_point=False, extrude_handle='VECTOR', delete_point=False, insert_point=False, move_segment=False, select_point=False, move_point=False, cycle_handle_type=False, size=0.01)

   Construct and edit splines

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
   :param extrude_point: Extrude Point, Add a point connected to the last selected point (optional)
   :type extrude_point: bool
   :param extrude_handle: Extrude Handle Type, Type of the extruded handle (optional)
   :type extrude_handle: Literal['AUTO', 'VECTOR']
   :param delete_point: Delete Point, Delete an existing point (optional)
   :type delete_point: bool
   :param insert_point: Insert Point, Insert Point into a curve segment (optional)
   :type insert_point: bool
   :param move_segment: Move Segment, Move an existing curve segment (optional)
   :type move_segment: bool
   :param select_point: Select Point, Select a point or its handles (optional)
   :type select_point: bool
   :param move_point: Move Point, Move a point or its handles (optional)
   :type move_point: bool
   :param cycle_handle_type: Cycle Handle Type, Cycle between all four handle types (optional)
   :type cycle_handle_type: bool
   :param size: Size, Diameter of new points (in [0, inf], optional)
   :type size: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: primitive_arc(*, subdivision=62, type='ARC')

   Create predefined Grease Pencil stroke arcs

   :param subdivision: Subdivisions, Number of subdivisions per segment (in [0, inf], optional)
   :type subdivision: int
   :param type: Type, Type of shape (optional)
   :type type: Literal['BOX', 'LINE', 'POLYLINE', 'CIRCLE', 'ARC', 'CURVE']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: primitive_box(*, subdivision=3, type='BOX')

   Create predefined Grease Pencil stroke boxes

   :param subdivision: Subdivisions, Number of subdivisions per segment (in [0, inf], optional)
   :type subdivision: int
   :param type: Type, Type of shape (optional)
   :type type: Literal['BOX', 'LINE', 'POLYLINE', 'CIRCLE', 'ARC', 'CURVE']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: primitive_circle(*, subdivision=94, type='CIRCLE')

   Create predefined Grease Pencil stroke circles

   :param subdivision: Subdivisions, Number of subdivisions per segment (in [0, inf], optional)
   :type subdivision: int
   :param type: Type, Type of shape (optional)
   :type type: Literal['BOX', 'LINE', 'POLYLINE', 'CIRCLE', 'ARC', 'CURVE']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: primitive_curve(*, subdivision=62, type='CURVE')

   Create predefined Grease Pencil stroke curve shapes

   :param subdivision: Subdivisions, Number of subdivisions per segment (in [0, inf], optional)
   :type subdivision: int
   :param type: Type, Type of shape (optional)
   :type type: Literal['BOX', 'LINE', 'POLYLINE', 'CIRCLE', 'ARC', 'CURVE']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: primitive_line(*, subdivision=6, type='LINE')

   Create predefined Grease Pencil stroke lines

   :param subdivision: Subdivisions, Number of subdivisions per segment (in [0, inf], optional)
   :type subdivision: int
   :param type: Type, Type of shape (optional)
   :type type: Literal['BOX', 'LINE', 'POLYLINE', 'CIRCLE', 'ARC', 'CURVE']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: primitive_polyline(*, subdivision=6, type='POLYLINE')

   Create predefined Grease Pencil stroke polylines

   :param subdivision: Subdivisions, Number of subdivisions per segment (in [0, inf], optional)
   :type subdivision: int
   :param type: Type, Type of shape (optional)
   :type type: Literal['BOX', 'LINE', 'POLYLINE', 'CIRCLE', 'ARC', 'CURVE']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: relative_layer_mask_add(*, mode='ABOVE')

   Mask active layer with layer above or below

   :param mode: Mode, Which relative layer (above or below) to use as a mask (optional)
   :type mode: Literal['ABOVE', 'BELOW']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/grease_pencil.py\:39 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/grease_pencil.py#L39>`__


.. function:: remove_fill_guides(*, mode='ALL_FRAMES')

   Remove all the strokes that were created from the fill tool as guides

   :param mode: Mode, (optional)
   :type mode: Literal['ACTIVE_FRAME', 'ALL_FRAMES']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: reorder(*, direction='TOP')

   Change the display order of the selected strokes

   :param direction: Direction, (optional)
   :type direction: Literal['TOP', 'UP', 'DOWN', 'BOTTOM']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: reproject(*, type='VIEW', keep_original=False, offset=0.0)

   Reproject the selected strokes from the current viewpoint as if they had been newly drawn (e.g. to fix problems from accidental 3D cursor movement or accidental viewport changes, or for matching deforming geometry)

   :param type: Projection Type, (optional)

      - ``FRONT``
        Front -- Reproject the strokes using the X-Z plane.
      - ``SIDE``
        Side -- Reproject the strokes using the Y-Z plane.
      - ``TOP``
        Top -- Reproject the strokes using the X-Y plane.
      - ``VIEW``
        View -- Reproject the strokes to end up on the same plane, as if drawn from the current viewpoint using 'Cursor' Stroke Placement.
      - ``SURFACE``
        Surface -- Reproject the strokes on to the scene geometry, as if drawn using 'Surface' placement.
      - ``CURSOR``
        Cursor -- Reproject the strokes using the orientation of 3D cursor.
   :type type: Literal['FRONT', 'SIDE', 'TOP', 'VIEW', 'SURFACE', 'CURSOR']
   :param keep_original: Keep Original, Keep original strokes and create a copy before reprojecting (optional)
   :type keep_original: bool
   :param offset: Surface Offset, (in [0, 10], optional)
   :type offset: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: reset_uvs()

   Reset UV transformation to default values

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: sculpt_paint(*, stroke=None, mode='NORMAL', brush_toggle='None', pen_flip=False)

   Sculpt strokes in the active Grease Pencil object

   :param stroke: Stroke, (optional)
   :type stroke: :class:`bpy_prop_collection`\ [:class:`OperatorStrokeElement`] | None
   :param mode: Stroke Mode, Action taken when a paint stroke is made (optional)

      - ``NORMAL``
        Regular -- Apply brush normally.
      - ``INVERT``
        Invert -- Invert action of brush for duration of stroke.
   :type mode: Literal['NORMAL', 'INVERT']
   :param brush_toggle: Temporary Brush Toggle Type, Brush to use for duration of stroke (optional)

      - ``None``
        None -- Apply brush normally.
      - ``SMOOTH``
        Smooth -- Switch to smooth brush for duration of stroke.
      - ``ERASE``
        Erase -- Switch to erase brush for duration of stroke.
      - ``MASK``
        Mask -- Switch to mask brush for duration of stroke.
   :type brush_toggle: Literal['None', 'SMOOTH', 'ERASE', 'MASK']
   :param pen_flip: Pen Flip, Whether a tablet's eraser mode is being used (optional)
   :type pen_flip: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: sculptmode_toggle(*, back=False)

   Enter/Exit sculpt mode for Grease Pencil strokes

   :param back: Return to Previous Mode, Return to previous mode (optional)
   :type back: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_all(*, action='TOGGLE')

   (De)select all visible strokes

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

.. function:: select_alternate(*, deselect_ends=False)

   Select alternated points in strokes with already selected points

   :param deselect_ends: Deselect Ends, (De)select the first and last point of each stroke (optional)
   :type deselect_ends: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_by_stroke_type(*, type='STROKE', deselect=False)

   Select/Deselect all strokes or fills

   :param type: Type, (optional)
   :type type: Literal['STROKE', 'FILL']
   :param deselect: Deselect, Unselect strokes (optional)
   :type deselect: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_ends(*, amount_start=0, amount_end=1)

   Select end points of strokes

   :param amount_start: Amount Start, Number of points to select from the start (in [0, inf], optional)
   :type amount_start: int
   :param amount_end: Amount End, Number of points to select from the end (in [0, inf], optional)
   :type amount_end: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_fill()

   Select all curves in a fill

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select_less()

   Shrink the selection by one point

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select_linked()

   Select all points in curves with any point selection

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select_more()

   Grow the selection by one point

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select_random(*, ratio=0.5, seed=0, action='SELECT')

   Selects random points from the current strokes selection

   :param ratio: Ratio, Portion of items to select randomly (in [0, 1], optional)
   :type ratio: float
   :param seed: Random Seed, Seed for the random number generator (in [0, inf], optional)
   :type seed: int
   :param action: Action, Selection action to execute (optional)

      - ``SELECT``
        Select -- Select all elements.
      - ``DESELECT``
        Deselect -- Deselect all elements.
   :type action: Literal['SELECT', 'DESELECT']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_similar(*, mode='LAYER', threshold=0.1)

   Select all strokes with similar characteristics

   :param mode: Mode, (optional)
   :type mode: Literal['LAYER', 'MATERIAL', 'VERTEX_COLOR', 'RADIUS', 'OPACITY']
   :param threshold: Threshold, (in [0, inf], optional)
   :type threshold: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: separate(*, mode='SELECTED')

   Separate the selected geometry into a new Grease Pencil object

   :param mode: Mode, (optional)

      - ``SELECTED``
        Selection -- Separate selected geometry.
      - ``MATERIAL``
        By Material -- Separate by material.
      - ``LAYER``
        By Layer -- Separate by layer.
   :type mode: Literal['SELECTED', 'MATERIAL', 'LAYER']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: separate_fills(*, individual=True)

   Separate the selected strokes from current fill

   :param individual: Individual, Create a separate fill for each individual stroke (optional)
   :type individual: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: set_active_material()

   Set the selected stroke material as the active material

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: set_corner_type(*, corner_type='SHARP', miter_angle=0.785398)

   Set the corner type of the selected points

   :param corner_type: Corner Type, (optional)
   :type corner_type: Literal['ROUND', 'FLAT', 'SHARP']
   :param miter_angle: Miter Cut Angle, All corners sharper than the Miter angle will be cut flat (in [0, 3.14159], optional)
   :type miter_angle: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: set_curve_resolution(*, resolution=12)

   Set resolution of selected curves

   :param resolution: Resolution, The resolution to use for each curve segment (in [0, 10000], optional)
   :type resolution: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: set_curve_type(*, type='POLY', use_handles=False)

   Set type of selected curves

   :param type: Type, Curve type (optional)
   :type type: Literal[:ref:`rna_enum_curves_type_items`]
   :param use_handles: Handles, Take handle information into account in the conversion (optional)
   :type use_handles: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: set_handle_type(*, type='AUTO')

   Set the handle type for Bézier curves

   :param type: Type, (optional)

      - ``AUTO``
        Auto -- The location is automatically calculated to be smooth.
      - ``VECTOR``
        Vector -- The location is calculated to point to the next/previous control point.
      - ``ALIGN``
        Align -- The location is constrained to point in the opposite direction as the other handle.
      - ``FREE_ALIGN``
        Free -- The handle can be moved anywhere, and does not influence the point's other handle.
      - ``TOGGLE_FREE_ALIGN``
        Toggle Free/Align -- Replace Free handles with Align, and all Align with Free handles.
   :type type: Literal['AUTO', 'VECTOR', 'ALIGN', 'FREE_ALIGN', 'TOGGLE_FREE_ALIGN']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: set_material(*, slot='DEFAULT')

   Set active material

   :param slot: Material Slot, (optional)
   :type slot: Literal['DEFAULT']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: set_selection_mode(*, mode='POINT')

   Change the selection mode for Grease Pencil strokes

   :param mode: Mode, (optional)
   :type mode: Literal[:ref:`rna_enum_grease_pencil_selectmode_items`]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: set_start_point()

   Select which point is the beginning of the curve

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: set_stroke_type(*, type='STROKE')

   Set the stroke type (stroke, fill, or both) of the selected strokes

   :param type: Type, (optional)
   :type type: Literal['STROKE', 'FILL', 'BOTH']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: set_uniform_opacity(*, opacity_stroke=1.0, opacity_fill=0.5)

   Set all stroke points to same opacity

   :param opacity_stroke: Stroke Opacity, (in [0, 1], optional)
   :type opacity_stroke: float
   :param opacity_fill: Fill Opacity, (in [0, 1], optional)
   :type opacity_fill: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: set_uniform_thickness(*, thickness=0.1)

   Set all stroke points to same thickness

   :param thickness: Thickness, Thickness (in [0, 1000], optional)
   :type thickness: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: snap_cursor_to_selected()

   Snap cursor to center of selected points

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: snap_to_cursor(*, use_offset=True)

   Snap selected points/strokes to the cursor

   :param use_offset: With Offset, Offset the entire stroke instead of selected points only (optional)
   :type use_offset: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: snap_to_grid()

   Snap selected points to the nearest grid points

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: stroke_material_set(*, material="")

   Assign the active material slot to the selected strokes

   :param material: Material, Name of the material (optional, never None)
   :type material: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: stroke_merge_by_distance(*, threshold=0.001, use_unselected=False)

   Merge points by distance

   :param threshold: Threshold, (in [0, 100], optional)
   :type threshold: float
   :param use_unselected: Unselected, Use whole stroke, not only selected points (optional)
   :type use_unselected: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: stroke_reset_vertex_color(*, mode='BOTH')

   Reset vertex color for all or selected strokes

   :param mode: Mode, (optional)
   :type mode: Literal['STROKE', 'FILL', 'BOTH']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: stroke_simplify(*, factor=0.01, length=0.05, distance=0.01, steps=1, mode='FIXED')

   Simplify selected strokes

   :param factor: Factor, (in [0, 100], optional)
   :type factor: float
   :param length: Length, (in [0, 100], optional)
   :type length: float
   :param distance: Distance, (in [0, 100], optional)
   :type distance: float
   :param steps: Steps, (in [0, 50], optional)
   :type steps: int
   :param mode: Mode, Method used for simplifying stroke points (optional)

      - ``FIXED``
        Fixed -- Delete alternating vertices in the stroke, except extremes.
      - ``ADAPTIVE``
        Adaptive -- Use a Ramer-Douglas-Peucker algorithm to simplify the stroke preserving main shape.
      - ``SAMPLE``
        Sample -- Re-sample the stroke with segments of the specified length.
      - ``MERGE``
        Merge -- Simplify the stroke by merging vertices closer than a given distance.
   :type mode: Literal['FIXED', 'ADAPTIVE', 'SAMPLE', 'MERGE']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: stroke_smooth(*, iterations=10, factor=1.0, smooth_ends=False, keep_shape=False, smooth_position=True, smooth_radius=True, smooth_opacity=False)

   Smooth selected strokes

   :param iterations: Iterations, (in [1, 100], optional)
   :type iterations: int
   :param factor: Factor, (in [0, 1], optional)
   :type factor: float
   :param smooth_ends: Smooth Endpoints, (optional)
   :type smooth_ends: bool
   :param keep_shape: Keep Shape, (optional)
   :type keep_shape: bool
   :param smooth_position: Position, (optional)
   :type smooth_position: bool
   :param smooth_radius: Radius, (optional)
   :type smooth_radius: bool
   :param smooth_opacity: Opacity, (optional)
   :type smooth_opacity: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: stroke_split()

   Split selected points to a new stroke

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: stroke_subdivide(*, number_cuts=1, only_selected=True)

   Subdivide between continuous selected points of the stroke adding a point half way between them

   :param number_cuts: Number of Cuts, (in [1, 32], optional)
   :type number_cuts: int
   :param only_selected: Selected Points, Smooth only selected points in the stroke (optional)
   :type only_selected: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: stroke_subdivide_smooth(*, GREASE_PENCIL_OT_stroke_subdivide={}, GREASE_PENCIL_OT_stroke_smooth={})

   Subdivide strokes and smooth them

   :param GREASE_PENCIL_OT_stroke_subdivide: Subdivide Stroke, Subdivide between continuous selected points of the stroke adding a point half way between them (optional, :func:`bpy.ops.grease_pencil.stroke_subdivide` keyword arguments)
   :type GREASE_PENCIL_OT_stroke_subdivide: dict[str, Any]
   :param GREASE_PENCIL_OT_stroke_smooth: Smooth Stroke, Smooth selected strokes (optional, :func:`bpy.ops.grease_pencil.stroke_smooth` keyword arguments)
   :type GREASE_PENCIL_OT_stroke_smooth: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: stroke_switch_direction()

   Change direction of the points of the selected strokes

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: stroke_trim(*, path=None, use_smooth_stroke=False, smooth_stroke_factor=0.75, smooth_stroke_radius=35)

   Delete stroke points in between intersecting strokes

   :param path: Path, (optional)
   :type path: :class:`bpy_prop_collection`\ [:class:`OperatorMousePath`] | None
   :param use_smooth_stroke: Stabilize Stroke, Selection lags behind mouse and follows a smoother path (optional)
   :type use_smooth_stroke: bool
   :param smooth_stroke_factor: Smooth Stroke Factor, Higher values give a smoother stroke (in [0.5, 0.99], optional)
   :type smooth_stroke_factor: float
   :param smooth_stroke_radius: Smooth Stroke Radius, Minimum distance from last point before selection continues (in [10, 200], optional)
   :type smooth_stroke_radius: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: texture_gradient(*, xstart=0, xend=0, ystart=0, yend=0, flip=False, cursor=5)

   Draw a line to set the fill material gradient for the selected strokes

   :param xstart: X Start, (in [-inf, inf], optional)
   :type xstart: int
   :param xend: X End, (in [-inf, inf], optional)
   :type xend: int
   :param ystart: Y Start, (in [-inf, inf], optional)
   :type ystart: int
   :param yend: Y End, (in [-inf, inf], optional)
   :type yend: int
   :param flip: Flip, (optional)
   :type flip: bool
   :param cursor: Cursor, Mouse cursor style to use during the modal operator (in [0, inf], optional)
   :type cursor: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: vertex_brush_stroke(*, stroke=None, mode='NORMAL', brush_toggle='None', pen_flip=False)

   Draw on vertex colors in the active Grease Pencil object

   :param stroke: Stroke, (optional)
   :type stroke: :class:`bpy_prop_collection`\ [:class:`OperatorStrokeElement`] | None
   :param mode: Stroke Mode, Action taken when a paint stroke is made (optional)

      - ``NORMAL``
        Regular -- Apply brush normally.
      - ``INVERT``
        Invert -- Invert action of brush for duration of stroke.
   :type mode: Literal['NORMAL', 'INVERT']
   :param brush_toggle: Temporary Brush Toggle Type, Brush to use for duration of stroke (optional)

      - ``None``
        None -- Apply brush normally.
      - ``SMOOTH``
        Smooth -- Switch to smooth brush for duration of stroke.
      - ``ERASE``
        Erase -- Switch to erase brush for duration of stroke.
      - ``MASK``
        Mask -- Switch to mask brush for duration of stroke.
   :type brush_toggle: Literal['None', 'SMOOTH', 'ERASE', 'MASK']
   :param pen_flip: Pen Flip, Whether a tablet's eraser mode is being used (optional)
   :type pen_flip: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: vertex_color_brightness_contrast(*, mode='BOTH', brightness=0.0, contrast=0.0)

   Adjust vertex color brightness/contrast

   :param mode: Mode, (optional)
   :type mode: Literal['STROKE', 'FILL', 'BOTH']
   :param brightness: Brightness, (in [-1, 1], optional)
   :type brightness: float
   :param contrast: Contrast, (in [-1, 1], optional)
   :type contrast: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: vertex_color_hsv(*, mode='BOTH', h=0.5, s=1.0, v=1.0)

   Adjust vertex color HSV values

   :param mode: Mode, (optional)
   :type mode: Literal['STROKE', 'FILL', 'BOTH']
   :param h: Hue, (in [0, 1], optional)
   :type h: float
   :param s: Saturation, (in [0, 2], optional)
   :type s: float
   :param v: Value, (in [0, 2], optional)
   :type v: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: vertex_color_invert(*, mode='BOTH')

   Invert RGB values

   :param mode: Mode, (optional)
   :type mode: Literal['STROKE', 'FILL', 'BOTH']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: vertex_color_levels(*, mode='BOTH', offset=0.0, gain=1.0)

   Adjust levels of vertex colors

   :param mode: Mode, (optional)
   :type mode: Literal['STROKE', 'FILL', 'BOTH']
   :param offset: Offset, Value to add to colors (in [-1, 1], optional)
   :type offset: float
   :param gain: Gain, Value to multiply colors by (in [0, inf], optional)
   :type gain: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: vertex_color_set(*, mode='BOTH', factor=1.0)

   Set active color to all selected vertices

   :param mode: Mode, (optional)
   :type mode: Literal['STROKE', 'FILL', 'BOTH']
   :param factor: Factor, Mix Factor (in [0, 1], optional)
   :type factor: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: vertex_group_normalize()

   Normalize weights of the active vertex group

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: vertex_group_normalize_all(*, lock_active=True)

   Normalize the weights of all vertex groups, so that for each vertex, the sum of all weights is 1.0

   :param lock_active: Lock Active, Keep the values of the active group while normalizing others (optional)
   :type lock_active: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: vertex_group_smooth(*, factor=0.5, repeat=1)

   Smooth the weights of the active vertex group

   :param factor: Factor, (in [0, 1], optional)
   :type factor: float
   :param repeat: Iterations, (in [1, 10000], optional)
   :type repeat: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: vertexmode_toggle(*, back=False)

   Enter/Exit vertex paint mode for Grease Pencil strokes

   :param back: Return to Previous Mode, Return to previous mode (optional)
   :type back: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: weight_brush_stroke(*, stroke=None, mode='NORMAL', brush_toggle='None', pen_flip=False)

   Draw weight on stroke points in the active Grease Pencil object

   :param stroke: Stroke, (optional)
   :type stroke: :class:`bpy_prop_collection`\ [:class:`OperatorStrokeElement`] | None
   :param mode: Stroke Mode, Action taken when a paint stroke is made (optional)

      - ``NORMAL``
        Regular -- Apply brush normally.
      - ``INVERT``
        Invert -- Invert action of brush for duration of stroke.
   :type mode: Literal['NORMAL', 'INVERT']
   :param brush_toggle: Temporary Brush Toggle Type, Brush to use for duration of stroke (optional)

      - ``None``
        None -- Apply brush normally.
      - ``SMOOTH``
        Smooth -- Switch to smooth brush for duration of stroke.
      - ``ERASE``
        Erase -- Switch to erase brush for duration of stroke.
      - ``MASK``
        Mask -- Switch to mask brush for duration of stroke.
   :type brush_toggle: Literal['None', 'SMOOTH', 'ERASE', 'MASK']
   :param pen_flip: Pen Flip, Whether a tablet's eraser mode is being used (optional)
   :type pen_flip: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: weight_invert()

   Invert the weight of active vertex group

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: weight_sample()

   Set the weight of the Draw tool to the weight of the vertex under the mouse cursor

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: weight_toggle_direction()

   Toggle Add/Subtract for the weight paint draw tool

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: weightmode_toggle(*, back=False)

   Enter/Exit weight paint mode for Grease Pencil strokes

   :param back: Return to Previous Mode, Return to previous mode (optional)
   :type back: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

