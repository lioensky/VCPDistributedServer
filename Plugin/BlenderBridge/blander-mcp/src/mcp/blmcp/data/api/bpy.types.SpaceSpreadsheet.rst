SpaceSpreadsheet(Space)
=======================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Space`

.. class:: SpaceSpreadsheet(Space)

   Spreadsheet space data

   .. attribute:: attribute_domain

      Attribute domain to display (default ``'POINT'``)

      :type: Literal[:ref:`rna_enum_attribute_domain_items`]

   .. attribute:: geometry_component_type

      Part of the geometry to display data from (default ``'MESH'``)

      :type: Literal[:ref:`rna_enum_geometry_component_type_items`]

   .. attribute:: geometry_item_type

      Item Type (default ``'DOMAIN'``)

      - ``DOMAIN``
        Domain -- Domain data.
      - ``BUNDLE``
        Bundle -- Bundle data.

      :type: Literal['DOMAIN', 'BUNDLE']

   .. attribute:: is_pinned

      Context path is pinned (default False)

      :type: bool

   .. attribute:: object_eval_state

      (default ``'EVALUATED'``)

      - ``EVALUATED``
        Evaluated -- Use data from fully or partially evaluated object.
      - ``ORIGINAL``
        Original -- Use data from original object without any modifiers applied.
      - ``VIEWER_NODE``
        Viewer Node -- Use intermediate data from viewer node.

      :type: Literal['EVALUATED', 'ORIGINAL', 'VIEWER_NODE']

   .. data:: row_filters

      Filters to remove rows from the displayed data (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`SpreadsheetRowFilter`]

   .. attribute:: show_internal_attributes

      Display attributes with names starting with a period that are meant for internal use (default False)

      :type: bool

   .. attribute:: show_only_selected

      Only include rows that correspond to selected elements (default False)

      :type: bool

   .. attribute:: show_region_channels

      (default False)

      :type: bool

   .. attribute:: show_region_footer

      (default False)

      :type: bool

   .. attribute:: show_region_toolbar

      (default False)

      :type: bool

   .. attribute:: show_region_ui

      (default False)

      :type: bool

   .. data:: tables

      Persistent data for the tables shown in this spreadsheet editor (default None, readonly)

      :type: :class:`SpreadsheetTables`\ [:class:`SpreadsheetTable`]

   .. attribute:: use_filter

      (default False)

      :type: bool

   .. data:: viewer_path

      Path to the data that is displayed in the spreadsheet (readonly)

      :type: :class:`ViewerPath` | None

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


   .. classmethod:: draw_handler_add(callback, args, region_type, draw_type)
   
      Add a new draw handler to this space type.
      It will be called every time the specified region in the space type will be drawn.
      Note: All arguments are positional only for now.
   
      :param callback:
         A function that will be called when the region is drawn.
         It gets the specified arguments as input, it's return value is ignored.
      :type callback: Callable[..., Any]
      :param args: Arguments that will be passed to the callback.
      :type args: tuple[Any, ...]
      :param region_type: The region type the callback draws in; usually ``WINDOW``. (:class:`bpy.types.Region.type`)
      :type region_type: str
      :param draw_type: Usually ``POST_PIXEL`` for 2D drawing and ``POST_VIEW`` for 3D drawing. In some cases ``PRE_VIEW`` can be used. ``BACKDROP`` can be used for backdrops in the node editor.
      :type draw_type: str
      :return: Handler that can be removed later on.
      :rtype: object


   .. classmethod:: draw_handler_remove(handler, region_type)
   
      Remove a draw handler that was added previously.
   
      :param handler: The draw handler that should be removed.
      :type handler: object
      :param region_type: Region type the callback was added to.
      :type region_type: str


Inherited Properties
--------------------

.. hlist::
   :columns: 2

   - :class:`bpy_struct.id_data`
   - :class:`Space.type`
   - :class:`Space.show_locked_time`
   - :class:`Space.show_region_header`

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
   - :class:`Space.bl_rna_get_subclass`
   - :class:`Space.bl_rna_get_subclass_py`
   - :class:`Space.draw_handler_add`
   - :class:`Space.draw_handler_remove`

