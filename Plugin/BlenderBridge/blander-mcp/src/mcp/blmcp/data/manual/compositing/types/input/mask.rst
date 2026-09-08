.. index:: Compositor Nodes; Mask
.. _bpy.types.CompositorNodeMask:

*********
Mask Node
*********

.. figure:: /images/node-types_CompositorNodeMask.webp
   :align: right
   :alt: Mask Node.

The Mask node can be used to select a :doc:`Mask data-block </movie_clip/masking/index>`.
This node can be used with other nodes, for example to Invert, Multiply or Mix, or used as a factor input.


Inputs
======

Feather
   Use or ignore feather points defined for splines see :ref:`Mask Feathers <mask-feather>` for more details.
Size Source
   Where to get the mask size from for aspect/size information.

   :Scene Size:
      Will give an image the size of the render resolution for the scene,
      scaling along when rendering with different resolutions.
   :Fixed:
      Gives a fixed size in pixels.
   :Fixed/Scene:
      Gives a size in pixels that still scales along when changing the render resolution percentage in the scene.


Motion Blur
-----------

For animated masks, creating a motion blurred mask from the surrounding frames.

Samples
   Number of motion blur samples.
   Higher values result in smoother and more accurate blur, but increase processing time.
Shutter
   Duration of the motion blur in seconds, corresponding to the exposure time simulated for each frame.


Properties
==========

Masks
   The selectable mask data-block. If the label is left blank, the mask name will be set.


Outputs
=======

Mask
   The black-and-white output of the mask.


Example
=======

.. figure:: /images/compositing_types_input_mask_example.png

   Example of the Mask node.

In the example above, the *Mask* node is used to isolate the object from the background
to preserve it from being corrected.
