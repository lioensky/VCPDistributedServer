.. _armature-bone-properties:

**********
Properties
**********

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Armature --> Bone Settings --> ...`
   :Shortcut:  :kbd:`Shift-W`, :kbd:`Shift-Ctrl-W`, :kbd:`Alt-W`

Most bones' properties (except the transform ones) are regrouped in each bone's panels,
in the *Bones* tab in *Edit Mode*. Let us detail them.

Note that some of them are also available in the 3D Viewport,
through the three pop-up menus within the same entry:

- *Toggle Setting*: :kbd:`Shift-W` or :menuselection:`Armature --> Bone Settings --> Toggle a Setting`
- *Enable Setting*: :kbd:`Shift-Ctrl-W` or :menuselection:`Armature --> Bone Settings --> Enable a Setting`
- *Disable Setting*: :kbd:`Alt-W` or :menuselection:`Armature --> Bone Settings --> Disable a Setting`

Display Wire
   Always display the bone as wireframe.
Deform
   (also :kbd:`Shift-W` :menuselection:`--> (Deform, ...)`).
Multiply Vertex Group by Envelope
   (also :kbd:`Shift-W` :menuselection:`--> (Multiply Vertex Group by Envelope, ...)`).

   These settings control how the bone influences its geometry, along with the bones' joints radius.
   This will be detailed in the :doc:`skinning part </animation/armatures/skinning/index>`.
Inherit Rotation
   The bone automatically rotates together with its parent in *Pose Mode*. For more details,
   see the :ref:`relations page <bpy.types.EditBone.parent>`.
Lock
   (also :kbd:`Shift-W` :menuselection:`--> (Locked, ...)`)
   This will prevent all editing of the bone in *Edit Mode*;
   see :ref:`bone locking <animation_armatures_bones_locking>`.
