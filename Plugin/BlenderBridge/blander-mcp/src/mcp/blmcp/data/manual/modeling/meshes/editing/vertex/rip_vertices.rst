.. _bpy.ops.mesh.rip_move:
.. _tool-mesh-rip_region:

************
Rip Vertices
************

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Vertex --> Rip Vertices`
   :Shortcut:  :kbd:`V`

Cuts the mesh open along two neighboring edges of each selected vertex.
The vertices can then be moved away using the mouse to create a hole.
When they're in the desired position, press :kbd:`LMB` or :kbd:`Return` to
confirm. Alternatively, press :kbd:`RMB` or :kbd:`Esc` to leave them
at their original position (but still disconnected).

When a single vertex is selected, the cutting direction is determined
by the position of the mouse cursor. Otherwise, it's determined by
the orientation of the selected edge(s).

.. note::

   *Rip Vertices* doesn't support "ripping out" entire faces from their
   surroundings. Use :ref:`bpy.ops.mesh.split` instead.

.. seealso::

   :ref:`bpy.ops.mesh.edge_split` only cuts along the selected edges,
   leaving surrounding unselected edges unchanged.

Examples
========

Ripping a single vertex:

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_vertex_rip-vertices_before.png

          Mouse cursor to the right.

     - .. figure:: /images/modeling_meshes_editing_vertex_rip-vertices_after.png

          Ripping results in a vertical cut.

   * - .. figure:: /images/modeling_meshes_editing_vertex_rip-vertices_alt-before.png

          Mouse cursor below.

     - .. figure:: /images/modeling_meshes_editing_vertex_rip-vertices_alt-after.png

          Ripping results in a horizontal cut.

Ripping vertices along edges in one direction:

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_vertex_rip-vertices_edges-before.png

          Vertical edges selected.

     - .. figure:: /images/modeling_meshes_editing_vertex_rip-vertices_edges-after.png

          Ripping cuts vertically regardless of mouse position.

As a less common scenario, it's also possible to cut in multiple directions:

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_vertex_rip-vertices_complexselection-before.png

          Before ripping.

     - .. figure:: /images/modeling_meshes_editing_vertex_rip-vertices_complexselection-after.png

          After ripping.

Ripping multiple disjoint "islands" of vertices, however, is not supported and will result in an error.
