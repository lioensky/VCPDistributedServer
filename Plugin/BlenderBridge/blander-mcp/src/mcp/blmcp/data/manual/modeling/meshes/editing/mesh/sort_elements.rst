.. _bpy.ops.mesh.sort_elements:
.. _mesh-edit-sort-elements:

*************
Sort Elements
*************

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Sort Elements...`

Changes the internal storage order of the selected mesh elements.

.. hint::

   To see the storage indices of the selected elements, first ensure the
   :ref:`bpy.types.PreferencesView.show_developer_ui` option is enabled in the Preferences,
   then enable the :ref:`bpy.types.View3DOverlay.show_extra_indices` overlay in the 3D Viewport.

View Z Axis
   Sort along the active view's Z axis, from farthest to nearest.
View X Axis
   Sort along the active view's X axis, from left to right.
Cursor Distance
   Sort by distance from the :doc:`/editors/3dview/3d_cursor`, from nearest to farthest.
Material
   Sort faces by their :ref:`material slot <bpy.types.MaterialSlot>` index, from lowest
   to highest. The order of faces within each "material group" remains unchanged.
Selected
   Move all selected elements to the beginning (without affecting their relative order).
   Warning: This will also affect the indices of **unselected** elements!
Randomize
   Randomize the order of the selected elements.
Reverse
   Reverse the order of the selected elements.

The :ref:`bpy.ops.screen.redo_last` panel has the following options:

Type
   The sort order as described above.
Elements
   Whether to sort vertices, edges, or faces. This is initially determined by the
   current :ref:`selection mode <bpy.ops.mesh.select_mode>`.
Reverse
   Sort in the opposite order than the default one.
Seed
   When using *Randomize*, changing the seed will result in a different order.
