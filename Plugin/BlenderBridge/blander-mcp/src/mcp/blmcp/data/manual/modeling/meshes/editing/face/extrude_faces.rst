.. _bpy.ops.view3d.edit_mesh_extrude_individual_move:
.. _bpy.ops.view3d.edit_mesh_extrude_move_normal:

*************
Extrude Faces
*************

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Face --> Extrude Faces`,
               :menuselection:`Mesh --> Extrude --> Extrude Faces`
   :Shortcut:  :kbd:`E`

This tool creates new faces around the border of the selected faces,
then allows moving the selected faces along an axis using the mouse.
The result is an extrusion: a square gets turned into a box, a disc
into a cylinder, and so on. This is used very often in modeling and can
serve to add limbs to characters, branches to trees, and so on.

Once the faces are in place, press :kbd:`LMB` or :kbd:`Return` to confirm.
Pressing :kbd:`RMB` or :kbd:`Esc` will cancel the move and leave the selected faces
at their original location, but the newly created faces will still be there.

By default, the extrusion axis is the average of the face normals,
but this :doc:`/scene_layout/object/editing/transform/control/axis_locking` can be
changed by pressing an axis key (:kbd:`X`, :kbd:`Y`, or :kbd:`Z`):

- Press once to use the corresponding global axis.
- Press twice to use the average of the faces' local axes.
- Press three times to disable axis locking (allows moving the faces anywhere).

.. list-table::

   * - .. figure:: /images/modeling_meshes_tools_extrude-region_face-before.png
          :width: 200px

          Selected face.

     - .. figure:: /images/modeling_meshes_tools_extrude-region_face-after.png
          :width: 200px

          During extrude.

     - .. figure:: /images/modeling_meshes_tools_extrude-region_face-after-zaxis.png
          :width: 200px

          Using the global Z axis.

After extruding, the following options are available in the :ref:`bpy.ops.screen.redo_last` panel:

Flip Normals
   Flip the normals of the newly created faces, as they might be pointing the wrong way
   depending on the extrusion direction. See the :ref:`bpy.types.View3DOverlay.show_face_orientation`
   overlay of the 3D Viewport to check whether they are correct.

Dissolve Orthogonal Edges
   When enabled, newly created faces will be merged with surrounding existing faces
   (potentially turning them into :term:`n-gons <n-gon>`) *if* they form a flat surface together.

:doc:`Orientation </editors/3dview/controls/orientation>`
   Determines the extrusion axis to use.

Mirror Editing
   Enabling this option moves the corresponding faces on the other side of the mesh *without*
   extruding them, making it not very useful here.

:doc:`Proportional Editing </editors/3dview/controls/proportional_editing>`
   Enabling this option moves the surrounding unselected faces together with the extruded ones,
   making it not very useful here.
