
******************
Grease Pencil Menu
******************

Transform
=========

Strokes can be edited by transforming the locations of points.


Move, Rotate & Scale
--------------------

.. reference::

   :Mode:      Edit Mode
   :Tool:      :menuselection:`Toolbar --> Move, Rotate, Scale`
   :Menu:      :menuselection:`Grease Pencil --> Transform --> Move, Rotate, Scale`
   :Shortcut:  :kbd:`G`, :kbd:`R`, :kbd:`S`

Like other elements in Blender, points and strokes can be
moved :kbd:`G`, rotated :kbd:`R` or scaled :kbd:`S` as described in
the :doc:`Basic Transformations </scene_layout/object/editing/transform/introduction>` section.
When in *Edit Mode*,
:doc:`Proportional Editing </editors/3dview/controls/proportional_editing>`
is also available for the transformation actions.


Transform Snapping
------------------

Basic move, rotate and scale transformations for selected points/strokes.
See :doc:`Move, Rotate, Scale Basics </modeling/meshes/editing/mesh/transform/basic>` for more information.


Tools
-----

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Grease Pencil --> Transform`
   :Tool:      :menuselection:`Toolbar --> Bend/Shear`

The *Bend*, *Shear*, *To Sphere*, *Extrude* and *Shrink Fatten* transform tools are described
in the :doc:`Editing tools </grease_pencil/modes/edit/tools/index>` section.


Mirror
======

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Grease Pencil --> Mirror`
   :Shortcut:  :kbd:`Ctrl-M`

The *Mirror* tool is also available, behaving exactly the same as with
:doc:`mesh vertices </modeling/meshes/editing/mesh/mirror>`.


.. _bpy.ops.grease_pencil.snap_to_grid:
.. _bpy.ops.grease_pencil.snap_to_cursor:
.. _bpy.ops.grease_pencil.snap_cursor_to_selected:
.. _bpy.ops.view3d.snap_cursor_to_center:

Snap
====

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Grease Pencil --> Snap`
   :Shortcut:  :kbd:`Shift-S`

:doc:`Mesh snapping </editors/3dview/controls/snapping>`
also works with Grease Pencil components.


Active Layer
============

.. reference::

   :Mode:      Edit Mode, Draw Mode
   :Menu:      :menuselection:`Grease Pencil --> Active Layer`
   :Shortcut:  :kbd:`Y`

Select the active layer.


Animation
=========

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Grease Pencil --> Animation`
   :Shortcut:  :kbd:`I`

The stroke animation operations are described in the :doc:`Animation </grease_pencil/animation/tools>` section.


Interpolate Sequence
====================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Grease Pencil --> Interpolate Sequence`

See :ref:`bpy.ops.grease_pencil.interpolate_sequence`.


.. _bpy.ops.grease_pencil.duplicate_move:

Duplicate
=========

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Grease Pencil --> Duplicate`
   :Shortcut:  :kbd:`Shift-D`

Duplicates the selected elements, without creating any connections
with the rest of the strokes (unlike *Extrude*, for example),
and places the duplicate at the location of the original elements.


.. _bpy.ops.grease_pencil.stroke_split:

Split
=====

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Grease Pencil --> Split`
   :Shortcut:  :kbd:`V`

The *Split* operator separates the selected portion of a curve from the rest,
creating a new, independent curve segment.
This curve can then be moved or altered without affecting the other curve.

- If a segment of the curve is selected, it will be split off
  as a new curve that can be moved or edited independently.
- If only a single control point is selected, it will be duplicated as a loose control point,
  while the original remains attached to the rest of the curve.


.. _bpy.ops.grease_pencil.copy:

Copy
====

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Grease Pencil --> Copy`
   :Shortcut:  :kbd:`Ctrl-C`

Copy the selected points/strokes to the clipboard.


.. _bpy.ops.grease_pencil.paste:

Paste
=====

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Grease Pencil --> Paste`
   :Shortcut:  :kbd:`Ctrl-V`

Paste Grease Pencil points or strokes from the internal clipboard to the active layer.

Paste on Back :kbd:`Shift-Ctrl-V`
    Add pasted strokes behind all strokes.
Keep World Transform
   Keep the world transform of strokes from the clipboard unchanged.


Show/Hide
=========

Contains operators to adjust the visibility of points and strokes in the viewport.


Show All Layers
---------------

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Grease Pencil --> Show/Hide --> Show All Layers`
   :Shortcut:  :kbd:`Alt-H`

Shows all Grease Pencil :doc:`layers </grease_pencil/properties/layers>`.


.. _bpy.ops.grease_pencil.layer_hide:

Hide Active Layer
-----------------

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Grease Pencil --> Show/Hide --> Hide Active Layer`
   :Shortcut:  :kbd:`H`

Hides the active Grease Pencil :doc:`layers </grease_pencil/properties/layers>`.


Hide Inactive Layers
--------------------

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Grease Pencil --> Show/Hide --> Hide Active Layer`
   :Shortcut:  :kbd:`Shift-H`

Hides the all Grease Pencil :doc:`layers </grease_pencil/properties/layers>` except the active layer.


.. _bpy.ops.grease_pencil.separate:

Separate
========

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Grease Pencil --> Separate`
   :Shortcut:  :kbd:`P`

Separate different elements into new Grease Pencil objects based on specific criteria.

Selection
   Separates the selected points or strokes into a new object.
By Material
   Separates the geometry by creating a new object for each material.
By Layer
   Separates the geometry by creating a new object for each layer.
   See :doc:`2D Layers </grease_pencil/properties/layers>` for more information.


Clean Up
========

These tools help to cleanup degenerate geometry on the strokes.


.. _bpy.ops.grease_pencil.clean_loose:

Clean Loose Points
------------------

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Grease Pencil --> Clean Up --> Delete Loose Points`

