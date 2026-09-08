Operator(bpy_struct)
====================

.. currentmodule:: bpy.types


Basic Operator Example
++++++++++++++++++++++

This script shows simple operator which prints a message.

Since the operator only has an :class:`Operator.execute` function it takes no
user input.

The function should return ``{'FINISHED'}`` or ``{'CANCELLED'}``, the latter
meaning that operator execution was aborted without making any changes, and
that no undo step will created (see next example for more info about undo).

.. note::

   Operator subclasses must be registered before accessing them from Blender.

.. literalinclude:: ./examples/bpy.types.Operator.0.py
   :lines: 19-


.. _operator_modifying_blender_data_undo:

Modifying Blender Data & Undo
+++++++++++++++++++++++++++++

Any operator modifying Blender data should enable the ``'UNDO'`` option.
This will make Blender automatically create an undo step when the operator
finishes its ``execute`` (or ``invoke``, see below) functions, and returns
``{'FINISHED'}``.

Otherwise, no undo step will be created, which will at best corrupt the
undo stack and confuse the user (since modifications done by the operator
may either not be undoable, or be undone together with other edits done
before). In many cases, this can even lead to data corruption and crashes.

Note that when an operator returns ``{'CANCELLED'}``, no undo step will be
created. This means that if an error occurs *after* modifying some data
already, it is better to return ``{'FINISHED'}``, unless it is possible to
fully undo the changes before returning.

.. note::

   Most examples in this page do not do any edit to Blender data, which is
   why it is safe to keep the default ``bl_options`` value for these operators.

.. note::

   In some complex cases, the automatic undo step created on operator exit may
   not be enough. For example, if the operator does mode switching, or calls
   other operators that should create an extra undo step, etc.

   Such manual undo push is possible using the :class:`bpy.ops.ed.undo_push`
   function. Be careful though, this is considered an advanced feature and
   requires some understanding of the actual undo system in Blender code.

.. literalinclude:: ./examples/bpy.types.Operator.1.py
   :lines: 38-


Invoke Function
+++++++++++++++

:class:`Operator.invoke` is used to initialize the operator from the context
at the moment the operator is called.
invoke() is typically used to assign properties which are then used by
execute().
Some operators don't have an execute() function, removing the ability to be
repeated from a script or macro.

When an operator is called via :mod:`bpy.ops`, the execution context depends
on the argument provided to :mod:`bpy.ops`. By default, it uses execute().
When an operator is activated from a button or menu item, it follows
the setting in :class:`UILayout.operator_context`. In most cases, invoke() is used.
Running an operator via a key shortcut always uses invoke(),
and this behavior cannot be changed.

This example shows how to define an operator which gets mouse input to
execute a function and that this operator can be invoked or executed from
the Python API.

Also notice this operator defines its own properties, these are different
to typical class properties because Blender registers them with the
operator, to use as arguments when called, saved for operator undo/redo and
automatically added into the user interface.

.. literalinclude:: ./examples/bpy.types.Operator.2.py
   :lines: 28-


Calling a File Selector
+++++++++++++++++++++++
This example shows how an operator can use the file selector.

Notice the invoke function calls a window manager method and returns
``{'RUNNING_MODAL'}``, this means the file selector stays open and the operator does not
exit immediately after invoke finishes.

The file selector runs the operator, calling :class:`Operator.execute` when the
user confirms.

The :class:`Operator.poll` function is optional, used to check if the operator
can run.

.. literalinclude:: ./examples/bpy.types.Operator.3.py
   :lines: 16-


Dialog Box
++++++++++

This operator uses its :class:`Operator.invoke` function to call a popup.

.. literalinclude:: ./examples/bpy.types.Operator.4.py
   :lines: 7-


Custom Drawing
++++++++++++++

By default operator properties use an automatic user interface layout.
If you need more control you can create your own layout with a
:class:`Operator.draw` function.

This works like the :class:`Panel` and :class:`Menu` draw functions, its used
for dialogs and file selectors.

.. literalinclude:: ./examples/bpy.types.Operator.5.py
   :lines: 12-


.. _modal_operator:

Modal Execution
+++++++++++++++

This operator defines a :class:`Operator.modal` function that will keep being
run to handle events until it returns ``{'FINISHED'}`` or ``{'CANCELLED'}``.

Modal operators run every time a new event is detected, such as a mouse click
or key press. Conversely, when no new events are detected, the modal operator
will not run. Modal operators are especially useful for interactive tools, an
operator can have its own state where keys toggle options as the operator runs.
Grab, Rotate, Scale, and Fly-Mode are examples of modal operators.

:class:`Operator.invoke` is used to initialize the operator as being active
by returning ``{'RUNNING_MODAL'}``, initializing the modal loop.

Notice ``__init__()`` and ``__del__()`` are declared.
For other operator types they are not useful but for modal operators they will
be called before the :class:`Operator.invoke` and after the operator finishes.
Also see the
:ref:`class construction and destruction section <info_overview_class_construction_destruction>`.

