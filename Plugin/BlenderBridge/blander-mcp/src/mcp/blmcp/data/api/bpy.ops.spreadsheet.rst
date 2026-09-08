Spreadsheet Operators
=====================

.. module:: bpy.ops.spreadsheet

.. function:: add_row_filter_rule()

   Add a filter to remove rows from the displayed data

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: change_spreadsheet_data_source(*, component_type=0, attribute_domain_type=0)

   Change visible data source in the spreadsheet

   :param component_type: Component Type, (in [0, 32767], optional)
   :type component_type: int
   :param attribute_domain_type: Attribute Domain Type, (in [0, 32767], optional)
   :type attribute_domain_type: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: fit_column()

   Resize a spreadsheet column to the width of the data

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: remove_row_filter_rule(*, index=0)

   Remove a row filter from the rules

   :param index: Index, (in [0, inf], optional)
   :type index: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: reorder_columns()

   Change the order of columns

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: resize_column()

   Resize a spreadsheet column

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: toggle_pin()

   Turn on or off pinning

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/spreadsheet.py\:21 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/spreadsheet.py#L21>`__

