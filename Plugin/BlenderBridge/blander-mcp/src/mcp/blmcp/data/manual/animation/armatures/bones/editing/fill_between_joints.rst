.. _bpy.ops.armature.fill:

*******************
Fill Between Joints
*******************

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Armature --> Fill Between Joints`
   :Shortcut:  :kbd:`F`

The main use of this tool is to create one bone between two selected joints by pressing
:kbd:`F`, similar to how in mesh editing you can "create edges/faces".

If you have one root and one tip selected, the new bone:

- Will have the root placed on the selected tip.
- Will have the tip placed on the selected root.
- Will be parented and connected to the bone owning the selected tip.

.. list-table:: Fill between a tip and a root.

   * - .. figure:: /images/animation_armatures_bones_editing_fill-between-joints_example-1.png

          Active tip on the left.

     - .. figure:: /images/animation_armatures_bones_editing_fill-between-joints_example-2.png

          Active tip on the right.

If you have two tips selected, the new bone:

- Will have the root placed on the selected tip closest to the 3D cursor.
- Will have the tip placed on the other selected tip.
- Will be parented and connected to the bone owning the tip used as the new bone's root.

.. list-table:: Fill between tips.

   * - .. figure:: /images/animation_armatures_bones_editing_fill-between-joints_example-3.png

          3D cursor on the left.

     - .. figure:: /images/animation_armatures_bones_editing_fill-between-joints_example-4.png

          3D cursor on the right.

If you have two roots selected, you will face a small problem due to the event system in
Blender not updating the interface in real-time.

When clicking :kbd:`F`, similar to the previous case, you will see a new bone:

- With the root placed on the selected root closest to the 3D cursor.
- With the tip placed on the other selected root.
- Parented and connected to the bone owning the root used as the new bone's root.

If you try to move the new bone, Blender will update the interface and you will see
that the new bone's root moves to the tip of the parent bone.

.. list-table:: Fill between roots.

   * - .. figure:: /images/animation_armatures_bones_editing_fill-between-joints_example-5.png

          Before UI update (3D cursor on the left).

     - .. figure:: /images/animation_armatures_bones_editing_fill-between-joints_example-6.png

          After UI update, correct visualization.

Clicking :kbd:`F` with only one bone joint selected will create a bone from the selected
joint to the 3D cursor position, and it will not parent it to any bone in the armature.

.. list-table:: Fill with only one bone joint selected.

   * - .. figure:: /images/animation_armatures_bones_editing_fill-between-joints_example-7.png

          Fill with only one tip selected.

     - .. figure:: /images/animation_armatures_bones_editing_fill-between-joints_example-8.png

          Fill with only one root selected.

You will get an error when:

- Trying to fill two joints of the same bone.
- Trying to fill more than two bone joints.
