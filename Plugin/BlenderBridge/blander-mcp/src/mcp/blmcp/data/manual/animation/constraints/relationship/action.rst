.. index:: Object Constraints; Action Constraint
.. _bpy.types.ActionConstraint:

*****************
Action Constraint
*****************

The *Action* constraint evaluates the location, rotation, and scale inside
a certain :doc:`Action </animation/actions>` at a certain frame,
then applies those to an object or bone.

The frame can either be given directly, or it can be derived from a location
coordinate, rotation angle, or scale factor of another object or bone.
An example of the latter would be to use frame 0 of the Action if an
:doc:`Empty </modeling/empties>` is at X = 0 and frame 100 if the Empty is at X = 10.
If the Empty is then placed at X = 5, the constraint will interpolate this and
evaluate frame 50.

.. seealso::

   The :doc:`/animation/constraints/transform/copy_transforms` may be a sufficient
   replacement if the Action is very simple.

   :doc:`Drivers </animation/drivers/index>` allow defining more complex mathematical
   relationships, again without setting up an Action.

An alternative (if obscure) way of using this constraint is to reference an Action
that animates properties of *other* constraints. The *Action* constraint will
then apply these properties to the constraints that come after it, as long
as their names match the ones in the Action.


Options
=======

.. figure:: /images/animation_constraints_relationship_action_panel.png

   Action constraint.

:ref:`Target <rigging-constraints-interface-common-target>`
   The object or bone to use for calculating the Action frame. Not needed if *Evaluation Time* is used.

Evaluation Time
   Allows specifying the Action frame through a number rather than through a transform property of a *Target*.
   A value of 0 corresponds to *Frame Start* while 1 corresponds to *Frame End* (see below).

   Like other properties, the *Evaluation Time* can be fixed,
   :doc:`keyframed </animation/keyframes/introduction>`, or controlled by a
   :doc:`Driver </animation/drivers/introduction>`. The latter can further make use of
   :doc:`Custom Properties </files/custom_properties>`.

Mix
   Specifies how the evaluated Action transformation is combined with the owner's original transformation
   (from its preceding constraints).

   :Replace:
      The Action's transformation replaces the owner's.
   :Before Original (Full):
      The Action's transformation is applied before the owner's. The result is the same as
      the owner's transformation if it were a child of the Action and there was no constraint.

      If the "parent" is non-uniformly scaled and the "child" was originally rotated,
      the constraint will cause shearing, just like the default
      :ref:`Inherit Scale Full <bpy.types.EditBone.inherit_scale>` setting for bones.
   :Before Original (Aligned):
      Prevents shearing by scaling the "child" along its own axes instead of the axes of
      the "parent," just like the :ref:`Inherit Scale Aligned <bpy.types.EditBone.inherit_scale>`
      setting for bones.
   :Before Original (Split Channels):
      Calculates each transform "channel" -- location, rotation, and scale -- separately
      from the others. The difference with *Before Original (Aligned)* is that the child's
      location is only affected by the parent's location, not by its rotation and scale.
   :After Original (Full/Aligned/Split Channels):
      Like *Before Original*, except the result is the transformation of the Action
      if it were a child of the owner.

   .. seealso::

      The page of the :doc:`/animation/constraints/transform/copy_transforms` demonstrates
      the Mix modes with screenshots.

   .. warning::

      For technical reasons, modes other than *After Original (Full)* and *After Original (Aligned)* may
      not work as expected on objects (not bones) without a parent.

:ref:`bpy.types.constraint.influence`
   How strongly the constraint affects the owner.


Target
------

Channel
   The transform property (location/rotation/scale) and axis to use for calculating the Action frame.

:ref:`Target <rigging-constraints-interface-common-space>`
   The space in which to evaluate the above *Channel*.

Range Min/Max
   The values of the *Channel* that correspond to *Frame Start/End*.
   Despite the names, *Range Max* is allowed to be less than *Range Min*.

   .. warning::

      Target rotations are "wrapped around" so they're always in the range -180° to 180°.

      Negative scales don't work (they are treated as positive scales instead).


Action
------

Action
   The Action to use.

   .. hint::

      Actions can be stored as :term:`Assets <Asset>` for reuse.
      See :doc:`/animation/armatures/posing/editing/pose_library` for details.

Slot
   The Slot inside the Action to use.

Object Action :guilabel:`Bone constraint only`
   By default, the constraint finds Action keyframes for a bone with the same name.
   Checking *Object Action* will use the Action's object keyframes instead.

   The opposite -- applying a bone animation to a constrained object -- is not supported.
   Neither is applying all bone animations in an Action to all bones in an Armature.

Frame Start/End
   The frames within the Action that correspond to *Range Min/Max*. *Frame End* is allowed
   to be less than *Frame Start* -- this will play the animation in reverse.


Example
=======

.. peertube:: c138e7b5-34cb-49cb-af07-d5d5f27f1cfb
