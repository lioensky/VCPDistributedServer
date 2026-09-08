.. _bpy.types.FluidDomainSettings.use_guide:

******
Guides
******

.. reference::

   :Panel:     :menuselection:`Physics --> Fluid --> Guides`
   :Type:      Domain

Fluid guides are used to apply forces onto the simulation. They are like simple external forces
but also seek to preserve the physically accurate flow of the fluid.
The *Guides* panel allows you to adjust guiding forces globally, i.e. for the entire domain.
Enabling the guides hints the fluid solver to use the more accurate,
but also computationally more expensive pressure solving step.

Even when there are no guiding objects baked or there is no guiding domain attached,
the fluid solver will still perform the more expensive pressure guiding algorithm
if guiding is enabled. It is
therefore recommended to only enable *Guides* when there is a clear intention to
use guiding in the simulation.

.. seealso::

   Fluid guiding is an implementation of
   `Primal-Dual Optimization for Fluids <https://ge.in.tum.de/publications/2017-cgf-eckert/>`__.

.. _bpy.types.FluidDomainSettings.guide_alpha:

Weight
   Controls the lag of the guiding. A larger value (also known as the 'alpha' guiding value)
   results in a greater lag.

.. _bpy.types.FluidDomainSettings.guide_beta:

Size
   This setting determines the size of the vortices that the guiding produces.
   A greater guiding size (also known as the blur radius or 'beta' guiding value)
   results in larger vortices.

.. _bpy.types.FluidDomainSettings.guide_vel_factor:

Velocity Factor
   All guiding velocities are multiplied by this factor. That is, every cell of the guiding grid,
   which has the same size as the domain object, is multiplied by this factor.

.. _bpy.types.FluidDomainSettings.guide_source:

Velocity Source
   Guiding velocities can either come from objects that move inside the domain or from other fluid
   domains.

   :Effector:
      All effector objects inside the domain will be considered for the global guiding velocity grid.
      Once effector objects have been baked it is not possible to change the fluid domain resolution
      anymore.
   :Domain:
      When using another fluid domain as the guiding velocity source this domain may have a different
      resolution and may also be of a different type (e.g. the guiding domain is of type *Gas*
      while the actual domain with the guiding effect in it is of type *Liquid*).

      In order to use a domain as the velocity source, this domain needs to be baked already.

.. _bpy.types.FluidDomainSettings.guide_parent:

Guide Parent
   When using *Domain* as the velocity source, this field serves to select the guiding domain object.

.. _bpy.ops.fluid.bake_guides:
.. _bpy.ops.fluid.free_guides:

Bake Guides, Free Guides
   This option is only available when using the :ref:`Modular <bpy.types.FluidDomainSettings.cache_type>` cache type
   and when using *Effector* as the :ref:`Velocity Source <bpy.types.FluidDomainSettings.guide_source>`.
   *Bake Guides* writes vertex velocities of effector objects to drive.
   It is meant to be used before baking the fluid simulation.

   The progress will be displayed in the status bar. Pressing :kbd:`Esc` will pause the simulation.

   Once the simulation has been baked, the cache can be deleted by pressing *Free Guides*.
   It is possible to pause or resume a *Bake Guides* process.
