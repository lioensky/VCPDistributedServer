.. _bpy.types.ShaderNodeBsdfMetallic:

*************
Metallic BSDF
*************

.. figure:: /images/node-types_ShaderNodeBsdfMetallic.webp
   :align: right
   :alt: Metallic BSDF node.

The *Metallic* :abbr:`BSDF (Bidirectional Scattering Distribution Function)`
node is used to recreate the appearance of metals.


Inputs
======

F82 Tint
--------

Base Color
   Color of the material when viewed straight on.

Edge Tint
   Color of the material when viewed at a 82° angle.

Physical Conductor
------------------

IOR
   Refractive index per color channel. This is the real part of a complex refractive index,
   scientifically denoted as n.

Extinction
   Extinction coefficients per color channel. This is the imaginary part of a
   complex refractive index, scientifically denoted as k.

Common
------

Roughness
   Sharpness of the reflection; perfectly sharp at 0.0 and smoother with higher values.

Anisotropy :guilabel:`Cycles Only`
   Amount of anisotropy. Higher values give elongated highlights along the tangent direction;
   negative values give highlights shaped perpendicular to the tangent direction.

Rotation :guilabel:`Cycles Only`
   Rotates the direction of anisotropy, with 1.0 going full circle.

   Compared to the *Glossy BSDF* node, the direction of highlight elongation
   is rotated by 90°. Add 0.25 to the value to correct.

Normal
   Normal used for shading; if nothing is connected the default shading normal is used.

Tangent
   Tangent used for shading; if nothing is connected the default shading tangent is used.


Properties
==========

Distribution
   Microfacet distribution to use.

   :GGX:
      GGX microfacet distribution.
   :Multiscatter GGX:
      Takes multiple scattering events between microfacets into account.
      This gives more energy conserving results, which would otherwise be visible as excessive darkening.
   :Beckmann: :guilabel:`Cycles Only`
      Beckmann microfacet distribution.

Fresnel Type
   Models for describing the metal's appearance, by specifying the apparent color or the physical IOR.

   :F82 Tint:
      Uses the `Adobe F82-Tint formula <https://helpx.adobe.com/content/dam/substance-3d/general-knowledge/asm/Adobe%20Standard%20Material%20-%20Technical%20Documentation%20-%20May2023.pdf>`__
      for the metallic fresnel. This allows for artist friendly control of the color near the edge of the
      material to simulate a complex IOR.
   :Physical Conductor:
      Accepts Complex IOR measurements from real world metals to replicate a more accurate rendering
      of metals than the *F82 Tint* Fresnel type.

      Complex IOR values can be found from sources like the
      `Physically Based database for CG artists <https://physicallybased.info/>`__
      and `Refractive Index nk database <https://refractiveindex.info/>`__.


Outputs
=======

BSDF
   Standard shader output.


Examples
========

F82 Tint
--------

.. list-table::
   :widths: 12 22 22 22 22

   * -
     - .. figure:: /images/render_shader-nodes_shader_metallic_f82-Ti.webp
     - .. figure:: /images/render_shader-nodes_shader_metallic_f82-Al.webp
     - .. figure:: /images/render_shader-nodes_shader_metallic_f82-Cu.webp
     - .. figure:: /images/render_shader-nodes_shader_metallic_f82-Au.webp
   * - Material
     - Titanium (Default)
     - Aluminum
     - Copper
     - Gold
   * - Base Color
     - 0.617, 0.576, 0.540
     - 0.911, 0.912, 0.917
     - 0.972, 0.694, 0.486
     - 1.000, 0.735, 0.353
   * - Edge Tint
     - 0.695, 0.726, 0.770
     - 0.848, 0.877, 0.916
     - 0.961, 0.969, 0.942
     - 0.993, 1.000, 1.000

Physical Conductor
------------------

.. list-table::
   :widths: 12 22 22 22 22

   * -
     - .. figure:: /images/render_shader-nodes_shader_metallic_physical-Ti.webp
     - .. figure:: /images/render_shader-nodes_shader_metallic_physical-Al.webp
     - .. figure:: /images/render_shader-nodes_shader_metallic_physical-Cu.webp
     - .. figure:: /images/render_shader-nodes_shader_metallic_physical-Au.webp
   * - Material
     - Titanium (Default)
     - Aluminum
     - Copper
     - Gold
   * - IOR
     - 2.757, 2.512, 2.231
     - 1.333, 0.945, 0.582
     - 0.235, 0.729, 1.369
     - 0.000, 0.470, 1.439
   * - Extinction
     - 3.867, 3.404, 3.009
     - 7.434, 6.340, 5.181
     - 5.666, 2.562, 2.227
     - 182.6, 2.189, 1.660
