RenderResult(bpy_struct)
========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: RenderResult(bpy_struct)

   Result of rendering, including all layers and passes

   .. data:: layers

      (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`RenderLayer`]

   .. data:: resolution_x

      (in [-inf, inf], default 0, readonly)

      :type: int

   .. data:: resolution_y

      (in [-inf, inf], default 0, readonly)

      :type: int

   .. data:: views

      (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`RenderView`]

   .. method:: load_from_file(filepath)

      Copies the pixels of this render result from an image file

      :param filepath: File Name, Filename to load into this render tile, must be no smaller than the render result (never None)
      :type filepath: str

   .. method:: stamp_data_add_field(field, value)

      Add engine-specific stamp data to the result

      :param field: Field, Name of the stamp field to add (never None)
      :type field: str
      :param value: Value, Value of the stamp data (never None)
      :type value: str

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

   - :class:`RenderEngine.begin_result`
   - :class:`RenderEngine.end_result`
   - :class:`RenderEngine.get_result`
   - :class:`RenderEngine.update_result`

