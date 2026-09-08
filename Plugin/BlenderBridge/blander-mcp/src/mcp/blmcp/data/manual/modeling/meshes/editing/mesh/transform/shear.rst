.. _bpy.ops.transform.shear:
.. _tool-transform-shear:

*****
Shear
*****

.. reference::

   :Mode:      Object and Edit Mode
   :Tool:      :menuselection:`Toolbar --> Shear`
   :Menu:      :menuselection:`Object/Mesh/Curve/Surface --> Transform --> Shear`
   :Shortcut:  :kbd:`Shift-Ctrl-Alt-S`

Shearing deforms the selected geometry by moving the vertices above the
:doc:`Pivot Point </editors/3dview/controls/pivot_point/index>` to the left and the vertices below
that point to the right (or vice versa). The higher or lower a vertex is compared to the pivot point,
the further it will be moved. The result is that vertical edges become diagonal while horizontal edges
stay the same.

Usage
=====

Tool
----

Set up a pivot point and optionally a :doc:`transform orientation </editors/3dview/controls/orientation>`.
Pick an axis on the gizmo that matches the desired "above"/"below" direction (which determines
how much each vertex should be sheared). Finally, drag the handle that matches the desired
"horizontal" direction (in which the vertices should be moved).

.. figure:: /images/modeling_meshes_editing_mesh_transform_shear_tool.png

   Using the Shear tool.

Operator
--------

Set up a pivot point, then either click the menu item or press the keyboard shortcut.
Move the mouse left or right to shear, then click :kbd:`LMB` to confirm.

By default, the meanings of "above," "below," and "horizontal" are all in the current
viewing plane in the 3D Viewport, but this can be changed in the options.

.. figure:: /images/modeling_meshes_editing_mesh_transform_shear_operator.png

   Using the Shear operator with different pivot points.

Options
=======

Angle
   How much to "rotate" the vertical edges.
Axis
   The axis that's perpendicular to the shearing plane. For example, if the vertices
   should move along the X axis and their distance from the pivot point should be
   measured along the Y axis, the *Axis* should be set to Z.
Axis Ortho
   The axis along which the vertices should move. This must be different from *Axis*.
Orientation
   The :doc:`Transform Orientation </editors/3dview/controls/orientation>` from which
   to pick the *Axis* and *Axis Ortho*.
Mirror Editing
   Whether to also affect matching geometry on the other side of the mesh.
   :ref:`Mesh Symmetry <modeling_meshes_tools-settings_mirror>`
   needs to be enabled for this to work.
Proportional Editing
   See :doc:`Proportional Editing </editors/3dview/controls/proportional_editing>`.
