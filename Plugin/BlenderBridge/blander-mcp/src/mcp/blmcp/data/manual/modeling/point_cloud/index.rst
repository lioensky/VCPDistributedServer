.. _bpy.ops.object.pointcloud:

###############
  Point Cloud
###############

:term:`Point clouds <Point Cloud>` are a type of object used to represent
large numbers of individual points in 3D space.
They are particularly useful for visualizing 3D scan data, particle simulations,
or sparse datasets where a surface mesh is unnecessary or impractical.

Each point in a point cloud can store data using *Attributes*
that define properties such as position, color, and more.
Future updates may expand support to include simulation systems like particles.

.. figure:: /images/modeling_point-cloud_example.png

   Example of a monkey object represented as a point cloud.

.. toctree::
   :maxdepth: 2

   tools.rst
   Selecting <selecting.rst>
   Editing <editing.rst>
   Properties <properties.rst>

