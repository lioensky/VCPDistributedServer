.. _bpy.ops.mesh.beautify_fill:

**************
Beautify Faces
**************

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Face --> Beautify Faces`

Rearranges the selected faces to obtain cleaner topology.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_face_beautify-faces_before.png
          :width: 320px

          Text converted to a mesh.

     - .. figure:: /images/modeling_meshes_editing_face_beautify-faces_after.png
          :width: 320px

          Result of Beautify Faces.

Options
=======

Max Angle
   Maximum allowed angle between face normals (meaning that two faces that lie in the
   same plane are considered to have an angle of 0°, not 180°). If an edge lies between
   two faces that exceed this angle, it will not be changed.
