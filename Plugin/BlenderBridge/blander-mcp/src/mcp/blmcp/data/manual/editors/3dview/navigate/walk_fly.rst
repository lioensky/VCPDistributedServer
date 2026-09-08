.. _3dview-fly-walk:

*******************
Fly/Walk Navigation
*******************

The standard navigation controls are sometimes limiting,
especially for large environments such as architectural models.
In these cases, it may be preferable to use first person controls instead,
where you can look around while "standing" in one place
rather than orbiting around a central viewpoint.

Blender offers two such alternative navigation methods: Flying and Walking.
You can initiate either method from the :menuselection:`View --> Navigation`
menu. You can also initiate your preferred one (configured
in the :doc:`Preferences </editors/preferences/navigation>`)
by pressing :kbd:`Shift-AccentGrave`.

.. figure:: /images/editors_3dview_navigate_walk-fly_view-navigation-panel.png

   View Navigation.

Common use cases for Fly/Walk include:

Navigating
   This can be a quick way to navigate a large scene.
Positioning a camera
   When activated from a camera view :kbd:`Numpad0`,
   the camera will move along with you.
Recording camera movement
   You can record the path you take by entering a camera view, enabling
   :ref:`bpy.types.ToolSettings.use_keyframe_insert_auto`,
   starting animation playback, and finally activating Fly/Walk navigation.
   The path will be recorded as camera keyframes which can then be
   used for rendering.

   Animation playback can't be controlled while Fly/Walk navigation is active,
   so when you're done recording, you first need to exit the navigation
   with :kbd:`LMB` before you can stop playback.


.. _bpy.ops.view3d.walk:

Walk Navigation
===============

.. reference::

   :Mode:      All modes
   :Menu:      :menuselection:`View --> Navigation --> Walk Navigation`

This navigation method behaves like a typical first person game.
It works with a combination of keyboard keys and mouse movement.


Usage
-----

Move the mouse in the direction you want to look and use the keys
listed below to walk around the scene.

When you are happy with the new view, press :kbd:`LMB` to confirm.
In case you want to go back to where you started, press :kbd:`Esc` or :kbd:`RMB`.

All these keys are also listed in the Status Bar while navigating.
Settings like mouse sensitivity and default speed can be adjusted in the
:doc:`Preferences </editors/preferences/navigation>`.

.. list-table::
   :widths: 10 90

   * - :kbd:`W`/:kbd:`Up`
     - Move forward.
   * - :kbd:`S`/:kbd:`Down`
     - Move backward.
   * - :kbd:`A`/:kbd:`Left`
     - Strafe left.
   * - :kbd:`D`/:kbd:`Right`
     - Strafe right.
   * - :kbd:`E`
     - Move up (global) -- only available if *Gravity* is off.
   * - :kbd:`Q`
     - Move down (global) -- only available if *Gravity* is off.
   * - :kbd:`R`
     - Move up (local) -- only available if *Gravity* is off.
   * - :kbd:`F`
     - Move down (local) -- only available if *Gravity* is off.
   * - :kbd:`Spacebar`
     - Teleport to the location at the crosshair
       (offset by the *Camera Height* value set in the Preferences).
   * - :kbd:`WheelUp`/:kbd:`NumpadPlus`
     - Increase the movement speed.
   * - :kbd:`WheelDown`/:kbd:`NumpadMinus`
     - Decrease the movement speed.
   * - :kbd:`Shift`
     - Speed up the movement temporarily.
   * - :kbd:`Alt`
     - Slow down the movement temporarily.
   * - :kbd:`V`
     - Jump -- only available if *Gravity* is on.
   * - :kbd:`Tab`
     - Toggle *Gravity*.
   * - :kbd:`Z`
     - Correct the Z axis of the view (smoothly roll it to ensure it's upright,
       not tilted to a side).
   * - :kbd:`Period`
     - Increases the jump height.
   * - :kbd:`Comma`
     - Decreases the jump height.


.. _bpy.ops.view3d.fly:

Fly Navigation
==============

.. reference::

   :Mode:      All modes
   :Menu:      :menuselection:`View --> Navigation --> Fly Navigation`

On activation, the cursor is centered inside a rectangle that defines a safe zone.
When the cursor is outside this zone, the view will rotate/pan.


Usage
-----

Move the mouse outside the safe zone in the direction you want to look.

Click :kbd:`LMB` or press :kbd:`Spacebar` to keep the current view and exit Fly navigation.
In case you want to go back to where you started, press :kbd:`Esc` or :kbd:`RMB`.

.. list-table::
   :widths: 10 90

   * - :kbd:`W`/:kbd:`Up`
     - Accelerate forward.
   * - :kbd:`S`/:kbd:`Down`
     - Accelerate backward.
   * - :kbd:`A`/:kbd:`Left`
     - Accelerate left.
   * - :kbd:`D`/:kbd:`Right`
     - Accelerate right.
   * - :kbd:`E`
     - Accelerate upward.
   * - :kbd:`Q`
     - Accelerate downward.
   * - :kbd:`MMB`
     - Drag to pan the view. Flying will pause while you're doing this.
   * - :kbd:`WheelUp`/:kbd:`NumpadPlus`
     - Increase the acceleration in the direction of motion.
       If there is no motion, start accelerating forward.
   * - :kbd:`WheelDown`/:kbd:`NumpadMinus`
     - Decrease the acceleration in the direction of motion.
       If there is no motion, start accelerating backward.
   * - :kbd:`Alt`
     - Slow down as long as the key is held, until the view eventually comes to a standstill.
   * - :kbd:`Ctrl`
     - Disable rotation -- while held, the view rotation doesn't influence the flight direction.
       This allows you to fly past an object, keeping it centered in the view
       even as you fly away from it.
   * - :kbd:`X`
     - Toggle X axis correction. If enabled, the view will smoothly pitch to look at the
       horizon when the cursor is in the safe zone.
   * - :kbd:`Z`
     - Toggle Z axis correction. If enabled, the view will smoothly roll to an upright
       orientation.
