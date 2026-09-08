
************
Introduction
************

Geometry Nodes is a system for modifying the geometry of an object with node-based operations.
It can be accessed by adding a :doc:`Geometry Nodes Modifier </modeling/modifiers/geometry_nodes>`
and setting up the nodes in the :doc:`/editors/geometry_node`.

.. figure:: /images/modeling_geometry-nodes_introduction_properties.png

   The properties of a Geometry Nodes modifier in the modifier stack.

The geometry node tree connected to a modifier is a :doc:`Node Group </interface/controls/nodes/groups>`.
The geometry from the state before the modifier (the original geometry or the result of the previous
modifier) will be passed to the *Group Input* node. Then the node group can operate on the geometry
and pass an output to the *Group Output* node, where it will be passed to the next modifier.

Geometry nodes can modify different types of geometry:

- :doc:`Meshes </modeling/meshes/introduction>`
- :doc:`Curves </modeling/curves/introduction>`
- :doc:`Point Clouds </modeling/point_cloud/index>`
- :doc:`Volumes </modeling/volumes/introduction>`
- :doc:`Instances </modeling/geometry_nodes/instances>`

The interface of the modifier is described in the
:doc:`Modifier </modeling/modifiers/geometry_nodes>` page.

To expand Blender with node-group operators, see the :doc:`/modeling/geometry_nodes/tools` page.
