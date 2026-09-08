.. index:: Compositor Nodes; Track Position
.. _bpy.types.CompositorNodeTrackPos:

*******************
Track Position Node
*******************

.. figure:: /images/node-types_CompositorNodeTrackPos.webp
   :align: right
   :alt: Track Position Node.

The *Track Position node* is used to return information about a tracking marker to the Compositor.


Inputs
======

Mode
   Which marker position to use for output.

   :Absolute: Outputs an absolute position of a marker.
   :Relative Start: Outputs the positions of a marker relative to the first marker of a track.
   :Relative Frame: Outputs the positions of a marker relative to the markers of the given *Frame*.
   :Absolute Frame: Outputs the absolute positions of a marker at the given *Frame*.


Properties
==========

Movie Clip
   Used to select a Movie Clip data-block to use, for controls see :ref:`ui-data-block`.

Tracking Object
   Camera object to get track information from.

Track
   The name of the track to get track information from.


Outputs
=======

X/Y
   The marker's X and Y location.
Speed
   The velocity of the marker, measured in pixels per frame.
   This could be used to fake effects like motion blur by connecting it to the Vector Blur Node.
