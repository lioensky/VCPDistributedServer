.. _bpy.ops.mesh.subdivide_edgering:

*******************
Subdivide Edge-Ring
*******************

.. reference::

   :Mode:      Edit Mode
   :Panel:     :menuselection:`Edge --> Subdivide Edge-Ring`

Subdivides an edge ring with optional interpolation.

.. note::

   In Blender terminology, an *edge ring* is any series of edges that lie on a row of connected faces
   and are perpendicular to the direction of that row. The row *could* form a closed loop,
   but this doesn't have to be the case: it could also just be a "ribbon" instead of a "ring."

   See also :ref:`modeling-meshes-selecting-edge-rings`.

Options
=======

Number of Cuts
   The number of edge loops to create along the edge ring.
Interpolation
   How to place the new edge loops.

   Linear
      Place the new edge loops in a straight line.
   Blend Path
      Place the new edge loops along a Bézier spline, disregarding the surrounding surface.
   Blend Surface
      Place the new edge loop vertices along Bézier splines, taking into account the normals
      of the surrounding surface.

   .. list-table::

      * - .. figure:: /images/modeling_meshes_editing_edge_subdivide-edge-ring_interpolation-before.png

             Before subdividing

        - .. figure:: /images/modeling_meshes_editing_edge_subdivide-edge-ring_interpolation-linear.png

             Linear

        - .. figure:: /images/modeling_meshes_editing_edge_subdivide-edge-ring_interpolation-blend-path.png

             Blend Path

        - .. figure:: /images/modeling_meshes_editing_edge_subdivide-edge-ring_interpolation-blend-surface.png

             Blend Surface

Smoothness
   Smoothness factor for the *Blend Path* and *Blend Surface* interpolations. A value of 1 uses full
   Bézier splines, while a value of 0 is essentially the same as using *Linear*.
Profile Factor
   Strength factor for the *Profile Shape*. A negative value will shrink the edge ring in the middle,
   while a positive value will inflate it.
Profile Shape
   How to vary the thickness of the edge ring between its center and its ends.
   See the :ref:`Proportional Editing <bpy.types.ToolSettings.proportional_edit_falloff>` page
   for a description of each option.
