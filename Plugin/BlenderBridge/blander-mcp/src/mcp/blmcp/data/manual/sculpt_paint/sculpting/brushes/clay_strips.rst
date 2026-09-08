
***********
Clay Strips
***********

.. reference::

   :Mode:      Sculpt Mode
   :Brush:     :menuselection:`Sidebar --> Tool --> Brush Settings --> Advanced --> Brush Type`

Similar to the :doc:`Clay </sculpt_paint/sculpting/brushes/clay>` brush,
but it uses a square tip shape instead of a round one.

Just like the *Clay* brush, it's useful for building and removing volumes
and shapes like real clay, because it flattens details as you add/subtract from the surfaces.

Clay Strips is very commonly used for aggressive building of volumes
and deliberate control over shapes on the surface.
This brush alone can be used for a fast rough pass over the entire sculpt,
with additional smoothing or polishing often required afterwards.
This brush can be very versatile with varying stroke directions, repeated strokes
and pen pressure to achieve various results.

If used together with :ref:`Dyntopo <bpy.ops.sculpt.dynamic_topology_toggle>`
it's easy to continuously build shapes, even in a single stroke.


Brush Settings
==============

General
-------

Normal Radius
   Higher by default. This ensures that the brush does not change directions to sporadically during a stroke.
   More info at :ref:`Normal Radius <bpy.types.Brush.normal_radius_factor>`

Tip Roundness
   Very low by default for a square shape for more deliberate shaping.
   More info at :ref:`Tip Roundness <bpy.types.Brush.tip_roundness>`

.. note::

   More info at :ref:`sculpt-tool-settings-brush-settings-general` brush settings
   and on :ref:`sculpt-tool-settings-brush-settings-advanced` brush settings.
