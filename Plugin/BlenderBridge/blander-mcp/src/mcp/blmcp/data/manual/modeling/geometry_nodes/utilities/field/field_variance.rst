.. index:: Geometry Nodes; Field Variance
.. _bpy.types.GeometryNodeFieldVariance:

*******************
Field Variance Node
*******************

.. figure:: /images/node-types_GeometryNodeFieldVariance.webp
   :align: right
   :alt: Field Variance Node.

The *Field Variance* node computes the variance and standard deviation of a field over a given domain.
This is useful for measuring how much a value varies across geometry or within specific groups.

For example, it can be used to analyze the spread of values like weights, positions, or custom attributes
within each group defined by the *Group ID*.


Inputs
======

Value
   The field to evaluate. Can be a float or a vector depending on the *Data Type*.
   For vector values, variance is computed separately per component (X, Y, Z).

Group ID
   An index used to group values together for multiple separate variances.
   This can be thought of as a choice of the "bin" in which to place each value.
   This input has no effect when it is only a single value.


Properties
==========

Data Type
   :Float: The node will average a *Float* field.
   :Vector: The node will average a *Vector* field.

Domain
   The :ref:`attribute domain <attribute-domains>` used for evaluate the *Value* input.


Output
======

Standard Deviation
   The square root of the variance, describing the spread of values.

Variance
   A measure of the average squared deviation from the mean.
   Higher values indicate more variation in the input field.
