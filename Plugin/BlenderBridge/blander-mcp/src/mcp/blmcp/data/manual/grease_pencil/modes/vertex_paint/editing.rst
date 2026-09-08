
***************************
Editing Vertex Paint Colors
***************************

.. _bpy.ops.grease_pencil.vertex_color_set:

Set Color Attribute
===================

.. reference::

   :Mode:      Vertex Paint Mode
   :Menu:      :menuselection:`Paint --> Set Color Attribute`

Sets the :ref:`active color <grease-pencil-vertex-paint-brush-color>` to all selected vertices.


.. _bpy.ops.grease_pencil.stroke_reset_vertex_color:

Reset Vertex Color
==================

.. reference::

   :Mode:      Vertex Paint Mode
   :Menu:      :menuselection:`Paint --> Reset Vertex Color`

Removes the Color Attribute information of the active strokes,
if no strokes are selected, all strokes are reset.


.. _bpy.ops.grease_pencil.vertex_color_invert:

Invert
======

.. reference::

   :Mode:      Vertex Paint Mode
   :Menu:      :menuselection:`Paint --> Invert`

Invert RGB values.


.. _bpy.ops.grease_pencil.vertex_color_levels:

Levels
======

.. reference::

   :Mode:      Vertex Paint Mode
   :Menu:      :menuselection:`Paint --> Levels`

Adjust the levels of Color Attributes.


.. _bpy.ops.grease_pencil.vertex_color_hsv:

Hue/Saturation/Value
====================

.. reference::

   :Mode:      Vertex Paint Mode
   :Menu:      :menuselection:`Paint --> Hue/Saturation/Value`

Adjust the color's HSV values.


.. _bpy.ops.grease_pencil.vertex_color_brightness_contrast:

Brightness/Contrast
===================

.. reference::

   :Mode:      Vertex Paint Mode
   :Menu:      :menuselection:`Paint --> Brightness/Contrast`

Adjust the color's brightness/contrast.


Sample Color
============

.. reference::

   :Mode:      Vertex Paint Mode
   :Menu:      :menuselection:`Paint --> Sample Color`
   :Shortcut:  :kbd:`Shift-X`

   .. :Shortcut:  :kbd:`Shift-X`, :kbd:`Shift-Ctrl-X`

Samples a color from the viewport and assigns it to the active
:doc:`Paint </sculpt_paint/sculpting/brushes/paint>` brush.

This allows quickly matching the brush color to existing painted details
directly on the model.

- Press :kbd:`Shift-X` to sample a color at the mouse cursor position.

.. - Press :kbd:`Shift-Ctrl-X` to sample the **merged viewport color**,
..   including lighting, shading, and all visible layers.

The sampled color becomes the primary color of the active Paint brush.
