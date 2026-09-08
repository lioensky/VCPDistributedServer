.. index:: Geometry Nodes; Instances to Points
.. _bpy.types.GeometryNodeInstancesToPoints:

************************
Instances to Points Node
************************

.. figure:: /images/node-types_GeometryNodeInstancesToPoints.webp
   :align: right
   :alt: Instances to Points node.

The *Instances to Points* node generates points at the origins of top-level instances.
Attributes on the :ref:`instance domain <attribute-domains>` are moved to the point cloud points.

.. note::

   Top-level instances are those that are owned by the node's input geometry.
   Instances owned by other instances, i.e. nested instances, are not considered
   by this node.


Inputs
======

Instances
   Standard geometry input.

Selection
   The instances used to generate points. True values mean a point is created for the instance,
   false values mean the instance is skipped.

Position
   Overrides the default position of generated point.

Radius
   Controls the radius of the result points.


Outputs
=======

Points
   Standard geometry output.
