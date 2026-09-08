.. _bpy.types.ShaderNodeVolumeScatter:

**************
Volume Scatter
**************

.. figure:: /images/node-types_ShaderNodeVolumeScatter.png
   :align: right
   :alt: Volume Scatter node.

The *Volume Scatter* node allows light to be scattered as it passes through the volume.
Typical usage would be to add fog to a scene. It can also be used with
the :doc:`Volume Absorption </render/shader_nodes/shader/volume_absorption>` node to create smoke.


Inputs
======

Color
   Scattering coefficients per color channel.
Density
   The density of the scatter effect.
Anisotropy :guilabel:`Henyey-Greenstein` :guilabel:`Draine`
   Controls the relative amount of backward and forward scattering.
IOR :guilabel:`Fournier-Forand`
   Refractive index of the scattering particles relative to water. Common ocean waters range between
   1.0 and 1.2, while turbid waters with higher density of particles have higher IORs.
Backscatter :guilabel:`Fournier-Forand`
   Fraction of light that is scattered backwards. Most oceanic particles have backscatter
   values between 0.001 (e.g., very large phytoplankton) and 0.1 (e.g., very small mineral particles),
   pure water has a backscatter of 0.5. Values taken from
   `Ocean Optics Web Book <https://www.oceanopticsbook.info/view/scattering/the-fournier-forand-phase-function>`__.
Alpha :guilabel:`Draine`
   Blending factor between Henyey-Greenstein (:math:`\alpha = 0`)
   and Cornette & Shanks (:math:`\alpha = 1`) phase functions.
Diameter :guilabel:`Mie`
   Diameter of the scattering particles in µm.


Properties
==========

.. _bpy.types.ShaderNodeVolumeScatter.phase:

Phase
  Volume scattering phase function.

  :Henyey-Greenstein:
     Simple and widely used phase function, useful for approximating scattering in biological tissues.
  :Fournier-Forand:
     :guilabel:`Cycles Only`
     Suitable for modeling the scattering of light in underwater environments.
  :Draine:
     :guilabel:`Cycles Only`
     Suitable for modeling the scattering of interstellar dust.
  :Rayleigh:
     :guilabel:`Cycles Only`
     Describes the scattering by particles with a size smaller than the wavelength of light,
     such as the scattering of sunlight in earth's atmosphere.
  :Mie:
     :guilabel:`Cycles Only`
     Describes the scattering by particles with a size larger than the wavelength of light, such as cloud and fog.

  .. tip::
      These phase functions can be combined using a :doc:`/render/shader_nodes/shader/mix`.

.. figure:: /images/render_shader-nodes_shader_volume-scatter_phase.svg
   :align: center
   :alt: Volume Scattering Function in logarithmic scale.

   Volume scattering phase as a function of angles between the incoming and the outgoing direction,
   in logarithmic scale. Light comes from the left side.

Outputs
=======

Volume
   The Volume Shader output must be plugged into the *Volume Input*
   of the :doc:`Material </render/shader_nodes/output/material>`
   or :doc:`World </render/shader_nodes/output/world>` Output node.


Examples
========

.. figure:: /images/render_shader-nodes_shader_volume-scatter_example.png

   Example of Volume Scatter.
