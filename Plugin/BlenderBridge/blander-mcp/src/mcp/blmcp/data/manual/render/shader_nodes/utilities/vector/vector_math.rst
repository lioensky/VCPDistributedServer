.. _bpy.types.ShaderNodeVectorMath:
.. Editor's Note: This page gets copied into:
.. - :doc:`</compositing/types/utilities/vector/vector_math>`
.. - :doc:`</modeling/geometry_nodes/vector/vector_math>`

.. --- copy below this line ---

****************
Vector Math Node
****************

.. figure:: /images/node-types_ShaderNodeVectorMath.webp
   :align: right
   :alt: Vector Math Node.

The *Vector Math* node performs the selected math operation on the input vectors.


Inputs
======

The inputs of the node are dynamic. Some inputs are only available in certain operations.
For instance, the *Scale* input is only available in the *Scale* operator.

Vector
   Input vector :math:`A = \begin{pmatrix} A_x \\ A_y \\ A_z \end{pmatrix}`.
Vector
   Input vector :math:`B = \begin{pmatrix} B_x \\ B_y \\ B_z \end{pmatrix}`.
Scale
   Input Scale :math:`s`.


Properties
==========

Operation
   The vector math operator to be applied on the input vectors.

   :Add: The sum of A and B.
      :math:`\begin{pmatrix} A_x + B_x \\ A_y + B_y \\ A_z + B_z \end{pmatrix}`
   :Subtract: The difference between A and B.
      :math:`\begin{pmatrix} A_x - B_x \\ A_y - B_y \\ A_z - B_z \end{pmatrix}`
   :Multiply: The entrywise product of A and B.
      :math:`\begin{pmatrix} A_x \cdot B_x \\ A_y \cdot B_y \\ A_z \cdot B_z \end{pmatrix}`
   :Divide: The entrywise division of A by B. Division by zero results in zero.
      :math:`\begin{pmatrix} A_x / B_x \\ A_y / B_y \\ A_z / B_z \end{pmatrix}`
   :Multiply Add:
      The entrywise combination of the multiply and addition operations.
      :math:`A × B + C`
   :Cross Product: The cross product of A and B.
      :math:`\begin{pmatrix} A_y \cdot B_z - A_z \cdot B_y \\ A_z \cdot B_x - A_x \cdot B_z
      \\ A_x \cdot B_y - A_y \cdot B_x \end{pmatrix}`
   :Project: The projection of A onto B.
   :Reflect: The reflection of A around the normal B. B need not be normalized.
   :Refract:
      For a given incident vector A, surface normal B and ratio of indices of refraction (IOR),
      refract outputs the refraction vector R.
   :Faceforward: Orients a vector A to point away from a surface B as defined by its normal C.
      Computes :math:`(dot(B, C) < 0) ? A : -A`.
   :Dot Product: The dot product of A and B.
      :math:`A_x \cdot B_x + A_y \cdot B_y + A_z \cdot B_z`
   :Distance: The distance between A and B.
   :Length: The length of A.
      :math:`\sqrt{A_x^2 + A_y^2 + A_z^2}`
   :Scale: The result of multiplying A by the scalar input *Scale*.
      :math:`\begin{pmatrix} s \cdot A_x \\ s \cdot A_y \\ s \cdot A_z \end{pmatrix}`
   :Normalize: The result of normalizing A. The result vector points to the same direction as A and
      has a length of 1. If A is (0, 0, 0), the result is (0, 0, 0) as well.
   :Absolute: The entrywise absolute value of A.
   :Power: The entrywise power operator where the *Base* raised to the power of *Exponent*.
   :Sign:
      Extracts the sign of the input value. All positive numbers will output 1.0.
      All negative numbers will output -1.0. And 0.0 will output 0.0.
   :Minimum: The entrywise minimum value from A and B.
   :Maximum: The entrywise maximum value from A and B.
   :Round:
      Rounds the input value entrywise to the nearest integer,
      and upward if the fraction part is 0.5.
   :Floor: Rounds the input value entrywise down to the nearest integer.
   :Ceil: Rounds the input value entrywise up to the nearest integer.
   :Fraction: Returns the fractional part of the *value* entrywise.
   :Modulo: The entrywise modulo of A by B.
   :Wrap:
      The entrywise output of a value between Min and Max based on the absolute difference
      between the input value and the nearest integer multiple of Max less than the value.
   :Snap: The result of rounding A to the largest integer multiple of B less than or equal A.
   :Sine: The entrywise `Sine <https://en.wikipedia.org/wiki/Sine>`__ of A.
   :Cosine: The entrywise `Cosine <https://en.wikipedia.org/wiki/Trigonometric_functions>`__ of A.
   :Tangent: The entrywise `Tangent <https://en.wikipedia.org/wiki/Trigonometric_functions>`__ of A.


Outputs
=======

The output of the node is dynamic. It is either a vector or a scalar depending on the operator.
For instance, the *Length* operator has a scalar output while the *Add* operator has a vector output.

Vector
   Output vector.
Value
   Output value.
