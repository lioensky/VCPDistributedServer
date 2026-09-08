Attribute(bpy_struct)
=====================

.. currentmodule:: bpy.types


Attributes are used to store data that corresponds to geometry elements.
Geometry elements are items in one of the geometry domains like points, curves, or faces.

An attribute has a ``name``, a ``type``, and is stored on a ``domain``.

``name``
   The name of this attribute. Names have to be unique within the same geometry.
   If the name starts with a ``.``, the attribute is hidden from the UI.
``type``
   The type of data that this attribute stores, e.g. a float, integer, color, etc.
   See `Attribute Type Items <bpy_types_enum_items/attribute_type_items.html>`__.
``domain``
   The geometry domain that the attribute is stored on.
   See `Attribute Domain Items <bpy_types_enum_items/attribute_domain_items.html>`__.


Using Attributes
++++++++++++++++

Attributes can be stored on geometries like :class:`Mesh`, :class:`Curves`, :class:`PointCloud`, etc.
These geometries have attribute groups (usually called ``attributes``).
Using the groups, attributes can then be accessed by their name:

.. code-block:: python

   radii = curves.attributes["radius"]

Creating and storing custom attributes is done using the ``attributes.new`` function:

.. code-block:: python

   # Add a new attribute named `my_attribute_name` of type `float` on the point domain of the geometry.
   my_attribute = curves.attributes.new("my_attribute_name", 'FLOAT', 'POINT')

Removing attributes can be done like so:

.. code-block:: python

   attribute = drawing.attributes["some_attribute"]
   drawing.attributes.remove(attribute)

.. note::

   Some attributes are required and cannot be removed, like ``"position"``.

Attribute values are read by accessing their ``attribute.data`` collection property.
However, in cases where multiple values should be read at once,
it is better to use the :class:`bpy_prop_collection.foreach_get` function and read the values into a ``numpy`` buffer.

.. code-block:: python

   import numpy as np

   # Get the radius attribute.
   radii = curves.attributes["radius"]
   # Print the radius of the first point.
   print(radii.data[0].value)
   # Output: 0.005

   # Get the total number of points.
   num_points = attributes.domain_size('POINT')
   # Create an empty buffer to read all the radii into.
   radii_data = np.zeros(num_points, dtype=np.float32)
   # Read all the radii of the curves into `radii_data` at once.
   radii.data.foreach_get('value', radii_data)
   # Print all the radii.
   print(radii_data)
   # Output: [0.1, 0.2, 0.3, 0.4, ... ]

.. note::

   Some attribute types use different named properties to access their value.
   Instead of ``value``, vectors use ``vector``, and colors use ``color``.

Writing to different attribute types is very similar. You can simply assign to a value directly.
Again, when writing to multiple values, it is recommended to use the :class:`bpy_prop_collection.foreach_set` function
to write the values from a ``numpy`` buffer.

.. code-block:: python

   import numpy as np

   radii = curves.attributes["radius"]
   # Write a radius with a value of 0.5 to the first point.
   radii.data[0].value = 0.5
   print(radii.data[0].value)
   # Output: 0.5

   num_points = attributes.domain_size('POINT')
   # Generate random radii with values between 0.001 and 0.05 using numpy.
   new_radii = np.random.uniform(0.001, 0.05, num_points)
   # Write the new radii to the radius attribute.
   radii.data.foreach_set('value', new_radii)


The :class:`bpy_prop_collection.foreach_get` / :class:`bpy_prop_collection.foreach_set` methods require a flat array.
This is sometimes not desirable, e.g. when reading/writing positions, which are 3D vectors.
In these cases, it's possible to use ``np.ravel`` to pass the data as a flat array:

.. code-block:: python

   num_points = attributes.domain_size('POINT')
   positions = curves.attributes['position']
   # Here, we're using a numpy array with shape (num_points, 3) so that each
   # element is a 3d vector.
   positions_data = np.zeros((num_points, 3), dtype=np.float32)
   # The `np.ravel` function will pass the `positions_data` as a flat array
   # without changing the original shape.
   positions.data.foreach_get('vector', np.ravel(positions_data))
   print(positions_data)
   # Output: [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], ...]

base class --- :class:`bpy_struct`

subclasses --- 
:class:`BoolAttribute`, :class:`ByteColorAttribute`, :class:`ByteIntAttribute`, :class:`Float2Attribute`, :class:`Float4x4Attribute`, :class:`FloatAttribute`, :class:`FloatColorAttribute`, :class:`FloatVectorAttribute`, :class:`Int2Attribute`, :class:`IntAttribute`, :class:`QuaternionAttribute`, :class:`Short2Attribute`, :class:`StringAttribute`

