
**********
Snake Hook
**********

.. reference::

   :Mode:      Sculpt Mode
   :Brush:     :menuselection:`Sidebar --> Tool --> Brush Settings --> Advanced --> Brush Type`

Pulls vertices along with the movement of the brush to create long, snake-like forms.
During the stroke, geometry will be dynamically picked up & let go.

When the *Rake* setting is used,
the brush can also be used to rotate geometry via dragging.


Brush Settings
==============

General
-------

.. note::

   More info at :ref:`sculpt-tool-settings-brush-settings-general` brush settings
   and on :ref:`sculpt-tool-settings-brush-settings-advanced` brush settings.


Unique
------

Magnify
   Pulled geometry tends to lose volume along the stroke.
   With *Magnify* value greater than 0.5 this is prevented.
   More info at :ref:`Pinch/Magnify <bpy.types.Brush.crease_pinch_factor>`

.. _bpy.types.Brush.rake_factor:

Rake
   Rotates geometry along the direction of the stroke.

.. _bpy.types.Brush.snake_hook_deform_type:

Deformation
   Deformation type that is used by the brush.

   :Radius Falloff:
      Applies the brush falloff to the tip of the brush.
   :Elastic:
      Modifies the entire mesh using an :term:`Elastic` deformation.
      More info in the :doc:`Elastic Deform </sculpt_paint/sculpting/brushes/elastic_deform>` brush.
