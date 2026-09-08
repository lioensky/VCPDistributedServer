.. index:: Geometry Nodes; SDF Grid Mean
.. _bpy.types.GeometryNodeSDFGridMean:

******************
SDF Grid Mean Node
******************

.. figure:: /images/node-types_GeometryNodeSDFGridMean.webp
   :align: right
   :alt: SDF Grid Mean node.

The *SDF Grid Mean* node applies mean (box) filter smoothing to a Signed Distance Field (SDF) grid.
This operation averages voxel values within a local neighborhood to smooth
out small variations and noise while preserving the overall shape of the field.

The filter works as a fast, separable averaging operation—sometimes called a
*box filter*—and is well suited for general-purpose smoothing or softening of
SDF data after boolean, voxelization, or other volumetric operations.


Inputs
======

Grid
   The input signed distance field to be smoothed.

Width
   The radius of the smoothing kernel in voxels.
   Larger values result in a broader smoothing effect, producing softer,
   less detailed surfaces. Smaller values restrict smoothing to immediate
   neighbors, retaining more fine detail.

Iterations
   The number of times the mean filter is applied.
   Each iteration increases the smoothness of the surface.
   Multiple passes can approximate a Gaussian-like blur effect.


Outputs
=======

Grid
   The resulting SDF grid after mean filtering.
   The surface becomes smoother and more uniform, making it useful for
   refining noisy or rough SDFs before further operations such as
   :doc:`Grid to Mesh </modeling/geometry_nodes/volume/operations/grid_to_mesh>`.
