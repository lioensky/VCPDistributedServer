.. _bpy.types.ShaderNodeVolumeCoefficients:

*******************
Volume Coefficients
*******************

.. figure:: /images/node-types_ShaderNodeVolumeCoefficients.png
   :align: right
   :alt: Volume Coefficients node.

The *Volume Coefficients* node models three physical processes in a volume:
Absorption, Scattering and Emission, represented by their coefficients.
Typical usage is to plug in values from real-world measurements.


Inputs
======

Absorption
----------

Coefficients
   Probability density per color channel that light is absorbed per unit distance traveled in the medium.
   It is equivalent to :math:`(1-\text{Color}) \times \text{Density}` in
   :ref:`Volume Absorption <bpy.types.ShaderNodeVolumeAbsorption>`.

Scatter
-------

Coefficients
   Probability density per color channel of an out-scattering event occurring per unit distance traveled in the
   medium. It is equivalent to :math:`\text{Color} \times \text{Density}` in
   :ref:`Volume Scatter <bpy.types.ShaderNodeVolumeScatter>`.
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

.. note::

   Above inputs are the same in :ref:`Volume Scatter <bpy.types.ShaderNodeVolumeScatter>`.


Emission
--------

Coefficients
   Emitted radiance per color channel that is added to a ray per unit distance.
   It is equivalent to :math:`\text{Color} \times \text{Strength}` in :ref:`Emission <bpy.types.ShaderNodeEmission>`.


Properties
==========

Phase
  .. note:: Same as :ref:`Phase <bpy.types.ShaderNodeVolumeScatter.phase>` in Volume Scatter.

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


Outputs
=======

Volume
   The Volume Shader output must be plugged into the *Volume Input*
   of the :doc:`Material </render/shader_nodes/output/material>`
   or :doc:`World </render/shader_nodes/output/world>` Output node.
