.. index:: Geometry Nodes; For Each Element
.. _bpy.types.GeometryNodeForEachGeometryElementInput:
.. _bpy.types.GeometryNodeForEachGeometryElementOutput:

******************************
For Each Geometry Element Zone
******************************

This zone type allows executing nodes for each element of a geometry. For example, the nodes can process
every face of a mesh, or every instance.

.. figure:: /images/modeling_geometry-nodes_foreach_geometry_element_zone.png
   :align: center

   The *For Each Element* zone.

The zone is ideal for tasks that generate large or complex geometry for every element of an input geometry.
For example, generating a unique tree for every input curve, or a unique building on every input face.

The zone makes less sense for processing small amounts of geometry. In that case (for example each of a character's
hairs separately) it will likely **always be slower** than working on fewer larger geometries. The additional
flexibility from processing each element separately comes at the cost that Blender can't optimize the operation
as well. For node groups that need to handle lots of geometry elements, it's recommended to design the node setup
so that iteration over tiny sub-geometries is not required.


Inputs
======

Geometry
    Geometry whose elements are iterated over.

Selection
    Which subset of the chosen *Domain* to process.

Index
   Index of the element in the source geometry. Note that the same index can occur more than
   once when iterating over multiple geometry component types at once.

Element
   The input geometry is split up into a separate geometry for each element.
   This is the single element geometry for the current iteration. This is not available
   for the *Face Corner* domain, since face corners cannot exist without their face.

   .. note::
      It can be quite inefficient to split up large geometries into many small elements.
      Because this output isn't computed if it's not used in the node graph, not using it
      will typically improve performance.

Properties
==========

Domain
   Which :ref:`attribute domain <attribute-domains>` to process.

Inspection Index
   Geometry element index that is used by inspection features like the :doc:`/modeling/geometry_nodes/output/viewer`
   or :doc:`socket inspection </modeling/geometry_nodes/inspection>`.


Outputs
=======

The *Main Geometry* outputs create attributes on the "main" output geometry (the first output).
Every single value on the inside of the zone becomes a value of the attribute at the current index.

The outputs in the *Generated* panel, including the default *Geometry* output are joined together from the
geometry generated from each element. Any non-geometry type below a specific geometry in this list will output
as an :ref:`anonymous attribute <anonymous-attributes>` on that joined geometry (and not the others).
Attributes from the zone's input geometry are also propagated to these geometry outputs.
