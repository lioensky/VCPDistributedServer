.. index:: Compositor Nodes; Movie Distortion
.. _bpy.types.CompositorNodeMovieDistortion:

*********************
Movie Distortion Node
*********************

.. figure:: /images/node-types_CompositorNodeMovieDistortion.webp
   :align: right
   :alt: Movie Distortion Node.

In the real world, all camera lenses produce some or the other sort of lens distortion.
But, whatever we render has got no distortion. So, this node helps in removing distortion from movies
or adding distortion to render to make our render blend in with the movie clip.

Usually, it is used while motion tracking.


Calculating Distortion
======================

Before using this node, one has to calculate the lens distortion of the clip. This can be done by adjusting
K1, K2 and K3 values in :menuselection:`Movie Clip Editor --> Properties --> Lens`.
For more information on how to edit those values,
`check this out <https://blender.stackexchange.com/questions/15620>`__.


Inputs
======

Image
   Standard color input.
Type
   :Undistort:
      Used to undistort the image received, and is usually used for the raw distorted movie clip.
   :Distort:
      Used to distort the image received, and is usually used for rendered images.


Properties
==========

Movie Clip
   Used to select the movie clip whose distortion is to be used.
   This can be useful if more than one movie clips are present, each having a different distortion setting.
   For controls see :ref:`ui-data-block`.


Outputs
=======

Image
   The image after distorting/undistorting.


Distortion vs Undistortion
==========================

Although, both, distortion of render and undistortion of movie clip are possible, and produce similar results,
there is a difference between these two methods.

There are two kinds of lens distortion possible and, in simple terms, they can be said as:

#. When the movie clip is bulging out.
#. When the movie clip is bulging in.

For the first case, it is recommended to distort the render and leave the movie clip as it is, because,
undistorting the movie clip will require extra pixel information, which is not available to Blender.
Similarly, in the second case, it is recommended to undistort the movie clip and leave the render as it is,
because, distorting the render will require those extra unavailable pixels.
Doing the wrong method in the wrong case can create weird results around the edges, such as in the image shown.

.. figure:: /images/compositing_types_distort_movie-distortion_problems.jpg

   Problems (notice the edges?)
