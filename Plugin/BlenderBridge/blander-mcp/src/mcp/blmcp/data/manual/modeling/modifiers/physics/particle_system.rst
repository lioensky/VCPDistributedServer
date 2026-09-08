.. index:: Modeling Modifiers; Particle System Modifier

************************
Particle System Modifier
************************

The Particle System modifier is a container for :doc:`Particle Systems </physics/particles/index>`.

.. note::

   By default the Particle System modifier does not take into account the :ref:`modifier stack <modifier-stack>`.
   Make sure to enable :ref:`Use Modifier Stack <bpy.types.ParticleSettings.use_modifier_stack>`
   in the Particle properties if you want Particle System modifier to take other modifiers into account.


Options
=======

As the modifier is only a container its actual options are configured in the *Particle Properties* tab.
See the :doc:`Particle Systems Properties </physics/particles/index>` for more information.


Converting Particle Systems
===========================

Make Instances Real
   Creates a new object of each instanced :ref:`object <particle-object>` or :ref:`collection <particle-collection>`.
   See :ref:`bpy.ops.object.duplicates_make_real` for more information.

Convert to Mesh
   Converts :ref:`path <particle-path>` particles to mesh objects.
   See :ref:`bpy.ops.object.convert` for more information.


Example
=======

.. figure:: /images/physics_particles_introduction_fur-example.jpg

   Fur made from particles.
