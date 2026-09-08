.. index:: Geometry Nodes; Sample UV Surface
.. _bpy.types.GeometryNodeSampleUVSurface:

**********************
Sample UV Surface Node
**********************

.. figure:: /images/node-types_GeometryNodeSampleUVSurface.webp
   :align: center
   :alt: Sample UV Surface node.

The *Sample UV Surface* node finds values on a mesh's surface at specific UV locations.
Internally the process is a "reverse UV lookup" from a location in 2D space. The node then
finds the face that corresponds to each UV coordinate, and the location within that face.

.. warning::

   Because of the node's method of computation, the UV map should not have any overlapping faces.
   If the UV map is sampled at a location with no faces or overlapping faces, the node will
   output the default value for the data type, which is zeros for most types.


Inputs
======

Mesh
   A geometry containing the mesh with a UV map for sampling.

Value
   A field to evaluate on the target *Mesh* geometry for later sampling at the surface positions.

UV Map
   The mesh UV map to sample, evaluated on the *Mesh* input. Should not have overlapping faces.

Sample UV
   The coordinates to sample within the UV map.


Properties
==========

Data Type
   The :ref:`data type <attribute-data-types>` to use for the retrieved values.


Outputs
=======

Value
   The data retrieved and interpolated from the *Mesh* geometry, mapped based on the node's settings and inputs.

Is Valid
   Whether the node could find a single face to sample at the UV coordinate.
