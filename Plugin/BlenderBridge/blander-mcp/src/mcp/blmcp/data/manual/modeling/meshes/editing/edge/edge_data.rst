
*********
Edge Data
*********

The operators below change edge properties which in turn influence certain tools or modifiers.
To quickly access an operator that doesn't have its own shortcut, press :kbd:`Ctrl-E`
to open the :menuselection:`Edge` menu as a popover at the mouse cursor.

.. _bpy.ops.transform.edge_bevelweight:

Edge Bevel Weight
=================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Edge --> Edge Bevel Weight`

Interactively changes the :ref:`Bevel Weight <modeling-edges-bevel-weight>` of the selected edges.
After clicking the menu item, move the mouse to change the weight or type a (positive or negative)
number to add to the existing weight. (The value is shown at the top of the 3D Viewport.)
Then press :kbd:`LMB` or :kbd:`Return` to confirm, or :kbd:`RMB` or :kbd:`Esc` to cancel.

The Bevel Weight can also be seen and changed in the
:ref:`Sidebar <modeling-mesh-transform-panel>`.


.. _bpy.ops.transform.edge_crease:

Edge Crease
===========

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Edge --> Edge Crease`
   :Shortcut:  :kbd:`Shift-E`

Interactively changes the :ref:`Crease <modeling-edges-bevel-weight>` amount of the selected edges.
After clicking the menu item or pressing the shortcut, move the mouse to change the value
or type a (positive or negative) number to add to the existing value. (The value is shown
at the top of the 3D Viewport.) Then press :kbd:`LMB` or :kbd:`Return` to confirm,
or :kbd:`RMB` or :kbd:`Esc` to cancel.

The Crease value can also be seen and changed in the
:ref:`Sidebar <modeling-mesh-transform-panel>`.



.. _bpy.ops.mesh.mark_seam:

Mark/Clear Seam
===============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Edge --> Mark/Clear Seam`

Mark or unmark the selected edges as being
:doc:`UV Seams </modeling/meshes/uv/unwrapping/seams>`.


.. _bpy.ops.mesh.mark_sharp:

Mark/Clear Sharp
================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Edge --> Mark/Clear Sharp`

Mark or unmark the selected edges as being Sharp. This property is used for the following:

- Making edges appear sharp, and faces appear flat, in meshes that are otherwise
  :ref:`smoothly shaded <bpy.ops.object.shade_smooth>`. Specifically, this is done by changing
  the :ref:`normals <modeling-meshes-structure-normals>` of vertices that are connected to
  at least two Sharp edges.
- Indicating which edges should be affected by the :doc:`/modeling/modifiers/generate/edge_split`.
- Indicating which edges should *not* be affected by the :doc:`/modeling/modifiers/normals/smooth_by_angle`
  and the :doc:`/modeling/modifiers/normals/weighted_normal`.
- Exporting smoothing groups to external file formats (e.g. :doc:`FBX </addons/import_export/scene_fbx>`,
  :doc:`OBJ </files/import_export/obj>`).

Internally, the Sharp state is stored in the ``sharp_edge`` :ref:`attribute <geometry-nodes_builtin-attributes>`.

.. seealso::

   - :doc:`/modeling/geometry_nodes/mesh/read/is_edge_smooth`
   - :doc:`/modeling/geometry_nodes/mesh/write/set_shade_smooth`


.. _bpy.ops.mesh.set_sharpness_by_angle:

Set Sharpness by Angle
======================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Edge --> Set Sharpness by Angle`

Sets the :ref:`sharp edge attribute <geometry-nodes_builtin-attributes>`
based on the angle between neighboring faces.

Angle
   Maximum angle between face normals that will be considered as smooth.
Extend
   Add new sharp edges without clearing existing sharp edges.


.. _bpy.ops.mesh.mark_freestyle_edge:

Mark/Clear Freestyle Edge
=========================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Edge --> Mark/Clear Freestyle Edge`

Marks or unmarks the selected edges as requiring Freestyle lines.
See :ref:`freestyle-edge-marks`.
