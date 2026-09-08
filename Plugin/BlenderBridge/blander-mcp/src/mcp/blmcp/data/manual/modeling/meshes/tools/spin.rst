.. _bpy.ops.mesh.spin:
.. _tool-mesh-spin:

****
Spin
****

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Extrude --> Spin`
   :Tool:      :menuselection:`Toolbar --> Spin`

The *Spin* tool extrudes (or duplicates it if the selection is manifold) the selected elements,
rotating around a specific point and axis.

Use the tool to create the sort of objects that you would produce on a lathe
(this tool is often called "lathe" tool or "sweep" tool in the literature, for this reason).
In fact, it does a sort of circular extrusion of your selected elements,
centered on the 3D cursor, and around the axis perpendicular to the working view...

- The point of view will determine around which axis the extrusion spins...
- The position of the 3D cursor will be the center of the rotation.


Tool Settings
=============

Steps
   Specifies how many copies will be extruded along the "sweep".
Use Duplicates
   When enabled, will keep the original selected elements as separated islands in the mesh
   (i.e. unlinked to the result of the spin extrusion).
Axis
   Specifies the axis to use as the pivot of the spin operation.


Options
=======

Steps
   Specifies how many copies will be extruded along the "sweep".
Angle
   Specifies the angle "swept" by this tool, in degrees (e.g. set it to 180 for half a turn).
Auto Merge
   Automatically merges the first a last duplicates,
   if they make a full revolution which results in overlapping geometry.
Flip Normals
   Reverses the :term:`Normal's <Normal>` direction for any resulting geometry.
Center X, Y, Z
   Specifies the center of the spin. By default it uses the cursor position.
Axis X, Y, Z
   Specify the spin axis as a vector. By default it uses the view axis (viewport).


Example
=======

.. _fig-mesh-spin-glass:

.. figure:: /images/modeling_meshes_tools_spin_glass-profile.png
   :width: 300px

   Glass profile.

First, create a mesh representing the profile of your object.
If you are modeling a hollow object, it is a good idea to thicken the outline.
Fig. :ref:`fig-mesh-spin-glass` shows the profile for a wine glass we will model as a demonstration.

We will be rotating the object around the cursor in the top view,
so switch to the top view with :kbd:`Numpad7`.

.. _fig-mesh-spin-glass-top:

.. figure:: /images/modeling_meshes_tools_spin_glass-profile-before.png
   :width: 300px

   Glass profile, top view in Edit Mode, just before spinning.

Place the cursor along the center of the profile by entering Edit Mode
and selecting one of the vertices along the center, and snapping the 3D cursor to
that location with :menuselection:`Mesh --> Snap --> Cursor to Selection`.
(Fig. :ref:`fig-mesh-spin-glass-top`) shows the wine glass profile from
top view, with the cursor correctly positioned.

Select all the vertices with :kbd:`A` and select the *Spin* tool from the Toolbar
and use the Gizmo to spin the vertices. Fig. :ref:`fig-mesh-spin-profile` shows the result of a successful spin.


Angle
-----

.. _fig-mesh-spin-profile:

.. list-table:: Spun profile.

   * - .. figure:: /images/modeling_meshes_tools_spin_spun-profile360.png
          :width: 320px

          Spun profile using an angle of 360.

     - .. figure:: /images/modeling_meshes_tools_spin_spun-profile120.png
          :width: 320px

          Spun profile using an angle of 120.


Duplicate
---------

.. list-table::

   * - .. figure:: /images/modeling_meshes_tools_spin_result.png
          :width: 320px

          Result of spin operation.

     - .. figure:: /images/modeling_meshes_tools_spin_dubli.png
          :width: 320px

          Result of *Duplicate* enabled.


Merge Duplicates
----------------

.. _fig-mesh-screw-duplicate:

.. figure:: /images/modeling_meshes_tools_spin_dublicate-vertices.png
   :width: 300px

   Duplicate vertices.

The spin operation leaves duplicate vertices along the profile.
You can select all vertices at the seam with Box select :kbd:`B`
(shown in Fig. :ref:`fig-mesh-screw-duplicate`) and perform a *Merge by Distance* operation.

Notice the selected vertex count before and after the *Merge by Distance* operation
``Vertex count after removing doubles``. If all goes well, the final vertex count
(38 in this example) should match the number of the original profile noted in
:menuselection:`Mesh data --> Vertex and face numbers`.
If not, some vertices were missed and you will need to weld them manually.
Or, worse, too many vertices will have been merged.

.. note:: Merging Two Vertices into One

   To merge (weld) two vertices together, select both of them by :kbd:`Shift-LMB`
   clicking on them. Press :kbd:`S` to start scaling and hold down :kbd:`Ctrl`
   while scaling to scale the points down to 0 units in the X, Y and Z axis. :kbd:`LMB`
   to complete the scaling operation and click :menuselection:`Mesh --> Merge --> By Distance`
   to merge the vertices. Alternatively, you can use :menuselection:`Context Menu --> Merge Vertices` (or :kbd:`M`).
   Then, in the new pop-up menu, choose to merge *By Distance*.


Recalculate Normals
-------------------

All that remains now is to recalculate the normals to the outside by selecting all vertices,
pressing :kbd:`Alt-N` and validating *Recalculate Normals Outside* in the pop-up menu.
