
*****
Layer
*****

.. reference::

   :Mode:      Sculpt Mode
   :Brush:     :menuselection:`Sidebar --> Tool --> Brush Settings --> Advanced --> Brush Type`

This brush is similar to :doc:`Draw </sculpt_paint/sculpting/brushes/clay>`,
except that the height capped.
This creates the appearance of a flat layer.

It is recommended to use the :ref:`Persistent <bpy.types.Brush.use_persistent>` setting
and regularly :ref:`Set Persistent Base <bpy.ops.sculpt.set_persistent_base>`,
so that multiple strokes to not add on top of each other.


Brush Settings
==============

General
-------

Hardness
   Higher by default to ensure the profile of layers is more noticeable.
   More info at :ref:`Hardness <bpy.types.Brush.hardness>`

.. note::

   More info at :ref:`sculpt-tool-settings-brush-settings-general` brush settings
   and on :ref:`sculpt-tool-settings-brush-settings-advanced` brush settings.


Unique
------

.. _bpy.types.Brush.height:

Height
   The fixed height of each stroke. This is measured using the :ref:`scene scale <bpy.types.UnitSettings.system>`,
   so it is consistent no matter the amount of zoom or object size.

.. _bpy.types.Brush.use_persistent:

Persistent
   This will ensure that multiple strokes use the same height, as if sculpting a single layer.

.. _bpy.ops.sculpt.set_persistent_base:

Set Persistent Base
   This button resets a new base so that you can sculpt new layer.
