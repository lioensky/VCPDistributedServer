LineStyleGeometryModifier_Blueprint(LineStyleGeometryModifier)
==============================================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`LineStyleModifier`, :class:`LineStyleGeometryModifier`

.. class:: LineStyleGeometryModifier_Blueprint(LineStyleGeometryModifier)

   Produce a blueprint using circular, elliptic, and square contour strokes

   .. attribute:: backbone_length

      Amount of backbone stretching (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: expanded

      True if the modifier tab is expanded (default False)

      :type: bool

   .. attribute:: random_backbone

      Randomness of the backbone stretching (in [0, inf], default 0)

      :type: int

   .. attribute:: random_center

      Randomness of the center (in [0, inf], default 0)

      :type: int

   .. attribute:: random_radius

      Randomness of the radius (in [0, inf], default 0)

      :type: int

   .. attribute:: rounds

      Number of rounds in contour strokes (in [1, 1000], default 0)

      :type: int

   .. attribute:: shape

      Select the shape of blueprint contour strokes (default ``'CIRCLES'``)

      - ``CIRCLES``
        Circles -- Draw a blueprint using circular contour strokes.
      - ``ELLIPSES``
        Ellipses -- Draw a blueprint using elliptic contour strokes.
      - ``SQUARES``
        Squares -- Draw a blueprint using square contour strokes.

      :type: Literal['CIRCLES', 'ELLIPSES', 'SQUARES']

   .. data:: type

      Type of the modifier (default ``'2D_OFFSET'``, readonly)

      :type: Literal[:ref:`rna_enum_linestyle_geometry_modifier_type_items`]

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
   - :class:`LineStyleGeometryModifier.name`

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
   - :class:`LineStyleGeometryModifier.bl_rna_get_subclass`
   - :class:`LineStyleGeometryModifier.bl_rna_get_subclass_py`

