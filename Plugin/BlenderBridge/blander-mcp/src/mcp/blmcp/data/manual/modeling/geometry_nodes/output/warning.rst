.. index:: Geometry Nodes; Warning
.. _bpy.types.GeometryNodeWarning:

************
Warning Node
************

.. figure:: /images/node-types_GeometryNodeWarning.webp
   :align: right
   :alt: Warning Node.

Outputs a custom message that is displayed in the
:ref:`modifiers-geometry-nodes-warnings` panel of the Geometry Nodes modifier.

This allows node groups to communicate expectations, assumptions, or error conditions
about input values, such as required ranges, missing data, or unsupported configurations.

By default, warnings are propagated through all parent node groups.
This behavior can be controlled using the
:ref:`bpy.types.Node.warning_propagation` setting on each node.


Inputs
======

Show
   Controls whether the warning is shown in the
   :ref:`modifiers-geometry-nodes-warnings` panel.
   When disabled, the warning is suppressed.

Message
   The text message to display.
   This can be used to describe incorrect inputs, required conditions,
   or other relevant information for users of the node group.


Properties
==========

Warning Type
   The severity of the message, which also affects the icon shown in the warnings panel.

   :Info:
      Informational message that does not indicate a problem.
   :Warning:
      Indicates a potential issue that may produce unexpected results.
   :Error:
      Indicates an invalid configuration that is likely to produce incorrect results.


Outputs
=======

Show
   Passthrough of the *Show* input, allowing the warning state to be forwarded
   to other nodes.
