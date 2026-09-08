.. index:: Compositor Nodes; Channel Key
.. _bpy.types.CompositorNodeChannelMatte:

****************
Channel Key Node
****************

.. figure:: /images/node-types_CompositorNodeChannelMatte.webp
   :align: right
   :alt: Channel Key Node.

The *Channel Key* node determines background objects from foreground objects by
the difference in the selected channel's levels.

For example in the YUV :term:`Color Model`,
this node is useful when compositing stock footage of explosions (very bright)
which are normally shot against a solid, dark background.


Inputs
======

Image
   Standard color input.
Minimum
   Determines the lowest values that are considered foreground.
   (Which is supposed to be -- relatively -- high values: from this value to 1.0.)
Maximum
   Determines the highest values that are considered to be background objects.
   (Which is supposed to be -- relatively -- low values: from 0.0 to this value.)

.. tip::

   It is possible to have a separation between the *Minimum* and *Maximum* values to allow
   for a gradient of transparency between foreground and background objects.

Color Space
   This button selects what color model the channels will represent.

   RGB, HSV, YUV, YCbCr

Key Channel
   This button selects the channel, defined by the *Color Space*, to use to determine the matte.

Limit Method
   Method to calculate the difference between levels.

   :Max:
      Limit by the maximum of the other two channels other than the *Key Channel*.
   :Single:
      Limit by the maximum of the selected *Limit Channel*.

Limit Channel
   The channel to use when computing the maximum, the options are defined by the *Color Space*.


Outputs
=======

Image
   Image with an alpha channel adjusted for the keyed selection.
Matte
   A black-and-white alpha mask of the key.
