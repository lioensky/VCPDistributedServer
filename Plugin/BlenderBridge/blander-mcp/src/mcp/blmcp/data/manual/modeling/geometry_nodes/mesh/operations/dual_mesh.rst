.. index:: Geometry Nodes; Dual Mesh
.. _bpy.types.GeometryNodeDualMesh:

**************
Dual Mesh Node
**************

.. figure:: /images/node-types_GeometryNodeDualMesh.webp
   :align: right
   :alt: Dual Mesh node.

The *Dual Mesh Node* converts a mesh into its dual, i.e. faces are turned into
vertices and vertices are turned into faces. This also means that attributes
which were on the face domain are transferred to the point domain in the dual mesh.

.. warning::

   The Dual Mesh node only works on manifold geometry. To work with non-manifold geometry
   it's best to remesh the geometry first.


Inputs
======

Mesh
   Standard geometry input.

Keep Boundaries
   Keeps the non-manifold boundaries of the input mesh in place, by creating
   extra geometry, and avoiding the dual mesh transformation there.


Output
======

Dual Mesh
   Standard geometry output.


Examples
========

The *Dual Mesh Node* combines nicely with triangulated meshes. In this case
an Ico Sphere is used, which is made up of nice and evenly spaced triangles.

.. figure:: /images/modeling_geometry-nodes_dual-mesh_icosphere.png
