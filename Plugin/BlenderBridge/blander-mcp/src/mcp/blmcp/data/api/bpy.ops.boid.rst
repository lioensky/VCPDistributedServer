Boid Operators
==============

.. module:: bpy.ops.boid

.. function:: rule_add(*, type='GOAL')

   Add a boid rule to the current boid state

   :param type: Type, (optional)
   :type type: Literal[:ref:`rna_enum_boidrule_type_items`]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: rule_del()

   Delete current boid rule

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: rule_move_down()

   Move boid rule down in the list

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: rule_move_up()

   Move boid rule up in the list

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: state_add()

   Add a boid state to the particle system

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: state_del()

   Delete current boid state

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: state_move_down()

   Move boid state down in the list

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: state_move_up()

   Move boid state up in the list

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
