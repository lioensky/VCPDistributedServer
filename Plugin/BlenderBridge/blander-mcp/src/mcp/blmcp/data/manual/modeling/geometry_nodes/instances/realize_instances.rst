.. index:: Geometry Nodes; Realize Instances
.. _bpy.types.GeometryNodeRealizeInstances:

**********************
Realize Instances Node
**********************

.. figure:: /images/node-types_GeometryNodeRealizeInstances.webp
   :align: right
   :alt: Realize Instances node.

The *Realize Instances* node makes any instances (efficient duplicates of the same geometry)
into real geometry data. This makes it possible to affect each instance individually,
whereas without this node, the exact same changes are applied to every instance of
the same geometry. However, performance can become much worse when the input
contains many instances of complex geometry, which is a fundamental limitation
when procedurally processing geometry.

.. note::

   If the input contains multiple volume instances, only the first volume component is moved to the output.


.. editors note: keep up to date with :doc:`/modeling/geometry_nodes/geometry/join_geometry`

Attributes
==========

When merging attributes from multiple geometry inputs, the highest complexity data type is chosen
for the output attribute. For example, if a ``weight`` attribute is a Boolean on one geometry input
and a vector on another, the ``weight`` attribute on the output geometry will use the vector data type.

Named and anonymous attributes are propagated from the :ref:`instance domain <attribute-domains>`
to the realized geometry. If an attribute exists both on the base geometry and on an instance,
the attribute values from the base geometry take precedence.

.. note::

   - The ``id`` attribute receives special handling to prevent duplicate values. ``id`` values or indices
     of each instance are combined with ``id`` values from the geometry data points.
   - Vertex groups are preserved when realizing instances or joining geometries.
     If the domain and type propagation rules above result with the vertex domain and float type,
     then an attribute will be a vertex group on the output mesh.


Inputs
======

Geometry
   Standard geometry input.
Selection
   Which top-level instances to realize.
Realize All
   Realize all levels of nested instances for each top-level instances
   (overrides the value of the *Depth* input).
Depth
   Number of levels of nested instances to realize for each top-level instance.


Outputs
=======

Geometry
   Standard geometry output.
