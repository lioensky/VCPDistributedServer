.. _bpy.ops.transform.resize:

*****
Scale
*****

.. reference::

   :Mode:      Object and Edit Modes
   :Menu:      :menuselection:`Object/Mesh/Curve/Surface --> Transform --> Scale`
   :Shortcut:  :kbd:`S`

Scaling means changing proportions of objects. Pressing :kbd:`S` will enter
the *Scale* transformation mode where the selected element is scaled inward or
outward according to the mouse pointer's location. The element's scale will
increase as the mouse pointer is moved away from the Pivot Point and decrease as
the pointer is moved towards it. If the mouse pointer crosses from the original side of
the :doc:`Pivot Point </editors/3dview/controls/pivot_point/index>`
to the opposite side, the scale will continue in the negative direction and flip the element.

.. figure:: /images/scene-layout_object_editing_transform_scale_basic-usage.png

   Basic scale usage. From left to right, the panels show: the original object,
   a scaled down object, a scaled up object and a scale-flipped object.

The amount of scaling will be displayed in the header of the 3D Viewport.

.. figure:: /images/scene-layout_object_editing_transform_scale_display-values.png

   Scale values.

.. seealso::

   Using a combination of shortcuts gives you more control over your transformation.
   See :doc:`Transform Control </scene_layout/object/editing/transform/control/index>`.


Options
=======

Scale X, Y, Z
   The amount to resize the selection on the respected axis.

Orientation
   Aligns the transformation axes to a specified orientation constraint.
   See :doc:`Transform Orientations </editors/3dview/controls/orientation>` for more information.

Proportional Editing
   The extruded face will affect nearby geometry.
   See :doc:`Proportional Editing </editors/3dview/controls/proportional_editing>` for a full reference.
