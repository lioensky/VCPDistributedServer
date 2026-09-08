
*************
Editing Nodes
*************

.. _nodes-editing-transform:

Transform
=========

.. reference::

   :Menu:      :menuselection:`Node --> Move, Rotate, Resize`
   :Shortcut:  :kbd:`G`, :kbd:`R`, :kbd:`S`

You can move the selected node(s) by clicking and dragging any empty part of them.
Alternatively, press :kbd:`G`, move the mouse, and click :kbd:`LMB` to confirm.

Dragging a node on top of an existing link will intelligently insert the selected node into the link path.
This generally uses the first socket that matches the link type.
The automatic node attachment feature can be toggled with :kbd:`Alt`.
When a node is automatically attached, the surrounding nodes
will be offset to the right or left depending on the :kbd:`T` toggle;
see :ref:`editors-nodes-usage-auto-offset` for more information.

While dragging nodes, you can press :kbd:`F` to toggle their parent 
:doc:`Frame </interface/controls/nodes/types/layout/frame>`:

- If the nodes are inside a frame, they will be detached from it.
- If the nodes are not inside a frame and there is a frame under the cursor, they will be attached to that frame.

In general, it is recommended to arrange your nodes so that data flows from left to right, top to bottom.

The width of a node can be changed by dragging its left or right border.

Rotating (:kbd:`R`) and scaling (:kbd:`S`) only apply when multiple nodes are selected,
and only affect their positions.


Connecting Sockets
==================

:kbd:`LMB`-click on a socket and drag. "Connect to Output" will see a line coming out of it; this is called a *link*.
Keep dragging and connect the link to an input socket of another node, then release the :kbd:`LMB`.

While multiple links can route out of an output socket, typically a single link can be attached to an input socket,
that is unless the input is a multi-socket input with looks like a pill shaped socket.

To swap multiple links of a similar type, press and hold :kbd:`Alt` while moving a link.
This feature also works when adding a new link into a pre-existing socket.

To reposition the outgoing links of a node, rather than adding a new one,
hold :kbd:`Ctrl` while dragging from an output socket.
This works for single as well as for multiple outgoing links.

Nodes that have no connections can be inserted on a link
by just move the node over the link and release when the link is highlighted.

.. _bpy.ops.node.link_make:

Make Links :kbd:`J`
   Select multiple nodes with open sockets, then use the Make Links to create links between them.
   Use Make Links again if there are other nodes which can be connected.

Make and Replace Links :kbd:`Shift-J`
   *Make and Replace Links* works similarly to *Make Links*, but it will replace existing links if any exist.


Disconnecting Sockets
=====================

Interactively
-------------

Drag the link away from its input socket and let it go, keeping it unconnected.


.. _bpy.ops.node.links_mute:

Mute Links
----------

.. reference::

   :Menu:      :menuselection:`Node --> Mute Links`
   :Shortcut:  :kbd:`Ctrl-Alt-RMB`

Activate the menu item or hold the key combination,
then draw a line across one or more links to mute/unmute them.
A muted link acts as though it's no longer there; this also means the input fields
for specifying fixed values become visible again.

When muting links on the input side of a :doc:`reroute node </interface/controls/nodes/types/layout/reroute>`,
the links on its output side will be muted too.

.. figure:: /images/interface_controls_nodes_editing_mute_links.png


.. _bpy.ops.node.links_cut:

Cut Links
---------

.. reference::

   :Menu:      :menuselection:`Node --> Cut Links`
   :Shortcut:  :kbd:`Ctrl-RMB`

Activate the menu item or hold the key combination,
then draw a line across one or more links to delete them.

.. note::

   The key combination is normally reserved for :doc:`Lasso Select </interface/selecting>`.
   In node editors, lasso selection is instead performed with :kbd:`Ctrl-Alt-LMB`.


.. _bpy.ops.node.move_detach_links:

Detach Links :kbd:`Alt-LMB` drag
   Use Detach Links to cut all the links attached to the selected nodes
   and move the nodes to a new location.


.. _bpy.ops.node.clipboard_copy:
.. _bpy.ops.node.clipboard_paste:

Copy/Paste
==========

.. reference::

   :Menu:      :menuselection:`Node --> Copy`, :menuselection:`Node --> Paste`
   :Shortcut:  :kbd:`Ctrl-C`, :kbd:`Ctrl-V`

Not only the selected nodes but also the connections between them are copied to the clipboard.

.. note::

   The pasted node will be placed in the *same* position as when it was copied.
   Use the same cautions as when duplicating.


.. _bpy.ops.node.duplicate_move:

Duplicate
=========

.. reference::

   :Menu:      :menuselection:`Node --> Duplicate`
   :Shortcut:  :kbd:`Shift-D`

