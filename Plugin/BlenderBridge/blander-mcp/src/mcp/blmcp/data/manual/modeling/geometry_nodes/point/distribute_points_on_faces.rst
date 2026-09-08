.. index:: Geometry Nodes; Distribute Points on Faces
.. _bpy.types.GeometryNodeDistributePointsOnFaces:

**************************
Distribute Points on Faces
**************************

.. figure:: /images/node-types_GeometryNodeDistributePointsOnFaces.webp
   :align: right
   :alt: Distribute Points on Faces node.

The *Distribute Points on Faces* node places points on the surface of the input geometry object.
Point, corner, and polygon attributes of the input geometry are transferred to the generated points.
That includes vertex weights and UV maps.
Additionally, the node has *Normal* and *Rotation* outputs.

The node also generates a stable ID, stored in the built-in ``id`` attribute, used as
a stable identifier for each point. When the mesh is deformed or the density changes
the values will be consistent for each remaining point. This attribute is used in
the :doc:`Random Value </modeling/geometry_nodes/utilities/random_value>` and
:doc:`Instance on Points </modeling/geometry_nodes/instances/instance_on_points>` nodes.


Inputs
======

Mesh
   Standard geometry input.

   .. note::

      The input geometry must contain a mesh with faces.

Selection
   The selection of which face corners should be considered for point distribution.

Distance Min
   The minimal distance points can have to each other.
   This option is only available for the *Poisson Disk* distribution method.
   At its default value of zero, the node's behavior is the same as it is in *Random* mode,
   because none of the internally generated points are removed.

Density Max
   The point density for the point distribution. The unit is in number of points per square meter.
   This value is multiplied by the values from the *Density* input. Only available in *Poisson Disk* mode.

   .. note::

      This will be capped on distributions by the *Distance Min* option.
      If the density is greater than what the minimal distance allows,
      no new points will be added after this threshold has been passed.

Density
   The number of points to distribute per square meter on each mesh face.
   This value is multiplied by the values from the *Density Attribute*.

   In *Poisson Disk* mode, this value is multiplied by the *Density Max* input for the final density.

Seed
   The random :term:`Seed` to use when generating points.


Properties
==========

Distribution Method
   :Random:
      Distribute points randomly on the surface. This is the fastest distribution method.
   :Poisson Disk:
      Distribute points randomly on the surface while taking a minimum distance into account.

Legacy Normal
   By default, the node uses smooth and custom normals for the *Normal* and *Rotation* values .
   An earlier version of this node only uses "true" normals,
   this option brings back this behavior of only using "true" normals.

   This option can only be available in the Sidebar.


Outputs
=======

Points
   Generated points. Named attributes are copied to the result mesh, along with the data in the other
   attribute field outputs.

Normal
   The :term:`Normal` of the triangle on which each point is scattered.

Rotation
   An XYZ :term:`Euler` rotation built from the normal attribute for convenience. Such a value can also be
   built from the normal with the :doc:`/modeling/geometry_nodes/utilities/rotation/euler_to_rotation`.
   Keep in mind that the Z axis of the result rotation will be arbitrary, since the mesh normal used
   to create the rotation does not have enough information to set all three rotation axes.
