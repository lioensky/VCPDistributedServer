.. index:: Editors; Movie Clip Editor

************
Introduction
************

The Movie Clip Editor is used for :doc:`tracking and masking </movie_clip/index>` movies.

.. figure:: /images/editors_clip_introduction_example.png

   Movie Clip Editor interface.


Header
======

.. figure:: /images/movie-clip_masking_introduction_header.png

   The Movie Clip Editor header in Mask mode.

Mode
----

:doc:`Tracking </movie_clip/tracking/index>`
   For placing markers in a video and tracking their movement.

:doc:`Mask </movie_clip/masking/index>`
   For creating and animating masks.

View Type
---------

:doc:`Clip </movie_clip/tracking/clip/index>`
   The default view, for placing and tracking markers.
:doc:`Graph </movie_clip/tracking/graph>`
   Plots the movement speed of the markers on a graph.
:doc:`Dope Sheet </movie_clip/tracking/dope_sheet>`
   Shows an overview of marker keyframes on a timeline.

View Menu
---------

Toolbar :kbd:`T`
   Show or hide the tab panel on the left for creating and manipulating markers and masks.
Sidebar :kbd:`N`
   Show or hide the :ref:`Sidebar <ui-region-sidebar>`.
:ref:`Adjust Last Operation <bpy.ops.screen.redo_last>`
   Display a pop-up panel to alter the properties of the last
   completed operation.

----------

Show Metadata
   Displays metadata encoded in the video, if available.

----------

Frame All :kbd:`Home`
   Zooms and pans the view so that the whole video is visible.
Frame Selected :kbd:`NumpadPeriod`
   Zooms and pans the view to focus on the selected items.
Center View to Cursor :guilabel:`Mask Mode`
   Pans the view so that the :ref:`2D Cursor <editors-clip-2d_cursor>` is in the center.
Zoom
   Menu with convenient zoom levels and operations.
   The zoom levels are calculated based on the images resolution compared to the screen resolution.

   - 12.5% (1:8) :kbd:`Numpad8` zoom out to a factor of 12.5%.
   - 25% (1:4) :kbd:`Numpad4` zoom out to a factor of 25%.
   - 50% (1:2) :kbd:`Numpad2` zoom out to a factor of 50%.
   - 100% (1:1) :kbd:`Numpad1` resets the zoom to 100%.
   - 200% (2:1) :kbd:`Ctrl-Numpad2` zoom in to a factor of 200%.
   - 400% (4:1) :kbd:`Ctrl-Numpad4` zoom in to a factor of 400%.
   - 800% (8:1) :kbd:`Ctrl-Numpad8` zoom in to a factor of 800%.

   Zoom In/Out :kbd:`Wheel`
      Zooms the view in or out.
   Zoom to Fit :kbd:`F`
      Like *Frame All*, but uses as much space in the editor as possible.

----------

Area
   Area controls. See the :doc:`user interface </interface/window_system/areas>`
   documentation for more information.


Select Menu
-----------

Menu for selecting :doc:`markers </movie_clip/tracking/clip/selecting>`
and :doc:`masks </movie_clip/masking/selecting>`.

Clip Menu
---------

Menu for :doc:`loading movie clips and creating proxies </movie_clip/tracking/clip/editing/clip>`.

Track Menu
----------

Menu for performing :doc:`tracking </movie_clip/tracking/clip/editing/track>` operations.

Reconstruction Menu
-------------------

Menu for setting up the :doc:`reconstruction </movie_clip/tracking/clip/editing/reconstruction>`
of 3D information from the tracked points in the 2D video.

Add Menu
--------

Use to add primitive mask shapes.

Circle
   Adds a circle-shaped mask.
Square
   Adds a square-shaped mask.


Mask Menu
---------

Menu for operators used to :doc:`Edit </movie_clip/masking/editing>` masks.


Other
-----

Clip
   A :ref:`data-block menu <ui-data-block>` used for loading and selecting movies.
   Both video files and image sequences can be used.
   When a movie clip is loaded into the Clip editor, extra panels are displayed in the interface.

Pivot Point
   See :doc:`Pivot Points </editors/3dview/controls/pivot_point/index>`.

Proportional Editing :guilabel:`Mask Mode`
   See :doc:`/editors/3dview/controls/proportional_editing`.

Mask :guilabel:`Mask Mode`
   A :ref:`data-block menu <ui-data-block>` for creating and selecting masks.

Mask Display :guilabel:`Mask Mode`
   See :doc:`/editors/clip/display/mask_display`.

.. _bpy.types.SpaceClipEditor.lock_selection:
.. _bpy.ops.clip.lock_selection_toggle:

Toggle Lock Selection :kbd:`L`
   Automatically pans the view to follow the selected markers,
   so that they remain in the same location on screen during tracking and playback.

   This option "locks the view onto the selection" and is not to be confused with the
   :ref:`Lock <bpy.types.MovieTrackingTrack.lock>` option in the Sidebar,
   which instead prevents you from changing the active marker.

Clip Display
   See :doc:`/editors/clip/display/clip_display`.

Gizmos
   See :doc:`/editors/clip/display/gizmo`.
