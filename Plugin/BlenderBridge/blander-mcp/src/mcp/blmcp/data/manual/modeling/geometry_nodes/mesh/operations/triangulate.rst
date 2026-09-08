.. index:: Geometry Nodes; Triangulate
.. _bpy.types.GeometryNodeTriangulate:

****************
Triangulate Node
****************

.. figure:: /images/node-types_GeometryNodeTriangulate.webp
   :align: right
   :alt: Triangulate Node.

The *Triangulate* node converts all faces in a mesh (quads and n-gons) to triangular faces.
It functions the same as the :ref:`Triangulate <bpy.ops.mesh.quads_convert_to_tris>` tool in Edit Mode.


Inputs
======

Mesh
   Standard geometry input.

Selection
   A standard Boolean selection input to determine which faces will be triangulated.

Quad Method
   :Beauty:
      Split the quads in nice triangles, slower method.
   :Fixed:
      Split the quads on their 1st and 3rd vertices.
   :Fixed Alternate:
      Split the quads on their 2nd and 4th vertices.
   :Shortest Diagonal:
      Split the quads along their shortest diagonal.
   :Longest Diagonal:
      Split the quads along their longest diagonal. This is the preferred mode for cloth simulations.

N-gon Method
   :Beauty:
      Arrange the new triangles nicely, slower method.
   :Clip:
      Split n-gons using an ear-clipping algorithm
      (the same method of tessellation used for viewport display).


Outputs
=======

Mesh
   Standard geometry output.


Example
=======

.. list-table::

   * - .. figure:: /images/modeling_modifiers_generate_triangulate_before.png
          :width: 320px

          Mesh before triangulation.

     - .. figure:: /images/modeling_modifiers_generate_triangulate_after.png
          :width: 320px

          Mesh after triangulation.
