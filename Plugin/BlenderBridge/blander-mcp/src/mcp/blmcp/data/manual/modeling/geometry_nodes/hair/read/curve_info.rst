.. index:: Geometry Nodes; Curve Info

**********
Curve Info
**********

The *Curve Info* node provides per-curve attributes describing the identity,
geometry, and relationships of each curve in a hair or curve system.
It is often used in procedural grooming and deformation setups to drive
randomization, orientation, or effects that depend on each curve's properties.

.. peertube:: 2tqKoeqhj6dbwMzHeEd9yQ


Inputs
======

This node has no inputs.


Outputs
=======

Curve Index
   The index of each curve within the geometry component.
   This can be used for deterministic indexing or pattern generation.

Curve ID
   A stable unique ID for each curve.
   Unlike *Curve Index*, this value remains consistent even if curves are added or removed.

Length
   The total length of each curve, measured along its evaluated spline.
   Useful for scaling effects or adjusting deformation strength based on hair length.

Direction
   A normalized vector pointing from the root toward the tip of each curve.
   This represents the overall direction of the curve and can be used for
   orienting instances or driving direction-dependent effects.

Random
   A random vector assigned per curve, based on the *Curve ID*.
   It provides consistent randomization between evaluations, allowing for
   reproducible but varied results across curves.

Surface UV
   The UV coordinates on the surface mesh where each curve is attached.
   This is typically used for sampling textures, transferring color data,
   or controlling procedural effects based on surface location.
