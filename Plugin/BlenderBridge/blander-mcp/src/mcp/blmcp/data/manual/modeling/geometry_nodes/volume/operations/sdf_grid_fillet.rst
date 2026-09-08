.. index:: Geometry Nodes; SDF Fillet
.. _bpy.types.GeometryNodeSDFGridFillet:

***************
SDF Fillet Node
***************

.. figure:: /images/node-types_GeometryNodeSDFGridFillet.webp
   :align: right
   :alt: SDF Fillet node.

The *SDF Fillet* node smooths or rounds off concave internal corners in a Signed Distance Field (SDF) grid.
It modifies the field to produce softer transitions between surfaces that meet
at sharp inward angles, similar to adding a *fillet* or *bevel* in mesh modeling.

This operation only affects regions with **negative principal curvature**
(concave corners) and preserves overall volume. The result is a more organic
and continuous surface, useful for soft blending of intersecting shapes or
removing hard transitions after boolean operations.


Inputs
======

Grid
   The input SDF grid to be smoothed.
   Typically generated from another SDF operation such as a boolean or mesh conversion.

Iterations
   The number of smoothing iterations to apply.
   Higher values produce a larger, smoother fillet radius but also increase computation time.
   A single iteration results in a subtle rounding, while multiple iterations
   create progressively softer surfaces.


Outputs
=======

Grid
   The resulting SDF grid with concave corners rounded off.
   The output can be visualized by converting it to a mesh with
   :doc:`Grid to Mesh </modeling/geometry_nodes/volume/operations/grid_to_mesh>` or
   used in further volumetric operations.
