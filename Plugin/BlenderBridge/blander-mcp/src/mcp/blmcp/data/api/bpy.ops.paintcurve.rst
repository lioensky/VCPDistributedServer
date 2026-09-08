Paintcurve Operators
====================

.. module:: bpy.ops.paintcurve

.. function:: add_point(*, location=(0, 0))

   Add New Paint Curve Point

   :param location: Location, Location of vertex in area space (array of 2 items, in [0, 32767], optional)
   :type location: Sequence[int]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: add_point_slide(*, PAINTCURVE_OT_add_point={}, PAINTCURVE_OT_slide={})

   Add new curve point and slide it

   :param PAINTCURVE_OT_add_point: Add New Paint Curve Point, Add New Paint Curve Point (optional, :func:`bpy.ops.paintcurve.add_point` keyword arguments)
   :type PAINTCURVE_OT_add_point: dict[str, Any]
   :param PAINTCURVE_OT_slide: Slide Paint Curve Point, Select and slide paint curve point (optional, :func:`bpy.ops.paintcurve.slide` keyword arguments)
   :type PAINTCURVE_OT_slide: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: cursor()

   Place cursor

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: delete_point()

   Remove Paint Curve Point

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: draw()

   Draw curve

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: new()

   Add new paint curve

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select(*, location=(0, 0), toggle=False, extend=False)

   Select a paint curve point

   :param location: Location, Location of vertex in area space (array of 2 items, in [0, 32767], optional)
   :type location: Sequence[int]
   :param toggle: Toggle, (De)select all (optional)
   :type toggle: bool
   :param extend: Extend, Extend selection (optional)
   :type extend: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: slide(*, align=False, select=True)

   Select and slide paint curve point

   :param align: Align Handles, Aligns opposite point handle during transform (optional)
   :type align: bool
   :param select: Select, Attempt to select a point handle before transform (optional)
   :type select: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

