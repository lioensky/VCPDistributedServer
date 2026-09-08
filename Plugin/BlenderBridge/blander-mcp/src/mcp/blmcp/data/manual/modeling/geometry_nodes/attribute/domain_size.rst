.. index:: Geometry Nodes; Domain Size
.. _bpy.types.GeometryNodeAttributeDomainSize:

****************
Domain Size Node
****************

.. figure:: /images/node-types_GeometryNodeAttributeDomainSize.webp
   :align: right
   :alt: Domain Size node.

The *Domain Size* outputs the size of an attribute domain on the selected geometry type,
for example, the number of edges in a mesh, or the number of points in a point cloud.

For more information about attribute domains, see the :ref:`geometry attributes page <attribute-domains>`.


Inputs
======

Geometry
   Standard geometry input.


Properties
==========

Component
    Which geometry type to retrieve the domain sizes from.

Outputs
=======

Point Count
   The size of the *Point* domain on any supported geometry.

Edge Count
   The size of the *Edge* domain on meshes.

Face Count
   The size of the *Face* domain on meshes.

Face Corner Count
   The size of the *Face Corner* domain on meshes.

Spline Count
   The size of the *Spline* domain on curves.

Instance Count
   The number of top-level instances in the geometry. :ref:`Nested instances <geometry-nodes_nested-instancing>`
   are not considered.
