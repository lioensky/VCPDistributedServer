.. _bpy.types.ShaderNodeHairInfo:

****************
Curves Info Node
****************

.. figure:: /images/node-types_ShaderNodeHairInfo.webp
   :align: right
   :alt: Curves Info Node.

The *Curves Info* node gives access to :doc:`Hair </physics/particles/hair/index>` information.


Inputs
======

This node has no inputs.


Properties
==========

This node has no properties.


Outputs
=======

Is Strand
   Outputs 1 when the shader is acting on a strand, otherwise 0.
Intercept
   The point along the strand where the ray hits the strand (1 at the tip and 0 at the root).
Length
   The total measurement from the root to the tip of the strand,
   interpreted as a grayscale value from 0 to infinity.
Thickness
   The thickness of the strand at the point where the ray hits the strand.
Tangent Normal
   Tangent normal of the strand.
Random
   A random per-curve value in the range from 0 to 1.
   It can for example be used in combination with a color ramp, to randomize the curve's color.
