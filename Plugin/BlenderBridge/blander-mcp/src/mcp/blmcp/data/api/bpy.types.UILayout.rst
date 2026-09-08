UILayout(bpy_struct)
====================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: UILayout(bpy_struct)

   User interface layout in a panel or header

   .. attribute:: activate_init

      When true, buttons defined in popups will be activated on first display (use so you can type into a field without having to click on it first) (default False)

      :type: bool

   .. attribute:: active

      (default False)

      :type: bool

   .. attribute:: active_default

      When true, an operator button defined after this will be activated when pressing return(use with popup dialogs) (default False)

      :type: bool

   .. attribute:: alert

      (default False)

      :type: bool

   .. attribute:: alignment

      (default ``'EXPAND'``)

      :type: Literal['EXPAND', 'LEFT', 'CENTER', 'RIGHT']

   .. data:: direction

      (default ``'HORIZONTAL'``, readonly)

      :type: Literal['HORIZONTAL', 'VERTICAL']

   .. attribute:: emboss

      (default ``'NORMAL'``)

      - ``NORMAL``
        Regular -- Draw standard button emboss style.
      - ``NONE``
        None -- Draw only text and icons.
      - ``PULLDOWN_MENU``
        Pull-down Menu -- Draw pull-down menu style.
      - ``PIE_MENU``
        Pie Menu -- Draw radial menu style.
      - ``NONE_OR_STATUS``
        None or Status -- Draw with no emboss unless the button has a coloring status like an animation state.

      :type: Literal['NORMAL', 'NONE', 'PULLDOWN_MENU', 'PIE_MENU', 'NONE_OR_STATUS']

   .. attribute:: enabled

      When false, this (sub)layout is grayed out (default False)

      :type: bool

   .. attribute:: operator_context

      Typically set to 'INVOKE_REGION_WIN', except some cases in :class:`bpy.types.Menu` when it's set to 'EXEC_REGION_WIN'. (default ``'INVOKE_DEFAULT'``)

      :type: Literal[:ref:`rna_enum_operator_context_items`]

   .. attribute:: scale_x

      Scale factor along the X for items in this (sub)layout (in [0, inf], default 0.0)

      :type: float

   .. attribute:: scale_y

      Scale factor along the Y for items in this (sub)layout (in [0, inf], default 0.0)

      :type: float

   .. attribute:: ui_units_x

      Fixed size along the X for items in this (sub)layout (in [0, inf], default 0.0)

      :type: float

   .. attribute:: ui_units_y

      Fixed size along the Y for items in this (sub)layout (in [0, inf], default 0.0)

      :type: float

   .. attribute:: use_property_decorate

      (default False)

      :type: bool

   .. attribute:: use_property_split

      (default False)

      :type: bool

   .. method:: row(*, align=False, heading="", heading_ctxt="", translate=True)

      Sub-layout. Items placed in this sublayout are placed next to each other in a row.

      :param align: Align buttons to each other (optional)
      :type align: bool
      :param heading: Heading, Label to insert into the layout for this sub-layout (optional, never None)
      :type heading: str
      :param heading_ctxt: Override automatic translation context of the given heading (optional, never None)
      :type heading_ctxt: str
      :param translate: Translate the given heading, when UI translation is enabled (optional)
      :type translate: bool
      :return: Sub-layout to put items in
      :rtype: :class:`UILayout`

   .. method:: column(*, align=False, heading="", heading_ctxt="", translate=True)

      Sub-layout. Items placed in this sublayout are placed under each other in a column.

      :param align: Align buttons to each other (optional)
      :type align: bool
      :param heading: Heading, Label to insert into the layout for this sub-layout (optional, never None)
      :type heading: str
      :param heading_ctxt: Override automatic translation context of the given heading (optional, never None)
      :type heading_ctxt: str
      :param translate: Translate the given heading, when UI translation is enabled (optional)
      :type translate: bool
      :return: Sub-layout to put items in
      :rtype: :class:`UILayout`

   .. method:: panel(idname, *, default_closed=False)

      Creates a collapsible panel. Whether it is open or closed is stored in the region using the given idname. This can only be used when the panel has the full width of the panel region available to it. So it can't be used in e.g. in a box or columns.

      :param idname: Identifier of the panel (never None)
      :type idname: str
      :param default_closed: Open by Default, When true, the panel will be open the first time it is shown (optional)
      :type default_closed: bool
      :return:
         ``layout_header``, Sub-layout to put items in, :class:`UILayout`

         ``layout_body``, Sub-layout to put items in. Will be none if the panel is collapsed., :class:`UILayout`

      :rtype: tuple[:class:`UILayout`, :class:`UILayout`]

   .. method:: panel_prop(data, property)

      Similar to ``.panel(...)`` but instead of storing whether it is open or closed in the region, it is stored in the provided boolean property. This should be used when multiple instances of the same panel can exist. For example one for every item in a collection property or list. This can only be used when the panel has the full width of the panel region available to it. So it can't be used in e.g. in a box or columns.

      :param data: Data from which to take the open-state property (never None)
      :type data: :class:`AnyType` | None
      :param property: Identifier of the boolean property that determines whether the panel is open or closed (never None)
      :type property: str
      :return:
         ``layout_header``, Sub-layout to put items in, :class:`UILayout`

         ``layout_body``, Sub-layout to put items in. Will be none if the panel is collapsed., :class:`UILayout`

      :rtype: tuple[:class:`UILayout`, :class:`UILayout`]

   .. method:: column_flow(*, columns=0, align=False)

      column_flow

      :param columns: Number of columns, 0 is automatic (in [0, inf], optional)
      :type columns: int
      :param align: Align buttons to each other (optional)
      :type align: bool
      :return: Sub-layout to put items in
      :rtype: :class:`UILayout`

   .. method:: grid_flow(*, row_major=False, columns=0, even_columns=False, even_rows=False, align=False)

      grid_flow

      :param row_major: Fill row by row, instead of column by column (optional)
      :type row_major: bool
      :param columns: Number of columns, positive are absolute fixed numbers, 0 is automatic, negative are automatic multiple numbers along major axis (e.g. -2 will only produce 2, 4, 6 etc. columns for row major layout, and 2, 4, 6 etc. rows for column major layout). (in [-inf, inf], optional)
      :type columns: int
      :param even_columns: All columns will have the same width (optional)
      :type even_columns: bool
      :param even_rows: All rows will have the same height (optional)
      :type even_rows: bool
      :param align: Align buttons to each other (optional)
      :type align: bool
      :return: Sub-layout to put items in
      :rtype: :class:`UILayout`

   .. method:: box()

      Sublayout (items placed in this sublayout are placed under each other in a column and are surrounded by a box)

      :return: Sub-layout to put items in
      :rtype: :class:`UILayout`

   .. method:: split(*, factor=0.0, align=False)

      split

      :param factor: Percentage, Percentage of width to split at (leave unset for automatic calculation) (in [0, 1], optional)
      :type factor: float
      :param align: Align buttons to each other (optional)
      :type align: bool
      :return: Sub-layout to put items in
      :rtype: :class:`UILayout`

   .. method:: menu_pie()

      Sublayout. Items placed in this sublayout are placed in a radial fashion around the menu center).

      :return: Sub-layout to put items in
      :rtype: :class:`UILayout`

   .. classmethod:: icon(data)

      Return the custom icon for this data, use it e.g. to get materials or texture icons.

      :param data: Data from which to take the icon (never None)
      :type data: :class:`AnyType` | None
      :return: Icon identifier (in [0, inf])
      :rtype: int

   .. classmethod:: enum_item_name(data, property, identifier)

      Return the UI name for this enum item

      :param data: Data from which to take property (never None)
      :type data: :class:`AnyType` | None
      :param property: Identifier of property in data (never None)
      :type property: str
      :param identifier: Identifier of the enum item (never None)
      :type identifier: str
      :return: UI name of the enum item (never None)
      :rtype: str

   .. classmethod:: enum_item_description(data, property, identifier)

      Return the UI description for this enum item

      :param data: Data from which to take property (never None)
      :type data: :class:`AnyType` | None
      :param property: Identifier of property in data (never None)
      :type property: str
      :param identifier: Identifier of the enum item (never None)
      :type identifier: str
      :return: UI description of the enum item (never None)
      :rtype: str

   .. classmethod:: enum_item_icon(data, property, identifier)

      Return the icon for this enum item

      :param data: Data from which to take property (never None)
      :type data: :class:`AnyType` | None
      :param property: Identifier of property in data (never None)
      :type property: str
      :param identifier: Identifier of the enum item (never None)
      :type identifier: str
      :return: Icon identifier (in [0, inf])
      :rtype: int

   .. method:: prop(data, property, *, text="", text_ctxt="", translate=True, icon='NONE', placeholder="", expand=False, slider=False, toggle=-1, icon_only=False, event=False, full_event=False, emboss=True, index=-1, icon_value=0, invert_checkbox=False)

      Item. Exposes an RNA item and places it into the layout.

      :param data: Data from which to take property (never None)
      :type data: :class:`AnyType` | None
      :param property: Identifier of property in data (never None)
      :type property: str
      :param text: Override automatic text of the item (optional)
      :type text: str
      :param text_ctxt: Override automatic translation context of the given text (optional)
      :type text_ctxt: str
      :param translate: Translate the given text, when UI translation is enabled (optional)
      :type translate: bool
      :param icon: Icon, Override automatic icon of the item (optional)
      :type icon: Literal[:ref:`rna_enum_icon_items`]
      :param placeholder: Hint describing the expected value when empty (optional)
      :type placeholder: str
      :param expand: Expand button to show more detail (optional)
      :type expand: bool
      :param slider: Use slider widget for numeric values (optional)
      :type slider: bool
      :param toggle: Use toggle widget for boolean values, or a checkbox when disabled (the default is -1 which uses toggle only when an icon is displayed) (in [-1, 1], optional)
      :type toggle: int
      :param icon_only: Draw only icons in buttons, no text (optional)
      :type icon_only: bool
      :param event: Use button to input key events (optional)
      :type event: bool
      :param full_event: Use button to input full events including modifiers (optional)
      :type full_event: bool
      :param emboss: Draw the button itself, not just the icon/text. When false, corresponds to the 'NONE_OR_STATUS' layout emboss type. (optional)
      :type emboss: bool
      :param index: The index of this button, when set a single member of an array can be accessed, when set to -1 all array members are used (in [-2, inf], optional)
      :type index: int
      :param icon_value: Icon Value, Override automatic icon of the item (in [0, inf], optional)
      :type icon_value: int
      :param invert_checkbox: Draw checkbox value inverted (optional)
      :type invert_checkbox: bool

   .. method:: props_enum(data, property)

      props_enum

      :param data: Data from which to take property (never None)
      :type data: :class:`AnyType` | None
      :param property: Identifier of property in data (never None)
      :type property: str

   .. method:: prop_menu_enum(data, property, *, text="", text_ctxt="", translate=True, icon='NONE')

      prop_menu_enum

      :param data: Data from which to take property (never None)
      :type data: :class:`AnyType` | None
      :param property: Identifier of property in data (never None)
      :type property: str
      :param text: Override automatic text of the item (optional)
      :type text: str
      :param text_ctxt: Override automatic translation context of the given text (optional)
      :type text_ctxt: str
      :param translate: Translate the given text, when UI translation is enabled (optional)
      :type translate: bool
      :param icon: Icon, Override automatic icon of the item (optional)
      :type icon: Literal[:ref:`rna_enum_icon_items`]

   .. method:: prop_with_popover(data, property, *, text="", text_ctxt="", translate=True, icon='NONE', icon_only=False, panel)

      prop_with_popover

      :param data: Data from which to take property (never None)
      :type data: :class:`AnyType` | None
      :param property: Identifier of property in data (never None)
      :type property: str
      :param text: Override automatic text of the item (optional)
      :type text: str
      :param text_ctxt: Override automatic translation context of the given text (optional)
      :type text_ctxt: str
      :param translate: Translate the given text, when UI translation is enabled (optional)
      :type translate: bool
      :param icon: Icon, Override automatic icon of the item (optional)
      :type icon: Literal[:ref:`rna_enum_icon_items`]
      :param icon_only: Draw only icons in tabs, no text (optional)
      :type icon_only: bool
      :param panel: Identifier of the panel (never None)
      :type panel: str

   .. method:: prop_with_menu(data, property, *, text="", text_ctxt="", translate=True, icon='NONE', icon_only=False, menu)

      prop_with_menu

      :param data: Data from which to take property (never None)
      :type data: :class:`AnyType` | None
      :param property: Identifier of property in data (never None)
      :type property: str
      :param text: Override automatic text of the item (optional)
      :type text: str
      :param text_ctxt: Override automatic translation context of the given text (optional)
      :type text_ctxt: str
      :param translate: Translate the given text, when UI translation is enabled (optional)
      :type translate: bool
      :param icon: Icon, Override automatic icon of the item (optional)
      :type icon: Literal[:ref:`rna_enum_icon_items`]
      :param icon_only: Draw only icons in tabs, no text (optional)
      :type icon_only: bool
      :param menu: Identifier of the menu (never None)
      :type menu: str

   .. method:: prop_tabs_enum(data, property, *, data_highlight=None, property_highlight="", icon_only=False, expand_as='DEFAULT')

      prop_tabs_enum

      :param data: Data from which to take property (never None)
      :type data: :class:`AnyType` | None
      :param property: Identifier of property in data (never None)
      :type property: str
      :param data_highlight: Data from which to take highlight property (optional, never None)
      :type data_highlight: :class:`AnyType` | None
      :param property_highlight: Identifier of highlight property in data (optional, never None)
      :type property_highlight: str
      :param icon_only: Draw only icons in tabs, no text (optional)
      :type icon_only: bool
      :param expand_as: (optional)
      :type expand_as: Literal['DEFAULT', 'ROW']

   .. method:: prop_enum(data, property, value, *, text="", text_ctxt="", translate=True, icon='NONE')

      prop_enum

      :param data: Data from which to take property (never None)
      :type data: :class:`AnyType` | None
      :param property: Identifier of property in data (never None)
      :type property: str
      :param value: Enum property value (never None)
      :type value: str
      :param text: Override automatic text of the item (optional)
      :type text: str
      :param text_ctxt: Override automatic translation context of the given text (optional)
      :type text_ctxt: str
      :param translate: Translate the given text, when UI translation is enabled (optional)
      :type translate: bool
      :param icon: Icon, Override automatic icon of the item (optional)
      :type icon: Literal[:ref:`rna_enum_icon_items`]

   .. method:: prop_search(data, property, search_data, search_property, *, text="", text_ctxt="", translate=True, icon='NONE', results_are_suggestions=False, item_search_property="")

      prop_search

      :param data: Data from which to take property (never None)
      :type data: :class:`AnyType` | None
      :param property: Identifier of property in data (never None)
      :type property: str
      :param search_data: Data from which to take collection to search in (never None)
      :type search_data: :class:`AnyType` | None
      :param search_property: Identifier of search collection property (never None)
      :type search_property: str
      :param text: Override automatic text of the item (optional)
      :type text: str
      :param text_ctxt: Override automatic translation context of the given text (optional)
      :type text_ctxt: str
      :param translate: Translate the given text, when UI translation is enabled (optional)
      :type translate: bool
      :param icon: Icon, Override automatic icon of the item (optional)
      :type icon: Literal[:ref:`rna_enum_icon_items`]
      :param results_are_suggestions: Accept inputs that do not match any item (optional)
      :type results_are_suggestions: bool
      :param item_search_property: Identifier of the string property in each collection's items to use for searching (defaults to the items' type 'name property') (optional, never None)
      :type item_search_property: str

   .. method:: prop_decorator(data, property, *, index=-1)

      prop_decorator

      :param data: Data from which to take property (never None)
      :type data: :class:`AnyType` | None
      :param property: Identifier of property in data (never None)
      :type property: str
      :param index: The index of this button, when set a single member of an array can be accessed, when set to -1 all array members are used (in [-2, inf], optional)
      :type index: int

   .. method:: operator(operator, *, text="", text_ctxt="", translate=True, icon='NONE', emboss=True, depress=False, icon_value=0, search_weight=0.0)

      Item. Places a button into the layout to call an Operator.

      :param operator: Identifier of the operator (never None)
      :type operator: str
      :param text: Override automatic text of the item (optional)
      :type text: str
      :param text_ctxt: Override automatic translation context of the given text (optional)
      :type text_ctxt: str
      :param translate: Translate the given text, when UI translation is enabled (optional)
      :type translate: bool
      :param icon: Icon, Override automatic icon of the item (optional)
      :type icon: Literal[:ref:`rna_enum_icon_items`]
      :param emboss: Draw the button itself, not just the icon/text (optional)
      :type emboss: bool
      :param depress: Draw pressed in (optional)
      :type depress: bool
      :param icon_value: Icon Value, Override automatic icon of the item (in [0, inf], optional)
      :type icon_value: int
      :param search_weight: Search Weight, Influences the sorting when using menu-seach (in [-inf, inf], optional)
      :type search_weight: float
      :return: Operator properties to fill in
      :rtype: :class:`OperatorProperties`

   .. method:: operator_menu_hold(operator, *, text="", text_ctxt="", translate=True, icon='NONE', emboss=True, depress=False, icon_value=0, menu)

      Item. Places a button into the layout to call an Operator.

      :param operator: Identifier of the operator (never None)
      :type operator: str
      :param text: Override automatic text of the item (optional)
      :type text: str
      :param text_ctxt: Override automatic translation context of the given text (optional)
      :type text_ctxt: str
      :param translate: Translate the given text, when UI translation is enabled (optional)
      :type translate: bool
      :param icon: Icon, Override automatic icon of the item (optional)
      :type icon: Literal[:ref:`rna_enum_icon_items`]
      :param emboss: Draw the button itself, not just the icon/text (optional)
      :type emboss: bool
      :param depress: Draw pressed in (optional)
      :type depress: bool
      :param icon_value: Icon Value, Override automatic icon of the item (in [0, inf], optional)
      :type icon_value: int
      :param menu: Identifier of the menu (never None)
      :type menu: str
      :return: Operator properties to fill in
      :rtype: :class:`OperatorProperties`

   .. method:: operator_enum(operator, property, *, icon_only=False)

      operator_enum

      :param operator: Identifier of the operator (never None)
      :type operator: str
      :param property: Identifier of property in operator (never None)
      :type property: str
      :param icon_only: Draw only icons in buttons, no text (optional)
      :type icon_only: bool

   .. method:: operator_menu_enum(operator, property, *, text="", text_ctxt="", translate=True, icon='NONE')

      operator_menu_enum

      :param operator: Identifier of the operator (never None)
      :type operator: str
      :param property: Identifier of property in operator (never None)
      :type property: str
      :param text: Override automatic text of the item (optional)
      :type text: str
      :param text_ctxt: Override automatic translation context of the given text (optional)
      :type text_ctxt: str
      :param translate: Translate the given text, when UI translation is enabled (optional)
      :type translate: bool
      :param icon: Icon, Override automatic icon of the item (optional)
      :type icon: Literal[:ref:`rna_enum_icon_items`]
      :return: Operator properties to fill in
      :rtype: :class:`OperatorProperties`

   .. method:: label(*, text="", text_ctxt="", translate=True, icon='NONE', icon_value=0)

      Item. Displays text and/or icon in the layout.

      :param text: Override automatic text of the item (optional)
      :type text: str
      :param text_ctxt: Override automatic translation context of the given text (optional)
      :type text_ctxt: str
      :param translate: Translate the given text, when UI translation is enabled (optional)
      :type translate: bool
      :param icon: Icon, Override automatic icon of the item (optional)
      :type icon: Literal[:ref:`rna_enum_icon_items`]
      :param icon_value: Icon Value, Override automatic icon of the item (in [0, inf], optional)
      :type icon_value: int

   .. method:: menu(menu, *, text="", text_ctxt="", translate=True, icon='NONE', icon_value=0)

      menu

      :param menu: Identifier of the menu (never None)
      :type menu: str
      :param text: Override automatic text of the item (optional)
      :type text: str
      :param text_ctxt: Override automatic translation context of the given text (optional)
      :type text_ctxt: str
      :param translate: Translate the given text, when UI translation is enabled (optional)
      :type translate: bool
      :param icon: Icon, Override automatic icon of the item (optional)
      :type icon: Literal[:ref:`rna_enum_icon_items`]
      :param icon_value: Icon Value, Override automatic icon of the item (in [0, inf], optional)
      :type icon_value: int

   .. method:: menu_contents(menu)

      menu_contents

      :param menu: Identifier of the menu (never None)
      :type menu: str

   .. method:: popover(panel, *, text="", text_ctxt="", translate=True, icon='NONE', icon_value=0, direction='VERTICAL')

      popover

      :param panel: Identifier of the panel (never None)
      :type panel: str
      :param text: Override automatic text of the item (optional)
      :type text: str
      :param text_ctxt: Override automatic translation context of the given text (optional)
      :type text_ctxt: str
      :param translate: Translate the given text, when UI translation is enabled (optional)
      :type translate: bool
      :param icon: Icon, Override automatic icon of the item (optional)
      :type icon: Literal[:ref:`rna_enum_icon_items`]
      :param icon_value: Icon Value, Override automatic icon of the item (in [0, inf], optional)
      :type icon_value: int
      :param direction: Popup Direction, The direction in which the popup panel is drawn relative to button position (optional)

         - ``VERTICAL``
           Vertical -- Draw popup panel above or below the button.
         - ``HORIZONTAL``
           Horizontal -- Draw popup panel to the side of the button.
      :type direction: Literal['VERTICAL', 'HORIZONTAL']

   .. method:: popover_group(space_type, region_type, context, category)

      popover_group

      :param space_type: Space Type
      :type space_type: Literal[:ref:`rna_enum_space_type_items`]
      :param region_type: Region Type
      :type region_type: Literal[:ref:`rna_enum_region_type_items`]
      :param context: panel type context (never None)
      :type context: str
      :param category: panel type category (never None)
      :type category: str

   .. method:: separator(*, factor=1.0, type='AUTO')

      Item. Inserts empty space into the layout between items.

      :param factor: Percentage, Percentage of width to space (leave unset for default space) (in [0, inf], optional)
      :type factor: float
      :param type: Type, The type of the separator (optional)

         - ``AUTO``
           Auto -- Best guess at what type of separator is needed..
         - ``SPACE``
           Empty space -- Horizontal or Vertical empty space, depending on layout direction..
         - ``LINE``
           Line -- Horizontal or Vertical line, depending on layout direction..
      :type type: Literal['AUTO', 'SPACE', 'LINE']

   .. method:: separator_spacer()

      Item. Inserts horizontal spacing empty space into the layout between items.


   .. method:: progress(*, text="", text_ctxt="", translate=True, factor=0.0, type='BAR')

      Progress indicator

      :param text: Override automatic text of the item (optional)
      :type text: str
      :param text_ctxt: Override automatic translation context of the given text (optional)
      :type text_ctxt: str
      :param translate: Translate the given text, when UI translation is enabled (optional)
      :type translate: bool
      :param factor: Factor, Amount of progress from 0.0f to 1.0f (in [0, 1], optional)
      :type factor: float
      :param type: Type, The type of progress indicator (optional)
      :type type: Literal['BAR', 'RING']

   .. method:: context_pointer_set(name, data)

      context_pointer_set

      :param name: Name, Name of entry in the context (never None)
      :type name: str
      :param data: Pointer to put in context
      :type data: :class:`AnyType` | None

   .. method:: context_string_set(name, value)

      context_string_set

      :param name: Name, Name of entry in the context (never None)
      :type name: str
      :param value: Value, String to put in context (never None)
      :type value: str

   .. method:: template_header()

      Inserts common Space header UI (editor type selector)


   .. method:: template_ID(data, property, *, new="", open="", unlink="", filter='ALL', live_icon=False, text="", text_ctxt="", translate=True)

      template_ID

      :param data: Data from which to take property (never None)
      :type data: :class:`AnyType` | None
      :param property: Identifier of property in data (never None)
      :type property: str
      :param new: Operator identifier to create a new ID block (optional, never None)
      :type new: str
      :param open: Operator identifier to open a file for creating a new ID block (optional, never None)
      :type open: str
      :param unlink: Operator identifier to unlink the ID block (optional, never None)
      :type unlink: str
      :param filter: Optionally limit the items which can be selected (optional)
      :type filter: Literal['ALL', 'AVAILABLE']
      :param live_icon: Show preview instead of fixed icon (optional)
      :type live_icon: bool
      :param text: Override automatic text of the item (optional)
      :type text: str
      :param text_ctxt: Override automatic translation context of the given text (optional)
      :type text_ctxt: str
      :param translate: Translate the given text, when UI translation is enabled (optional)
      :type translate: bool

   .. method:: template_ID_session_uid(data, property, id_type)

      Template ID search menu button for session_uid Int properties

      :param data: Data from which to take property (never None)
      :type data: :class:`AnyType` | None
      :param property: Identifier of property in data (never None)
      :type property: str
      :type id_type: Literal[:ref:`rna_enum_id_type_items`]

   .. method:: template_ID_preview(data, property, *, new="", open="", unlink="", rows=0, cols=0, filter='ALL', hide_buttons=False)

      template_ID_preview

      :param data: Data from which to take property (never None)
      :type data: :class:`AnyType` | None
      :param property: Identifier of property in data (never None)
      :type property: str
      :param new: Operator identifier to create a new ID block (optional, never None)
      :type new: str
      :param open: Operator identifier to open a file for creating a new ID block (optional, never None)
      :type open: str
      :param unlink: Operator identifier to unlink the ID block (optional, never None)
      :type unlink: str
      :param rows: Number of thumbnail preview rows to display, (in [0, inf], optional)
      :type rows: int
      :param cols: Number of thumbnail preview columns to display, (in [0, inf], optional)
      :type cols: int
      :param filter: Optionally limit the items which can be selected (optional)
      :type filter: Literal['ALL', 'AVAILABLE']
      :param hide_buttons: Show only list, no buttons (optional)
      :type hide_buttons: bool

   .. method:: template_matrix(data, property)

      Insert a readonly Matrix UI. The UI displays the matrix components - translation, rotation and scale. The **property** argument must be the identifier of an existing 4x4 float vector property of subtype 'MATRIX'.

      :param data: Data from which to take property (never None)
      :type data: :class:`AnyType` | None
      :param property: Identifier of property in data (never None)
      :type property: str

   .. method:: template_any_ID(data, property, type_property, *, text="", text_ctxt="", translate=True)

      template_any_ID

      :param data: Data from which to take property (never None)
      :type data: :class:`AnyType` | None
      :param property: Identifier of property in data (never None)
      :type property: str
      :param type_property: Identifier of property in data giving the type of the ID-blocks to use (never None)
      :type type_property: str
      :param text: Override automatic text of the item (optional)
      :type text: str
      :param text_ctxt: Override automatic translation context of the given text (optional)
      :type text_ctxt: str
      :param translate: Translate the given text, when UI translation is enabled (optional)
      :type translate: bool

   .. method:: template_ID_tabs(data, property, *, new="", menu="", filter='ALL')

      template_ID_tabs

      :param data: Data from which to take property (never None)
      :type data: :class:`AnyType` | None
      :param property: Identifier of property in data (never None)
      :type property: str
      :param new: Operator identifier to create a new ID block (optional, never None)
      :type new: str
      :param menu: Context menu identifier (optional, never None)
      :type menu: str
      :param filter: Optionally limit the items which can be selected (optional)
      :type filter: Literal['ALL', 'AVAILABLE']

   .. method:: template_action(id, *, new="", unlink="", text="", text_ctxt="", translate=True)

      template_action

      :param id: The data-block for which to select an Action (never None)
      :type id: :class:`ID` | None
      :param new: Operator identifier to create a new ID block (optional, never None)
      :type new: str
      :param unlink: Operator identifier to unlink the ID block (optional, never None)
      :type unlink: str
      :param text: Override automatic text of the item (optional)
      :type text: str
      :param text_ctxt: Override automatic translation context of the given text (optional)
      :type text_ctxt: str
      :param translate: Translate the given text, when UI translation is enabled (optional)
      :type translate: bool

   .. method:: template_search(data, property, search_data, search_property, *, new="", unlink="", text="", text_ctxt="", translate=True)

      template_search

      :param data: Data from which to take property (never None)
      :type data: :class:`AnyType` | None
      :param property: Identifier of property in data (never None)
      :type property: str
      :param search_data: Data from which to take collection to search in (never None)
      :type search_data: :class:`AnyType` | None
      :param search_property: Identifier of search collection property (never None)
      :type search_property: str
      :param new: Operator identifier to create a new item for the collection (optional, never None)
      :type new: str
      :param unlink: Operator identifier to unlink or delete the active item from the collection (optional, never None)
      :type unlink: str
      :param text: Override automatic text of the item (optional)
      :type text: str
      :param text_ctxt: Override automatic translation context of the given text (optional)
      :type text_ctxt: str
      :param translate: Translate the given text, when UI translation is enabled (optional)
      :type translate: bool

   .. method:: template_search_preview(data, property, search_data, search_property, *, new="", unlink="", text="", text_ctxt="", translate=True, rows=0, cols=0)

      template_search_preview

      :param data: Data from which to take property (never None)
      :type data: :class:`AnyType` | None
      :param property: Identifier of property in data (never None)
      :type property: str
      :param search_data: Data from which to take collection to search in (never None)
      :type search_data: :class:`AnyType` | None
      :param search_property: Identifier of search collection property (never None)
      :type search_property: str
      :param new: Operator identifier to create a new item for the collection (optional, never None)
      :type new: str
      :param unlink: Operator identifier to unlink or delete the active item from the collection (optional, never None)
      :type unlink: str
      :param text: Override automatic text of the item (optional)
      :type text: str
      :param text_ctxt: Override automatic translation context of the given text (optional)
      :type text_ctxt: str
      :param translate: Translate the given text, when UI translation is enabled (optional)
      :type translate: bool
      :param rows: Number of thumbnail preview rows to display, (in [0, inf], optional)
      :type rows: int
      :param cols: Number of thumbnail preview columns to display, (in [0, inf], optional)
      :type cols: int

   .. method:: template_path_builder(data, property, root, *, text="", text_ctxt="", translate=True)

      template_path_builder

      :param data: Data from which to take property (never None)
      :type data: :class:`AnyType` | None
      :param property: Identifier of property in data (never None)
      :type property: str
      :param root: ID-block from which path is evaluated from
      :type root: :class:`ID` | None
      :param text: Override automatic text of the item (optional)
      :type text: str
      :param text_ctxt: Override automatic translation context of the given text (optional)
      :type text_ctxt: str
      :param translate: Translate the given text, when UI translation is enabled (optional)
      :type translate: bool

   .. method:: template_modifiers()

      Generates the UI layout for the modifier stack


   .. method:: template_strip_modifiers()

      Generates the UI layout for the strip modifier stack


   .. method:: template_collection_exporters()

      Generates the UI layout for collection exporters


   .. method:: template_constraints(*, use_bone_constraints=True)

      Generates the panels for the constraint stack

      :param use_bone_constraints: Add panels for bone constraints instead of object constraints (optional)
      :type use_bone_constraints: bool

   .. method:: template_shaderfx()

      Generates the panels for the shader effect stack


   .. method:: template_greasepencil_color(data, property, *, rows=0, cols=0, scale=1.0, filter='ALL')

      template_greasepencil_color

      :param data: Data from which to take property (never None)
      :type data: :class:`AnyType` | None
      :param property: Identifier of property in data (never None)
      :type property: str
      :param rows: Number of thumbnail preview rows to display, (in [0, inf], optional)
      :type rows: int
      :param cols: Number of thumbnail preview columns to display, (in [0, inf], optional)
      :type cols: int
      :param scale: Scale of the image thumbnails, (in [0.1, 1.5], optional)
      :type scale: float
      :param filter: Optionally limit the items which can be selected (optional)
      :type filter: Literal['ALL', 'AVAILABLE']

   .. method:: template_constraint_header(data)

      Generates the header for constraint panels

      :param data: Constraint data (never None)
      :type data: :class:`Constraint` | None

   .. method:: template_preview(id, *, show_buttons=True, parent=None, slot=None, preview_id="")

      Item. A preview window for materials, textures, lights or worlds.

      :param id: ID data-block
      :type id: :class:`ID` | None
      :param show_buttons: Show preview buttons? (optional)
      :type show_buttons: bool
      :param parent: ID data-block (optional)
      :type parent: :class:`ID` | None
      :param slot: Texture slot (optional)
      :type slot: :class:`TextureSlot` | None
      :param preview_id: Identifier of this preview widget, if not set the ID type will be used (i.e. all previews of materials without explicit ID will have the same size...). (optional, never None)
      :type preview_id: str

   .. method:: template_curve_mapping(data, property, *, type='NONE', levels=False, brush=False, use_negative_slope=False, show_tone=False, show_presets=False)

      Item. A curve mapping widget used for e.g falloff curves for lights.

      :param data: Data from which to take property (never None)
      :type data: :class:`AnyType` | None
      :param property: Identifier of property in data (never None)
      :type property: str
      :param type: Type, Type of curves to display (optional)
      :type type: Literal['NONE', 'VECTOR', 'COLOR', 'HUE']
      :param levels: Show black/white levels (optional)
      :type levels: bool
      :param brush: Show brush options (optional)
      :type brush: bool
      :param use_negative_slope: Use a negative slope by default (optional)
      :type use_negative_slope: bool
      :param show_tone: Show tone options (optional)
      :type show_tone: bool
      :param show_presets: Show preset options (optional)
      :type show_presets: bool

   .. method:: template_curveprofile(data, property)

      A profile path editor used for custom profiles

      :param data: Data from which to take property (never None)
      :type data: :class:`AnyType` | None
      :param property: Identifier of property in data (never None)
      :type property: str

   .. method:: template_color_ramp(data, property, *, expand=False)

      Item. A color ramp widget.

      :param data: Data from which to take property (never None)
      :type data: :class:`AnyType` | None
      :param property: Identifier of property in data (never None)
      :type property: str
      :param expand: Expand button to show more detail (optional)
      :type expand: bool

   .. method:: template_icon(icon_value, *, scale=1.0)

      Display a large icon

      :param icon_value: Icon to display, (in [0, inf])
      :type icon_value: int
      :param scale: Scale, Scale the icon size (by the button size) (in [1, 100], optional)
      :type scale: float

   .. method:: template_icon_view(data, property, *, show_labels=False, scale=6.0, scale_popup=5.0)

      Enum. Large widget showing Icon previews.

      :param data: Data from which to take property (never None)
      :type data: :class:`AnyType` | None
      :param property: Identifier of property in data (never None)
      :type property: str
      :param show_labels: Show enum label in preview buttons (optional)
      :type show_labels: bool
      :param scale: UI Units, Scale the button icon size (by the button size) (in [1, 100], optional)
      :type scale: float
      :param scale_popup: Scale, Scale the popup icon size (by the button size) (in [1, 100], optional)
      :type scale_popup: float

   .. method:: template_histogram(data, property)

      Item. A histogramm widget to analyze imaga data.

      :param data: Data from which to take property (never None)
      :type data: :class:`AnyType` | None
      :param property: Identifier of property in data (never None)
      :type property: str

   .. method:: template_waveform(data, property)

      Item. A waveform widget to analyze imaga data.

      :param data: Data from which to take property (never None)
      :type data: :class:`AnyType` | None
      :param property: Identifier of property in data (never None)
      :type property: str

   .. method:: template_vectorscope(data, property)

      Item. A vectorscope widget to analyze imaga data.

      :param data: Data from which to take property (never None)
      :type data: :class:`AnyType` | None
      :param property: Identifier of property in data (never None)
      :type property: str

   .. method:: template_layers(data, property, used_layers_data, used_layers_property, active_layer)

      template_layers

      :param data: Data from which to take property (never None)
      :type data: :class:`AnyType` | None
      :param property: Identifier of property in data (never None)
      :type property: str
      :param used_layers_data: Data from which to take property
      :type used_layers_data: :class:`AnyType` | None
      :param used_layers_property: Identifier of property in data (never None)
      :type used_layers_property: str
      :param active_layer: Active Layer, (in [0, inf])
      :type active_layer: int

   .. method:: template_color_picker(data, property, *, value_slider=False, lock=False, lock_luminosity=False, cubic=False)

      Item. A color wheel widget to pick colors.

      :param data: Data from which to take property (never None)
      :type data: :class:`AnyType` | None
      :param property: Identifier of property in data (never None)
      :type property: str
      :param value_slider: Display the value slider to the right of the color wheel (optional)
      :type value_slider: bool
      :param lock: Lock the color wheel display to value 1.0 regardless of actual color (optional)
      :type lock: bool
      :param lock_luminosity: Keep the color at its original vector length (optional)
      :type lock_luminosity: bool
      :param cubic: Cubic saturation for picking values close to white (optional)
      :type cubic: bool

   .. method:: template_palette(data, property, *, color=False)

      Item. A palette used to pick colors.

      :param data: Data from which to take property (never None)
      :type data: :class:`AnyType` | None
      :param property: Identifier of property in data (never None)
      :type property: str
      :param color: Display the colors as colors or values (optional)
      :type color: bool

   .. method:: template_image_layers(image, image_user)

      template_image_layers

      :type image: :class:`Image` | None
      :type image_user: :class:`ImageUser` | None

   .. method:: template_image(data, property, image_user, *, compact=False, multiview=False)

      Item(s). User interface for selecting images and their source paths.

      :param data: Data from which to take property (never None)
      :type data: :class:`AnyType` | None
      :param property: Identifier of property in data (never None)
      :type property: str
      :param image_user: (never None)
      :type image_user: :class:`ImageUser` | None
      :param compact: Use more compact layout (optional)
      :type compact: bool
      :param multiview: Expose Multi-View options (optional)
      :type multiview: bool

   .. method:: template_image_settings(image_settings, *, color_management=False)

      User interface for setting image format options

      :param image_settings: (never None)
      :type image_settings: :class:`ImageFormatSettings` | None
      :param color_management: Show color management settings (optional)
      :type color_management: bool

   .. method:: template_image_stereo_3d(stereo_3d_format)

      User interface for setting image stereo 3d options

      :param stereo_3d_format: (never None)
      :type stereo_3d_format: :class:`Stereo3dFormat` | None

   .. method:: template_image_views(image_settings)

      User interface for setting image views output options

      :param image_settings: (never None)
      :type image_settings: :class:`ImageFormatSettings` | None

   .. method:: template_movieclip(data, property, *, compact=False)

      Item(s). User interface for selecting movie clips and their source paths.

      :param data: Data from which to take property (never None)
      :type data: :class:`AnyType` | None
      :param property: Identifier of property in data (never None)
      :type property: str
      :param compact: Use more compact layout (optional)
      :type compact: bool

   .. method:: template_track(data, property)

      Item. A movie-track widget to preview tracking image.

      :param data: Data from which to take property (never None)
      :type data: :class:`AnyType` | None
      :param property: Identifier of property in data (never None)
      :type property: str

   .. method:: template_marker(data, property, clip_user, track, *, compact=False)

      Item. A widget to control single marker settings.

      :param data: Data from which to take property (never None)
      :type data: :class:`AnyType` | None
      :param property: Identifier of property in data (never None)
      :type property: str
      :param clip_user: (never None)
      :type clip_user: :class:`MovieClipUser` | None
      :param track: (never None)
      :type track: :class:`MovieTrackingTrack` | None
      :param compact: Use more compact layout (optional)
      :type compact: bool

   .. method:: template_movieclip_information(data, property, clip_user)

      Item. Movie clip information data.

      :param data: Data from which to take property (never None)
      :type data: :class:`AnyType` | None
      :param property: Identifier of property in data (never None)
      :type property: str
      :param clip_user: (never None)
      :type clip_user: :class:`MovieClipUser` | None

   .. method:: template_list(listtype_name, list_id, dataptr, propname, active_dataptr, active_propname, *, item_dyntip_propname="", rows=5, maxrows=5, type='DEFAULT', columns=9, sort_reverse=False, sort_lock=False)

      Item. A list widget to display data, e.g. vertexgroups.

      :param listtype_name: Identifier of the list type to use (never None)
      :type listtype_name: str
      :param list_id: Identifier of this list widget. Necessary to tell apart different list widgets. Mandatory when using default "UI_UL_list" class. If this not an empty string, the uilist gets a custom ID, otherwise it takes the name of the class used to define the uilist (for example, if the class name is "OBJECT_UL_vgroups", and list_id is not set by the script, then bl_idname = "OBJECT_UL_vgroups") (never None)
      :type list_id: str
      :param dataptr: Data from which to take the Collection property
      :type dataptr: :class:`AnyType` | None
      :param propname: Identifier of the Collection property in data (never None)
      :type propname: str
      :param active_dataptr: Data from which to take the integer property, index of the active item (never None)
      :type active_dataptr: :class:`AnyType` | None
      :param active_propname: Identifier of the integer property in active_data, index of the active item (never None)
      :type active_propname: str
      :param item_dyntip_propname: Identifier of a string property in items, to use as tooltip content (optional, never None)
      :type item_dyntip_propname: str
      :param rows: Default and minimum number of rows to display (in [0, inf], optional)
      :type rows: int
      :param maxrows: Default maximum number of rows to display (in [0, inf], optional)
      :type maxrows: int
      :param type: Type, Type of layout to use (optional)
      :type type: Literal[:ref:`rna_enum_uilist_layout_type_items`]
      :param columns: Number of items to display per row, for GRID layout (in [0, inf], optional)
      :type columns: int
      :param sort_reverse: Display items in reverse order by default (optional)
      :type sort_reverse: bool
      :param sort_lock: Lock display order to default value (optional)
      :type sort_lock: bool

   .. method:: template_running_jobs()

      template_running_jobs


   .. method:: template_operator_search()

      template_operator_search


   .. method:: template_menu_search()

      template_menu_search


   .. method:: template_header_3D_mode()

      


   .. method:: template_edit_mode_selection()

      Inserts common 3DView Edit modes header UI (selector for selection mode)


   .. method:: template_reports_banner()

      template_reports_banner


   .. method:: template_input_status()

      template_input_status


   .. method:: template_status_info()

      template_status_info


   .. method:: template_node_link(ntree, node, socket)

      template_node_link

      :type ntree: :class:`NodeTree` | None
      :type node: :class:`Node` | None
      :type socket: :class:`NodeSocket` | None

   .. method:: template_node_view(ntree, node, socket)

      template_node_view

      :type ntree: :class:`NodeTree` | None
      :type node: :class:`Node` | None
      :type socket: :class:`NodeSocket` | None

   .. method:: template_node_operator_registration_errors(*, idname="")

      template_node_operator_registration_errors

      :param idname: (optional, never None)
      :type idname: str

   .. method:: template_node_asset_menu_items(*, catalog_path="", operator='ADD')

      template_node_asset_menu_items

      :param catalog_path: (optional, never None)
      :type catalog_path: str
      :param operator: Operator, The operator the asset menu will use (optional)

         - ``ADD``
           Add Node -- Add a node to the active tree..
         - ``SWAP``
           Swap Node -- Replace the selected nodes with the specified type..
      :type operator: Literal['ADD', 'SWAP']

   .. method:: template_modifier_asset_menu_items(*, catalog_path="", skip_essentials=False)

      template_modifier_asset_menu_items

      :param catalog_path: (optional, never None)
      :type catalog_path: str
      :param skip_essentials: (optional)
      :type skip_essentials: bool

   .. method:: template_node_operator_asset_menu_items(*, catalog_path="")

      template_node_operator_asset_menu_items

      :param catalog_path: (optional, never None)
      :type catalog_path: str

   .. method:: template_node_operator_asset_root_items()

      template_node_operator_asset_root_items


   .. method:: template_texture_user()

      template_texture_user


   .. method:: template_keymap_item_properties(item)

      template_keymap_item_properties

      :param item: (never None)
      :type item: :class:`KeyMapItem` | None

   .. method:: template_component_menu(data, property, *, name="")

      Item. Display expanded property in a popup menu

      :param data: Data from which to take property
      :type data: :class:`AnyType` | None
      :param property: Identifier of property in data (never None)
      :type property: str
      :param name: (optional, never None)
      :type name: str

   .. method:: template_colorspace_settings(data, property)

      Item. A widget to control input color space settings.

      :param data: Data from which to take property (never None)
      :type data: :class:`AnyType` | None
      :param property: Identifier of property in data (never None)
      :type property: str

   .. method:: template_colormanaged_view_settings(data, property)

      Item. A widget to control color managed view settings.

      :param data: Data from which to take property (never None)
      :type data: :class:`AnyType` | None
      :param property: Identifier of property in data (never None)
      :type property: str

   .. method:: template_node_socket(*, color=(0.0, 0.0, 0.0, 1.0))

      Node Socket Icon

      :param color: Color, (array of 4 items, in [0, 1], optional)
      :type color: Sequence[float]

   .. method:: template_cache_file(data, property)

      Item(s). User interface for selecting cache files and their source paths

      :param data: Data from which to take property (never None)
      :type data: :class:`AnyType` | None
      :param property: Identifier of property in data (never None)
      :type property: str

   .. method:: template_cache_file_velocity(data, property)

      Show cache files velocity properties

      :param data: Data from which to take property (never None)
      :type data: :class:`AnyType` | None
      :param property: Identifier of property in data (never None)
      :type property: str

   .. method:: template_cache_file_time_settings(data, property)

      Show cache files time settings

      :param data: Data from which to take property (never None)
      :type data: :class:`AnyType` | None
      :param property: Identifier of property in data (never None)
      :type property: str

   .. method:: template_cache_file_layers(data, property)

      Show cache files override layers properties

      :param data: Data from which to take property (never None)
      :type data: :class:`AnyType` | None
      :param property: Identifier of property in data (never None)
      :type property: str

   .. method:: template_recent_files(*, rows=6)

      Show list of recently saved .blend files

      :param rows: Maximum number of items to show (in [1, inf], optional)
      :type rows: int
      :return: Number of items drawn (in [0, inf])
      :rtype: int

   .. method:: template_file_select_path(params)

      Item. A text button to set the active file browser path.

      :type params: :class:`FileSelectParams` | None

   .. method:: template_event_from_keymap_item(item, *, text="", text_ctxt="", translate=True)

      Display keymap item as icons/text

      :param item: Item, (never None)
      :type item: :class:`KeyMapItem` | None
      :param text: Override automatic text of the item (optional)
      :type text: str
      :param text_ctxt: Override automatic translation context of the given text (optional)
      :type text_ctxt: str
      :param translate: Translate the given text, when UI translation is enabled (optional)
      :type translate: bool

   .. method:: template_light_linking_collection(context_layout, data, property)

      Visualization of a content of a light linking collection

      :param context_layout: Layout to set active list element as context properties (never None)
      :type context_layout: :class:`UILayout` | None
      :param data: Data from which to take property (never None)
      :type data: :class:`AnyType` | None
      :param property: Identifier of property in data (never None)
      :type property: str

   .. method:: template_bone_collection_tree()

      Show bone collections tree


   .. method:: template_grease_pencil_layer_tree()

      View of the active Grease Pencil layer tree


   .. method:: template_node_tree_interface(interface)

      Show a node tree interface

      :param interface: Node Tree Interface, Interface of a node tree to display (never None)
      :type interface: :class:`NodeTreeInterface` | None

   .. method:: template_node_inputs(node)

      Show a node settings and input socket values

      :param node: Node, Display inputs of this node (never None)
      :type node: :class:`Node` | None

   .. method:: template_asset_shelf_popover(asset_shelf, *, name="", icon='NONE', icon_value=0)

      Create a button to open an asset shelf in a popover

      :param asset_shelf: Identifier of the asset shelf to display (``bl_idname``) (never None)
      :type asset_shelf: str
      :param name: Optional name to indicate the active asset (optional)
      :type name: str
      :param icon: Icon, Override automatic icon of the item (optional)
      :type icon: Literal[:ref:`rna_enum_icon_items`]
      :param icon_value: Icon Value, Override automatic icon of the item (in [0, inf], optional)
      :type icon_value: int

   .. method:: template_popup_confirm(operator, *, text="", text_ctxt="", translate=True, icon='NONE', cancel_text="", cancel_default=False)

      Add confirm & cancel buttons into a popup which will close the popup when pressed

      :param operator: Identifier of the operator (never None)
      :type operator: str
      :param text: Override automatic text of the item (optional)
      :type text: str
      :param text_ctxt: Override automatic translation context of the given text (optional)
      :type text_ctxt: str
      :param translate: Translate the given text, when UI translation is enabled (optional)
      :type translate: bool
      :param icon: Icon, Override automatic icon of the item (optional)
      :type icon: Literal[:ref:`rna_enum_icon_items`]
      :param cancel_text: Optional text to use for the cancel, not shown when an empty string (optional, never None)
      :type cancel_text: str
      :param cancel_default: Cancel button by default (optional)
      :type cancel_default: bool
      :return: Operator properties to fill in
      :rtype: :class:`OperatorProperties`

   .. method:: template_shape_key_tree()

      Shape Key tree view


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


   .. method:: introspect()
   
      Return a list of dictionaries containing a textual representation of the UI layout.
   
      :rtype: list[dict[str, Any]]


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

   - :class:`AssetShelf.draw_context_menu`
   - :class:`Header.layout`
   - :class:`Menu.layout`
   - :class:`Node.draw_buttons`
   - :class:`Node.draw_buttons_ext`
   - :class:`NodeInternal.draw_buttons`
   - :class:`NodeInternal.draw_buttons_ext`
   - :class:`NodeSocket.draw`
   - :class:`NodeSocketStandard.draw`
   - :class:`NodeTreeInterfaceSocket.draw`
   - :class:`NodeTreeInterfaceSocketBool.draw`
   - :class:`NodeTreeInterfaceSocketBundle.draw`
   - :class:`NodeTreeInterfaceSocketClosure.draw`
   - :class:`NodeTreeInterfaceSocketCollection.draw`
   - :class:`NodeTreeInterfaceSocketColor.draw`
   - :class:`NodeTreeInterfaceSocketFloat.draw`
   - :class:`NodeTreeInterfaceSocketFloatAngle.draw`
   - :class:`NodeTreeInterfaceSocketFloatColorTemperature.draw`
   - :class:`NodeTreeInterfaceSocketFloatDistance.draw`
   - :class:`NodeTreeInterfaceSocketFloatFactor.draw`
   - :class:`NodeTreeInterfaceSocketFloatFrequency.draw`
   - :class:`NodeTreeInterfaceSocketFloatMass.draw`
   - :class:`NodeTreeInterfaceSocketFloatPercentage.draw`
   - :class:`NodeTreeInterfaceSocketFloatTime.draw`
   - :class:`NodeTreeInterfaceSocketFloatTimeAbsolute.draw`
   - :class:`NodeTreeInterfaceSocketFloatUnsigned.draw`
   - :class:`NodeTreeInterfaceSocketFloatWavelength.draw`
   - :class:`NodeTreeInterfaceSocketGeometry.draw`
   - :class:`NodeTreeInterfaceSocketImage.draw`
   - :class:`NodeTreeInterfaceSocketInt.draw`
   - :class:`NodeTreeInterfaceSocketIntFactor.draw`
   - :class:`NodeTreeInterfaceSocketIntPercentage.draw`
   - :class:`NodeTreeInterfaceSocketIntUnsigned.draw`
   - :class:`NodeTreeInterfaceSocketMaterial.draw`
   - :class:`NodeTreeInterfaceSocketMatrix.draw`
   - :class:`NodeTreeInterfaceSocketMenu.draw`
   - :class:`NodeTreeInterfaceSocketObject.draw`
   - :class:`NodeTreeInterfaceSocketRotation.draw`
   - :class:`NodeTreeInterfaceSocketShader.draw`
   - :class:`NodeTreeInterfaceSocketString.draw`
   - :class:`NodeTreeInterfaceSocketStringFilePath.draw`
   - :class:`NodeTreeInterfaceSocketTexture.draw`
   - :class:`NodeTreeInterfaceSocketVector.draw`
   - :class:`NodeTreeInterfaceSocketVector2D.draw`
   - :class:`NodeTreeInterfaceSocketVector4D.draw`
   - :class:`NodeTreeInterfaceSocketVectorAcceleration.draw`
   - :class:`NodeTreeInterfaceSocketVectorAcceleration2D.draw`
   - :class:`NodeTreeInterfaceSocketVectorAcceleration4D.draw`
   - :class:`NodeTreeInterfaceSocketVectorDirection.draw`
   - :class:`NodeTreeInterfaceSocketVectorDirection2D.draw`
   - :class:`NodeTreeInterfaceSocketVectorDirection4D.draw`
   - :class:`NodeTreeInterfaceSocketVectorEuler.draw`
   - :class:`NodeTreeInterfaceSocketVectorEuler2D.draw`
   - :class:`NodeTreeInterfaceSocketVectorEuler4D.draw`
   - :class:`NodeTreeInterfaceSocketVectorFactor.draw`
   - :class:`NodeTreeInterfaceSocketVectorFactor2D.draw`
   - :class:`NodeTreeInterfaceSocketVectorFactor4D.draw`
   - :class:`NodeTreeInterfaceSocketVectorPercentage.draw`
   - :class:`NodeTreeInterfaceSocketVectorPercentage2D.draw`
   - :class:`NodeTreeInterfaceSocketVectorPercentage4D.draw`
   - :class:`NodeTreeInterfaceSocketVectorTranslation.draw`
   - :class:`NodeTreeInterfaceSocketVectorTranslation2D.draw`
   - :class:`NodeTreeInterfaceSocketVectorTranslation4D.draw`
   - :class:`NodeTreeInterfaceSocketVectorVelocity.draw`
   - :class:`NodeTreeInterfaceSocketVectorVelocity2D.draw`
   - :class:`NodeTreeInterfaceSocketVectorVelocity4D.draw`
   - :class:`NodeTreeInterfaceSocketVectorXYZ.draw`
   - :class:`NodeTreeInterfaceSocketVectorXYZ2D.draw`
   - :class:`NodeTreeInterfaceSocketVectorXYZ4D.draw`
   - :class:`Operator.layout`
   - :class:`Panel.layout`
   - :class:`UILayout.box`
   - :class:`UILayout.column`
   - :class:`UILayout.column_flow`
   - :class:`UILayout.grid_flow`
   - :class:`UILayout.menu_pie`
   - :class:`UILayout.panel`
   - :class:`UILayout.panel`
   - :class:`UILayout.panel_prop`
   - :class:`UILayout.panel_prop`
   - :class:`UILayout.row`
   - :class:`UILayout.split`
   - :class:`UILayout.template_light_linking_collection`
   - :class:`UIList.draw_filter`
   - :class:`UIList.draw_item`
   - :class:`UIPieMenu.layout`
   - :class:`UIPopover.layout`
   - :class:`UIPopupMenu.layout`

