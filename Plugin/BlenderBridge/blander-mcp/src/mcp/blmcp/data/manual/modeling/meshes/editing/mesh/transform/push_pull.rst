.. _bpy.ops.transform.push_pull:
.. _tool-transform-push_pull:

*********
Push/Pull
*********

.. reference::

   :Mode:      Object and Edit Modes
   :Tool:      :menuselection:`Toolbar --> Shrink/Fatten --> Push/Pull`
   :Menu:      :menuselection:`Object/Mesh --> Transform --> Push/Pull`

Moves the selected elements further away from or closer to the
:doc:`Pivot Point </editors/3dview/controls/pivot_point/index>`,
all by the same distance.

When using the tool, simply drag the yellow pin.

When using the menu item, move the mouse down to Push or up to Pull
(Alternatively, type a number for the *Distance* option.)
Then press :kbd:`LMB` or :kbd:`Return` to confirm,
or :kbd:`RMB` or :kbd:`Esc` to cancel.

After confirming, the distance can still be changed in the
:ref:`bpy.ops.screen.redo_last` panel.

Options
=======

Distance
   How far to push (negative) or pull (positive) the selected items.
Mirror Editing
   Whether to also affect matching geometry on the other side of the mesh.
   :ref:`Mesh Symmetry <modeling_meshes_tools-settings_mirror>`
   needs to be enabled for this to work.
Proportional Editing
   See :doc:`Proportional Editing </editors/3dview/controls/proportional_editing>`.

Example
=======

.. figure:: /images/modeling_meshes_editing_mesh_transform_push-pull_vertices.png

   Pushing vertices away from the 3D Cursor (middle) compared to scaling (right).
