.. _bpy.types.Nodes:
.. _bpy.types.Node:
.. _bpy.ops.node:
.. index:: Nodes

#########
  Nodes
#########

Blender contains different node-based editors with different purposes,
so this section only explains how to work with nodes in general.
The list below shows the different types of nodes and where they're documented.

.. figure:: /images/interface_controls_nodes_introduction_example.jpg

   Example of a node editor.

.. _tab-node-tree-types:

.. list-table::
   :header-rows: 1
   :class: valign
   :widths: 10 30 60

   * - Icon
     - Name
     - Description
   * - .. rubric:: :bl-icon:`geometry_nodes`
     - :doc:`Geometry Nodes </modeling/geometry_nodes/index>`
     - Used for procedural modeling.
   * - .. rubric:: :bl-icon:`node_material`
     - :doc:`Shader Nodes </render/shader_nodes/index>`
     - Used to create materials for objects.
   * - .. rubric:: :bl-icon:`node_compositing`
     - :doc:`Composite Nodes </compositing/index>`
     - Used to edit rendered images.
   * - .. rubric:: :bl-icon:`node_texture`
     - :doc:`Texture Nodes </editors/texture_node/introduction>`
     - Used to create custom textures.

.. toctree::
   :maxdepth: 2

   node_editors.rst
   parts.rst
   Selecting <selecting.rst>
   arranging.rst
   Editing <editing.rst>
   types/index.rst
   groups.rst
