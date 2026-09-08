.. _bpy.types.ShaderNodeBsdfGlass:

**********
Glass BSDF
**********

.. figure:: /images/node-types_ShaderNodeBsdfGlass.webp
   :align: right
   :alt: Glass BSDF node.

The *Glass* :abbr:`BSDF (Bidirectional Scattering Distribution Function)`
is used to add a Glass-like shader mixing refraction and reflection at grazing angles.
Like the transparent shader, only pure white will make it transparent.
The glass shader tends to cause noise due to caustics.
Since the Cycles path tracing integrator is not very good at rendering caustics,
it helps to combine this with a transparent shader for shadows;
for :ref:`more details see here <render-cycles-reducing-noise-glass-and-transp-shadows>`.


Inputs
======

Color
   Color of the surface, or physically speaking, the probability that light is transmitted for each wavelength.
Roughness
   Influences sharpness of the refraction; perfectly sharp at 0.0 and smoother with higher values.
IOR
   Index of refraction (:term:`IOR`) defining how much the ray changes direction. At 1.
   0 rays pass straight through like transparent; higher values give more refraction.
Normal
   Normal used for shading.


Thin Film :guilabel:`Cycles Only`
---------------------------------

Thin Film simulates the effect of interference in a thin film sitting on top of the material.
This causes the specular reflection to be colored in a way which strongly depends on the view
angle as well as the film thickness and the index of refraction (:term:`IOR`) of the film and
the material itself.

This effect is commonly seen on e.g. oil films, soap bubbles or glass coatings. While its
influence is more obvious in specular highlights, it also affects transmission.

Thickness
   The thickness of the film in nanometers. A value of 0 disables the simulation.
   The interference effect is strongest between roughly 100 and 1000 nanometers, since this is
   near the wavelengths of visible light.
IOR
   Index of refraction (:term:`IOR`) of the thin film.
   The common range for this value is between 1.0 (vacuum and air) and roughly 2.0,
   though some materials can reach higher values.
   The default value of 1.33 is a good approximation for water.
   Note that when the value is set to 1.0 or to the main IOR of the material, the thin film
   effect disappears since the film optically blends into the air or the material.


Properties
==========

Distribution
   Microfacet distribution to use.

   :GGX: GGX microfacet distribution.
   :Multiscatter GGX:
      Takes multiple scattering events between microfacets into account.
      This gives more energy conserving results, which would otherwise be visible as excessive darkening.
   :Beckmann: :guilabel:`Cycles Only`
      Beckmann microfacet distribution.


Outputs
=======

BSDF
   Standard shader output.


Examples
========

.. list-table::
   :widths: auto

   * - .. figure:: /images/render_shader-nodes_shader_glass_example.jpg

          Sharp Glass example.

     - .. figure:: /images/render_shader-nodes_shader_glass_behavior-sharp.svg
          :width: 308px

          Sharp Glass behavior.

   * - .. figure:: /images/render_shader-nodes_shader_glass_example-rough.jpg

          Rough Glass example.

     - .. figure:: /images/render_shader-nodes_shader_glass_behavior.svg
          :width: 308px

          Rough Glass behavior.
