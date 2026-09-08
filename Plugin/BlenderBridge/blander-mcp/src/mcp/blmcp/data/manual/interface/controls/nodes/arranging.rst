
***************
Arranging Nodes
***************

Snapping
========

.. _bpy.types.ToolSettings.use_snap_node:

Snapping aligns the position and size of nodes to the background grid.
This feature allows nodes to snap to a grid, ensuring that node layouts remain clean and visually aligned.
Snapping can be toggling the snap icon (:bl-icon:`snap_off`/:bl-icon:`snap_on`) in the editor's headers
or toggled temporarily while :ref:`transforming <nodes-editing-transform>` nodes by holding :kbd:`Ctrl`.


.. _editors-nodes-usage-auto-offset:

Auto-Offset
===========

When you drop a node with at least one input and one output socket onto an existing connection between two nodes,
*Auto-offset* will, depending on the direction setting, automatically move the left or right node away to make room
for the new node.
*Auto-offset* is a feature that helps organizing node layouts interactively without interrupting the user workflow.

.. figure:: /images/interface_controls_nodes_arranging_auto-offset.png

Auto-offset is enabled by default,
but it can be disabled in the :ref:`Preferences <preferences-editing-node-editor>`.

You can toggle the offset direction while you are moving the node by pressing :kbd:`T`.

The offset margin can be changed using the *Auto-offset Margin*
setting in the Editing section of the Preferences.

.. admonition:: Example Video
   :class: seealso

   `Auto-Offset. A workflow enhancement for Blender's node editors <https://vimeo.com/135125839>`__.
