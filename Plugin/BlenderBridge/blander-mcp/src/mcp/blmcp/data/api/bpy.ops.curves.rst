Curves Operators
================

.. module:: bpy.ops.curves

.. function:: add_bezier(*, radius=1.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Add new Bézier curve

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

.. function:: add_circle(*, radius=1.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Add new circle curve

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

.. function:: attribute_set(*, value_float=0.0, value_float_vector_2d=(0.0, 0.0), value_float_vector_3d=(0.0, 0.0, 0.0), value_int=0, value_int_vector_2d=(0, 0), value_color=(1.0, 1.0, 1.0, 1.0), value_bool=False)

   Set values of the active attribute for selected elements

   :param value_float: Value, (in [-inf, inf], optional)
   :type value_float: float
   :param value_float_vector_2d: Value, (array of 2 items, in [-inf, inf], optional)
   :type value_float_vector_2d: Sequence[float]
   :param value_float_vector_3d: Value, (array of 3 items, in [-inf, inf], optional)
   :type value_float_vector_3d: Sequence[float]
   :param value_int: Value, (in [-inf, inf], optional)
   :type value_int: int
   :param value_int_vector_2d: Value, (array of 2 items, in [-inf, inf], optional)
   :type value_int_vector_2d: Sequence[int]
   :param value_color: Value, (array of 4 items, in [-inf, inf], optional)
   :type value_color: Sequence[float]
   :param value_bool: Value, (optional)
   :type value_bool: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: convert_from_particle_system()

   Add a new curves object based on the current state of the particle system

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: convert_to_particle_system()

   Add a new or update an existing hair particle system on the surface object

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: curve_type_set(*, type='POLY', use_handles=False)

   Set type of selected curves

   :param type: Type, Curve type (optional)
   :type type: Literal[:ref:`rna_enum_curves_type_items`]
   :param use_handles: Handles, Take handle information into account in the conversion (optional)
   :type use_handles: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: cyclic_toggle()

   Make active curve closed/open loop

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: delete()

   Remove selected control points or curves

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: draw(*, error_threshold=0.0, fit_method='REFIT', corner_angle=1.22173, use_cyclic=True, stroke=None, wait_for_input=True, is_curve_2d=False, bezier_as_nurbs=False)

   Draw a freehand curve

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
   :param is_curve_2d: Curve 2D, (optional)
   :type is_curve_2d: bool
   :param bezier_as_nurbs: As NURBS, (optional)
   :type bezier_as_nurbs: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: duplicate()

   Copy selected points or curves

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: duplicate_move(*, CURVES_OT_duplicate={}, TRANSFORM_OT_translate={})

   Make copies of selected elements and move them

   :param CURVES_OT_duplicate: Duplicate, Copy selected points or curves (optional, :func:`bpy.ops.curves.duplicate` keyword arguments)
   :type CURVES_OT_duplicate: dict[str, Any]
   :param TRANSFORM_OT_translate: Move, Move selected items (optional, :func:`bpy.ops.transform.translate` keyword arguments)
   :type TRANSFORM_OT_translate: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: extrude()

   Extrude selected control point(s)

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: extrude_move(*, CURVES_OT_extrude={}, TRANSFORM_OT_translate={})

   Extrude curve and move result

   :param CURVES_OT_extrude: Extrude, Extrude selected control point(s) (optional, :func:`bpy.ops.curves.extrude` keyword arguments)
   :type CURVES_OT_extrude: dict[str, Any]
   :param TRANSFORM_OT_translate: Move, Move selected items (optional, :func:`bpy.ops.transform.translate` keyword arguments)
   :type TRANSFORM_OT_translate: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: handle_type_set(*, type='AUTO')

   Set the handle type for bezier curves

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

.. function:: pen(*, extend=False, deselect=False, toggle=False, deselect_all=False, select_passthrough=False, extrude_point=False, extrude_handle='VECTOR', delete_point=False, insert_point=False, move_segment=False, select_point=False, move_point=False, cycle_handle_type=False, size=0.01)

   Construct and edit Bézier curves

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

.. function:: sculptmode_toggle()

   Enter/Exit sculpt mode for curves

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

.. function:: select_ends(*, amount_start=0, amount_end=1)

   Select end points of curves

   :param amount_start: Amount Front, Number of points to select from the front (in [0, inf], optional)
   :type amount_start: int
   :param amount_end: Amount Back, Number of points to select from the back (in [0, inf], optional)
   :type amount_end: int
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
.. function:: select_linked_pick(*, deselect=False)

   Select all points in the curve under the cursor

   :param deselect: Deselect, Deselect linked control points rather than selecting them (optional)
   :type deselect: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_more()

   Grow the selection by one point

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select_random(*, seed=0, probability=0.5)

   Randomize existing selection or create new random selection

   :param seed: Seed, Source of randomness (in [-inf, inf], optional)
   :type seed: int
   :param probability: Probability, Chance of every point or curve being included in the selection (in [0, 1], optional)
   :type probability: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: separate()

   Separate selected geometry into a new object

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: set_selection_domain(*, domain='POINT')

   Change the mode used for selection masking in curves sculpt mode

   :param domain: Domain, (optional)
   :type domain: Literal[:ref:`rna_enum_attribute_curves_domain_items`]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: snap_curves_to_surface(*, attach_mode='NEAREST')

   Move curves so that the first point is exactly on the surface mesh

   :param attach_mode: Attach Mode, How to find the point on the surface to attach to (optional)

      - ``NEAREST``
        Nearest -- Find the closest point on the surface for the root point of every curve and move the root there.
      - ``DEFORM``
        Deform -- Re-attach curves to a deformed surface using the existing attachment information. This only works when the topology of the surface mesh has not changed.
   :type attach_mode: Literal['NEAREST', 'DEFORM']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: split()

   Split selected points

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: subdivide(*, number_cuts=1)

   Subdivide selected curve segments

   :param number_cuts: Number of Cuts, (in [1, 1000], optional)
   :type number_cuts: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: surface_set()

   Use the active object as surface for selected curves objects and set it as the parent

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: switch_direction()

   Reverse the direction of the selected curves

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: tilt_clear()

   Clear the tilt of selected control points

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
