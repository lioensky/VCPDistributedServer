.. index:: Geometry Nodes; Braid Hair Curves

*****************
Braid Hair Curves
*****************

The *Braid Hair Curves* node deforms existing hair curves into braided strands by
grouping nearby curves around guide curves. The deformation creates a multi-strand
braid pattern, with options for radius, twist frequency, strand thickness, and an
optional flare or tied ending.

This node is designed for grooming workflows where a few curves act as braid guides,
and surrounding curves are wrapped around them to form a structured braid.

.. peertube:: wqJoqfqsWvT6msnD75RV2Q


Inputs
======

Geometry
   The input geometry containing the hair curves to deform into braids.

Factor
   Controls how strongly the braiding effect is applied.
   A value of 0.0 leaves the hair unchanged, while 1.0 applies the full braid deformation.

Subdivision
   The number of subdivisions applied to curves before deformation.
   Higher values allow smoother braids at the cost of performance.

Braid Start
   Controls where along each curve the braid effect begins, measured from the root.
   Lower values start the braid closer to the root, higher values leave more unbraided length.

Radius
   The overall radius of the braid.
   Larger values create a thicker braid by moving the strands farther from the braid center.

Shape
   Adjusts the radius profile along each curve.
   This can be used to taper or vary the braid width from root to tip.

Frequency
   Controls how quickly the curves twist around the center of the braid.
   Higher values create tighter, more frequent wrapping.
   This input can vary per point along a curve, allowing twists to tighten or loosen along the length.


Shape Parameters
----------------

Factor Min
   Minimum radius factor for the braid cross-section.
   This determines how close strands can get to the braid center.

Factor Max
   Maximum radius factor for the braid cross-section.
   This determines how far strands can move outward from the center.

Thickness
   The thickness of each strand of hair within the braid.

Thickness Shape
   Adjusts how strand thickness changes along the length of the braid.

Shape Asymmetry
   Introduces asymmetry in the strand shaping.
   This breaks perfect radial uniformity, helping the braid feel more organic.

Flare Length
   The length of the flare at the end of the braid, where the strands loosen or fan out.

Flare Opening
   The radius of that flare at the tip of the braid.
   Higher values create a wider, more open flare.


Hair Tie
--------

Hair Tie Input Type
   Defines how the hair tie object (e.g. a band or wrap) is provided for instancing.

   :Object:
      Use an object reference for the hair tie instance.
   :Geometry:
      Use a geometry input directly.

Hair Tie
   The object or geometry used as the hair tie to cap or bind the end of the braid.

Scale
   The scale of the hair tie instance.


Guide Map
---------

Guide Index
   A map that specifies which curve should act as the central "guide" for each braid group.
   If provided, this overrides any existing ``guide_curve_index`` attribute,
   and the *Guide Distance* and *Guide Mask* inputs are ignored.

Guide Distance
   The minimum spacing between selected guides when automatically generating a guide map.
   Larger values result in fewer guides, forming larger braid groups.

Guide Mask
   A mask that determines which curves are allowed to be considered as guides.

Existing Guide Map
   When enabled, use an existing guide map attribute (for example,
   ``guide_curve_index``) if it is already present.
   If this is disabled and *Guide Index* is not provided, a new
   :doc:`guide map </modeling/geometry_nodes/hair/guides/create_guide_index_map>`
   is generated using *Guide Distance* and *Guide Mask*.
   Creating the guide map ahead of time, in a separate node or modifier,
   gives more precise control over which curves act as braid guides.


Outputs
=======

Geometry
   The resulting geometry with braided deformation applied.

Flare Parameter
   A value from 0 to 1 indicating the position along the braid flare region.
   This can be used for shading or for adding effects (such as tying, binding, or loosening
   near the braid tip).

Strand Index
   An index identifying which strand of the braid each curve belongs to within its braid group.


Guide Map
---------

Guide Index
   The guide index map actually used to generate the braid.
   If a new guide map was created by this node, it is provided here for reuse downstream.
