.. index:: Geometry Nodes; Curl Hair Curves

****************
Curl Hair Curves
****************

The *Curl Hair Curves* node deforms existing hair curves into curls by wrapping them
around nearby guide curves.
It is useful for creating coiled, spiral, or wavy hair patterns and for adding stylized
variation or realism to a groom.
The curls can vary in radius, frequency, and start position, with optional random offsets
for natural variation.

.. peertube:: 3AcYeH2nqMzjEXFUNqTbj7


Inputs
======

Geometry
   The input geometry containing the hair curves to deform into curls.

Factor
   Controls the overall strength of the curling effect.
   A value of 0.0 disables the effect, while 1.0 applies the full curl deformation.

Subdivision
   The number of subdivisions applied to curves before deformation.
   Higher values produce smoother curls but increase processing time.

Curl Start
   Defines the percentage along each curve (from root to tip) at which the curl effect begins.
   This allows keeping part of the strand straight before the curl starts.

Radius
   The overall radius of the curls.
   Larger values produce looser curls, while smaller values create tighter spirals.

Factor Start
   Multiplies the curl radius near the start of the curl region, allowing tapering or
   gradual buildup of curl tightness.

Factor End
   Multiplies the curl radius near the end of the curve, controlling how curls taper off
   or unwind toward the tip.

Frequency
   Controls how many full rotations occur along the length of the curve.
   Higher values produce more frequent curls.
   This input can vary per point along the curve, allowing complex wave patterns.

Random Offset
   Adds random variation to the curl phase or starting angle per curve, creating a
   more natural, less uniform look.

Seed
   Sets the random seed used for generating the random offsets.
   Changing this value produces different curl variations while maintaining the same parameters.


Guide Map
---------

Guide Index
   A map that specifies which curve should act as the guide or central reference
   for each group of curled curves.
   If provided, this overrides any existing ``guide_curve_index`` attribute,
   and the *Guide Distance* and *Guide Mask* inputs are ignored.

Guide Distance
   The minimum spacing between selected guides when generating a new guide map.
   Larger values result in fewer guide curves and broader curl groups.

Guide Mask
   A mask that determines which curves are eligible to be used as guides.

Existing Guide Map
   When enabled, uses the existing guide map attribute if one is already present.
   If disabled and *Guide Index* is not provided, a new
   :doc:`guide map </modeling/geometry_nodes/hair/guides/create_guide_index_map>`
   is created using *Guide Distance* and *Guide Mask*.
   Creating the guide map separately allows for more control and consistency
   across multiple grooming operations.


Outputs
=======

Geometry
   The resulting geometry with curled hair curves.


Guide Map
---------

Guide Index
   The guide index map used for the operation.
   If this node created a new guide map, it is stored and output here
   for use in subsequent nodes.
