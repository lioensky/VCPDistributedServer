
****************
Global Transform
****************

Copy and paste object and bone transforms with ease.

When copying, the global (:term:`World Space`) transform is placed on the clipboard.
This can then be pasted onto any object or bone, at the current frame or at another one.

.. reference::

   :Panel:     :menuselection:`3D Viewport --> Sidebar --> Animation --> Global Transform`

.. figure:: /images/copy_global_transform-main.webp
   :align: right

The figure on the right shows the main functionality of the Copy Global
Transform panel. The collapsed panels are described each in their own section
below.

.. _bpy.ops.object.copy_global_transform:

Copy
   Inspects the active Object (in Object mode) or Bone (in Pose mode) and places
   its current global transform onto the clipboard as a matrix.

.. _bpy.ops.object.paste_transform:

Paste
   Takes the copied global transform and applies it to the active Object or Bone.
   This is done by **adjusting its location, rotation, and scale properties**.

Mirrored
   Same as 'Paste' above, but then mirrored relative to some other object or
   bone. This can be useful, for example, to copy the foot position of one foot
   to the other. See :ref:`copy-global-transform-mirror-options` below.

Paste to Selected Keys
   Paste as described above and additionally use auto-keying to update one or
   more frames. The key selection is used to tell Blender *which frames* this
   should happen on; it does not influence which parts of the transform are
   keyed. *What* is keyed is determined by the active keying set.

Paste and Bake
   Almost the same as *Paste to Selected Keys*. Instead of only pasting on the
   selected keys, *Paste and Bake* will paste & auto-key on every frame between
   the first and last selected keys.


.. _copy-global-transform-mirror-options:

Mirror
------

.. figure:: /images/copy_global_transform-mirror_options.webp
   :align: right

The copied transform can be mirrored relative to an object or a :term:`Bone`.
This requires choosing that object or bone first.

.. _bpy.types.ToolSettings.anim_mirror_object:

Object
   This will just mirror relative to the chosen object.

   Choosing an :term:`Armature` object as mirror object will show the bone
   selector. You can use that to pick the bone to use as mirror. This will
   always use the named bone on that specific armature object.

.. _bpy.types.ToolSettings.anim_mirror_bone:

Bone
   When you choose *no mirror object* at all, you can still choose a *bone
   name*. This is used for mirroring against a bone in the *active armature*.
   This can be useful to mirror bone transforms relative to the 'chest' bone
   of the active character.

After pasting with 'Paste Mirrored', the mirror axes can be chosen in the
:ref:`redo panel <bpy.ops.screen.redo_last>`.


.. _bpy.ops.object.copy_relative_transform:

Relative
--------

.. figure:: /images/copy_global_transform-relative.webp
   :align: right

The "Relative" panel has copy/paste buttons that work relative to a chosen
object. When copying, the world-space transform is determined, and then adjusted
to become relative to the world-space transform of the chosen object. When
pasting, this happens in reverse.

If no object is chosen, the copy/paste will happen relative to the active scene
camera. What is the active scene camera is determined for every action, so when
you paste it can be different from when you copied. This can help to keep an
object visually in the same place when switching cameras, or when switching
between scenes.


.. _bpy.types.ToolSettings.anim_fix_to_cam:

Fix to Camera
-------------

.. figure:: /images/copy_global_transform-fix_to_camera.webp
   :align: right

Also known as "bake to camera", this operator will ensure selected objects/bones
remain static (relative to the camera) on unkeyed frames.

This is done by generating new keys. These keys will be of :ref:`type
'Generated' <keyframe-type>` so that it remains clear which keys were manually
created, and which were generated. This way the tool can be re-run to
re-generate the keys.

#. Ensure your animation is keyed using constant interpolation. If this is not
   the case yet, bake your animation (at least the transform channels). This
   tool does _not_ work with the :ref:`"Stepped" F-Curve modifier <bpy.types.FModifierStepped>`
#. Choose which of the Location/Rotation/Scale channels you want to fix to the
   camera. When unsure, make sure they are all checked.
#. Press the "Fix to Camera" button.

To undo the effect of the "Fix to Camera" operator, click on the trash bin
button. That will remove all the generated keys in either the scene range or the
frame range.

The tool operates on the scene frame range, or on the preview range if that is
active. Keys outside that range are ignored, both when fixing to the camera and
when removing generated keys.

.. warning::

   This tool assumes that *all* keys with type 'Generated' are equal. It will
   overwrite them (or remove them, depending on which button you press).


Limitations
===========

Pasting a transform adjusts the Object/Bone's location, rotation, and
scale. This means that when copying a skewed transform, this skew is lost.

If there are constraints on the Object/Bone, the resulting visual transformation
may not be the same as the pasted one. To give a concrete example: if you have a
constraint that adds a rotation, it will always add that rotation on top of the pasted transform.

.. seealso::

   :doc:`/animation/armatures/posing/editing/pose_library` for a way to manage
   and share entire poses.
