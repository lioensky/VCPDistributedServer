.. _bpy.ops.mesh.convex_hull:

***********
Convex Hull
***********

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Convex Hull`

Creates a convex hull surrounding the selected vertices.
Original edges and faces that lie on this hull may be reused.

This operator can also serve as an alternative for
:doc:`/modeling/meshes/editing/edge/bridge_edge_loops`.

.. figure:: /images/modeling_meshes_editing_mesh_convex-hull_example.png

   Input mesh, loose vertices, and Convex Hull result for both.

Options
=======

Delete Unused
   Removes vertices, edges, and faces that were selected, but not used as part of the hull.
   Note that vertices and edges that are used
   by other edges and faces not part of the selection will not be deleted.

Use Existing Faces
   Where possible, use existing faces that lie on the hull.
   This allows the hull to contain n-gons rather than just triangles and quads.

Make Holes
   Delete edges and faces that were reused.
   Useful in cases like bridging to delete faces between the existing mesh and the convex hull.

Join Triangles
   The hull is initially generated using only triangles; this option tries to join them into quads.
   Has all the same properties as the :ref:`bpy.ops.mesh.tris_convert_to_quads`
   operator (angle limit, compare UVs, etc.).

Max Face Angle, Max Shape Angle, Compare
   See :ref:`bpy.ops.mesh.tris_convert_to_quads`.
