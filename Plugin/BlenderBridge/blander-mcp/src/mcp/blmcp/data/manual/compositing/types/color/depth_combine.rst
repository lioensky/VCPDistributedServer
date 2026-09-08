.. index:: Compositor Nodes; Depth Combine
.. _bpy.types.CompositorNodeZcombine:

******************
Depth Combine Node
******************

.. figure:: /images/node-types_CompositorNodeZcombine.webp
   :align: right
   :alt: Depth Combine Node.

The Depth Combine node combines two images based on their depth maps.
It overlays the images using the provided depth values to
detect which parts of one image are in front of the other.


Inputs
======

A
   The background image.
Depth A
   Depth pass of the background image.
B
   The foreground image.
Depth B
   Depth pass of the foreground image.
Use Alpha
   The chosen Image pixel alpha channel is also carried over.
   If a pixel is partially or totally transparent,
   the result of the Depth Combine will also be partially transparent;
   in which case the background image will show through the foreground (chosen) pixel.
Anti-Alias
   Applies :term:`Anti-Aliasing` to avoid artifacts at sharp edges or areas with a high contrast.


Outputs
=======

Result
   If both depth values are equal, it will use the foreground image.
   Whichever depth value is less decides which image pixel is used.
   See :term:`Z-buffer`.
Depth
   The combined depth, which allows to thread multiple Depth Combine nodes together.


Examples
========

.. figure:: /images/compositing_types_color_depth-combine_example-1.png
   :width: 700px

   Choosing closest pixels.

In the example above, the render output from two scenes are mixed using the Depth Combine node,
one from a sphere of size 1.3, and the other a cube of size 1.0.
The sphere and square are located at the same place. The cube is tipped forward,
so the corner in the center is closer to the camera than the sphere surface;
so Depth Combine chooses to use the cube's pixels. But the sphere is slightly larger
(a size of 1.3 versus 1.0), so it does not fit totally inside the cube. At some point,
as the cube's sides recede back away from the camera, the sphere's sides are closer.
When this happens, Depth Combine uses the sphere's pixels to form the resulting picture.

This node can be used to combine a foreground with a background matte painting.
Walt Disney pioneered the use of multi-plane mattes, where three or four partial mattes were
painted on glass and placed on the left and right at different depth positions; minimal camera
moves to the right created the illusion of depth as Bambi moved through the forest.

.. note:: Valid Input

   The depth input sockets do not accept fixed values; they must get a vector set (see Map Value node).
   Image input sockets will not accept a color since they do not have UV coordinates.

.. figure:: /images/compositing_types_color_depth-combine_example-2.png
   :width: 700px

   Mix and match images.

The Depth Combine can be used to merge two images as well.
Using the depth values from the sphere and cube scenes above, but inputting different images,
yields the example to the right.

.. figure:: /images/compositing_types_color_depth-combine_example-3.png
   :width: 700px

   Depth Combine in action.

In this node setup a render scene is mixed with a flat image. In the side view of the scene,
the orange cube is 10 units away from the camera, and the blue ball is at a depth of 20.
The 3D cursor is about 15 units away from the camera.
The image depth is 15, thus inserting it in between the cube and the ball.
The resulting image appears to have the cube on the green image.

.. note:: Invisible Man Effect

   If a foreground image with a higher Alpha than the background,
   is then mixed in the Depth Combine with a slightly magnified background,
   the outline of the transparent area will distort the background,
   enough to make it look like seeing a part of the background through
   an invisible yet Fresnel-lens object.
