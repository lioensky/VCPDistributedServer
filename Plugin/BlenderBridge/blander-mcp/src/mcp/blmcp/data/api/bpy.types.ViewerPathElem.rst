ViewerPathElem(bpy_struct)
==========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

subclasses --- 
:class:`EvaluateClosureNodeViewerPathElem`, :class:`ForeachGeometryElementZoneViewerPathElem`, :class:`GroupNodeViewerPathElem`, :class:`IDViewerPathElem`, :class:`ModifierViewerPathElem`, :class:`RepeatZoneViewerPathElem`, :class:`SimulationZoneViewerPathElem`, :class:`ViewerNodeViewerPathElem`

.. class:: ViewerPathElem(bpy_struct)

   Element of a viewer path

   .. data:: type

      Type of the path element (default ``'ID'``, readonly)

      :type: Literal['ID', 'MODIFIER', 'GROUP_NODE', 'SIMULATION_ZONE', 'VIEWER_NODE', 'REPEAT_ZONE', 'FOREACH_GEOMETRY_ELEMENT_ZONE', 'EVALUATE_CLOSURE']

   .. data:: ui_name

      Name that can be displayed in the UI for this element (default "", readonly, never None)

      :type: str

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

   - :class:`ViewerPath.path`

