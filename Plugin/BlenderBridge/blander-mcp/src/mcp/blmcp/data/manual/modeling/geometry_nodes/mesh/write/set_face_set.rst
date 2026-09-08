.. index:: Geometry Nodes; Set Face Set
.. _bpy.types.GeometryNodeToolSetFaceSet:

*****************
Set Face Set Node
*****************

.. figure:: /images/node-types_GeometryNodeToolSetFaceSet.webp
   :align: right
   :alt: Set Face Set node.

The *Set Face Set* node controls which :ref:`face set <face_sets>` that faces are in.

The input node for this data is the :doc:`/modeling/geometry_nodes/mesh/read/face_set`.

.. note::

   This node can only be used in the :ref:`Tool context <tool_context>`.


Inputs
======

Mesh
   Standard geometry input.

Selection
   Boolean field that controls which faces will have the Face Set value applied.

Face Set
   Integer field for specifying which face set each selected face should be moved to.
   Ignored for faces where the value of Selection is false.


Outputs
=======

Mesh
   Standard geometry output.
