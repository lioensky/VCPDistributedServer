NormalEditModifier(Modifier)
============================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: NormalEditModifier(Modifier)

   Modifier affecting/generating custom normals

   .. attribute:: invert_vertex_group

      Invert vertex group influence (default False)

      :type: bool

   .. attribute:: mix_factor

      How much of generated normals to mix with existing ones (in [0, 1], default 1.0)

      :type: float

   .. attribute:: mix_limit

      Maximum angle between old and new normals (in [0, 3.14159], default 3.14159)

      :type: float

   .. attribute:: mix_mode

      How to mix generated normals with existing ones (default ``'COPY'``)

      - ``COPY``
        Copy -- Copy new normals (overwrite existing).
      - ``ADD``
        Add -- Copy sum of new and old normals.
      - ``SUB``
        Subtract -- Copy new normals minus old normals.
      - ``MUL``
        Multiply -- Copy product of old and new normals (not cross product).

      :type: Literal['COPY', 'ADD', 'SUB', 'MUL']

   .. attribute:: mode

      How to affect (generate) normals (default ``'RADIAL'``)

      - ``RADIAL``
        Radial -- From an ellipsoid (shape defined by the boundbox's dimensions, target is optional).
      - ``DIRECTIONAL``
        Directional -- Normals 'track' (point to) the target object.

      :type: Literal['RADIAL', 'DIRECTIONAL']

   .. attribute:: no_polynors_fix

      Do not flip polygons when their normals are not consistent with their newly computed custom vertex normals (default False)

      :type: bool

   .. attribute:: offset

      Offset from object's center (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: target

      Target object used to affect normals

      :type: :class:`Object` | None

   .. attribute:: use_direction_parallel

      Use same direction for all normals, from origin to target's center (Directional mode only) (default True)

      :type: bool

   .. attribute:: vertex_group

      Vertex group name for selecting/weighting the affected areas (default "", never None)

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
   - :class:`Modifier.name`
   - :class:`Modifier.type`
   - :class:`Modifier.show_viewport`
   - :class:`Modifier.show_render`
   - :class:`Modifier.show_in_editmode`
   - :class:`Modifier.show_on_cage`
   - :class:`Modifier.show_expanded`
   - :class:`Modifier.is_active`
   - :class:`Modifier.use_pin_to_last`
   - :class:`Modifier.is_override_data`
   - :class:`Modifier.use_apply_on_spline`
   - :class:`Modifier.execution_time`
   - :class:`Modifier.persistent_uid`

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
   - :class:`Modifier.bl_rna_get_subclass`
   - :class:`Modifier.bl_rna_get_subclass_py`

