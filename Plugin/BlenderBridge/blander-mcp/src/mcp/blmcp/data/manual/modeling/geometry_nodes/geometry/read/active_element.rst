.. index:: Geometry Nodes; Active Element
.. _bpy.types.GeometryNodeToolActiveElement:

*******************
Active Element Node
*******************

.. figure:: /images/node-types_GeometryNodeToolActiveElement.webp
   :align: right
   :alt: Active Element node.

The *Active Element* node outputs the index of the :term:`Active` point, edge, face, or layer.

.. note::

   This node can only be used in the :ref:`Tool context <tool_context>`.


Inputs
======

This node has no inputs.


Properties
==========

Domain
   Which :ref:`domain <attribute-domains>` to return the index of.


Outputs
=======

Index
   Index of the active element in the specified domain.

Exists
   True if an active element exists in the mesh, false otherwise
