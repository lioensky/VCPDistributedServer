.. index:: Grease Pencil Modifiers; Outline Modifier
.. _bpy.types.GreasePencilOutlineModifier:

****************
Outline Modifier
****************

The *Outline* modifier convert strokes to outline tracing all strokes perimeter with new strokes.


Options
=======

.. figure:: /images/grease-pencil_modifiers_generate_outline_panel.png
   :align: right

   The Outline modifier.

Thickness
   The thickness of the generated strokes outline.

   Keep shape
      The perimeter strokes are maintaining inside the original stroke perimeter trying to keep the original shape.

Subdivisions
   controls the number of subdivision of the generated strokes outline.

Sample Length
   Controls the accuracy of the perimeter conversion.

Outline Material
   Defines the material to use on the generated strokes outline.

Target Object
   Controls the origin of the cyclic strokes generated.


Influence Filters
-----------------

See :ref:`grease-pencil-modifier-influence-filters`.
