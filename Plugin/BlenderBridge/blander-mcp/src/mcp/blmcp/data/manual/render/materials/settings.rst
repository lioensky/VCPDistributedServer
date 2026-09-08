
********
Settings
********

.. reference::

   :Panel:     :menuselection:`Material --> Settings`


Renderer Settings
=================

While shading nodes control the appearance, these settings control the quality and algorithms
that each renderer uses to render the material.

- :doc:`EEVEE specific settings </render/eevee/material_settings>`
- :doc:`Cycles specific settings </render/cycles/material_settings>`


Pass Index
==========

.. _bpy.types.Material.pass_index:

Pass Index
   Index number for the *Material Index* :doc:`render pass </render/layers/passes>`.
   This can be used to give a mask to a material and then be read with
   the :doc:`ID Mask Node </compositing/types/mask/id_mask>` in the Compositor.

.. note::

   :doc:`Volume Objects </modeling/volumes/introduction>` are not supported.


.. _render-materials-settings-viewport-display:

Viewport Display
================

These settings control the 3D Viewport display in solid shading.
They provide a faster alternative to full shader nodes,
which may be too heavy or distracting for tasks like modeling, layout or sculpting.

.. _bpy.types.Material.diffuse_color:

Color
   Diffuse or metal surface color.

.. _bpy.types.Material.metallic:

Metallic
   Blends between a non-metallic and metallic material model.
   A value of 1.0 gives a fully specular reflection tinted with the base color,
   without diffuse reflection or transmission.
   At 0.0 the material consists of a diffuse or transmissive base layer, with a specular reflection layer on top.

.. _bpy.types.Material.roughness:

Roughness
   Specifies microfacet roughness of the surface for metal and specular reflection.
