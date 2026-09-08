Mball Operators
===============

.. module:: bpy.ops.mball

.. function:: delete_metaelems(*, confirm=True)

   Delete selected metaball element(s)

   :param confirm: Confirm, Prompt for confirmation (optional)
   :type confirm: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: duplicate_metaelems()

   Duplicate selected metaball element(s)

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: duplicate_move(*, MBALL_OT_duplicate_metaelems={}, TRANSFORM_OT_translate={})

   Make copies of the selected metaball elements and move them

   :param MBALL_OT_duplicate_metaelems: Duplicate Metaball Elements, Duplicate selected metaball element(s) (optional, :func:`bpy.ops.mball.duplicate_metaelems` keyword arguments)
   :type MBALL_OT_duplicate_metaelems: dict[str, Any]
   :param TRANSFORM_OT_translate: Move, Move selected items (optional, :func:`bpy.ops.transform.translate` keyword arguments)
   :type TRANSFORM_OT_translate: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: hide_metaelems(*, unselected=False)

   Hide (un)selected metaball element(s)

   :param unselected: Unselected, Hide unselected rather than selected (optional)
   :type unselected: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: reveal_metaelems(*, select=True)

   Reveal all hidden metaball elements

   :param select: Select, (optional)
   :type select: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_all(*, action='TOGGLE')

   Change selection of all metaball elements

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

.. function:: select_random_metaelems(*, ratio=0.5, seed=0, action='SELECT')

   Randomly select metaball elements

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

.. function:: select_similar(*, type='TYPE', threshold=0.1)

   Select similar metaballs by property types

   :param type: Type, (optional)
   :type type: Literal['TYPE', 'RADIUS', 'STIFFNESS', 'ROTATION']
   :param threshold: Threshold, (in [0, inf], optional)
   :type threshold: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

