.. _bpy.ops.node.sockets_sync:
.. --- copy below this line ---

*************
Node Closures
*************

A *closure* allows passing custom functionality into a node group.
It acts like a function input, enabling user-defined behavior to be evaluated inside another node tree.

Closures make node groups more flexible and reusable by letting users inject part of a node network into another.
This allows building higher-level tools where specific parts of a process can be customized without modifying the
group itself.

.. figure:: /images/nodes_closure_example_scatter_functions.png
   :align: center

   Using a closure to customize tree scattering within a terrain generator.


Overview
========

Closures are a socket type that represent callable node graphs.
They define a set of inputs and outputs that can be evaluated inside another node group through the
:doc:`Evaluate Closure </interface/controls/nodes/types/utilities/closure/evaluate_closure>` node.

When a closure is connected, its internal node graph is *injected* into the evaluation of the node group where it is
used. This allows procedural systems to remain flexible while exposing clear, customizable control points.

Closures can be thought of as function parameters for node groups.
They let users define operations that can be executed in a controlled environment defined by the parent node tree.


Nodes
=====

Closures are created and evaluated with the following nodes:

.. toctree::
   :maxdepth: 1

   closure.rst
   evaluate_closure.rst


Socket Syncing
==============

Closure nodes use socket names to match their inputs and outputs.
If two closure nodes are connected but have mismatched signatures, Blender can offer to sync them automatically.

- Sync happens automatically when a node is connected for the first time.
- Existing sockets are never changed automatically to avoid overwriting user data.
- A :bl-icon:`file_refresh` button (*Sync Sockets*) button appears in the node header when a mismatch is detected,
  allowing manual synchronization.


Example
=======

Closures are useful when part of a node group's logic should be user-defined.
For example, a terrain generator can use a closure to define tree placement:

- The :doc:`Evaluate Closure </interface/controls/nodes/types/utilities/closure/evaluate_closure>`
  node is placed where tree instances are distributed.
- A closure input is exposed on the group's interface.
- A :doc:`Closure </interface/controls/nodes/types/utilities/closure/closure>`
  node is connected defining any custom placement logic.

When the closure is evaluated, the contents of the connected node graph
are executed inside the context of the terrain generator.
This allows the generator to provide stable infrastructure
(e.g., scattering, masks, attributes) while users supply their own functional behavior.

.. figure:: /images/nodes_closure_example.png
   :align: center

   A terrain generator node group using closures for custom tree placement.
