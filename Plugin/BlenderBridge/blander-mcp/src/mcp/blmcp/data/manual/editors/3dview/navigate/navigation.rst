
**********
Navigation
**********


.. _bpy.ops.view3d.view_orbit:

Orbit
=====

.. reference::

   :Mode:      All modes
   :Menu:      :menuselection:`View --> Navigation --> Orbit`
   :Shortcut:  :kbd:`MMB`, :kbd:`Numpad2`, :kbd:`Numpad4`, :kbd:`Numpad6`, :kbd:`Numpad8`.

Rotate the view around the point of interest by clicking and dragging
:kbd:`MMB` on the viewport's area.

:kbd:`RMB` cancels the orbit operation.

The :kbd:`Alt` key has several effects on orbiting:

- Clicking a point with :kbd:`Alt-MMB` will make it the point of interest:
  it becomes the central point which the view orbits around.
- Holding :kbd:`Alt` and then dragging with :kbd:`MMB` in a certain direction
  will :doc:`align </editors/3dview/navigate/viewpoint>` the view to an axis
  and make it orthographic.
- Dragging with :kbd:`MMB` and then holding :kbd:`Alt`
  will perform an orbit while also snapping to the world axes,
  as well as the diagonals between them.

To change the viewing angle in discrete steps, use :kbd:`Numpad8` and :kbd:`Numpad2`
to go up and down, or :kbd:`Numpad4` and :kbd:`Numpad6` for left and right.
You can also press :kbd:`Numpad9` to switch to the opposite side of the view
(rotates the camera 180° around the Z axis).

.. seealso::

   - :ref:`Orbit Style Preference <prefs-input-orbit-style>`
   - :ref:`Auto-Perspective Preference <bpy.types.PreferencesInput.use_auto_perspective>`


.. _bpy.ops.view3d.view_roll:

Roll
====

.. reference::

   :Mode:      All modes
   :Menu:      :menuselection:`View --> Navigation --> Roll`
   :Shortcut:  :kbd:`Shift-Numpad4`, :kbd:`Shift-Numpad6`

Rotate the viewport camera around its viewing direction in 15° discrete steps by default.
See the :ref:`rotation angle <bpy.types.PreferencesView.rotation_angle>` preference to configure.

To reset the roll, you can first align the view to the global X axis
using :kbd:`Numpad3`, then orbit to get back to the regular perspective view.

:kbd:`RMB` cancels the roll operation.


.. _bpy.ops.view3d.view_pan:

Pan
===

.. reference::

   :Mode:      All modes
   :Menu:      :menuselection:`View --> Navigation --> Pan`
   :Shortcut:  :kbd:`Shift-MMB`, :kbd:`Ctrl-Numpad2`, :kbd:`Ctrl-Numpad4`,
               :kbd:`Ctrl-Numpad6`, :kbd:`Ctrl-Numpad8`

Pans the 3D Viewport by moving the view left, right, up, or down without rotating it.
This is useful for repositioning your view without changing orientation.

- :kbd:`Shift-MMB` -- Pan the view freely by dragging the mouse.
- :kbd:`Shift-WheelUp` / :kbd:`Shift-WheelDown` -- Pan the view vertically.
- :kbd:`Shift-WheelLeft` / :kbd:`Shift-WheelRight` -- Pan the view horizontally.
- :kbd:`Ctrl-Numpad8` / :kbd:`Ctrl-Numpad2` -- Pan the view up/down in fixed steps.
- :kbd:`Ctrl-Numpad4` / :kbd:`Ctrl-Numpad6` -- Pan the view left/right in fixed steps.


.. _bpy.ops.view3d.zoom:

Zoom In/Out
===========

.. reference::

   :Mode:      All modes
   :Menu:      :menuselection:`View --> Navigation --> Zoom In/Out`
   :Shortcut:  :kbd:`Ctrl-MMB`, :kbd:`Wheel`, :kbd:`NumpadPlus`, :kbd:`NumpadMinus`

Moves the view closer to, or further away from, the point of interest.
You can zoom in and out by rolling the :kbd:`Wheel` or dragging with :kbd:`Ctrl-MMB`.
To zoom with discrete steps, use the hotkeys :kbd:`NumpadPlus` and :kbd:`NumpadMinus`.

.. hint::

   If you get lost in 3D space (which is not uncommon),
   :ref:`bpy.ops.view3d.view_all` and :ref:`bpy.ops.view3d.view_selected`
   can be used to show the contents of your scene.

:kbd:`RMB` cancels the zoom operation.

.. _bpy.ops.view3d.zoom_border:

Zoom Region
===========

.. reference::

   :Mode:      All modes
   :Menu:      :menuselection:`View --> Navigation --> Zoom Region...`
   :Shortcut:  :kbd:`Shift-B`

The *Zoom Region* tool allows you to specify a rectangular region
by dragging with :kbd:`LMB`. The view will then zoom in on this region.

You can also drag with :kbd:`MMB` to zoom out instead.

.. _bpy.ops.view3d.dolly:

Dolly View
==========

.. reference::

   :Mode:      All modes
   :Menu:      :menuselection:`View --> Navigation --> Dolly View...`
   :Shortcut:  :kbd:`Shift-Ctrl-MMB`

In most cases it's sufficient to zoom the view to get a closer look at something.
However, zooming only gets you up to the point of interest and no further.
If you hit this point where zooming no longer works, you can instead Dolly
by holding :kbd:`Shift-Ctrl` and dragging up or down with :kbd:`MMB`.
This will move the point of interest (and the view along with it).

:kbd:`RMB` cancels the dolly operation.

.. hint::

   Dolly changes orthographic views to a perspective projection.

   This is done because dolly doesn't work well with an orthographic projection because *moving* forwards/backwards
   with an orthographic projection doesn't have the effect of zooming.

.. NOTE(@campbellbarton): "Frame All" & "Frame Selected" could be documented elsewhere,
   however there doesn't seem to be an ideal location as only items in the View sub-menus have their own files.
   Loosely speaking these are navigation - so keep here.

.. _bpy.ops.view3d.view_all:

Frame All
=========

.. reference::

   :Mode:      All modes
   :Menu:      :menuselection:`View --> Frame All`
   :Shortcut:  :kbd:`Home`

Changes the view so that you can see all objects.


.. _bpy.ops.view3d.view_selected:

Frame Selected
==============

.. reference::

   :Mode:      Object, Edit, Pose
   :Menu:      :menuselection:`View --> Frame Selected`
   :Shortcut:  :kbd:`NumpadPeriod`

Changes the view so that you can see the selected object(s).


Frame Last Stroke
=================

.. reference::

   :Mode:      Texture Paint, Vertex Paint, Weight Paint, Sculpt
   :Menu:      :menuselection:`View --> Frame Last Stroke`
   :Shortcut:  :kbd:`NumpadPeriod`

Centers the view on the region of the last brush stroke.
