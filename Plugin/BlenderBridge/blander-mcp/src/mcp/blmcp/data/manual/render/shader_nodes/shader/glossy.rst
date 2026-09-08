.. _bpy.types.ShaderNodeBsdfAnisotropic:

***********
Glossy BSDF
***********

.. figure:: /images/node-types_ShaderNodeBsdfAnisotropic.webp
   :align: right
   :alt: Glossy BSDF node.

The *Glossy* :abbr:`BSDF (Bidirectional Scattering Distribution Function)`
node is used to add reflection with microfacet distribution, used for materials such as metal or mirrors.


Inputs
======

Color
   Color of the surface, or physically speaking, the probability that light is reflected for each wavelength.
Roughness
   Sharpness of the reflection; perfectly sharp at 0.0 and smoother with higher values.
Anisotropy :guilabel:`Cycles Only`
   Controls the amount the reflection stretches the reflection along the surface of the material.
   A value of 0.0 results in no anisotropic reflections.
   Higher values give elongated highlights orthogonal to the tangent direction;
   negative values give highlights shaped along the tangent direction.

   This is a phenomenon know as "Anisotropic Reflections" which is often seen in metallic materials.
Rotation
   Rotation of the anisotropic tangent direction.
   Value 0.0 equals 0° rotation, 0.25 equals 90° and 1.0 equals 360° = 0°.
   This can be used to texture the tangent direction.

   .. list-table::

      * - .. figure:: /images/render_shader-nodes_shader_anisotropic_rot0.jpg

             Anisotropic rotation on 0.

        - .. figure:: /images/render_shader-nodes_shader_anisotropic_rot025.jpg

             Anisotropic rotation on 0.25 (90°).

Normal
   Normal used for shading; if nothing is connected the default shading normal is used.
Tangent
   Tangent used for shading; if nothing is connected the default shading tangent is used.


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

   * - .. figure:: /images/render_shader-nodes_shader_glossy_example.jpg

          Sharp Glossy example.

     - .. figure:: /images/render_shader-nodes_shader_glossy_behavior-sharp.svg
          :width: 308px

          Sharp Glossy behavior.

   * - .. figure:: /images/render_shader-nodes_shader_glossy_rough.jpg

          Rough Glossy example.

     - .. figure:: /images/render_shader-nodes_shader_glossy_behavior.svg
          :width: 308px

          Rough Glossy behavior.

.. figure:: /images/render_shader-nodes_shader_anisotropic_example.jpg

   Anisotropic shading with 0° rotation, 90° rotation and textured rotation of the tangent direction.
   `Example blend-file <https://archive.blender.org/wiki/2015/uploads/b/b7/Blender2.65_cycles_anisotropic.blend>`__.
