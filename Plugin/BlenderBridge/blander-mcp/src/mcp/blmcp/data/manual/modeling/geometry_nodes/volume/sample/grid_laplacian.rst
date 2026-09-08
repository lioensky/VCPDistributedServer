.. index:: Geometry Nodes; Grid Laplacian
.. _bpy.types.GeometryNodeGridLaplacian:

*******************
Grid Laplacian Node
*******************

.. figure:: /images/node-types_GeometryNodeGridLaplacian.webp
   :align: right
   :alt: Grid Laplacian node.

The *Grid Laplacian* node computes the Laplacian of a scalar voxel grid.
The Laplacian measures how a value at each voxel differs from the average
of its neighbors—essentially, how much the field "curves" or deviates locally.

Mathematically, the Laplacian is defined as the divergence of the gradient
of a scalar field. It is commonly used in physics and geometry for diffusion,
smoothing, curvature analysis, and solving partial differential equations.

For a scalar field :math:`f(x, y, z)`, the Laplacian :math:`\nabla^2 f`
is given by:

.. math::

   \nabla^2 f = \nabla f =
   \frac{\partial^2 f}{\partial x^2} +
   \frac{\partial^2 f}{\partial y^2} +
   \frac{\partial^2 f}{\partial z^2}

The Laplacian is positive where the field has a local minimum (value smaller
than its surroundings) and negative where it has a local maximum (value
larger than its surroundings).


Inputs
======

Grid
   The input scalar grid on which to compute the Laplacian.
   The grid must store scalar (float) values such as density, temperature,
   or a signed distance field.


Outputs
=======

Laplacian
   A float grid representing the Laplacian of the input field.

   Each voxel contains the sum of the second derivatives of the input
   field along the X, Y, and Z axes. This can be used to detect local
   peaks and valleys or to drive smoothing and diffusion effects in
   procedural grids.
