.. _bpy.ops.armature.extrude_move:
.. _bpy.ops.armature.extrude_forked:

*******
Extrude
*******

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Armature --> Extrude`
   :Shortcut:  :kbd:`E`, :kbd:`Shift-E`

When you press :kbd:`E`, for each selected tip
(either explicitly or implicitly), a new bone is created.
This bone will be the child of "its" tip owner, and connected to it. As usual,
once extrusion is done, only the new bones' tips are selected, and in select mode,
so you can place them to your liking. See Fig. :ref:`fig-rig-bones-extrusion`.

.. _fig-rig-bones-extrusion:

.. list-table:: Extrusion example.

   * - .. figure:: /images/animation_armatures_bones_editing_extrude_example-1.png

          An armature with three selected tips.

     - .. figure:: /images/animation_armatures_bones_editing_extrude_example-2.png

          The three extruded bones.

You also can use the rotating/scaling extrusions,
as with meshes, by pressing respectively :kbd:`E R` and :kbd:`E S` --
as well as :doc:`locked </scene_layout/object/editing/transform/control/axis_locking>`
extrusion along a global or local axis.

.. _fig-rig-bone-mirror:

.. list-table:: Mirror extrusion example.

   * - .. figure:: /images/animation_armatures_bones_editing_extrude_mirror-1.png

          A single selected bone's tip.

     - .. figure:: /images/animation_armatures_bones_editing_extrude_mirror-2.png

          The two mirror-extruded bones.

Bones have an extra "mirror extruding" tool, called by pressing :kbd:`Shift-E`.
By default, it behaves exactly like the standard extrusion.
But once you have enabled :ref:`bpy.types.Armature.use_mirror_x` editing option,
each extruded tip will produce *two new bones*, having the same name except for the "_L"/ "_R" suffix
(for left/right, see the :ref:`naming conventions <armature-editing-naming-conventions>`).
The "_L" bone behaves like the single one produced by the default extrusion --
you can move, rotate or scale it exactly the same way.
The "_R" bone is its mirror counterpart (along the armature's local X axis),
see Fig. :ref:`fig-rig-bone-mirror`.

.. important::

   Canceling the extrude action causes the newly created bones to snap back to the source position,
   (creating zero length bones). These will be removed when exiting Edit Mode,
   however, they can cause confusion and it's unlikely you want to keep them.
   If you realize the problem immediately, undo the extrude action.

In case you are wondering, you cannot just press :kbd:`X` to solve this as you would in mesh editing,
because extrusion selects the newly created tips, and as explained below the Delete tool ignores bones' joints.
To get rid of these extruded bones without undoing, you would have to move the tips,
then select the bones and :ref:`delete <bpy.ops.armature.delete>` them.


.. _bpy.ops.armature.click_extrude:

Mouse Clicks
============

.. reference::

   :Mode:      Edit Mode
   :Shortcut:  :kbd:`Ctrl-RMB`

If at least one bone is selected, :kbd:`Ctrl-RMB`-clicking adds a new bone.

About the new bone's tip:

After you :kbd:`Ctrl-RMB`-clicked it becomes the active element in the armature,
it appears to be right where you clicked, but (as in mesh editing)
it will be on the plane parallel to the view and passing through the 3D cursor.

The position of the root and the parenting of the new bone depends on the active element:

.. figure:: /images/animation_armatures_bones_editing_extrude_mouse-clicks-1.png
   :width: 300px

   :kbd:`Ctrl`\ -clicking when the active element is a bone.

If the active element is a *bone*:

- The new bone's root is placed on the active bone's tip.
- The new bone is parented and connected to the active bone
  (check the Outliner in Fig. :ref:`fig-rig-bone-active-tip`).

.. _fig-rig-bone-active-tip:

.. figure:: /images/animation_armatures_bones_editing_extrude_mouse-clicks-2.png
   :width: 300px

   :kbd:`Ctrl`\ -clicking when the active element is a tip.

If the active element is a *tip*:

- The new bone's root is placed on the active tip.
- The new bone is parented and connected to the bone owning the active tip
  (check the Outliner in Fig. :ref:`fig-rig-bone-active-tip`).

.. todo:: This doesn't seem to work as documented:

.. _fig-rig-bone-disconnected-tip:

.. figure:: /images/animation_armatures_bones_editing_extrude_mouse-clicks-3.png
   :width: 300px

   :kbd:`Ctrl`\ -clicking when the active element is a disconnected root.

If the active element is a *disconnected root*:

- The new bone's root is placed on the active root.
- The new bone is **not** parented to the bone owning the active root
  (check the Outliner in Fig. :ref:`fig-rig-bone-disconnected-tip`).

And hence the new bone will **not** be connected to any bone.

.. _fig-rig-bone-connected-root:

.. figure:: /images/animation_armatures_bones_editing_extrude_mouse-clicks-4.png
   :width: 300px

   :kbd:`Ctrl`\ -clicking when the active element is a connected root.

If the active element is a *connected root*:

- The new bone's root is placed on the active root.
- The new bone **is** parented and connected to the parent of the bone owning the active root
  (check the Outliner in Fig. :ref:`fig-rig-bone-connected-root`).

This should be obvious because if the active element is a connected root
then the active element will be also the tip of the parent bone,
so it is the same as the second case.

As the tip of the new bone becomes the active element,
you can repeat these :kbd:`Ctrl-RMB` clicks several times,
to consecutively add several bones to the end of the same chain.
