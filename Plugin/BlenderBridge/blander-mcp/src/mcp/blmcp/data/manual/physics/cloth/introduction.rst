
************
Introduction
************

Cloth simulation is one of the hardest aspects of computer graphics,
it is a deceptively simple real-world item that is taken for granted,
but it actually has very complex internal and environmental interactions.
Cloth is commonly modeled as 2D mesh to simulate real world objects such as fabrics, flags, banners.
And yet cloth can also be used to model 3D objects such as teddy bears, pillows, balloons, or balls.

Cloth interacts with and is affected by other moving objects,
the wind and other forces, as well as a general aerodynamic model,
all of which is under your control.

.. list-table::

   * - .. figure:: /images/physics_cloth_introduction_example1.jpg

          Cloth example.

     - .. figure:: /images/physics_cloth_introduction_oncarved-wood.jpg

          Cloth on carved wooden men (made by motorsep).

     - .. figure:: /images/physics_cloth_introduction_example2.jpg

          Cloth example.

Once Cloth physics have been added to a mesh, a :doc:`/modeling/modifiers/physics/cloth`
will be added to the object's modifier stack. As a modifier then,
it can interact with other modifiers, such as *Armature* and *Smooth*. In these cases,
the ultimate shape of the mesh is computed in accordance with the order of the modifier stack.
For example, you should smooth the cloth *after* the modifier computes the shape of the cloth.

You can *Apply* the Cloth Modifier to freeze, or lock in,
the shape of the mesh at that frame, which removes the modifier. For example,
you can drape a flat cloth over a table, let the simulation run, and then apply the modifier.
In this sense, you are using the simulator to save yourself a lot of modeling time.

Results of the simulation are saved in a cache, so that the shape of the mesh,
once calculated for a frame in an animation, does not have to be recomputed again.
If changes to the simulation are made, you have full control over clearing the cache and re-running the simulation.
Running the simulation for the first time is fully automatic and no baking or separate step interrupts the workflow.

Computation of the shape of the cloth at every frame is automatic and done in the background;
thus you can continue working while the simulation is computed. However, it is CPU-intensive
and depending on the power of your PC and the complexity of the simulation,
the amount of CPU needed to compute the mesh varies, as does the lag you might notice.

.. note:: Do Not Jump Ahead

   If you set up a cloth simulation but Blender has not computed the shapes for the duration of the simulation,
   and if you jump ahead a lot of frames forward in your animation,
   the cloth simulator may not be able to compute or show you an accurate mesh shape for that frame,
   if it has not previously computed the shape for the previous frame(s).


Workflow
========

A general process for working with cloth is to:

#. Model the cloth object as a general starting shape.
#. Designate the object as a "cloth" in the *Physics* tab of the Properties.
#. Model other deflection objects that will interact with the cloth.
   Ensure the Deflection modifier is last on the modifier stack, after any other mesh deforming modifiers.
#. Light the cloth and assign materials and textures, UV unwrapping if desired.
#. If desired, give the object particles, such as steam coming off the surface.
#. Run the simulation and adjust settings to obtain satisfactory results.
   The Timeline editors playback controls are great for this step.
#. Optionally age the mesh to some point in the simulation to obtain a new default starting shape.
#. Make minor edits to the mesh on a frame-by-frame basis to correct minor tears.

.. tip::

   To avoid unstable simulation, make sure that the cloth object does not penetrate any of the deflection objects.


.. _physics-cloth-introduction-springs:

Springs
=======

Internally, cloth physics is simulated with virtual springs that connect the vertices of a mesh.
There are four types of springs that control how the cloth bends.
These four types are defined below and illustrated in the following image:

.. figure:: /images/physics_cloth_introduction_springs.png
   :align: center

   Illustration of cloth springs; tension springs (blue),
   compression springs (red), shear springs (cyan),
   and angular bending springs (green).

Tension Springs
   Control the stiffness of the cloth.
Compression Springs
   Control the amount of force required to collapse or compress the cloth.
Shear Springs
   Like compression springs but it controls the angular deformation.
Angular Bending Springs
   Control how resilient the cloth is to folding or crumpling.

All four of these spring types can be controlled independently in
the :doc:`/physics/cloth/settings/physical_properties` panel. While these settings
control surface springs, optionally, internal springs can be used for 3D meshes
and behave similarly to :doc:`Soft Bodies </physics/soft_body/index>`.
