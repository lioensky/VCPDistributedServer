.. index:: Geometry Nodes; Separate Matrix
.. _bpy.types.FunctionNodeSeparateMatrix:

********************
Separate Matrix Node
********************

.. figure:: /images/node-types_FunctionNodeSeparateMatrix.webp
   :align: center
   :alt: Separate Matrix node.

The *Separate Matrix* node splits a 4x4 matrix into its individual values.


Inputs
======

Matrix
   The matrix to split into individual values.


Outputs
=======

The outputs of this node are split into panels for each column of the matrix.
Each panel, has four value outputs for the four rows of the matrix.
