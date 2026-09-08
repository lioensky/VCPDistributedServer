.. index:: Compositor Nodes; Image
.. _bpy.types.CompositorNodeImage:

**********
Image Node
**********

.. figure:: /images/node-types_CompositorNodeImage.webp
   :align: right
   :alt: Image Node.

The *Image* node injects any image :doc:`format that is supported by Blender </files/media/image_formats>`.


Inputs
======

This node has no input sockets.


Properties
==========

Image
   Selection of different types of media. For controls see :ref:`ui-data-block`.
   For the options see :doc:`/editors/image/image_settings`.

Source
   Type of image (Single Image, Movie...). See :doc:`/editors/image/image_settings`.

Frames
   How many frames of the Movie-type image (video) to play. Past this point, the video will be paused
   (unless *Cyclic* is enabled).

   If you want to play the whole video, you can click
   :ref:`Match Movie Length <bpy.ops.image.match_movie_length>` in the Image Editor's Sidebar,
   then copy the *Frames* from there to the node.

Start Frame
   Scene frame at which the video should start playing.

Offset
   Number of frames to offset the video to an earlier point in time.
   (Put differently: how many frames at the start of the video to skip.)

   .. hint::

      Blender plays video textures at the scene frame rate, not their original frame rate,
      meaning they'll be faster or slower than intended if these frame rates don't match up.
      You can put a :doc:`Driver </animation/drivers/introduction>` on the Offset to work
      around this. Simply type the following into the field, replacing *StartFrame*,
      *VideoFrameRate* and *SceneFrameRate* by their respective numbers:

      #(frame - StartFrame) * (VideoFrameRate - SceneFrameRate) / SceneFrameRate

Cyclic
   Start over after the last frame to create a continuous loop.

Auto-Refresh
   Update the video texture in the 3D Viewport when moving through the timeline.

Color Space
   The :term:`Color Space` the image file was saved in.
   See :ref:`Image Settings <bpy.types.ColorManagedInputColorspaceSettings.name>` for details.

Alpha
   How the image uses its :term:`Alpha Channel`.
   See :ref:`Image Settings <bpy.types.Image.alpha_mode>` for details.


Outputs
=======

The first two sockets are the minimum.

Image
   Standard color output.
Alpha
   Separate Alpha value.

.. note:: Multi-Layer Format

   When a multi-layer file format, like ``EXR``, is loaded,
   each layer is made available as a socket.
