BoneCollection(bpy_struct)
==========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: BoneCollection(bpy_struct)

   Bone collection in an Armature data-block

   .. data:: bones

      Bones assigned to this bone collection. In armature edit mode this will always return an empty list of bones, as the bone collection memberships are only synchronized when exiting edit mode. (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`Bone`]

   .. attribute:: child_number

      Index of this collection into its parent's list of children. Note that finding this index requires a scan of all the bone collections, so do access this with care. (in [-inf, inf], default 0)

      :type: int

   .. data:: children

      (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`BoneCollection`]

   .. data:: index

      Index of this bone collection in the armature.collections_all array. Note that finding this index requires a scan of all the bone collections, so do access this with care. (in [-inf, inf], default 0, readonly)

      :type: int

   .. data:: is_editable

      This collection is owned by a local Armature, or was added via a library override in the current blend file (default False, readonly)

      :type: bool

   .. attribute:: is_expanded

      This bone collection is expanded in the bone collections tree view (default False)

      :type: bool

   .. data:: is_local_override

      This collection was added via a library override in the current blend file (default False, readonly)

      :type: bool

   .. attribute:: is_solo

      Show only this bone collection, and others also marked as 'solo' (default False)

      :type: bool

   .. attribute:: is_visible

      Bones in this collection will be visible in pose/object mode (default False)

      :type: bool

   .. data:: is_visible_ancestors

      True when all of the ancestors of this bone collection are marked as visible; always True for root bone collections (default False, readonly)

      :type: bool

   .. data:: is_visible_effectively

      Whether this bone collection is effectively visible in the viewport. This is True when this bone collection and all of its ancestors are visible, or when it is marked as 'solo'. (default False, readonly)

      :type: bool

   .. attribute:: name

      Unique within the Armature (default "", never None)

      :type: str

   .. attribute:: parent

      Parent bone collection. Note that accessing this requires a scan of all the bone collections to find the parent.

      :type: :class:`BoneCollection` | None

   .. data:: bones_recursive

      A set of all bones assigned to this bone collection and its child collections.

      (readonly)

   .. method:: bl_system_properties_get(*, do_create=False)

      DEBUG ONLY. Internal access to runtime-defined RNA data storage, intended solely for testing and debugging purposes. Do not access it in regular scripting work, and in particular, do not assume that it contains writable data

      :param do_create: Ensure that system properties are created if they do not exist yet (optional)
      :type do_create: bool
      :return: The system properties root container, or None if there are no system properties stored in this data yet, and its creation was not requested
      :rtype: :class:`PropertyGroup`

   .. method:: assign(bone)

      Assign the given bone to this collection

      :param bone: Bone, PoseBone, or EditBone to assign to this collection
      :type bone: :class:`AnyType` | None
      :return: Assigned, Whether the bone was actually assigned; will be false if the bone was already member of the collection
      :rtype: bool

   .. method:: unassign(bone)

      Remove the given bone from this collection

      :param bone: Bone, PoseBone, or EditBone to remove from this collection
      :type bone: :class:`AnyType` | None
      :return: Unassigned, Whether the bone was actually removed; will be false if the bone was not a member of the collection to begin with
      :rtype: bool

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
   - :class:`Armature.collections_all`
   - :class:`Bone.collections`
   - :class:`BoneCollection.children`
   - :class:`BoneCollection.parent`
   - :class:`BoneCollections.active`
   - :class:`BoneCollections.new`
   - :class:`BoneCollections.new`
   - :class:`BoneCollections.remove`
   - :class:`EditBone.collections`

