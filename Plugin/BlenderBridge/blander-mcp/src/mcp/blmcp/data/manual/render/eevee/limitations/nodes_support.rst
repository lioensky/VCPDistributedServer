***************
Supported Nodes
***************

Most nodes are taken from Cycles. However, some features are missing and
may (or may not) be implemented in EEVEE in the future.

.. seealso::

   :doc:`Shader Nodes </render/shader_nodes/index>`.


EEVEE only Nodes
================

These nodes are only available if EEVEE is the active render engine. These nodes will not work in Cycles.


Shader to RGB
-------------

EEVEE supports the conversion of BSDF outputs into color inputs to make a wide variety of custom shading.
This is supported using the :doc:`Shader to RGB </render/shader_nodes/color/shader_to_rgb>` node.
This node evaluates the lighting of the BSDFs connected to it just like a *Blended* material and inherits
its limitation.


Specular BSDF
-------------

This :doc:`node </render/shader_nodes/shader/specular_bsdf>` implements the specular workflow
found in other render engines.


Other Nodes Support
===================

If something is not listed here, it is supported.


Shader Nodes
------------

In the general case, shader nodes should behave more or less like in Cycles.
So be sure to check out the Cycles section of this manual for that.

.. seealso::

   :doc:`Materials </render/shader_nodes/shader/index>`.

Although most BSDFs are supported, many of them are approximations and are not feature complete.

Diffuse BSDF
   Roughness is not supported. Only Lambertian diffusion is supported.

Glass / Refraction BSDF
   Only supports GGX and Multiscatter GGX distribution.
   See :ref:`Raytracing limitations <eevee-limitations-raytracing>`.

Glossy BSDF
   Only supports GGX and Multiscatter GGX distributions.

Subsurface Scattering
   Random Walk sampling, IOR and Anisotropic are not supported.

Transparent BSDF
   Colored and additive transparency are only compatible with blended modes.

Translucent BSDF
   Does not diffuse the light inside the object. It only lights the object with reversed normals.

Principled BSDF
   Cumulative limitations from Diffuse BSDF, Glossy BSDF, Refraction BSDF and Subsurface Scattering.
   Anisotropy is not supported. The Sheen layer is a crude approximation.

Volume Absorption
   See :ref:`Volume Limitation <eevee-limitations-volumetrics>`.

Volume Scatter
   The anisotropy parameter will be mixed and averaged for all overlapping volumetric objects,
   which is not physically correct and differs from Cycles.
   Also see :ref:`Volume Limitation <eevee-limitations-volumetrics>`.

Principled Volume
   Same as Volume Scatter. See :ref:`Volume Limitation <eevee-limitations-volumetrics>`.

Holdout
   Partially supported, using dithered mode may give incorrect results.

Anisotropic BSDF
   Not supported.

Toon BSDF
   Not supported.

Hair BSDF
   Not supported.

Sheen BSDF
   Not supported.

Principled Hair BSDF
   Not supported.


Input Nodes
-----------

Ambient Occlusion
   The *Only Local* option is not supported.

Geometry
   Pointiness is not supported.

Random per Island
   Random per Island is not supported.

Attribute
   Defaults to active UV layer. Only "density", "color", "flame" and "temperature" built-in Geometry attributes
   are supported. UVs and Color Attributes are supported.
   Only up to 8 Object or Instancer attributes per material (both types share the same limit), and 512 View Layer
   attributes per scene are supported.

Bevel
   Not supported.

Curves Info
   The Random output uses a different :abbr:`RNG (Random Number Generator)` algorithm.
   Range and statistical distribution of the values should be the same but the values will be different.

Light Path
   EEVEE has no real concept of rays. But in order to ease the workflow between Cycles and EEVEE
   some of the outputs are only supported in particular cases.
   This node makes it possible to tweak indirect lighting in the shader.

   - *Is Camera*: Supported.
   - *Is Shadow*: Supported.
   - *Is Diffuse*: Set to 1.0 when baking light probe volume. Otherwise is set to 0.0.
   - *Is Glossy*: Set to 1.0 when baking light probe sphere or plane. Otherwise is set to 0.0.
   - *Is Singular*: Not supported. Same as Is Glossy.
   - *Is Reflection*: Not supported. Same as Is Glossy.
   - *Is Transmission*: Not supported. Same as Is Glossy.
   - *Ray Length*: Not supported. Defaults to 1.0.
   - *Ray Depth*: Not supported. Defaults to 0.0.
   - *Diffuse Depth*: Partially supported. Set to 1.0 when baking light probe volume. Otherwise is set to 0.0.
   - *Glossy Depth*: Partially supported. Set to 1.0 when baking light probe sphere or plane. Otherwise is set to 0.0.
   - *Transparent Depth*: Not supported. Defaults to 0.
   - *Transmission Depth*: Not supported. Same as Glossy Depth.

   .. note::

      *Is Glossy* does not work with Screen Space Reflections/Refractions
      but does work with reflection planes (whether used with SSR or not).

Particle Info
   Not supported.

Texture Coordinate
   *From Instancer* is not supported.

UV Map
   *From Instancer* is not supported.

Wireframe
   Pixel size option does not give exactly the same output as Cycles. The width can be a bit different.


Texture Nodes
-------------

Most texture nodes are supported except for the exceptions listed below:

:abbr:`IES (Illuminating Engineering Society)` Texture
   Not supported.

Image Texture
   Smart Interpolation always uses Cubic interpolation.
   Artifact present using Tube or Sphere projection with linear interpolation.
   This is due to hardware mip-mapping and Anisotropic filtering.
   This kind of artifact will be also visible if the texture coordinates provided are not continuous.
   Using Box projection with *Extend type* set to Clip or Extend is not supported.
   Instead, it will always use Repeat.

Point Density
   Not supported.

Sky Texture
   In Nishita mode, the *Sun Disc* property is not supported.


Other Nodes
-----------

Light Falloff
   Not supported.
