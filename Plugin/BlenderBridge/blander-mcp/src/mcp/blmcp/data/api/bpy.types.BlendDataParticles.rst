BlendDataParticles(bpy_prop_collection)
=======================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_prop`, :class:`bpy_prop_collection`

.. class:: BlendDataParticles(bpy_prop_collection)

   Collection of particle settings

   .. method:: new(name)

      Add a new particle settings instance to the main database

      :param name: New name for the data-block (never None)
      :type name: str
      :return: New particle settings data-block
      :rtype: :class:`ParticleSettings`

   .. method:: remove(particle, *, do_unlink=True, do_id_user=True, do_ui_user=True)

      Remove a particle settings instance from the current blendfile

      :param particle: Particle Settings to remove (never None)
      :type particle: :class:`ParticleSettings` | None
      :param do_unlink: Unlink all usages of those particle settings before deleting them (optional)
      :type do_unlink: bool
      :param do_id_user: Decrement user counter of all data-blocks used by this particle settings (optional)
      :type do_id_user: bool
      :param do_ui_user: Make sure interface does not reference this particle settings (optional)
      :type do_ui_user: bool

   .. method:: tag(value)

      tag

      :param value: Value
      :type value: bool

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

   - :class:`BlendData.particles`

