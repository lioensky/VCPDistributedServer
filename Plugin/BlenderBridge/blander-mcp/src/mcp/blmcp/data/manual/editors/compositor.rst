.. index:: Editors; Compositor

**********
Compositor
**********

The Compositor lets you manage :doc:`nodes </interface/controls/nodes/index>`
for compositing.

.. figure:: /images/compositing_types_distort_map-uv_example-2.png

   Nodes in the Compositor.

The use of the Compositor is explained in :doc:`/compositing/index`.


Interface
=========

Header
------

.. _bpy.ops.node.new_compositing_node_group:

Node Tree
   Chooses which node group (compositor node tree) to display and edit.
   Each :doc:`Scene </scene_layout/scene/index>` can have its own compositor node tree.
   You can also create and switch to custom node groups for reuse.

:bl-icon:`pinned` Pinned
   When enabled, the editor always displays the selected node tree, regardless of the active scene.
   This is useful when working with multiple scenes but wanting to keep the compositor focused on one node tree.


.. _bpy.types.SpaceNodeEditor.show_gizmo:

Gizmos
^^^^^^

Controls the display of gizmos in the Compositor.

Clicking :bl-icon:`gizmo` (Show Gizmos) toggles all gizmos in the Compositor
The drop-down button displays a popover with more detailed settings,
which are described below.

.. rubric:: Viewport Gizmos

.. _bpy.types.SpaceNodeEditor.show_gizmo_active_node:

Active Node
   Display a context-sensitive gizmo for the currently selected node.
   This may include transform controls or other visual aids depending on the node type.


Asset Shelf
-----------

The *Asset Shelf* provides quick access to compositor node assets, allowing users to drag and drop
predefined node setups directly into the compositor workspace.
Any node group marked as an asset will appear here automatically.

Located at the bottom of the editor, the shelf offers a compact and easily accessible interface for
inserting and organizing compositor assets. Compared to the
:doc:`Asset Browser </editors/asset_browser>`, it integrates more seamlessly into the
compositing workflow and can be shown or hidden as needed.

The Asset Shelf helps users:

- Quickly build node setups using reusable assets.
- Explore common compositing techniques and effects.
- Work entirely within Blender for post-processing.

The Asset Shelf can be toggled on or off from the compositor editor's header.
