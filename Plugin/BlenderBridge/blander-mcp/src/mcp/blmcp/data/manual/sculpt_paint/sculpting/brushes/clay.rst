
****
Clay
****

.. reference::

   :Mode:      Sculpt Mode
   :Brush:     :menuselection:`Sidebar --> Tool --> Brush Settings --> Advanced --> Brush Type`

Similar to the :doc:`Draw </sculpt_paint/sculpting/brushes/draw>` brush,
but includes settings to adjust the :ref:`sculpt plane <bpy.types.Brush.sculpt_plane>`
on which the brush acts. That's because it behaves like a combination of the
:doc:`Plane </sculpt_paint/sculpting/brushes/plane>` and *Draw* brushes.

This brush is useful for building and removing volumes and shapes like real clay,
because it flattens details as you add/subtract from the surfaces.

If used together with :ref:`Dyntopo <bpy.ops.sculpt.dynamic_topology_toggle>`
it's easy to continuously build shapes, even in a single stroke.


Brush Settings
==============

General
-------

Hardness
   Slightly higher by default. This makes the profile of the brush more noticeable.
   More info at :ref:`Hardness <bpy.types.Brush.hardness>`

Auto-Smooth
   Enabled by default for a consistent smoothing effect.
   With lower brush strength (for example with lower pen pressure) the smoothing effect will be more noticeable
   and can be used to create and then blend/polish shapes in a single stroke.
   Enable Pressure to modulate the use of auto-smooth even more with pen inputs.
   More info at :ref:`Auto-Smooth <bpy.types.Brush.auto_smooth_factor>`

.. note::

   More info at :ref:`sculpt-tool-settings-brush-settings-general` brush settings
   and on :ref:`sculpt-tool-settings-brush-settings-advanced` brush settings.
