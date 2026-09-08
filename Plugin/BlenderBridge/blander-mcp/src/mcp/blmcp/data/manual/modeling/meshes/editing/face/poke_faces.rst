.. _bpy.ops.mesh.poke:

**********
Poke Faces
**********

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Face --> Poke Faces`

Splits each selected face into a triangle fan with a newly created vertex in the middle.
This new vertex can further be raised or lowered to create a pyramid/cone.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_face_poke-faces_before.png

          Before poking.

     - .. figure:: /images/modeling_meshes_editing_face_poke-faces_after.png

          After poking.

     - .. figure:: /images/modeling_meshes_editing_face_poke-faces_offset.png

          Adding a Poke Offset.

Options
=======

Poke Offset
   Distance to move the new center vertex along the face normal.
Offset Relative
   Make the *Poke Offset* relative to face size. More specifically, this multiplies the offset
   for each face by the average distance from its center to its corners.
Poke Center
   How to determine the position of the face center:

   Weighted Median
      Use the average position of the face corners, weighted by the lengths of those
      corners' neighboring edges.
   Median
      Use the average position of the face corners.
   Bounds
      Use the center of the bounding box.
