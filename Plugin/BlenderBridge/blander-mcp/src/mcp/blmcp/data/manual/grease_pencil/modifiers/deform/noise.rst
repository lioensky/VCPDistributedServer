.. index:: Grease Pencil Modifiers; Noise Modifier
.. _bpy.types.GreasePencilNoiseModifier:

**************
Noise Modifier
**************

The *Noise* Modifier changes the value of one or more stroke/points properties like:
location, strength, thickness or UV texture position
by adding varied values that make the line unstable and noisy.

Random values can be used for the noise factor for more vivid effects.


Options
=======

.. figure:: /images/grease-pencil_modifiers_deform_noise_panel.png
   :align: right

   Noise Modifier.

Position
   Strength of the noise effect over the point location.

Strength
   Strength of the noise effect over the point strength (opacity).

Thickness
   Strength of the noise effect over the point thickness.

UV
   Strength of the noise effect over the point UV rotation.

Noise Scale
   Control the noise frequency scale.

Noise Offset
   Moves the noise along the strokes.

Seed
   :term:`Seed` used by the pseudo-random number generator.


Randomize
---------

When enabled, the noise uses a random value over time.

Mode
   :Steps:
      New random value at defined steps.

      Step
         Number of frames before using a new random value.
   :Keyframes:
      New random value only on keyframes.


Influence
---------

See :ref:`grease-pencil-modifier-influence-filters`.
