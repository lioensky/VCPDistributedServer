BlendDataMeshes(bpy_prop_collection)
====================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_prop`, :class:`bpy_prop_collection`

.. class:: BlendDataMeshes(bpy_prop_collection)

   Collection of meshes

   .. method:: new(name)

      Add a new mesh to the main database

      :param name: New name for the data-block (never None)
      :type name: str
      :return: New mesh data-block
      :rtype: :class:`Mesh`

   .. method:: new_from_object(object, *, preserve_all_data_layers=False, depsgraph=None)

      Add a new mesh created from given object (undeformed geometry if object is original, and final evaluated geometry, with all modifiers etc., if object is evaluated)

      :param object: Object to create mesh from (never None)
      :type object: :class:`Object` | None
      :param preserve_all_data_layers: Preserve all data layers in the mesh, like UV maps and vertex groups. By default Blender only computes the subset of data layers needed for viewport display and rendering, for better performance. (optional)
      :type preserve_all_data_layers: bool
      :param depsgraph: Dependency Graph, Evaluated dependency graph which is required when preserve_all_data_layers is true (optional)
      :type depsgraph: :class:`Depsgraph` | None
      :return: Mesh created from object, remove it if it is only used for export
      :rtype: :class:`Mesh`

   .. method:: remove(mesh, *, do_unlink=True, do_id_user=True, do_ui_user=True)

      Remove a mesh from the current blendfile

      :param mesh: Mesh to remove (never None)
      :type mesh: :class:`Mesh` | None
      :param do_unlink: Unlink all usages of this mesh before deleting it (WARNING: will also delete objects instancing that mesh data) (optional)
      :type do_unlink: bool
      :param do_id_user: Decrement user counter of all data-blocks used by this mesh data (optional)
      :type do_id_user: bool
      :param do_ui_user: Make sure interface does not reference this mesh data (optional)
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

   - :class:`BlendData.meshes`

