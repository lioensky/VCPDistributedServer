.. _bpy.ops.mesh.intersect:

*****************
Intersect (Knife)
*****************

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Face --> Intersect (Knife)`

Creates new edges along the lines where faces intersect.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_face_intersect-knife_before.png

          Before intersect.

     - .. figure:: /images/modeling_meshes_editing_face_intersect-knife_after.png

          After intersect.

.. seealso::

   :doc:`/modeling/meshes/editing/face/intersect_boolean` in *Union* mode doesn't
   just create intersection edges, but also removes faces that end up enclosed in a volume.

Options
=======

Source
   Self Intersect
      Intersect selected faces with other selected faces.
   Selected/Unselected
      Intersect selected faces with unselected faces.

Separate Mode
   Whether to disconnect faces from each other after edge creation.

   :All: Disconnect all faces at each intersection edge.
   :Cut: If *Source* is set to *Selected/Unselected*, only disconnect the selected faces
         from the unselected ones. Otherwise, this option does the same as *All*.
   :Merge: Connect all faces at each intersection edge.

.. list-table::
   :widths: 1 1 1

   * - .. figure:: /images/modeling_meshes_editing_face_intersect-knife_separate-all.png

          Separate All: the cylinder and the plane stay separate and are each split in two.

     - .. figure:: /images/modeling_meshes_editing_face_intersect-knife_separate-cut.png

          Separate Cut: the cylinder and the plane stay separate.

     - .. figure:: /images/modeling_meshes_editing_face_intersect-knife_separate-merge.png

          Merge: the cylinder and the plane are connected to each other.

Solver
   Algorithm used to calculate the intersections.

   Float
      Uses a simple solver which offers good performance but lacks support for overlapping geometry.

      Merge Threshold
         Tolerance for close faces to be considered touching.
         It may be useful to increase this when some intersections aren't detected that should be and
         when extra geometry is being created because edges aren't detected as overlapping.

         .. warning::

            A threshold approaching the size of faces may cause very slow calculation.
            In general, keep this value small.

   Exact
      Uses a complex solver which offers the best results and has full
      support for overlapping geometry, but is much slower.
