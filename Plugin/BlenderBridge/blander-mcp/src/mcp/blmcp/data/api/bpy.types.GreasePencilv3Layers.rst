GreasePencilv3Layers(bpy_prop_collection)
=========================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_prop`, :class:`bpy_prop_collection`

.. class:: GreasePencilv3Layers(bpy_prop_collection)

   Collection of Grease Pencil layers

   .. attribute:: active

      Active Grease Pencil layer

      :type: :class:`GreasePencilLayer` | None

   .. method:: new(name, *, set_active=True, layer_group=None)

      Add a new Grease Pencil layer

      :param name: Name, Name of the layer (never None)
      :type name: str
      :param set_active: Set Active, Set the newly created layer as the active layer (optional)
      :type set_active: bool
      :param layer_group: The layer group the new layer will be created in (use None for the main stack) (optional)
      :type layer_group: :class:`GreasePencilLayerGroup` | None
      :return: The newly created layer
      :rtype: :class:`GreasePencilLayer`

   .. method:: remove(layer)

      Remove a Grease Pencil layer

      :param layer: The layer to remove (never None)
      :type layer: :class:`GreasePencilLayer` | None

   .. method:: move(layer, type)

      Move a Grease Pencil layer in the layer group or main stack

      :param layer: The layer to move (never None)
      :type layer: :class:`GreasePencilLayer` | None
      :param type: Direction of movement
      :type type: Literal['DOWN', 'UP']

   .. method:: move_top(layer)

      Move a Grease Pencil layer to the top of the layer group or main stack

      :param layer: The layer to move (never None)
      :type layer: :class:`GreasePencilLayer` | None

   .. method:: move_bottom(layer)

      Move a Grease Pencil layer to the bottom of the layer group or main stack

      :param layer: The layer to move (never None)
      :type layer: :class:`GreasePencilLayer` | None

   .. method:: move_to_layer_group(layer, layer_group)

      Move a Grease Pencil layer into a layer group

      :param layer: The layer to move (never None)
      :type layer: :class:`GreasePencilLayer` | None
      :param layer_group: The layer group the layer will be moved into (use None for the main stack)
      :type layer_group: :class:`GreasePencilLayerGroup` | None

   .. classmethod:: bl_rna_get_subclass(id, default=None, /)
   
      :param id: The RNA type identifier.
      :type id: str
      :param default: The value to return when not found.
      :type default: :class:`bpy.types.Struct` | None
      :return: The RNA type or default when not found.
      :rtype: :class:`bpy.types.Struct`


   .. classmethod:: bl_rna_get_subclass_py(id, default=None, /)
   
      :param id: The RNA type identifier.
      :type id: str
      :param default: The value to return when not found.
      :type default: type | None
      :return: The class or default when not found.
      :rtype: type


Inherited Properties
--------------------

.. hlist::
   :columns: 2

   - :class:`bpy_struct.id_data`

Inherited Functions
-------------------

.. hlist::
   :columns: 2

   - :class:`bpy_struct.as_pointer`
   - :class:`bpy_struct.driver_add`
   - :class:`bpy_struct.driver_remove`
   - :class:`bpy_struct.get`
   - :class:`bpy_struct.id_properties_clear`
   - :class:`bpy_struct.id_properties_ensure`
   - :class:`bpy_struct.id_properties_ui`
   - :class:`bpy_struct.is_property_hidden`
   - :class:`bpy_struct.is_property_overridable_library`
   - :class:`bpy_struct.is_property_readonly`
   - :class:`bpy_struct.is_property_set`
   - :class:`bpy_struct.items`
   - :class:`bpy_struct.keyframe_delete`
   - :class:`bpy_struct.keyframe_insert`
   - :class:`bpy_struct.keys`
   - :class:`bpy_struct.path_from_id`
   - :class:`bpy_struct.path_from_module`
   - :class:`bpy_struct.path_resolve`
   - :class:`bpy_struct.pop`
   - :class:`bpy_struct.property_overridable_library_set`
   - :class:`bpy_struct.property_unset`
   - :class:`bpy_struct.rna_ancestors`
   - :class:`bpy_struct.type_recast`
   - :class:`bpy_struct.values`

References
----------

.. hlist::
   :columns: 2

   - :class:`GreasePencil.layers`

