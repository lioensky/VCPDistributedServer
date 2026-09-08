.. index:: Geometry Nodes; Raycast
.. _bpy.types.GeometryNodeRaycast:

************
Raycast Node
************

.. figure:: /images/node-types_GeometryNodeRaycast.webp
   :align: center
   :alt: Raycast node.

The *Raycast* node intersects rays from one geometry onto another. The source geometry is defined by
the context of the node that the *Raycast* node is connected to.
Each ray computes hit points on the target mesh and outputs normals, distances
and any surface attribute specified.


Inputs
======

Target Geometry
   Geometry that rays are tested against.

Attribute
   An optional field input evaluated on the *Target Geometry* that will be interpolated at the hit points.
   The resulting values are outputted with the *Attribute* output.

Interpolation
   How attributes of the target mesh are mapped to the attribute values on the result geometry.

   :Interpolated:
      Vertex and corner attributes are interpolated smoothly, with a barycentric function.
   :Nearest:
      Choose the value of the closest vertex without interpolating.

Source Position
   The position from where to start each ray. By default, this is the same as
   if the :doc:`/modeling/geometry_nodes/geometry/read/position` was connected.

Ray Direction
   Direction of each ray from the starting position.
   The field is evaluated on the geometry from the context of the field evaluation, not the *Target Geometry*.

Ray Length
   Maximum distance a ray can travel before being considered "no hit".


Properties
==========

Data Type
   The :ref:`data type <attribute-data-types>` used for the evaluated data.


Outputs
=======

Is Hit
   Boolean output that is true for each ray which has hit the *Target Geometry*.

Hit Position
   The location of the intersection point with the target mesh.

Hit Normal
   The surface :term:`Normal` vector at the hit location.

Hit Distance
   The distance from the *Source Position* to the *Hit Position*.
   If the ray does not hit, the *Ray Length* is returned.

Attribute
   Interpolated values of the *Attribute* input sampled at the *Hit Position*.
