.. index:: Geometry Nodes; Delete Geometry
.. _bpy.types.GeometryNodeDeleteGeometry:

********************
Delete Geometry Node
********************

.. figure:: /images/node-types_GeometryNodeDeleteGeometry.webp
   :align: center
   :alt: Delete Geometry node.

The *Delete Geometry* node removes the selected part of a geometry.
It behaves similarly to the :ref:`Delete <bpy.ops.mesh.delete>` tool in Edit Mode.
The type of elements to be deleted can be specified with the domain and mode properties.


Inputs
======

Geometry
   Standard geometry input.

Selection
   Boolean field that is true for parts of the geometry to be deleted.


Properties
==========

Domain
   The domain on which the selection field is evaluated.

   :Point:
      The selection is on the points, control points, and vertices of the geometry.
   :Edge:
      The selection is on the edges of the mesh component. The other components
      are not modified.
   :Face:
      The selection is on the faces of the mesh component. The other components
      are not modified.
   :Spline:
      The selection is on the splines in the curve component. For each spline, it
      will either be deleted entirely or not at all. The other components are not
      modified.
   :Instance:
      The selection is on the top-level instances, and the entire instance is
      removed if it is selected. If the input also contains realized geometry,
      that will be unaffected.

Mode
   The type of elements to be affected.
   This only applies to the mesh component.

   :All:
      Vertices, edges, and faces in the selection will be deleted.
   :Only Edges & Faces:
      Vertices won't be deleted, even if they are in the selection.
   :Only Faces:
      Only faces in the selection will be deleted.


Output
======

Geometry
   Standard geometry output.
