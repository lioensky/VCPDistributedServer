.. index:: Geometry Nodes; Edge Angle
.. _bpy.types.GeometryNodeInputMeshEdgeAngle:

***************
Edge Angle Node
***************

.. figure:: /images/node-types_GeometryNodeInputMeshEdgeAngle.webp
   :align: right
   :alt: Edge Angle Node.

The *Edge Angle* node calculates the angle in radians between two faces that meet at an edge.
For the Face, Face Corner, and Point :ref:`domains <attribute-domains>`,
the node uses simple domain interpolation to move values from the mesh's edges.

.. note::

   The output of this node depends on the density of the mesh. If there are more edges
   closer together and the curvature of the mesh stays the same, the edge angle will
   be different.

Inputs
======

This node has no inputs.


Outputs
=======

Unsigned Angle
   The shortest angle in radians between two faces where they meet at an edge.
   The range of the data is from zero to PI. Flat edges and :term:`Non-manifold`
   edges have an angle of zero. An edge between two faces completely folded
   back on each other has an angle of PI, or 180 degrees.

   .. tip::

      Computing this value is slightly faster than the signed angle, so if there is no need to distinguish
      between convex and concave angles, using this value can provide a performance improvement.

Signed Angle
   The signed angle in radians between two faces where they meet at an edge. Flat edges
   and Non-manifold edges have an angle of zero. Concave angles are positive and convex
   angles are negative.
