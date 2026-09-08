.. index:: Compositor Nodes; Sensor Noise

*****************
Sensor Noise Node
*****************

.. figure:: /images/node-types_CompositorNodeSensorNoise.webp
   :align: right
   :alt: Sensor Noise Node.

The *Sensor Noise* node simulates the random noise patterns produced by digital camera sensors.
This can be used to match real footage, add realism to rendered images, or stylistically mimic
the imperfections of digital imaging systems.


Inputs
======

Image
   Standard color input image.

Luminance Noise
   Controls the amount of brightness variation (value noise) applied to the image.
   Higher values create stronger light and dark fluctuations, similar to high ISO noise.

Chroma Noise
   Controls the amount of color noise added to the image.
   Higher values introduce visible color speckling, typical of low-light digital images.

Animated
   When enabled, generates a new noise pattern on each frame, mimicking real sensor noise.
   When disabled, the noise remains static across frames.


Outputs
=======

Image
   The input image with sensor noise applied.
