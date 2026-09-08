.. _bpy.types.ClothCollisionSettings:

**********
Collisions
**********

.. reference::

   :Panel:     :menuselection:`Physics --> Cloth --> Collision`

In most cases, a piece of cloth does not just hang there in 3D space,
it collides with other objects in the environment. To ensure proper simulation,
there are several items that have to be set up and working together:

- The *Cloth* object must be told to participate in collisions.
- Optionally (but recommended) tell the cloth to collide with itself.
- Other objects must be visible to the *Cloth* object *via* shared layers.
- The other objects must be mesh objects.
- The other objects may move or be themselves deformed by other objects (like an armature or shape key).
- The other mesh objects must be told to deflect the cloth object.
- The blend-file must be saved in a directory so that simulation results can be saved.
- You then *Bake* the simulation. The simulator computes the shape of the cloth for a frame range.
- You can then edit the simulation results, or make adjustments to the cloth mesh, at specific frames.
- You can make adjustments to the environment or deforming objects,
  and then re-run the cloth simulation from the current frame forward.

.. figure:: /images/physics_cloth_settings_collisions_panel.png

   Cloth Collisions panel.

.. _bpy.types.ClothCollisionSettings.collision_quality:

Quality
   A general setting for how fine and good a simulation you wish.
   Higher numbers take more time but ensure less tears and penetrations through the cloth.


.. _bpy.types.ClothCollisionSettings.use_collision:

Object Collisions
-----------------

If the cloth object needs to be deflected by some other object. To deflect a cloth,
the object must be enabled as an object that collides with the cloth object.
To enable objects to collide with cloth objects enable
:ref:`collision physics <physics-collision-soft-bodt-cloth>`
for the collider object (not on the cloth object).

.. note::

   If your colliding object is not a mesh object, such as a NURBS surface, or a text object,
   you must convert it to a mesh object using :ref:`object-convert-to`.

.. _bpy.types.ClothCollisionSettings.distance_min:

Distance
   The distance another object must get to the cloth for
   the simulation to repel the cloth out of the way.
   Smaller values might give errors but gives some speed-up while
   larger will give unrealistic results if too large and can be slow.
   It is best to find a good in between value.

.. _bpy.types.ClothCollisionSettings.impulse_clamp:

Impulse Clamping
   Prevents explosions in tight and complicated collision situations
   by restricting the amount of movement after a collision.

.. _bpy.types.ClothCollisionSettings.vertex_group_object_collisions:

Vertex Group
   Faces that have all vertices assigned to this
   :doc:`Vertex Group </modeling/meshes/properties/vertex_groups/index>` are excluded from collision with objects.

.. _bpy.types.ClothCollisionSettings.collection:

Collision Collection
   Only objects that are a part of this :doc:`Collection </scene_layout/collections/index>`
   can collide with the cloth. Note that these objects must also have Collision physics enabled.


.. _bpy.types.ClothCollisionSettings.use_self_collision:

Self-Collisions
---------------

Real cloth cannot penetrate itself, so you normally want the cloth to self-collide.
Enable this to tell the cloth object that it should not penetrate itself.
This adds to the simulation's compute time, but provides more realistic results.

.. tip::

   A flag, viewed from a distance does not need this enabled,
   but a close-up of a cape or blouse on a character should have this enabled.

.. _bpy.types.ClothCollisionSettings.self_friction:

Friction
   A coefficient for how slippery the cloth is when it collides with itself.
   For example, silk has a lower coefficient of friction than cotton.

.. _bpy.types.ClothCollisionSettings.self_distance_min:

Distance
   As cloth at this distance begins to repel away from itself.
   Smaller values might give errors but gives some speed-up while
   larger will give unrealistic results if too large and can be slow.
   It is best to find a good in between value.

.. _bpy.types.ClothCollisionSettings.self_impulse_clamp:

Impulse Clamping
   Prevents explosions in tight and complicated collision situations
   by restricting the amount of movement after a collision.

.. _bpy.types.ClothCollisionSettings.vertex_group_self_collisions:

Vertex Group
   Faces that have all vertices assigned to this
   :doc:`Vertex Group </modeling/meshes/properties/vertex_groups/index>` are excluded from self-collision.

.. seealso::

   Example blend-file:
   `Cloth self-collisions <https://archive.blender.org/wiki/2015/index.php/File:Cloth-regression-selfcollisions.blend>`__.


Troubleshooting
===============

If you encounter some problems with collision detection, there are a few ways to fix them:

- The fastest solution is to increase the *Distance* for Object/Self Collisions.
  This will be the fastest way to fix the clipping; however, it will be less accurate and will not look as good.
  Using this method tends to make it look like the cloth is resting on air, and gives it a very rounded look.
- A second method is to increase the *Quality* (in the *Cloth* panel).
  This results in smaller steps for the simulator and
  therefore to a higher probability that fast-moving collisions get caught.
  You can also increase the Collisions *Quality* to perform more iterations to get collisions solved.
- If none of the methods help, you can easily edit the cached/baked result in *Edit Mode* afterwards.
- If the Cloth is torn by the deforming mesh; increase the stiffness settings.
