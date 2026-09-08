StripColorBalanceData(bpy_struct)
=================================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

subclasses --- 
:class:`StripColorBalance`

.. class:: StripColorBalanceData(bpy_struct)

   Color balance parameters for a sequence strip and its modifiers

   .. attribute:: correction_method

      (default ``'LIFT_GAMMA_GAIN'``)

      - ``LIFT_GAMMA_GAIN``
        Lift/Gamma/Gain.
      - ``OFFSET_POWER_SLOPE``
        Offset/Power/Slope (ASC-CDL) -- ASC-CDL standard color correction.

      :type: Literal['LIFT_GAMMA_GAIN', 'OFFSET_POWER_SLOPE']

   .. attribute:: gain

      Color balance gain (highlights) (array of 3 items, in [0, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. attribute:: gamma

      Color balance gamma (midtones) (array of 3 items, in [0, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. attribute:: invert_gain

      Invert the gain color (default False)

      :type: bool

   .. attribute:: invert_gamma

      Invert the gamma color (default False)

      :type: bool

   .. attribute:: invert_lift

      Invert the lift color (default False)

      :type: bool

   .. attribute:: invert_offset

      Invert the offset color (default False)

      :type: bool

   .. attribute:: invert_power

      Invert the power color (default False)

      :type: bool

   .. attribute:: invert_slope

      Invert the slope color (default False)

      :type: bool

   .. attribute:: lift

      Color balance lift (shadows) (array of 3 items, in [0, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. attribute:: offset

      Correction for entire tonal range (array of 3 items, in [0, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. attribute:: power

      Correction for midtones (array of 3 items, in [0, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. attribute:: slope

      Correction for highlights (array of 3 items, in [0, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

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

   - :class:`ColorBalanceModifier.color_balance`

