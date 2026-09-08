
*****
Cache
*****

The *Cache* is used to store preview frames in memory so they can be displayed much faster
during playback, rather than being re-rendered for each frame. This is especially useful for
maintaining smooth performance when editing or scrubbing through a sequence.

The total cache memory limit can be configured in the :doc:`System tab </editors/preferences/system>`
of the Preferences.

.. seealso::

   Which frames are cached can be visualized by enabling
   :ref:`Show Cache <bpy.types.SequencerCacheOverlay.show_cache>` in the Timeline overlay settings.


Cache Settings
==============

.. reference::

   :Panel:     :menuselection:`Sidebar --> Cache --> Cache Settings`

This panel allows configuration of how and when image data is cached during editing.
These settings apply globally to all strips in the Video Sequence Editor.

.. _bpy.types.SequenceEditor.use_prefetch:

Prefetch Frames
   When enabled, Blender will automatically prefetch and cache frames after the current frame
   in the background. This can result in smoother playback performance.

   Note: prefetching is not currently supported for Scene strips.

.. _bpy.types.SequenceEditor.use_cache_raw:
.. _bpy.types.SequenceEditor.use_cache_final:

Cache
   Raw
      Caches raw image data immediately after it is read from disk.
      This speeds up adjustments to strip parameters such as color correction,
      but increases memory usage.
   Final
      Caches the final composited image for each frame,
      allowing faster playback of fully processed strips.


Display
-------

Visual indicators in the Timeline showing which frames are cached.

.. _bpy.types.SequencerCacheOverlay.show_cache_raw:
.. _bpy.types.SequencerCacheOverlay.show_cache_final:

Cache
   Raw
      Displays a red bar in the Timeline below frames cached in their raw state.
   Final
      Displays a blue bar at the top of Timeline for frames cached in their final composited state.

A readout at the bottom of the panel shows real-time statistics about cache usage:

- **Current Cache Size**: Total amount of memory currently used by the cache system.
- **Raw**: Memory usage by raw image cache.
- **Final**: Memory usage by final rendered frame cache.
