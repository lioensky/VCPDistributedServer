.. index:: Geometry Nodes; Scatter on Surface

***********************
Scatter on Surface Node
***********************

.. figure:: /images/node-types_GeometryNodeScatterOnSurface.webp
   :align: right
   :alt: Scatter on Surface node.

The *Scatter on Surface* node distributes points or instances across the surface of a mesh.
It provides flexible control over how elements are placed using density, randomization,
and Poisson disk sampling.
This node is useful for procedural scattering of objects such as grass, rocks, or debris
on terrain or any other surface.


Inputs
======

Mesh
   The input surface geometry on which points or instances will be scattered.

.. section-inputs

Selection
   Determines which faces or parts of the mesh are used for scattering.
   Unselected areas will not receive any scattered elements.

Density Method
   Determines how the number of scattered points is controlled.

   :Density:
      Uses a density field to define how many points are scattered per unit area.
   :Amount:
      Uses a fixed number of total scattered points across the surface.

Distribution Method :guilabel:`Density`
   Determines the pattern of scattered points when *Density* is used.

   :Random: Distributes points randomly across the surface.
   :Poisson Disk: Distributes points evenly using a minimum separation distance.

Density :guilabel:`Density`
   Controls the number of scattered points per unit area when using the *Density* method.

Amount :guilabel:`Amount`
   The total number of points to scatter when using the *Amount* method.

Distribution Mask
   A mask that limits the areas where scattering occurs.
   Values closer to ``1.0`` allow scattering, while values near ``0.0`` exclude it.

Minimum Distance :guilabel:`Poisson Disk`
   Defines the minimum spacing between scattered points when using *Poisson Disk* distribution.
   Higher values result in more evenly spaced points but fewer total points.

Keep Surface
   Keeps the original surface geometry in the output, instead of outputting only the instances.

Scatter on Instances
   Enables scattering directly on existing instances rather than on a single mesh surface.

Seed
   Random seed value used to vary the distribution pattern of scattered points or instances.


Instancing
----------

Input Type
   Defines how the instance geometry input is provided.

   :Data-Block: Instances are created from an object or collection data-block.
   :Geometry: Instances are created from input geometry provided to the node.

Instance Type :guilabel:`Data-Block`
   When using *Data-Block* input, determines whether to instance an *Object* or a *Collection*.

Object / Collection :guilabel:`Data-Block`
   The specific object or collection to instance when using *Data-Block* input mode.

Instance :guilabel:`Geometry`
   The geometry to instance when using *Geometry* input mode.

Viewport Visibility
   Controls the percentage of scattered instances that are visible in the viewport.

Realize Instances
   Converts all instances into real geometry, producing a single combined geometry output.
   This can be required for some subsequent geometry operations or modifiers.


Pick Instance :guilabel:`Data-Block` :guilabel:`Collection`
-----------------------------------------------------------

When instancing from a collection, this option enables random or controlled selection
of which child object to instance per scattered point.

Reset Transform
   Resets the transform of instances before applying the scattering transform.

Instance Seed
   Controls the randomization of instance selection and transforms per scattered element.


Transform
^^^^^^^^^

Surface Offset
   Moves instances along the element normal, offsetting them from the surface.

Align Rotation
   Aligns instance rotation to the orientation of the geometry element (e.g., normal direction).

Alignement Axis

Scale
   Controls the uniform or per-axis scaling of instances.


Randomize
"""""""""

Can be enabled through the boolean found in the panel header.

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


Masking
-------

Image Mask
   An image used to control scattering density or placement via UV mapping.

UV Map
   The UV map used to interpret the image mask for controlling distribution.


.. section-outputs

Outputs
=======

Instances
   The resulting instances scattered across the surface, distributed according to the selected method and parameters.
