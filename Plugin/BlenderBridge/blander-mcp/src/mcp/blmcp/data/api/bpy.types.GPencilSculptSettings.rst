GPencilSculptSettings(bpy_struct)
=================================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: GPencilSculptSettings(bpy_struct)

   General properties for Grease Pencil stroke sculpting tools

   .. data:: guide

      (readonly)

      :type: :class:`GPencilSculptGuide` | None

   .. attribute:: intersection_threshold

      Threshold for stroke intersections (in [0, 10], default 0.1)

      :type: float

   .. attribute:: lock_axis

      (default ``'VIEW'``)

      - ``VIEW``
        View -- Align strokes to current view plane.
      - ``AXIS_Y``
        Front (X-Z) -- Project strokes to plane locked to Y.
      - ``AXIS_X``
        Side (Y-Z) -- Project strokes to plane locked to X.
      - ``AXIS_Z``
        Top (X-Y) -- Project strokes to plane locked to Z.
      - ``CURSOR``
        Cursor -- Align strokes to current 3D cursor orientation.

      :type: Literal['VIEW', 'AXIS_Y', 'AXIS_X', 'AXIS_Z', 'CURSOR']

   .. data:: multiframe_falloff_curve

      Custom curve to control falloff of brush effect by Grease Pencil frames (readonly)

      :type: :class:`CurveMapping` | None

   .. data:: thickness_primitive_curve

      Custom curve to control primitive thickness (readonly)

      :type: :class:`CurveMapping` | None

   .. attribute:: use_automasking_layer_active

      Affect only the Active Layer (default False)

      :type: bool

   .. attribute:: use_automasking_layer_stroke

      Affect only strokes below the cursor (default False)

      :type: bool

   .. attribute:: use_automasking_material_active

      Affect only the Active Material (default False)

      :type: bool

   .. attribute:: use_automasking_material_stroke

      Affect only strokes below the cursor (default False)

      :type: bool

   .. attribute:: use_automasking_stroke

      Affect only strokes below the cursor (default False)

      :type: bool

   .. attribute:: use_multiframe_falloff

      Use falloff effect when edit in multiframe mode to compute brush effect by frame (default False)

      :type: bool

   .. attribute:: use_scale_thickness

      Scale the stroke thickness when transforming strokes (default False)

      :type: bool

   .. attribute:: use_thickness_curve

      Use curve to define primitive stroke thickness (default False)

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

   - :class:`ToolSettings.gpencil_sculpt`

