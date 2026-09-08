
*********************
Particle System Panel
*********************

.. reference::

   :Panel:     :menuselection:`Particle System --> Particle System`

.. figure:: /images/physics_particles_particle-system-panel_panel.png

   Particle System panel.

These are the basic settings.

Active Particle System
   The :ref:`List View <ui-list-view>` of the objects Particle Modifier(s).

   Specials
      Copy Active to Selected Objects
         Copies the active particle system to all selected objects.
      Copy All to Selected Objects
         Copies all particle systems from the active object to all selected objects.
      Duplicate Particle Systems
         Duplicates the particle system within the active object.
         The *Duplicate Settings* option (in the :ref:`bpy.ops.screen.redo_last` panel) will duplicate
         settings as well, so the new particle system uses its own settings.

      .. _bpy.ops.particle.particle_system_remove_all:

      Remove All Particle Systems
         Remove all particle system within the active object.

Particle Settings
   The :ref:`Data-Block menu <ui-data-block>` for settings.

Type
   Main selector of the system type.

   Emitter
      In such a system, particles are :doc:`emitted </physics/particles/emitter/index>` from the object.
   Hair
      Use :doc:`Hair </physics/particles/hair/index>` type, rendered as strands.

      Regrow
         Regrows the hair for each frame. This is useful when you are animating properties.
      Advanced
         Enables advanced settings which reflect the same ones as working in Emitter mode.

         .. note::

            This manual assumes that this option is enabled.

      Segments
         Controls the number of parts a hair is made of.
         Increasing this value will improve the quality of animations.


Workflow
========

The process for working with standard particles is:

#. Create the mesh which will emit the particles.
#. Create one or more Particle Systems to emit from the mesh. Many times, multiple
   particle systems interact or merge with each other to achieve the overall desired effect.
#. Tailor each Particle System's settings to achieve the desired effect.
#. Animate the base mesh and other particle meshes involved in the scene.
#. Define and shape the path and flow of the particles.
#. For :doc:`Hair </physics/particles/hair/index>` particle systems: Sculpt the emitter's flow
   (cut the hair to length and comb it for example).
#. Make final render and do physics simulation(s), and tweak as needed.


Creating a Particle System
--------------------------

.. figure:: /images/physics_particles_particle-system-panel_create-new.png

   Adding a particle system.

To add a new particle system to an object, go to the *Particles* tab of the Properties
editor and click the :bl-icon:`add` button. An object can have many Particle Systems.

Each particle system has separate settings attached to it.
These settings can be shared among different particle systems, so one does not have to copy
every setting manually and can use the same effect on multiple objects.


Types of Particle Systems
^^^^^^^^^^^^^^^^^^^^^^^^^

.. _fig-particle-intro-system-type:

.. figure:: /images/physics_particles_particle-system-panel_select-type.png

   Particle System Types.

After you have created a particle system,
the Properties fills with many panels and buttons.
But do not panic! There are two different types of particle systems,
and you can change between these two with the *Type* selector:
Emitter and Hair.

The settings in the *Particle System* tab are partially different for each system type.
