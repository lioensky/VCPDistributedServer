.. index:: Grease Pencil Modifiers; Offset Modifier
.. _bpy.types.GreasePencilOffsetModifier:

***************
Offset Modifier
***************

The *Offset* Modifier changes the strokes location, rotation or scale
starting from the object origin.


Options
=======

.. figure:: /images/grease-pencil_modifiers_deform_offset_panel.png
   :align: right

   Offset Modifier.


General
-------

Location X, Y, Z
   Sets strokes location offset from its object origin.

Rotation X, Y, Z
   Sets strokes rotation.

Scale X, Y, Z
   Sets strokes scale.


Advanced
--------

Mode
   :Random: Add random values to the individual strokes offset.
   :Layer: Offset by layers.
   :Stroke: Offset by strokes (based on the stroke draw order).
   :Material: Offset by Materials.

Offset X, Y, Z
   Sets individual element location offset.

Rotation X, Y, Z
   Sets individual element rotation.

Scale X, Y, Z
   Sets individual element scale.

Uniform Scale (Random mode)
   Use the same random *Seed* for each scale axis in the strokes for a uniform scale.

Seed (Random mode)
   :term:`Seed` used by the pseudo-random number generator.

Layer/Stroke/Material Step (For Layer, Stroke and Material mode)
   The number of elements to be grouped and offset together.

Offset (For Layer, Stroke and Material mode)
   Offset the element starting point.


Influence
---------

See :ref:`grease-pencil-modifier-influence-filters`.
