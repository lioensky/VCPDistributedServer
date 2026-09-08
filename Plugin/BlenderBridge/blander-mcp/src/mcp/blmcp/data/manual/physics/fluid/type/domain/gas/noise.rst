.. _bpy.types.FluidDomainSettings.use_noise:

*****
Noise
*****

.. reference::

   :Type:      Domain
   :Panel:     :menuselection:`Physics --> Fluid --> Noise`

Adding noise to the gas simulation creates a finer detailed looking simulation on top of the base.
This makes it possible to add more details to gases (i.e. fire or smoke or both) without changing
the overall fluid motion.

.. seealso::

   Fluid noise is an implementation of `Wavelet Turbulence for Fluid Simulation
   <http://www.cs.cornell.edu/~tedkim/WTURB/>`__.

Besides enabling parts of the interface, checking *Noise* lets the cache know
which simulation data to read. If, for example, *Noise* is enabled but
there is no noise simulation data to read it will show an empty domain.
The checkbox does not reset the cache and can be used to switch
the view between base resolution and noise view.

.. _bpy.types.FluidDomainSettings.noise_scale:

Upres Factor
   Factor by which to enhance the resolution of the noise. The scaling factor is coupled
   to the :ref:`Resolution Divisions <bpy.types.FluidDomainSettings.resolution_max>`.

.. _bpy.types.FluidDomainSettings.noise_strength:

Strength
   Strength of the noise. Higher values result in more turbulent vortices.

.. _bpy.types.FluidDomainSettings.noise_pos_scale:

Scale
   Scale of the noise. Greater values result in larger vortices.

.. _bpy.types.FluidDomainSettings.noise_time_anim:

Time
   Animation time of the noise. This value has an influence on where the noise field is evaluated.
   It can be used as a seed to give wavelet noise a slightly different look in two domains that are
   otherwise the same.

   .. list-table:: Smoke plume with varying animation time. While the fluid motion of all four smoke
      plumes are alike each example has a unique look.

      * - .. figure:: /images/physics_fluid_type_domain_gas_noise_timeanim-0-1.png

             Animation Time: 0.1

        - .. figure:: /images/physics_fluid_type_domain_gas_noise_timeanim-1-0.png

             Animation Time: 1.0

      * - .. figure:: /images/physics_fluid_type_domain_gas_noise_timeanim-2-5.png

             Animation Time: 2.5

        - .. figure:: /images/physics_fluid_type_domain_gas_noise_timeanim-10-0.png

             Animation Time: 10.0

   .. note::

      *Resolution Divisions* and *Upres Factor* are not equivalent.
      By using different combinations of these resolution settings,
      you can obtain a variety of different styles of smoke.

   .. list-table:: Comparison of fire simulations with and without noise at the same grid
      resolution.

      * - .. figure:: /images/physics_fluid_type_domain_gas_noise_base-res-1.png

             Resolution Divisions: 200, without noise

        - .. figure:: /images/physics_fluid_type_domain_gas_noise_base-res-2.png

             Resolution Divisions: 100, Noise scale: 2.

   Low division simulations with lots of *Upres Factor* divisions generally appear smaller in
   real-world scale and can be used to achieve pyroclastic plumes such as in the following image:

   .. figure:: /images/physics_fluid_type_domain_gas_noise_note-resolution.jpg
      :align: center

.. _bpy.ops.fluid.bake_noise:
.. _bpy.ops.fluid.free_noise:

Bake Noise, Free Noise
   This option is only available when using the :ref:`Modular <bpy.types.FluidDomainSettings.cache_type>` cache type.

   The progress will be displayed in the status bar. Pressing :kbd:`Esc` will pause the simulation.

   Once the simulation has been baked, the cache can be deleted by pressing *Free Noise*.
   It is possible to pause or resume a *Bake Noise* process.
