ShapeKey(bpy_struct)
====================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ShapeKey(bpy_struct)

   Shape key in a shape keys data-block

   .. data:: data

      (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`UnknownType`]

   .. data:: frame

      Frame for absolute keys (in [-inf, inf], default 0.0, readonly)

      :type: float

   .. attribute:: interpolation

      Interpolation type for absolute shape keys (default ``'KEY_LINEAR'``)

      :type: Literal['KEY_LINEAR', 'KEY_CARDINAL', 'KEY_CATMULL_ROM', 'KEY_BSPLINE']

   .. attribute:: lock_shape

      Protect the shape key from accidental sculpting and editing (default False)

      :type: bool

   .. attribute:: mute

      Toggle this shape key (default False)

      :type: bool

   .. attribute:: name

      Name of Shape Key (default "", never None)

      :type: str

   .. data:: points

      Optimized access to shape keys point data, when using foreach_get/foreach_set accessors. Warning: Does not support legacy Curve shape keys. (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`ShapeKeyPoint`]

   .. attribute:: relative_key

      Shape used as a relative key (never None)

      :type: :class:`ShapeKey`

   .. attribute:: select

      Shape key selection state (default False)

      :type: bool

   .. attribute:: slider_max

      Maximum for slider (in [-10, 10], default 1.0)

      :type: float

   .. attribute:: slider_min

      Minimum for slider (in [-10, 10], default 0.0)

      :type: float

   .. attribute:: value

      Value of shape key at the current frame (in [0, 1], default 0.0)

      :type: float

   .. attribute:: vertex_group

      Vertex weight group, to blend with basis shape (default "", never None)

      :type: str

   .. method:: normals_vertex_get()

      Compute local space vertices' normals for this shape key

      :return: normals, (in [-1, 1])
      :rtype: float

   .. method:: normals_polygon_get()

      Compute local space faces' normals for this shape key

      :return: normals, (in [-1, 1])
      :rtype: float

   .. method:: normals_split_get()

      Compute local space face corners' normals for this shape key

      :return: normals, (in [-1, 1])
      :rtype: float

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

   - :class:`ClothSettings.rest_shape_key`
   - :class:`Key.key_blocks`
   - :class:`Key.reference_key`
   - :class:`Object.active_shape_key`
   - :class:`Object.shape_key_add`
   - :class:`Object.shape_key_remove`
   - :class:`Object.shape_keys_selected`
   - :class:`ShapeKey.relative_key`

