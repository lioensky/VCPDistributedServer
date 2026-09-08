.. _bpy.ops.mesh.blend_from_shape:

****************
Blend from Shape
****************

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Vertex --> Blend from Shape`

Moves the selected vertices towards their position as stored in a specific
:doc:`Shape Key </animation/shape_keys/introduction>`.
This can be useful for correcting or refining geometry by borrowing deformations
from such a shape key.

Options
=======

Shape
   The shape key to use.

Blend
   How strongly to apply the shape key (similar to the shape key's own *Value*).
   0 means no change, 1 means that the vertices will exactly match the shape key.

Add
   If disabled, each vertex is interpolated between its current position and its
   absolute shape key position.

   If enabled, Blender first calculates the difference between the positions in the
   chosen shape key and its *Relative To* shape key, then adds that difference
   (multiplied by *Blend*) to the vertex.
