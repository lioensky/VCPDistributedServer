.. index:: Geometry Nodes; Self Object
.. _bpy.types.GeometryNodeSelfObject:

****************
Self Object Node
****************

.. figure:: /images/node-types_GeometryNodeSelfObject.webp
   :align: right
   :alt: Self Object node.

The *Self Object* node outputs the object that contains the geometry nodes modifier
currently being executed. This can be used to retrieve the original transforms.

When evaluated in the :ref:`Tool context <tool_context>`, this node returns the Active object.

.. note::

   The geometry cannot be retrieved from this object with the
   :doc:`/modeling/geometry_nodes/input/scene/object_info`, since its final geometry is still
   being evaluated.


Inputs
======

This node has no inputs.


Outputs
=======

Self Object
   The object currently being evaluated.
