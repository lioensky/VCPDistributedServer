
***************
Tracking Marker
***************

Point
=====

.. figure:: /images/movie-clip_tracking_clip_marker_schematic.svg
   :align: center

   Marker schematic.

The whole marker can be moved with :kbd:`RMB` or by dragging the anchor point (black dot) with :kbd:`LMB`.
Pressing :kbd:`G` also moves the whole marker. When pressing :kbd:`G` twice the marker will be moved
while keeping the anchor in place. Note that the anchor point outside the pattern area is shown as a cross connected
with marker position with a dashed line.

:kbd:`S` scales the whole marker.
The whole pattern area only will be scaled by pressing :kbd:`S` twice;
The Pattern can also be rotated using the :kbd:`R` key which, depending on the used pivot point,
will either rotate patterns around their own centers or rotate the whole markers around e.g. the median point.

To match the perspective transformation of a marker on a plane, the individual corners must be edited manually.
Each marker corner can deform individually to define the shapes.
Corner positions can be edited by dragging them with a mouse.
Dragging with :kbd:`LMB` will change the position of an individual corner.

.. note::

   Note that deforming a pattern is not only useful for planar / affine tracking.
   Since only pixels within the pattern will be considered this can help to
   specify a better pattern to track even for simple position tracking.

The Search area can not be rotated; this is intentional. It doesn't make sense to deform the search area.


Plane
=====

The left bottom corner of the plane does have X/Y axis (X is red, Y is green) to
help distinguishing orientation of the plane in space.

It is likely that corner of the plane object need to be manually adjusted.
To do this sliding individual corners with mouse :kbd:`LMB` or general transform tools
:kbd:`G`, :kbd:`R`, :kbd:`S` could be used.

Adjusting plane corners will keep it following the plane defined by tracks it was originally created from.
