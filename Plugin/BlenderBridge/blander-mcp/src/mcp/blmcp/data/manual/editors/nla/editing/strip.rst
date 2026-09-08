
**************
Editing Strips
**************

Transform
=========

.. reference::

   :Editor:    Nonlinear Animation
   :Menu:      :menuselection:`Strip --> Transform`

Move :kbd:`G`
   Move the selected strips in time or to a different track.
Extend :kbd:`E`
   Lets you quickly move the selected strips that are on a certain side of the Playhead.
   This is handy if you need to, say, move all the strips after a certain time point to
   the right to make space for new ones.

   To use this operator, first select some or all strips and place your mouse cursor to
   the left or right of the Playhead. Then, press :kbd:`E`, move the mouse to move (only)
   the strips on that side of the Playhead, and press :kbd:`LMB` to confirm
   (or :kbd:`RMB` to cancel).

   If a strip straddles the Playhead, only its starting/ending point will be moved
   (again depending on the position of the mouse cursor).
Scale :kbd:`S`
   Scales the selected strips, using the Playhead as the pivot point.


.. _bpy.ops.nla.swap:

Swap
----

.. reference::

   :Editor:    Nonlinear Animation
   :Menu:      :menuselection:`Strip --> Transform --> Swap`
   :Shortcut:  :kbd:`Alt-F`

Swap the order of the selected strips in their track.


.. _bpy.ops.nla.move_up:

Move Up
-------

.. reference::

   :Editor:    Nonlinear Animation
   :Menu:      :menuselection:`Strip --> Transform --> Move Up`
   :Shortcut:  :kbd:`PageUp`

Move selected strips up a track if there is room.


.. _bpy.ops.nla.move_down:

Move Down
---------

.. reference::

   :Editor:    Nonlinear Animation
   :Menu:      :menuselection:`Strip --> Transform --> Move Down`
   :Shortcut:  :kbd:`PageDown`

Move selected strips down a track if there is room.


.. _bpy.ops.nla.snap:

Snap
====

.. reference::

   :Editor:    Nonlinear Animation
   :Menu:      :menuselection:`Strip --> Snap`

Selection to Current Frame
   Move the start of the selected strips to the current frame.
Selection to Nearest Frame
   Move the start of the selected strips to the nearest full frame.
Selection to Nearest Second
   Move the start of the selected strips to the nearest second.
Selection to Nearest Marker
   Move the start of the selected strips to the nearest marker.


.. _bpy.ops.nla.split:

Split
=====

.. reference::

   :Editor:    Nonlinear Animation
   :Menu:      :menuselection:`Strip --> Split`
   :Shortcut:  :kbd:`Y`

Split the selected strips in two at the current frame.


.. _bpy.ops.nla.duplicate:

Duplicate
=========

.. reference::

   :Editor:    Nonlinear Animation
   :Menu:      :menuselection:`Strip --> Duplicate`
   :Shortcut:  :kbd:`Alt-D`

Creates copies of the selected strips, duplicating any actions they reference.
Editing the keyframes in a copied strip therefore doesn't affect the original.

.. _bpy.ops.nla.duplicate_linked_move:

Linked Duplicate
================

.. reference::

   :Editor:    Nonlinear Animation
   :Menu:      :menuselection:`Strip --> Linked Duplicate`
   :Shortcut:  :kbd:`Shift-D`

Creates copies of the selected strips, reusing any actions they reference.
Editing the keyframes in a copied strip therefore also affects the original
(and vice versa). Blender warns you about this by highlighting the other strip in red.

.. figure:: /images/editors_nla_editing_linked-strip-edit.png

   Linked duplicated strip being edited.


.. _bpy.ops.nla.delete:

Delete
======

.. reference::

   :Editor:    Nonlinear Animation
   :Menu:      :menuselection:`Strip --> Delete`
   :Shortcut:  :kbd:`Delete`, :kbd:`X`

Deletes the selected NLA-Strips.


.. _bpy.ops.nla.meta_add:

Make Meta
=========

.. reference::

   :Editor:    Nonlinear Animation
   :Menu:      :menuselection:`Strip --> Make Meta`
   :Shortcut:  :kbd:`Ctrl-G`

Groups the selected NLA-strips into a meta strip.

.. list-table::

   * - .. figure:: /images/editors_nla_strips_meta1.png
          :width: 320px

          Select two or more strips.

     - .. figure:: /images/editors_nla_strips_meta2.png
          :width: 320px

          Combine them into a meta strip.


.. _bpy.ops.nla.meta_remove:

Remove Meta
===========

.. reference::

   :Editor:    Nonlinear Animation
   :Menu:      :menuselection:`Strip --> Remove Meta`
   :Shortcut:  :kbd:`Ctrl-Alt-G`

Ungroups the selected meta strips, replacing them by their contents.


.. _bpy.ops.nla.mute_toggle:

Toggle Muting
=============

.. reference::

   :Editor:    Nonlinear Animation
   :Menu:      :menuselection:`Strip --> Toggle Muting`
   :Shortcut:  :kbd:`H`

Mutes or unmutes the selected strips. Muted strips have a dotted border and
don't influence the animation.


.. _bpy.ops.nla.bake:

Bake Action
===========

.. reference::

   :Editor:    Nonlinear Animation
   :Menu:      :menuselection:`Strip --> Bake Action`

.. reference::

   :Editor:    3D Viewport
   :Mode:      Object and Pose Modes
   :Menu:      :menuselection:`Header --> Object --> Animation --> Bake Action...`