.. class:: Attribute(bpy_struct)

   Geometry attribute

   .. data:: data_type

      Type of data stored in attribute (default ``'FLOAT'``, readonly)

      :type: Literal[:ref:`rna_enum_attribute_type_items`]

   .. data:: domain

      Domain of the Attribute (default ``'POINT'``, readonly)

      :type: Literal[:ref:`rna_enum_attribute_domain_items`]

   .. data:: is_internal

      The attribute is meant for internal use by Blender (default False, readonly)

      :type: bool

   .. data:: is_required

      Whether the attribute can be removed or renamed (default False, readonly)

      :type: bool

   .. attribute:: name

      Name of the Attribute (default "", never None)

      :type: str

   .. data:: storage_type

      Method used to store the data (default ``'ARRAY'``, readonly)

      :type: Literal[:ref:`rna_enum_attr_storage_type_items`]

   .. classmethod:: bl_rna_get_subclass(id, default=None, /)
   
      :param id: The RNA type identifier.
      :type id: str
      :param default: The value to return when not found.
      :type default: :class:`bpy.types.Struct` | None
      :return: The RNA type or default when not found.
      :rtype: :class:`bpy.types.Struct`


   .. classmethod:: bl_rna_get_subclass_py(id, default=None, /)
   
      :param id: The RNA type identifier.
      :type id: str
      :param default: The value to return when not found.
      :type default: type | None
      :return: The class or default when not found.
      :rtype: type


Inherited Properties
--------------------

.. hlist::
   :columns: 2

   - :class:`bpy_struct.id_data`

Inherited Functions
-------------------

.. hlist::
   :columns: 2

   - :class:`bpy_struct.as_pointer`
   - :class:`bpy_struct.driver_add`
   - :class:`bpy_struct.driver_remove`
   - :class:`bpy_struct.get`
   - :class:`bpy_struct.id_properties_clear`
   - :class:`bpy_struct.id_properties_ensure`
   - :class:`bpy_struct.id_properties_ui`
   - :class:`bpy_struct.is_property_hidden`
   - :class:`bpy_struct.is_property_overridable_library`
   - :class:`bpy_struct.is_property_readonly`
   - :class:`bpy_struct.is_property_set`
   - :class:`bpy_struct.items`
   - :class:`bpy_struct.keyframe_delete`
   - :class:`bpy_struct.keyframe_insert`
   - :class:`bpy_struct.keys`
   - :class:`bpy_struct.path_from_id`
   - :class:`bpy_struct.path_from_module`
   - :class:`bpy_struct.path_resolve`
   - :class:`bpy_struct.pop`
   - :class:`bpy_struct.property_overridable_library_set`
   - :class:`bpy_struct.property_unset`
   - :class:`bpy_struct.rna_ancestors`
   - :class:`bpy_struct.type_recast`
   - :class:`bpy_struct.values`

References
----------

.. hlist::
   :columns: 2

   - :class:`AttributeGroupCurves.active`
   - :class:`AttributeGroupCurves.new`
   - :class:`AttributeGroupCurves.remove`
   - :class:`AttributeGroupGreasePencil.active`
   - :class:`AttributeGroupGreasePencil.new`
   - :class:`AttributeGroupGreasePencil.remove`
   - :class:`AttributeGroupGreasePencilDrawing.active`
   - :class:`AttributeGroupGreasePencilDrawing.new`
   - :class:`AttributeGroupGreasePencilDrawing.remove`
   - :class:`AttributeGroupMesh.active`
   - :class:`AttributeGroupMesh.active_color`
   - :class:`AttributeGroupMesh.new`
   - :class:`AttributeGroupMesh.remove`
   - :class:`AttributeGroupPointCloud.active`
   - :class:`AttributeGroupPointCloud.new`
   - :class:`AttributeGroupPointCloud.remove`
   - :class:`Curves.attributes`
   - :class:`Curves.color_attributes`
   - :class:`GreasePencil.attributes`
   - :class:`GreasePencil.color_attributes`
   - :class:`GreasePencilDrawing.attributes`
   - :class:`GreasePencilDrawing.color_attributes`
   - :class:`Mesh.attributes`
   - :class:`Mesh.color_attributes`
   - :class:`PointCloud.attributes`
   - :class:`PointCloud.color_attributes`

