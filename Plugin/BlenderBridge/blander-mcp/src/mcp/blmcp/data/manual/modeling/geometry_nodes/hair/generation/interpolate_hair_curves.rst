.. index:: Geometry Nodes; Interpolate Hair Curves

***********************
Interpolate Hair Curves
***********************

The *Interpolate Hair Curves* node generates new hair curves by interpolating existing *guide* curves
on a surface mesh.
It allows for efficient grooming workflows where a small number of guide curves define the overall
shape, and the node fills in additional interpolated curves to create a dense, detailed hair system.

For simpler duplication-based setups, the
:doc:`Duplicate Hair Curves </modeling/geometry_nodes/hair/generation/duplicate_hair_curves>`
node provides a lighter-weight alternative that may perform faster.

.. note::

   This node or modifier requires valid *Surface* geometry or object inputs,
   along with a *Surface UV Map*, to function properly.

.. peertube:: 4dt7vp3qmry5MPZC3usxVb

Inputs
======

Geometry
   The input geometry containing the guide hair curves to interpolate.

Surface Input Type
   Determines how the surface data is provided for interpolation.

   :Object:
      Use an object reference to provide the surface.
   :Geometry:
      Use a geometry input directly connected to the surface mesh.

Surface
   The surface object used as the attachment base for the interpolated curves.
   Its transforms must match those of the modifier object.

Surface UV Map
   The UV map used to find attachment locations for the interpolated curves on the surface.

Surface Rest Position
   When enabled, sets the surface mesh to its rest position before attaching curves.
   This ensures consistent root positions when deformation is applied afterward.

   .. tip::

      When combining this node with :doc:`Deform Curves on Surface
      </modeling/geometry_nodes/curve/operations/deform_curves_on_surface>`,
      enable *Surface Rest Position* if the deformation node follows this one,
      so that pre-deformed coordinates are used for consistent interpolation.

Follow Surface Normal
   When enabled, aligns the interpolated curves with the surface normal at their root attachment point.

Part by Mesh Islands
   When enabled, treats separate mesh islands on the surface as independent regions for interpolation,
   preventing cross-blending of guides between disconnected areas.

Interpolation Guides
   The number of nearest guide curves used to interpolate the shape of each new curve.
   Higher values result in smoother transitions but may slightly reduce performance.

Distance to Guides
   The maximum distance from a guide curve within which interpolation occurs.
   Curves outside this range will not influence the result.


Distribution
------------

Distribution Method
   Determines how root points for interpolated curves are distributed across the surface.

   :Random:
      Distributes roots randomly across the surface.
   :Poisson Disk:
      Uses Poisson disk sampling to maintain a minimum distance between root points,
      producing an even and natural distribution.

Density
   The number of interpolated hair curves generated per unit of surface area.
   Higher values increase the total hair density.

Density Mask
   A scalar factor used to locally scale the curve density across the surface.

Mask Texture
   Uses an image texture to control which areas of the surface generate hair.
   The image is sampled using the *Surface UV Map* input.

   .. tip::

      Texture sampling occurs after root points are generated, so accuracy is not limited by mesh resolution.
      The *Density Mask* input is typically faster; using both together can balance quality and performance.

Viewport Amount
   A factor used to reduce curve density in the viewport for performance optimization.
   This does not affect the final render density.

Seed
   Sets the random seed for the interpolation and distribution processes.
   Changing this value generates a different random distribution while maintaining the same parameters.


Outputs
=======

Geometry
   The resulting geometry containing the interpolated hair curves.

Guide Index
   An integer attribute storing the index of the main guide curve used to generate each interpolated curve.

Surface Normal
   The surface normal direction at each curve's root attachment point.
