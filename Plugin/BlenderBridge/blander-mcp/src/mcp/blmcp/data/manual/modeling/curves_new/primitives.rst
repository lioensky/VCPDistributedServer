.. _bpy.ops.curves.add:

****************
Curve Primitives
****************

.. _bpy.ops.object.curves_empty_hair_add:

Empty Hair
==========

Adds an empty high-performance curves object and automatically:

- Assigns the active object as the :doc:`Surface </sculpt_paint/curves_sculpting/introduction>`.
- Set the surface object as the parent of the new object.
- Adds a Geometry Nodes modifier to deform the curves on the surface.


Fur
===

Adds a fur setup to the selected objects.
The fur setup is based on :doc:`/modeling/geometry_nodes/index` and built with
:doc:`Hair Node Groups </modeling/geometry_nodes/hair/index>` that come with Blender as bundled assets.

See :ref:`bpy.ops.object.quick_fur` for more information.
