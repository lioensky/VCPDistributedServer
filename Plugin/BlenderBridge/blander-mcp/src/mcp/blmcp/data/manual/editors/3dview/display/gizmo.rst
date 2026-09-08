
***************
Viewport Gizmos
***************

.. reference::

   :Mode:      All Modes
   :Location:  :menuselection:`Header --> Gizmos`

.. _bpy.types.SpaceView3D.show_gizmo:

Clicking :bl-icon:`gizmo` (Show Gizmos) toggles all gizmos in the 3D Viewport.
The drop-down button displays a popover with more detailed settings,
which are described below.


Viewport Gizmos
===============

Navigate
   Enable/disable the :ref:`navigation gizmo <navigation-gizmo>`.
Active Tool
   Enable/disable the gizmo of the active tool.
Active Object
   Enable/disable the Object Gizmos for the active element (see below).


Object Gizmos
=============

Object Gizmos allow mouse-controlled translation, rotation and scaling in the 3D Viewport.
While they're called "object" gizmos in the popover, they also apply to other transformable
elements such as mesh vertices.

There is a separate gizmo for each operation.
Each gizmo can be used separately or in combination with the others.

A gizmo always has three color-coded axes: X (red), Y (green), and Z (blue).
You can drag an axis with :kbd:`LMB` to transform along it. The Move and Scale gizmos
additionally have small colored squares for transforming along two axes in one go.

Various modifier keys can be used:

- Holding :kbd:`Ctrl` at any time will toggle :doc:`snapping </editors/3dview/controls/snapping>`
  and also make rotation and scaling work in coarse increments.
- Holding :kbd:`Shift` *after* pressing :kbd:`LMB` will do the opposite of the above, "slowing down"
  the transformation relative to mouse movement to allow finer adjustments.
- Holding :kbd:`Shift` *before* pressing :kbd:`LMB` will perform the transformation in the plane
  that's perpendicular to the clicked axis. See :ref:`view3d-transform-plane-lock`.

The Gizmos popover has the following settings for object gizmos:

Orientation
   The orientation to use for the gizmo. *Default* means to use the viewport's
   :doc:`Transform Orientation </editors/3dview/controls/orientation>`.
   The other options override it.
Move
   Show the gizmo to control the location.
   Dragging the small white circle allows free movement in the viewing plane.
Rotate
   Show the gizmo to control the rotation.
   Dragging the large white circle allows rotation around the viewing direction.
   Dragging the translucent white disc within that circle (only visible when
   hovering over the gizmo) allows :ref:`trackball rotation <view3d-transform-trackball>`.
Scale
   Show the gizmo to control the scale.
   Dragging the area between the small and large white circles scales along all three axes.

The latter three options are also available in a pie menu
if you have the *Grave Accent / Tilde Action* in the
:doc:`Keymap Preferences </editors/preferences/keymap>` set to *Gizmos*.

.. note::

   If you're using a tool that's tied to a particular gizmo setup (the *Move*, *Rotate*,
   *Scale* and *Transform* tools), the Move/Rotate/Scale checkboxes won't have any effect.

.. list-table::
   :widths: 1 1 1 1

   * - .. figure:: /images/editors_3dview_display_gizmo_options-translate.png

          Move.

     - .. figure:: /images/editors_3dview_display_gizmo_options-rotate.png

          Rotate.

     - .. figure:: /images/editors_3dview_display_gizmo_options-scale.png

          Scale.

     - .. figure:: /images/editors_3dview_display_gizmo_options-all.png

          Combination.

.. seealso::

   The :ref:`Gizmo Preferences <bpy.types.PreferencesView.gizmo_size>`.


Empty
=====

Gizmo settings for :doc:`empties </modeling/empties>`.

Image
   Show the gizmo to adjust the image size and position.
Force Field
   Show the gizmo to adjust the :doc:`force field </physics/forces/force_fields/introduction>`.


Light
=====

Gizmo settings for :doc:`lights </render/lights/light_object>`.

Size
   Show the gizmo to adjust the Spot Size of spotlights.
Look At
   Show the gizmo to adjust the direction of lights.


Camera
======

Gizmo settings for :doc:`cameras </render/cameras>`.

Lens
   Show the gizmo to adjust the focal length (for Perspective cameras)
   or orthographic scale (for Orthographic cameras).
Focus Distance
   Enable the gizmo for adjusting the focus distance. To see this gizmo,
   you need to enable the :menuselection:`Viewport Display --> Limits` checkbox
   in the camera's properties (green camera icon).
