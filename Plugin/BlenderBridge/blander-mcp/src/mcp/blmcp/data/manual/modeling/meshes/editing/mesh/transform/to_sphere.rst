.. _bpy.ops.transform.tosphere:
.. _tool-transform-to_sphere:

*********
To Sphere
*********

.. reference::

   :Mode:      Object and Edit Modes
   :Menu:      :menuselection:`Mesh --> Transform --> To Sphere`
   :Shortcut:  :kbd:`Shift-Alt-S`

The *To Sphere* transformation deforms the selected geometry to look more like a sphere.

.. _fig-mesh-deform-to-sphere-monkey:

.. figure:: /images/modeling_meshes_editing_mesh_transform_to-sphere_suzanne-spherical.png

   Monkey with increasing sphericity (0%, 25%, 50%, 100%).


Usage
=====

Click the menu item or press the keyboard shortcut, then move the mouse right or left
(or type a number between 0 and 1) to make the selection more or less spherical.
Finally, press :kbd:`LMB` or :kbd:`Return` to confirm, or :kbd:`RMB` or :kbd:`Esc` to cancel.

Options
=======

Factor
   A value between 0 and 1 indicating how strongly the selection is spherized.

Mirror Editing
   Whether to also affect matching geometry on the other side of the mesh.
   :ref:`Mesh Symmetry <modeling_meshes_tools-settings_mirror>`
   needs to be enabled for this to work.

Proportional Editing
   See :doc:`/editors/3dview/controls/proportional_editing`.

Examples
========

Meshes with higher density will give better results:

.. figure:: /images/modeling_meshes_editing_mesh_transform_to-sphere_cubes-spherical.png

   To Sphere applied to cubes with different subdivision levels.

The results are also different depending on the number and arrangement of the selected elements:

.. figure:: /images/modeling_meshes_editing_mesh_transform_to-sphere_other-spherical.png

   To Sphere applied to different selections.
