.. index:: Modifiers; Video Sequencer Modifiers
.. index:: Video Sequencer Modifiers

.. _bpy.types.StripModifier:

***************
Strip Modifiers
***************

.. reference::

   :Panel:     :menuselection:`Properties Editor --> Strip Modifiers`

.. figure:: /images/video-editing_sequencer_strip_modifiers_panel.webp
   :align: right
   :scale: 75%

Modifiers are used to make adjustments to the image, like contrast,
brightness, saturation, color balance and applying masks.

You can add these modifiers directly to a media strip,
or you can use them within an :doc:`Adjustment Layer </video_editing/edit/montage/strips/adjustment>`
strip, making them apply to several media strips in one go.

.. _bpy.types.Strip.use_linear_modifiers:

Linear Modifiers
   Calculates modifiers in :ref:`linear color space <color-management-linear-space>` instead of the
   :ref:`Sequencer color space <bpy.types.ColorManagedSequencerColorspaceSettings.name>`.

   Calculating modifiers in linear space will match the image processing of the compositor.
   In most cases, this should be enabled; working in a non-linear workflow could have unpredictable results.


Common Options
==============

Each modifier has several buttons at its top:

:bl-icon:`restrict_render_on` / :bl-icon:`restrict_render_off`  Enable
   Enables/Disables the modifier. Useful to compare the image with or without modifications.
:bl-icon:`x` Remove Strip Modifier
   Deletes the modifier from the stack.
:bl-icon:`grip` Move Strip Modifier
   Dragging this button changes the modifier's position in the stack which affects its computation order.


Masking
-------

You can mask each modifier to limit the area of the image it affects. This can be done using
either a :doc:`Mask </movie_clip/masking/introduction>` or another strip.

Mask Input Type
   Type of input data used for the mask.

   :Strip:
      Use the grayscale representation of another strip's image.
   :Mask:
      Use a Mask data-block.

Mask
   The Strip or Mask data-block to use.

Mask Time :guilabel:`Mask Input Only`
   How the start frame of the mask is calculated.

   :Relative: Mask animation is offset to the start of the strip.
   :Absolute: Mask animation is in sync with the scene frame.


Types
=====

Currently, the following modifiers are supported:


.. index:: Video Sequencer Modifiers; Brightness/Contrast Modifier
.. _bpy.types.BrightContrastModifier:

Brightness/Contrast Modifier
----------------------------

Adjusts the brightness and contrast of the image.


.. index:: Video Sequencer Modifiers; Color Balance Modifier
.. _bpy.types.ColorBalanceModifier:

Color Balance Modifier
----------------------

Color balance adjustments, either by the Lift/Gamma/Gain or the Offset/Power/Slope method.

This modifier works similar to the :doc:`Color Balance Node </compositing/types/color/adjust/color_balance>`.

.. figure:: /images/video-editing_sequencer_sidebar_color-balance-modifier.webp
   :align: right

Depending on the selected method, the following operations can be applied to the color values in the
sequencer color space:

Lift/Gamma/Gain
   Lift
      Increases the value of dark colors.
   Gamma
      Adjusts midtones.
   Gain
      Adjusts highlights.

Offset/Power/Slope (ASC-CDL)
   The following formula is applied to each RGB color value separately: :math:`c_{out} =  (c_{in}×s + o)^p`

   Slope
      The multiplier :math:`s` influences all color values except black. Its effect is stronger
      the brighter the source color is.
   Offset
      Shifts color values after applying Slope by adding the Offset :math:`o` to them. Note that
      the selected value shown in the UI will be reduced by 1, so the default value of 1 means
      effectively no offset is applied.
   Power
      Overall exponent :math:`p`, which mainly adjusts the midtones.


.. index:: Video Sequencer Modifiers; Compositor Modifier
.. _bpy.types.SequencerCompositorModifierData:

Compositor Modifier
-------------------

Compositor modifier is powerful tool to create arbitrary effects. To use it, you need to open compositor editor
and change node subtree to sequencer. Then you can add new node tree and use it for any strip. These node trees
can be marked as :doc:`asset </files/asset_libraries/index>` and reused across multiple .blend files.

.. figure:: /images/vse_compositor_modifier_example.png
   :alt: Compositor modifier setup

To learn more about how to use compositor, see :doc:`/compositing/index`


.. index:: Video Sequencer Modifiers; Curves Modifier
.. _bpy.types.CurvesModifier:

