
*******
Sidebar
*******

The Sidebar can be toggled with the menu item :menuselection:`View --> Sidebar`
or with the shortcut :kbd:`N`.

The image below shows two Video Sequencers, one in Preview mode and one in Sequencer mode,
both with their Sidebar open.

.. _fig-editors_vse_preview_sidebar-overview:
.. figure:: /images/editors_vse_preview_sidebar-overview.svg
   :alt: Sidebar overview


Tool
====

.. reference::

   :Editor:    Video Sequencer
   :View Type: Preview
   :Panel:     :menuselection:`Sidebar --> Tool tab`

Settings for the active :doc:`tool </editors/video_sequencer/preview/toolbar>`.

Drag
   What to do when dragging :kbd:`LMB` on a place other than the tool's gizmo.

   Active Tool
      Perform the same action as when dragging the gizmo.
   Tweak
      Move the image under the mouse cursor.
   Select Box
      Drag a selection rectangle and select all the images that are partially
      or completely inside it.

View
====

View Settings
-------------

.. reference::

   :Editor:    Video Sequencer
   :View Type: Preview
   :Panel:     :menuselection:`Sidebar --> View tab --> View Settings`

.. _bpy.types.SpaceSequenceEditor.proxy_render_size:

Proxy Render Size
   Controls the preview resolution. Lower values have worse detail but better performance.

   :No Display: Disable the preview entirely.
   :Scene Size: Preview at the full resolution without using proxies.
   :25%, 50%, 75%, 100%: Preview at a downscaled resolution, optionally using proxies (see below).
      Even selecting 100% can give a performance benefit due to the reduced image quality
      and corresponding smaller file size.

.. _bpy.types.SpaceSequenceEditor.use_proxies:

Use Proxies
   Enable the use of :doc:`proxies </editors/video_sequencer/sequencer/sidebar/proxy>`,
   which are copies of original footage stored at a lower resolution and/or quality
   for better preview performance.

   Proxies can be configured in the *Proxy* tab of the Sidebar, which is however
   only visible in the *Sequencer* and *Sequencer & Preview* modes.

.. _bpy.types.SpaceSequenceEditor.display_channel:

Channel
   Setting this to 0 shows all :doc:`channels </editors/video_sequencer/sequencer/channels>`.
   Setting it to something higher will only show the channels up to and including that number.

.. _bpy.types.SpaceSequenceEditor.show_overexposed:

Show Overexposed
   Highlight overexposed (bright white) areas using a zebra pattern.
   The threshold can be adjusted with the slider.

.. _bpy.types.SequenceEditor.show_missing_media:

Show Missing Media
   Render missing images/movies with a solid magenta color.
   When disabled, missing content will render fully transparent.

   .. tip::

      Strips with missing content will be displayed as red in the timeline.


.. _editors_sequencer_preview_2d-cursor:

2D Cursor
---------

.. reference::

   :Editor:    Video Sequencer
   :View Type: Preview
   :Panel:     :menuselection:`Sidebar --> View tab --> 2D Cursor`

The 2D Cursor is the white-red circle with a crosshair that is shown in the preview region
(provided that the :ref:`2D Cursor overlay <bpy.types.SequencerPreviewOverlay.show_cursor>`
is enabled). It can be used as a :ref:`Pivot Point <bpy.types.SequencerToolSettings.pivot_point>`
for rotating and scaling images.

.. _bpy.types.SpaceSequenceEditor.cursor_location:

Location X, Y
   The location of the 2D Cursor relative to the center of the video.
   The edges are 0.5 away, so (0.5, 0.5) is the top right corner.

   The 2D Cursor's location can also be set with the
   :doc:`Cursor tool </editors/video_sequencer/preview/toolbar>`
   or by dragging with :kbd:`Shift-RMB`.


.. _bpy.types.SequenceEditor.show_overlay:

Frame Overlay
-------------

.. reference::

   :Editor:    Video Sequencer
   :View Type: Preview
   :Panel:     :menuselection:`Sidebar --> View tab --> Frame Overlay`

The Frame Overlay lets you display a reference frame for comparing to the current frame.

.. _bpy.ops.sequencer.view_ghost_border:

Set Overlay Region
   Lets you drag a rectangle to define the bounds of the overlay.
   Instead of clicking this button, you can also press :kbd:`O` while hovering over the preview.

.. _bpy.types.SequenceEditor.overlay_frame:

Frame Offset
   The time offset between the reference frame and the current frame, in frames.

.. _bpy.types.SpaceSequenceEditor.overlay_frame_type:

Overlay Type
   How the reference frame should be displayed.

   :Rectangle: Display part of the reference frame (defined by the *Overlay Region*) on top of the current frame.
   :Reference: Display only the reference frame.
   :Current: Display only the current frame.

   .. tip::

      Each Video Sequencer editor can have its own *Overlay Type*.
      This means you can open two of them for showing the current frame and the reference frame next to each other.

.. _bpy.types.SequenceEditor.use_overlay_frame_lock:

Overlay Lock
   Keep displaying the same reference frame, even when moving to a different time point.
   This works by automatically adjusting the *Frame Offset*.

Safe Areas
----------

.. reference::

   :Editor:    Video Sequencer
   :View Type: Preview
   :Panel:     :menuselection:`Sidebar --> View tab --> Safe Areas`

Shows guides indicating the video area where content can be seen across all screens.

.. seealso::

   :ref:`Camera Safe Areas <bpy.types.DisplaySafeAreas>`.


Scene Strip Display
-------------------

.. reference::

   :Editor:    Video Sequencer
   :View Type: Preview
   :Panel:     :menuselection:`Sidebar --> View tab --> Scene Strip Display`

Controls how :doc:`Scene Strips </video_editing/edit/montage/strips/scene>`
are displayed in the preview.

.. _bpy.types.RenderSettings.sequencer_gl_preview:

Shading
   The :ref:`shading mode <view3d-viewport-shading>` to use.

.. _bpy.types.RenderSettings.use_sequencer_override_scene_strip:

Override Scene Settings
   Use the :doc:`Workbench render settings </render/workbench/index>` from the
   current scene rather than the scenes referenced by the strips.
   Only available for the *Wireframe* and *Solid* shading modes.


Annotations
-----------

.. reference::

   :Editor:    Video Sequencer
   :View Type: Preview
   :Panel:     :menuselection:`Sidebar --> View tab --> Annotations`

For managing the :doc:`Annotations </interface/annotate_tool>` in the Sequencer.


.. _editors_vse_preview_sidebar-metadata:

Metadata
========

.. reference::

   :Editor:    Video Sequencer
   :View Type: Preview
   :Panel:     :menuselection:`Sidebar --> Metadata tab`

Lists information that has been encoded in the currently visible movie or image file
(*not* the file referenced by the selected strip). This can include the filename,
the creation date, the camera model etc. This also works for images produced by Blender;
see :doc:`Render Output </render/output/properties/metadata>` for the metadata
that can be included in this case.

Other graphics programs may also store metadata,
but only the text in the header field "Comments" can be read.

Some of this metadata can also be made visible in the preview with the
:ref:`Metadata overlay <bpy.types.SequencerPreviewOverlay.show_metadata>`.

.. tip::

   The metadata can't be edited from Blender. Instead, you can use an external program such as exiftool.
   For example, the command to change the "Comments" field is:

   ``exiftool --comments="My new comment" name-of-file.png``

.. note::

   Metadata is only displayed for images/movies that don't have an effect applied.
