Ptcache Operators
=================

.. module:: bpy.ops.ptcache

.. function:: add()

   Add new cache

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: bake(*, bake=False)

   Bake physics

   :param bake: Bake, (optional)
   :type bake: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: bake_all(*, bake=True)

   Bake all physics

   :param bake: Bake, (optional)
   :type bake: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: bake_from_cache()

   Bake from cache

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: free_bake()

   Delete physics bake

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: free_bake_all()

   Delete all baked caches of all objects in the current scene

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: remove()

   Delete current cache

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
