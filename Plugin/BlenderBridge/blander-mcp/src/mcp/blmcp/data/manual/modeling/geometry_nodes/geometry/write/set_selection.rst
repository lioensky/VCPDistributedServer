.. index:: Geometry Nodes; Set Selection
.. _bpy.types.GeometryNodeToolSetSelection:

******************
Set Selection Node
******************

.. figure:: /images/node-types_GeometryNodeToolSetSelection.webp
   :align: right
   :alt: Set Selection node.

The *Set Selection* node controls which geometry is :doc:`selected </interface/selecting>`.

The input node for this data is the :doc:`/modeling/geometry_nodes/geometry/read/selection`.

.. note::

   This node can only be used in the :ref:`Tool context <tool_context>`.


Inputs
======

Geometry
   Standard geometry input.

Selection
   Boolean field for specifying which elements should be selected in the output geometry.
   Elements for which this field evaluates to false are implicitly de-selected.


Properties
==========

Domain
   Which :ref:`domain <attribute-domains>` to set the selection on.


Outputs
=======

Geometry
   Standard geometry output.
