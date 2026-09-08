.. _bpy.ops.mesh.separate:
.. _object-separate:

********
Separate
********

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Separate`
   :Shortcut:  :kbd:`P`

Splits the mesh into to two or more new, separate mesh objects.

.. figure:: /images/modeling_meshes_editing_mesh_separate_example.png

   Suzanne dissected neatly.

Options
=======

Selection
   Disconnects the selected geometry from its surroundings and moves it into a new object.
By Material
   Splits the mesh into an object per :ref:`material slot <bpy.types.MaterialSlot>`,
   each containing the faces using that material slot. This is done for the whole mesh regardless
   of the selection.
By Loose Parts
   Creates an object for every independent (disconnected) piece of the original mesh.
   This is done for the whole mesh regardless of the selection.

.. seealso::

   - :ref:`bpy.ops.mesh.split` for disconnecting geometry without moving it into a new object.
   - :doc:`/scene_layout/object/editing/join` for merging multiple objects into one.
