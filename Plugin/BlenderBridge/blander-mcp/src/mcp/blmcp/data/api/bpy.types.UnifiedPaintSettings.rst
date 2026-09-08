UnifiedPaintSettings(bpy_struct)
================================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: UnifiedPaintSettings(bpy_struct)

   Overrides for some of the active brush's settings

   .. attribute:: color

      (array of 3 items, in [0, 1], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. attribute:: hue_jitter

      Color jitter effect on hue (in [0, 1], default 0.0)

      :type: float

   .. attribute:: input_samples

      Number of input samples to average together to smooth the brush stroke (in [1, 64], default 1)

      :type: int

   .. attribute:: saturation_jitter

      Color jitter effect on saturation (in [0, 1], default 0.0)

      :type: float

   .. attribute:: secondary_color

      (array of 3 items, in [0, 1], default (1.0, 1.0, 1.0))

      :type: :class:`mathutils.Color`

   .. attribute:: size

      Diameter of the brush (in [1, 10000], default 100)

      :type: int

   .. attribute:: strength

      How powerful the effect of the brush is when applied (in [0, 10], default 0.5)

      :type: float

   .. attribute:: unprojected_size

      Diameter of brush in Blender units (in [0.001, inf], default 0.58)

      :type: float

   .. attribute:: use_color_jitter

      Jitter brush color (default False)

      :type: bool

   .. attribute:: use_locked_size

      Measure brush size relative to the view or the scene (default ``'VIEW'``)

      - ``VIEW``
        View -- Measure brush size relative to the view.
      - ``SCENE``
        Scene -- Measure brush size relative to the scene.

      :type: Literal['VIEW', 'SCENE']

   .. attribute:: use_random_press_hue

      Use pressure to modulate randomness (default False)

      :type: bool

   .. attribute:: use_random_press_sat

      Use pressure to modulate randomness (default False)

      :type: bool

   .. attribute:: use_random_press_val

      Use pressure to modulate randomness (default False)

      :type: bool

   .. attribute:: use_stroke_random_hue

      Use randomness at stroke level (default False)

      :type: bool

   .. attribute:: use_stroke_random_sat

      Use randomness at stroke level (default False)

      :type: bool

   .. attribute:: use_stroke_random_val

      Use randomness at stroke level (default False)

      :type: bool

   .. attribute:: use_unified_color

      Instead of per-brush color, the color is shared across brushes (default True)

      :type: bool

   .. attribute:: use_unified_input_samples

      Instead of per-brush input samples, the value is shared across brushes (default False)

      :type: bool

   .. attribute:: use_unified_size

      Instead of per-brush size, the size is shared across brushes (default True)

      :type: bool

   .. attribute:: use_unified_strength

      Instead of per-brush strength, the strength is shared across brushes (default False)

      :type: bool

   .. attribute:: use_unified_weight

      Instead of per-brush weight, the weight is shared across brushes (default False)

      :type: bool

   .. attribute:: value_jitter

      Color jitter effect on value (in [0, 1], default 0.0)

      :type: float

   .. attribute:: weight

      Weight to assign in vertex groups (in [0, 1], default 0.5)

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

   - :class:`Paint.unified_paint_settings`

