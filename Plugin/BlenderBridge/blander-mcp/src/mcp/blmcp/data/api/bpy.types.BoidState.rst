BoidState(bpy_struct)
=====================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: BoidState(bpy_struct)

   Boid state for boid physics

   .. data:: active_boid_rule

      (readonly)

      :type: :class:`BoidRule` | None

   .. attribute:: active_boid_rule_index

      (in [0, inf], default 0)

      :type: int

   .. attribute:: falloff

      (in [0, 10], default 0.0)

      :type: float

   .. attribute:: name

      Boid state name (default "", never None)

      :type: str

   .. attribute:: rule_fuzzy

      (in [0, 1], default 0.0)

      :type: float

   .. data:: rules

      (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`BoidRule`]

   .. attribute:: ruleset_type

      How the rules in the list are evaluated (default ``'FUZZY'``)

      - ``FUZZY``
        Fuzzy -- Rules are gone through top to bottom (only the first rule which effect is above fuzziness threshold is evaluated).
      - ``RANDOM``
        Random -- A random rule is selected for each boid.
      - ``AVERAGE``
        Average -- All rules are averaged.

      :type: Literal['FUZZY', 'RANDOM', 'AVERAGE']

   .. attribute:: volume

      (in [0, 100], default 0.0)

      :type: float

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

   - :class:`BoidSettings.states`

