.. index:: Compositor Nodes; Group Input

****************
Group Input Node
****************

.. figure:: /images/node-types_NodeGroupInput.webp
   :align: right
   :alt: Group Input Node.

The *Group Input* node provides access to input sockets of a node group.
It acts as the entry point for data passed into the group from the outside,
such as images, values, or other data types.

Additional input sockets can be added or removed from the *Group Input* node
through the *Group* panel in the Sidebar or by using the group interface editor
in the Node Editor header. When the node group is used in another compositor tree,
the sockets defined in *Group Input* appear as input sockets on the *Group* node itself.


Inputs
======

This node has no inputs.


Properties
==========

See :ref:`nodes-groups-properties-sockets`.


Outputs
=======

Image
   The default image input for the node group, available when the group is created.
   It can be used to feed images or render layers into the group.

Any additional inputs defined in the node group's interface will appear here as output sockets.
