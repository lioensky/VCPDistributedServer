Sculpt Curves Operators
=======================

.. module:: bpy.ops.sculpt_curves

.. function:: brush_stroke(*, stroke=None, mode='NORMAL', brush_toggle='None', pen_flip=False)

   Sculpt curves using a brush

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

.. function:: min_distance_edit()

   Change the minimum distance used by the density brush

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select_grow(*, distance=0.1)

   Select curves which are close to curves that are selected already

   :param distance: Distance, By how much to grow the selection (in [-inf, inf], optional)
   :type distance: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_random(*, seed=0, partial=False, probability=0.5, min=0.0, constant_per_curve=True)

   Randomizes existing selection or create new random selection

   :param seed: Seed, Source of randomness (in [-inf, inf], optional)
   :type seed: int
   :param partial: Partial, Allow points or curves to be selected partially (optional)
   :type partial: bool
   :param probability: Probability, Chance of every point or curve being included in the selection (in [0, 1], optional)
   :type probability: float
   :param min: Min, Minimum value for the random selection (in [0, 1], optional)
   :type min: float
   :param constant_per_curve: Constant per Curve, The generated random number is the same for every control point of a curve (optional)
   :type constant_per_curve: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

