.. index:: Geometry Nodes; Randomize Transforms

*************************
Randomize Transforms Node
*************************

.. figure:: /images/node-types_GeometryNodeRandomizeTransforms.webp
   :align: right
   :alt: Randomize Transforms node.

The *Randomize Transforms* node applies random translation, rotation, and scale to instances.
It is commonly used to create natural variation among duplicated objects, such as scattered
rocks, trees, or other elements in a scene.


Inputs
======

Instances
   The input geometry containing the instances to be randomized.

Selection
   Controls which instances are affected by the randomization.
   Only selected instances will receive random transformations.

Local Space
   - When enabled, transformations are applied in each instance's local coordinate space.
   - When disabled, randomization is performed in the global coordinate space.

Offset
   The maximum translation offset for each axis. Defines the random range for instance movement.

Rotation
   The maximum rotation for each axis. Defines how much each instance can be rotated.

Scale Axes
   Determines how scaling is applied.

   :Uniform:
      Applies a single random scale factor uniformly to all axes.
   :Axes:
      Applies an independent random scale factor to each axis.

Scale
   The maximum scaling factor applied to each instance.

Flipping
   Randomly flips instances along one or more axes, effectively mirroring them.

Seed
   An integer value that initializes the random number generator.
   Changing the seed produces a different random arrangement while keeping the same parameters.


Outputs
=======

Instances
   The resulting geometry with randomized instance transforms applied.
