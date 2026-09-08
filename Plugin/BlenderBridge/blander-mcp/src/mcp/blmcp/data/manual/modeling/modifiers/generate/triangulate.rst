.. index:: Modeling Modifiers; Triangulate Modifier
.. _bpy.types.TriangulateModifier:

********************
Triangulate Modifier
********************

The *Triangulate* modifier converts all faces in a mesh (quads and n-gons) to triangular faces.
It fulfills the exact same function as the :ref:`Triangulate <bpy.ops.mesh.quads_convert_to_tris>` tool in Edit Mode.

.. list-table::

   * - .. figure:: /images/modeling_modifiers_generate_triangulate_before.png
          :width: 320px

          Mesh before Triangulate modifier.

     - .. figure:: /images/modeling_modifiers_generate_triangulate_after.png
          :width: 320px

          Mesh after Triangulate modifier.


Options
=======

.. figure:: /images/modeling_modifiers_generate_triangulate_panel.png
   :align: right
   :width: 300px

   The Triangulate modifier.

Quad Method
   Beauty
      Split the quads in nice triangles, slower method.
   Fixed
      Split the quads on their 1st and 3rd vertices.
   Fixed Alternate
      Split the quads on their 2nd and 4th vertices.
   Shortest Diagonal
      Split the quads along their shortest diagonal.
   Longest Diagonal
      Split the quads along their longest diagonal. This is the preferred mode for cloth simulations.

N-gon Method
   Beauty
      Arrange the new triangles nicely, slower method.
   Clip
      Splits n-gons using an ear-clipping algorithm
      (the same method of tessellation used for viewport display).

Minimum Vertices
   Minimum number of vertices a face must have to be triangulated.
   For example, setting this value to 5, will prevent triangulation of :term:`Quads <Quad>`
   and only triangulate :term:`N-gons <N-gon>`.
