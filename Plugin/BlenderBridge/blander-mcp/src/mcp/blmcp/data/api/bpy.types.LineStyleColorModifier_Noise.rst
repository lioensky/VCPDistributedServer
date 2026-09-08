LineStyleColorModifier_Noise(LineStyleColorModifier)
====================================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`LineStyleModifier`, :class:`LineStyleColorModifier`

.. class:: LineStyleColorModifier_Noise(LineStyleColorModifier)

   Change line color based on random noise

   .. attribute:: amplitude

      Amplitude of the noise (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: blend

      Specify how the modifier value is blended into the base value (default ``'MIX'``)

      :type: Literal[:ref:`rna_enum_ramp_blend_items`]

   .. data:: color_ramp

      Color ramp used to change line color (readonly)

      :type: :class:`ColorRamp` | None

   .. attribute:: expanded

      True if the modifier tab is expanded (default False)

      :type: bool

   .. attribute:: influence

      Influence factor by which the modifier changes the property (in [0, 1], default 0.0)

      :type: float

   .. attribute:: period

      Period of the noise (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: seed

      Seed for the noise generation (in [1, 32767], default 0)

      :type: int

   .. data:: type

      Type of the modifier (default ``'ALONG_STROKE'``, readonly)

      :type: Literal[:ref:`rna_enum_linestyle_color_modifier_type_items`]

   .. attribute:: use

      Enable or disable this modifier during stroke rendering (default False)

      :type: bool

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
   - :class:`LineStyleColorModifier.name`

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
   - :class:`LineStyleModifier.bl_rna_get_subclass`
   - :class:`LineStyleModifier.bl_rna_get_subclass_py`
   - :class:`LineStyleColorModifier.bl_rna_get_subclass`
   - :class:`LineStyleColorModifier.bl_rna_get_subclass_py`

