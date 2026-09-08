.. _tool-scale-cage:

**********
Scale Cage
**********

.. reference::

   :Mode:      Object and Edit Modes
   :Tool:      :menuselection:`Toolbar --> Scale --> Scale Cage`

The *Scale Cage* tool is a bounding box around the object(s) which scales objects from a particular point or axis.
The tool works by selecting a scale point and dragging inwards or outwards to adjust the scale accordingly.
The origin for the scale will be from the point on the cube directly opposite from the point selected.
Selecting points on the faces of the cube scales along one axis,
selecting points on the edges of the cube scales along two axes,
and selecting points on the vertices of the cube scales along all three axes.

.. figure:: /images/scene-layout_object_tools_scale-cage_example.png
   :align: center

   Scale Cage tool.


Tool Settings
=============

Orientation
   Aligns the transformation axes to a specified orientation constraint.
   See :doc:`Transform Orientations </editors/3dview/controls/orientation>` for more information.


Options
=======

Scale X, Y, Z
   The amount to resize the selection on their respected axis.

Orientation
   Aligns the transformation axes to a specified orientation constraint.
   See :doc:`Transform Orientations </editors/3dview/controls/orientation>` for more information.

Proportional Editing
   The extruded face will affect nearby geometry.
   See :doc:`Proportional Editing </editors/3dview/controls/proportional_editing>` for a full reference.
