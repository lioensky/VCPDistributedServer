BoneCollections(bpy_prop_collection)
====================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_prop`, :class:`bpy_prop_collection`

.. class:: BoneCollections(bpy_prop_collection)

   The Bone Collections of this Armature

   .. attribute:: active

      Armature's active bone collection

      :type: :class:`BoneCollection` | None

   .. attribute:: active_index

      The index of the Armature's active bone collection; -1 when there is no active collection. Note that this is indexing the underlying array of bone collections, which may not be in the order you expect. Root collections are listed first, and siblings are always sequential. Apart from that, bone collections can be in any order, and thus incrementing or decrementing this index can make the active bone collection jump around in unexpected ways. For a more predictable interface, use ``active`` or ``active_name``. (in [-inf, inf], default 0)

      :type: int

   .. attribute:: active_name

      The name of the Armature's active bone collection; empty when there is no active collection (default "", never None)

      :type: str

   .. data:: is_solo_active

      Read-only flag that indicates there is at least one bone collection marked as 'solo' (default False, readonly)

      :type: bool

   .. method:: new(name, *, parent=None)

      Add a new empty bone collection to the armature

      :param name: Name, Name of the new collection. Blender will ensure it is unique within the collections of the Armature. (never None)
      :type name: str
      :param parent: Parent Collection, If not None, the new bone collection becomes a child of this collection (optional)
      :type parent: :class:`BoneCollection` | None
      :return: Newly created bone collection
      :rtype: :class:`BoneCollection`

   .. method:: remove(bone_collection)

      Remove the bone collection from the armature. If this bone collection has any children, they will be reassigned to their grandparent; in other words, the children will take the place of the removed bone collection.

      :param bone_collection: Bone Collection, The bone collection to remove
      :type bone_collection: :class:`BoneCollection` | None

   .. method:: move(from_index, to_index)

      Move a bone collection to a different position in the collection list. This can only be used to reorder siblings, and not to change parent-child relationships.

      :param from_index: From Index, Index to move (in [-inf, inf])
      :type from_index: int
      :param to_index: To Index, Target index (in [-inf, inf])
      :type to_index: int

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

   - :class:`Armature.collections`

