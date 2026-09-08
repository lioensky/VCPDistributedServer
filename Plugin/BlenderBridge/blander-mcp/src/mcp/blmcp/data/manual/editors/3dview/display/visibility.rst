.. _bpy.types.SpaceView3D.show_object_viewport:
.. _bpy.types.SpaceView3D.show_object_select:

**********************
Object Type Visibility
**********************

.. reference::

   :Mode:      All Modes
   :Location:  :menuselection:`Header --> Selectability & Visibility` (:bl-icon:`vis_sel_11`)

This popover lets you control the visibility and selectability of the various object types.
For example, you can hide all the Lights in the scene with one click.

The settings only apply to the current 3D Viewport. Object types marked as unselectable
can still be selected in other viewports and in the
:doc:`Outliner </editors/outliner/introduction>`, for example.

.. note::

   The object types apply to the evaluated geometry type rather than the original.
   For example, a mesh object changed to a volume with geometry nodes will be visible
   even if the *Mesh* option is unchecked.

.. seealso::

   Outliner :ref:`Restriction Columns <editors-outliner-interface-restriction_columns>`
   for making individual objects invisible or unselectable across all viewports.
