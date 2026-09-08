.. _bpy.ops.mesh.edge_face_add:

***************************
New Edge/Face from Vertices
***************************

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Vertex --> New Edge/Face from Vertices`
   :Shortcut:  :kbd:`F`

Creates a face between the selected vertices.
If only two vertices are selected, creates an edge instead.

.. seealso::

   - :doc:`Face Fill </modeling/meshes/editing/face/fill>`
   - :doc:`/modeling/meshes/editing/face/grid_fill`
   - :doc:`/modeling/meshes/editing/edge/bridge_edge_loops`

Use Cases
=========

The operator supports the following scenarios:

Edge from Vertices
------------------

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_vertex_make-face-edge_vert-pair-before.png
          :width: 200px

          Before.

     - .. figure:: /images/modeling_meshes_editing_vertex_make-face-edge_vert-pair-after.png
          :width: 200px

          After.

Face from Vertices
------------------

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_vertex_make-face-edge_verts-simple-before.png
          :width: 200px

          Before.

     - .. figure:: /images/modeling_meshes_editing_vertex_make-face-edge_verts-simple-after.png
          :width: 200px

          After.

Face from Edges
---------------

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_vertex_make-face-edge_edge-simple-before.png
          :width: 200px

          Before.

     - .. figure:: /images/modeling_meshes_editing_vertex_make-face-edge_edge-simple-after.png
          :width: 200px

          After.

Face from Vertices and Edges
----------------------------

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_vertex_make-face-edge_mix-simple-before.png
          :width: 200px

          Before.

     - .. figure:: /images/modeling_meshes_editing_vertex_make-face-edge_mix-simple-after.png
          :width: 200px

          After.

N-gon from Vertices
-------------------

Selecting more than four vertices results in a single n-gon.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_vertex_make-face-edge_cloud-before.png
          :width: 200px

          Before.

     - .. figure:: /images/modeling_meshes_editing_vertex_make-face-edge_cloud-after.png
          :width: 200px

          After.


N-gon from Edges
----------------

A chain of edges similarly results in an n-gon, albeit with more control over the shape of the outline.
This does not support holes; see :doc:`Face Fill </modeling/meshes/editing/face/fill>` for an alternative
that does.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_vertex_make-face-edge_ngon-before.png
          :width: 200px

          Before.

     - .. figure:: /images/modeling_meshes_editing_vertex_make-face-edge_ngon-after.png
          :width: 200px

          After.


Patch from Edges
----------------

If there are interior edges, Blender will create multiple faces instead of just one.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_vertex_make-face-edge_net-before.png
          :width: 200px

          Before.

     - .. figure:: /images/modeling_meshes_editing_vertex_make-face-edge_net-after.png
          :width: 200px

          After.


Face from Single Vertex or Edge
-------------------------------

If only a single vertex or edge is selected on the boundary of a hole, Blender creates a face
using the neighboring edges. In addition, only the new edge is selected afterwards,
making it possible to create another face right away.

.. figure:: /images/modeling_meshes_editing_vertex_make-face-edge_create-boundary.png

   Selecting a vertex and pressing F twice in a row.

.. _modeling-mesh-make-face-edge-dissolve:

Dissolve Existing Faces
-----------------------

If multiple existing faces are selected, Blender will :ref:`Dissolve <bpy.ops.mesh.dissolve_faces>`
those faces, merging them into one (instead of creating a new face that overlaps them).
This works for multiple "islands" in one go.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_mesh_delete_dissolve-faces_before.png

          Before dissolving.

     - .. figure:: /images/modeling_meshes_editing_mesh_delete_dissolve-faces_after.png

          After dissolving.
