.. _bpy.types.SoftBodySettings.use_goal:

****
Goal
****

.. reference::

   :Panel:     :menuselection:`Physics --> Soft Body --> Goal`

Enabling this tells Blender to use the motion from animations
(F-Curves, armatures, parents, lattices, etc.) in the simulation.
The "goal" is the desired end position for vertices based on this animation.

See :ref:`exterior forces <physics-softbody-forces-exterior-goal>` for details.

.. _bpy.types.SoftBodySettings.vertex_group_goal:

Vertex Group
   Use a vertex group to allow per-vertex goal weights (multiplied by the *Default* goal).


Settings
========

.. _bpy.types.SoftBodySettings.goal_spring:

Stiffness
   The spring stiffness for *Goal*. A low value creates very weak springs
   (more flexible "attachment" to the goal), a high value creates a strong spring
   (a stiffer "attachment" to the goal).

.. _bpy.types.SoftBodySettings.goal_friction:

Damping
   The friction coefficient for *Goal*. Higher values give damping of the spring effect (little jiggle),
   and the movement will soon come to an end.


Strengths
=========

.. _bpy.types.SoftBodySettings.goal_default:

Default
   Goal weight/strength for all vertices when no *Vertex Group* is assigned.
   If you use a vertex group the weight of a vertex defines its goal.

.. _bpy.types.SoftBodySettings.goal_min:
.. _bpy.types.SoftBodySettings.goal_max:

Min/Max
   When you use a vertex group, you can use the *Minimum* and *Maximum* to fine-tune (clamp) the weight values.
   The lowest vertex weight will become *Minimum*, the highest value becomes *Maximum*.
