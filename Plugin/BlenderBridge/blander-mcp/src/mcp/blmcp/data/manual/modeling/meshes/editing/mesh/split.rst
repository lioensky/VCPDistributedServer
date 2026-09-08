*****
Split
*****

The *Split* menu can be accessed as a popover by pressing :kbd:`Alt-M`.

These operators are about splitting meshes by disconnecting faces from each other.
For splitting faces into smaller ones, see the :doc:`/modeling/meshes/editing/mesh/knife_topology_tool`
or the :doc:`/modeling/meshes/editing/vertex/connect_vertex_path` operator.

.. _bpy.ops.mesh.split:

Split Selection
===============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Split --> Selection`
   :Shortcut:  :kbd:`Y`

Cuts the mesh along the border of the selected faces. The faces can then be moved elsewhere.

This operator can also disconnect "wires" (edges that are not part of a face) from
their surroundings. However, using it on edges that *are* part of a face will simply duplicate them.

.. figure:: /images/modeling_meshes_editing_mesh_split_selection.png

   Disconnecting inner faces from their surroundings.

.. seealso::

   The :doc:`/modeling/meshes/editing/mesh/separate` operator disconnects the selection
   and moves it into a new mesh object.


.. _bpy.ops.mesh.edge_split:

Split Faces by Edges
====================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Split --> Faces by Edges`

Cuts the mesh along the selected edges. The vertices can then be pulled apart to create a hole.

.. figure:: /images/modeling_meshes_editing_mesh_split_faces-by-edges.png

   Splitting by selected edges.

.. seealso::

   :doc:`/modeling/meshes/editing/vertex/rip_vertices` also cuts neighboring unselected edges.

Split Faces & Edges by Vertices
===============================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Split --> Faces & Edges by Vertices`

Cuts the mesh along *all* neighboring edges of each selected vertex. (This is different from
*Rip Vertices* which only cuts two edges per vertex.)

The vertices can then be pulled apart to create a hole.

.. figure:: /images/modeling_meshes_editing_mesh_split_faces-and-edges-by-vertices.png

   Splitting by selected vertices.
