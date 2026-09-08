.. index:: Editors; 3D Viewport

************
Introduction
************

The 3D Viewport is used to interact with the 3D scene for a variety of purposes,
such as modeling, animating, texture painting, etc.


Header Region
=============

.. figure:: /images/editors_3dview_introduction_3d-view-header-object-mode.png

   Object Mode header.

The header contains various menus and controls based on
the current :doc:`mode </editors/3dview/modes>`.
Its items are split into three groups:


Mode & Menus
------------

Mode :kbd:`Ctrl-Tab`
   The 3D Viewport has several :doc:`modes </editors/3dview/modes>`
   used for editing different kinds of data. For example, the default Object Mode
   would let you place a character in the scene, while Pose Mode would allow
   you to pose it.

   The shortcut :kbd:`Ctrl-Tab` brings up a pie menu for quick mode switching.
   If you have an :doc:`Armature </animation/armatures/introduction>` selected,
   it'll instead switch between Object Mode and Pose Mode.

   Pressing :kbd:`Tab` will switch between Object Mode and Edit Mode for objects
   that support it.

View
   This menu offers tools for :doc:`navigating </editors/3dview/navigate/introduction>` in 3D space.

The other menus depend on the current mode, Object Mode menus listed below:

Select
   Contains tools for :ref:`selecting <object-select-menu>` objects.
Add :kbd:`Shift-A`
   Contains a list of different :ref:`objects types <objects-types>` that can be added to the scene.
Object
   Contains tools for operating on :doc:`objects </scene_layout/object/editing/transform/introduction>`,
   such as duplicating them. A subset of these tools can also be accessed by right-clicking
   in the 3D Viewport.


Transform Controls
------------------

Transform Orientation :kbd:`Comma`
   Used to change the :doc:`Transform Orientation </editors/3dview/controls/orientation>`,
   which affects the rotation of the transform gizmo.
Pivot Point :kbd:`Period`
   Used to change the :doc:`Pivot Point </editors/3dview/controls/pivot_point/index>`,
   which affects the location of the transform gizmo.
Snapping :kbd:`Shift-Tab`
   Offers options for :doc:`snapping </editors/3dview/controls/snapping>` items
   to others that are nearby. You can hold :kbd:`Ctrl` to toggle snapping on/off temporarily
   (as long as the key is held).
Proportional Editing :kbd:`O`
   Used to smoothly transform unselected items that are near the selected ones.
   See :doc:`/editors/3dview/controls/proportional_editing`.


Display & Shading
-----------------

Object Type Visibility
   Change which types of objects are visible/selectable in the 3D Viewport.
   See :doc:`Object Type Visibility </editors/3dview/display/visibility>`.
Viewport Gizmos
   Change how :doc:`gizmos </editors/3dview/display/gizmo>` are
   displayed in the 3D Viewport.
Viewport Overlays
   Change how :doc:`overlays </editors/3dview/display/overlays>` are
   displayed in the 3D Viewport.

.. _bpy.ops.view3d.toggle_xray:

Toggle X-Ray :kbd:`Alt-Z`
   Make the whole scene transparent, allowing you to see and select items that would otherwise be occluded.
   This is a shortcut to the :ref:`X-Ray <bpy.types.View3DShading.show_xray>`
   option which can be found inside the Viewport Shading popover (see below).

   In Pose Mode, this same button controls a different setting with its own separate on/off state.
   Rather than making the scene transparent, it shows the armature in front of any geometry.

Viewport Shading
   Change the :doc:`shading </editors/3dview/display/shading>` of the 3D Viewport.


Toolbar Region
==============

The Toolbar contains tools depending on the current mode
(for example, modeling tools in *Edit Mode*, brush tools in *Sculpt Mode*...).

See :doc:`Tools </editors/3dview/toolbar/index>` for more information.


Sidebar Region
==============

The Sidebar region contains properties of the active object and tool,
as well as of the viewport itself.

See :doc:`Sidebar </editors/3dview/sidebar>` for more information.

Asset Shelf Region
==================

Depending on the current mode, the asset shelf may be available, providing quick access to assets
for this specific mode (for example pose assets in *Pose Mode*, brush assets in *Sculpt Mode*).

See :ref:`ui-region-asset_shelf` for more information.
