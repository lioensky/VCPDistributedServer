.. _bpy.types.ShaderNodeTexGradient:
.. --- copy below this line ---

*********************
Gradient Texture Node
*********************

.. figure:: /images/node-types_ShaderNodeTexGradient.webp
   :align: right
   :alt: Gradient Texture Node.

The *Gradient Texture* node generates interpolated color and intensity values based on the input vector.


Inputs
======

Vector
   Texture coordinate to sample texture at;
   defaults to Generated texture coordinates if the socket is left unconnected.


Properties
==========

Gradient Type
   Controls the type of gradient generated.

   :Linear: Directly outputs the input X coordinate.
   :Quadratic: Interpolates the input X coordinate quadratically.
   :Easing: Uses a combination of quadratic and linear interpolation
      to generate a smooth gradient from the input X coordinate.
   :Diagonal: Averages the input X and Y coordinates.
   :Spherical: Creates an inverse gradient using the length of the input vector; the maximum value is at (0, 0, 0).
   :Quadratic Sphere: The same as Spherical, except interpolated quadratically.
   :Radial: Outputs a value based on the angle of the input around the Z axis.


Outputs
=======

Color
   Texture color output.
Factor
   Texture intensity output.


Examples
========

.. figure:: /images/render_shader-nodes_textures_gradient_example.jpg
   :width: 200px

   Gradient texture using object coordinates.
