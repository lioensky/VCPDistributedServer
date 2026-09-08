.. index:: Modeling Modifiers; Geometry Nodes Modifier
.. _bpy.types.NodesModifier:

***********************
Geometry Nodes Modifier
***********************

The *Geometry Nodes* modifier creates a modifier with a node group which defines its functionality.

.. figure:: /images/modeling_modifiers_generate_geometry-nodes_panel.png

   A new Geometry Nodes modifier with a new node group.

This modifier is supported by mesh, curve, text, and volume objects.


Options
=======

Node Group
   A :doc:`Node Group </interface/controls/nodes/groups>` with the geometry input and output.
   Those are respectively what is received and passed to the previous and next modifier in the stack.
   See :doc:`Nodes </modeling/geometry_nodes/index>` for all available nodes.

Inputs
   A list of the node group's inputs which can have unique values even
   if the group is shared among multiple modifiers.

   .. _bpy.ops.object.geometry_nodes_input_attribute_toggle:

   If the input is connected to a :doc:`Field </modeling/geometry_nodes/fields>` socket,
   there will be a toggle to switch between using a single value for the input or
   using an attribute on the input geometry. Using an attribute for input means the
   value can be different for every element.

   The attribute name used by default when using the node group in a modifier for the first
   time is defined in the :doc:`node group inputs panel </interface/controls/nodes/groups>`.

   .. note::

      The :ref:`attribute domain <attribute-domains>` and the used to access the attribute is defined by the
      node the input is connected to.


.. _modifiers-geometry-nodes-warnings:

Warnings
--------

Nodes that show a warning message in the node editor will also show that message here.

Custom warning messages can be created using the :doc:`/modeling/geometry_nodes/output/warning`.


Output Attributes
-----------------

By connecting a field socket to the group output node,
you can create custom :doc:`Attributes </modeling/geometry_nodes/attributes_reference>`
from a :doc:`Field </modeling/geometry_nodes/fields>` output of any node in the node tree.
The domain of the attribute must be specified in the group node's output properties.
Note, this does not work with :doc:`Instanced Data </modeling/geometry_nodes/instances>`.

The attribute name used by default when using the node group in a modifier for the first
time is defined in the :doc:`node group outputs panel </interface/controls/nodes/groups>`.

This panel is hidden unless output node has attribute sockets.


.. _geometry_nodes-manage_panel:

Manage
------

Displays options for managing data within the node group,

.. _bpy.types.NodesModifier.show_manage_panel:

The *Manage* panel can be hidden by disabling *Show Manage Panel*
in the modifier's header options.
This controls whether the panel is shown for that specific modifier.

To disable the panel by default for new modifiers created from a node group asset,
toggle :ref:`bpy.types.GeometryNodeTree.show_modifier_manage_panel`
in the node group's properties.


Bake
^^^^

Bake Target
   Specifies where baked data should be stored. This can be overridden for individual bakes.

   :Packed:
      The baked data is packed into the .blend file. So no separate file is necessary.
   :Disk:
      The baked data is stored in a separate directory on disk.

.. _bpy.types.NodesModifier.bake_directory:

Bake Path
   Location on disk where the baked data for
   :doc:`Simulation Zones </modeling/geometry_nodes/simulation/simulation_zone>`
   and :doc:`Bake Nodes </modeling/geometry_nodes/geometry/operations/bake>` are stored.

.. seealso::

   :doc:`Geometry Node Baking </modeling/geometry_nodes/baking>`


.. _modifiers-geometry-nodes-named-attributes:

Named Attributes
^^^^^^^^^^^^^^^^

This panel displays information about all custom named attributes used by the node group.
More information is available in the
:ref:`geometry nodes inspection page <bpy.types.SpaceNodeOverlay.show_named_attributes>`.


.. _bpy.ops.object.geometry_nodes_move_to_nodes:

Move to Nodes Operator
======================

Creates a new geometry node tree with the name of the current node tree with ``.wrapper`` appended to the name.
This operation moves all inputs and outputs from the old modifier into a new node group.
In order for this operator to function, there **must** be a Group Input **and** a Group Output
each with a Geometry socket attached to the node group.
This action causes all *Output Attributes* to become *Internal Dependencies* utilizing the
:doc:`/modeling/geometry_nodes/attribute/store_named_attribute`.
All modifier "inputs" will then also become inputs of the newly created node group.

This operator is useful to easily allow a node tree to be reused in other trees
or to mark it as an :term:`Asset` to be reused in other projects.
