.. index:: Constraint; Object Constraints
.. index:: Object Constraints

************
Introduction
************

Constraints are a way of automatically controlling the location, rotation,
and scale of an :term:`object` or :term:`bone`. For example, they can
:doc:`attach </animation/constraints/relationship/child_of>`
a sword to a knight's hand, or make a tennis player's eyes
:doc:`point towards </animation/constraints/tracking/damped_track>` the ball.

.. seealso::

   :doc:`Bone Constraints </animation/armatures/posing/bone_constraints/introduction>`

Each object or bone can have a *stack* of constraints that's evaluated from top to bottom.
In addition, each constraint has an :ref:`Influence <bpy.types.constraint.influence>` factor
for weakening it or mixing it with other constraints. What's more, this Influence can be
keyframed, which makes it possible to turn constraints on and off over the course of an animation.

.. list-table::
   :widths: 1 1 5

   * - .. figure:: /images/animation_constraints_introduction_tab-object.png

          Object

     - .. figure:: /images/animation_constraints_introduction_tab-bone.png

          Bone

     - .. figure:: /images/animation_constraints_interface_stack_example.png
          :align: center

          Constraint Stack

Adding & Removing Constraints
=============================

To add a constraint, click on *Add Object/Bone Constraint* in the :doc:`/editors/properties_editor`
and choose a constraint type.

To remove a constraint, click its :bl-icon:`x` button.

To move a constraint to a different position in the stack, drag its handle :bl-icon:`grip`.

The :doc:`/scene_layout/object/editing/constraints` menu in the 3D Viewport offers further options
such as copying constraints and deleting all constraints in one go.
The :doc:`/scene_layout/object/editing/track` menu allows quickly adding a "track" (point at)
constraint.

.. _constraint-visual-transform:

Visual Transform
================

Constraints give their owning object or bone a new location, rotation, and/or scale which together
are called the *visual transform*. This transform is separate from the "base" transform found
in the *Transform* panel of the Properties Editor,
and as its name implies, it determines where the owner *really* appears in the world.

For example, even when an object's *Transform* panel still shows the original *Location* of (0, 0, 0),
a constraint could have placed it somewhere else entirely. What's more, attempting to move or even
animate that object won't work: its *Location* numbers will change, but visually,
it will remain stuck in place. The only way to "free" the object is to disable or delete the constraint,
or to set its :ref:`bpy.types.constraint.influence` to zero.

Of course, transform properties that are not constrained can still be changed as usual.

While the visual transform is not shown in the UI, it can be copied to the base transform:

- By running :ref:`Apply Visual Transform <bpy.ops.object.visual_transform_apply>`.
- By :ref:`applying <bpy.ops.constraint.apply>` the constraint. This also deletes the constraint.
