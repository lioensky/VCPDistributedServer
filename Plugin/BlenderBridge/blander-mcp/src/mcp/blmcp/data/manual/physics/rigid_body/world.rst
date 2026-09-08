.. _bpy.types.RigidBodyWorld:
.. _bpy.ops.rigidbody.world:

****************
Rigid Body World
****************

.. reference::

   :Panel:     :menuselection:`Scene --> Rigid Body World`

The *Rigid Body World* is a group of rigid body objects,
which holds settings that apply to all rigid bodies in this simulation.

When you add rigid body physics to an object,
primary there is created a group of objects with default "RigidBodyWorld" name.
Rigid body objects automatically are added to this group when you add rigid body physics for them.
You can create several Rigid Body World :doc:`Collections </scene_layout/collections/collections>`
and allocate the rigid body objects with the :ref:`Collections panel <scene-layout_collections_collections_panel>`.

Rigid body objects and constraints are only taken into account by the simulation
if they are in the collection specified in the *Collection* field of the *Rigid Body World* panel in the *Scene* tab.


Settings
========

Rigid Body World
   Enable/disable evaluation of the rigid body simulation based on the rigid body objects
   participating in the specified group of Rigid Body World.
Remove Rigid Body World
   Remove rigid body simulation from the current scene.
Collection
   Containing rigid body objects participating in this simulation.
Constraints
   Containing rigid body object constraints participating in the simulation.

Simulation quality and timing settings:

Speed
   Can be used to speed up/slow down the simulation.
Split Impulse
   Enable/disable reducing extra velocity that can build up when objects collide
   (lowers the simulation stability a little so use only when necessary).
   Limits the force with which objects are separated on collision, generally produces nicer
   results, but makes the simulation less stable (especially when stacking many objects).
Substeps Per Frame
   Number of simulation steps taken per frame (higher values are more accurate but slower).
   This only influences the accuracy and not the speed of the simulation.
Solver Iterations
   Amount of constraint solver iterations made per simulation step (higher values are more accurate but slower).
   Increasing this makes constraints and object stacking more stable.


Rigid Body Cache
================

.. reference::

   :Panel:     :menuselection:`Scene --> Rigid Body World --> Cache`

The *Cache* subpanel specifies the frame range in which the simulation is active.
Can be used to bake the simulation.

Start/End
   First and last frame of the simulation.
Bake
   Calculates the simulation and protects the cache. You need to be in *Object Mode* to bake.
Delete Bake
   Active after the baking of simulation. Clears the baked cache.
Calculate to Frame
   Bake physics to current frame.
Current Cache to Bake
   Bake from Cache.
Bake All Dynamics
   Bake all physics.
Delete All Bakes
   Deletes all baked caches of all objects in the current scene.
Update All to Frame
   Update cache to current frame.

If you have not saved the blend-file, the cache is created in memory,
so save your file first or the cache may be lost.


Rigid Body Field Weights
========================

.. reference::

   :Panel:     :menuselection:`Scene --> Rigid Body World --> Field Weights`

As other physics dynamics systems, rigid body simulation are also influenced by external force effectors.
