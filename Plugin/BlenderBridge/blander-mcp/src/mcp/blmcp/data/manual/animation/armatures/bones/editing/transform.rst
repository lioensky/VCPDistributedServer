
*********
Transform
*********

.. figure:: /images/animation_armatures_bones_editing_transform_panel.png
   :align: right
   :width: 165px
   :figwidth: 165px

   The Transform panel for armatures in Edit Mode.

We will not detail here the various transformations of bones, nor things like axis locking, pivot points, and so on,
as they are common to most object editing, and already described in
the :doc:`mesh section </scene_layout/object/editing/transform/control/index>`.
The same goes for mirroring,
as it is nearly the same as with :doc:`mesh editing </modeling/meshes/editing/mesh/mirror>`.
Just keep in mind that bones' roots and tips behave more or less like meshes' vertices,
and bones themselves act like edges in a mesh.

As you know, bones can have two types of relationships: They can be parented,
and in addition connected. Parented bones behave in *Edit Mode* exactly as if they
had no relations. They can be moved, rotated, scaled, etc. without affecting their descendants.
However, connected bones must always have parent's tips connected to child's roots,
so by transforming a bone, you will affect all its connected parent/children/siblings.

While with other transform tools, the "local axes" means the object's axes,
here they are the bone's own axes (when you lock to a local axis,
by pressing the relevant key twice, the constraint is applied along the selected bone's local axis,
not the armature object's axis).

Finally, you can edit in the *Transform* panel in the Sidebar region
the positions and radius of both joints of the active selected bone,
as well as its :ref:`roll rotation <armature-bone-roll>`.


Scale Radius
============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Armature --> Transform --> Scale Radius`
   :Shortcut:  :kbd:`Alt-S`

You can alter the radius that a bone has by selecting the head, body or tail of a bone,
and then press :kbd:`Alt-S` and move the mouse left or right.
If the body is selected the mean radius will be scaled.
And as usual, with connected bones, you scale at the same time the radius
of the parent's tip and of the children's roots.

You can also alter the bone radius by selecting the tail or head of the bone you wish to alter,
then navigate to :menuselection:`Properties --> Bone --> Deform --> Radius Section`
and entering new values for the *Tail* and *Head* number fields.

.. list-table:: Bone Scale and Scale Radius comparison.

   * - .. figure:: /images/animation_armatures_bones_selecting_single-bone.png

          A single selected bone in Octahedron visualization.

     - .. figure:: /images/animation_armatures_bones_editing_transform_scaling-bone-radius-2.png

          After normal scale.

   * - .. figure:: /images/animation_armatures_bones_editing_transform_scaling-bone-radius-3.png

          A single selected bone in Envelope visualization.

     - .. figure:: /images/animation_armatures_bones_editing_transform_scaling-bone-radius-4.png

          After Scaled Radius. Its length remains the same, but its joints' radius are bigger.

Note that, when you resize a bone (either by directly scaling it, or by moving one of its joints),
Blender automatically adjusts the end-radii of its envelope proportionally to the size of the modification.
Therefore, it is advisable to place all the bones first, and only then edit their properties.


Scale Envelope Distance
=======================

.. reference::

   :Mode:      Edit Mode and Pose Mode
   :Menu:      :menuselection:`Armature --> Transform --> Scale Envelope Distance`
   :Shortcut:  :kbd:`Ctrl-Alt-S`

You can alter the size of the Bone Envelope volume by clicking on the body of the bone you want to alter,
:kbd:`Ctrl-Alt-S` then drag your mouse left or right and the Bone Envelope volume will alter accordingly.

You can also alter the Bone Envelope volume by selecting the Bone you wish to alter and
then navigate to :menuselection:`Properties --> Bone --> Deform --> Envelope --> Distance`
then enter a new value into it.

Altering the Bone Envelope volume does not alter the size of the bone just the range
within which it can influence vertices of child objects.

.. list-table:: Envelope scaling example.

   * - .. figure:: /images/animation_armatures_bones_editing_transform_scaling-bone-radius-3.png

          A single bone selected in Envelope visualization.

     - .. figure:: /images/animation_armatures_bones_editing_transform_scaling-bone-radius-5.png

          Its envelope distance scaled.

.. list-table:: "Bone size" scaling example.

   * - .. figure:: /images/animation_armatures_bones_editing_transform_scaling-bone-size-1.png

          A single "default size" bone selected in B-Bone visualization.

     - .. figure:: /images/animation_armatures_bones_editing_transform_scaling-bone-size-2.png

          Its envelope distance scaled.

     - .. figure:: /images/animation_armatures_bones_editing_transform_scaling-bone-size-3.png

          The same armature in Object Mode and B-Bone visualization, with Bone.004's size scaled up.


.. _bpy.ops.armature.align:

Align Bones
===========

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Armature --> Transform --> Align Bones`
   :Shortcut:  :kbd:`Ctrl-Alt-A`

Rotates the selected bones to achieve the same orientation as the active one.