The final motion of objects and bones depends not only on the keyframed animation,
but also on :doc:`F-Curve modifiers </editors/graph_editor/fcurves/modifiers>`,
:doc:`drivers </animation/drivers/introduction>`,
and :doc:`constraints </animation/constraints/introduction>`.
The *Bake Action* operator computes this final motion and creates a corresponding
keyframe on every scene frame.

This can be useful for adding deviation to a cyclic action like a :term:`Walk Cycle`,
or to create a keyframe animation from drivers or constraints.

Start Frame
   Start frame for baking.
End Frame
   End frame for baking.
Frame Step
   Number of frames to skip forward while baking each frame.
Only Selected Bones
   Only key selected bones (Pose baking only).
Visual Keying
   Keyframe from the final transformations (with constraints applied).
Clear Constraints
   Remove all constraints from keyed object/bones, and do 'visual' keying.
Clear Parents
   Bake animation onto the object then clear parents (objects only).
Overwrite Current Action
   Bake animation into the current action instead of creating a new one
   (useful for baking only part of bones in an armature).
Clean Curves
   After baking curves, :ref:`remove redundant keys <bpy.ops.graph.clean>`.
Bake Data
   Which data transformations to bake.

   :Pose: Bake bone transformations.
   :Object: Bake object transformations.
Channels
   Which channels to bake.

   :Location: Bake location channels.
   :Rotation: Bake rotation channels.
   :Scale: Bake scale channels.
   :B-Bone: Bake :doc:`B-Bone </animation/armatures/bones/properties/bendy_bones>` channels.
   :Custom Properties: Bake custom properties.


.. _bpy.ops.nla.apply_scale:

Apply Scale
===========

.. reference::

   :Editor:    Nonlinear Animation
   :Menu:      :menuselection:`Strip --> Apply Scale`
   :Shortcut:  :kbd:`Ctrl-A`

Applies the scale of the selected strips to their referenced actions.


.. _bpy.ops.nla.clear_scale:

Clear Scale
===========

.. reference::

   :Editor:    Nonlinear Animation
   :Menu:      :menuselection:`Strip --> Clear Scale`
   :Shortcut:  :kbd:`Alt-S`

Resets the scale of the selected strips.


.. _bpy.ops.nla.action_sync_length:

Sync Action Length
==================

.. reference::

   :Editor:    Nonlinear Animation
   :Menu:      :menuselection:`Strip --> Sync Action Length`

Resets the strip's length to that of its underlying action,
ensuring that it (only) plays from the action's first keyframe to its last.

.. seealso::

   The Sync Length Now button in the :ref:`Sidebar <nla-sidebar-action-clip>`,
   which does the same thing.

.. _bpy.ops.nla.make_single_user:

Make Single User
================

.. reference::

   :Editor:    Nonlinear Animation
   :Menu:      :menuselection:`Strip --> Make Single User`
   :Shortcut:  :kbd:`U`

Duplicates actions where necessary so that each selected strip has its own action that's not used
by any others. This way, you can edit the keyframes in the selected strips knowing that you won't
affect any other part of the animation.

.. note::

   This does not recursively go inside meta strips.


.. _bpy.ops.nla.tweakmode_enter:

Start Editing Stashed Action
============================

.. reference::

   :Editor:    Nonlinear Animation
   :Menu:      :menuselection:`Strip --> Start Editing Stashed Action`
   :Shortcut:  :kbd:`Shift-Tab`

Enters Tweak Mode for the selected strip's action, making its keyframes available for editing in
e.g. the :doc:`Graph Editor </editors/graph_editor/introduction>`. In addition, marks the strip's
track as *Solo*, muting all the other tracks -- this way, they no longer influence the animation
and you can focus exclusively on the action you're editing.

While the menu item refers to stashed (muted) actions, this only reflects the typical use case.
It works on unmuted actions as well.

When you're done editing, click :menuselection:`Strip --> Stop Editing Stashed Action`
or press :kbd:`Shift-Tab` again.

.. list-table::

   * - .. figure:: /images/editors_nla_editing_nla-mode.png
          :width: 320px

          Strip in NLA mode.

     - .. figure:: /images/editors_nla_editing_edit-mode.png
          :width: 320px

          Strip in Tweak mode.


Start Tweaking Strips Actions (Full Stack)
==========================================

.. reference::

   :Editor:    Nonlinear Animation
   :Menu:      :menuselection:`Strip --> Start Tweaking Strips Actions (Full Stack)`
   :Shortcut:  :kbd:`Tab`

Enters Tweak Mode for the selected strip's action, making its keyframes available for editing.
Leaves all the other tracks enabled so that you can still see their effects while making changes.

When you're done, click :menuselection:`Strip --> Stop Tweaking Strips Actions`
or press :kbd:`Tab` again.

.. note::

   For transitions above the tweaked strip, keyframe remapping will fail
   for channel values that are affected by the transition.
   A workaround is to tweak the active strip without evaluating the upper NLA stack.


Start Tweaking Strips Actions (Lower Stack)
===========================================

.. reference::

   :Editor:    Nonlinear Animation
   :Menu:      :menuselection:`Strip --> Start Tweaking Strips Actions (Lower Stack)`

Enters Tweak Mode for the selected strip's action, making its keyframes available for editing.
Mutes any tracks above the current one so that they don't influence the animation while making changes.

When you're done, click :menuselection:`Strip --> Stop Tweaking Strips Actions` or press :kbd:`Tab`.
