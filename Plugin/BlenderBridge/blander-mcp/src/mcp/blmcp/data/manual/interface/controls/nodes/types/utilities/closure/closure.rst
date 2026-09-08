.. index:: Nodes; Closure
.. _bpy.types.NodeClosureInput:
.. _bpy.types.NodeClosureOutput:
.. --- copy below this line ---

*******
Closure
*******

The *Closure* node defines a zone that encapsulates a reusable section of nodes behaving like a function.
It specifies inputs, outputs, and internal logic that can be executed elsewhere in the node tree using an
:doc:`Evaluate Closure </interface/controls/nodes/types/utilities/closure/evaluate_closure>` node.

Closures allow users to pass custom procedural logic into node groups, making tools more modular and adaptable.
Instead of duplicating or editing an existing group, a closure can expose user-defined behavior while preserving
the structure of the main system.

.. figure:: /images/nodes_closure_zone.png
   :align: center

   An empty closure zone.


Inputs
======

Closures define their own inputs, which act as parameters for the internal node logic.
These inputs can be created by dragging the blank input socket into another socket or by adding sockets manually in
the node's properties. Each input defines a parameter that the closure can receive when it is evaluated elsewhere.


Properties
==========

The *Closure* node does not have functional properties of its own, but its interface is configurable through the
*Node* tab in the Sidebar. Inputs and outputs can be added, removed, and renamed to define the closure's signature.

Sync Sockets
   Updates the current node to match the socket signature of the connected nodes.
   Use this after renaming, adding, or removing sockets.

Define Signature
   Marks the current zone as the source of a closure signature that other nodes can reference. This ensures consistent
   input and output definitions across multiple closure instances.


Input Items
-----------

List of input sockets
   Displays one entry per socket defined in the closure. Double-click an entry to rename it.

Add Item
   Add a new input socket to the closure.

Remove Item
   Delete the selected input socket.

Type
   Defines the data type for the selected socket (e.g. Float, Vector, Geometry, Object, Bundle).
   For value types, a default value control appears and is used when the socket is unlinked.

Shape
   Defines the data structure supported by the input socket, such as a *Single* value, *Field*, or *Grid*.
   The shape determines how the data is evaluated and passed through the node network.
   See :ref:`interface-controls-nodes-socket_shape` for more information.


Output Items
------------

Available when the closure's output zone is selected.

List of output sockets
   Displays one entry per socket defined in the closure output. Double-click to rename.

Add Item
   Add a new output socket to the closure.

Remove Item
   Delete the selected output socket.

Type
   Defines the data type for the selected socket (e.g. Float, Vector, Geometry, Object, Bundle).
   For value types, a default value control appears and is used when the socket is unlinked.

Shape
   Defines the data structure supported by the input socket, such as a *Single* value, *Field*, or *Grid*.
   The shape determines how the data is evaluated and passed through the node network.
   See :ref:`interface-controls-nodes-socket_shape` for more information.


Outputs
=======

Closures define outputs that return values to the node tree in which they are evaluated.
Outputs can be created by dragging a socket from within the zone into the blank socket on the closure's output, or by
adding sockets manually in the node's properties.


Usage
=====

Closures define reusable logic that can be injected into another node tree. They are commonly used in procedural
systems where part of the behavior should remain user-defined.

Typical use cases include:

- Defining a custom scattering rule for a terrain generator.
- Describing how to distribute or modify instances procedurally.
- Providing adjustable mappings, field evaluations, or transformation logic.


Using External Values
---------------------

Closures can *capture* values from outside their zone. A captured value is stored as part of the closure definition
and remains available even when the closure is evaluated in a different context.

Captured values make it possible to preserve external parameters—such as scale, density, or color—without creating
explicit input sockets. This makes closures cleaner and easier to reuse in different node trees.

.. figure:: /images/nodes_closure_external_input.png
   :align: center

   Capturing an external input value inside a closure.


Example
-------

#. In a terrain generator node group, replace the tree distribution logic with an
   :doc:`Evaluate Closure </interface/controls/nodes/types/utilities/closure/evaluate_closure>` node.
#. Expose the closure input on the group's interface.
#. In the main node tree, create a *Closure Zone* and connect it to that input.
#. Inside the closure zone, define the desired tree placement logic.

When the generator evaluates the closure, the custom distribution defined in the zone is executed instead of the
default behavior.

.. figure:: /images/nodes_closure_example_scatter_functions.png
   :align: center

   A *Closure Zone* defining a custom distribution pattern for tree scattering.
