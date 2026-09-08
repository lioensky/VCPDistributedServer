SolidifyModifier(Modifier)
==========================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: SolidifyModifier(Modifier)

   Create a solid skin, compensating for sharp angles

   .. attribute:: bevel_convex

      Edge bevel weight to be added to outside edges (in [-1, 1], default 0.0)

      :type: float

   .. attribute:: edge_crease_inner

      Assign a crease to inner edges (in [0, 1], default 0.0)

      :type: float

   .. attribute:: edge_crease_outer

      Assign a crease to outer edges (in [0, 1], default 0.0)

      :type: float

   .. attribute:: edge_crease_rim

      Assign a crease to the edges making up the rim (in [0, 1], default 0.0)

      :type: float

   .. attribute:: invert_vertex_group

      Invert the vertex group influence (default False)

      :type: bool

   .. attribute:: material_offset

      Offset material index of generated faces (in [-32768, 32767], default 0)

      :type: int

   .. attribute:: material_offset_rim

      Offset material index of generated rim faces (in [-32768, 32767], default 0)

      :type: int

   .. attribute:: nonmanifold_boundary_mode

      Selects the boundary adjustment algorithm (default ``'NONE'``)

      - ``NONE``
        None -- No shape correction.
      - ``ROUND``
        Round -- Round open perimeter shape.
      - ``FLAT``
        Flat -- Flat open perimeter shape.

      :type: Literal['NONE', 'ROUND', 'FLAT']

   .. attribute:: nonmanifold_merge_threshold

      Distance within which degenerated geometry is merged (in [0, 1], default 0.0001)

      :type: float

   .. attribute:: nonmanifold_thickness_mode

      Selects the used thickness algorithm (default ``'CONSTRAINTS'``)

      - ``FIXED``
        Fixed -- Most basic thickness calculation.
      - ``EVEN``
        Even -- Even thickness calculation which takes the angle between faces into account.
      - ``CONSTRAINTS``
        Constraints -- Thickness calculation using constraints, most advanced.

      :type: Literal['FIXED', 'EVEN', 'CONSTRAINTS']

   .. attribute:: offset

      Offset the thickness from the center (in [-inf, inf], default -1.0)

      :type: float

   .. attribute:: rim_vertex_group

      Vertex group that the generated rim geometry will be weighted to (default "", never None)

      :type: str

   .. attribute:: shell_vertex_group

      Vertex group that the generated shell geometry will be weighted to (default "", never None)

      :type: str

   .. attribute:: solidify_mode

      Selects the used algorithm (default ``'EXTRUDE'``)

      - ``EXTRUDE``
        Simple -- Output a solidified version of a mesh by simple extrusion.
      - ``NON_MANIFOLD``
        Complex -- Output a manifold mesh even if the base mesh is non-manifold, where edges have 3 or more connecting faces. This method is slower..

      :type: Literal['EXTRUDE', 'NON_MANIFOLD']

   .. attribute:: thickness

      Thickness of the shell (in [-inf, inf], default 0.01)

      :type: float

   .. attribute:: thickness_clamp

      Offset clamp based on geometry scale (in [0, 100], default 0.0)

      :type: float

   .. attribute:: thickness_vertex_group

      Thickness factor to use for zero vertex group influence (in [0, 1], default 0.0)

      :type: float

   .. attribute:: use_even_offset

      Maintain thickness by adjusting for sharp corners (slow, disable when not needed) (default False)

      :type: bool

   .. attribute:: use_flat_faces

      Make faces use the minimal vertex weight assigned to their vertices (ensures new faces remain parallel to their original ones, slow, disable when not needed) (default False)

      :type: bool

   .. attribute:: use_flip_normals

      Invert the face direction (default False)

      :type: bool

   .. attribute:: use_quality_normals

      Calculate normals which result in more even thickness (slow, disable when not needed) (default False)

      :type: bool

   .. attribute:: use_rim

      Create edge loops between the inner and outer surfaces on face edges (slow, disable when not needed) (default True)

      :type: bool

   .. attribute:: use_rim_only

      Only add the rim to the original data (default False)

      :type: bool

   .. attribute:: use_thickness_angle_clamp

      Clamp thickness based on angles (default False)

      :type: bool

   .. attribute:: vertex_group

      Vertex group name (default "", never None)

      :type: str

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
   - :class:`Modifier.name`
   - :class:`Modifier.type`
   - :class:`Modifier.show_viewport`
   - :class:`Modifier.show_render`
   - :class:`Modifier.show_in_editmode`
   - :class:`Modifier.show_on_cage`
   - :class:`Modifier.show_expanded`
   - :class:`Modifier.is_active`
   - :class:`Modifier.use_pin_to_last`
   - :class:`Modifier.is_override_data`
   - :class:`Modifier.use_apply_on_spline`
   - :class:`Modifier.execution_time`
   - :class:`Modifier.persistent_uid`

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
   - :class:`Modifier.bl_rna_get_subclass`
   - :class:`Modifier.bl_rna_get_subclass_py`

