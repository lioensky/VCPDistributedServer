.. _bpy.ops.transform.skin_resize:

***********
Skin Resize
***********

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Transform --> Skin Resize`
   :Shortcut:  :kbd:`Ctrl-A`

Changes the X and Y skinning radii of the selected vertices for use with the
:doc:`/modeling/modifiers/generate/skin`. (For meshes that don't have this modifier,
activating this operator does nothing.)

To change only one of the radii, press :kbd:`X` or :kbd:`Y` while the operator is active,
or change a *Scale X/Y* property in the :ref:`bpy.ops.screen.redo_last` panel.

The radii can also be adjusted in the :ref:`modeling-mesh-transform-panel` in the Sidebar.

.. note::

   If the modifier is deleted, the skinning radii will be lost.

.. figure:: /images/modeling_modifiers_generate_skin_example.png

   Simple creature, made with only the Skin and Subdivision Surface modifiers.
