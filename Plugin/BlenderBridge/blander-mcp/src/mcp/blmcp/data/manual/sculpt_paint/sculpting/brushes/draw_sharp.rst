
**********
Draw Sharp
**********

.. reference::

   :Mode:      Sculpt Mode
   :Brush:     :menuselection:`Sidebar --> Tool --> Brush Settings --> Advanced --> Brush Type`

Similar to the :doc:`Draw </sculpt_paint/sculpting/brushes/draw>` brush,
but it always deforms the mesh from the original coordinates
and uses the *Sharper* Falloff by default.

Draw Sharp is useful on high density meshes for creating cloth wrinkles, stylized hair or hard surface edges.
To further sharpen or polish sharp edges in the case that the mesh density is not enough,
it's recommended to use the :doc:`Pinch </sculpt_paint/sculpting/brushes/pinch>`,
:doc:`Crease </sculpt_paint/sculpting/brushes/crease>` or
:doc:`Multiplane Scrape </sculpt_paint/sculpting/brushes/multiplane_scrape>` brushes.

A limitation is that the brush does not remesh the sculpted surfaces
with :ref:`Dyntopo <bpy.ops.sculpt.dynamic_topology_toggle>` enabled.
Because of that, a better brush to use with Dyntopo can be :doc:`Crease </sculpt_paint/sculpting/brushes/crease>`.


Brush Settings
==============

General
-------

Direction
   On *Subtract* by default to carve in creases. More info at :ref:`Direction <bpy.types.Brush.direction>`

.. note::

   More info at :ref:`sculpt-tool-settings-brush-settings-general` brush settings
   and on :ref:`sculpt-tool-settings-brush-settings-advanced` brush settings.
