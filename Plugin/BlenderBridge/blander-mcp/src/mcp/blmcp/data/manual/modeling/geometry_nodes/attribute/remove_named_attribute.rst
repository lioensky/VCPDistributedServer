.. index:: Geometry Nodes; Remove Named Attribute
.. _bpy.types.GeometryNodeRemoveAttribute:

***************************
Remove Named Attribute Node
***************************

.. figure:: /images/node-types_GeometryNodeRemoveAttribute.webp
   :align: right
   :alt: Remove Named Attribute node.

The *Remove Named Attribute* node deletes an attribute with a certain name from its geometry input.
Any attribute that exists on geometry data will be automatically propagated when the geometry storing it
is changed, which can be an expensive operation, so using this node can be a simple way to optimize
the performance of a geometry node tree or even to lower the memory usage of the entire scene.

Almost all named attributes can be removed. For certain :ref:`geometry-nodes_builtin-attributes`,
removing it will mean that a default value will be used instead. For example, removing the
:doc:`cyclic </modeling/geometry_nodes/curve/read/is_spline_cyclic>` attribute on curves means that
all curves will be non-cyclic.


Inputs
======

Geometry
   Standard geometry input.

Pattern Mode
   How the attributes to remove are chosen.

   :Exact: Remove the one attribute with the given name.
   :Wildcard: Remove all attributes that match the pattern which is allowed to contain a single wildcard (*).

Name
   The name of the attribute to remove.


Outputs
=======

Geometry
   Standard geometry output.
