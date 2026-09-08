.. index:: Geometry Nodes; Tools
.. _bpy.types.GeometryNodeTree:

****************
Node-Based Tools
****************

Geometry :doc:`node groups </interface/controls/nodes/groups>` can not just be applied to
an object using a modifier. It's also possible to turn them into tools that can be invoked
from the Blender menu.

You can create such tools in the :ref:`tool_context`, after which they appear in the
*Non-Assets* menu of the 3D Viewport. If you want to move them to a different menu,
reuse them in other blend-files, or share them with someone else, you need to turn
them into an asset as described below.

.. figure:: /images/modeling_geometry-nodes_tools.png
   :align: center

   Node group tools integrated in the Curves menu.


.. _tool_context:

Tool Context
============

Because tool node groups have different settings than modifier node groups, you need to change
the :ref:`bpy.types.SpaceNodeEditor.node_tree_sub_type` in the Geometry Node Editor's header
to *Tool* in order to edit them.

When this type is selected, the :ref:`data-block menu <ui-data-block>` in the editor's
header will only show the node groups that have the
:ref:`Tool Usage <bpy.types.GeometryNodeTree.is_tool>` enabled.

- If you create a new node group while in the *Tool* editor type, the *Tool* Usage will be
  enabled automatically.
- If you want to convert an existing modifier node group, you need to manually enable the
  *Tool* Usage in the Sidebar (and optionally disable the *Modifier* Usage) before switching
  to the *Tool* editor type. Also make sure to set up the :ref:`modeling-geometry_nodes-tools_contexts`.

.. note::

   The :doc:`inspection </modeling/geometry_nodes/inspection>`
   features are not supported in the *Tool* context.


Asset
=====

If you want to move a tool into a menu of your choice, reuse it in other blend-files,
or share it with other people, you need to turn it into an
:doc:`asset </files/asset_libraries/introduction>`. Simply right-click the node group name
in the Geometry Node Editor's header and choose *Mark as Asset*.

Once this is done, the node group will appear in the :doc:`Asset Browser </editors/asset_browser>`'s
*Unassigned* :doc:`catalog </files/asset_libraries/catalogs>`. You can then move it into a catalog
named after a menu to make it appear at the end of that menu.

Finally, you can save the blend-file as an :ref:`asset bundle <asset-bundles>` and copy it into
an asset library (described on linked page). From then on, the tool will be available in any
blend-file you work with. You can also share the asset bundle file with others.


Tool Settings
=============

If your tool requires any input from the user apart from the geometry to transform,
you can :ref:`add sockets <bpy.ops.node.interface_item_new>` to the *Group Input* node.
These will be exposed in the :ref:`bpy.ops.screen.redo_last` panel when running the tool.


.. _modeling-geometry_nodes-tools_contexts:

Supported Modes & Object Types
==============================

Node groups must specify which modes and object types they support.
This can be configured using the popover menus in the header of the
:ref:`Geometry Node Editor <editors-geometry_nodes-tool_context>`.

.. important::

   For mesh objects, :doc:`shape keys </animation/shape_keys/introduction>` are not supported.
   They will be removed if you run a node tool on the object.


Tool-specific Nodes
===================

The following nodes are only supported in the *Tool* context:

- :doc:`/modeling/geometry_nodes/input/scene/3d_cursor`
- :doc:`/modeling/geometry_nodes/input/scene/mouse_position`
- :doc:`/modeling/geometry_nodes/input/scene/viewport_transform`
- :doc:`/modeling/geometry_nodes/geometry/read/active_element`
- :doc:`/modeling/geometry_nodes/geometry/read/selection`
- :doc:`/modeling/geometry_nodes/geometry/write/set_selection`
- :doc:`/modeling/geometry_nodes/mesh/read/face_set`
- :doc:`/modeling/geometry_nodes/mesh/write/set_face_set`

.. note::

   The :doc:`Self Object </modeling/geometry_nodes/input/scene/self_object>`
   node returns the Active object when inside a *Tool* node group.


Non-supported Nodes
===================

These nodes are only supported in the *Modifier* context:

- :doc:`/modeling/geometry_nodes/simulation/simulation_zone`
- :doc:`/modeling/geometry_nodes/output/viewer`
