CurveMapping(bpy_struct)
========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: CurveMapping(bpy_struct)

   Curve mapping to map color, vector and scalar values to other values using a user defined curve

   .. attribute:: black_level

      For RGB curves, the color that black is mapped to (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. attribute:: clip_max_x

      (in [-100, 100], default 0.0)

      :type: float

   .. attribute:: clip_max_y

      (in [-100, 100], default 0.0)

      :type: float

   .. attribute:: clip_min_x

      (in [-100, 100], default 0.0)

      :type: float

   .. attribute:: clip_min_y

      (in [-100, 100], default 0.0)

      :type: float

   .. data:: curves

      (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`CurveMap`]

   .. attribute:: extend

      Extrapolate the curve or extend it horizontally (default ``'HORIZONTAL'``)

      :type: Literal['HORIZONTAL', 'EXTRAPOLATED']

   .. attribute:: tone

      Tone of the curve (default ``'STANDARD'``)

      - ``STANDARD``
        Standard -- Combined curve is applied to each channel individually, which may result in a change of hue.
      - ``FILMLIKE``
        Filmlike -- Keeps the hue constant.

      :type: Literal['STANDARD', 'FILMLIKE']

   .. attribute:: use_clip

      Force the curve view to fit a defined boundary (default False)

      :type: bool

   .. attribute:: white_level

      For RGB curves, the color that white is mapped to (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. method:: update()

      Update curve mapping after making changes


   .. method:: reset_view()

      Reset the curve mapping grid to its clipping size


   .. method:: initialize()

      Initialize curve


   .. method:: evaluate(curve, position)

      Evaluate curve at given location

      :param curve: curve, Curve to evaluate (never None)
      :type curve: :class:`CurveMap` | None
      :param position: Position, Position to evaluate curve at (in [-inf, inf])
      :type position: float
      :return: Value, Value of curve at given location (in [-inf, inf])
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

   - :class:`Brush.automasking_cavity_curve`
   - :class:`Brush.curve_distance_falloff`
   - :class:`Brush.curve_jitter`
   - :class:`Brush.curve_random_hue`
   - :class:`Brush.curve_random_saturation`
   - :class:`Brush.curve_random_value`
   - :class:`Brush.curve_size`
   - :class:`Brush.curve_strength`
   - :class:`BrushCurvesSculptSettings.curve_parameter_falloff`
   - :class:`BrushGpencilSettings.curve_jitter`
   - :class:`BrushGpencilSettings.curve_random_hue`
   - :class:`BrushGpencilSettings.curve_random_pressure`
   - :class:`BrushGpencilSettings.curve_random_saturation`
   - :class:`BrushGpencilSettings.curve_random_strength`
   - :class:`BrushGpencilSettings.curve_random_uv`
   - :class:`BrushGpencilSettings.curve_random_value`
   - :class:`BrushGpencilSettings.curve_sensitivity`
   - :class:`BrushGpencilSettings.curve_strength`
   - :class:`ColorManagedViewSettings.curve_mapping`
   - :class:`CompositorNodeCurveRGB.mapping`
   - :class:`CompositorNodeHueCorrect.mapping`
   - :class:`CompositorNodeTime.curve`
   - :class:`CurvesModifier.curve_mapping`
   - :class:`EQCurveMappingData.curve_mapping`
   - :class:`GPencilInterpolateSettings.interpolation_curve`
   - :class:`GPencilSculptSettings.multiframe_falloff_curve`
   - :class:`GPencilSculptSettings.thickness_primitive_curve`
   - :class:`GreasePencilColorModifier.custom_curve`
   - :class:`GreasePencilHookModifier.custom_curve`
   - :class:`GreasePencilNoiseModifier.custom_curve`
   - :class:`GreasePencilOpacityModifier.custom_curve`
   - :class:`GreasePencilSmoothModifier.custom_curve`
   - :class:`GreasePencilThickModifierData.custom_curve`
   - :class:`GreasePencilTintModifier.custom_curve`
   - :class:`HookModifier.falloff_curve`
   - :class:`HueCorrectModifier.curve_mapping`
   - :class:`LineStyleAlphaModifier_AlongStroke.curve`
   - :class:`LineStyleAlphaModifier_CreaseAngle.curve`
   - :class:`LineStyleAlphaModifier_Curvature_3D.curve`
   - :class:`LineStyleAlphaModifier_DistanceFromCamera.curve`
   - :class:`LineStyleAlphaModifier_DistanceFromObject.curve`
   - :class:`LineStyleAlphaModifier_Material.curve`
   - :class:`LineStyleAlphaModifier_Noise.curve`
   - :class:`LineStyleAlphaModifier_Tangent.curve`
   - :class:`LineStyleThicknessModifier_AlongStroke.curve`
   - :class:`LineStyleThicknessModifier_CreaseAngle.curve`
   - :class:`LineStyleThicknessModifier_Curvature_3D.curve`
   - :class:`LineStyleThicknessModifier_DistanceFromCamera.curve`
   - :class:`LineStyleThicknessModifier_DistanceFromObject.curve`
   - :class:`LineStyleThicknessModifier_Material.curve`
   - :class:`LineStyleThicknessModifier_Tangent.curve`
   - :class:`Paint.cavity_curve`
   - :class:`ParticleBrush.curve`
   - :class:`ParticleSettings.clump_curve`
   - :class:`ParticleSettings.roughness_curve`
   - :class:`ParticleSettings.twist_curve`
   - :class:`RenderSettings.motion_blur_shutter_curve`
   - :class:`Sculpt.automasking_cavity_curve`
   - :class:`Sculpt.automasking_cavity_curve_op`
   - :class:`ShaderNodeFloatCurve.mapping`
   - :class:`ShaderNodeRGBCurve.mapping`
   - :class:`ShaderNodeVectorCurve.mapping`
   - :class:`TextureNodeCurveRGB.mapping`
   - :class:`TextureNodeCurveTime.curve`
   - :class:`UvSculpt.curve_distance_falloff`
   - :class:`VertexWeightEditModifier.map_curve`
   - :class:`VertexWeightProximityModifier.map_curve`
   - :class:`WarpModifier.falloff_curve`

