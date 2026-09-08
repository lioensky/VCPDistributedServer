.. _bpy.types.ShaderNodeLightFalloff:

******************
Light Falloff Node
******************

:guilabel:`Cycles Only`

.. figure:: /images/node-types_ShaderNodeLightFalloff.webp
   :align: right
   :alt: Light Falloff Node.

The *Light Falloff* node allows you to manipulate how light intensity decreases over distance.
In reality light will always fall off quadratically; however,
it can be useful to manipulate as a non-physically-based lighting trick.
Note that using Linear or Constant falloff may cause more light to be introduced with every global
illumination bounce, making the resulting image extremely bright if many bounces are used.


Inputs
======

Strength
   Light strength before applying falloff modification.
Smooth
   Smooth intensity of light near light sources. This can avoid harsh highlights,
   and reduce global illumination noise. 0.0 corresponds to no smoothing; higher values smooth more.
   The maximum light strength will be strength/smooth.


Properties
==========

This node has no properties.


Outputs
=======

Quadratic
   Quadratic light falloff; this will leave strength unmodified if smooth is 0.0 and corresponds to reality.
Linear
   Linear light falloff, giving a slower decrease in intensity over distance.
Constant
   Constant light falloff, where the distance to the light has no influence on its intensity.


Examples
========

Todo <2.8 add.
