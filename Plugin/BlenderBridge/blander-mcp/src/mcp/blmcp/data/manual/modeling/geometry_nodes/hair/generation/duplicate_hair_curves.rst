.. index:: Geometry Nodes; Duplicate Hair Curves

*********************
Duplicate Hair Curves
*********************

The *Duplicate Hair Curves* node creates additional copies of existing hair curves,
distributing them around the original guide curves within a specified radius.
This is useful for increasing hair density, creating secondary strands around guides,
or achieving fuller grooms without manually adding more guides.

.. peertube:: es5bkTNvRwrvUFdjuK1UvB


Inputs
======

Geometry
   The input geometry containing the original hair curves to duplicate.

Amount
   The number of duplicates generated for each original curve.
   Higher values increase hair density.

Viewport Amount
   Defines the percentage of *Amount* used for viewport display.
   Reducing this value improves performance in the viewport while keeping render results unaffected.

Radius
   The maximum distance around each guide curve within which duplicates are placed.
   Larger values spread the duplicates further apart.

Distribution Shape
   Controls how duplicates are distributed within the radius, from the center to the outer edge.
   Different shapes can produce uniform, clustered, or edge-biased distributions.

Tip Roundness
   Adjusts the rounding of duplicate curves near their tips.
   Higher values make the distribution more circular and natural toward the ends.

Even Thickness
   When enabled, keeps an even density across the radius of duplicates.
   When disabled, density may vary depending on the distribution pattern.

Seed
   Sets the random seed for duplicate placement.
   Changing this value alters the random arrangement of duplicates while maintaining the same parameters.

Outputs
=======

Geometry
   The resulting geometry with duplicated hair curves.

Guide Index
   An integer attribute storing the index of the original guide curve for each duplicate.
   This can be used for further operations such as matching colors or following guide motion.
