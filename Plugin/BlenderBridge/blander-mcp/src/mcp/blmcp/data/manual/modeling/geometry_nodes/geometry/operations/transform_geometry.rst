.. index:: Geometry Nodes; Transform Geometry
.. _bpy.types.GeometryNodeTransform:

***********************
Transform Geometry Node
***********************

.. figure:: /images/node-types_GeometryNodeTransform.webp
   :align: right
   :alt: Transform Geometry node.
   :width: 190px

The *Transform Geometry Node* allows you to move, rotate or scale the geometry.
The transformation is applied to the entire geometry, and not per element.
The :doc:`/modeling/geometry_nodes/geometry/write/set_position` is used for moving
individual points of a geometry. For transforming instances individually, the instance
:doc:`translate </modeling/geometry_nodes/instances/translate_instances>`,
:doc:`rotate </modeling/geometry_nodes/instances/rotate_instances>`, or
:doc:`scale </modeling/geometry_nodes/instances/scale_instances>` nodes can be used.


Inputs
======

Geometry
   Standard geometry input.

Mode
   How the transformation is specified.

   :Components: Provide separate inputs for location, rotation and scale.
   :Matrix: Use a transformation matrix.

Translation
   Translation of the entire geometry in the local space of the modified object.

Rotation
   Euler rotation in the local space of the modified object.

Scale
   Scale for the geometry in the local space of the modified object.

Transform
   A :term:`Transformation Matrix`, available when using *Matrix* mode.


Output
======

Geometry
   Standard geometry output.
