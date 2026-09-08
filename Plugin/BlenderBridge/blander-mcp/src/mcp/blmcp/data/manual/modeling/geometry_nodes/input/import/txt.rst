.. index:: Geometry Nodes; Import Text
.. _bpy.types.GeometryNodeImportText:

****************
Import Text Node
****************

.. figure:: /images/node-types_GeometryNodeImportText.webp
   :align: right
   :alt: Import Text node.

The *Import Text* node reads the contents of a plain text file and outputs it as a single string.
This can be useful in motion graphics or data-driven workflows where external text needs to be
processed or displayed.

.. note::

   Currently, only files with the `.txt` extension are supported.


Inputs
======

Path
   The path to the txt file.


Outputs
=======


String
   The entire contents of the text file as a single string.
