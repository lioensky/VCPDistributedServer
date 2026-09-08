.. index:: Geometry Nodes; Blur Attribute
.. _bpy.types.GeometryNodeBlurAttribute:

*******************
Blur Attribute Node
*******************

.. figure:: /images/node-types_GeometryNodeBlurAttribute.webp
   :align: right
   :alt: Blur Attribute node.
   :width: 300px

The *Blur Attribute* node smooths attribute values between neighboring geometry elements.

The goal of each step is mixing values of each element with its neighbors.
The weight for element is factor for multiplying all neighbor's values before accumulating them as new primitive
value.

Blurring will only work with certain geometry types and :ref:`attribute domains <attribute-domains>`.
Therefore, the attribute can only be affected on the :doc:`Meshes </modeling/meshes/introduction>` and
:doc:`Curves </modeling/curves/introduction>` components.

The domains this node works on is based on the :ref:`field context <field-context>` of the node's evaluation.
Only domains with explicit relations with their neighbors will work with this node.
Explicit relations for correct blurring are vertices, edges, and faces of meshes, and curve control points.

.. note::

   Blurring of face corner attributes is not handled by this node,
   because the ideal behavior for mixing face corner values is not clear.

All :ref:`attribute data types <attribute-data-types>` are supported except
for boolean attributes.


Inputs
======

Value
   The immediate value of each primitive to blur.

Iterations
   Number of repetitions of mixing value with neighbors. Each iteration is independent.
   Until one iteration is completed, its results are not used as a source for next blurring.

Weight
   Weight of each primitive.


Properties
==========

Data Type
   The :ref:`data type <attribute-data-types>` used for the evaluated data.


Outputs
=======

Value
   Values, mixed with neighbors defined number of times.


Examples
========

.. figure:: /images/modeling_geometry-nodes_blur_attribute-attribute_example.png

Input is Mesh Plane. First :doc:`/modeling/geometry_nodes/mesh/operations/subdivide_mesh` add some
faces for capture color with :doc:`/modeling/geometry_nodes/utilities/random_value`
used as hue in :doc:`/modeling/geometry_nodes/color/combine_color` on this.
Now second :doc:`/modeling/geometry_nodes/mesh/operations/subdivide_mesh` split each face on a lot of new.
Each one new duplicates original attribute.
Blur Attribute node mixes all attributes for each face. Due to this, the result is smoothed.
