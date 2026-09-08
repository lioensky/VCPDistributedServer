.. _bpy.ops.mesh.solidify:

**************
Solidify Faces
**************

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Face --> Solidify Faces`

Extrudes the selected faces, turning them from an infinitely thin surface into
a :term:`manifold` mesh with volume.

The thickness can be changed in the :ref:`bpy.ops.screen.redo_last` panel:

Thickness
   Amount to offset the newly created surface.
   Positive values move inward relative to the face normals.
   Negative values move outward.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_face_solidify-faces_before.png
          :width: 200px

          Mesh before solidifying.

     - .. figure:: /images/modeling_meshes_editing_face_solidify-faces_after.png
          :width: 200px

          Solidify with a positive thickness.

     - .. figure:: /images/modeling_meshes_editing_face_solidify-faces_after2.png
          :width: 200px

          Solidify with a negative thickness.

.. seealso::

   The :doc:`/modeling/modifiers/generate/solidify` does this non-destructively
   and has many more options.
