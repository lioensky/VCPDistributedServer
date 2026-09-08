ColorMapping(bpy_struct)
========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ColorMapping(bpy_struct)

   Color mapping settings

   .. attribute:: blend_color

      Blend color to mix with texture output color (array of 3 items, in [0, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. attribute:: blend_factor

      (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: blend_type

      Mode used to mix with texture output color (default ``'MIX'``)

      :type: Literal['MIX', 'DARKEN', 'MULTIPLY', 'LIGHTEN', 'SCREEN', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE']

   .. attribute:: brightness

      Adjust the brightness of the texture (in [0, 2], default 0.0)

      :type: float

   .. data:: color_ramp

      (readonly)

      :type: :class:`ColorRamp` | None

   .. attribute:: contrast

      Adjust the contrast of the texture (in [0, 5], default 0.0)

      :type: float

   .. attribute:: saturation

      Adjust the saturation of colors in the texture (in [0, 2], default 0.0)

      :type: float

   .. attribute:: use_color_ramp

      Toggle color ramp operations (default False)

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

   - :class:`ShaderNodeTexBrick.color_mapping`
   - :class:`ShaderNodeTexChecker.color_mapping`
   - :class:`ShaderNodeTexEnvironment.color_mapping`
   - :class:`ShaderNodeTexGabor.color_mapping`
   - :class:`ShaderNodeTexGradient.color_mapping`
   - :class:`ShaderNodeTexImage.color_mapping`
   - :class:`ShaderNodeTexMagic.color_mapping`
   - :class:`ShaderNodeTexNoise.color_mapping`
   - :class:`ShaderNodeTexSky.color_mapping`
   - :class:`ShaderNodeTexVoronoi.color_mapping`
   - :class:`ShaderNodeTexWave.color_mapping`

