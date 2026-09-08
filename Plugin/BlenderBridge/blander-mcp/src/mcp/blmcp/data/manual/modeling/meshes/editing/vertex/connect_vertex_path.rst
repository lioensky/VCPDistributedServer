.. _bpy.ops.mesh.vert_connect_path:

*******************
Connect Vertex Path
*******************

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Vertex --> Connect Vertex Path`
   :Shortcut:  :kbd:`J`

Creates edges between vertices in the order they are selected, splitting faces along the way.
Running the operator a second time closes the loop.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_vertex_connect-vertex-path_multi-before.png

          Before.

     - .. figure:: /images/modeling_meshes_editing_vertex_connect-vertex-path_multi-after.png

          First execution.

     - .. figure:: /images/modeling_meshes_editing_vertex_connect-vertex-path_multi-loop.png

          Second execution.

It's also possible to create a path of edges along vertices that are isolated (not part of
any edges or faces).

.. seealso::

   The :doc:`/modeling/meshes/editing/mesh/knife_topology_tool` offers a more interactive
   way of splitting faces. Unlike *Connect Vertex Path*, however, it makes cuts that are
   perfectly straight as seen from the current viewpoint.