Removes strokes with only a few points.

Limit
   The number of points to consider a stroke as loose.


.. _bpy.ops.grease_pencil.frame_clean_duplicate:

Delete Duplicate Frames
-----------------------

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Grease Pencil --> Clean Up --> Delete Duplicate Frames`

Removes any duplicate keyframes.


.. _bpy.ops.grease_pencil.stroke_merge_by_distance:

Merge by Distance
-----------------

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Grease Pencil --> Clean Up --> Merge by Distance`

Simplifies a stroke by merging the selected points that are closer than a specified distance to each other.
Note, unless using *Unselected*, selected points must be contiguous, else they will not be merged.

Merge Distance
   Sets the distance threshold for merging points.
Unselected
   Allows points in selection to be merged with unselected points.
   When disabled, selected points will only be merged with other selected ones.


.. _bpy.ops.grease_pencil.reproject:

Reproject Strokes
-----------------

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Grease Pencil --> Clean Up --> Reproject`

Sometimes you may have drawn strokes unintentionally in different locations in the 3D space
but they look right from a certain plane or from the camera view.
You can use Reproject to flatten all the selected strokes from a certain viewpoint.

Reprojected Type
   :Front: Reproject selected strokes onto the front plane (XZ).
   :Side: Reproject selected strokes onto the side plane (YZ).
   :Top: Reproject selected strokes onto the top plane (XY).
   :View: Reproject selected strokes onto the current view.
   :Surface: Reproject selected strokes onto the mesh surfaces.

      Surface Offset
         When Surface Mode is activated controls the stroke offset from the object.
   :Cursor: Reproject selected strokes onto 3D cursor rotation.

Keep Original
   Maintains the original strokes after applying the tool.

.. list-table::

   * - .. figure:: /images/grease-pencil_modes_edit_grease-pencil-menu_reproject-strokes-1.png
          :width: 200px

          Original drawing from the front view.

     - .. figure:: /images/grease-pencil_modes_edit_grease-pencil-menu_reproject-strokes-2.png
          :width: 200px

          Original drawing in the 3D Viewport.

     - .. figure:: /images/grease-pencil_modes_edit_grease-pencil-menu_reproject-strokes-3.png
          :width: 200px

          Strokes reprojected onto the front plane to fix strokes misalignment.

     - .. figure:: /images/grease-pencil_modes_edit_grease-pencil-menu_reproject-strokes-1.png
          :width: 200px

          Drawing after reprojection operation from the front view.


.. _bpy.ops.grease_pencil.outline:

Outline
=======

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Grease Pencil --> Outline`

The *Outline* operator converts selected Grease Pencil strokes into closed perimeter shapes.
It creates new strokes around the outer boundary of the original stroke,
effectively generating a filled outline with adjustable thickness.

View
   Defines the projection method used to generate the outline:

   :View: Use the current viewport perspective as the projection plane.
   :Front: Use the X-Z axes as the projection plane (front view).
   :Side: Use the Y-Z axes as the projection plane (side view).
   :Top: Use the X-Y axes as the projection plane (top view).
   :Camera: Use the active camera's perspective as the projection plane.
Radius
   Sets the thickness of the outline on both sides of the original stroke.
   Higher values result in a wider perimeter.
Offset Factor
   Scales the stroke outline inward or outward.
   - Positive values push the perimeter outward.
   - Negative values pull it inward.
   - A value of 0 centers the perimeter on the original stroke.
Corner Subdivisions
   Number of subdivisions used to smooth corners at stroke endpoints and joints.
   Higher values result in smoother corners but increase stroke complexity.

.. list-table::

   * - .. figure:: /images/grease-pencil_modes_edit_stroke-menu_outline-1.png
          :width: 320px

          Original stroke.

     - .. figure:: /images/grease-pencil_modes_edit_stroke-menu_outline-2.png
          :width: 320px

          Stroke after applying the *Outline* operator.


Delete
======

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Grease Pencil --> Delete`
   :Shortcut:  :kbd:`X`, :kbd:`Delete`

Opens a pop-up menu with operators to remove geometry from the Grease Pencil object.

Frames
   Deletes all the strokes at the current frame and in the current layer/channel.


.. _bpy.ops.grease_pencil.delete:

Delete
------

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Grease Pencil --> Delete --> Delete`

Deletes the selected points.
When only one point remains, there is no more visible stroke,
and when all points are deleted, the stroke itself is deleted.


.. _bpy.ops.grease_pencil.dissolve:

Dissolve
--------

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Grease Pencil --> Delete --> Dissolve`
   :Shortcut:  :kbd:`Ctrl-X`

Dissolving removes points between other points and connect the remaining points.

:kbd:`Ctrl-X` Opens a pop-up to choose the dissolve type.

Dissolve
   Deletes the selected points without splitting the stroke.
   The remaining points in the strokes stay connected.
Dissolve Between
   Deletes all the points between the selected points without splitting the stroke.
   The remaining points in the strokes stay connected.
Dissolve Unselect
   Deletes all the points that are not selected in the stroke without splitting the stroke.
   The remaining points in the strokes stay connected.


Delete Active Keyframe (Active Layer)
-------------------------------------

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Grease Pencil --> Delete --> Delete Active Keyframe (Active Layer)`

Deletes all the strokes at the current frame in the active layer.


Delete Active Keyframes (All Layers)
------------------------------------

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Grease Pencil --> Delete --> Delete Active Keyframes (All Layers)`
   :Shortcut:  :kbd:`Shift-Delete`

Deletes all the strokes at the current frame in all layer.
