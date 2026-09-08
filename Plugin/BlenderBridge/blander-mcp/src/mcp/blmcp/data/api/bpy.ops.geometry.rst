Geometry Operators
==================

.. module:: bpy.ops.geometry

.. function:: attribute_add(*, name="", domain='POINT', data_type='FLOAT')

   Add attribute to geometry

   :param name: Name, Name of new attribute (optional, never None)
   :type name: str
   :param domain: Domain, Type of element that attribute is stored on (optional)
   :type domain: Literal[:ref:`rna_enum_attribute_domain_items`]
   :param data_type: Data Type, Type of data stored in attribute (optional)
   :type data_type: Literal[:ref:`rna_enum_attribute_type_items`]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: attribute_convert(*, mode='GENERIC', domain='POINT', data_type='FLOAT')

   Change how the attribute is stored

   :param mode: Mode, (optional)
   :type mode: Literal['GENERIC', 'VERTEX_GROUP']
   :param domain: Domain, Which geometry element to move the attribute to (optional)
   :type domain: Literal[:ref:`rna_enum_attribute_domain_items`]
   :param data_type: Data Type, (optional)
   :type data_type: Literal[:ref:`rna_enum_attribute_type_items`]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: attribute_remove()

   Remove attribute from geometry

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: color_attribute_add(*, name="", domain='POINT', data_type='FLOAT_COLOR', color=(0.0, 0.0, 0.0, 1.0))

   Add color attribute to geometry

   :param name: Name, Name of new color attribute (optional, never None)
   :type name: str
   :param domain: Domain, Type of element that attribute is stored on (optional)
   :type domain: Literal[:ref:`rna_enum_color_attribute_domain_items`]
   :param data_type: Data Type, Type of data stored in attribute (optional)
   :type data_type: Literal[:ref:`rna_enum_color_attribute_type_items`]
   :param color: Color, Default fill color (array of 4 items, in [0, inf], optional)
   :type color: Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: color_attribute_convert(*, domain='POINT', data_type='FLOAT_COLOR')

   Change how the color attribute is stored

   :param domain: Domain, Type of element that attribute is stored on (optional)
   :type domain: Literal[:ref:`rna_enum_color_attribute_domain_items`]
   :param data_type: Data Type, Type of data stored in attribute (optional)
   :type data_type: Literal[:ref:`rna_enum_color_attribute_type_items`]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: color_attribute_duplicate()

   Duplicate color attribute

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: color_attribute_remove()

   Remove color attribute from geometry

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: color_attribute_render_set(*, name="Color")

   Set default color attribute used for rendering

   :param name: Name, Name of color attribute (optional, never None)
   :type name: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: geometry_randomization(*, value=False)

   Toggle geometry randomization for debugging purposes

   :param value: Value, Randomize the order of geometry elements (e.g. vertices or edges) after some operations where there are no guarantees about the order. This avoids accidentally depending on something that may change in the future (optional)
   :type value: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

