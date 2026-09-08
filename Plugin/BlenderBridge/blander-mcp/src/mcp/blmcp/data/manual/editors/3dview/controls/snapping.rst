.. _bpy.types.ToolSettings.use_snap:

********
Snapping
********

.. reference::

   :Mode:      Object, Edit, and Pose Mode
   :Location:  :menuselection:`Header --> Snapping`
   :Shortcut:  :kbd:`Shift-Tab`

.. figure:: /images/editors_3dview_controls_snapping_element-menu.png
   :align: right

   Snap menu.

Snapping makes it easy to align objects and mesh elements to others.
It can be toggled by clicking :bl-icon:`snap_off` (Snap Off) / :bl-icon:`snap_on` (Snap On)
in the 3D Viewport's header, or more temporarily by holding :kbd:`Ctrl`.

.. container:: lead

   .. clear

.. seealso::

   :doc:`Transform Modal Map </modeling/transform/modal_map>` for further
   keyboard shortcuts.


.. _bpy.types.ToolSettings.snap_target:

Snap Base
=========

.. reference::

   :Mode:      Object, Edit, and Pose Mode
   :Header:    :menuselection:`Snapping --> Snap Base`
   :Shortcut:  :kbd:`Shift-Ctrl-Tab`

Determines which point in the geometry will snap to the target.

:Closest:
   Snaps using the bounding box corner (in Object Mode) or vertex (in Edit Mode)
   that's closest to the target.
:Center:
   Snaps using the current transformation center, which is another word for the
   :doc:`pivot point </editors/3dview/controls/pivot_point/index>`.
   This option is especially useful in combination with the
   :doc:`3D Cursor </editors/3dview/3d_cursor>` for choosing the snapping
   point completely manually.
:Median:
   Snaps using the average position of the selected objects' origins (in Object Mode)
   or vertices (in Edit Mode).
:Active:
   Snaps using the origin (in Object Mode) or center (in Edit Mode) of the active element.

.. list-table::

   * - .. figure:: /images/editors_3dview_controls_snapping_target-closest.png

          Closest.

     - .. figure:: /images/editors_3dview_controls_snapping_target-median.png

          Median.

     - .. figure:: /images/editors_3dview_controls_snapping_target-active.png

          Active.


.. _bpy.types.ToolSettings.snap_elements_base:

Snap Target
===========

.. reference::

   :Mode:      Object, Edit, and Pose Mode
   :Header:    :menuselection:`Snapping --> Snap Target`
   :Shortcut:  :kbd:`Shift-Ctrl-Tab`

Determines the target which the selection will be snapped to.

:Increment:
   Snaps to an imaginary grid that starts at the selection's original location and has the same
   resolution as the viewport grid. In other words, it allows moving the selection in "increments"
   of the grid cell size.
:Grid:
   Snaps to the grid that's displayed in the viewport.
:Vertex:
   Snaps to the vertex that's closest to the mouse cursor.
:Edge:
   Snaps to the edge that's closest to the mouse cursor.
:Face:
   Snaps to the surface of the face under the mouse cursor.
   This is useful for :ref:`retopologizing <modeling-meshes-remesh-retopology>`.
:Volume:
   Snaps the selection to a depth that's centered *inside* the object under the cursor.
   This is useful for positioning an :doc:`Armature </animation/armatures/introduction>`
   bone so it's centered inside a character's arm, for example; the other snapping options
   would place it on the arm's surface instead.

   While Blender also has :doc:`Volume objects </modeling/volumes/introduction>`, this option
   is not related to those.
:Edge Center:
   Snaps to the centerpoint of the edge that's closest to the mouse cursor.
:Edge Perpendicular:
   Snaps to a specific point on the edge so that the line from the selection's original location
   (indicated by a white cross) to its new location is perpendicular to that edge.
:Face Center:
   Snaps to the centerpoint of the face under the mouse cursor.

.. tip::

   Multiple snapping modes can be enabled at once using :kbd:`Shift-LMB`.


.. _bpy.types.ToolSettings.snap_elements_individual:

Snap Target for Individual Elements
===================================

