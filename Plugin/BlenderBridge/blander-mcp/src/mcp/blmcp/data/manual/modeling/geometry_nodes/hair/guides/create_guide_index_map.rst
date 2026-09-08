.. index:: Geometry Nodes; Create Guide Index Map

**********************
Create Guide Index Map
**********************

The *Create Guide Index Map* node generates an integer attribute named
``guide_curve_index`` that maps every hair curve to its nearest *guide* curve.
Each non-guide curve is assigned the index of the guide curve it should follow.

This guide map is used by other hair grooming nodes (for example,
:doc:`/modeling/geometry_nodes/hair/guides/braid_hair_curves`,
:doc:`/modeling/geometry_nodes/hair/guides/clump_hair_curves`)
to organize curves into logical groups around shared guides and apply
effects consistently.

Other nodes in the :doc:`/modeling/geometry_nodes/hair/guides/index`
category can generate a guide map internally for convenience, but the
resulting attribute is equivalent to what this node produces.

.. peertube:: cPLeMHSnPYidQmJezdhcyL


Inputs
======

Geometry
   The input geometry containing the hair curves to be grouped and,
   optionally, existing guide curves.

Guides
   The curves or points that can act as guides.
   These are the candidates that other curves will be assigned to.

Guide Distance
   The minimum spacing between chosen guides.
   This prevents guides from being selected too close together and helps control
   how large each guide's influence region will be.

Guide Mask
   A mask that restricts which curves are allowed to become guides.
   Curves with a mask value of 0 cannot be selected as guides.

Group ID
   An ID used to divide the curves into independent groups for guide assignment.
   A curve will only select a guide that has the same *Group ID* value.
   This is useful for ensuring that different regions (for example, left vs. right side of a groom)
   do not mix.


Outputs
=======

Geometry
   The input geometry with two additions:

   - A ``guide_curve_index`` attribute that stores, for every curve,
     the index of its assigned guide curve.
   - A :ref:`anonymous attribute <anonymous-attributes>` representing the guide
     selection.
     The resulting geometry still contains both normal curves and the chosen guide curves.

Guide Curves
   A geometry output that includes only the curves selected as guides.

Guide Index
   An integer attribute giving, for each curve, the index of the closest guide curve
   with the same *Group ID*.

Guide Selection
   A boolean selection attribute that is true only for curves that were chosen
   as guides.
   This can be used to isolate, visualize, or further process the guide curves.
