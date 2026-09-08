.. index:: Geometry Nodes; Index
.. _bpy.types.GeometryNodeInputIndex:

**********
Index Node
**********

.. figure:: /images/node-types_GeometryNodeInputIndex.webp
   :align: right
   :alt: Index node.

The *Index* node gives an integer value indicating the position of each element in the list,
starting at zero. This depends on the internal order of the data in the geometry, which is not
necessarily visible in the 3D Viewport. However, the index value is visible in the left-most column
in the :doc:`Spreadsheet Editor </editors/spreadsheet>`.

.. note::

   Indices in geometry data are often defined by the internals of complex algorithms that create it.
   If no inputs change, indices will be the same when the same node tree is executed multiple times.
   However, they may not be predictable when inputs to nodes that generate geometry or change its
   topology are adjusted. Additionally, updates to algorithms in newer versions of Blender may
   change the order of generated elements.

   To avoid relying on consistent indices, it is recommended to calculate them locally,
   or to avoid operations that change topology when they must be consistent over time.


Inputs
======

This node has no inputs.


Outputs
=======

Index
   Integer value which enumerates each point on the geometry.
