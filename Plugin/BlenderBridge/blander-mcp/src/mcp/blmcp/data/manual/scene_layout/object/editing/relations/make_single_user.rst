.. _bpy.ops.object.make_single_user:

****************
Make Single User
****************

.. reference::

   :Mode:      Object Mode
   :Menu:      :menuselection:`Object --> Relations --> Make Single User`

Makes the selected or all object data-blocks single users, that is, not shared
(linked) between other objects in the blend-file.

Additionally, it can also make single-user copies of its dependencies,
like meshes, curves, materials, animations...

Type
   These actions work on the selected objects, or on all the objects of the scene.

   All, Selected Objects

Data-blocks
   Lets you, in addition to the menu predefined selection, choose the type of data-blocks individually.

   :Object: Make single user objects.
   :Object Data: Make single user object data.
   :Materials: Make materials local to each data-block.
   :Object Animation:
      Make the animation of :doc:`Object Properties </scene_layout/object/properties/index>`
      data local to each object.
   :Object Data Animation: Make object data (mesh, curve etc.) animation data local to each object.

.. seealso::

   :ref:`data-system-datablock-make-single-user`
