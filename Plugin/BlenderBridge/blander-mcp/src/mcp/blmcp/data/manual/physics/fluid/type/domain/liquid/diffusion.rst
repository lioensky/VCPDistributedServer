.. |m2.s-1| replace:: :math:`m^{2}/s`
.. |kg.m-3| replace:: :math:`kg/m^{3}`
.. |Pa.s| replace:: :math:`Pa\cdot s`

.. _bpy.ops.fluid.preset:
.. _bpy.types.FluidDomainSettings.use_diffusion:

*********
Diffusion
*********

.. reference::

   :Type:      Domain
   :Panel:     :menuselection:`Physics --> Fluid --> Diffusion`

Liquid diffusion defines the physical properties of a liquid
and in turn define how a liquid interacts with its environment.
The main factors of diffusion are the *Viscosity* and *Surface Tension*.
These properties can be adjusted to create virtual liquids that behave like water,
oil, honey, or any other liquid. A couple presets exist to change the diffusion
for different substances are predefined and can be changed in the preset menu.
Fluid Diffusion settings can be enabled/disabled in the panel header.

.. rubric:: Viscosity

The viscosity refers to the "thickness" of the fluid and actually the force needed to
move an object of a certain surface area through it at a certain speed.

For manual entry, please note that real-world viscosity
(the so-called dynamic viscosity) is normally measured in Pascal-seconds (|Pa.s|),
or in Poise units (P, equal to 0.1 |Pa.s|), and commonly centiPoise units (cP, equal to 0.001 |Pa.s|).

Blender, on the other hand, uses the kinematic viscosity which is the dynamic viscosity divided by
the density, :math:`\frac{Pa\cdot s}{kg/m^{3}}`, which is |m2.s-1|. So for example, the viscosity
of water at room temperature is 1.002 cP, or 0.001002 |Pa.s|; the density of water is about
1000 |kg.m-3|, which gives a kinematic viscosity of 0.000001002 |m2.s-1| --  so the entry would be
1.002 times 10 to the minus six (1.002×10\ :sup:`-6` in scientific notation).

The table below gives some examples of fluids together with their dynamic and kinematic viscosities.

.. list-table:: Blender viscosity unit conversion.
   :header-rows: 1

   * - Fluid
     - Dynamic viscosity (in cP)
     - Kinematic viscosity (Blender, in |m2.s-1|)
   * - Water (20 °C)
     - 1.002×10\ :sup:`0` (1.002)
     - 1.002×10\ :sup:`-6` (0.000001002)
   * - Oil SAE 50
     - 5.0×10\ :sup:`2` (500)
     - 5.0×10\ :sup:`-5` (0.00005)
   * - Honey (20 °C)
     - 1.0×10\ :sup:`4` (10,000)
     - 2.0×10\ :sup:`-3` (0.002)
   * - Chocolate Syrup
     - 3.0×10\ :sup:`4` (30,000)
     - 3.0×10\ :sup:`-3` (0.003)
   * - Ketchup
     - 1.0×10\ :sup:`5` (100,000)
     - 1.0×10\ :sup:`-1` (0.1)
   * - Melting Glass
     - 1.0×10\ :sup:`15`
     - 1.0×10\ :sup:`0` (1.0)

.. tip::

   You can find the kinematic viscosity of more materials in the proper units by
   asking Wolfram Alpha, e.g. `"kinematic viscosity of alcohol in m^2/s"
   <https://www.wolframalpha.com/input?i=kinematic+viscosity+of+alcohol+in+m%5E2%2Fs>`__.

To simplify the input of these numbers, the viscosity is changed by entering values
in scientific notation by entering a base value and the exponent of that number.

.. _bpy.types.FluidDomainSettings.viscosity_base:

Base
   The base of the viscosity value (e.g. 1.002 in the case of water (20 °C)).

.. _bpy.types.FluidDomainSettings.viscosity_exponent:

Exponent
   The exponent of the viscosity value that will be multiplied by 10\ :sup:`-1`
   (e.g. 6 in the case of water (20 °C)).

.. note:: Viscosity Varies

   The default values in Blender are considered typical for those types of fluids and "look right" when animated.
   However, actual viscosity of some fluids,
   especially sugar-laden fluids like chocolate syrup and honey, depend highly on temperature and concentration.
   Oil viscosity varies by :abbr:`SAE (Society of Automobile Engineers)` rating.
   Glass at room temperature is basically a solid, but glass at 1500 °C flows (nearly) like water.

.. warning::

   The simulator is not suitable for non-fluids, such as materials that do not "flow".
   Simply setting the viscosity to very large values will not result in rigid body behavior,
   but might cause instabilities.

.. _bpy.types.FluidDomainSettings.surface_tension:

Surface Tension
   Surface tension in grid units. Higher value will produce liquids with greater surface tension.


.. _bpy.types.FluidDomainSettings.use_viscosity:

High Viscosity Solver
=====================

The high viscosity liquid solver can be used to simulate fluids with increased viscosity,
replicating the behavior of substances like honey or molasses.
This specialized solver enhances the accuracy of slow-moving and thick liquid simulations.

.. tip::

   A *Strength* value of 0 will still apply some viscosity.
   Uncheck the *High Viscosity Solver* to disable the high viscosity liquid solver simulation step completely.

.. _bpy.types.FluidDomainSettings.viscosity_value:

Strength
   The viscosity of the liquid. Higher values result in more viscous fluids.

   .. list-table:: Rotating liquid inflow with varying viscosities.

      * - .. figure:: /images/physics_fluid_type_domain_liquid_viscosity_0-2.png

             Strength of 0.2 (at frame 65).

        - .. figure:: /images/physics_fluid_type_domain_liquid_viscosity_0-4.png

             Strength of 0.4 (at frame 200).
