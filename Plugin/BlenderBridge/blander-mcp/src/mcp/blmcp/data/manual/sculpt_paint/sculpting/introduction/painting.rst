
********
Painting
********

Sculpt Mode also allows painting your geometry via
:ref:`modeling-meshes-properties-object_data-color-attributes` such as Vertex Colors. This ensures that the most
common actions related to the sculpting workflow are contained in the same mode, to avoid unnecessary mode switching.

.. figure:: /images/sculpt-paint_sculpt_paint_example.png

Other sculpt mode features such as face sets, masking and filters can also be used with painting tools.

The painting functionality in Sculpt Mode is limited to a
:doc:`Paint </sculpt_paint/sculpting/brushes/paint>`
and :doc:`Smear </sculpt_paint/sculpting/brushes/smear>` brush,
as well as a :doc:`Color Filter </sculpt_paint/sculpting/tools/color_filter>`
and :doc:`Mask by Color </sculpt_paint/sculpting/tools/mask_by_color>` tool.

Just like any other brush, :kbd:`Shift` can be used to smooth.
In the case of painting brushes it will blur the colors within the brush radius instead.

.. note::

   Once any painting tool is executed, the :ref:`viewport color shading <viewport_shading_solid_color>` is switched
   to "Attribute".  This ensures that color attributes are shown on all objects once painting is needed.
