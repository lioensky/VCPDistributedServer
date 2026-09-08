.. index:: Geometry Nodes; Duplicate Elements
.. _bpy.types.GeometryNodeDuplicateElements:

***********************
Duplicate Elements Node
***********************

.. figure:: /images/node-types_GeometryNodeDuplicateElements.webp
   :align: center
   :alt: Duplicate Elements node.

The *Duplicate Elements* node creates a new geometry with the specified elements
from the input duplicated an arbitrary number of times. The positions of elements
are not changed, so all of the duplicates will be at the exact same location.


Inputs
======

Geometry
   Standard geometry input.

Selection
   Boolean field that is true for parts of the geometry to be deleted.

Amount
   Field indicating how many times each input element should be duplicated.
   If the value is zero for an element, it will not be included in the output at all.


Properties
==========

Domain
   The type of geometry element to duplicate

   :Point:
      Duplicate the points of meshes, curves, or point clouds.
      Any other elements will not be included in the output.
   :Edge:
      Duplicate mesh edges. Faces will not be included in the output.
   :Faces:
      Duplicate mesh faces. Each duplicated face will be separate,
      in other words they will not share edges with other faces.
   :Spline:
      Individual curves from the input curves component will be duplicated.
   :Instances:
      Input top-level instances will be duplicated.


Output
======

Geometry
   Standard geometry output.

Duplicate Index
   An attribute field with a value for every output element describing which
   duplicate of the corresponding input. The value for every input element will
   start at 0 and increase to ``Amount - 1``.


Examples
========

.. figure:: /images/modeling_geometry-nodes_geometry_duplicate-elements_instance.png
   :align: center


Combined with the :doc:`/modeling/geometry_nodes/geometry/geometry_to_instance`,
this can be used to create a basic efficient "Array" operation. This should be more efficient
because the duplicates are :doc:`instances </modeling/geometry_nodes/instances>`.

The "Duplicate Index" is used to move each instance in the result a different amount.
