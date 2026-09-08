.. index:: Geometry Nodes; Menu Switch
.. _bpy.types.GeometryNodeMenuSwitch:
.. --- copy below this line ---

****************
Menu Switch Node
****************

.. figure:: /images/node-types_GeometryNodeMenuSwitch.webp
   :align: right
   :alt: Menu Switch Node.

The *Menu Switch* node outputs one of its inputs based on a selected menu item.
Only the active input is evaluated, allowing efficient switching between multiple options.

The available menu entries are defined by the user. Menu items can be
added and removed, as well as renamed and reordered in the editor side
bar. Renaming a menu entry keeps existing links of the matching input
socket.

The menu can be used in node groups and the nodes modifier UI.
Connecting the menu input with a *Group Input* node will expose the menu
as a group input. A menu socket in a node group, reroute node, or other
pass-through nodes needs to be connected to a *Menu Switch* node in
order to work. An unconnected menu socket will show an empty menu by
default.

Connecting multiple *Menu Switch* nodes to the same output
socket creates a conflict (even when the menu entries are the same).
To avoid this a menu switch can be wrapped in a node group. Multiple
node groups of the same type can be connected to the same menu, since
they contain the same menu switch node.

.. list-table::

   * - .. figure:: /images/node-types_GeometryNodeMenuSwitch_conflict.png

          Conflict caused by connecting different menus.

     - .. figure:: /images/node-types_GeometryNodeMenuSwitch_group_wrapper.png

          Same node group can be connected without conflict.


.. seealso::

   The :doc:`/modeling/geometry_nodes/utilities/index_switch`
   is similar but it exposes the choices as an integer index.


Inputs
======

Menu
   Determines which input socket is passed through to the output.

One input is created for each menu entry. The input corresponding to the selected menu item
is evaluated and passed through.

Menu item labels can be renamed using :kbd:`Ctrl-LMB` on the socket name or in the node's *Properties* panel.

Additional input sockets can be added by:
- Dragging a connection onto the empty socket at the bottom of the list.
- Clicking the :bl-icon:`add` icon in the node header.

Unused inputs are not computed, improving performance in complex node networks.


Properties
==========

Type
   Determines the type of the data that is handled by the node.


Outputs
=======

Output
   Outputs the value from the input corresponding to the selected menu item, unchanged.

For each menu entry, an additional Boolean output is created.
The output corresponding to the selected item is *true*, and all others are *false*.
These Boolean outputs can be used to trigger different node branches, control visibility,
or drive conditional operations elsewhere in the node tree.
