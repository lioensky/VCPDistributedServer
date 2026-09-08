.. index:: Geometry Nodes; Cone
.. _bpy.types.GeometryNodeMeshCone:

*********
Cone Node
*********

.. figure:: /images/node-types_GeometryNodeMeshCone.webp
   :align: right
   :alt: Cone node.

Generates a cone mesh that is optionally truncated.


Inputs
======

Vertices
   Number of vertices in the top and/or bottom circle of the cone.
   No geometry is generated if the number is below three.

Side Segments
   Number of vertically stacked face loops that make up the cone's sides.
   Increasing this will add horizontal cuts.
   No geometry is generated if the number is below one.

Fill Segments
   Number of concentric rings in the top and/or bottom.
   No geometry is generated if the number is below one.

Radius Top
   The radius of the cone's top circle.
   If this is zero, the circle is reduced to a single vertex.

Radius Bottom
   Same as *Radius Top* but for the bottom circle.

Depth
   Height of the generated cone.

.. note::

   If the top and bottom radii are both zero, this node will output a single line.


Properties
==========

Fill Type
   How the circles at the top and bottom are filled with faces when their radius is larger than zero.

   :None: Do not fill the circles.
   :N-Gon: Fill the innermost circles with a single face.
   :Triangles: Fill the innermost circles with triangles connected to a vertex in the center.


Outputs
=======

Mesh
   Standard geometry output.

Top
   A boolean field with a selection of the faces on the top of the cone. If the *Fill Type*
   is set to *None*, this will be a selection of the top edges instead. If *Radius Top*
   is zero, this will be a selection of the top vertex.

Side
   A boolean field with a selection of the faces on the side of the cone.

Bottom
   A boolean field with a selection of the faces on the bottom of the cone. If the *Fill Type*
   is set to *None*, this will be a selection of the bottom edges instead. If *Radius Bottom*
   is zero, this will be a selection of the bottom vertex.

UV Map
   The default UV coordinate of each face corner. This can be connected to the
   :doc:`/modeling/geometry_nodes/attribute/store_named_attribute` for populating a :term:`UV Map`.
