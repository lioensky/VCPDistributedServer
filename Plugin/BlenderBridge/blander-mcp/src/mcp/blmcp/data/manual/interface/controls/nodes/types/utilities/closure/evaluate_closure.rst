.. index:: Nodes; Evaluate Closure
.. _bpy.types.NodeEvaluateClosure:
.. --- copy below this line ---

****************
Evaluate Closure
****************

.. figure:: /images/node-types_NodeEvaluateClosure.webp
   :align: right
   :alt: Evaluate Closure Node

The *Evaluate Closure* node executes a connected
:doc:`Closure Zone </interface/controls/nodes/types/utilities/closure/closure>`.
It acts as the *call site* of the closure, running its internal node graph and returning the resulting values.

Closures enable dynamic and customizable node groups by allowing users to pass procedural logic into another node
tree. When the *Evaluate Closure* node runs, the connected closure is evaluated within the current context, matching
its input and output sockets by name.

Common uses for the *Evaluate Closure* node include:

- Allowing user-defined behaviors inside procedural systems (e.g. custom scattering, placement rules, or shading
  logic).
- Injecting logic into reusable node groups for advanced effects.
- Providing optional customization inputs for high-level node-based tools.


Inputs
======

Closure
   The closure to evaluate.
   This input expects a connection from a
   :doc:`Closure Zone </interface/controls/nodes/types/utilities/closure/closure>`.
   If no closure is connected, the node operates in *pass-through mode* (see below).


Interface
---------

The node can define additional inputs manually, which are matched by name to the corresponding inputs of the connected
closure. When the closure is connected, these sockets automatically sync to reflect the closure's defined interface.


Properties
==========

The *Evaluate Closure* node does not have functional properties, but its input and output interface can be managed in
the *Node* tab of the Sidebar.

Sync Sockets
   Updates the current node to match the socket signature of the connected nodes.
   Use this after renaming, adding, or removing sockets.

Define Signature
   Marks the node as defining a closure signature to be used by other closure nodes. Ensures consistent input and
   output definitions across related closures.


Input Items
-----------

List of input sockets
   Displays one entry per socket defined in the closure. Double-click to rename.

Add Item
   Add a new input socket to the closure interface.

Remove Item
   Delete the selected input socket.

Type
   The data type for the selected socket (e.g. Float, Vector, Geometry, Object, Bundle).
   For value types, a default value field appears and is used when the socket is unlinked.

Shape
   Defines the data structure supported by the input socket, such as a *Single* value, *Field*, or *Grid*.
   The shape determines how the data is evaluated and passed through the node network.
   See :ref:`interface-controls-nodes-socket_shape` for more information.


Output Items
------------

List of output sockets
   Displays one entry per output socket. Double-click to rename.

Add Item
   Add a new output socket to the node.

Remove Item
   Delete the selected output socket.

Type
   The data type for the selected socket (e.g. Float, Vector, Geometry, Object, Bundle).
   For value types, a default value field appears and is used when the socket is unlinked.


Outputs
=======

The outputs of the *Evaluate Closure* node depend on its current configuration:

- **When a closure is connected** -- Each output corresponds to an output socket of the *Closure Zone* with the same
  name.
- **When no closure is connected** -- Outputs are defined manually through the *Output Items* section of the Sidebar.


Behavior
========

When executed, this node evaluates the connected closure's internal node graph.
All input values are passed into the closure by name, and all resulting values are returned through the corresponding
outputs.

If no closure is connected, or if the node is muted, *Evaluate Closure* automatically passes through any matching
inputs and outputs by name. This *pass-through mode* makes closures optional and allows node groups to function even
without one.

Evaluation occurs in the local context of the node tree where *Evaluate Closure* resides, inheriting relevant fields,
attributes, and geometry data.


Usage
=====

The *Evaluate Closure* node is typically used to make a node group partially customizable while maintaining a stable,
reusable framework.

For example, a terrain generator might use *Evaluate Closure* to define how trees are distributed across a landscape:

#. Inside the generator group, replace the fixed tree placement logic with an *Evaluate Closure* node.
#. Expose the closure input on the group's interface.
#. In the main node tree, connect a *Closure Zone* defining the desired tree distribution behavior.

Whenever the closure is evaluated, the connected node graph runs within the terrain generator's context, producing a
customized result.

.. figure:: /images/nodes_closure_example.png
   :align: center

   Example: custom tree distribution using *Evaluate Closure*.


Socket Syncing
==============

Closures rely on matching socket names to connect inputs and outputs correctly.
If the connected *Closure Zone* and *Evaluate Closure* nodes have mismatched signatures, Blender can synchronize them
automatically.

- A sync icon appears when the socket layout differs.
- Clicking the icon updates sockets to match the connected closure.
- Automatic syncing occurs the first time a closure is connected.
- Existing sockets are never modified automatically afterward to prevent data loss.


Limitations
===========

- Viewer and inspection nodes may not display accurate values when closures are evaluated in multiple contexts.
- Captured external values are read-only and cannot be modified inside the evaluation.
- Closures currently cannot access attributes or data outside their evaluation context.
