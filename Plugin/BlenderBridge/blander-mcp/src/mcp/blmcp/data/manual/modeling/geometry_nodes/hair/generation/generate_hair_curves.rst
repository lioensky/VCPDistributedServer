.. index:: Geometry Nodes; Generate Hair Curves

********************
Generate Hair Curves
********************

The *Generate Hair Curves* node procedurally creates new hair curves on the surface of a mesh.
It generates curves from scratch at sampled point locations rather than using existing hair data.
For cases where curves should interpolate or follow existing guides, use the
:doc:`Interpolate Hair Curves </modeling/geometry_nodes/hair/generation/interpolate_hair_curves>` node instead.

.. note::

   This node or modifier requires valid *Surface* geometry or object inputs,
   along with a *Surface UV Map*, to function properly.

.. peertube:: nkB43evNMakLmvuoExgKuF


Inputs
======

Surface Input Type
   Determines how the surface data is provided for interpolation.

   :Object:
      Use an object reference to provide the surface.
   :Geometry:
      Use a geometry input directly connected to the surface mesh.

Surface
   The surface object used for generation.
   Its transforms must match those of the modifier object to ensure correct placement.

Surface UV Map
   The UV map used to determine the root positions of the hair curves on the surface mesh.

Surface Rest Position
   When enabled, sets the surface mesh to its rest position before generating the hair curves.
   This ensures consistent attachment locations when deforming the surface later.

   .. tip::

      When combining this node with :doc:`Deform Curves on Surface
      </modeling/geometry_nodes/curve/operations/deform_curves_on_surface>`,
      enable *Surface Rest Position* if the deformation node follows this one in the modifier stack,
      so the generation uses pre-deformed surface positions.

Hair Length
   The length of the generated hair curves.

Hair Material
   The material assigned to the generated hair curves.

Control Points
   The number of control points used for each generated curve.
   More points allow smoother deformations and finer control.


Distribution
------------

Distribution Method
   Determines how the root points are distributed across the surface.

   :Random:
      Places points randomly on the surface.
   :Poisson Disk:
      Uses a Poisson disk distribution to ensure a minimum spacing between points.
      See :doc:`Distribute Points on Faces </modeling/geometry_nodes/point/distribute_points_on_faces>` for more
      details.

Density
   Controls the number of generated hair curves per surface area.
   Higher values produce denser hair coverage.

Density Mask
   A scalar factor that modulates the density across the surface.
   This allows certain regions to have more or fewer generated curves.

Mask Texture
   An image texture used to discard curves based on pixel values sampled with the *Surface UV Map* input.
   White areas retain curves, while black areas remove them.

   .. tip::

      The accuracy of the *Mask Texture* is independent of the mesh vertex density,
      since it is evaluated after the root points are distributed.
      However, using the *Density Mask* input instead can improve performance,
      and combining both provides flexibility and efficiency.

Viewport Amount
   A factor applied to reduce curve density in the viewport for better performance,
   without affecting the final render.

Seed
   Sets the random seed for the distribution process.
   Changing this value alters the pattern of generated curves while maintaining the same parameters.


Outputs
=======

Geometry
   The output geometry containing the generated hair curves.

Curves
   A separate output of the generated curve data for further processing or inspection.

Surface Normal
   The surface normal direction at each curve's attachment point.
