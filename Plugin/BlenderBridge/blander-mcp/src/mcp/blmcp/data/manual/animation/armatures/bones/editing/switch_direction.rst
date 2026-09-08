.. _bpy.ops.armature.switch_direction:

****************
Switch Direction
****************

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Armature --> Switch Direction`
   :Shortcut:  :kbd:`Alt-F`

This tool allows you to switch the direction of the selected bones
(i.e. their root will become their tip, and vice versa).

Switching the direction of a bone will generally break the chain(s) it belongs to.
However, if you switch a whole (part of a) chain, the switched bones will still be parented/connected,
but in "reversed order". See the Fig. :ref:`fig-rig-properties-switch`.

.. _fig-rig-properties-switch:

.. list-table:: Switching example.

   * - .. figure:: /images/animation_armatures_bones_editing_switch-direction_example-1.png

          An armature with one selected bone, and one selected chain of three bones, just before switching.

     - .. figure:: /images/animation_armatures_bones_editing_switch-direction_example-2.png

          The selected bones have been switched. Bone.005 is no more connected nor parented to anything.
          The chain of switched bones still exists, but reversed (now Bone.002 is its root, and Bone is its tip).
          Bone.003 is now a free bone.
