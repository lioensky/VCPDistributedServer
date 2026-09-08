Palette Operators
=================

.. module:: bpy.ops.palette

.. function:: color_add()

   Add new color to active palette

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: color_delete()

   Remove active color from palette

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: color_move(*, type='UP')

   Move the active Color up/down in the list

   :param type: Type, (optional)
   :type type: Literal['UP', 'DOWN']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: extract_from_image(*, threshold=1)

   Extract all colors used in Image and create a Palette

   :param threshold: Threshold, (in [-inf, inf], optional)
   :type threshold: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: join(*, palette="")

   Join Palette Swatches

   :param palette: Palette, Name of the Palette (optional, never None)
   :type palette: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: new()

   Add new palette

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: sort(*, type='HSV')

   Sort Palette Colors

   :param type: Type, (optional)
   :type type: Literal['HSV', 'SVH', 'VHS', 'LUMINANCE']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

