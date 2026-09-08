.. _bpy.types.MovieTracking.active_object_index:
.. _bpy.ops.clip.tracking_object_new:
.. _bpy.ops.clip.tracking_object_remove:
.. _movie-clip-tracking-properties-object:

*************
Objects Panel
*************

.. figure:: /images/movie-clip_tracking_clip_sidebar_track_objects_panel.png
   :align: right
   :width: 195px

   Objects panel.

This panel contains a :ref:`list view <ui-list-view>` with all objects which can be used for tracking,
camera or object solving.
By default there is only one object in this list which is used for camera solving.
It cannot be deleted and other objects cannot be used for camera solving;
all added objects are used for object tracking and solving only.
These objects can be referenced from Follow Track and Object Solver constraints.
Follow Track uses the camera object by default.

If some tracks were added and tracked to the wrong object, they can be copied to another
object using :menuselection:`Track --> Copy Tracks` and :menuselection:`Track --> Paste Tracks`.

The usage for all kind of objects (used for camera and object tracking) is the same:
track features, set camera data, solve motion. Camera data is sharing between all objects and
refining of camera intrinsics happens when solving camera motion only.
