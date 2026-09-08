.. index:: Compositor Nodes; Ellipse Mask
.. _bpy.types.CompositorNodeEllipseMask:

*****************
Ellipse Mask Node
*****************

.. figure:: /images/node-types_CompositorNodeEllipseMask.webp
   :align: right
   :alt: Ellipse Mask Node.

The *Ellipse Mask* node creates an image suitable for use as a simple matte or vignette mask.


Inputs
======

Operation
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
   Position of the center of the ellipse as a fraction of the total width or height.
   (0.5, 0.5 creates a centered ellipse; 0.0, 0.0 creates an ellipse with its center in the lower left.)
Size
   Width/Height of the ellipse as a fraction of the total image *width*, not height.
   Equal *Width* and *Height* values with produce a circle.
Rotation
   Rotation of the ellipse around its center point.


Outputs
=======

Mask
   A generated elliptical mask merged with the input mask.
   The created mask is the size of the current scene render dimensions.

.. tip::

   For soft edges, pass the output mask through a slight :doc:`Blur node </compositing/types/filter/blur/blur>`.
   For a vignette, pass the output of this through a heavy blur.


Usage
=====

The Ellipse Mask node supports an interactive gizmo in the node editor.
To enable it, make sure :ref:`Active Node <bpy.types.SpaceNodeEditor.show_gizmo_active_node>`  gizmo is enabled,
and select the Ellipse Mask node in the Compositor.

The gizmo allows direct manipulation of the mask shape:

- Drag edges to adjust the width or height individually.
- Drag corners to adjust width and height simultaneously.
- Drag the center cross (X) to move the mask's position.
- Drag the center dot to rotate the mask.
- Hold :kbd:`Shift` while dragging edges or corners to preserve the current aspect ratio.
