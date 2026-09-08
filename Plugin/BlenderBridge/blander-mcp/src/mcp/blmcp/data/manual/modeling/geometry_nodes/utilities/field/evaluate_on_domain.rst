.. index:: Geometry Nodes; Evaluate on Domain
.. _bpy.types.GeometryNodeFieldOnDomain:

***********************
Evaluate on Domain Node
***********************

.. figure:: /images/node-types_GeometryNodeFieldOnDomain.webp
   :align: right
   :alt: Evaluate on Domain Node.

The *Evaluate on Domain* allows evaluating a field for a different :ref:`attribute domain <attribute-domains>`
than the domain from the :ref:`field context <field-context>`. For example, the face index could be used instead
of the face corner index, when setting the values of a :term:`UV Map`

.. note::

   This node is not necessary to retrieve data from other attribute domains; that is done automatically.
   Its utility comes from the fact that it's possible to control *when* the domain interpolation happens.
   Normally, input nodes interpolate their data to the current context's domain as soon as they create
   their output.

.. tip::

   It may be preferable to use this node over the :doc:`/modeling/geometry_nodes/attribute/capture_attribute`,
   since it allows using a specific attribute domain without requiring a geometry socket input,
   which allows creating more reusable node groups.

.. seealso::

   The method of retrieving data from another domain is somewhat similar to the
   :doc:`/modeling/geometry_nodes/utilities/field/evaluate_at_index`.


Inputs
======

Value
   The field to evaluate on the chosen attribute domain.


Properties
==========

Domain
   The :ref:`attribute domain <attribute-domains>` used for evaluation of the *Value* input.


Output
======

Value
   The values from the input, evaluated on the chosen domain, then interpolated to the domain from
   the :ref:`field context <field-context>`.
