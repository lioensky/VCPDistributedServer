.. _bpy.types.MaterialGPencilStyle:

###########################
  Grease Pencil Materials
###########################

Materials control the appearance of the Grease Pencil object.
They define the base color and texture of the strokes and filled areas.

There is always only one active material in the list (the selected one).
When you draw, the new strokes use the active material.

You can override the base material color using the tools in
:doc:`Vertex Mode </grease_pencil/modes/vertex_paint/introduction>`
or the Draw and Tint tool in Draw Mode.

The material always remains linked to the strokes, this means that any change in a material will change
the look of already drawn strokes.

.. figure:: /images/grease-pencil_materials_introduction_sample.png

   Same stroke linked to different materials.


Material Shader
===============

Grease Pencil materials use a special :doc:`shader </grease_pencil/materials/properties>`
that define the appearance of the surface of the stroke and fill.

Stroke and fill components has it own section panel and
they can be enabled with a checkbox on the panel header.

*Stroke* only has effect on the lines and *Fill* only on the areas
determined by closed lines (by connecting the lines start and end points).

.. note::

   The shader is not a BSDF capable shader and can only be setting up
   on the Material Properties panel (it is not a shader node).


Setting Up Materials
====================

.. reference::

   :Mode:      Drawing Mode
   :Panel:     :menuselection:`Material --> Material Slots`
   :Shortcut:  :kbd:`U`

Grease Pencil materials can be created in the :doc:`Material properties </editors/properties_editor>`
as any other materials in Blender.
See :doc:`Material assignment </render/materials/assignment>` for more information.

The 3D Viewport can be set to Material Preview or Rendered shading,
to interactively preview how the material looks in the scene.

Grease Pencil materials are data-blocks that can be :doc:`assigned </render/materials/assignment>`
to one or more objects, and different materials can be assigned to different strokes.

In Grease Pencil the :doc:`brush </grease_pencil/modes/draw/brushes/index>`
settings together with the material used will define the look and feel of the final strokes.

:ref:`Materials slots <gp-material-slots>` also have some extra controls
that help to work with materials while drawing or editing lines.


:doc:`Properties <properties>`
==============================

.. toctree::
   :maxdepth: 2
   :hidden:

   Properties <properties.rst>

:ref:`Material Slots <gp-material-slots>`
-----------------------------------------

:ref:`Surface <gp-material-surface>`
------------------------------------

:ref:`Settings <gp-material-settings>`
--------------------------------------
