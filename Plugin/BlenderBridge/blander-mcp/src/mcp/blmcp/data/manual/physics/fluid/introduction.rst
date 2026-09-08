
************
Introduction
************

Liquid Simulations
==================

Fluid physics are used to simulate physical properties of liquids especially water.
While creating a scene in Blender, certain objects can be marked to become a part of the fluid simulation.
For a fluid simulation you have to have a domain to define the space that the simulation takes up.
In the domain settings you will be able to define the global simulation parameters (such as viscosity
and gravity).

.. figure:: /images/physics_fluid_introduction_liquid-example.png
   :align: center

   Example of a liquid simulation.


Gas Simulations
===============

Gas or smoke simulations are a subset of the fluids system, and can be used for simulating collections
of airborne solids, liquid particulates and gases, such as those that make up smoke.
It simulates the fluid movement of air and generates animated :term:`Voxel`
textures representing the density, heat, and velocity of other fluids or suspended particles
(e.g. smoke) which can be used for rendering.

.. figure:: /images/physics_fluid_introduction_fire-example.png
   :align: center

   Example of a fire simulation.

Gases or smoke are emitted inside of a :doc:`Domain </physics/fluid/type/domain/index>` from
a mesh object or particle system. The smoke movement is controlled by airflow inside the domain,
which can be influenced by :doc:`Effector </physics/fluid/type/effector>` objects.
Smoke will also be affected by the scene's gravity and :doc:`force fields </physics/forces/force_fields/index>`.
Airflow inside the domain can affect other physics simulations
via the :doc:`Fluid Flow </physics/forces/force_fields/types/fluid_flow>` force field.


Workflow
========

At least a :doc:`Domain </physics/fluid/type/domain/index>` object and
one :doc:`Flow </physics/fluid/type/flow>` object are required to create a fluid simulation.

#. Create a :doc:`Domain object </physics/fluid/type/domain/index>`
   that defines the bounds of the simulation volume.
#. Set up :doc:`Flow </physics/fluid/type/flow>` objects which will emit fluid.
#. Set up :doc:`Effector </physics/fluid/type/effector>` objects to make
   the fluid interact with objects in the scene.
#. Assign a :doc:`material </physics/fluid/material>` to the domain object.
#. Save the blend-file.
#. :doc:`Bake the Cache </physics/fluid/type/domain/cache>` for the simulation.

.. note::

   There are :ref:`Quick Liquid and Quick Smoke <bpy.ops.object.quick>` tools
   which will automatically create a domain object with a basic liquid or smoke and fire material.
