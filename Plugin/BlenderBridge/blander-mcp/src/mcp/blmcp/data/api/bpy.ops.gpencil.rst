Gpencil Operators
=================

.. module:: bpy.ops.gpencil

.. function:: annotate(*, mode='DRAW', arrowstyle_start='NONE', arrowstyle_end='NONE', use_stabilizer=False, stabilizer_factor=0.75, stabilizer_radius=35, stroke=None, wait_for_input=True)

   Make annotations on the active data

   :param mode: Mode, Way to interpret mouse movements (optional)

      - ``DRAW``
        Draw Freehand -- Draw freehand stroke(s).
      - ``DRAW_STRAIGHT``
        Draw Straight Lines -- Draw straight line segment(s).
      - ``DRAW_POLY``
        Draw Poly Line -- Click to place endpoints of straight line segments (connected).
      - ``ERASER``
        Eraser -- Erase Annotation strokes.
   :type mode: Literal['DRAW', 'DRAW_STRAIGHT', 'DRAW_POLY', 'ERASER']
   :param arrowstyle_start: Start Arrow Style, Stroke start style (optional)

      - ``NONE``
        None -- Don't use any arrow/style in corner.
      - ``ARROW``
        Arrow -- Use closed arrow style.
      - ``ARROW_OPEN``
        Open Arrow -- Use open arrow style.
      - ``ARROW_OPEN_INVERTED``
        Segment -- Use perpendicular segment style.
      - ``DIAMOND``
        Square -- Use square style.
   :type arrowstyle_start: Literal['NONE', 'ARROW', 'ARROW_OPEN', 'ARROW_OPEN_INVERTED', 'DIAMOND']
   :param arrowstyle_end: End Arrow Style, Stroke end style (optional)

      - ``NONE``
        None -- Don't use any arrow/style in corner.
      - ``ARROW``
        Arrow -- Use closed arrow style.
      - ``ARROW_OPEN``
        Open Arrow -- Use open arrow style.
      - ``ARROW_OPEN_INVERTED``
        Segment -- Use perpendicular segment style.
      - ``DIAMOND``
        Square -- Use square style.
   :type arrowstyle_end: Literal['NONE', 'ARROW', 'ARROW_OPEN', 'ARROW_OPEN_INVERTED', 'DIAMOND']
   :param use_stabilizer: Stabilize Stroke, Helper to draw smooth and clean lines. Press Shift for an invert effect (even if this option is not active) (optional)
   :type use_stabilizer: bool
   :param stabilizer_factor: Stabilizer Stroke Factor, Higher values give a smoother stroke (in [0, 1], optional)
   :type stabilizer_factor: float
   :param stabilizer_radius: Stabilizer Stroke Radius, Minimum distance from last point before stroke continues (in [0, 200], optional)
   :type stabilizer_radius: int
   :param stroke: Stroke, (optional)
   :type stroke: :class:`bpy_prop_collection`\ [:class:`OperatorStrokeElement`] | None
   :param wait_for_input: Wait for Input, Wait for first click instead of painting immediately (optional)
   :type wait_for_input: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: annotation_active_frame_delete()

   Delete the active frame for the active Annotation Layer

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: annotation_add()

   Add new Annotation data-block

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: data_unlink()

   Unlink active Annotation data-block

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: layer_annotation_add()

   Add new Annotation layer or note for the active data-block

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: layer_annotation_move(*, type='UP')

   Move the active Annotation layer up/down in the list

   :param type: Type, (optional)
   :type type: Literal['UP', 'DOWN']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: layer_annotation_remove()

   Remove active Annotation layer

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
