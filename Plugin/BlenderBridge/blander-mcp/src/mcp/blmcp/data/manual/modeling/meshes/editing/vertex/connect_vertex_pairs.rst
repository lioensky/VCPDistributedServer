.. _bpy.ops.mesh.vert_connect:

********************
Connect Vertex Pairs
********************

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Vertex --> Connect Vertex Pairs`

Creates an edge between each pair of selected vertices that share a face, splitting that face in two.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_vertex_connect-vertex-pairs_before.png

          Before.

     - .. figure:: /images/modeling_meshes_editing_vertex_connect-vertex-pairs_after.png

          After.

Unlike :doc:`/modeling/meshes/editing/vertex/connect_vertex_path`, this operator doesn't connect
vertices that are more than one face apart from each other. Also, selection order doesn't matter.
