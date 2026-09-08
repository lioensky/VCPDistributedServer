StudioLight(bpy_struct)
=======================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: StudioLight(bpy_struct)

   Studio light

   .. data:: has_specular_highlight_pass

      Studio light image file has separate "diffuse" and "specular" passes (default False, readonly)

      :type: bool

   .. data:: index

      (in [-inf, inf], default 0, readonly)

      :type: int

   .. data:: is_user_defined

      (default False, readonly)

      :type: bool

   .. data:: light_ambient

      Color of the ambient light that uniformly lit the scene (array of 3 items, in [0, inf], default (0.0, 0.0, 0.0), readonly)

      :type: :class:`mathutils.Color`

   .. data:: name

      (default "", readonly, never None)

      :type: str

   .. data:: path

      (default "", readonly, never None)

      :type: str

   .. data:: solid_lights

      Lights used to display objects in solid draw mode (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`UserSolidLight`]

   .. data:: type

      (default ``'STUDIO'``, readonly)

      :type: Literal['STUDIO', 'WORLD', 'MATCAP']

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

   - :class:`Preferences.studio_lights`
   - :class:`StudioLights.load`
   - :class:`StudioLights.new`
   - :class:`StudioLights.remove`
   - :class:`View3DShading.selected_studio_light`

