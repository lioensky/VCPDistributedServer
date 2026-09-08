.. index:: Geometry Nodes; Matrix Singular Value Decomposition (SVD)
.. _bpy.types.FunctionNodeMatrixSVD:

***************
Matrix SVD Node
***************

.. figure:: /images/node-types_FunctionNodeMatrixSVD.webp
   :align: right
   :alt: Matrix SVD node.

The *Matrix SVD* node computes the 3D `singular value decomposition
<https://en.wikipedia.org/wiki/Singular_value_decomposition>`__ of the input matrix. The SVD describes the matrix in
terms of a left and a right transformation ``U`` and ``V`` with a diagonal scaling matrix ```S`` inbetween.

``M = U * S * transpose(V)``

Only the 3x3 part of the input matrix ``M`` is used, the translation part (4th column vector) is not used. The matrix
does not have to be a pure (affine) transformation, any input matrix can be decomposed.

The output matrices ``U`` and ``V`` consist only of rotations and reflections (+1 or -1 scaling). If the input matrix
``M`` has a positive determinant then ``U`` and ``V`` are pure rotations. The scaling matrix ``S`` is described only
by the diagonal vector.


Inputs
======

Matrix
   The matrix to decompose.


Outputs
=======

U
   Left-hand transform.
S
   Singular values.
V
   Right-hand transform.
