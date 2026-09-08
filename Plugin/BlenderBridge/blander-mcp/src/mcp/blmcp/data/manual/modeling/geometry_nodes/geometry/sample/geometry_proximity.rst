.. index:: Geometry Nodes; Geometry Proximity
.. _bpy.types.GeometryNodeProximity:

***********************
Geometry Proximity Node
***********************

.. figure:: /images/node-types_GeometryNodeProximity.webp
   :align: center
   :alt: Geometry Proximity node.

The *Geometry Proximity* node computes the closest location on the target geometry.

.. tip::

   The :doc:`/modeling/geometry_nodes/utilities/math/map_range` is often helpful to use with the distance
   output of this node to create a falloff with a maximum distance.


Inputs
======

Geometry
   Standard geometry input.

Group ID
   Splits the elements of the input geometry into groups which can be sampled individually.

Sample Position
   The given position to calculate the closest location on the target.

Sample Group ID
   Determines in which group the closest nearest element is detected.


Properties
==========

Target Element
   :Faces:
      Calculate the closest point anywhere on the faces of the target's mesh geometry.
   :Edges:
      Calculate the closest point anywhere on the edges of the target's mesh geometry.
   :Points:
      Calculate the closest point or vertex on the target geometry. This mode is usually the fastest.
      This mode works for both point cloud and mesh geometry, the other modes only work for meshes.


Outputs
=======

Position
   Closest location on the surface of the target mesh, or the closest point in the target point cloud
   in *Points* mode.

Distance
   Distance (as floating-point value) from the source position to the closest location in the target.

Is Valid
   Whether the sampling was successful. It can fail when the sampled group is empty.


Examples
========

The different modes of the node: faces, edges and points.
In this example the Geometry Nodes modifier is added on the target plane.
Note that the larger plane is subdivided and the smaller plane is not.

.. figure:: /images/modeling_geometry-nodes_geometry-proximity_modes.png
   :align: center

   The three target element modes: faces, edges, and points.

.. figure:: /images/modeling_geometry-nodes_geometry-proximity_example.png
   :align: center

   Points distributed on a sphere used as a target for a distance used in a shader.
