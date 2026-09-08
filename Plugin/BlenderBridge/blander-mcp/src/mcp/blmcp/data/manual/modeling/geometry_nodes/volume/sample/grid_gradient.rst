.. index:: Geometry Nodes; Grid Gradient
.. _bpy.types.GeometryNodeGridGradient:

******************
Grid Gradient Node
******************

.. figure:: /images/node-types_GeometryNodeGridGradient.webp
   :align: right
   :alt: Grid Gradient node.

The *Grid Gradient* node calculates the gradient of a scalar voxel grid.
The gradient is a vector field that describes both the direction and rate of
the steepest increase in the grid's values at each voxel.

In other words, it shows how and where the scalar quantity (such as density,
temperature, or distance) changes in 3D space. The direction of the gradient
vector points toward increasing values, and its magnitude represents how
quickly the value changes in that direction.

Mathematically, for a scalar field :math:`f(x, y, z)`, the gradient is defined as:

.. math::

   \nabla f =
   \frac{\partial f}{\partial x} \mathbf{\hat{i}} +
   \frac{\partial f}{\partial y} \mathbf{\hat{j}} +
   \frac{\partial f}{\partial z} \mathbf{\hat{k}}

This operation is often used in procedural modeling or simulation workflows
to derive direction fields from scalar quantities, such as computing surface
normals from a signed distance field (SDF) or determining the flow direction
in density or temperature fields.


Inputs
======

Grid
   The input grid from which to compute the gradient.
   The grid must contain float values, such as density or distance.


Outputs
=======

Gradient
   A vector grid representing the gradient of the input field.
   Each vector points toward the direction of greatest increase in the scalar
   value, with its length corresponding to the rate of change.
