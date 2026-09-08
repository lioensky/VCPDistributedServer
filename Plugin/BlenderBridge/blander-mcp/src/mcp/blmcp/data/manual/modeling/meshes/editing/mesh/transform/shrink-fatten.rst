.. _bpy.ops.transform.shrink_fatten:
.. _tool-mesh-shrink-fatten:

*************
Shrink/Fatten
*************

.. reference::

   :Mode:      Edit Mode
   :Tool:      :menuselection:`Toolbar --> Shrink/Fatten`
   :Menu:      :menuselection:`Mesh --> Transform --> Shrink/Fatten`
   :Shortcut:  :kbd:`Alt-S`

Moves the selected vertices "inwards" or "outwards" along their normal,
all by the same distance.

After clicking the menu item or pressing the keyboard shortcut, move the mouse down to
shrink or up to fatten. (Alternatively, type a distance on the keyboard.) Then
press :kbd:`LMB` or :kbd:`Return` to confirm or :kbd:`RMB` or :kbd:`Esc` to cancel.

.. list-table::
   :widths: 1 1 1

   * - .. figure:: /images/modeling_meshes_editing_mesh_transform_shrink-fatten_before.png

          Mesh before shrink/fatten.

     - .. figure:: /images/modeling_meshes_editing_mesh_transform_shrink-fatten_inflate-negative.png

          Shrunk using a negative value.

     - .. figure:: /images/modeling_meshes_editing_mesh_transform_shrink-fatten_inflate-positive.png

          Fattened using a positive value.

Options
=======

These settings can be changed in the :ref:`bpy.ops.screen.redo_last` panel.

Offset
   How far to move each vertex.

Offset Even
   When disabled, each vertex is offset by the same distance.
   When enabled, each *edge* is offset by the same distance.

   This option can also be toggled before confirming by pressing :kbd:`S` or holding :kbd:`Alt`.
   (These shortcuts are shown in the status bar.)

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_face_extrude-faces-normal_offset-even-off.png

          Fattening with Offset Even disabled.

     - .. figure:: /images/modeling_meshes_editing_face_extrude-faces-normal_offset-even-on.png

          Fattening with Offset Even enabled.

Mirror Editing
   Whether to also affect matching geometry on the other side of the mesh.
   :ref:`Mesh Symmetry <modeling_meshes_tools-settings_mirror>`
   needs to be enabled for this to work.

Proportional Editing
   See :doc:`Proportional Editing </editors/3dview/controls/proportional_editing>`.
