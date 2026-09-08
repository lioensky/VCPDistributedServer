.. index:: Compositor Nodes; Vector Blur
.. _bpy.types.CompositorNodeVecBlur:

****************
Vector Blur Node
****************

.. figure:: /images/node-types_CompositorNodeVecBlur.webp
   :align: right
   :alt: Vector Blur Node.

The Vector Blur node is a fast method for simulating :term:`Motion Blur` in compositing.
It uses the vector speed render pass to blur the image pixels in 2D.


Inputs
======

Image
   Image input, to be linked to the "Combined" render pass.
Speed
   Input for the "Vector" render pass.
   See :doc:`Cycles render passes </render/layers/passes>`.
Z
   Z depth, to be linked to the "Depth" render pass.
Samples
   Quality factor.
Shutter
   Duration of the motion blur in seconds, corresponding to the exposure time simulated for each frame.


Outputs
=======

Image
   Motion blurred image output.


Usage
=====

Even with a correct compositing setup with Image, Z and Speed nodes all linked to the appropriate passes,
there may still be artifacts. The 2D render passes does not contain 3D information,
and so the information what is behind a moving object or outside the camera view is lost.

Better results can be achieved by rendering the scene into multiple render layers,
applying vector blur to each render layer, and then compositing the results together.
Typically an animated character would be rendered in a separate render layer than the background set.
Especially if hair or transparency is involved this is important.

For other artifacts it can help to slightly blur the Speed pass or to set a Maximum Speed limit.
This helps to smoothen out the motion, but too much blurring leads to its own problems.


Example
=======

The *speed vector* in this example was created by animating the patterned sphere horizontally and
using a frame at the mid-point of the sequence.

.. list-table::

   * - .. figure:: /images/compositing_types_filter_vector-blur_example-base.jpg
          :width: 300px

          Render result, no post-processing.

     - .. figure:: /images/compositing_types_filter_vector-blur_example-1.jpg
          :width: 300px

          Composite, with Samples set to 32 and Blur set to 1.0.
