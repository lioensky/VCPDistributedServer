.. _bpy.ops.mesh.subdivide:

*********
Subdivide
*********

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Edge --> Subdivide`

Subdividing adds resolution to the mesh by dividing faces or edges into smaller units.

This process follows a few rules depending on the situation:

- When only one edge of a triangle or :term:`quad` is selected,
  that face is turned into a quad or :term:`N-gon` respectively.
  If the *Create N-Gons* option is disabled, the face is split into triangles instead.
- When two edges of a face are selected:

  - If the face is a triangle, a new edge is created between the two new vertices,
    subdividing the triangle into a triangle and a quad.
  - If the face is a quad and the edges are neighbors, the face is split according
    to the *Quad Corner Type* setting (see below).
  - If the face is a quad and the edges are opposite,
    the quad is just subdivided in two quads by the edge linking the two new vertices.

- When three edges of a face are selected:

  - If the face is a triangle, this means the whole face is selected and
    it is subdivided into four smaller triangles.
  - If the face is a quad, first the two opposite edges are subdivided as described above.
    Then, the "middle" edge is subdivided, affecting its new "sub-quad" as described above for only one edge.

- When all four edges of a quad are selected, the face is subdivided into four smaller quads.
- When one or more edges of an N-gon are selected,
  the individual edges will be subdivided but the face will stay unsubdivided.


Options
=======

These options are available in the :ref:`Adjust Last Operation <bpy.ops.screen.redo_last>` panel after
running the operator:

Number of Cuts
   The number of cuts per edge to make. By default this is 1, cutting edges in half.
   A value of 2 will cut them into thirds, and so on.
Smoothness
   Displaces subdivisions to maintain approximate curvature.
   The effect is similar to the way the :doc:`/modeling/modifiers/generate/subdivision_surface`
   might deform the mesh.

   .. list-table::

      * - .. figure:: /images/modeling_meshes_editing_edge_subdivide_smooth-before.png
             :width: 200px

             Mesh before subdividing.

        - .. figure:: /images/modeling_meshes_editing_edge_subdivide_smooth-none.png
             :width: 200px

             Subdivided with no smoothing.

        - .. figure:: /images/modeling_meshes_editing_edge_subdivide_smooth-after.png
             :width: 200px

             Subdivided with Smoothness set to 1.

Create N-Gons
   When unchecked, forces the subdivision to create triangles or quads instead of n-gons
   (see examples below).
Quad Corner Type
   Controls the subdivision for quads with two selected, neighboring edges.

   Inner Vertices
      The selected edges are subdivided, then an edge is created between the two new vertices,
      creating a small triangle. This edge is also subdivided,
      and the "inner vertex" thus created is linked by another edge to the one opposite
      to the original selected edges. This results in a triangle and two quads.
   Path
      The selected edges are subdivided, then new edges are created between the new vertices
      as well as the existing outer vertices. This results in two triangles and a quad.
   Straight Cut
      The selected edges are subdivided, then an edge is created between
      the two new vertices, creating a small triangle and N-gon.
      If *Create N-Gons* is unchecked, this option works like *Inner Vertices* instead.
   Fan
      The quad is subdivided into a fan of a quad and two triangles,
      the common vertex being the one opposite to the selected edges.

   .. list-table::

      * - .. figure:: /images/modeling_meshes_editing_edge_subdivide_two-edges-quad-innervert.png
             :width: 200px

             Inner Vertices corner type.
        - .. figure:: /images/modeling_meshes_editing_edge_subdivide_two-edges-quad-path.png
             :width: 200px

             Path corner type.
        - .. figure:: /images/modeling_meshes_editing_edge_subdivide_two-edges-quad-straight_cut.png
             :width: 200px

             Straight Cut corner type.
        - .. figure:: /images/modeling_meshes_editing_edge_subdivide_two-edges-quad-fan2.png
             :width: 200px

             Fan corner type.
Fractal
   Displaces the vertices in random directions after the mesh is subdivided.

   .. list-table::

      * - .. figure:: /images/modeling_meshes_editing_edge_subdivide_fractal-before.png
             :width: 200px

             Plane before subdivision.

        - .. figure:: /images/modeling_meshes_editing_edge_subdivide_fractal-none.png
             :width: 200px

             Regular subdivision.

        - .. figure:: /images/modeling_meshes_editing_edge_subdivide_fractal-after1.png
             :width: 200px

             Same mesh with fractal added.

Along Normal
   Causes the vertices to move along their normals, instead of random directions.

   .. figure:: /images/modeling_meshes_editing_edge_subdivide_fractal-along-normal.png
      :width: 200px

      Along Normal set to 1.

Random Seed
   Changes the random seed of the *Fractal* noise function, producing a different result for each seed value.

   .. figure:: /images/modeling_meshes_editing_edge_subdivide_fractal-after2.png
      :width: 200px

      Same mesh with a different seed value.

.. seealso::

   :doc:`/modeling/meshes/editing/mesh/transform/randomize` randomly displaces vertices without
   subdividing first.

Examples
========

Below are some examples illustrating edge subdivision in various scenarios.

.. figure:: /images/modeling_meshes_editing_edge_subdivide_before.png
   :width: 300px

   The sample mesh.


One Edge
--------

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_edge_subdivide_one-edge.png
          :width: 250px

          One edge.

     - .. figure:: /images/modeling_meshes_editing_edge_subdivide_one-edge-tri.png
          :width: 250px

          *Create N-Gons* unchecked.


Two Tri Edges
-------------

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_edge_subdivide_two-edges-tri.png
          :width: 250px

          Two tri edges.

     - .. figure:: /images/modeling_meshes_editing_edge_subdivide_two-edges-tri-tri.png
          :width: 250px

          *Create N-Gons* unchecked.


Two Opposite Quad Edges
-----------------------

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_edge_subdivide_two-edges-opposite.png
          :width: 250px

          Two quad edges.

     - .. figure:: /images/modeling_meshes_editing_edge_subdivide_two-edges-opposite-tri.png
          :width: 250px

          *Create N-Gons* unchecked.


Two Adjacent Quad Edges
-----------------------

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_edge_subdivide_two-edges-quad-innervert.png
          :width: 250px

          Inner Vertices corner type.

     - .. figure:: /images/modeling_meshes_editing_edge_subdivide_two-edges-quad-innervert-tri.png
          :width: 250px

          *Create N-Gons* unchecked.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_edge_subdivide_two-edges-quad-path.png
          :width: 250px

          Path corner type.

     - .. figure:: /images/modeling_meshes_editing_edge_subdivide_two-edges-quad-path-tri.png
          :width: 250px

          *Create N-Gons* unchecked.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_edge_subdivide_two-edges-quad-straight_cut.png
          :width: 250px

          Straight Cut corner type.

     - .. figure:: /images/modeling_meshes_editing_edge_subdivide_two-edges-quad-innervert-tri.png
          :width: 250px

          *Create N-Gons* unchecked.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_edge_subdivide_two-edges-quad-fan2.png
          :width: 250px

          Fan cut type.

     - .. figure:: /images/modeling_meshes_editing_edge_subdivide_two-edges-quad-fan.png
          :width: 250px

          *Create N-Gons* unchecked.


Three Quad Edges
----------------

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_edge_subdivide_three-edges.png
          :width: 250px

          Three edges.

     - .. figure:: /images/modeling_meshes_editing_edge_subdivide_three-edges-tri.png
          :width: 250px

          *Create N-Gons* unchecked.


Full Triangle
-------------

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_edge_subdivide_three-edges-tri2.png
          :width: 250px

          Full triangle.

     - .. figure:: /images/modeling_meshes_editing_edge_subdivide_three-edges-tri-tri.png
          :width: 250px

          *Create N-Gons* unchecked.


Full Quad
---------

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_edge_subdivide_four-edges.png
          :width: 250px

          Full quad.

     - .. figure:: /images/modeling_meshes_editing_edge_subdivide_four-edges-tri.png
          :width: 250px

          *Create N-Gons* unchecked.


Multiple Cuts
-------------

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_edge_subdivide_tri-multi.png
          :width: 250px

          Triangle with two cuts.

     - .. figure:: /images/modeling_meshes_editing_edge_subdivide_quad-multi.png
          :width: 250px

          Quad with two cuts.
