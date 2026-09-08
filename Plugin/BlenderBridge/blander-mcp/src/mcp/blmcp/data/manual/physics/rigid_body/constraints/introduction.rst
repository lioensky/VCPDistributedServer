.. index:: Constraint; Rigid Body Constraints
.. index:: Rigid Body Constraints

************
Introduction
************

:term:`Constraints <Constraint>` (also known as joints) for rigid bodies connect two rigid bodies.
The physics constraints are meant to be attached to an :term:`Empty` object.
The constraint then has fields which can be pointed at the two physics-enabled object
which will be bound by the constraint.
The empty object provides a location and axis for the constraint distinct from the two constrained objects.
The location of the entity hosting the physics constraint marks a location and
set of axes on each of the two constrained objects.
These two anchor points are calculated at the beginning of the animation and their position and
orientation remain fixed in the *local* coordinate system of the object for the duration of the animation.
The objects can move far from the constraint object, but the constraint anchor moves with the object.
If this feature seems limiting, consider using multiple objects with a non-physics *Child of* constraint and
animate the relative location of the child.


Connect
=======

The quickest way to constrain two objects is to select both and
click the *Connect* button in :menuselection:`Object --> Rigid Body`.
This creates a new empty object (named "Constraint") with a physics constraint
already attached and pointing at the two selected objects.


Physics Menu
============

Also you can create *Rigid Body Constraint* on one of the two constrained objects with
*Rigid Body Constraint* button of the *Physics* tab in the Properties.
This constraint is dependent on the object location and rotation on which it was created.
This way, there are no empty object created for the constraint.
The role of the empty object is put on this object.
The constrained object can be then be set as a *Passive* type for better driving of the constraint.

Additional parameters appear in the *Rigid Body Constraint* panel of the *Physics* tab in the Properties
for the selected empty object or the one of the two constrained objects with the created constraint.


Common Options
==============

.. reference::

   :Panel:     :menuselection:`Physics --> Rigid Body Constraint`


Settings
--------

.. _bpy.types.RigidBodyConstraint.enabled:

Enabled
   Specifies whether the constraint is active during the simulation.

.. _bpy.types.RigidBodyConstraint.disable_collisions:

Disable Collisions
   Allows constrained objects to pass through one another.

.. _bpy.types.RigidBodyConstraint.use_breaking:

Breakable
   Allows constraint to break during simulation. Disabled for the *Motor* constraint.
   This can be used to simulate destruction.

.. _bpy.types.RigidBodyConstraint.breaking_threshold:

Threshold
   Impulse strength that needs to be reached before the constraint breaks.


.. _bpy.types.RigidBodyConstraint.use_limit:
.. _bpy.types.RigidBodyConstraint.limit:

Limits
------

By using limits you can constrain objects even more by specifying a translation/rotation range on/around
respectively one axis (see below for each one individually). To lock one axis, set both limits to 0.


.. _bpy.types.RigidBodyConstraint.object1:
.. _bpy.types.RigidBodyConstraint.object2:

Objects
-------

First
   First object to be constrained.
Second
   Second object to be constrained.


.. _bpy.types.RigidBodyConstraint.use_override_solver_iterations:
.. _bpy.types.RigidBodyConstraint.solver_iterations:

Override Iterations
-------------------

Allows making constraints stronger (more iterations) or weaker (less iterations)
than specified in the rigid body world.

Iterations
   Number of constraint solver iterations made per simulation step for this constraint.