.. literalinclude:: ./examples/bpy.types.Operator.6.py
   :lines: 25-


Enum Search Popup
+++++++++++++++++

You may want to have an operator prompt the user to select an item
from a search field, this can be done using :class:`bpy.types.Operator.invoke_search_popup`.

.. literalinclude:: ./examples/bpy.types.Operator.7.py
   :lines: 8-

base class --- :class:`bpy_struct`

.. class:: Operator(bpy_struct)

   Storage of an operator being executed, or registered after execution

   .. attribute:: bl_cursor_pending

      Cursor to use when waiting for the user to select a location to activate the operator (when ``bl_options`` has ``DEPENDS_ON_CURSOR`` set) (default ``'DEFAULT'``)

      :type: Literal[:ref:`rna_enum_window_cursor_items`]

   .. attribute:: bl_description

      (default "", never None)

      :type: str

   .. attribute:: bl_idname

      (default "", never None)

      :type: str

   .. attribute:: bl_label

      (default "", never None)

      :type: str

   .. attribute:: bl_options

      Options for this operator type (default set())

      :type: set[Literal[:ref:`rna_enum_operator_type_flag_items`]]

   .. attribute:: bl_translation_context

      (default "Operator", never None)

      :type: str

   .. attribute:: bl_undo_group

      (default "", never None)

      :type: str

   .. data:: has_reports

      Operator has a set of reports (warnings and errors) from last execution (default False, readonly)

      :type: bool

   .. data:: layout

      (readonly)

      :type: :class:`UILayout` | None

   .. data:: macros

      (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`Macro`]

   .. data:: name

      (default "", readonly, never None)

      :type: str

   .. data:: options

      Runtime options (readonly, never None)

      :type: :class:`OperatorOptions`

   .. data:: properties

      (readonly, never None)

      :type: :class:`OperatorProperties`

   .. attribute:: bl_property

      The name of a property to use as this operators primary property.
      Currently this is only used to select the default property when
      expanding an operator into a menu.
      
      :type: str

   .. method:: report(type, message)

      report

      :param type: Type
      :type type: set[Literal[:ref:`rna_enum_wm_report_items`]]
      :param message: Report Message, (never None)
      :type message: str

   .. method:: is_repeat()

      is_repeat

      :return: result
      :rtype: bool

   .. classmethod:: poll(context)

      Test if the operator can be called or not

      :param context: (never None)
      :type context: :class:`Context` | None
      :rtype: bool

   .. method:: execute(context)

      Execute the operator

      :param context: (never None)
      :type context: :class:`Context` | None
      :return: result
      :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

   .. method:: check(context)

      Check the operator settings, return True to signal a change to redraw

      :param context: (never None)
      :type context: :class:`Context` | None
      :return: result
      :rtype: bool

   .. method:: invoke(context, event)

      Invoke the operator

      :param context: (never None)
      :type context: :class:`Context` | None
      :param event: (never None)
      :type event: :class:`Event` | None
      :return: result
      :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

   .. method:: modal(context, event)

      Modal operator function

      :param context: (never None)
      :type context: :class:`Context` | None
      :param event: (never None)
      :type event: :class:`Event` | None
      :return: result
      :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

   .. method:: draw(context)

      Draw function for the operator

      :param context: (never None)
      :type context: :class:`Context` | None

   .. method:: cancel(context)

      Called when the operator is canceled

      :param context: (never None)
      :type context: :class:`Context` | None

   .. classmethod:: description(context, properties)

      Compute a description string that depends on parameters

      :param context: (never None)
      :type context: :class:`Context` | None
      :param properties: (never None)
      :type properties: :class:`OperatorProperties` | None
      :return: result
      :rtype: str

   .. method:: as_keywords(*, ignore=())

      :return: A copy of the properties as a dictionary.
      :rtype: dict[str, Any]

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


   .. classmethod:: poll_message_set(message, *args)
   
      Set the message to show in the tool-tip when poll fails.
   
      When message is callable, additional user defined positional arguments are passed to the message function.
   
      :param message: The message or a function that returns the message.
      :type message: str | Callable[..., str | None]
      :param args: A sequence of arguments to pass to ``message``, if it's a callable, otherwise argument is not available.
      :type args: Any


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

   - :mod:`bpy.context.active_operator`
   - :class:`SpaceFileBrowser.active_operator`
   - :class:`SpaceFileBrowser.operator`
   - :class:`Window.modal_operators`
   - :class:`WindowManager.fileselect_add`
   - :class:`WindowManager.invoke_confirm`
   - :class:`WindowManager.invoke_popup`
   - :class:`WindowManager.invoke_props_dialog`
   - :class:`WindowManager.invoke_props_popup`
   - :class:`WindowManager.invoke_search_popup`
   - :class:`WindowManager.modal_handler_add`
   - :class:`WindowManager.operators`

