******
Render
******

.. reference::

   :Panel:     :menuselection:`Particle System --> Render`

The Render Panel controls how particles appear when they are rendered.

.. note::

   Cycles supports only Object and Collection render types.


Common Settings
===============

Scale

.. todo:: Add this information.

Scale Randomness

.. todo:: Add this information.

Material
   Set which of the object's materials is used to shade the particles.
Coordinates System
   Use a different object's coordinates to determine the birth of particles.
Show Emitter
   When disabled, the emitter is no longer rendered. Activate the button *Emitter* to also render the mesh.


Render As
=========

None
----

When set to *None*, particles are not rendered.
This is useful if you are using the particles to duplicate objects.


.. _particle-halo:

Halo
----

Halos are rendered as glowing dots or a little cloud of light.
Although they are not really lights because they do not cast light into the scene like a light object.
They are called *Halos* because you can see them, but they do not have any substance.


.. _particle-path:

Path
----

.. figure:: /images/physics_particles_emitter_render_path.png

   The Visualization panel for Path visualization.

The *Path* visualization needs a :doc:`Hair </physics/particles/hair/index>` particle system or
:doc:`Keyed </physics/particles/emitter/physics/keyed>` particles.

B-Spline
   Interpolate hair using B-splines.
   This may be an option for you if you want to use low *Render* values.
   You loose a bit of control but gain smoother paths.
Steps
   Set the number of subdivisions of the rendered paths (the value is a power of 2).
   You should set this value carefully,
   because if you increase the render value by two you need four times more memory to render.
   Also the rendering is faster if you use low render values (sometimes drastically).
   But how low you can go with this value depends on the waviness of the hair (the value is a power of 2).
   This means 0 steps give 1 subdivision,
   1 give 2 subdivisions, 2 → 4, 3 → 8, 4 → 16, ... 𝓃 → 2\ :sup:`𝓃`.


Timing
------

.. reference::

   :Panel:     :menuselection:`Particle System --> Render --> Timing`
   :Type:      Hair

Absolute Path Time
   Path timing is in absolute frames.
End
   End time of the practical path.
Random
   Give the path length a random variation.


.. _particle-object:

Object
------

.. reference::

   :Panel:     :menuselection:`Particle System --> Render --> Object`

Instance Object
   The specified object is instanced in place of each particle.

Global Coordinates
   Use object's global coordinates for instancing.
Object Rotation
   Use the rotation of the object.
Object Scale
   Use the size of the object.


.. _particle-collection:

Collection
----------

.. reference::

   :Panel:     :menuselection:`Particle System --> Render --> Collection`

Instance Collection
   The objects that belong to a collection are instanced sequentially in the place of the particles.
Whole Collection
   Use the whole group at once, instead of one of its elements, the group being displayed in place of each particle.
Pick Random
   The objects in the group are selected in a random order, and only one object is displayed in place of a particle.
Global Coordinates
   Use object's global coordinates for instancing.
Object Rotation
   Use the rotation of the objects.
Object Scale
   Use the size of the objects.


Use Count
^^^^^^^^^

.. reference::

   :Panel:     :menuselection:`Particle System --> Render --> Collection --> Use Count`

Use objects multiple times in the same groups.
Specify the order and number of times to repeat each object with the :ref:`list view <ui-list-view>` that appears.

:bl-icon:`add` Copy Particle Instance Object
   Duplicates the selected object in the list.
:bl-icon:`remove` Remove Particle Instance Object
   Removes the selected object from the list.


Extra
=====

.. reference::

   :Panel:     :menuselection:`Particle System --> Render --> Extra`

.. _bpy.types.ParticleSettings.use_parent_particles:

Parents Particles
   Render also parent particles if child particles are used.
   Children have a lot of different deformation options,
   so the straight parents would stand between their curly children.
   So by default *Parents* are not rendered if you activate *Children*.
   See :doc:`Children </physics/particles/emitter/children>`.

Unborn
   Render particles before they are born.
Dead
   Render particles after they have died.
   This is very useful if particles die in a collision *Die on hit*, so you can cover objects with particles.
