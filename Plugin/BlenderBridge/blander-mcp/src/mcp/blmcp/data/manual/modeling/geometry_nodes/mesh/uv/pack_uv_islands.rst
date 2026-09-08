.. index:: Geometry Nodes; Pack UV Islands
.. _bpy.types.GeometryNodeUVPackIslands:

********************
Pack UV Islands Node
********************

.. figure:: /images/node-types_GeometryNodeUVPackIslands.webp
   :align: right
   :alt: Pack UV Islands node.

The *Pack UV Islands* node rearranges UV islands so they efficiently fill a given UV space.
It scales, translates, and optionally rotates islands while keeping a defined margin between them.
This is useful for procedurally optimizing UV layouts inside Geometry Nodes workflows,
such as generating texture atlases or preparing geometry for baking.

.. tip::

   Unlike the :ref:`UV Editor operator <bpy.ops.uv.pack_islands>`, this node works non-destructively and can be driven
   by procedural inputs, making it suitable for automated or parametric UV generation.


Inputs
======

UV
   The UV map to pack. The topology of UV islands is determined from this input.

Selection
   Faces to consider when packing islands.
   Only UV islands that include at least one selected face are affected.
   UVs belonging exclusively to unselected faces remain unchanged.

Margin
   The distance to leave between UV islands, expressed in UV space units.

Rotate
   Allow rotating islands to achieve a more efficient packing result.

Method
   Determines how the shape of each island is evaluated during packing.

   :Bounding Box:
      Uses the axis-aligned bounding box of each island.
      This is the fastest method but may be less space-efficient.
   :Convex Hull:
      Uses the convex hull of each island.
      This method will not place islands inside holes and provides a balance
      between accuracy and performance.
   :Exact Shape:
      Uses the full island shape, including concave regions and holes.
      This produces the tightest packing but is the slowest option.

Bottom Left
   The bottom-left corner of the region into which islands are packed.

Top Right
   The top-right corner of the region into which islands are packed.


Output
======

UV
   The packed UVs, with islands repositioned and scaled according to the node settings.
