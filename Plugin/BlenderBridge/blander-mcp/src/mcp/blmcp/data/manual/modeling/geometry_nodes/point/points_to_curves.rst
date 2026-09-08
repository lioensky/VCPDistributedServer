.. index:: Geometry Nodes; Points to Curves
.. _bpy.types.GeometryNodePointsToCurves:

*********************
Points to Curves Node
*********************

.. figure:: /images/node-types_GeometryNodePointsToCurves.webp
   :align: right
   :alt: Points to Curves node.
   :width: 250px

The *Points to Curves* node generates a :doc:`Curves </modeling/curves/introduction>` geometry by taking all
points and inserting them to new curves. All :doc:`Attributes </modeling/geometry_nodes/attributes_reference>`
from points are propagated to :ref:`Curve Points <attribute-domains>`.
:ref:`Built-in <geometry-nodes_builtin-attributes>` curves attributes stored in points will be ignored.

.. tip::

   To simplify thinking about points, attributes and their positions in each curve,
   The weight of each point in curve can be associated with a point attributes value.
   The sorting and grouping will be reflected on the attributes as like on the Weight and Group ID.


Inputs
======

Points
   The Point Cloud geometry component.

Curve Group ID
   All points with the same Group ID value will be joined in the same curve.
   The value of Group ID can be any value (negative, zero, or infinity, etc.).
   All created curves must have at least a single point.
   The order of curves depends both on Group ID value and on the order of Group ID values in the Point Cloud.

Weight
   If the curve contains more than one Point, the Weight of each Point is used to define the
   order of all points in curve via sorting. The goal of sorting is to have points with the minimal
   Weight value at the start of curve and the maximum Weight at the end of curve.

.. note::

   If points of curve have the same Weight value, the order will be the same as its original relative location.
   Without any Weight and Group ID inputs, each point will have the same indices in the curve.


Outputs
=======

Curves
   The curves with all copied points from the Point Cloud,
   but joined in curves. All other components aren't saved.
   The resulting curves are always non-cyclic.


Examples
========

.. figure:: /images/modeling_geometry-nodes_points-to-curves.png

The above example creates a curve Array with connections between curves.
This is created by duplicating the :doc:`Arc primitive </modeling/geometry_nodes/curve/primitives/arc>`
curve with the :doc:`/modeling/geometry_nodes/geometry/operations/duplicate_elements`.
Each curve is shifted in a top direction based on its index value.
All the curves are converted to the Point Cloud by the
:doc:`/modeling/geometry_nodes/curve/operations/curve_to_points`.
Finally, the points are converted to curves by the Points to Curves node.

All the Points of the resulting Curves geometry have the same
attributes as points on the initial Arc primitive.
