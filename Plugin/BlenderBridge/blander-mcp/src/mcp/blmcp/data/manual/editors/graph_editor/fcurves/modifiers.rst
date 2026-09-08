.. index:: Modifiers; F-Curve Modifiers
.. index:: F-Curve Modifiers

.. _bpy.types.FCurveModifiers:
.. _bpy.types.FModifier:

*****************
F-Curve Modifiers
*****************

.. reference::

   :Panel:     :menuselection:`Sidebar region --> Modifiers`

F-Curve modifiers are similar to object modifiers, in that they add non-destructive effects
that can be adjusted at any time and layered to create more complex effects.

Modifiers are evaluated from top to bottom.
You can change their order by dragging the dots in their top right corner.

Some modifiers require being first and cannot be used together.
These currently include the :ref:`Cycles <bpy.types.FModifierCycles>`
and :ref:`Smooth (Gaussian) <bpy.types.FModifierSmooth>` modifiers.

Interface
=========

.. _bpy.types.FModifier.name:

Name
   By default, modifiers are named after their function, but this can be changed.

.. _bpy.types.FModifier.mute:

Mute
   Click the checkbox in a modifier's header to disable it.

Delete
   Click the cross in a modifier's header to delete it.

Influence
   Lets you blend between the original curve and the modified one.

Restrict Frame Range
   Start/End
      The frame on which the modifier's effect starts/ends.
   Blend In/Out
      The number of frames, relative the start/end values above, it takes the modifier to fade in/out.

Adding a Modifier
=================

.. figure:: /images/editors_graph-editor_fcurves_sidebar_modifiers_panel.png

   Modifiers panel.

Modifiers can be managed on the *Modifiers* tab of the Sidebar.
Select an F-Curve (in the channel region or by selecting one of its keyframes),
then click the *Add Modifier* dropdown and choose the modifier to add.


Types of Modifiers
==================

.. index:: F-Curve Modifiers; Generator Modifier
.. _bpy.types.FModifierGenerator:

Generator Modifier
------------------

Creates a polynomial function.
These are basic mathematical formulas that represent lines, parabolas,
and other more complex curves, depending on the values used.

.. seealso::

   The `Wikipedia Page <https://en.wikipedia.org/wiki/Polynomial>`__
   for more information on polynomials.

Mode
   Method used to represent the equation.

   Expanded Polynomial
      Equation in the form :math:`y = A + Bx^1 + Cx^2 + ... + Dx^n`.
   Factorized Polynomial
      Equation in the form :math:`y = (Ax + B)(Cx + D)`.

Additive
   Add the polynomial to the curve rather than replacing it.

Order
   The highest power of ``x`` for this polynomial.

Coefficient
   The constants A, B, C... in the equation.


.. index:: F-Curve Modifiers; Built-in Function Modifier
.. _bpy.types.FModifierFunctionGenerator:

Built-in Function Modifier
--------------------------

These are additional formulas, each with the same options to control their shape.
Consult mathematics reference for more detailed information on each function:

Type
   The built-in function to use:

   - `Sine <https://en.wikipedia.org/wiki/Sine>`__
   - `Cosine <https://en.wikipedia.org/wiki/Trigonometric_functions>`__
   - `Tangent <https://en.wikipedia.org/wiki/Trigonometric_functions>`__
   - `Square Root <https://en.wikipedia.org/wiki/Square_root>`__
   - `Natural Logarithm <https://en.wikipedia.org/wiki/Natural_logarithm>`__
   - Normalized Sine: :math:`sin(x)/x`

Additive
   Add the function to the curve rather than replacing it.

Amplitude
   Adjusts the Y scaling.
Phase Multiplier
   Adjusts the X scaling.
Phase Offset
   Adjusts the X offset.
Value Offset
   Adjusts the Y offset.


.. index:: F-Curve Modifiers; Envelope Modifier
.. _bpy.types.FModifierEnvelope:
.. _bpy.types.FModifierEnvelopeControlPoint:

Envelope Modifier
-----------------

Lets you reshape the curve. First, you define an envelope, which consists of two horizontal
lines that more or less match the curve's lower and upper bounds. Then, you add control points,
where each point can push, squeeze, and stretch the envelope (and the curve along with it)
at a certain frame.

.. figure:: /images/editors_graph-editor_fcurves_modifiers_envelope.png

   The Envelope modifier.

Reference
   The value which the envelope is centered around.
Min/Max
   The offset from the reference value to the envelope's initial lower/upper bound.

Add Control Point
   Adds a control point at the current frame.

Point
   Frame
      The frame of the control point.
   Min/Max
      The offset from the reference value to the envelope's adjusted lower/upper bound
      at this frame.


