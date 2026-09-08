WindowManager(ID)
=================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: WindowManager(ID)

   Window manager data-block defining open windows and other user interface data

   .. attribute:: addon_filter

      Filter add-ons by category

      :type: str

   .. attribute:: addon_search

      Filter by add-on name, author & category (default "", never None)

      :type: str

   .. attribute:: addon_support

      Display support level (default {``'COMMUNITY'``, ``'OFFICIAL'``})

      - ``OFFICIAL``
        Official -- Officially supported.
      - ``COMMUNITY``
        Community -- Maintained by community developers.

      :type: set[Literal['OFFICIAL', 'COMMUNITY']]

   .. data:: addon_tags

      (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`BlExtDummyGroup`]

   .. data:: asset_path_dummy

      Full path to the Blender file containing the active asset (default "", readonly, never None)

      :type: str

   .. attribute:: extension_repo_filter

      Filter extensions by repository

      :type: str

   .. attribute:: extension_search

      Filter by extension name, author & category (default "", never None)

      :type: str

   .. attribute:: extension_show_panel_available

      Show the available extensions panel (default True)

      :type: bool

   .. attribute:: extension_show_panel_installed

      Show the installed extensions panel (default True)

      :type: bool

   .. data:: extension_tags

      (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`BlExtDummyGroup`]

   .. attribute:: extension_type

      Show extensions by type (default ``'ADDON'``)

      - ``ALL``
        All -- Show all extension types.
      - ``ADDON``
        Add-ons -- Only show add-ons.
      - ``THEME``
        Themes -- Only show themes.

      :type: Literal['ALL', 'ADDON', 'THEME']

   .. attribute:: extension_use_filter

      Filter Extensions by Tags & Repository (default False)

      :type: bool

   .. attribute:: extensions_blocked

      Number of installed extensions which are blocked (in [-inf, inf], default 0)

      :type: int

   .. attribute:: extensions_updates

      Number of extensions with available update (in [-inf, inf], default 0)

      :type: int

   .. data:: is_interface_locked

      If true, the interface is currently locked by a running job and data should not be modified from application timers. Otherwise, the running job might conflict with the handler causing unexpected results or even crashes. (default False, readonly)

      :type: bool

   .. data:: keyconfigs

      Registered key configurations (default None, readonly)

      :type: :class:`KeyConfigurations`\ [:class:`KeyConfig`]

   .. data:: operators

      Operator registry (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`Operator`]

   .. attribute:: poselib_previous_action

      :type: :class:`Action` | None

   .. attribute:: preset_name

      Name for new preset (default "New Preset", never None)

      :type: str

   .. data:: windows

      Open windows (default None, readonly)

      :type: :class:`Windows`\ [:class:`Window`]

   .. data:: xr_session_settings

      (readonly, never None)

      :type: :class:`XrSessionSettings`

   .. data:: xr_session_state

      Runtime state information about the VR session (readonly)

      :type: :class:`XrSessionState` | None

   .. attribute:: clipboard

      Clipboard text storage.
      
      :type: str


   .. classmethod:: fileselect_add(operator)

      Opens a file selector with an operator.

      :param operator: Operator to call
      :type operator: :class:`Operator` | None

      This method is used from the operators ``invoke`` callback
      which must then return ``{'RUNNING_MODAL'}``.

      Accepting the file selector will run the operators ``execute`` callback.

      The following properties are supported:

      ``filepath``: ``bpy.props.StringProperty(subtype='FILE_PATH')``
         Represents the absolute path to the file.
      ``dirpath``: ``bpy.props.StringProperty(subtype='DIR_PATH')``
         Represents the absolute path to the directory.
      ``filename``: ``bpy.props.StringProperty(subtype='FILE_NAME')``
         Represents the filename without the leading directory.
      ``files``: ``bpy.props.CollectionProperty(type=bpy.types.OperatorFileListElement)``
         When present in the operator this collection includes all selected files.
      ``filter_glob``: ``bpy.props.StringProperty(default="*.ext")``
         When present in the operator and it's not empty,
         it will be used as a file filter (example value: ``*.zip;*.py;*.exe``).
      ``check_existing``: ``bpy.props.BoolProperty()``
         If this property is present and set to ``True``,
         the operator will warn if the provided file-path already exists
         by highlighting the filename input field in red.


      .. warning::

         After opening the file-browser the user may continue to use Blender,
         this means it is possible for the user to change the context in ways
         that would cause the operators ``poll`` function to fail.

         Unless the operator reads all necessary data from the context before the file-selector is opened,
         it is recommended for operators to check the ``poll`` function from ``execute``
         to ensure the context is still valid.

         Example from the body of an operators ``execute`` function:

         .. code-block:: python

            if self.options.is_invoke:
                # The context may have changed since invoking the file selector.
                if not self.poll(context):
                    self.report({'ERROR'}, "Invalid context")
                    return {'CANCELLED'}


   .. classmethod:: modal_handler_add(operator)

      Add a modal handler to the window manager, for the given modal operator (called by invoke() with self, just before returning {'RUNNING_MODAL'})

      :param operator: Operator to call
      :type operator: :class:`Operator` | None
      :return: Whether adding the handler was successful
      :rtype: bool

   .. method:: event_timer_add(time_step, *, window=None)

      Add a timer to the given window, to generate periodic 'TIMER' events

      :param time_step: Time Step, Interval in seconds between timer events (in [0, inf])
      :type time_step: float
      :param window: Window to attach the timer to, or None (optional)
      :type window: :class:`Window` | None
      :rtype: :class:`Timer`

   .. method:: event_timer_remove(timer)

      event_timer_remove

      :param timer: (never None)
      :type timer: :class:`Timer` | None

   .. classmethod:: gizmo_group_type_ensure(identifier)

      Activate an existing widget group (when the persistent option isn't set)

      :param identifier: Gizmo group type name (never None)
      :type identifier: str

   .. classmethod:: gizmo_group_type_unlink_delayed(identifier)

      Unlink a widget group (when the persistent option is set)

      :param identifier: Gizmo group type name (never None)
      :type identifier: str

   .. method:: progress_begin(min, max)

      Start progress report

      :param min: min, any value in range [0,9999] (in [-inf, inf])
      :type min: float
      :param max: max, any value in range [min+1,9998] (in [-inf, inf])
      :type max: float

   .. method:: progress_update(value)

      Update the progress feedback

      :param value: value, Any value between min and max as set in progress_begin() (in [-inf, inf])
      :type value: float

   .. method:: progress_end()

      Terminate progress report


   .. classmethod:: invoke_props_popup(operator, event)

      Operator popup invoke (show operator properties and execute it automatically on changes)

      :param operator: Operator to call
      :type operator: :class:`Operator` | None
      :param event: Event
      :type event: :class:`Event` | None
      :return: result
      :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

   .. classmethod:: invoke_props_dialog(operator, *, width=300, title="", confirm_text="", cancel_default=False, text_ctxt="", translate=True)

      Operator dialog (non-autoexec popup) invoke (show operator properties and only execute it on click on OK button)

      :param operator: Operator to call
      :type operator: :class:`Operator` | None
      :param width: Width of the popup (in [0, inf], optional)
      :type width: int
      :param title: Title, Optional text to show as title of the popup (optional, never None)
      :type title: str
      :param confirm_text: Confirm Text, Optional text to show instead to the default "OK" confirmation button text (optional, never None)
      :type confirm_text: str
      :param cancel_default: cancel_default, (optional)
      :type cancel_default: bool
      :param text_ctxt: Override automatic translation context of the given text (optional)
      :type text_ctxt: str
      :param translate: Translate the given text, when UI translation is enabled (optional)
      :type translate: bool
      :return: result
      :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

   .. classmethod:: invoke_search_popup(operator)

      Operator search popup invoke which searches values of the operator's :class:`bpy.types.Operator.bl_property` (which must be an EnumProperty), executing it on confirmation

      :param operator: Operator to call
      :type operator: :class:`Operator` | None

   .. classmethod:: invoke_popup(operator, *, width=300)

      Operator popup invoke (only shows operator's properties, without executing it)

      :param operator: Operator to call
      :type operator: :class:`Operator` | None
      :param width: Width of the popup (in [0, inf], optional)
      :type width: int
      :return: result
      :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

   .. classmethod:: invoke_confirm(operator, event, *, title="", message="", confirm_text="", icon='NONE', text_ctxt="", translate=True)

      Operator confirmation popup (only to let user confirm the execution, no operator properties shown)

      :param operator: Operator to call
      :type operator: :class:`Operator` | None
      :param event: Event
      :type event: :class:`Event` | None
      :param title: Title, Optional text to show as title of the popup (optional, never None)
      :type title: str
      :param message: Message, Optional first line of content text (optional, never None)
      :type message: str
      :param confirm_text: Confirm Text, Optional text to show instead to the default "OK" confirmation button text (optional, never None)
      :type confirm_text: str
      :param icon: Icon, Optional icon displayed in the dialog (optional)
      :type icon: Literal['NONE', 'WARNING', 'QUESTION', 'ERROR', 'INFO']
      :param text_ctxt: Override automatic translation context of the given text (optional)
      :type text_ctxt: str
      :param translate: Translate the given text, when UI translation is enabled (optional)
      :type translate: bool
      :return: result
      :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

   .. classmethod:: popmenu_begin__internal(title, *, icon='NONE')

      popmenu_begin__internal

      :param title: (never None)
      :type title: str
      :param icon: icon, (optional)
      :type icon: Literal[:ref:`rna_enum_icon_items`]
      :return: (never None)
      :rtype: :class:`UIPopupMenu`

   .. classmethod:: popmenu_end__internal(menu)

      popmenu_end__internal

      :param menu: (never None)
      :type menu: :class:`UIPopupMenu` | None

   .. classmethod:: popover_begin__internal(*, ui_units_x=0, from_active_button=False)

      popover_begin__internal

      :param ui_units_x: ui_units_x, (in [0, inf], optional)
      :type ui_units_x: int
      :param from_active_button: Use Button, Use the active button for positioning (optional)
      :type from_active_button: bool
      :return: (never None)
      :rtype: :class:`UIPopover`

   .. classmethod:: popover_end__internal(menu, *, keymap=None)

      popover_end__internal

      :param menu: (never None)
      :type menu: :class:`UIPopover` | None
      :param keymap: Key Map, Active key map (optional)
      :type keymap: :class:`KeyMap` | None

   .. classmethod:: piemenu_begin__internal(title, *, icon='NONE', event=None)

      piemenu_begin__internal

      :param title: (never None)
      :type title: str
      :param icon: icon, (optional)
      :type icon: Literal[:ref:`rna_enum_icon_items`]
      :param event: (optional, never None)
      :type event: :class:`Event` | None
      :return: (never None)
      :rtype: :class:`UIPieMenu`

   .. classmethod:: piemenu_end__internal(menu)

      piemenu_end__internal

      :param menu: (never None)
      :type menu: :class:`UIPieMenu` | None

   .. classmethod:: operator_properties_last(operator)

      operator_properties_last

      :param operator: (never None)
      :type operator: str
      :return: (never None)
      :rtype: :class:`OperatorProperties`

   .. method:: print_undo_steps()

      print_undo_steps


   .. classmethod:: tag_script_reload()

      Tag for refreshing the interface after scripts have been reloaded


   .. method:: popover(draw_func, *, ui_units_x=0, keymap=None, from_active_button=False)

   .. method:: popup_menu(draw_func, *, title='', icon='NONE')


      Popup menus can be useful for creating menus without having to register menu classes.

      Note that they will not block the scripts execution, so the caller can't wait for user input.

      .. literalinclude:: ./examples/bpy.types.WindowManager.popup_menu.0.py
         :lines: 7-

   .. method:: popup_menu_pie(event, draw_func, *, title='', icon='NONE')

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


   .. classmethod:: draw_cursor_add(callback, args, space_type, region_type)
   
      Add a new draw cursor handler to this space type.
      It will be called every time the cursor for the specified region in the space type will be drawn.
      Note: All arguments are positional only for now.
   
      :param callback:
         A function that will be called when the cursor is drawn.
         It gets the specified arguments as input with the mouse position (``tuple[int, int]``) as last argument.
      :type callback: Callable[..., Any]
      :param args: Arguments that will be passed to the callback.
      :type args: tuple[Any, ...]
      :param space_type: The space type the callback draws in; for example ``VIEW_3D``. (:class:`bpy.types.Space.type`)
      :type space_type: str
      :param region_type: The region type the callback draws in; usually ``WINDOW``. (:class:`bpy.types.Region.type`)
      :type region_type: str
      :return: Handler that can be removed later on.
      :rtype: object


   .. classmethod:: draw_cursor_remove(handler)
   
      Remove a draw cursor handler that was added previously.
   
      :param handler: The draw cursor handler that should be removed.
      :type handler: object


Inherited Properties
--------------------

.. hlist::
   :columns: 2

   - :class:`bpy_struct.id_data`
   - :class:`ID.name`
   - :class:`ID.name_full`
   - :class:`ID.id_type`
   - :class:`ID.session_uid`
   - :class:`ID.is_evaluated`
   - :class:`ID.original`
   - :class:`ID.users`
   - :class:`ID.use_fake_user`
   - :class:`ID.use_extra_user`
   - :class:`ID.is_embedded_data`
   - :class:`ID.is_linked_packed`
   - :class:`ID.is_missing`
   - :class:`ID.is_runtime_data`
   - :class:`ID.is_editable`
   - :class:`ID.tag`
   - :class:`ID.is_library_indirect`
   - :class:`ID.library`
   - :class:`ID.library_weak_reference`
   - :class:`ID.asset_data`
   - :class:`ID.override_library`
   - :class:`ID.preview`

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
   - :class:`ID.bl_system_properties_get`
   - :class:`ID.rename`
   - :class:`ID.evaluated_get`
   - :class:`ID.copy`
   - :class:`ID.asset_mark`
   - :class:`ID.asset_clear`
   - :class:`ID.asset_generate_preview`
   - :class:`ID.override_create`
   - :class:`ID.override_hierarchy_create`
   - :class:`ID.user_clear`
   - :class:`ID.user_remap`
   - :class:`ID.make_local`
   - :class:`ID.user_of_id`
   - :class:`ID.animation_data_create`
   - :class:`ID.animation_data_clear`
   - :class:`ID.update_tag`
   - :class:`ID.preview_ensure`
   - :class:`ID.bl_rna_get_subclass`
   - :class:`ID.bl_rna_get_subclass_py`

References
----------

.. hlist::
   :columns: 2

   - :class:`BlendData.window_managers`
   - :class:`Context.window_manager`

