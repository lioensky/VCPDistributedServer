PropertyGroup(bpy_struct)
=========================

.. currentmodule:: bpy.types


Custom Properties
+++++++++++++++++

PropertyGroups are the base class for dynamically defined sets of properties.

They can be used to extend existing Blender data with your own types which can
be animated, accessed from the user interface and from Python.

.. note::

   The values assigned to Blender data are saved to disk but the class
   definitions are not, this means whenever you load Blender the class needs
   to be registered too.

   This is best done by creating an add-on which loads on startup and registers
   your properties.

.. note::

   PropertyGroups must be registered before assigning them to Blender data.

.. seealso::

   Property types used in class declarations are all in :mod:`bpy.props`

.. literalinclude:: ./examples/bpy.types.PropertyGroup.0.py
   :lines: 27-

base class --- :class:`bpy_struct`

subclasses --- 
:class:`OperatorFileListElement`, :class:`OperatorMousePath`, :class:`OperatorStrokeElement`, :class:`SelectedUvElement`

.. class:: PropertyGroup(bpy_struct)

   Group of ID properties

   .. attribute:: name

      Unique name used in the code and scripting, can be re-defined in Python sub-classes if needed (default "", never None)

      :type: str

   .. method:: bl_system_properties_get(*, do_create=False)

      DEBUG ONLY. Internal access to runtime-defined RNA data storage, intended solely for testing and debugging purposes. Do not access it in regular scripting work, and in particular, do not assume that it contains writable data

      :param do_create: Ensure that system properties are created if they do not exist yet (optional)
      :type do_create: bool
      :return: The system properties root container, or None if there are no system properties stored in this data yet, and its creation was not requested
      :rtype: :class:`PropertyGroup`

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

   - :class:`AddonPreferences.bl_system_properties_get`
   - :class:`Bone.bl_system_properties_get`
   - :class:`BoneCollection.bl_system_properties_get`
   - :class:`CollectionExport.export_properties`
   - :class:`EditBone.bl_system_properties_get`
   - :class:`GizmoGroupProperties.bl_system_properties_get`
   - :class:`GizmoProperties.bl_system_properties_get`
   - :class:`ID.bl_system_properties_get`
   - :class:`IDPropertyWrapPtr.bl_system_properties_get`
   - :class:`KeyConfigPreferences.bl_system_properties_get`
   - :class:`Node.bl_system_properties_get`
   - :class:`NodeSocket.bl_system_properties_get`
   - :class:`NodeTreeInterfaceSocket.bl_system_properties_get`
   - :class:`NodesModifier.bl_system_properties_get`
   - :class:`OperatorProperties.bl_system_properties_get`
   - :class:`PoseBone.bl_system_properties_get`
   - :class:`PropertyGroup.bl_system_properties_get`
   - :class:`PropertyGroupItem.collection`
   - :class:`PropertyGroupItem.group`
   - :class:`PropertyGroupItem.idp_array`
   - :class:`Strip.bl_system_properties_get`
   - :class:`TimelineMarker.bl_system_properties_get`
   - :class:`UIList.bl_system_properties_get`
   - :class:`View3DShading.bl_system_properties_get`
   - :class:`ViewLayer.bl_system_properties_get`

