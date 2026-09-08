
************
Introduction
************

Vertex Painting is a simple way of painting color onto a Grease Pencil object,
by directly manipulating the color of points/vertices, rather than use only the materials base color.

.. figure:: /images/grease-pencil_modes_vertex-paint_introduction_sample.png

   Stroke with original base material color (left) and with vertex painting (right).

When a point is painted, the color of the points is mixing with the base material color according to
the settings of the brush.

.. note::

   A vertex in Grease Pencil is called point. Point and vertex names are equivalent.


Vertex Paint Mode
=================

Vertex Paint Mode is selected from the *Mode* menu in the 3D Viewport header.
Once Vertex Paint Mode is activated, the Toolbar of the 3D Viewport will change to Vertex Paint Mode specific panels.

.. figure:: /images/grease-pencil_modes_vertex-paint_introduction_mode-selector.png

   3D Viewport Mode selector set to Vertex Paint Mode.


Vertex Paint Options
====================

.. _bpy.types.ToolSettings.use_gpencil_vertex_select_mask_stroke:

Selection Mask
   Vertex Paint Mode in Grease Pencil allows you to select points or strokes to restrict the effect
   of the painting tools to only a certain areas of your drawing.

   You can use the selection tools in the Toolbar for a quick selections.

   You can restrict painting only on the selected points or strokes with the Selection mode toggle.
   The three modes can be toggled with :kbd:`1`, :kbd:`2`, or :kbd:`3` respectively.

Multiframe
   Sometimes you may need to modify several frames at the same time with the painting tools.

   You can activate multiframe editing with the Multiframe button next to the modes selector (faded lines icon).
   See :doc:`Multiframe </grease_pencil/multiframe>` for more information.
