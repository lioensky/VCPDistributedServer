LayerCollection(bpy_struct)
===========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: LayerCollection(bpy_struct)

   Layer collection

   .. data:: children

      Layer collection children (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`LayerCollection`]

   .. data:: collection

      Collection this layer collection is wrapping (readonly, never None)

      :type: :class:`Collection`

   .. attribute:: exclude

      Exclude from view layer (default False)

      :type: bool

   .. attribute:: hide_viewport

      Temporarily hide in viewport (default False)

      :type: bool

   .. attribute:: holdout

      Mask out objects in collection from view layer (default False)

      :type: bool

   .. attribute:: indirect_only

      Objects in collection only contribute indirectly (through shadows and reflections) in the view layer (default False)

      :type: bool

   .. data:: is_visible

      Whether this collection is visible for the view layer, take into account the collection parent (default False, readonly)

      :type: bool

   .. data:: name

      Name of this layer collection (same as its collection one) (default "", readonly, never None)

      :type: str

   .. method:: visible_get()

      Whether this collection is visible, take into account the collection parent and the viewport

      :rtype: bool

   .. method:: has_objects()

      

      :rtype: bool

   .. method:: has_selected_objects(view_layer)

      

      :param view_layer: View layer the layer collection belongs to
      :type view_layer: :class:`ViewLayer` | None
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

   - :mod:`bpy.context.collection`
   - :class:`Context.layer_collection`
   - :class:`LayerCollection.children`
   - :class:`ViewLayer.active_layer_collection`
   - :class:`ViewLayer.layer_collection`

