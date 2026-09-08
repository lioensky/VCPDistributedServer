
*******
Display
*******

.. _bpy.types.SpaceSequenceEditor.show_overlays:
.. _bpy.types.SequencerTimelineOverlay:

Sequencer Overlays
==================

.. reference::

   :Location:    :menuselection:`Header --> Overlays`

.. figure:: /images/editors-video_sequencer-sequencer-overlays.png

Overlays are information that is displayed on top of the sequencer region.
Clicking :bl-icon:`overlay` (Show Overlays) toggles all overlays in one go,
while the drop-down button shows a pop-over where you can toggle individual ones:

.. _bpy.types.SequencerTimelineOverlay.show_grid:

Grid
   Shows vertical lines at regular time intervals.

.. _bpy.types.SequencerCacheOverlay.show_cache:

Cache
   Visualize cached images on the timeline.


Strips
------

.. _bpy.types.SequencerTimelineOverlay.show_strip_name:

Name
   Shows the :ref:`Name <bpy.types.Strip.name>` of each strip.

.. _bpy.types.SequencerTimelineOverlay.show_strip_source:

Source
   Shows the file path of each strip.

.. _bpy.types.SequencerTimelineOverlay.show_strip_duration:

Duration
   Shows the length of each strip (in frames).

.. _bpy.types.SequencerTimelineOverlay.show_fcurves:

Animation Curves
   Shows animation curves for volume (Sound strips) and opacity (other strips).

.. _bpy.types.SequencerTimelineOverlay.show_thumbnails:

Thumbnails
   Displays thumbnails across the full width of each Movie or Image strip.
   The thumbnail size depends on the vertical zoom level (which can be adjusted
   by dragging up and down with :kbd:`Ctrl-MMB`). Zooming in results in taller
   strips with bigger, but fewer thumbnails. Zooming out results in narrower
   strips with smaller, but more thumbnails.


.. _bpy.types.SequencerTimelineOverlay.show_strip_tag_color:

Color Tags
   Displays each strip in its designated custom color (if applied) rather than a
   :ref:`color representing its type <sequencer-strip-colors>`. To set a custom color,
   either click the *Color Tag* button next to the strip's name in
   :menuselection:`Sidebar --> Strip`, or use *Set Color Tag* in the strip's context menu.

.. _bpy.types.SequencerTimelineOverlay.show_strip_offset:

Offsets
   Shows overflow bars of content that was trimmed from the strip (by moving
   the strip's handles). See :ref:`bpy.types.Strip.frame_offset_start`.


Waveforms
---------

.. _bpy.types.SequencerTimelineOverlay.waveform_display_type:

Type
   Global options for waveform display on Sound strips.

   :On: Enable waveforms for all strips.
   :Strip:
      Use the :ref:`Display Waveform <bpy.types.SoundStrip.show_waveform>`
      option of each individual strip.
   :Off: Disable waveforms for all strips.

.. _bpy.types.SequencerTimelineOverlay.waveform_display_style:

Style
   How Waveforms are displayed.

   :Full: Displays the audio amplitude.
   :Half: Displays the audio level.
