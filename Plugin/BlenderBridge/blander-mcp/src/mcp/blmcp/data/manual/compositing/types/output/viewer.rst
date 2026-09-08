.. index:: Compositor Nodes; Viewer
.. _bpy.types.CompositorNodeViewer:

***********
Viewer Node
***********

.. figure:: /images/node-types_CompositorNodeViewer.webp
   :align: right
   :alt: Viewer Node.

The *Viewer* node is used to preview image data or value maps anywhere within a compositor node graph.
It is a diagnostic tool that allows users to inspect intermediate results without affecting the final output.

You can quickly assign a node to a Viewer by pressing :kbd:`Shift-Ctrl-LMB` on the desired node.
To switch between multiple Viewer nodes, simply select one with :kbd:`LMB`.
Only the active Viewer node (with the :bl-icon:`restrict_view_off` icon in the header)
will be displayed in the backdrop or Image Editor.


Inputs
======

Image
   Outputs the result of this input directly to the viewer result.
   If this socket is left unconnected, the output will be a black image.


Outputs
=======

This node has no output sockets.


Usage
=====

.. _bpy.ops.node.viewer_shortcut_set:
.. _bpy.ops.node.viewer_shortcut_get:

Keyboard Shortcuts
------------------

Viewer node provide a quick way to toggle between different viewer nodes while compositing using keyboard shortcuts,
improving workflow efficiency when comparing outputs.

- **Assign Shortcut** (:kbd:`Ctrl-1`, :kbd:`Ctrl-2`, etc.):
  Select a node and press a shortcut to assign it. If no Viewer node is attached, one is created and activated.
  The number will be shown in the upper right part of the node to identify which shortcut is assigned.
- **Activate Node** (:kbd:`1`, :kbd:`2`, etc.):
  Press the assigned number key to activate the node's Viewer output.

.. note:: Only number keys (`1-9`) are supported.


Using the Image Editor
----------------------

The Viewer node allows results to be displayed in the Image Editor.
The image is facilitated in the header by selecting *Viewer Node* in the linked *Image* data-block menu.
The Image Editor will display the image from the currently selected Viewer node.

To save the image being viewed,
use :menuselection:`Image --> Save As...`, :kbd:`Alt-S` to save the image to a file.

The Image Editor also has three additional options in its header to view Images with or
without Alpha, or to view the Alpha or Z itself.
Click and holding the mouse in the Image displayed allows you to sample the values.

.. seealso::

   For overlays specific to the Viewer node (such as text info and render guides),
   see :ref:`Guides Overlays <editors-image-overlays-guides>`.
