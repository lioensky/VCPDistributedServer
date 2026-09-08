Curve Operators
===============

.. module:: bpy.ops.curve

.. function:: cyclic_toggle(*, direction='CYCLIC_U')

   Make active spline closed/open loop

   :param direction: Direction, Direction to make surface cyclic in (optional)
   :type direction: Literal['CYCLIC_U', 'CYCLIC_V']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: de_select_first()

   (De)select first of visible part of each NURBS

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: de_select_last()

   (De)select last of visible part of each NURBS

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: decimate(*, ratio=1.0)

   Simplify selected curves

   :param ratio: Ratio, (in [0, 1], optional)
   :type ratio: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: delete(*, type='VERT')

   Delete selected control points or segments

   :param type: Type, Which elements to delete (optional)
   :type type: Literal['VERT', 'SEGMENT']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: dissolve_verts()

   Delete selected control points, correcting surrounding handles

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: draw(*, error_threshold=0.0, fit_method='REFIT', corner_angle=1.22173, use_cyclic=True, stroke=None, wait_for_input=True)

   Draw a freehand spline

   :param error_threshold: Error, Error distance threshold (in object units) (in [0, 10], optional)
   :type error_threshold: float
   :param fit_method: Fit Method, (optional)
   :type fit_method: Literal[:ref:`rna_enum_curve_fit_method_items`]
   :param corner_angle: Corner Angle, (in [0, 3.14159], optional)
   :type corner_angle: float
   :param use_cyclic: Cyclic, (optional)
   :type use_cyclic: bool
   :param stroke: Stroke, (optional)
   :type stroke: :class:`bpy_prop_collection`\ [:class:`OperatorStrokeElement`] | None
   :param wait_for_input: Wait for Input, (optional)
   :type wait_for_input: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: duplicate()

   Duplicate selected control points

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: duplicate_move(*, CURVE_OT_duplicate={}, TRANSFORM_OT_translate={})

   Duplicate curve and move

   :param CURVE_OT_duplicate: Duplicate Curve, Duplicate selected control points (optional, :func:`bpy.ops.curve.duplicate` keyword arguments)
   :type CURVE_OT_duplicate: dict[str, Any]
   :param TRANSFORM_OT_translate: Move, Move selected items (optional, :func:`bpy.ops.transform.translate` keyword arguments)
   :type TRANSFORM_OT_translate: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: extrude(*, mode='TRANSLATION')

   Extrude selected control point(s)

   :param mode: Mode, (optional)
   :type mode: Literal[:ref:`rna_enum_transform_mode_type_items`]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: extrude_move(*, CURVE_OT_extrude={}, TRANSFORM_OT_translate={})

   Extrude curve and move result

   :param CURVE_OT_extrude: Extrude, Extrude selected control point(s) (optional, :func:`bpy.ops.curve.extrude` keyword arguments)
   :type CURVE_OT_extrude: dict[str, Any]
   :param TRANSFORM_OT_translate: Move, Move selected items (optional, :func:`bpy.ops.transform.translate` keyword arguments)
   :type TRANSFORM_OT_translate: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: handle_type_set(*, type='AUTOMATIC')

   Set type of handles for selected control points

   :param type: Type, Spline type (optional)
   :type type: Literal['AUTOMATIC', 'VECTOR', 'ALIGNED', 'FREE_ALIGN', 'TOGGLE_FREE_ALIGN']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: hide(*, unselected=False)

   Hide (un)selected control points

   :param unselected: Unselected, Hide unselected rather than selected (optional)
   :type unselected: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: make_segment()

   Join two curves by their selected ends

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: match_texture_space()

   Match texture space to object's bounding box

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: normals_make_consistent(*, calc_length=False)

   Recalculate the direction of selected handles

   :param calc_length: Length, Recalculate handle length (optional)
   :type calc_length: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: pen(*, extend=False, deselect=False, toggle=False, deselect_all=False, select_passthrough=False, extrude_point=False, extrude_handle='VECTOR', delete_point=False, insert_point=False, move_segment=False, select_point=False, move_point=False, close_spline=True, close_spline_method='OFF', toggle_vector=False, cycle_handle_type=False)

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
   :param close_spline: Close Spline, Make a spline cyclic by clicking endpoints (optional)
   :type close_spline: bool
   :param close_spline_method: Close Spline Method, The condition for close spline to activate (optional)

      - ``OFF``
        None.
      - ``ON_PRESS``
        On Press -- Move handles after closing the spline.
      - ``ON_CLICK``
        On Click -- Spline closes on release if not dragged.
   :type close_spline_method: Literal['OFF', 'ON_PRESS', 'ON_CLICK']
   :param toggle_vector: Toggle Vector, Toggle between Vector and Auto handles (optional)
   :type toggle_vector: bool
   :param cycle_handle_type: Cycle Handle Type, Cycle between all four handle types (optional)
   :type cycle_handle_type: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: primitive_bezier_circle_add(*, radius=1.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Construct a Bézier Circle

   :param radius: Radius, (in [0, inf], optional)
   :type radius: float
   :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object (optional)
   :type enter_editmode: bool
   :param align: Align, The alignment of the new object (optional)

      - ``WORLD``
        World -- Align the new object to the world.
      - ``VIEW``
        View -- Align the new object to the view.
      - ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: Literal['WORLD', 'VIEW', 'CURSOR']
   :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type rotation: :class:`mathutils.Euler` | Sequence[float]
   :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type scale: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: primitive_bezier_curve_add(*, radius=1.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Construct a Bézier Curve

   :param radius: Radius, (in [0, inf], optional)
   :type radius: float
   :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object (optional)
   :type enter_editmode: bool
   :param align: Align, The alignment of the new object (optional)

      - ``WORLD``
        World -- Align the new object to the world.
      - ``VIEW``
        View -- Align the new object to the view.
      - ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: Literal['WORLD', 'VIEW', 'CURSOR']
   :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type rotation: :class:`mathutils.Euler` | Sequence[float]
   :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type scale: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: primitive_nurbs_circle_add(*, radius=1.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Construct a Nurbs Circle

   :param radius: Radius, (in [0, inf], optional)
   :type radius: float
   :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object (optional)
   :type enter_editmode: bool
   :param align: Align, The alignment of the new object (optional)

      - ``WORLD``
        World -- Align the new object to the world.
      - ``VIEW``
        View -- Align the new object to the view.
      - ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: Literal['WORLD', 'VIEW', 'CURSOR']
   :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type rotation: :class:`mathutils.Euler` | Sequence[float]
   :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type scale: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: primitive_nurbs_curve_add(*, radius=1.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Construct a Nurbs Curve

   :param radius: Radius, (in [0, inf], optional)
   :type radius: float
   :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object (optional)
   :type enter_editmode: bool
   :param align: Align, The alignment of the new object (optional)

      - ``WORLD``
        World -- Align the new object to the world.
      - ``VIEW``
        View -- Align the new object to the view.
      - ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: Literal['WORLD', 'VIEW', 'CURSOR']
   :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type rotation: :class:`mathutils.Euler` | Sequence[float]
   :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type scale: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: primitive_nurbs_path_add(*, radius=1.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Construct a Path

   :param radius: Radius, (in [0, inf], optional)
   :type radius: float
   :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object (optional)
   :type enter_editmode: bool
   :param align: Align, The alignment of the new object (optional)

      - ``WORLD``
        World -- Align the new object to the world.
      - ``VIEW``
        View -- Align the new object to the view.
      - ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: Literal['WORLD', 'VIEW', 'CURSOR']
   :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type rotation: :class:`mathutils.Euler` | Sequence[float]
   :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type scale: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: radius_set(*, radius=1.0)

   Set per-point radius which is used for bevel tapering

   :param radius: Radius, (in [0, inf], optional)
   :type radius: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: reveal(*, select=True)

   Reveal hidden control points

   :param select: Select, (optional)
   :type select: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_all(*, action='TOGGLE')

   (De)select all control points

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

.. function:: select_less()

   Deselect control points at the boundary of each selection region

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select_linked()

   Select all control points linked to the current selection

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select_linked_pick(*, deselect=False)

   Select all control points linked to already selected ones

   :param deselect: Deselect, Deselect linked control points rather than selecting them (optional)
   :type deselect: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_more()

   Select control points at the boundary of each selection region

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select_next()

   Select control points following already selected ones along the curves

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select_nth(*, skip=1, nth=1, offset=0)

   Deselect every Nth point starting from the active one

   :param skip: Deselected, Number of deselected elements in the repetitive sequence (in [1, inf], optional)
   :type skip: int
   :param nth: Selected, Number of selected elements in the repetitive sequence (in [1, inf], optional)
   :type nth: int
   :param offset: Offset, Offset from the starting point (in [-inf, inf], optional)
   :type offset: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_previous()

   Select control points preceding already selected ones along the curves

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select_random(*, ratio=0.5, seed=0, action='SELECT')

   Randomly select some control points

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

.. function:: select_row()

   Select a row of control points including active one. Successive use on the same point switches between U/V directions

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select_similar(*, type='WEIGHT', compare='EQUAL', threshold=0.1)

   Select similar curve points by property type

   :param type: Type, (optional)
   :type type: Literal['TYPE', 'RADIUS', 'WEIGHT', 'DIRECTION']
   :param compare: Compare, (optional)
   :type compare: Literal['EQUAL', 'GREATER', 'LESS']
   :param threshold: Threshold, (in [0, inf], optional)
   :type threshold: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: separate()

   Separate selected points from connected unselected points into a new object

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: shade_flat()

   Set shading to flat

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: shade_smooth()

   Set shading to smooth

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: shortest_path_pick()

   Select shortest path between two selections

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: smooth()

   Flatten angles of selected points

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: smooth_radius()

   Interpolate radii of selected points

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: smooth_tilt()

   Interpolate tilt of selected points

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: smooth_weight()

   Interpolate weight of selected points

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: spin(*, center=(0.0, 0.0, 0.0), axis=(0.0, 0.0, 0.0))

   Extrude selected boundary row around pivot point and current view axis

   :param center: Center, Center in global view space (array of 3 items, in [-inf, inf], optional)
   :type center: :class:`mathutils.Vector` | Sequence[float]
   :param axis: Axis, Axis in global view space (array of 3 items, in [-1, 1], optional)
   :type axis: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: spline_type_set(*, type='POLY', use_handles=False)

   Set type of active spline

   :param type: Type, Spline type (optional)
   :type type: Literal['POLY', 'BEZIER', 'NURBS']
   :param use_handles: Handles, Use handles when converting Bézier curves into polygons (optional)
   :type use_handles: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: spline_weight_set(*, weight=1.0)

   Set softbody goal weight for selected points

   :param weight: Weight, (in [0, 1], optional)
   :type weight: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: split()

   Split off selected points from connected unselected points

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: subdivide(*, number_cuts=1)

   Subdivide selected segments

   :param number_cuts: Number of Cuts, (in [1, 1000], optional)
   :type number_cuts: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: switch_direction()

   Switch direction of selected splines

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: tilt_clear()

   Clear the tilt of selected control points

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: vertex_add(*, location=(0.0, 0.0, 0.0))

   Add a new control point (linked to only selected end-curve one, if any)

   :param location: Location, Location to add new vertex at (array of 3 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

