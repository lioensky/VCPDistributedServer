
*************
Tool Settings
*************

Pose Options
============

.. _bpy.types.Pose.use_auto_ik:

Auto IK
-------

.. reference::

   :Mode:      Pose Mode
   :Panel:     :menuselection:`Sidebar --> Tool --> Pose Options --> Auto IK`

Automatic IK is a tool for quick posing, when enabled, translating a bone will activate
inverse kinematics and rotate the parent bone, and the parent's parent, and so on, to
follow the selected bone. The IK chain can only extend from a child to a parent bone
if the child is *connected* to it.

While moving bones, the length of the chain (the number of affected bones)
can be increased or decreased using keyboard hotkeys.
Pressing :kbd:`PageUp` will increase in chain length by one
and :kbd:`PageDown` decreases the length by one.
The chain length can also be controlled with :kbd:`WheelUp` or :kbd:`WheelDown`.

The initial chain length is 0, which effectively means follow
the connections to parent bones as far as possible, with no length limit.
So pressing increasing the chain length the first time sets the length to 1 (move only the selected bone),
and at this point, decreasing the length point sets it back to 0 (unlimited) again.
Thus, you have to increase the chain length *more than once* from the initial state
to set a finite chain length greater than 1.

This is a more limited feature than using an IK constraint,
which can be configured, but it can be useful for quick posing.


.. _bpy.types.Pose.use_mirror_x:

X-Axis Mirror
-------------

.. reference::

   :Mode:      Edit and Pose Mode
   :Panel:     :menuselection:`Sidebar --> Tool --> Options --> X-Axis Mirror`

This option enables automatic mirroring of editing actions along the X axis.
You can enable this option in the :menuselection:`Tool tab --> Options panel`,
while the armature is selected in *Edit Mode*.
When you have pairs of bones of the same name with just a different "side suffix"
(e.g. ".R"/".L", or "_right"/"_left" ...), once this option is enabled,
each time you transform (move, rotate, scale...) a bone,
its "other side" counterpart will be transformed accordingly,
through a symmetry along the armature local X axis.
As most rigs have at least one axis of symmetry (animals, humans, ...),
it is an easy way to keep the model symmetrical.


Relative Mirror
---------------

.. reference::

   :Mode:      Edit and Pose Mode
   :Panel:     :menuselection:`Sidebar --> Tool --> Options --> Relative Mirror`

Accounts for any relative transformations when using *X-Axis Mirror*.

.. seealso::

   :ref:`Naming bones <armature-editing-naming-bones>`.


Known Limitations
=================

Relative Mirror is not supported with `Auto IK`_ enabled.
