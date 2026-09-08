.. index:: Geometry Nodes; Import STL
.. _bpy.types.GeometryNodeImportSTL:

***************
Import STL Node
***************

.. figure:: /images/node-types_GeometryNodeImportSTL.webp
   :align: right
   :alt: Import STL node.

The *Import STL* node imports mesh geometry from a `.stl` (Stereolithography) file.

STL files are commonly used for 3D printing and CAD applications and contain only surface geometry,
typically as a collection of triangles with no color, texture, or other attributes.

This node enables incorporating external STL assets into Geometry Nodes for procedural processing or visualization.

.. seealso::

   :ref:`STL Import Operator <bpy.ops.wm.stl_import>`


Inputs
======

Path
   The path to the `.stl` file to be imported.


Outputs
=======

Mesh
   The mesh geometry imported from the STL file.
