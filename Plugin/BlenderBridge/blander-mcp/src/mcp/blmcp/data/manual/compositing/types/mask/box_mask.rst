.. index:: Compositor Nodes; Box Mask
.. _bpy.types.CompositorNodeBoxMask:

*************
Box Mask Node
*************

.. figure:: /images/node-types_CompositorNodeBoxMask.webp
   :align: right
   :alt: Box Mask Node.

The *Box Mask* node creates an image suitable for use as a simple matte.


Inputs
======

Mask Type
   Operation to use against the input mask.

   :Add:
      This yields the *union* of the input mask and the generated mask:
      Areas covered by the generated mask are set to the specified *Value*.
      Other parts of the input masked are passed through unchanged, or set to black if there is no input mask.
   :Subtract:
      Values of the input mask have the specified *Value* subtracted from them.
   :Multiply:
      This yields the *intersection* of this generated mask and the input mask:
      Values of the input mask are multiplied by the specified *Value* for the area covered by the generated mask.
      All other areas become black.
   :Not:
      Any area covered by both the input mask and the generated mask becomes black.
      Areas covered by the generated mask that are black on the input mask become the specified *Value*.
      Areas uncovered by the generated mask remain unchanged.
Mask
   An optional mask to use as the base for mask operations.
Value
   Intensity of the generated mask.
Position
   Position of the center of the box as a fraction of the total width or height.
   (0.5, 0.5 creates a centered box; 0.0, 0.0 creates a box in the lower left.)
Size
   Width/height of the box as a fraction of the total image width.
Rotation
   Rotation of the box around its center point.


Outputs
=======

Mask
   A generated rectangular mask merged with the input mask.
   The created mask is the size of the current scene render dimensions.

.. tip::

   For soft edges, pass the output mask through a slight :doc:`Blur node </compositing/types/filter/blur/blur>`.
