Dpaint Operators
================

.. module:: bpy.ops.dpaint

.. function:: bake()

   Bake dynamic paint image sequence surface

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: output_toggle(*, output='A')

   Add or remove Dynamic Paint output data layer

   :param output: Output Toggle, (optional)
   :type output: Literal['A', 'B']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: surface_slot_add()

   Add a new Dynamic Paint surface slot

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: surface_slot_remove()

   Remove the selected surface slot

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: type_toggle(*, type='CANVAS')

   Toggle whether given type is active or not

   :param type: Type, (optional)
   :type type: Literal[:ref:`rna_enum_prop_dynamicpaint_type_items`]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

