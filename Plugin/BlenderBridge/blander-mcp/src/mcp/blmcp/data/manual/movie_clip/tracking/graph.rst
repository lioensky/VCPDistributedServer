
**********
Graph View
**********

The graph or curves view has numerous purposes based on the color of the lines.
The red and green lines on the graph show you the speed of the trackers at a given frame.
Green is vertical movement, Red is horizontal. Therefore the first frames will always be at zero.

The blue line is the line that comes out when you click on the film strip is the average per-frame error.
This curve is available only after pressing camera solve and is not editable.
This is the one line that you want to be as flat as possible and as closer to zero as you can.
The high points will show you where in your shot you are having inaccurate tracking.

Frames outside of scene frame range are darkened.

.. figure:: /images/movie-clip_tracking_graph_example.png

   Graph View.


Header
======

:bl-icon:`restrict_select_off` Only Show Selected
   Displays the graph for only selected trackers.
:bl-icon:`ghost_enabled` Display Hidden
   Displays channels from objects that are hidden.
:bl-icon:`sequence` Show Frames
   Visualizes per-frame average reprojection error of all tracks in the active tracking object.
:bl-icon:`graph` Show Tracks Motion
   Shows curves for X and Y speed of tracks.
:bl-icon:`anim` Show Tracks Error
   Per-frame reprojection error of tracks.


Usage
=====

The curves are useful to see if particular trackers are moving differently than the average.
A line that spikes from the rest of the curve usually means a tracking error.

You can manually edit the curve by selecting a point in the curve and dragging it or deleting,
that will affect the corresponding tracker on that particular frame.

Lock to Selection :kbd:`L`
   Locks the view to selected markers during playback.
