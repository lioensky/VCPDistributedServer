.. _bpy.types.TextureNodeAt:

*******
At Node
*******

.. figure:: /images/node-types_TextureNodeAt.webp
   :align: right
   :alt: At node.

Returns the color of a texture at the specified coordinates.


Inputs
======

Texture
   Standard color input.
Coordinates
   The point at which to sample the color. For images, the space is between -1 and 1 for X and Y.
   If the coordinates are not spatially varying, the node will return a single color.


Properties
==========

This node has no properties.


Outputs
=======

Texture
   Standard color output.
