.. _bpy.ops.mesh.fill_grid:

*********
Grid Fill
*********

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Face --> Grid Fill`

Generates a grid of quads. Two types of input are supported:

- If a (roughly) rectangular loop of edges is selected -- or just two opposing sides of such a loop --
  it generates a grid inside those edges.
- If a (roughly) rectangular patch of faces is selected, it generates a grid replacing those faces.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_face_grid-fill_before.png
          :width: 320px

          Input.

     - .. figure:: /images/modeling_meshes_editing_face_grid-fill_after.png
          :width: 320px

          Grid Fill result.

The operator gives the best results if each pair of opposing sides has the same number of vertices.
However, this is not required.

Options
=======

Span
   The number of columns in the grid. (The number of rows is calculated automatically based on this.)
Offset
   Determines which vertex is the first corner of the grid.
   By default, this is the active vertex. Use this to rotate the grid layout.
Simple Blending
   Use a simpler interpolation algorithm for generating grid geometry.
   This method is better suited for flat surfaces or cases where preserving curvature gives undesirable results.

.. tip::

   Blender may give an error such as "Loops are not connected by wire/boundary edges." The "loops" here
   can be confusing as it is Blender terminology for "chains," not "closed loops." As such, this error
   really means "The selected *edge chains* are not connected to each other; please create more edges
   to form a closed loop."

.. seealso::

   :doc:`/modeling/meshes/editing/edge/bridge_edge_loops`
