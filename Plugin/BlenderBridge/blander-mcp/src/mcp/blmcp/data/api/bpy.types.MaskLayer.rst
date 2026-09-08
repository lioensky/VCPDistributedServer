MaskLayer(bpy_struct)
=====================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MaskLayer(bpy_struct)

   Single layer used for masking pixels

   .. attribute:: alpha

      Render Opacity (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: blend

      Method of blending mask layers (default ``'ADD'``)

      :type: Literal['MERGE_ADD', 'MERGE_SUBTRACT', 'ADD', 'SUBTRACT', 'LIGHTEN', 'DARKEN', 'MUL', 'REPLACE', 'DIFFERENCE']

   .. attribute:: falloff

      Falloff type of the feather (default ``'SMOOTH'``)

      :type: Literal[:ref:`rna_enum_proportional_falloff_curve_only_items`]

   .. attribute:: hide

      Restrict visibility in the viewport (default False)

      :type: bool

   .. attribute:: hide_render

      Restrict renderability (default False)

      :type: bool

   .. attribute:: hide_select

      Restrict selection in the viewport (default False)

      :type: bool

   .. attribute:: invert

      Invert the mask black/white (default False)

      :type: bool

   .. attribute:: name

      Unique name of layer (default "", never None)

      :type: str

   .. attribute:: select

      Layer is selected for editing in the Dope Sheet (default False)

      :type: bool

   .. data:: splines

      Collection of splines which defines this layer (default None, readonly)

      :type: :class:`MaskSplines`\ [:class:`MaskSpline`]

   .. attribute:: use_fill_holes

      Calculate holes when filling overlapping curves (default True)

      :type: bool

   .. attribute:: use_fill_overlap

      Calculate self intersections and overlap before filling (default False)

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

   - :class:`Mask.layers`
   - :class:`MaskLayers.active`
   - :class:`MaskLayers.new`
   - :class:`MaskLayers.remove`

