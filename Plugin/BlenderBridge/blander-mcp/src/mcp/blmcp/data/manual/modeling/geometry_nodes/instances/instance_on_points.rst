.. index:: Geometry Nodes; Instance on Points
.. _bpy.types.GeometryNodeInstanceOnPoints:

***********************
Instance on Points Node
***********************

.. figure:: /images/node-types_GeometryNodeInstanceOnPoints.webp
   :align: center
   :alt: Instance on Points node.

The *Instance on Points* node adds a reference to a geometry to each of the points present
in the input geometry. Instances are a fast way to add the same geometry to a scene many times
without duplicating the underlying data. The node works on any geometry type
with a *Point* domain, including meshes, point clouds, and curve control points.

Any attributes on the points from the *Geometry* input will be available on the instance
domain of the generated instances.

.. tip::

   The :ref:`bpy.ops.object.duplicates_make_real` operator can be used to create objects
   from instances generated with this node.

.. note::

   To instance object types that do not contain geometry, like a light object, the
   :doc:`/modeling/geometry_nodes/input/scene/object_info` can be used. Other objects like
   :doc:`Metaball </modeling/metas/introduction>` objects are not supported for instancing.

Inputs
======

Points
   Standard geometry input. The position of the points of this geometry affect the transforms of
   each instance output.

   .. note::

      If the input geometry contains instances, the node will create more instances on
      the points inside the instances, creating :ref:`nested instancing <geometry-nodes_nested-instancing>`.
      In this case, each new instance will have the transform created by the node from the *Rotation*
      and *Scale* inputs, but it will *also* be transformed based on the parent instances.

Selection
   Whether to instance on each point. True values mean an instance will be generated on the point,
   false values mean the point will be skipped.

Instance
   The geometry to instance on each selected point. This can contain real geometry, or multiple instances,
   which can be useful when combined with the *Pick Instance* option.

Pick Instances
   If enabled, instead of adding the entire geometry from the *Instance* input on every point,
   choose an instance from the instance list of the geometry based on the *Instance Index* input.
   This option is intended to be used with the :doc:`/modeling/geometry_nodes/input/scene/collection_info`.

Instance Index
   The selection of index for every selected point, only used when *Pick Instances* is true.
   By default the point :doc:`ID </modeling/geometry_nodes/geometry/read/id>` is used,
   or the :doc:`index </modeling/geometry_nodes/geometry/read/input_index>` if that doesn't exist.
   Negative values or values that are too large are wrapped around to the other end of
   the instance list.

Rotation
   The :term:`Euler` rotation for every instance. This can use the rotation output of nodes like
   :doc:`Distribute Points on Faces </modeling/geometry_nodes/point/distribute_points_on_faces>`
   and :doc:`Curve to Points </modeling/geometry_nodes/curve/operations/curve_to_points>`. An Euler rotation
   can also be created from a direction vector like the :doc:`normal </modeling/geometry_nodes/geometry/read/normal>`
   with the :doc:`/modeling/geometry_nodes/utilities/rotation/align_rotation_to_vector`.

Scale
   The size of each generated instance.


Outputs
=======

Instances
   Standard geometry output. If the ``id`` attribute exists on the input geometry,
   it will be copied to the result instances.
