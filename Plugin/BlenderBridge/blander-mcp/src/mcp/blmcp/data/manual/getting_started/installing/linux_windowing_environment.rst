:orphan:

.. _linux-windowing-environment:

***************************
Linux Windowing Environment
***************************

On Linux Blender supports both X11 and Wayland for official releases.

When Wayland is detected, it is the preferred system, otherwise X11 will be used.

.. hint::

   The current Windowing Environment is listed in :menuselection:`Topbar --> Blender --> About Blender`.


X11
===

This is the windowing environment that has historically been used most widely on Linux & Unix systems.

There are no near-term plans to deprecate or remove X11 support.


Wayland
=======

Support for Wayland is a more recent addition, so there may be configurations that have not been tested yet. Please
:doc:`report a bug </troubleshooting/report_bug>` if you experience problems.

Blender has been tested with Gnome-Shell (mutter), KDE (plasma) & SWAY (wlroots) based compositors.


Requirements
------------

Gnome-Shell
   Under Gnome-Shell the ``libdecor`` library is required. This is available as a package on most Linux distribution.

   If the library isn't found X11 will be used as a fallback.


Troubleshooting
---------------

Detailed Wayland output can help to track down problems. Launch Blender from the
:doc:`command-line </advanced/command_line/launch/linux>` with additional arguments:

Blender's Wayland Logging
   .. code-block:: sh

      blender --log "ghost.wl.*" --log-level 2

Wayland Built-In Logging
   .. code-block:: sh

      WAYLAND_DEBUG=1 blender

Disable Wayland (forcing X11)
   .. code-block:: sh

      WAYLAND_DISPLAY="" blender

Disable ``libdecor`` (forcing borderless windows under Gnome-Shell)
   Uninstall ``libdecor``, then run Blender with an empty X11 display variable.

   .. code-block:: sh

      DISPLAY="" blender


Environment Variables
---------------------

``XCURSOR_THEME``
   The cursor theme to use (must refer to a locally installed cursor).

``XCURSOR_SIZE``
   The cursor size, defaults to 28, you may wish to increase the size on Hi-DPI displays.


Known Limitations
-----------------

Gnome Shell's Fractional Scaling (before version 44)
   Versions of Gnome-Shell prior to 44 don't fully support fractional scaling.

   Using fractional under older versions of Gnome-Shell may result in glitches such as a `small cursor size
   <https://projects.blender.org/blender/blender/issues/105895>`__.

NVIDIA GPU
   Currently NVIDIA drivers don't fully support features needed for Wayland. Graphical glitches and flickering are
   common problems. In some cases, there can be `crashes on startup
   <https://projects.blender.org/blender/blender/issues/103999>`__. This is not specific to Blender, so NVIDIA users
   may want to use X11 until driver support improves.

----


Feature Comparison
==================

.. |tick|  unicode:: U+2713
.. |cross| unicode:: U+2717
.. |none|  unicode:: U+2014

.. list-table::
   :header-rows: 1
   :class: valign
   :widths: 30 5 5 60

   * - Feature
     - X11
     - Wayland
     - Notes
   * - Smooth Scroll
     - |cross|
     - |tick|
     - | Smooth scrolling with track-pads.
   * - Multi-Touch Gestures
     - |cross|
     - |tick|
     - | Track-pad and tablet support for
       | pinch to zoom, pan and orbit.
   * - Reliable Cursor Warping
     - |cross| :sup:`*1`
     - |tick|
     - | Cursor warping is used while transforming
       | and orbiting the viewport for e.g.
   * - Window Positioning
     - |tick|
     - |cross| :sup:`*2`
     - | Needed for dragging between windows and
       | restoring window positions on file load.

Other features which both systems support such as Hi-DPI, 3D-mouse, tablet input, ... etc.
have been left out of this list.

| :sup:`*1` In X11 fast cursor motion may exit the window bounds while the cursor is grabbed (transforming for e.g.).
| :sup:`*2` Wayland doesn't support setting the window position, as this is a design decision it's unlikely to be
  supported (see issues for `position <https://projects.blender.org/blender/blender/issues/98928>`__).
