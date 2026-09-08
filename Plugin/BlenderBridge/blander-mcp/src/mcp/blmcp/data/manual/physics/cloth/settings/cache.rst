*****
Cache
*****

.. reference::

   :Panel:     :menuselection:`Physics --> Cloth Cache`

After you have set up the deflection mesh for the frame range you intend to run the simulation
(including animating that mesh *via* armatures),
you can now tell the cloth simulation to compute (and avoid) collisions.
Select the cloth object and in the *Object* tab,
*Physics* tab, set the *Start* and *End* settings for
the simulation frames you wish to compute, and click the *Bake* button.

Cache settings for cloth are the same as with other dynamic systems.
See :doc:`Particle Cache </physics/particles/emitter/cache>` for details.

.. note::

   If you move or edit the cloth object **after** you have already run the simulations,
   you must clear the cache; otherwise, Blender will use the position of
   the current/cached mesh's vertices when trying to represent where they are.

.. note:: Subdivision Surface Modifier

   A bake/cache is done for every subdivision level so please use
   the **equal** subdivision level for render and preview.

.. note::

   You cannot change *Start* or *End* without clearing the bake simulation.
   When the simulation has finished, you will notice you have the option to free
   the bake, edit the bake and re-bake.


Editing the Cached Simulation
=============================

.. important::

   Editing the cached simulation is not currently working, see:
   `blender/blender#77114 <https://projects.blender.org/blender/blender/issues/77114>`__ for details.

.. The cache contains the shape of the mesh at each frame. You can edit the cached simulation,
   after you have baked the simulation and pressed the *Bake Editing* button.
   Just go to the frame you want to fix and :kbd:`Tab` into *Edit Mode*.
   There you can move your vertices using all of Blender's mesh shaping tools. When you exit,
   the shape of the mesh will be recorded for that frame of the animation.
   If you want Blender to resume the simulation using the new shape going forward,
   select *Rebake from next Frame* and play the animation.
   Blender will then pick up with that shape and resume the simulation.

   Edit the mesh to correct minor tears and
   places where the colliding object has punctured the cloth.

   If you add, delete, or extrude vertices in the mesh, Blender will take the new mesh as
   the starting shape of the mesh back to the *first frame* of the animation,
   replacing the original shape you started with,
   up to the frame you were on when you edited the mesh. Therefore,
   if you change the content of a mesh, when you press :kbd:`Tab` out of *Edit Mode*,
   you should unprotect and clear the cache so that Blender will make a consistent simulation.
