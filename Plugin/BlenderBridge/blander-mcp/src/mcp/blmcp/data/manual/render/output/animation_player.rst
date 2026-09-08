.. _bpy.ops.render.play_rendered_anim:

.. |numsp| unicode:: U+2007

****************
Animation Player
****************

.. reference::

   :Menu:      :menuselection:`Topbar --> Render --> View Animation`
   :Shortcut:  :kbd:`Ctrl-F11`

The animation player is a utility typically used for previewing rendered animations,
supporting all image and video formats also supported by Blender.
This is a convenient way to play back image sequences at the correct frame rate.

Launching the animation player opens a new window,
playing back images or a video located at the render output of the current scene.
You can also drop images or movie files in a running animation player.
It will then restart the player with the new data.

.. tip::

   An external player can also be used instead of the one included in Blender.
   To do this, select it in the :doc:`Preferences </editors/preferences/file_paths>`.


Player Options
==============

Ping Pong
   When enabled, playback loops forwards than backwards.
X/Y Flip
   Flip the image horizontally or vertically.

   *Viewing the animation from a different perspective can help you see the animation with "fresh eyes".*


Hotkeys
=======

The following table shows the available hotkeys for the animation player.


.. rubric:: Playback

.. list-table::
   :header-rows: 1

   * - Action
     - Hotkey
   * - Start/Pause:
     - :kbd:`Spacebar`
   * - Start playback (when paused):
     - :kbd:`Return`
   * - Quit:
     - :kbd:`Esc`


.. rubric:: Timeline

.. list-table::
   :header-rows: 1

   * - Action
     - Hotkey
   * - Scrub in time:
     - :kbd:`LMB`
   * - Step back one frame:
     - :kbd:`Left`
   * - Step forward one frame:
     - :kbd:`Right`
   * - Step back 10 frames:
     - :kbd:`Down`
   * - Step forward 10 frames:
     - :kbd:`Up`
   * - Manual frame stepping:
     - :kbd:`NumpadPeriod`


.. rubric:: Playback Options

.. list-table::
   :header-rows: 1

   * - Action
     - Hotkey
   * - Backward playback:
     - :kbd:`Shift-Down`
   * - Forward playback
     - :kbd:`Shift-Up`
   * - Slow down playback:
     - :kbd:`NumpadMinus`
   * - Speed up playback:
     - :kbd:`NumpadPlus`
   * - Toggle looping:
     - :kbd:`Numpad0`
   * - Toggle frame skipping:
     - :kbd:`A`
   * - Toggle ping-pong:
     - :kbd:`P`


.. rubric:: Display

.. list-table::
   :header-rows: 1

   * - Action
     - Hotkey
   * - Toggle Playhead (Indicator):
     - :kbd:`I`
   * - Flip image on the X axis:
     - :kbd:`F`
   * - Flip image on the Y axis:
     - :kbd:`Shift-F`
   * - Hold to show frame numbers:
     - :kbd:`Shift`
   * - Zoom in:
     - :kbd:`Ctrl-NumpadPlus`
   * - Zoom out:
     - :kbd:`Ctrl-NumpadMinus`


.. rubric:: Frame Rate

.. list-table::
   :header-rows: 1

   * - Action
     - Hotkey
   * - 60 fps
     - :kbd:`Numpad1`
   * - 50 fps
     - :kbd:`Numpad2`
   * - 30 fps
     - :kbd:`Numpad3`
   * - 25 fps
     - :kbd:`Numpad4`
   * - 24 fps
     - :kbd:`Shift-Numpad4`
   * - 20 fps
     - :kbd:`Numpad5`
   * - 15 fps
     - :kbd:`Numpad6`
   * - 12 fps
     - :kbd:`Numpad7`
   * - 10 fps
     - :kbd:`Numpad8`
   * - |numsp|\ 6 fps
     - :kbd:`Numpad9`
   * - |numsp|\ 5 fps
     - :kbd:`NumpadSlash`


Frame Cache
===========

Image files are cached during playback for faster access.

While loading images is rarely a bottleneck,
there are situations where high resolution images may slow down playback causing frame skipping.

.. seealso::

   :ref:`Memory Cache Limit <bpy.types.PreferencesSystem.memory_cache_limit>` preference to control this limit,
   which may be increased to cache more images during playback.
   :ref:`command-line-args-animation-playback-options` to specify this value when launching from the command line.
