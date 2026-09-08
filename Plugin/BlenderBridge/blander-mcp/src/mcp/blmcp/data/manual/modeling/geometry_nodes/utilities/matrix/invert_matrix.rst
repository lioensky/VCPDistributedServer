.. index:: Geometry Nodes; Invert Matrix
.. _bpy.types.FunctionNodeInvertMatrix:

******************
Invert Matrix Node
******************

.. figure:: /images/node-types_FunctionNodeInvertMatrix.webp
   :align: right
   :alt: Invert Matrix node.

Returns the `inverse <https://mathworld.wolfram.com/MatrixInverse.html>`__ of the given matrix.


Inputs
======

Matrix
   The matrix to invert.


Outputs
=======

Matrix
   The inverted matrix.
Invertible
   Returns whether the matrix could be inverted.
   This can be false when a transformation matrix has a scale of zero, for example.
   See `Invertible matrix <https://en.wikipedia.org/wiki/Invertible_matrix>`__ for more information.

   .. important::

      When a matrix is not invertible, the `identity matrix <https://en.wikipedia.org/wiki/Identity_matrix>`__
      is returned.
