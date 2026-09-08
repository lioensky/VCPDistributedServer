Macro(bpy_struct)
=================

.. currentmodule:: bpy.types


Example Macro
+++++++++++++

This example creates a simple macro operator that
moves the active object and then rotates it.
It demonstrates:

- Defining a macro operator class.
- Registering it and defining sub-operators.
- Setting property values for each step.

.. literalinclude:: ./examples/bpy.types.Macro.0.py
   :lines: 14-

base class --- :class:`bpy_struct`

.. class:: Macro(bpy_struct)

   Storage of a macro operator being executed, or registered after execution

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

   .. data:: name

      (default "", readonly, never None)

      :type: str

   .. data:: properties

      (readonly, never None)

      :type: :class:`OperatorProperties`

   .. method:: report(type, message)

      report

      :param type: Type
      :type type: set[Literal[:ref:`rna_enum_wm_report_items`]]
      :param message: Report Message, (never None)
      :type message: str

   .. classmethod:: poll(context)

      Test if the operator can be called or not

      :param context: (never None)
      :type context: :class:`Context` | None
      :rtype: bool

   .. method:: draw(context)

      Draw function for the operator

      :param context: (never None)
      :type context: :class:`Context` | None

   .. classmethod:: define(operator)

      Append an operator to a registered macro class.
      
      :param operator: Identifier of the operator. This does not have to be defined when this function is called.
      :type operator: str
      :return: The operator macro for property access.
      :rtype: :class:`OperatorMacro`

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

   - :class:`Operator.macros`

