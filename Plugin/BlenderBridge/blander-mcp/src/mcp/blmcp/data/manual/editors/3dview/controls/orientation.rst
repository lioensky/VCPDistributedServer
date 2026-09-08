.. _bpy.types.TransformOrientation:
.. todo/Review: {{review|Need to change and explain the behavior of the transform orientation.
   It is toggled between the chosen orientation and
   the global orientation when transformations are made by shortcuts}}.

*********************
Transform Orientation
*********************

.. reference::

   :Mode:      Object and Edit Modes
   :Panel:     :menuselection:`Header --> Transform Orientation`
   :Shortcut:  :kbd:`Comma`

The *Transform Orientation* determines the orientation of the
:doc:`Object Gizmo </editors/3dview/display/gizmo>`.
Changing this orientation can make it easier to perform
transformations in the direction you want.

.. figure:: /images/editors_3dview_controls_orientation_demo.png
   :align: center

   With the default Global transform orientation (left) it's tricky to
   move the plane in the direction it's facing, but with Local (right)
   it's easy.

The Transform Orientation can be changed using a
selector in the 3D Viewport's header:

.. figure:: /images/editors_3dview_controls_orientation_menu.png

   Transform Orientation selector.

The orientation can also be changed temporarily while performing
a hotkey-based transformation with
:doc:`axis locking </scene_layout/object/editing/transform/control/axis_locking>`.
For example, if you first press :kbd:`G` to start moving an object,
then :kbd:`X` to lock to the orientation's X axis, and finally :kbd:`X` a second time,
you'll get a lock to an alternative orientation:
the Local orientation if it was Global previously, and the Global orientation
otherwise.

In addition to the builtin orientations,
you can also define your own (see `Custom Orientations`_ below).


.. _bpy.types.TransformOrientationSlot.type:

Orientations
============

Global
   Align the transformation axes to world space.
   The world axes are shown by the :ref:`Navigation Gizmo <navigation-gizmo>`
   in the top right corner of the viewport, as well as the *Grid Floor*.

Local
   Align the transformation axes to the active object's orientation.

Normal
   In Edit Mode, orient the transformation axes so that the Z axis of the gizmo
   matches the average :doc:`Normal </modeling/meshes/editing/mesh/normals>`
   of the selected elements.

   In Object Mode, this is equivalent to *Local* orientation.

Gimbal
   Orient the transformation axes to visualize the workings of the object's
   :ref:`Rotation Mode <bpy.types.Object.rotation_mode>`.
   This is specifically useful for the Euler modes,
   where the object is rotated one axis at a time: the rotation axes don't
   stay perpendicular to each other and might even overlap, a phenomenon
   known as :term:`gimbal lock` that complicates animation.

View
   Align the transformation axes to the view (meaning they change as you orbit around):

   - X: Left/Right
   - Y: Up/Down
   - Z: Towards/Away from the screen

Cursor
   Align the transformation axes to the :doc:`3D Cursor </editors/3dview/3d_cursor>`.

Parent
   Align the transformation axes to the :doc:`Parent </scene_layout/object/editing/parent>`.


Examples
--------

.. list-table:: Cube with the rotation gizmo active in multiple transform orientations.
   :widths: 1 1 1

   * - .. figure:: /images/editors_3dview_controls_orientation_manipulator-global-1.png

          Default cube with Global transform orientation selected.

     - .. figure:: /images/editors_3dview_controls_orientation_manipulator-global-2.png

          Rotated cube with Global orientation, gizmo has not changed.

     - .. figure:: /images/editors_3dview_controls_orientation_manipulator-local.png

          Local orientation, gizmo matches the object's rotation.

   * - .. figure:: /images/editors_3dview_controls_orientation_manipulator-normal.png

          Normal orientation, in Edit Mode.

     - .. figure:: /images/editors_3dview_controls_orientation_manipulator-gimbal.png

          Gimbal transform orientation.

     - .. figure:: /images/editors_3dview_controls_orientation_manipulator-view.png

          View transform orientation.
   * - .. figure:: /images/editors_3dview_controls_orientation_manipulator-parent.png

          Parent transform orientation. Cube parented to rotated empty.

     - ..

     - ..


.. _bpy.types.TransformOrientation.name:
.. _bpy.ops.transform.delete_orientation:

Custom Orientations
-------------------

.. reference::

   :Mode:      Object and Edit Modes
   :Panel:     :menuselection:`Header --> Transform Orientation`

You can define custom transform orientations using objects or mesh elements.
Custom orientations defined from an object use the *Local* orientation of that object,
whereas those defined from mesh elements (vertices, edges, faces)
use the average *Normal* orientation of those elements.

.. figure:: /images/editors_3dview_controls_orientation_custom.png

   Transform Orientation panel.

The *Transform Orientation* panel, found in the header of the 3D Viewport,
can be used to select, add, remove, and rename transform orientations.

The default name for these orientations is derived from the selection.
If it's an object it will take that object's name,
if it's an edge it will be titled "Edge", and so on.


.. _bpy.ops.transform.create_orientation:

Create Orientation
^^^^^^^^^^^^^^^^^^

To create a custom orientation, select an object or mesh element(s) and
click the "+" button in the *Transform Orientation* panel.

.. figure:: /images/editors_3dview_controls_orientation_custom-name.png

   Create Orientation :ref:`bpy.ops.screen.redo_last` panel.

Right after creating the orientation,
the *Create Orientation* :ref:`bpy.ops.screen.redo_last` panel gives a few options:

Name
   Text field for naming the new orientation.
Use View
   The new orientation will be aligned to the view space.
Use After Creation
   The new orientation stays selected.
Overwrite Previous
   If the new orientation is given an existing name, a suffix will be added
   to it's name to avoid overwriting the existing orientation,
   unless *Overwrite Previous* is checked, in which case it will be overwritten.


Delete Orientation
^^^^^^^^^^^^^^^^^^

To delete a custom orientation, simply select it and click the × button.
