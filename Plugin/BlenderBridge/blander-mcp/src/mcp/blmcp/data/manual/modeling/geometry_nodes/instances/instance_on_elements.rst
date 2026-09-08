.. index:: Geometry Nodes; Instance on Elements

*************************
Instance on Elements Node
*************************

.. figure:: /images/node-types_GeometryNodeInstanceOnElements.webp
   :align: right
   :alt: Instance on Elements node.

The *Instance on Elements* node creates instances of an object, collection, or geometry
on selected elements of an input geometry.
It can be used to distribute instances on points, edges, faces, or face corners,
providing flexibility for procedural instancing workflows.


Inputs
======

Geometry
   The geometry on which to create instances.

Instance On
   The geometry element type to instance on.

   :Points: Instances are created at the location of each point.
   :Edges: Instances are placed along edges.
   :Faces: Instances are placed on the surface of each face.
   :Corners: Instances are created at each face corner (vertex per face).

Mask
   A selection controlling which elements are used for instancing.
   Floating-point values between 0 and 1 are treated as probabilistic selections,
   resulting in a random subset of elements being used.

Input Type
   Defines how the instance geometry input is provided.

   :Data-Block: Instances are created from an object or collection data-block.
   :Geometry: Instances are created from input geometry provided to the node.

Instance Type :guilabel:`Data-Block`
   When using *Data-Block* input, determines whether to instance an *Object* or a *Collection*.

Object / Collection :guilabel:`Data-Block`
   The specific object or collection to instance when using *Data-Block* input mode.

Instance :guilabel:`Geometry`
   The geometry to instance when using *Geometry* input mode.

Realize Instances
   Converts all instances into real geometry, producing a single combined geometry output.
   This can be required for some subsequent geometry operations or modifiers.

Keep Surface
   Keeps the underlying surface used for instancing, rather than outputting only the instances.

Seed
   Random seed value used to vary random selections or random instance indexing.


Pick Instance :guilabel:`Data-Block` :guilabel:`Collection`
-----------------------------------------------------------

When instancing from a collection, this option enables random or controlled selection
of which child object to instance per element.

Instance Index
   Determines how a child instance is chosen from the collection.

   :Random:
      Picks a random object from the collection for each element.
   :Sequence:
      Cycles through objects in collection order.
   :Input:
      Uses the value from the *Instance Index* input socket.

Instance Index :guilabel:`Input`
   Specifies the index of the object in the collection to be instanced,
   used when the *Instance Index* method is set to *Input*.


Transform
---------

Surface Offset
   Moves instances along the element normal, offsetting them from the surface.

Align Rotation
   Aligns instance rotation to the orientation of the geometry element (e.g., normal direction).

Scale
   Controls the uniform or per-axis scaling of instances.


Outputs
=======

Geometry
   The resulting geometry containing all instances created on the selected elements.
