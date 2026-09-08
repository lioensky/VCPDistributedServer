.. index:: Geometry Nodes; Set Hair Curve Profile

**********************
Set Hair Curve Profile
**********************

The *Set Hair Curve Profile* node defines the radius of hair curves along their length
according to a customizable profile shape.
It allows artists to control the thickness variation from root to tip, producing
natural tapering or stylized width adjustments.

.. peertube:: gpQi2ZRQ3usV1FbQ9p3FHw


Inputs
======

Geometry
   The input geometry containing the hair curves whose radius will be modified.

Replace Radius
   When enabled, the node replaces the existing radius attribute with a new one.
   When disabled, the new radius is multiplied with the existing value instead.

Radius
   The base radius value applied to all curves when *Replace Radius* is enabled.
   This sets the overall scale of the hair thickness.

Shape
   Defines how the radius changes along the curve.
   For example, this can create a tapered profile, with thicker roots and thinner tips.

Factor Min
   The multiplier applied to the radius at the start (root) of each curve.
   Typically used to control how thick the curve starts.

Factor Max
   The multiplier applied to the radius at the end (tip) of each curve.
   Typically used to control how thin the curve becomes toward the tip.


Outputs
=======

Geometry
   The resulting geometry with updated radius attributes along each hair curve.
