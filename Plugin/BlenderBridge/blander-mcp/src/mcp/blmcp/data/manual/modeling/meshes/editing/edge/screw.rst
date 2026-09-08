.. _bpy.ops.mesh.screw:

*****
Screw
*****

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Edge --> Screw`

The *Screw* operator extrudes geometry along a helix. You can use it to create screws, springs,
sea shells and so on.

While it's similar to the :doc:`Screw Modifier </modeling/modifiers/generate/screw>`,
there are some important differences:

.. list-table::
   :header-rows: 1

   * - Screw operator
     - Screw modifier
   * - Works in world space.
     - Works in object space.
   * - Extrudes only the selected geometry.
     - Extrudes all geometry.
   * - The centerpoint can be specified manually.
     - The centerpoint is always the object's origin.
   * - One revolution is always 360°.
     - The angle can be chosen freely.
   * - The height offset of each revolution is calculated automatically based on the geometry.
     - The height offset must be specified manually.
   * - Each revolution can also have a radial offset away from/towards the central axis
       (again determined by the geometry).
     - The radius stays constant.

As described above, the Screw operator automatically determines the height offset and radial
offset to apply after each revolution. It does this by looking for the endpoints of an open profile --
a series of connected edges that don't form a closed loop. The geometry is extruded so that the
profile's top vertex in one revolution will coincide with the bottom vertex in the next.

The most common use case is extruding such an open profile. You're not limited to this, however.
As long as there is one open profile in the selection -- even just a single loose edge --
you can also extrude closed profiles and even geometry with faces.

You can see some examples below.

.. list-table::

   * - .. _fig-mesh-screw-wood:

       .. figure:: /images/modeling_meshes_editing_edge_screw_example-shell.png

          Wood Screw.

     - .. _fig-mesh-screw-spring:

       .. figure:: /images/modeling_meshes_editing_edge_screw_example-spring.png

          Spring.


Usage
=====

First, make sure you have an open profile in your mesh. If you want to extrude anything else
(such as one or more circles), you should create an open profile next to it.

Once that's done, enter *Edit Mode* and select the geometry you want to extrude,
making sure to include exactly one open profile. If you have fewer or more, the operator will
fail with the error "You have to select a string of connected vertices too."

Make sure the :doc:`/editors/3dview/3d_cursor` is at the centerpoint around which you want
the geometry to turn. Also make sure that the vertical axis on your screen matches the direction
of the axis around which it should turn. The most common example is turning around the global Z
axis: for that, you'd place the 3D Cursor at the world origin and switch to an orthographic side view.

Now you're ready to run the operator: open the *Edge* menu (by clicking it in the 3D Viewport's
header or pressing :kbd:`Ctrl-E`) and click *Screw*.

You can change the number of steps and turns in the
:ref:`Adjust Last Operation <bpy.ops.screen.redo_last>` panel.

If you only created an open profile to guide the extrusion (not because you wanted its geometry),
you can select its extruded faces by hovering over one and pressing :kbd:`L`,
then delete them by pressing :kbd:`X` or :kbd:`Delete`.


Options
=======

.. figure:: /images/modeling_meshes_editing_edge_screw_interactive-panel.png

   Screw panel (in Edit Mode).

Steps
   The number of extrusions to be done for each 360° turn.
Turns
   The number of turns to create.
Center X, Y, Z
   The world space coordinates of the centerpoint around which to spin the geometry.
   Initially this is the location of the 3D Cursor.
Axis X, Y, Z
   The direction vector around which to spin the geometry.
   Initially this is the screen-space vertical axis (so the global Z axis when in a
   side view or the global Y axis when in top view). By inverting the *Axis*,
   you can flip between going clockwise and counterclockwise.

.. tip::
   You can use the :doc:`Align View to Active </editors/3dview/navigate/align>`
   menu item to align the viewport, and thereby the *Axis*, to a certain item
   in the scene.

Notice that the *Axis* only determines how the geometry spins "horizontally" around
the centerpoint. It doesn't determine how the geometry moves "vertically."
Instead, the geometry always moves by a distance and direction given by the endpoints
of the open profile, and goes downward in the object's local space.


Examples
========

Creating a Spring
-----------------

First, let's create a circle to serve as the spring's cross section:

#. Open Blender and delete the default Cube.
#. Add a circle by pressing :kbd:`Shift-A` and selecting :menuselection:`Mesh --> Circle`.
#. Set the *Location X* property of this new object to -3 and its *Rotation X* property to 90°.
#. Enter *Edit Mode* by pressing :kbd:`Tab`.
#. Switch to the *Front Orthographic* view by pressing :kbd:`Numpad1`.

.. figure:: /images/modeling_meshes_editing_edge_screw_circle-moved-x-3units.png

   Extrusion profile created.

Next, let's create a vertical line to specify the distance between spring loops:

#. Deselect all vertices by clicking on an empty space or pressing :kbd:`Alt-A`.
#. Click :kbd:`Ctrl-RMB` twice to create two vertices connected by an edge.
#. Select both vertices and press :kbd:`S X 0 Return` to ensure they have the same X coordinate.
   (This is necessary to keep the spring's radius constant.)

.. figure:: /images/modeling_meshes_editing_edge_screw_spring-profile-ready.png

   Guide profile created.

Now, we're ready to create the spring:

#. Select both the circle and the line by pressing :kbd:`A`.
#. Click :menuselection:`Edge --> Screw`.
#. Adjust the *Steps* and *Turns* to your liking.
#. Try changing *Axis Z* to -1 and see that this makes the spring turn the other way.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_edge_screw_spring-counterclockwise.png

          Counterclockwise direction.

     - .. figure:: /images/modeling_meshes_editing_edge_screw_spring-clockwise.png

          Flipped to Clockwise direction.

You can get some interesting results by making the *Axis* diagonal (e.g. keeping *Axis Z*
at -1 and setting *Axis X* to 1). Notice that each individual spring loop is inclined by 45°,
but that after each loop, we still go down vertically (in the direction of the guide line).

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_edge_screw_angular-vector-example1.png

     - .. figure:: /images/modeling_meshes_editing_edge_screw_angular-vector-example2.png


Creating a Screw Spindle
------------------------

The Screw operator is perfectly suited for creating helices without any gaps between the turns.

#. Open Blender and enter *Edit Mode* for the default cube.
#. Delete all vertices by pressing :kbd:`X` or :kbd:`Delete`.
#. Switch to the *Front Orthographic* view by pressing :kbd:`Numpad1`.
#. Click :kbd:`Ctrl-RMB` three times to create a profile like the one below.
#. Select the two vertices closest to the global Z axis and press :kbd:`S X 0 Return`
   to ensure they have the same X coordinate.
#. Select all three vertices and click :menuselection:`Edge --> Screw`.
#. Adjust the *Steps* and *Turns* to your liking.

.. list-table::

   * - .. _fig-mesh-screw-spindle:

       .. figure:: /images/modeling_meshes_editing_edge_screw_perfect-spindle-profile.png

          Profile for a screw spindle.

     - .. _fig-mesh-screw-generated-mesh:

       .. figure:: /images/modeling_meshes_editing_edge_screw_generated-perfect-spindle.png

          Result after running the Screw operator.

You can also create more interesting shapes, like this spiral "staircase":

.. list-table:: Ramp.

   * - .. figure:: /images/modeling_meshes_editing_edge_screw_ramp-like-profile.png

          Profile.

     - .. figure:: /images/modeling_meshes_editing_edge_screw_ramp-like-generated.png

          Generated mesh.


Creating a Screw Tip
--------------------

Until now, we've always made sure that the first and last vertex of the profile
have the same X coordinate, thereby keeping the radius of the helix constant.
However, nothing stops you from using different X coordinates and having the helix
shrink/expand along its height.

.. list-table::

   * - .. _fig-mesh-screw-start:

       .. figure:: /images/modeling_meshes_editing_edge_screw_profile-with-vector-angle.png

          Profile.

     - .. _fig-mesh-screw-start-mesh:

       .. figure:: /images/modeling_meshes_editing_edge_screw_generated-with-base-vector-angle.png

          Generated.
