.. _bpy.types.FluidDomainSettings.use_adaptive_domain:

***************
Adaptive Domain
***************

.. reference::

   :Type:      Domain
   :Panel:     :menuselection:`Physics --> Fluid --> Adaptive Domain`

When enabled, the domain will adaptively shrink to best fit the gas,
saving computation time by leaving voxels without gas out of the simulation.
Unless the *Add Resolution* is used, the adaptive domain will not exceed the bounds of the original domain.

.. _bpy.types.FluidDomainSettings.additional_res:

Add Resolution
   Number of voxels to add around the outside of the domain.

.. _bpy.types.FluidDomainSettings.adapt_margin:

Margin
   Amount of extra space to leave around gas, measured in voxels.
   With very fast-moving gas larger margins may be required to prevent the gas from being cut off
   by the adaptive boundary, but note this will increase the number of voxels which need to be computed.

.. _bpy.types.FluidDomainSettings.adapt_threshold:

Threshold
   Smallest amount of gas a voxel can contain before it is considered empty
   and the adaptive domain is allowed to cut it out of the simulation.
