Header(bpy_struct)
==================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: Header(bpy_struct)

   Editor header containing UI elements

   .. attribute:: bl_idname

      If this is set, the header gets a custom ID, otherwise it takes the name of the class used to define the header; for example, if the class name is "OBJECT_HT_hello", and bl_idname is not set by the script, then bl_idname = "OBJECT_HT_hello" (default "", never None)

      :type: str

   .. attribute:: bl_region_type

      The region where the header is going to be used in (defaults to header region) (default ``'HEADER'``)

      :type: Literal[:ref:`rna_enum_region_type_items`]

   .. attribute:: bl_space_type

      The space where the header is going to be used in (default ``'EMPTY'``)

      :type: Literal[:ref:`rna_enum_space_type_items`]

   .. data:: layout

      Structure of the header in the UI (readonly)

      :type: :class:`UILayout` | None

   .. method:: draw(context)

      Draw UI elements into the header UI layout

      :type context: :class:`Context` | None

   .. classmethod:: append(draw_func)

      Append a draw function to this menu,
      takes the same arguments as the menus draw function

   .. classmethod:: is_extended()

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

