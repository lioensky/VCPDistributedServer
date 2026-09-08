.. index:: Compositor Nodes; Group Output

************
Group Output
************

.. figure:: /images/node-types_NodeGroupOutput.webp
   :align: right
   :alt: Group Output Node.

The *Group Output* node defines the final output of a node group.
It determines which values are passed out of the node group to the parent node tree
(or to the renderer, in the case of the Compositor).

In the Compositor, this node defines the image result that is sent to the renderer or to
image output after rendering.

This node is updated automatically after each evaluation or render,
and updates interactively when connected inputs are changed—provided that all inputs are fully evaluated.

.. note::

   If multiple *Group Output* nodes are present in a node tree, only the **active** one is used.
   All others will show a "Unused Output" warning.
   The active output can be changed in the *header* of the node.


Inputs
======

By default, the node has no input sockets.
Sockets appear when outputs are defined for the node group in the *Group* tab of the sidebar
(or when dragging a connection onto the blank socket area).

Each input corresponds to a group output socket that can be exposed to the parent node tree.

.. note::

   In the Compositor, only the first image input is used as the final render result.
   Any additional sockets will be ignored.


Properties
==========

See :ref:`nodes-groups-properties-sockets`.


Outputs
=======

This node has no output sockets.
Its sole purpose is to define which values leave the node group.
