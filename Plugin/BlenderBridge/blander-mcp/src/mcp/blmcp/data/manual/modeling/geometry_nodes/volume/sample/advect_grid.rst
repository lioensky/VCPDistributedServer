.. index:: Geometry Nodes; Advect Grid
.. _bpy.types.GeometryNodeGridAdvect:

****************
Advect Grid Node
****************

.. figure:: /images/node-types_GeometryNodeGridAdvect.webp
   :align: right
   :alt: Advect Grid node.

The *Advect Grid* node moves voxel values through a velocity field over time
using numerical integration. This operation is called *advection* and is
commonly used in fluid, smoke, and motion simulation systems to evolve
quantities such as density, temperature, or color according to a flow field.

The node supports multiple integration schemes that trade off between speed,
accuracy, and numerical stability. It can be used for both scalar and vector
grids, provided the voxel size is uniform across the domain.

Advection is conceptually equivalent to tracing each voxel backward through the
velocity field by a small time step, sampling the grid value from the previous
location, and assigning that value to the current voxel.


Inputs
======

Grid
   The input grid to advect. Must have a uniform voxel scale.

Velocity
   The vector grid defining the flow direction and magnitude at each voxel.
   The *Velocity* field determines how grid values are transported through
   space.

Time Step
   The time step used for advection, in seconds.
   Larger values result in faster motion but may reduce accuracy or stability.

Integration Scheme
   The numerical integration method used to trace voxel positions through the
   velocity field:

   :Semi-Lagrangian:
      First-order semi-Lagrangian integration. Fastest and most stable but
      introduces noticeable numerical diffusion (blurring).
   :Midpoint:
      Second-order midpoint integration. Balances speed and accuracy, suitable
      for most cases.
   :Runge-Kutta 3:
      Third-order Runge-Kutta integration. Provides higher accuracy with
      moderate computational cost.
   :Runge-Kutta 4:
      Fourth-order Runge-Kutta integration. Highest accuracy single-step
      scheme, ideal for detailed simulations but slower to compute.
   :MacCormack:
      MacCormack scheme with implicit diffusion control. Reduces numerical
      dissipation while maintaining stability.
   :BFECC:
      Back and Forth Error Compensation and Correction. An advanced scheme that
      minimizes dissipation and maintains sharper features.

Limiter
   The limiting strategy used to reduce overshoot or undershoot artifacts
   in high-order advection schemes:

   :None:
      No limiting applied. Fastest but can introduce artifacts in regions with
      steep gradients.
   :Clamp:
      Clamps values to the range of the original neighborhood, preventing
      overshooting and undershooting while preserving stability.
   :Revert:
      Reverts to first-order integration in cases where clamping would be
      necessary. More conservative and stable than clamping alone.


Properties
==========

Data Type
   The type of data stored in the grid (e.g. *Float*, *Integer*, *Vector*).
   Determines the kind of field being advected.


Outputs
=======

Grid
   The resulting grid after advection. Each voxel value has been transported
   according to the specified velocity field and integration scheme.
   The result represents the grid state after the given *Time Step* has elapsed.