Select one or more nodes, activate the menu item or press the key combination,
then move the mouse to a new location and click :kbd:`LMB` (or press :kbd:`Return`)
to place the duplicated node(s).

.. note::

   When you duplicate a node, the new node will be positioned *exactly* on top of the node that was duplicated.
   If you leave it there (and it is quite easy to do so),
   you can **not** easily tell that there are *two* nodes there!
   When in doubt, select a node and move it slightly to see if something is hidden underneath.


.. _bpy.ops.node.duplicate_move_linked:

Duplicate Linked
================

.. reference::

   :Menu:      :menuselection:`Node --> Duplicate Linked`
   :Shortcut:  :kbd:`Alt-D`

Duplicate selected nodes, but not their node trees (in the case of group nodes), and move them.


.. _bpy.ops.node.delete:

Delete
======

.. reference::

   :Menu:      :menuselection:`Node --> Delete`
   :Shortcut:  :kbd:`X`, :kbd:`Delete`

Deletes the selected node(s).


.. _bpy.ops.node.delete_reconnect:

Delete with Reconnect
=====================

.. reference::

   :Menu:      :menuselection:`Node --> Delete`
   :Shortcut:  :kbd:`Ctrl-X`

Deletes the selected node(s), then creates new links connecting their former input nodes
to their former output nodes.


.. _bpy.ops.node.swap_node:

Swap
====

.. reference::

   :Menu:      :menuselection:`Node --> Swap`
   :Shortcut:  :kbd:`Shift-S`

The *Swap* operator replaces the selected node with another node type chosen from the menu.

All existing links are automatically reconnected where possible,
matching input and output sockets by name and type.
If a connection cannot be matched, it is left unconnected.


Show/Hide
=========

.. _bpy.ops.node.mute_toggle:

Mute
----

.. reference::

   :Menu:      :menuselection:`Node --> Show/Hide --> Mute`
   :Shortcut:  :kbd:`M`

Muting a node removes its contribution to the node tree,
and makes all links pass through it without change.
Links will appear red as an indicator of passing through the muted node.

.. tip::

   Individual node links can be muted with :ref:`bpy.ops.node.links_mute`.


.. _bpy.ops.node.preview_toggle:

Node Preview
------------

.. reference::

   :Menu:      :menuselection:`Node --> Show/Hide --> Node Preview`
   :Shortcut:  :kbd:`Shift-H`

Shows/Hides a preview region on the node that displays the frame
after that node's operation has been applied. This can also be toggled
by clicking the material ball icon in the node header.

.. note:: This operator are only available in the :doc:`Compositor </compositing/index>`.


.. _bpy.ops.node.options_toggle:

Node Options
------------

.. reference::

   :Menu:      :menuselection:`Node --> Show/Hide --> Node Options`

Shows/Hides all node properties.


.. _bpy.ops.node.hide_socket_toggle:

Unconnected Sockets
-------------------

.. reference::

   :Menu:      :menuselection:`Node --> Show/Hide --> Unconnected Sockets`
   :Shortcut:  :kbd:`Ctrl-H`

Collapses/Expands any input or output sockets that have no other nodes connected to them.


.. _bpy.ops.node.hide_toggle:

Collapse
--------

.. reference::

   :Menu:      :menuselection:`Node --> Show/Hide --> Unconnected Sockets`
   :Shortcut:  :kbd:`H`

Collapses the node so only the node header is visible.
This can also be toggled by clicking the triangle on the left of the node header.


.. _bpy.ops.node.collapse_hide_unused_toggle:

Collapse and Hide Unused Sockets
--------------------------------

.. reference::

   :Menu:      :menuselection:`Node --> Show/Hide --> Unconnected Sockets`
   :Shortcut:  :kbd:`H`

Applies both the :ref:`bpy.ops.node.hide_socket_toggle` and :ref:`bpy.ops.node.hide_toggle` operations.


.. _bpy.ops.node.read_viewlayers:

Read View Layers
================

.. reference::

   :Menu:      :menuselection:`Node --> Read View Layers`
   :Shortcut:  :kbd:`Ctrl-R`

Reads all the current scene's render layers from cache, as needed.
This can be used to save RAM while rendering because the render layers do not have to be saved in RAM.
And also for recovering some information from a failed render.
For this to work, :ref:`Cache Result <bpy.types.RenderSettings.use_render_cache>` must be enabled.

.. note:: This operator are only available in the :doc:`Compositor </compositing/index>`.


.. _bpy.ops.node.connect_to_output:

Connect to Output
=================

.. reference::

   :Shortcut:  :kbd:`Shift-Alt-LMB`

Connect the output of the selected node to the final output of the node tree
(Material Output or World Output in Shader,
the final Group Output in Geometry Nodes and Compositor, Output in Texture Nodes),
or, if the node is inside a group, to the Group Output.
