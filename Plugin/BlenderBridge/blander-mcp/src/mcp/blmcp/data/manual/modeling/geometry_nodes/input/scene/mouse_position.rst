.. index:: Geometry Nodes; Mouse Position
.. _bpy.types.GeometryNodeToolMousePosition:

*******************
Mouse Position Node
*******************

.. figure:: /images/node-types_GeometryNodeToolMousePosition.webp
   :align: right
   :alt: Mouse Position node.

The *Mouse Position* node returns information about the mouse cursor
such as its position and the :doc:`region's </interface/window_system/regions>` dimensions.

.. tip::

   When using this node, enable :ref:`Wait for Click <bpy.types.GeometryNodeTree.use_wait_for_click>`.
   to wait for a mouse click input (:kbd:`LMB`) before running the operator from a menu.

.. note::

   This node can only be used in the :ref:`Tool context <tool_context>`.


Inputs
======

This node has no inputs.


Outputs
=======

Mouse X
   The region-space mouse X location, in pixels, increasing from 0 at the left.
Mouse Y
   The region-space mouse Y location, in pixels, increasing from 0 at the bottom.
Region Width
   The total X size of the :doc:`region </interface/window_system/regions>` in pixels.
Region Height
   The total Y size of the :doc:`region </interface/window_system/regions>` in pixels.
