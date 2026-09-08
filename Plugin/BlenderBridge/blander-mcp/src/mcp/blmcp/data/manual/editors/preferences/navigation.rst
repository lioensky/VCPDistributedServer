**********
Navigation
**********

.. figure:: /images/editors_preferences_section_navigation.webp

   Blender Preferences navigation section.


.. _prefs-input-orbit-style:

Orbit & Pan
===========


.. _bpy.types.PreferencesInput.view_rotate_method:

Orbit Method
   Choose your preferred method of interactively rotating the 3D Viewport.

   :Turntable:
      Rotates the view keeping the horizon horizontal.

      This behaves like a potter's wheel or record player where you have two axes of rotation available,
      and the world seems to have a better definition of what is "Up" and "Down" in it.

      The drawback to using the *Turntable* style is that you lose some flexibility when working with your objects.
      However, you gain the sense of "Up" and "Down" which can help if you are feeling disoriented.
   :Trackball:
      Is less restrictive, allowing any orientation.

.. _bpy.types.PreferencesInput.view_rotate_sensitivity_turntable:

Orbit Sensitivity
   Adjusts the reactivity/speed of orbiting in the 3D Viewport.
   This setting works differently depending on what *Orbit Method* is used:

   - Turntable: *Orbit Sensitivity* controls the amount
     of rotation per-pixel to control how fast the 3D Viewport rotates.
   - Trackball: *Orbit Sensitivity* as a simple factor for how fast the 3D Viewport rotates.

.. _bpy.types.PreferencesInput.use_rotate_around_active:

Orbit Around Selection
   The selection center becomes the rotation center of the viewport.
   When there is no selection the last selection will be used.

   The method used to calculate the center depends on the current mode:

   - Object mode uses the selections bounding box center.
   - Edit & pose mode use the selected elements center.
   - Paint modes use the center of the last brush stroke.

   .. note::

      While this may seem like ideal behavior,
      it can be inconvenient for larger objects such as a terrain mesh,
      where the center is not necessarily a point of interest.

.. _bpy.types.PreferencesInput.use_auto_perspective:

Auto -- Perspective
   When enabled, the view switches to Perspective when orbiting the view,
   and to Orthographic when aligning to an axis (Top, Side, Front, Back, etc.).

   When disabled, this switching needs to be done manually.

.. _bpy.types.PreferencesInput.use_mouse_depth_navigate:

Auto -- Depth
   Use the depth under the mouse to improve view pan, rotate, zoom functionality.
   Useful in combination with *Zoom To Mouse Position*.

.. _bpy.types.PreferencesView.smooth_view:

Smooth View
   Time (in milliseconds) the animation takes when changing views
   (Top/Side/Front/Camera...). Reduce to zero to remove the animation.

.. _bpy.types.PreferencesView.rotation_angle:

Rotation Angle
   Rotation step size in degrees, when :kbd:`Numpad4`, :kbd:`Numpad6`, :kbd:`Numpad8`,
   or :kbd:`Numpad2` are used to rotate the 3D Viewport.


Zoom
====

.. _bpy.types.PreferencesInput.view_zoom_method:

Zoom Method
   Choose your preferred style of zooming in and out,
   when using interactive zoom.

   :Scale:
      *Scale* zooming depends on where you first click in the view.
      To zoom out, move the cursor to the area center.
      To zoom in, move the cursor away from the area center.
   :Continue:
      The *Continue* zooming option allows you to control the speed
      (and not the value) of zooming by moving away from the initial cursor position.

      Moving up from the initial click point or to the right will zoom out,
      moving down or to the left will zoom in. The further away you move,
      the faster the zoom movement will be.
      The directions can be altered by the *Vertical* and *Horizontal* radio buttons and
      the *Invert Zoom Direction* option.
   :Dolly:
      *Dolly* zooming works similarly to *Continue* zooming except that zoom speed is constant.

.. _bpy.types.PreferencesInput.view_zoom_axis:

Zoom Axis
   The axis of the mouse to use for zooming.

   :Vertical: Moving up zooms out and moving down zooms in.
   :Horizontal: Moving left zooms in and moving right zooms out.

.. _bpy.types.PreferencesInput.use_zoom_to_mouse:

Zoom to Mouse Position
   When enabled, the mouse pointer position becomes the focus point of zooming instead of the 2D window center.
   Helpful to avoid panning if you are frequently zooming in and out.

   .. tip::

      This is useful in combination with :ref:`Auto Depth <bpy.types.PreferencesInput.use_mouse_depth_navigate>`
      to quickly zoom into the point under the cursor.

.. _bpy.types.PreferencesInput.invert_mouse_zoom:

Invert Zoom Direction -- Mouse
   Inverts the Zoom direction for *Dolly* and *Continue* zooming.

.. _bpy.types.PreferencesInput.invert_zoom_wheel:

Invert Zoom Direction -- Wheel
   Inverts the direction of the mouse wheel zoom.


Fly & Walk
==========

.. _bpy.types.PreferencesInput.navigation_mode:

View Navigation
   The default mode for interactive first person navigation.

   See :ref:`3dview-fly-walk`.


.. _bpy.types.WalkNavigation:

Walk
----

.. _bpy.types.WalkNavigation.use_mouse_reverse:

Reverse Mouse
   Inverts the mouse's Y movement.

.. _bpy.types.WalkNavigation.mouse_speed:

Mouse Sensitivity
   Speed factor for when looking around, high values mean faster mouse movement.

.. _bpy.types.WalkNavigation.teleport_time:

Teleport Duration
   Interval of time warp when teleporting in navigation mode.

.. _bpy.types.WalkNavigation.walk_speed:

Walk Speed
   Base speed for walking and flying.

.. _bpy.types.WalkNavigation.walk_speed_factor:

Speed Factor
   The multiplication factor for the speed boost.


.. _bpy.types.WalkNavigation.use_gravity:

Gravity
-------

Simulates the effect of gravity when walking.

.. _bpy.types.WalkNavigation.view_height:

View Height
   The distance from the ground floor to the camera when walking.

.. _bpy.types.WalkNavigation.jump_height:

Jump Height
   The maximum height of a jump.
