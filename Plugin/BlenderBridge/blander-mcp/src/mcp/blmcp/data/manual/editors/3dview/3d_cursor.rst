.. _bpy.types.View3DCursor:
.. _editors-3dview-3d_cursor:

*********
3D Cursor
*********

The 3D Cursor is a point in space that has both a location and a rotation.
It's used for a number of purposes. For example, it defines where newly
added objects are placed, and can also be used to manually position and orient
the transform gizmo (see :doc:`Pivot Point </editors/3dview/controls/pivot_point/index>`
and :doc:`Transform Orientation </editors/3dview/controls/orientation>`).
Some tools, such as :doc:`Bend </modeling/meshes/editing/mesh/transform/bend>`,
also use the Cursor.


Placement
=========

There are a few methods to position the 3D Cursor.


.. _bpy.ops.view3d.cursor3d:

Direct Placement with the Mouse
-------------------------------

.. reference::

   :Mode:      Object, Edit, and Pose Mode
   :Tool:      Cursor
   :Shortcut:  :kbd:`Shift-RMB`

.. figure:: /images/editors_3dview_3d-cursor_two-view-positioning.png
   :align: center

   Positioning the 3D Cursor with two orthogonal views.

The Cursor tool offers the most flexibility. Simply select it in the Toolbar
and click a point in the scene with :kbd:`LMB` to place the 3D Cursor there.
In the tool settings, you can choose how it should be oriented:
by default, it matches the view orientation, but you can also make it
match the surface normal of a piece of geometry,
or the :doc:`transform orientation </editors/3dview/controls/orientation>`.

Alternatively, you can press :kbd:`Shift-RMB` with any tool selected.
In this case, the 3D Cursor will always be aligned to the view orientation.

For accuracy you should use two perpendicular orthogonal 3D Viewports,
i.e. any combination of top :kbd:`Numpad7`, front :kbd:`Numpad1` and side :kbd:`Numpad3`.
That way you can control the positioning along two axes in one view and
determine the depth in the other.

By default, the depth of the geometry under the cursor is used.
This can be disabled using the *Cursor Surface Project* toggle
in the :doc:`Preferences </editors/preferences/editing>`.


Sidebar
-------

.. reference::

   :Mode:      All Modes
   :Panel:     :menuselection:`Sidebar region --> View --> 3D Cursor`

.. figure:: /images/editors_3dview_3d-cursor_panel.png

   The 3D Cursor panel of the Sidebar region.

The 3D Cursor can also be positioned and oriented by editing the
respective values in the Sidebar.


Snapping
--------

.. reference::

   :Mode:      Object, Edit, and Pose Mode
   :Menu:      :menuselection:`Object/Mesh/... --> Snap --> Cursor to ...`
   :Shortcut:  :kbd:`Shift-S`

One more way of positioning the 3D Cursor is through the Snap menu,
which allows you to move the Cursor to the origin of the selected object
for example.
