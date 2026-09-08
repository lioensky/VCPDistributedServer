
*******
Volumes
*******

.. reference::

   :Panel:     :menuselection:`Render --> Volumes`

.. _bpy.types.CyclesRenderSettings.volume_biased:

Biased
   Default volume rendering algorithm is based on null scattering, which is unbiased and has less artifacts,
   but could be noisier. Biased option uses ray marching, with controls for steps size and max steps.

.. note::
   The following only exists for biased ray marching.

Volume *Step* size is the distance between volume shader samples.
Cycles automatically estimates this distance based on voxel size in
volume objects and smoke simulations.

Render time can be reduced by increasing the step size, at the cost of
potentially losing some volume detail. For procedural volume shaders
that add detail, step size can be increased per object, material or world.

.. _bpy.types.CyclesRenderSettings.volume_step_rate:

Step Rate Render :guilabel:`Biased`
   Global multiplier on the step size for all volumes in renders.
   Increase to reduce render time, at the cost of losing detail.

.. _bpy.types.CyclesRenderSettings.volume_preview_step_rate:

Viewport :guilabel:`Biased`
   Global multiplier on the step size for all volumes in the viewport.
   Increase for more responsive viewport rendering.

.. _bpy.types.CyclesRenderSettings.volume_max_steps:

Max Steps :guilabel:`Biased`
   Maximum number of steps through the volume before giving up,
   to protect from extremely long render times with big objects or small step sizes.