Curves Modifier
---------------

Color and RGB curves.

This modifier works the same as the :doc:`/compositing/types/color/adjust/rgb_curves`.


.. index:: Video Sequencer Modifiers; Hue Correct Modifier
.. _bpy.types.HueCorrectModifier:

Hue Correct Modifier
--------------------

HSV multi points curves.

This modifier works the same as the :doc:`/compositing/types/color/adjust/hue_correct`.


.. index:: Video Sequencer Modifiers; Mask Modifier

Mask Modifier
-------------

The mask modifier is used to affect the :term:`Alpha Channel` of the current strip.

.. _bpy.types.StripModifier.input_mask_type:

Mask Input Type
   Type of input data used for the mask.

   :Strip:
      Use the grayscale representation of another strip to affect the alpha of the current strip.
   :Mask:
      Use a mask data-block to affect the alpha of the current strip.

.. _bpy.types.StripModifier.input_mask_id:
.. _bpy.types.StripModifier.input_mask_strip:

Mask
   The Strip or Mask data-block to use.

.. _bpy.types.StripModifier.mask_time:

Mask Time :guilabel:`Mask Input Only`
   How the start frame of the mask is calculated.

   :Relative: Mask animation is offset to the start of the strip.
   :Absolute: Mask animation is in sync with the scene frame.


.. index:: Video Sequencer Modifiers; Tone Map Modifier

Tone Map Modifier
-----------------

Used to map one set of colors to another in order to approximate the appearance
of high dynamic range images in a medium that has a more limited dynamic range.

This modifier works the same as the :doc:`Tone Map Node </compositing/types/color/adjust/tone_map>`.


.. index:: Video Sequencer Modifiers; White Balance Modifier
.. _bpy.types.WhiteBalanceModifier:

White Balance Modifier
----------------------

Used to adjust the white balance by choosing the color that should be white.


.. index:: Video Sequencer Modifiers; Sound Equalizer Modifier
.. _bpy.types.SoundEqualizerModifier:

Sound Equalizer Modifier
------------------------

This modifier can be used to emphasize or suppress sound frequencies.
The range is limited to 35Hz - 20kHz and +/-35dB.


.. index:: Video Sequencer Modifiers; Sound Pitch Modifier
.. _bpy.types.PitchModifier:

Pitch
-----

The *Pitch* modifier changes the pitch of a sound strip without altering its timing.
It can be used to correct pitch, create voice effects, or match the key of other audio.

Mode
   Mode of the pitch shift.

   :Semitones:
      Shift pitch using musical intervals.

      Semitones
         Number of semitones to shift the pitch.
         Positive values raise the pitch, negative values lower it.
      Cents
         Fine adjustment in cents (1/100 of a semitone).

   :Ratio:
      Shift pitch using a direct multiplier.

      Ratio
         Factor by which the audio pitch is scaled.
         Values greater than 1 raise the pitch, values less than 1 lower it.

Preserve Vocal Format
   Preserve vocal formants when shifting pitch.
   This helps keep speech sounding more natural (for example, raising pitch without making the voice
   sound "chipmunk-like"), but may introduce additional processing artifacts depending on the audio.

Quality
   Quality of the pitch shifting.

   :High:
      Prioritize high-quality pitch processing, typically at the cost of performance.
      Best for final renders.
   :Fast:
      Prioritize speed over audio quality.
      Useful for editing and preview playback.
   :Consistent:
      Prioritize stability when pitch changes dynamically over time (for example, when animated).
      This can reduce sudden changes in processing quality, at the cost of additional artifacts in some cases.


.. index:: Video Sequencer Modifiers; Sound Echo Modifier
.. _bpy.types.EchoModifierModifier:

Echo
----

The *Echo* modifier adds delayed repetitions of the sound, creating an echo effect.
It can be used to simulate reflections, add depth, or create rhythmic audio effects.

Delay
   Time between each echo repetition in seconds.
   Larger values increase the spacing between echoes, while smaller values create
   a tighter, more rapid echo effect.

Feedback
   Amount of the echoed signal that is fed back into the effect.
   Higher values produce more repetitions and a longer decay,
   while lower values result in fewer echoes.

Mix
   Balance between the original (dry) signal and the echoed (wet) signal.
   A value of 0 uses only the original sound, while a value of 1 outputs only
   the echoed signal.
