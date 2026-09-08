NodeTreeInterfaceSocketVectorFactor2D(NodeTreeInterfaceSocket)
==============================================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`NodeTreeInterfaceItem`, :class:`NodeTreeInterfaceSocket`

.. class:: NodeTreeInterfaceSocketVectorFactor2D(NodeTreeInterfaceSocket)

   3D vector socket of a node

   .. attribute:: default_value

      Input value used for unconnected socket (array of 2 items, in [0, 1], default (0.0, 0.0))

      :type: :class:`bpy_prop_array`\ [float]

   .. attribute:: dimensions

      Dimensions of the vector socket (in [2, 4], default 0)

      :type: int

   .. attribute:: max_value

      Maximum value (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: min_value

      Minimum value (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: subtype

      Subtype of the default value (default ``'DEFAULT'``)

      :type: Literal['DEFAULT']

   .. method:: draw(context, layout)

      Draw interface socket settings

      :param context: (never None)
      :type context: :class:`Context` | None
      :param layout: Layout, Layout in the UI (never None)
      :type layout: :class:`UILayout` | None

   .. method:: init_socket(node, socket, data_path)

      Initialize a node socket instance

      :param node: Node, Node of the socket to initialize (never None)
      :type node: :class:`Node` | None
      :param socket: Socket, Socket to initialize (never None)
      :type socket: :class:`NodeSocket` | None
      :param data_path: Data Path, Path to specialized socket data (never None)
      :type data_path: str

   .. method:: from_socket(node, socket)

      Setup template parameters from an existing socket

      :param node: Node, Node of the original socket (never None)
      :type node: :class:`Node` | None
      :param socket: Socket, Original socket (never None)
      :type socket: :class:`NodeSocket` | None

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
   - :class:`NodeTreeInterfaceItem.item_type`
   - :class:`NodeTreeInterfaceItem.parent`
   - :class:`NodeTreeInterfaceItem.position`
   - :class:`NodeTreeInterfaceItem.index`
   - :class:`NodeTreeInterfaceSocket.name`
   - :class:`NodeTreeInterfaceSocket.identifier`
   - :class:`NodeTreeInterfaceSocket.description`
   - :class:`NodeTreeInterfaceSocket.socket_type`
   - :class:`NodeTreeInterfaceSocket.in_out`
   - :class:`NodeTreeInterfaceSocket.hide_value`
   - :class:`NodeTreeInterfaceSocket.hide_in_modifier`
   - :class:`NodeTreeInterfaceSocket.force_non_field`
   - :class:`NodeTreeInterfaceSocket.is_inspect_output`
   - :class:`NodeTreeInterfaceSocket.is_panel_toggle`
   - :class:`NodeTreeInterfaceSocket.layer_selection_field`
   - :class:`NodeTreeInterfaceSocket.menu_expanded`
   - :class:`NodeTreeInterfaceSocket.optional_label`
   - :class:`NodeTreeInterfaceSocket.select`
   - :class:`NodeTreeInterfaceSocket.attribute_domain`
   - :class:`NodeTreeInterfaceSocket.default_attribute_name`
   - :class:`NodeTreeInterfaceSocket.structure_type`
   - :class:`NodeTreeInterfaceSocket.default_input`
   - :class:`NodeTreeInterfaceSocket.bl_socket_idname`

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
   - :class:`NodeTreeInterfaceItem.bl_rna_get_subclass`
   - :class:`NodeTreeInterfaceItem.bl_rna_get_subclass_py`
   - :class:`NodeTreeInterfaceSocket.bl_system_properties_get`
   - :class:`NodeTreeInterfaceSocket.draw`
   - :class:`NodeTreeInterfaceSocket.init_socket`
   - :class:`NodeTreeInterfaceSocket.from_socket`
   - :class:`NodeTreeInterfaceSocket.bl_rna_get_subclass`
   - :class:`NodeTreeInterfaceSocket.bl_rna_get_subclass_py`

