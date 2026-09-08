.. index:: Geometry Nodes; ID
.. _bpy.types.GeometryNodeInputID:

*******
ID Node
*******

.. figure:: /images/node-types_GeometryNodeInputID.webp
   :align: right
   :alt: ID node.

The *ID* node gives an integer value indicating the stable random identifier of each element on the point domain,
which is stored in the ``id`` attribute.

The node to set this data is the :doc:`/modeling/geometry_nodes/geometry/write/set_id` node.

.. note::

   Unlike other built-in attributes, the ``id`` attribute does not always exist.
   In that case, this node will output the :doc:`index </modeling/geometry_nodes/geometry/read/input_index>`.


Inputs
======

This node has no inputs.


Outputs
=======

ID
   Integer value.
