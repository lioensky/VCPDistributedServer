.. index:: Geometry Nodes; Merge by Distance
.. _bpy.types.GeometryNodeMergeByDistance:

**********************
Merge by Distance Node
**********************

.. figure:: /images/node-types_GeometryNodeMergeByDistance.webp
   :align: right
   :alt: Merge by Distance node.

The *Merge by Distance* node merges selected mesh vertices or point cloud points within a given distance,
merging surrounding geometry where necessary. This operation is similar to the :ref:`bpy.ops.mesh.remove_doubles`
operator or the :doc:`/modeling/modifiers/generate/weld`.


Inputs
======

Geometry
   Standard geometry input.

Selection
   Boolean field that is true for parts of the geometry to be deleted.
   Unselected points will be completely unused for the operation--
   they will not be merged into other points, and no points will merge into them either.

   .. tip::

      When possible, using the selection input can be a simple way to speed up the node,
      since searching for nearby points is a relatively expensive operation that gets even
      more expensive when more points are involved.

Mode
   Method for choosing which vertices are merged.

   :All: Merge includes all geometry including loose parts.
   :Connected: Merge only includes attached geometry i.e. the modifier will not merge loose parts together.

Distance
    The distance to use for searching for nearby points.


Output
======

Geometry
   Standard geometry output.


Examples
========

.. figure:: /images/modeling_geometry-nodes_geometry_merge-by-distance_points.png
   :align: center

   Using the selection input to only merge some of the points in a point cloud.
