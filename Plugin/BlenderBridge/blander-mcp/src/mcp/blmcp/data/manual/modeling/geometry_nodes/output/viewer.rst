.. index:: Geometry Nodes; Viewer
.. _bpy.types.GeometryNodeViewer:

***********
Viewer Node
***********

.. figure:: /images/node-types_GeometryNodeViewer.webp
   :align: right
   :alt: The Viewer node.

The *Viewer* node allows viewing data from inside a geometry node group in both the
:doc:`Spreadsheet Editor </editors/spreadsheet>` and the 3D Viewport.

Any geometry or attribute connected to the viewer can be visualized in the viewport,
and its evaluated attribute values can be inspected in the spreadsheet.
Other data can also be viewed and inspected such as scaler values and grids by showing them in the spreadsheet.

.. note::

   The *Viewer* node cannot be used in the :ref:`Tool context <tool_context>`—only in the *Modifier* context.


Usage
=====

Activation and Deactivation
---------------------------

Use :kbd:`Shift-Ctrl-LMB` on any node or socket to connect it to the active viewer.

.. _bpy.types.SpaceView3D.show_viewer:

In the viewport *View* menu, the *Viewer Node* option can toggle the visibility of
all viewer visualizations, allowing you to compare the evaluated result with the final object output.


Keyboard Shortcuts
------------------

The Viewer node system provides shortcuts to quickly assign and activate viewers:

- **Assign Shortcut** (:kbd:`Ctrl-1`, :kbd:`Ctrl-2`, etc.):
  Select a viewer node and press a shortcut to assign it to that number.
  The assigned number appears in the upper-right corner of the node.
- **Activate Viewer** (:kbd:`1`, :kbd:`2`, etc.):
  Press the assigned number key to activate the corresponding viewer node.

.. note::

   Only number keys (:kbd:`1` - :kbd:`9`) are supported.


Viewing Single Socket Values
----------------------------

In addition to using the Viewer node, single-value sockets can display their evaluated values
directly within the node editor.
When enabled, the current evaluated value is shown beside the socket input, making it easy
to inspect and debug data flow without connecting a Viewer node.

This feature is available for scalar and small data types, such as *Float*, *Integer*, *Boolean*, or *Vector* sockets.
The displayed value updates interactively as the node tree evaluates or parameters change.

.. note::

   Complex data types such as geometry or grids cannot be previewed this way and must be visualized
   using the Viewer node or the Spreadsheet editor.


Attribute Field Visualization
-----------------------------

When the Viewer node has both a *Geometry* and a field input connected,
the values can be visualized directly in the 3D Viewport via the
:ref:`Viewer Overlay <3dview-overlays-view_node>`.

The attribute's :ref:`domain <attribute-domains>` is determined automatically when possible.
Otherwise, the Viewer defaults to the *Face Corner* domain for meshes and the *Point* domain for curves.
The domain can also be set manually from the node's properties.

In the Spreadsheet Editor, only the columns for attributes corresponding to the currently selected domain are shown.

.. important::

   The *Geometry* socket must be first.


Pinning
-------

The Viewer node can be *pinned* in the Spreadsheet Editor to keep its data visible even when it becomes inactive.
When pinned, the Spreadsheet continues showing the data from the pinned Viewer node,
regardless of changes to the active object or node selection.


Inputs
======

Inputs can be added by dragging a socket into the blank socket
or from the :ref:`bpy.types.NodeGeometryViewerItem` properties.


Properties
==========

Domain
   The :ref:`attribute domain <attribute-domains>` used to evaluate the *Value* input.
   The *Auto* option chooses the domain automatically based on the connected nodes.


.. _bpy.types.NodeGeometryViewerItem:

Viewer Items
------------

Socket Type
   The data type used to evaluate the input.
Auto Remove
   Remove the item automatically when it is unlinked.


Outputs
=======

This node has no outputs.


Examples
========

.. figure:: /images/modeling_geometry-nodes_viewer_example-1.jpg
   :align: center

   Visualizing the Noise Texture Factor on the default cube.

.. figure:: /images/modeling_geometry-nodes_viewer_example-2.jpg
   :align: center

   Visualizing the Index Attribute as text on the default cube.
