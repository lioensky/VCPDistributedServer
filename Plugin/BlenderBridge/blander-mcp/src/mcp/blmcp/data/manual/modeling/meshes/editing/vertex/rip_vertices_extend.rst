.. _bpy.ops.mesh.rip_edge_move:
.. _tool-mesh-rip_edge:

***********************
Rip Vertices and Extend
***********************

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Vertex --> Rip Vertices and Extend`
   :Shortcut:  :kbd:`Alt-D`

This tool "rips" (duplicates) the outermost vertices of the selected edges, then creates new edges
between these copies and their originals. The neighboring faces stay connected and are "extended"
with the new vertices, turning them into n-gons.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_vertex_rip-vertices-extend_before.png

          Before ripping.

     - .. figure:: /images/modeling_meshes_editing_vertex_rip-vertices-extend_after.png

          After ripping.

When run on border vertices, the result is similar to :doc:`/modeling/meshes/editing/edge/extrude_edges`,
except that (again) the existing faces are merely extended with new vertices. No new faces are created.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_vertex_rip-vertices-extend_border-before.png

          Before ripping.

     - .. figure:: /images/modeling_meshes_editing_vertex_rip-vertices-extend_border-after.png

          After ripping.
