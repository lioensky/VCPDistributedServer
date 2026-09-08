.. index:: Geometry Nodes; Scale Instances
.. _bpy.types.GeometryNodeScaleInstances:

********************
Scale Instances Node
********************

.. figure:: /images/node-types_GeometryNodeScaleInstances.webp
   :align: right
   :alt: Scale Instances node.

The *Scale Instances* node scales geometry instances in local or global space.

The :doc:`/modeling/geometry_nodes/instances` page contains more information about geometry instances.


Inputs
======

Instances
   Standard geometry input.

Selection
   Boolean field used to determine if an instance will be scaled.

Scale
   The scale factor to apply to the instance's transform on each axis.

Center
   The position from which the instance origins are scaled. Each instance will move away from this location.
   When the *Local Space* input is enabled, this location is relative to the initial transform
   of each instance.

Local Space
   If enabled, the instances are scaled in local space. In other words,
   they are scaled in the directions the described by the initial transform of each instance.
   When the input is disabled, the *Center* and *Scale* inputs are specified in
   the local space of the modifier object.


Outputs
=======

Instances
   Standard geometry output.
