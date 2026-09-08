Lattice Operators
=================

.. module:: bpy.ops.lattice

.. function:: flip(*, axis='U')

   Mirror all control points without inverting the lattice deform

   :param axis: Flip Axis, Coordinates along this axis get flipped (optional)
   :type axis: Literal['U', 'V', 'W']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: make_regular()

   Set UVW control points a uniform distance apart

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select_all(*, action='TOGGLE')

   Change selection of all UVW control points

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

   Deselect vertices at the boundary of each selection region

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select_mirror(*, axis={'X'}, extend=False)

   Select mirrored lattice points

   :param axis: Axis, (optional)
   :type axis: set[Literal[:ref:`rna_enum_axis_flag_xyz_items`]]
   :param extend: Extend, Extend the selection (optional)
   :type extend: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_more()

   Select vertices directly linked to already selected ones

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select_random(*, ratio=0.5, seed=0, action='SELECT')

   Randomly select UVW control points

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

.. function:: select_ungrouped(*, extend=False)

   Select vertices without a group

   :param extend: Extend, Extend the selection (optional)
   :type extend: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

