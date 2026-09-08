.. _modeling-meshes-editing-edges-rotate:
.. _bpy.ops.mesh.edge_rotate:

***********
Rotate Edge
***********

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Edge --> Rotate Edge CW / Rotate Edge CCW`

Restructures the neighboring faces of each selected edge, rotating that edge
clockwise (CW) or counterclockwise (CCW).

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_edge_rotate-edge_flip-before.png
          :width: 320px

          Selected edge.

     - .. figure:: /images/modeling_meshes_editing_edge_rotate-edge_flip-after.png
          :width: 320px

          Edge rotated CCW.

It's also possible to select pairs of adjacent faces, in which case each pair's shared
edge will be rotated:

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_edge_rotate-edge_face-mode1.png
          :width: 320px

          Two adjacent faces selected.

     - .. figure:: /images/modeling_meshes_editing_edge_rotate-edge_face-mode2.png
          :width: 320px

          Shared edge rotated.
