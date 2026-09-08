.. index:: Compositor Nodes; Plane Track Deform
.. _bpy.types.CompositorNodePlaneTrackDeform:

***********************
Plane Track Deform Node
***********************

.. figure:: /images/node-types_CompositorNodePlaneTrackDeform.webp
   :align: right
   :alt: Plane Track Deform Node.

The Plane Track Deform Node is used replace flat planes in footage by another image,
using plane tracks from motion tracking.


Plane Track
===========

Before using this node, :ref:`plane track <clip-tracking-plane>` for the footage
should be made in the *Movie Clip Editor*.


Inputs
======

Image
   Image to put in place of the plane track, and thus, override that area in the movie clip.

Motion Blur
-----------

Specify whether to use blur caused by motion of the plane track or not.

Samples
   Set the number of samples to take for each frame.
   The higher this number, the smoother the blur effect,
   but the longer the render, as each virtual intermediate frame has to be rendered.

   .. note::

      Samples are taken only from the *next* frame, not the previous one.
      Therefore the blurred object will appear to be slightly ahead of how it would look without motion blur.

Shutter
   Time (in frames) the shutter is open.
   If you are rendering at 24 fps, and the Shutter is set to 0.5,
   the time in between frames is 41.67 ms,
   so the shutter is open for half that, 20.83 ms.


Properties
==========

Movie Clip
   Used to select the movie clip whose plane track to use.
   For controls see :ref:`ui-data-block`.
Object
   Used to select the object to which the plane track is linked.
Track
   Used to select the plane track to use.


Outputs
=======

Image
   The output by perspective wrapping the image to that plane track.
Plane
   Produces a black-and-white mask of the plane track.


Examples
========

Using Image Output
------------------

This can simply be achieved by using the Alpha Over node.

.. figure:: /images/compositing_types_distort_plane-track-deform_example-image-output.png

   Image output.


Using Plane Output
------------------

This can be achieved by mixing the movie clip and the image by using the plane output as the factor.

.. figure:: /images/compositing_types_distort_plane-track-deform_example-plane-output.png

   Plane output.


Using Image Output vs Using Original Image
==========================================

Using Image output scales, moves, and skews the input image according to the track
while using the original image and mixing it with the movie clip using Plane output as factor
will display the part of the image that lies inside that mask. This image shows the difference:

.. figure:: /images/compositing_types_distort_plane-track-deform_output-comparison.png

   Comparison between image output and original image (see Viewer nodes carefully).
