
***********
In-Betweens
***********

.. figure:: /images/animation_armatures_posing_editing_in-betweens_tools.png
   :align: right

   In-Betweens Tools.

There are several tools for editing poses in an animation.

There are also in *Pose Mode* a bunch of armature-specific editing options/tools,
like :ref:`auto-bones naming <armature-editing-naming-bones>`,
:ref:`properties switching/enabling/disabling <armature-bone-properties>`, etc.,
that were already described in the armature editing pages. See the links above...


.. _bpy.ops.pose.push_rest:

Push Pose from Rest Pose
========================

.. reference::

   :Mode:      Pose Mode
   :Menu:      :menuselection:`Pose --> In-Betweens --> Push Pose from Rest Pose`

Similar to *Push Pose from Breakdown* but interpolates the pose to the rest position instead.
Only one keyframe is needed for this tool unlike two for the other.


.. _bpy.ops.pose.relax_rest:

Relax Pose to Rest Pose
=======================

.. reference::

   :Mode:      Pose Mode
   :Menu:      :menuselection:`Pose --> In-Betweens --> Relax Pose to Rest Pose`

Similar to *Relax Pose to Breakdown* but works to bring the pose back to the rest position instead.
Only one keyframe is needed for this tool unlike two for the other.


.. _bpy.ops.pose.push:

Push Pose from Breakdown
========================

.. reference::

   :Mode:      Pose Mode
   :Tool:      :menuselection:`Toolbar --> In-Betweens Tools --> Push`
   :Menu:      :menuselection:`Pose --> In-Betweens --> Push Pose from Breakdown`
   :Shortcut:  :kbd:`Ctrl-E`

*Push Pose* interpolates the current pose by making it closer to the next keyframed position.


.. _bpy.ops.pose.relax:

Relax Pose to Breakdown
=======================

.. reference::

   :Mode:      Pose Mode
   :Tool:      :menuselection:`Toolbar --> In-Betweens Tools --> Relax`
   :Menu:      :menuselection:`Pose --> In-Betweens --> Relax Pose to Breakdown`
   :Shortcut:  :kbd:`Alt-E`

Relax pose is somewhat related to the above topic, but it is only useful with keyframed bones.
When you edit such a bone (and hence take it "away" from its "keyed position"),
using this tool will progressively "bring it back" to its "keyed position",
with smaller and smaller steps as it comes near it.


.. _bpy.ops.pose.breakdown:

Pose Breakdowner
================

.. reference::

   :Mode:      Pose Mode
   :Tool:      :menuselection:`Toolbar region --> In-Betweens Tools --> Breakdowner`
   :Menu:      :menuselection:`Pose --> In-Betweens --> Pose Breakdowner`
   :Shortcut:  :kbd:`LMB`-drag

Creates a suitable breakdown pose on the current frame.

The Breakdowner tool can be constrained to work on specific transforms and axes,
by pressing the following keys while the tool is active:

- :kbd:`G`, :kbd:`R`, :kbd:`S`: move, rotate, scale
- :kbd:`B`: Bendy bones
- :kbd:`C`: custom properties
- :kbd:`X`, :kbd:`Y`, :kbd:`Z`: to the corresponding axes


.. _bpy.ops.pose.blend_to_neighbor:

Blend to Neighbor
=================

.. reference::

   :Mode:      Pose Mode
   :Menu:      :menuselection:`Pose --> In-Betweens --> Blend to Neighbor`
   :Shortcut:  :kbd:`Shift-Alt-E`

Transitions the current pose with the neighboring keyframes in the timeline.
In order for this operator to work, there must be a keyframe before and after the current frame.