.. index:: F-Curve Modifiers; Cycles Modifier
.. _bpy.types.FModifierCycles:

Cycles Modifier
---------------

Makes the curve repeat itself.

.. note::

   The Cycles Modifier has to be the first modifier in the list.

   This modifier needs to know exactly where the keyframes are located,
   which is not possible when other modifiers are processed first.
   This means this modifier is not compatible with the `Smooth (Gaussian) Modifier`_.

Before/After Mode
   No Cycles
      Do not repeat the curve before/after the original.
   Repeat Motion
      Repeats the curve, keeping the values of each copy the same.
   Repeat with Offset
      Repeats the curve, offsetting each copy vertically so that its first keyframe matches the
      previous last keyframe.
   Repeat Mirrored
      Repeats the curve, flipping every other copy horizontally.

Count
   The number of copies to create. A value of 0 means infinite.


Trivially Cyclic Curves
^^^^^^^^^^^^^^^^^^^^^^^

When the *Cycle Mode* for both ends is set to either *Repeat Motion* or
*Repeat with Offset*, and no other options of the modifier are
changed from their defaults, it defines a simple infinite cycle.

This special case receives some additional support from other areas of Blender:

- Automatic Bézier handle placement is aware of the cycle and adjusts to achieve a smooth transition.
- The :ref:`Cycle-Aware Keying <bpy.types.ToolSettings.use_keyframe_cycle_aware>`
  option can be enabled to take the cycle into account when inserting new keyframes.


.. index:: F-Curve Modifiers; Noise Modifier
.. _bpy.types.FModifierNoise:

Noise Modifier
--------------

Modifies the curve with a noise formula.
This is useful for adding subtle or extreme randomness to animated movements,
like camera shake.

Blend Type
   :Replace: Adds noise in the range [-0.5, 0.5].
   :Add: Adds noise in the range [0, 1].
   :Subtract: Subtracts noise in the range [0, 1].
   :Multiply: Multiplies by noise in the range [0, 1].

Scale
   Changes the horizontal scale of the noise. Higher values make for less dense oscillation.
Strength
   Changes the vertical scale of the noise.
Offset
   Offsets the noise in time.
Phase
   Adjusts the random seed of the noise.
Depth
   Adjusts how detailed the noise function is.
Lacunarity
   Gap between successive frequencies. Depth has to be greater than 0 for this to have an effect.
Roughness
   The amount of high frequency detail. Depth has to be greater than 0 for this to have an effect.


.. index:: F-Curve Modifiers; Limits Modifier
.. _bpy.types.FModifierLimits:

Limits Modifier
---------------

Limits the curve to specific time and value ranges.

Minimum, Maximum X
   Removes the original curve data to the left of the minimum frame and to the right of the maximum,
   replacing it by :ref:`Constant extrapolation <bpy.ops.graph.extrapolation_type>`.
Minimum, Maximum Y
   Clamps the curve values, never letting them go below the minimum or above the maximum.


.. index:: F-Curve Modifiers; Stepped Interpolation Modifier
.. _bpy.types.FModifierStepped:

Stepped Interpolation Modifier
------------------------------

Gives the curve a stepped appearance by sampling it every N frames and making it hold its value
after each sample. In a sense, this lowers the curve's frame rate by letting it change its value
less frequently, producing choppy movement as a result.

Step Size
   The number of frames to hold each step.
Offset
   The number of frames to offset the sample points.
Start Frame
   The frame where to start applying the effect.
End Frame
   The frame where to stop applying the effect.

Smooth (Gaussian) Modifier
---------------------------

Uses Gaussian smoothing to reduce detail and noise in the curve.
It performs the same smoothing as the :ref:`Smoothing Operator <bpy.ops.graph.gaussian_smooth>`.

This uses linear interpolation for subframes which can introduce issues related to motion blur.

Note that this can be a resource-heavy modifier, and its effect on performance can become noticeable
when used on many F-Curves.

.. note::

   The Smooth (Gaussian) modifier has to be the first modifier in the list.

   This modifier needs to know exactly where the keyframes are located,
   which is not possible when other modifiers are processed first.
   This means this modifier is not compatible with the `Cycles Modifier`_.

Sigma
   The shape of the Gaussian distribution in frames.
   Lower values will increase sharpness, reducing the smoothing effect.
   Larger values will result in more smoothing, but are limited by the Filter Width (see below).
Filter Width
   The number of frames the filter "sees" around each keyframe.
   Higher values allow more smoothing (larger Sigma can then smooth over more frames),
   but this will decrease performance.

.. index:: F-Curve Modifiers; Gaussian Smoothing
.. _bpy.types.FModifierSmooth:
