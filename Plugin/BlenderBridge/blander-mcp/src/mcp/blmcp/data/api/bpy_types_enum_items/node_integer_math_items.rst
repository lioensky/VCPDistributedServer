.. _rna_enum_node_integer_math_items:

Node Integer Math Items
#######################



**Functions**

:ADD: Add.

   A + B.
:SUBTRACT: Subtract.

   A - B.
:MULTIPLY: Multiply.

   A \* B.
:DIVIDE: Divide.

   A / B.
:MULTIPLY_ADD: Multiply Add.

   A \* B + C.


----

:ABSOLUTE: Absolute.

   Non-negative value of A, abs(A).
:NEGATE: Negate.

   -A.
:POWER: Power.

   A power B, pow(A,B).


**Comparison**

:MINIMUM: Minimum.

   The minimum value from A and B, min(A,B).
:MAXIMUM: Maximum.

   The maximum value from A and B, max(A,B).
:SIGN: Sign.

   Return the sign of A, sign(A).


**Rounding**

:DIVIDE_ROUND: Divide Round.

   Divide and round result toward zero.
:DIVIDE_FLOOR: Divide Floor.

   Divide and floor result, the largest integer smaller than or equal A.
:DIVIDE_CEIL: Divide Ceiling.

   Divide and ceil result, the smallest integer greater than or equal A.


----

:FLOORED_MODULO: Floored Modulo.

   Modulo that is periodic for both negative and positive operands.
:MODULO: Modulo.

   Modulo which is the remainder of A / B.


----

:GCD: Greatest Common Divisor.

   The largest positive integer that divides into each of the values A and B, e.g. GCD(8,12) = 4.
:LCM: Least Common Multiple.

   The smallest positive integer that is divisible by both A and B, e.g. LCM(6,10) = 30.
