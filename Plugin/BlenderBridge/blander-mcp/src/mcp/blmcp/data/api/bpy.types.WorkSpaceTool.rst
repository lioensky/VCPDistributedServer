WorkSpaceTool(bpy_struct)
=========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: WorkSpaceTool(bpy_struct)


   .. data:: brush_type

      If the tool uses brushes and is limited to a specific brush type, the identifier of the brush type (default ``'DEFAULT'``, readonly)

      :type: Literal['DEFAULT']

   .. data:: has_datablock

      (default False, readonly)

      :type: bool

   .. attribute:: idname

      (default "", never None)

      :type: str

   .. attribute:: idname_fallback

      (default "", never None)

      :type: str

   .. data:: index

      (in [-inf, inf], default 0, readonly)

      :type: int

   .. data:: mode

      (default ``'DEFAULT'``, readonly)

      :type: Literal['DEFAULT']

   .. data:: space_type

      (default ``'EMPTY'``, readonly)

      :type: Literal[:ref:`rna_enum_space_type_items`]

   .. data:: use_brushes

      (default False, readonly)

      :type: bool

   .. data:: use_paint_canvas

      Does this tool use a painting canvas (default False, readonly)

      :type: bool

   .. data:: widget

      (default "", readonly, never None)

      :type: str

   .. method:: setup(idname, *, cursor='DEFAULT', keymap="", gizmo_group="", brush_type='', data_block="", operator="", index=0, options=set(), idname_fallback="", keymap_fallback="")

      Set the tool settings

      :param idname: Identifier, (never None)
      :type idname: str
      :param cursor: cursor, (optional)
      :type cursor: Literal[:ref:`rna_enum_window_cursor_items`]
      :param keymap: Key Map, (optional, never None)
      :type keymap: str
      :param gizmo_group: Gizmo Group, (optional, never None)
      :type gizmo_group: str
      :param brush_type: Brush Type, Limit this tool to a specific type of brush (optional)
      :type brush_type: str
      :param data_block: Data Block, (optional, never None)
      :type data_block: str
      :param operator: Operator, (optional, never None)
      :type operator: str
      :param index: Index, (in [-inf, inf], optional)
      :type index: int
      :param options: Tool Options, (optional)

         - ``KEYMAP_FALLBACK``
           Fallback.
         - ``USE_BRUSHES``
           Uses Brushes -- Allow this tool to use brushes via the asset system.
      :type options: set[Literal['KEYMAP_FALLBACK', 'USE_BRUSHES']]
      :param idname_fallback: Fallback Identifier, (optional, never None)
      :type idname_fallback: str
      :param keymap_fallback: Fallback Key Map, (optional, never None)
      :type keymap_fallback: str

   .. method:: operator_properties(operator)

      operator_properties

      :param operator: (never None)
      :type operator: str
      :return: (never None)
      :rtype: :class:`OperatorProperties`

   .. method:: gizmo_group_properties(group)

      gizmo_group_properties

      :param group: (never None)
      :type group: str
      :return: (never None)
      :rtype: :class:`GizmoGroupProperties`

   .. method:: refresh_from_context()

      refresh_from_context


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

   - :class:`WorkSpace.tools`
   - :class:`wmTools.from_space_image_mode`
   - :class:`wmTools.from_space_node`
   - :class:`wmTools.from_space_sequencer`
   - :class:`wmTools.from_space_view3d_mode`

