
*****************************
Working with Multiple Objects
*****************************

Unlike Edit Mode, there is no multi-object editing supported for Sculpt Mode. Since sculpting often involves editing
many separate objects, it is recommended to use the shortcut :kbd:`Alt Q` while pointing at other objects, for
:ref:`bpy.ops.object.transfer_mode` quickly.

.. figure:: /images/sculpt-paint_sculpt_multi_object_example.png

The advantage of using multiple objects is that each can have its own origin and modifiers.
Splitting the geometry among multiple objects can also improve the sculpt mode performance.
Alternatively objects can also be :doc:`joined </scene_layout/object/editing/join>`
so there is no need to switch objects.

.. figure:: /images/sculpt-paint_sculpt_joined_object_example.png

In the case that Face Sets were already used, joining objects or creating new geometry in Edit Mode will
automatically assign new Face Sets. This makes it immediately possible to target each new geometry, for example via
auto-masking. If no Face Sets are created, use the :ref:`bpy.ops.sculpt.face_sets_init` operator to create them.

Face Sets and Masked geometry can also be extracted via :ref:`bpy.ops.sculpt.paint_mask_extract`
or sliced into a new object via :ref:`bpy.ops.sculpt.paint_mask_slice`.
