Menu(bpy_struct)
================

.. currentmodule:: bpy.types


Basic Menu Example
++++++++++++++++++

Here is an example of a simple menu. Menus differ from panels in that they must
reference from a header, panel or another menu.

Notice the 'CATEGORY_MT_name' in  :class:`Menu.bl_idname`, this is a naming
convention for menus.

.. note::

   Menu subclasses must be registered before referencing them from Blender.

.. note::

   Menus have their :class:`UILayout.operator_context` initialized as
   'EXEC_REGION_WIN' rather than 'INVOKE_REGION_WIN' (see :ref:`Execution Context <rna_enum_operator_context_items>`).
   If the operator context needs to initialize inputs from the
   :class:`Operator.invoke` function, then this needs to be explicitly set.
   When a menu is added to UI elements such as a panel or header,
   the operator execution context will be inherited from them.

.. literalinclude:: ./examples/bpy.types.Menu.0.py
   :lines: 24-


Submenus
++++++++

This menu demonstrates some different functions.

.. literalinclude:: ./examples/bpy.types.Menu.1.py
   :lines: 7-


Extending Menus
+++++++++++++++

When creating menus for add-ons you can't reference menus
in Blender's default scripts.
Instead, the add-on can add menu items to existing menus.

The function menu_draw acts like :class:`Menu.draw`.

.. literalinclude:: ./examples/bpy.types.Menu.2.py
   :lines: 11-


Preset Menus
++++++++++++

Preset menus are simply a convention that uses a menu sub-class
to perform the common task of managing presets.

This example shows how you can add a preset menu.

This example uses the object display options,
however you can use properties defined by your own scripts too.

.. literalinclude:: ./examples/bpy.types.Menu.3.py
   :lines: 14-


Extending the Button Context Menu
+++++++++++++++++++++++++++++++++

This example enables you to insert your own menu entry into the common
right click menu that you get while hovering over a UI button (e.g. operator,
value field, color, string, etc.)

To make the example work, you have to first select an object
then right click on an user interface element (maybe a color in the
material properties) and choose *Execute Custom Action*.

Executing the operator will then print all values.

.. literalinclude:: ./examples/bpy.types.Menu.4.py
   :lines: 16-

base class --- :class:`bpy_struct`

.. class:: Menu(bpy_struct)

   Editor menu containing buttons

   .. attribute:: bl_description

      (default "")

      :type: str

   .. attribute:: bl_idname

      If this is set, the menu gets a custom ID, otherwise it takes the name of the class used to define the menu (for example, if the class name is "OBJECT_MT_hello", and bl_idname is not set by the script, then bl_idname = "OBJECT_MT_hello") (default "", never None)

      :type: str

   .. attribute:: bl_label

      The menu label (default "", never None)

      :type: str

   .. attribute:: bl_options

      Options for this menu type (default set())

      - ``SEARCH_ON_KEY_PRESS``
        Search on Key Press -- Open a menu search when a key pressed while the menu is open.

      :type: set[Literal['SEARCH_ON_KEY_PRESS']]

   .. attribute:: bl_owner_id

      (default "", never None)

      :type: str

   .. attribute:: bl_translation_context

      (default "*", never None)

      :type: str

   .. data:: layout

      Defines the structure of the menu in the UI (readonly)

      :type: :class:`UILayout` | None

   .. classmethod:: poll(context)

      If this method returns a non-null output, then the menu can be drawn

      :type context: :class:`Context` | None
      :rtype: bool

   .. method:: draw(context)

      Draw UI elements into the menu UI layout

      :type context: :class:`Context` | None

   .. classmethod:: append(draw_func)

      Append a draw function to this menu,
      takes the same arguments as the menus draw function

   .. classmethod:: draw_collapsible(context, layout)

   .. method:: draw_preset(_context)

      Define these on the subclass:
      - preset_operator (string)
      - preset_subdir (string)
      
      Optionally:
      - preset_add_operator (string)
      - preset_extensions (set of strings)
      - preset_operator_defaults (dict of keyword args)

   .. classmethod:: is_extended()

   .. method:: path_menu(searchpaths, operator, *, props_default=None, prop_filepath='filepath', filter_ext=None, filter_path=None, display_name=None, add_operator=None, add_operator_props=None, translate=True)

      Populate a menu from a list of paths.
      
      :param searchpaths: Paths to scan.
      :type searchpaths: Sequence[str]
      :param operator: The operator id to use with each file.
      :type operator: str
      :param prop_filepath: Optional operator filepath property (defaults to "filepath").
      :type prop_filepath: str
      :param props_default: Properties to assign to each operator.
      :type props_default: dict[str, Any] | None
      :param filter_ext: Optional callback that takes the file extensions.
      
         Returning false excludes the file from the list.
      
      :type filter_ext: Callable[[str], bool] | None
      :param display_name: Optional callback that takes the full path, returns the name to display.
      :type display_name: Callable[[str], str] | None

   .. classmethod:: prepend(draw_func)

      Prepend a draw function to this menu, takes the same arguments as
      the menus draw function

   .. classmethod:: remove(draw_func)

      Remove a draw function that has been added to this menu.

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

