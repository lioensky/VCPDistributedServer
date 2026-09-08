.. index:: Geometry Nodes; Import CSV
.. _bpy.types.GeometryNodeImportCSV:

***************
Import CSV Node
***************

.. figure:: /images/node-types_GeometryNodeImportCSV.webp
   :align: right
   :alt: Import CSV node.

The *Import CSV* node reads data from a CSV (Comma-Separated Values) file and generates a point cloud.
Each row in the file becomes a point, with numeric columns imported as attributes.

Attribute names are taken from the header row (if present), and types are inferred from the first value in each
column:

- Integer values create integer attributes.
- Float values create float attributes.

.. note::

   Only integer and float columns are supported. Other types, such as strings, are ignored.

This node is useful for visualizing external datasets in Geometry Nodes,
such as for scientific visualization or procedural generation based on tabular data.


Inputs
======

Path
   The path to the CSV file. The file must be structured with one row per point and values separated by a delimiter.

Delimiter
   The character used to separate values within each row of the CSV file,
   such as a comma (`,`), semicolon (`;`), or tab character.

   .. tip::

      Tab characters can be inserted using the :doc:`/modeling/geometry_nodes/utilities/text/special_characters`.


Outputs
=======

Point Cloud
   A point cloud geometry where each row of the CSV file corresponds to a point.
