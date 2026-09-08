Texture Operators
=================

.. module:: bpy.ops.texture

.. function:: new()

   Add a new texture

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: slot_copy()

   Copy the material texture settings and nodes

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: slot_move(*, type='UP')

   Move texture slots up and down

   :param type: Type, (optional)
   :type type: Literal['UP', 'DOWN']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: slot_paste()

   Paste the texture settings and nodes

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
