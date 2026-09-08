.. index:: Geometry Nodes; Capture Attribute
.. _bpy.types.GeometryNodeCaptureAttribute:

**********************
Capture Attribute Node
**********************

.. figure:: /images/node-types_GeometryNodeCaptureAttribute.webp
   :align: right
   :alt: Capture Attribute node.

The *Capture Attribute* node stores one or more fields on a geometry,
and outputs those same fields so they can be read by other nodes.

This storing and retrieving of a field can also be done with the
:doc:`/modeling/geometry_nodes/attribute/store_named_attribute`
and the :doc:`/modeling/geometry_nodes/geometry/read/named_attribute`
respectively. The difference is that the *Capture Attribute* node creates
an :ref:`anonymous attribute <anonymous-attributes>`, meaning there's no
need to specify a name and there's no clutter at the end.
This makes the node ideal for temporary data storage.

A common use case is saving information that would normally be lost while
converting geometry -- see the example below.

.. note::

   The new attribute is only available in the geometry produced by this node.
   It can't be read in the geometry of "sibling" or "upstream" nodes.


Inputs
======

Geometry
   Standard geometry input.

Capture Items
   The fields to store. Inputs can be added by connecting another node's output
   to this node's blank input, or by using the *Capture Items* list in the node's
   *Properties* panel.

   The inputs can be renamed by clicking them with :kbd:`Ctrl-LMB` in the node
   itself or in its *Capture Items* list. The latter also accepts double clicking.


Properties
==========

Domain
   Which :ref:`attribute domain <attribute-domains>` to store the evaluated data on.


Capture Items
-------------

.. reference::

   :Menu: :menuselection:`Sidebar --> Node --> Properties --> Capture Items`

:ref:`ui-list-view` for adding, removing, reordering, and renaming the inputs of the node.

Data Type
   The :ref:`data type <attribute-data-types>` of the selected input.


Outputs
=======

Geometry
   Standard geometry output.

Attribute
   The node has an attribute output for each of its field inputs.


Example
=======

.. figure:: /images/modeling_geometry-nodes_attribute_capture-attribute_example.png

The goal of this example is to turn a Curve into a tube-shaped mesh with pieces
cut away at regular intervals. At first, this seems straightforward: use the
:doc:`/modeling/geometry_nodes/curve/operations/curve_to_mesh` to create the tube,
read from the :doc:`/modeling/geometry_nodes/curve/read/spline_parameter` to find
out where each tube vertex lies on the original curve, and do some math to decide
whether to delete the vertex.

This alone doesn't work, however: the *Spline Parameter* node calculates its outputs
on the fly, and it can only do so for curves. Once the curve has been converted
to a mesh, this node can no longer be used.

This is where the *Capture Attribute* node comes in: it can *store* the calculated
distance on each curve control point. The *Curve to Mesh* node then transfers these
numbers to the mesh vertices (as it does for any attribute). From there, the attribute
can be retrieved again by connecting to the same *Capture Attribute* node that stored it.
