
*************
Object Origin
*************

Each object has an origin point. The location of this point determines where the object is located in 3D space.
When an object is selected, a small dot appears, denoting the origin point.
The location of the origin point is important when translating, rotating or scaling an object.
See :doc:`Pivot Points </editors/3dview/controls/pivot_point/index>` for more.

The color of the origin changes based on the :doc:`selection </scene_layout/object/selecting>`
state of the object.

:Yellow: Object is active.
:Orange: Object is selected, but not active.
:White: Object is not linked and not selected.
:Turquoise: Object is linked.
:Light Turquoise: Object is selected, linked, but not active.

.. note::

   Colors are themeable and might appear different.
   The colors described here are from the default Dark Theme.


.. _bpy.ops.object.origin_set:

Set Origin
==========

.. reference::

   :Mode:      Object Mode
   :Menu:      :menuselection:`Object --> Set Origin`

The object origin and geometry can be moved relative to each other and to the 3D cursor.

Type
   Geometry to Origin
      Moves the model to the origin and this way the origin of the object will
      also be at the center of the object.
   Origin to Geometry
      Moves the origin to the center of the object.
   Origin to 3D Cursor
      Moves the origin of the model to the position of the 3D cursor.
   Origin to Center of Mass
      Moves the origin to the calculated center of mass of model
      (assuming the mesh has a uniform density).
Center
   Median Point Center, Bounding Box Center

.. tip::

   To transform an object's origin directly, enable
   :ref:`Affect Only Origins <bpy.types.ToolSettings.use_transform_data_origin>`
   in the *Tool Settings Options*.
