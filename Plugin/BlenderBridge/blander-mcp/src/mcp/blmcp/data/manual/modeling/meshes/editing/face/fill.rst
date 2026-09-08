.. _bpy.ops.mesh.fill:
.. _modeling-meshes-editing-fill:

****
Fill
****

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Face --> Fill`
   :Shortcut:  :kbd:`Alt-F`

Fills a closed loop of selected edges with triangular faces.
This also supports holes:

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_face_fill_holes.png
          :width: 320px

          Before filling.

     - .. figure:: /images/modeling_meshes_editing_face_fill_holes-filled.png
          :width: 320px

          After filling.

.. seealso::

   :doc:`/modeling/meshes/editing/vertex/make_face_edge` fills a set of edges
   (or vertices) with a single :term:`n-gon`.
