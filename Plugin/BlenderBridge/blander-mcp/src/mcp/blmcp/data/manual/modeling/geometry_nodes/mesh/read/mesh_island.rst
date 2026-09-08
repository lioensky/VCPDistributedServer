.. index:: Geometry Nodes; Mesh Island
.. _bpy.types.GeometryNodeInputMeshIsland:

****************
Mesh Island Node
****************

.. figure:: /images/node-types_GeometryNodeInputMeshIsland.webp
   :align: right
   :alt: Mesh Island Node.

The *Mesh Island* node outputs information about separate connected regions, or "islands" of a mesh.
Whenever two vertices are connected together by an edge, they are considered as part of the same island,
and will have the same *Island Index* output.

This node's behavior is similar to the :ref:`Select Linked <bpy.ops.mesh.select_linked>` operator
in edit mode, or the *Random per Island* output of the
:doc:`Geometry shader node </render/shader_nodes/input/geometry>`.


Inputs
======

This node has no inputs.


Outputs
=======

Island Index
   The index of each vertex's island. Indices are decided based on the
   lowest vertex index contained in each island.

Island Count
   The total number of mesh islands. This is a single value, and does not vary per element.
