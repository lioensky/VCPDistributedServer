.. index:: Force Fields; Fluid Force

**********
Fluid Flow
**********

.. reference::

   :Panel:     :menuselection:`Physics --> Force Fields`
   :Type:      Fluid Flow

The *Fluid Flow* force field creates a force based on a :doc:`Fluid simulation </physics/fluid/index>` air flow.
It applies the smoke simulation air flow velocity as a force to other simulations that use force fields.
To use it you need to add a *Fluid Flow* force field and select a domain object for it.
For example fire sparkles can realistically flow along the air turbulence near the simulated fire.


Options
=======

.. figure:: /images/physics_forces_force-fields_types_fluid-flow_panel.png

   UI for a Fluid Flow force field.

Domain Object
   An object that is used as a domain for the smoke simulation.
Apply Density
   Adjust the force strength based on the smoke density.
