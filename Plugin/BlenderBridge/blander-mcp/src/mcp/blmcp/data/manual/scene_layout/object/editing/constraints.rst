
***********
Constraints
***********

Operators for working with an object's :doc:`/animation/constraints/index`.


.. _bpy.ops.object.constraint_add_with_targets:

Add Constraint (with Targets)
=============================

.. reference::

   :Mode:      Object Mode and Pose Mode
   :Menu:      :menuselection:`Object --> Constraint --> Add Constraint (with Targets)`

Adds a constraint to the active object.
The type of constraint must be chosen from a pop-up menu,
though it can be changed later from the *Add Constraint (with Targets)*
:ref:`bpy.ops.screen.redo_last` panel.
If there is an other object selected besides the active one,
that object will be the constraint target (if the chosen constraint accepts targets).

When using a bone from another armature as the target for a constraint, the tool
will look inside the non-active armature and use its active bone,
provided that armature is in Pose Mode.


.. _bpy.ops.object.constraints_copy:

Copy Constraints to Selected Objects
====================================

.. reference::

   :Mode:      Object Mode and Pose Mode
   :Menu:      :menuselection:`Object --> Constraint --> Copy Constraints to Selected Objects`

Copies the active object Constraints to the rest of the selected objects.


.. _bpy.ops.object.constraints_clear:

Clear Object Constraints
========================

.. reference::

   :Mode:      Object Mode and Pose Mode
   :Panel:     :menuselection:`Object --> Constraint --> Clear Object Constraints`

Removes all Constraints of the selected object(s).
