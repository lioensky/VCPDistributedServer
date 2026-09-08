.. index:: Editors; Texture Node Editor
.. index:: Nodes; Texture Nodes

************
Introduction
************

The Texture Node Editor allows creating custom textures by combining colors,
procedural patterns, and images in various ways. This is a step up from the
:doc:`built-in textures </render/materials/legacy_textures/introduction>`,
where you can select a type from a list and not much more.

.. note::

   Textures -- both built-in ones and node-based ones -- are a legacy feature.
   For their original main purpose, which was of course texturing objects,
   they have been replaced by :doc:`Materials </render/materials/introduction>`
   which are set up in the :doc:`/editors/shader_editor`.

   Today, the use of Textures is limited to:

   - :doc:`Brushes </sculpt_paint/brush/texture>`.
   - The :doc:`/modeling/modifiers/deform/displace`.
   - Influencing size, density etc. of :doc:`particle systems </physics/particles/texture_influence>`.
   - Influencing emission locations of :ref:`fire/smoke simulations <bpy.types.FluidFlowSettings.use_texture>`.

   In addition, the Displace modifier and fire/smoke simulations don't support
   node-based textures, instead only working with the built-in ones.

.. figure:: /images/editors_texture-node_introduction_types-combined.png
   :width: 600px

   Combined textures based on nodes.


Using Texture Nodes
===================

The default Blender layout has no workspace containing the Texture Node Editor.
You need to manually open it in an :doc:`area </interface/window_system/areas>` of choice.

Once the editor is open, you first need to set the empty *Texture Type* selector to *Brush*,
after which you can use the :doc:`/interface/controls/templates/data_block`
to start creating textures. Note that you need to enable *Use Nodes* in the header
before you can add nodes.


Header
======

See :doc:`Nodes </interface/controls/nodes/index>` for the header items common to
all node editors.

Texture Type
   World
      Deprecated -- the scene's :doc:`/render/lights/world` is now defined using
      a Material rather than a Texture.
   Brush
      Show brush Textures in the data-block menu. Because the other two types are deprecated,
      this effectively shows all Textures.
   Line Style
      Deprecated -- :doc:`Line Styles </render/freestyle/view_layer/line_style/index>`
      for the Freestyle renderer are now defined using Materials rather than Textures.
