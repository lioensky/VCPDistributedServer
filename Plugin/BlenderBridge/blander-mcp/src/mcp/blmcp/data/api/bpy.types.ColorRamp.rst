ColorRamp(bpy_struct)
=====================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ColorRamp(bpy_struct)

   Color ramp mapping a scalar value to a color

   .. attribute:: color_mode

      Set color mode to use for interpolation (default ``'RGB'``)

      :type: Literal['RGB', 'HSV', 'HSL']

   .. data:: elements

      (default None, readonly)

      :type: :class:`ColorRampElements`\ [:class:`ColorRampElement`]

   .. attribute:: hue_interpolation

      Set color interpolation (default ``'NEAR'``)

      :type: Literal['NEAR', 'FAR', 'CW', 'CCW']

   .. attribute:: interpolation

      Set interpolation between color stops (default ``'LINEAR'``)

      :type: Literal['EASE', 'CARDINAL', 'LINEAR', 'B_SPLINE', 'CONSTANT']

   .. method:: evaluate(position)

      Evaluate Color Ramp

      :param position: Position, Evaluate Color Ramp at position (in [0, 1])
      :type position: float
      :return: Color, Color at given position (array of 4 items, in [-inf, inf])
      :rtype: :class:`bpy_prop_array`\ [float]

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

   - :class:`Brush.gradient`
   - :class:`ColorMapping.color_ramp`
   - :class:`DynamicPaintBrushSettings.paint_ramp`
   - :class:`DynamicPaintBrushSettings.velocity_ramp`
   - :class:`FluidDomainSettings.color_ramp`
   - :class:`GreasePencilTintModifier.color_ramp`
   - :class:`LineStyleColorModifier_AlongStroke.color_ramp`
   - :class:`LineStyleColorModifier_CreaseAngle.color_ramp`
   - :class:`LineStyleColorModifier_Curvature_3D.color_ramp`
   - :class:`LineStyleColorModifier_DistanceFromCamera.color_ramp`
   - :class:`LineStyleColorModifier_DistanceFromObject.color_ramp`
   - :class:`LineStyleColorModifier_Material.color_ramp`
   - :class:`LineStyleColorModifier_Noise.color_ramp`
   - :class:`LineStyleColorModifier_Tangent.color_ramp`
   - :class:`PreferencesView.weight_color_range`
   - :class:`ShaderNodeValToRGB.color_ramp`
   - :class:`Texture.color_ramp`
   - :class:`TextureNodeValToRGB.color_ramp`

