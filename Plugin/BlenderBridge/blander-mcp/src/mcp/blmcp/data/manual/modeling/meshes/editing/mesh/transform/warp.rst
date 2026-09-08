
****
Warp
****

.. reference::

   :Mode:      Edit Modes
   :Menu:      :menuselection:`Object/Mesh/Curve/Surface --> Transform --> Warp`

This transformation bends part of the selection into a circle segment.
It's similar to :doc:`/modeling/meshes/editing/mesh/transform/bend`,
except that here, the 3D Cursor is at the center instead of on the circle.

Usage
=====

#. Align the 3D Viewport's :doc:`viewpoint </editors/3dview/navigate/viewpoint>` to the plane
   in which the warp should happen.
#. Place the :doc:`/editors/3dview/3d_cursor` at the center point for the warp.
#. Click *Warp* in the menu.
#. Adjust the options in the :ref:`bpy.ops.screen.redo_last` panel.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_mesh_transform_warp_mesh.png

          Before.

     - .. figure:: /images/modeling_meshes_editing_mesh_transform_warp_mesh-90.png

          Warp Angle 90°.

   * - .. figure:: /images/modeling_meshes_editing_mesh_transform_warp_mesh-180.png

          Warp Angle 180°.

     - .. figure:: /images/modeling_meshes_editing_mesh_transform_warp_mesh-360.png

          Warp Angle 360°.

.. note::

   Unlike most other transform tools, *Warp* does not take into account the
   :doc:`transform orientation </editors/3dview/controls/orientation>` or the
   :doc:`pivot point </editors/3dview/controls/pivot_point/index>`, instead always
   using the view plane and the 3D Cursor.


Options
=======

Warp Angle
   The size of the circle segment along which to bend the selection.
Offset Angle
   Direction angle for the line going from the 3D Cursor to the center of the selection.
   A value of 0° means straight up, and higher values go clockwise.
Min/Max
   Distance from the above centerline to the leftmost/rightmost part of geometry that will
   be included in the circle segment. The geometry that "sticks out of" these limits
   will be rotated but not bent.

.. figure:: /images/modeling_meshes_editing_mesh_transform_warp_properties.png

   Warping with an Offset Angle of 45°, a Min and Max of -0.5 and 0.5,
   and a Warp Angle of 90°.

Example
=======

.. figure:: /images/modeling_meshes_editing_mesh_transform_warp_text.jpg

   Text wrapped around logo.

This was made by creating the Blender logo and text as separate objects.
The text was :doc:`converted </scene_layout/object/editing/convert>`
to a mesh and then warped around the logo.
