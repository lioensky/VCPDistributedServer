SpaceTextEditor(Space)
======================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Space`

.. class:: SpaceTextEditor(Space)

   Text editor space data

   .. attribute:: find_text

      Text to search for with the find tool (default "", never None)

      :type: str

   .. attribute:: font_size

      Font size to use for displaying the text (in [1, 256], default 0)

      :type: int

   .. attribute:: margin_column

      Column number to show right margin at (in [0, 1024], default 0)

      :type: int

   .. attribute:: replace_text

      Text to replace selected text with using the replace tool (default "", never None)

      :type: str

   .. attribute:: show_line_highlight

      Highlight the current line (default False)

      :type: bool

   .. attribute:: show_line_numbers

      Show line numbers next to the text (default False)

      :type: bool

   .. attribute:: show_margin

      Show right margin (default False)

      :type: bool

   .. attribute:: show_region_footer

      (default False)

      :type: bool

   .. attribute:: show_region_ui

      (default False)

      :type: bool

   .. attribute:: show_syntax_highlight

      Syntax highlight for scripting (default False)

      :type: bool

   .. attribute:: show_word_wrap

      Wrap words if there is not enough horizontal space (default False)

      :type: bool

   .. attribute:: tab_width

      Number of spaces to display tabs with (in [2, 8], default 0)

      :type: int

   .. attribute:: text

      Text displayed and edited in this space

      :type: :class:`Text` | None

   .. attribute:: top

      Top line visible (in [0, inf], default 0)

      :type: int

   .. attribute:: use_find_all

      Search in all text data-blocks, instead of only the active one (default False)

      :type: bool

   .. attribute:: use_find_wrap

      Search again from the start of the file when reaching the end (default False)

      :type: bool

   .. attribute:: use_live_edit

      Run Python while editing (default False)

      :type: bool

   .. attribute:: use_match_case

      Search string is sensitive to uppercase and lowercase letters (default False)

      :type: bool

   .. attribute:: use_overwrite

      Overwrite characters when typing rather than inserting them (default False)

      :type: bool

   .. data:: visible_lines

      Amount of lines that can be visible in current editor (in [-inf, inf], default 0, readonly)

      :type: int

   .. method:: is_syntax_highlight_supported()

      Returns True if the editor supports syntax highlighting for the current text data-block

      :rtype: bool

   .. method:: region_location_from_cursor(line, column)

      Retrieve the region position from the given line and character position

      :param line: Line, Line index (in [-inf, inf])
      :type line: int
      :param column: Column, Column index (in [-inf, inf])
      :type column: int
      :return: Region coordinates (array of 2 items, in [-1, inf])
      :rtype: :class:`bpy_prop_array`\ [int]

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