.. reference::

   :Mode:      Object, Edit, and Pose Mode
   :Header:    :menuselection:`Snapping --> Snap Target for Individual Elements`
   :Shortcut:  :kbd:`Shift-Ctrl-Tab`

:Face Project:
   Individually snaps each object (in Object Mode) or vertex (in Edit Mode) to the face found by
   projecting from the current viewing depth along the current viewing direction. This can be used for
   bending a flat sheet so it snugly fits against a curved surface, for example.
:Face Nearest:
   Individually snaps each object or vertex to the face that's closest to its new location.
   Contrary to *Face Project*, this allows snapping to occluded geometry.

.. seealso::

   Shrinkwrap
   :doc:`constraint </animation/constraints/relationship/shrinkwrap>` /
   :doc:`modifier </modeling/modifiers/deform/shrinkwrap>`.

Target Selection
================

Sets more detailed snapping options. The available options depend on the mode
(Object/Edit) as well as the :ref:`Snap Target <bpy.types.ToolSettings.snap_elements_base>`.

.. _bpy.types.ToolSettings.use_snap_align_rotation:

Align Rotation to Target
   Rotate the selection so that its Z axis gets aligned to the normal of the target.

.. _bpy.types.ToolSettings.use_snap_backface_culling:

Backface Culling
   Exclude back-facing geometry from snapping.

.. _bpy.types.ToolSettings.use_snap_self:

Include Active :guilabel:`Edit Mode`
   Snap to other mesh elements of the active object.

   This option is ignored if
   :doc:`Proportional Editing </editors/3dview/controls/proportional_editing>`
   is enabled.

.. _bpy.types.ToolSettings.use_snap_edit:

Include Edited :guilabel:`Edit Mode`
   Snap to other objects that are also in Edit Mode.

.. _bpy.types.ToolSettings.use_snap_nonedit:

Include Non-Edited :guilabel:`Edit Mode`
   Snap to other objects that are not in Edit Mode.

.. _bpy.types.ToolSettings.use_snap_selectable:

Exclude Non-Selectable
   Snap only to objects that are :ref:`selectable <bpy.types.ObjectBase.select>`.

.. _bpy.types.ToolSettings.use_snap_grid_absolute:

Absolute Increment Snap :guilabel:`Increment`
   Snap to the viewport grid (instead of moving by increments of the grid cell size).
   This is similar to setting the *Snap Target* to *Grid*, except that the latter moves the selection to the
   grid point closest to the mouse cursor.

.. _bpy.types.ToolSettings.use_snap_peel_object:

Snap Peel Object :guilabel:`Volume`
   If the target object is composed of several disconnected mesh islands that
   intersect each other, *Snap To Volume* will normally snap to the island under the
   mouse cursor, ignoring the others. Enabling *Snap Peel Object* instead
   treats the target object as one connected whole, looking only at the "peel"
   (outer surface) while ignoring inner/enclosed faces.

.. _bpy.types.ToolSettings.use_snap_to_same_target:

Snap to Same Target :guilabel:`Face Nearest`
   Snap only to the object which the selection was nearest to before starting
   the transformation.

.. _bpy.types.ToolSettings.snap_face_nearest_steps:

Face Nearest Steps :guilabel:`Face Nearest` :guilabel:`Edit Mode`
   Breaks the overall transformation into multiple steps, performing a snap each time.
   This can give better results in certain cases.


.. _bpy.types.ToolSettings.use_snap_translate:
.. _bpy.types.ToolSettings.use_snap_rotate:
.. _bpy.types.ToolSettings.use_snap_scale:

Affect
======

Specifies which transformations are affected by snapping.
By default, snapping only happens while moving something,
but it can also be enabled for rotating and scaling.


.. _bpy.types.ToolSettings.snap_angle_increment_3d:
.. _bpy.types.ToolSettings.snap_angle_increment_3d_precision:

Rotation Increment
==================

Angle used in incremental snapping for the rotation operator.
The second value is the *Rotation Precision Increment*, used for finer transformations
and activated by default with the :kbd:`Shift` key.
