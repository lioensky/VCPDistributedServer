.. index:: Compositor Nodes; Bokeh Image
.. _bpy.types.CompositorNodeBokehImage:

****************
Bokeh Image Node
****************

.. figure:: /images/node-types_CompositorNodeBokehImage.webp
   :align: right
   :alt: Bokeh Image Node.

The *Bokeh Image* node generates a special input image for use with
the :doc:`Bokeh Blur </compositing/types/filter/blur/bokeh_blur>` filter node.

The *Bokeh Image* node is designed to create a reference image which simulates optical parameters
such as aperture shape and lens distortions which have important impacts on bokeh in real cameras.


Inputs
======

The first three settings simulate the aperture of the camera.

Flaps
   Sets an integer number of blades for the cameras iris diaphragm.
Angle
   Gives these blades an angular offset relative to the image plane.
Roundness
   Sets the curvature of the blades with (0 to 1) from straight to bringing them to a perfect circle.
Catadioptric Size
   Provides a type of distortion found in mirror lenses and some telescopes.
   This can be useful to produce a visual complex bokeh.
Color Shift
   Introduces chromatic aberration into the blur such as would be caused by a tilt-shift lens.


Outputs
=======

Image
   The generated bokeh image.


Example
=======

In the example below the *Bokeh Image* is used to define the shape of the bokeh for
the :doc:`Bokeh Blur </compositing/types/filter/blur/bokeh_blur>` node.

.. figure:: /images/compositing_types_filter_bokeh-blur_example-1.png
   :width: 640px

   Example of *Bokeh Image* node.
