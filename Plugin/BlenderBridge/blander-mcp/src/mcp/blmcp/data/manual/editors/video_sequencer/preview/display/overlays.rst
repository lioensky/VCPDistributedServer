.. _bpy.types.SequencerPreviewOverlay:

**************************
Sequencer Preview Overlays
**************************

.. reference::

   :Location:    :menuselection:`Header --> Overlays`

Clicking :bl-icon:`overlay` (Show Overlays) toggles all overlays in the Video Sequencer.
The drop-down button displays a popover with more detailed settings,
which are described below.

Image Outline
   Shows an outline around the selected images.

.. _bpy.types.SequencerPreviewOverlay.show_cursor:

2D Cursor
   Shows the :ref:`editors_sequencer_preview_2d-cursor`.

Frame Overlay
   Shows the :ref:`Frame Overlay <bpy.types.SequenceEditor.show_overlay>`
   for comparing the current frame to a reference frame.

.. _bpy.types.SequencerPreviewOverlay.show_safe_areas:

Safe Areas
   Shows guides indicating the video area where content can be seen across all screens.

   .. seealso::

      :ref:`Camera Safe Areas <bpy.types.DisplaySafeAreas>`.

.. _bpy.types.SequencerPreviewOverlay.show_metadata:

Metadata
   Shows :ref:`file metadata <editors_vse_preview_sidebar-metadata>`.

.. _bpy.types.SequencerPreviewOverlay.show_annotation:

Annotations
   Shows :doc:`Annotations </interface/annotate_tool>`.
