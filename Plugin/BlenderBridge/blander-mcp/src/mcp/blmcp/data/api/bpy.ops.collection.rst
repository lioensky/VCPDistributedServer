Collection Operators
====================

.. module:: bpy.ops.collection

.. function:: create(*, name="")

   Create an object collection from selected objects

   :param name: Name, Name of the new collection (optional, never None)
   :type name: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: export_all()

   Invoke all configured exporters on this collection

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: exporter_add(*, name="")

   Add exporter to the exporter list

   :param name: Name, FileHandler idname (optional, never None)
   :type name: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: exporter_export(*, index=0)

   Invoke the export operation

   :param index: Index, Exporter index (in [0, inf], optional)
   :type index: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: exporter_move(*, direction='UP')

   Move exporter up or down in the exporter list

   :param direction: Direction, Direction to move the active exporter (optional)
   :type direction: Literal['UP', 'DOWN']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: exporter_remove(*, index=0)

   Remove exporter from the exporter list

   :param index: Index, Exporter index (in [0, inf], optional)
   :type index: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: objects_add_active(*, collection='')

   Add selected objects to one of the collections the active-object is part of. Optionally add to "All Collections" to ensure selected objects are included in the same collections as the active object

   :param collection: Collection, The collection to add other selected objects to (optional)
   :type collection: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: objects_remove(*, collection='')

   Remove selected objects from a collection

   :param collection: Collection, The collection to remove this object from (optional)
   :type collection: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: objects_remove_active(*, collection='')

   Remove the object from an object collection that contains the active object

   :param collection: Collection, The collection to remove other selected objects from (optional)
   :type collection: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: objects_remove_all()

   Remove selected objects from all collections

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
