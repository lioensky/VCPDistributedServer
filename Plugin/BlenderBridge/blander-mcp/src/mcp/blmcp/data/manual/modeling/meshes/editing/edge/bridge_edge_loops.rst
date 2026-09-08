.. _bpy.ops.mesh.bridge_edge_loops:
.. _modeling-meshes-editing-bridge-edge-loops:

*****************
Bridge Edge Loops
*****************

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Edge --> Bridge Edge Loops`

Deletes any selected faces, then creates new faces between two or more selected edge loops.

.. note::

   In Blender terminology, an *edge loop* is any chain of connected edges --
   it doesn't have to be a closed loop. See :ref:`bpy.ops.mesh.loop_select`.

Options
=======

Connect Loops
   Open Loop
      The last edge loop is not connected back to the first.
   Closed Loop
      The last edge loop is connected back to the first.
   Loop Pairs
      The first edge loop is connected to the second, the third to the fourth, and so on.
Merge
   Instead of creating faces, merges all the edge loops (or each pair of edge loops if *Loop Pairs*
   is selected) into a single edge loop.
Merge Factor
   When set to 0, the loops are merged into the first loop. When set to 1, they're merged into the last.
   Other values result in interpolation.
Twist
   Offsets the choice of target vertex which each source vertex is connected to.
   This makes the generated tube twist along its axis.
Number of Cuts
   The number of intermediate edge loops to create between each pair of existing edge loops.
Interpolation
   How to calculate the new edge loops when *Number of Cuts* is greater than zero.

   Linear
      Create the new edge loops in a straight line.
   Blend Path
      Create the new edge loops along a Bézier spline, disregarding any neighboring surfaces.
   Blend Surface
      Create the new edge loop vertices along Bézier splines, taking into account the normals
      of neighboring surfaces.

   .. list-table::

      * - .. figure:: /images/modeling_meshes_editing_edge_bridge-edge-loops_interpolation-before.png

             Before bridging

        - .. figure:: /images/modeling_meshes_editing_edge_bridge-edge-loops_interpolation-linear.png

             Linear

        - .. figure:: /images/modeling_meshes_editing_edge_bridge-edge-loops_interpolation-blend-path.png

             Blend Path

        - .. figure:: /images/modeling_meshes_editing_edge_bridge-edge-loops_interpolation-blend-surface.png

             Blend Surface

Smoothness
   Smoothness factor for the *Blend Path* and *Blend Surface* interpolations. A value of 1 uses full
   Bézier splines, while a value of 0 is essentially the same as using *Linear*.
Profile Factor
   Strength factor for the *Profile Shape*. A negative value will shrink each tube segment in the middle,
   while a positive value will inflate it.
Profile Shape
   How to vary the thickness of each tube segment from one original edge loop to the next.
   See the :ref:`Proportional Editing <bpy.types.ToolSettings.proportional_edit_falloff>` page
   for a description of each option.

Examples
========

Bridging two edge loops with the same number of vertices:

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_edge_bridge-edge-loops_simple-before.png
          :width: 320px

          Input.

     - .. figure:: /images/modeling_meshes_editing_edge_bridge-edge-loops_simple-after.png
          :width: 320px

          Bridge result.

Bridging edge loops with different numbers of vertices:

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_edge_bridge-edge-loops_uneven-before.png
          :width: 320px

          Input.

     - .. figure:: /images/modeling_meshes_editing_edge_bridge-edge-loops_uneven-after.png
          :width: 320px

          Bridge result.

Cutting holes in surfaces and connecting them:

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_edge_bridge-edge-loops_faces-before.png
          :width: 320px

          Input.

     - .. figure:: /images/modeling_meshes_editing_edge_bridge-edge-loops_faces-after.png
          :width: 320px

          Bridge result.

Connecting a series of loops in one go:

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_edge_bridge-edge-loops_multi-before.png
          :width: 320px

          Input.

     - .. figure:: /images/modeling_meshes_editing_edge_bridge-edge-loops_multi-after.png
          :width: 320px

          Bridge result.

Using *Blend Surface* interpolation to connect textured surfaces:

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_edge_bridge-edge-loops_advanced-before.png
          :width: 320px

          Input.

     - .. figure:: /images/modeling_meshes_editing_edge_bridge-edge-loops_advanced-after.png
          :width: 320px

          Bridge result.

.. seealso::

   :doc:`/modeling/meshes/editing/face/grid_fill`
