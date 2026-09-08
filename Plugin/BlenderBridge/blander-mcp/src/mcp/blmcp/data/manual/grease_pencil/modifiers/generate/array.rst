.. index:: Grease Pencil Modifiers; Array Modifier
.. _bpy.types.GreasePencilArrayModifier:

**************
Array Modifier
**************

The *Array* modifier creates an array of copies of the base object, with each copy being offset from
the previous one in any of a number of possible ways.

Useful for creating complex repetitive drawings.

Multiple Array modifiers may be active for an object at the same time
(e.g. to create complex three-dimensional constructs).

.. seealso::

   This documentation refers to the Array Modifier specific to the Grease Pencil object.
   For uses with other object types refer to the general :doc:`/modeling/modifiers/generate/array`.


Options
=======

.. figure:: /images/grease-pencil_modifiers_generate_array_panel.png
   :align: right

   The Array modifier.

Count
   Total number of copies.

Material Override
   Index of the material to use on duplicated strokes (0 use strokes original materials).


Relative Offset
---------------

Factor X, Y, Z
   Adds a translation equal to the object's bounding box size along each axis,
   multiplied by a scaling factor, to the offset. X, Y and Z scaling factors can be specified.


Constant Offset
---------------

Factor X, Y, Z
   Adds a constant translation component to the duplicate object's offset.
   X, Y and Z constant components can be specified.


Object Offset
-------------

Distance X, Y, Z
   Adds a transformation taken from an object (relative to the current object) to the offset.
   It is good practice to use an empty object centered or near to the initial object.


Randomize
---------

Offset X, Y, Z
   Add random offset values to the copies.

Rotation X, Y, Z
   Add random rotation values to the copies.

Scale X, Y, Z
   Add random scale values to the copies.

Uniform Scale
   Use the same random *Seed* for each scale axis in the copies for a uniform scale.

Seed
   :term:`Seed` used by the pseudo-random number generator.

.. note::

   The *Depth Order* used in the Grease Pencil object has an influence on
   the visualization of the strokes when using the Array modifier.
   See :doc:`Depth Order </grease_pencil/properties/strokes>` for more information.


Influence
---------

See :ref:`grease-pencil-modifier-influence-filters`.
