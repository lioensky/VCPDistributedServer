GreasePencilTreeNode(bpy_struct)
================================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

subclasses --- 
:class:`GreasePencilLayer`, :class:`GreasePencilLayerGroup`

.. class:: GreasePencilTreeNode(bpy_struct)

   Grease Pencil node in the layer tree. Either a layer or a group

   .. attribute:: channel_color

      Color of the channel in the dope sheet (array of 3 items, in [0, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. attribute:: hide

      Set tree node visibility (default False)

      :type: bool

   .. attribute:: lock

      Protect tree node from editing (default False)

      :type: bool

   .. attribute:: name

      The name of the tree node (default "", never None)

      :type: str

   .. data:: next_node

      The layer tree node after (i.e. above) this one (readonly)

      :type: :class:`GreasePencilTreeNode` | None

   .. data:: parent_group

      The parent group of this layer tree node (readonly)

      :type: :class:`GreasePencilLayerGroup` | None

   .. data:: prev_node

      The layer tree node before (i.e. below) this one (readonly)

      :type: :class:`GreasePencilTreeNode` | None

   .. attribute:: select

      Tree node is selected (default False)

      :type: bool

   .. attribute:: use_masks

      The visibility of drawings in this tree node is affected by the layers in the masks list (default True)

      :type: bool

   .. attribute:: use_onion_skinning

      Display onion skins before and after the current frame (default True)

      :type: bool

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

   - :class:`GreasePencil.root_nodes`
   - :class:`GreasePencilLayerGroup.children`
   - :class:`GreasePencilTreeNode.next_node`
   - :class:`GreasePencilTreeNode.prev_node`

