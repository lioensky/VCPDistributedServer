SubsurfModifier(Modifier)
=========================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: SubsurfModifier(Modifier)

   Subdivision surface modifier

   .. attribute:: adaptive_object_edge_length

      Target object space edge length for adaptive subdivision (in [0.0001, 1000], default 0.01)

      :type: float

   .. attribute:: adaptive_pixel_size

      Target polygon pixel size for adaptive subdivision (in [0.1, 1000], default 1.0)

      :type: float

   .. attribute:: adaptive_space

      How to adaptively subdivide the mesh (default ``'PIXEL'``)

      - ``PIXEL``
        Pixel -- Subdivide polygons to reach a specified pixel size on screen.
      - ``OBJECT``
        Object -- Subdivide to reach a specified edge length in object space. This is required to use adaptive subdivision for instanced meshes.

      :type: Literal['PIXEL', 'OBJECT']

   .. attribute:: boundary_smooth

      Controls how open boundaries are smoothed (default ``'ALL'``)

      :type: Literal[:ref:`rna_enum_subdivision_boundary_smooth_items`]

   .. attribute:: levels

      Number of subdivisions to perform in the 3D viewport (in [0, 11], default 1)

      :type: int

   .. attribute:: open_adaptive_subdivision_panel

      (default False)

      :type: bool

   .. attribute:: open_advanced_panel

      (default False)

      :type: bool

   .. attribute:: quality

      Accuracy of vertex positions, lower value is faster but less precise (in [1, 10], default 3)

      :type: int

   .. attribute:: render_levels

      Number of subdivisions to perform when rendering (in [0, 11], default 2)

      :type: int

   .. attribute:: show_only_control_edges

      Skip displaying interior subdivided edges (default True)

      :type: bool

   .. attribute:: subdivision_type

      Select type of subdivision algorithm (default ``'CATMULL_CLARK'``)

      - ``CATMULL_CLARK``
        Catmull-Clark -- Create a smooth curved surface using the Catmull-Clark subdivision scheme.
      - ``SIMPLE``
        Simple -- Subdivide faces without changing shape.

      :type: Literal['CATMULL_CLARK', 'SIMPLE']

   .. attribute:: use_adaptive_subdivision

      Adaptively subdivide mesh based on camera distance (default False)

      :type: bool

   .. attribute:: use_creases

      Use mesh crease information to sharpen edges or corners (default True)

      :type: bool

   .. attribute:: use_custom_normals

      Interpolates existing custom normals to resulting mesh (default False)

      :type: bool

   .. attribute:: use_limit_surface

      Place vertices at the surface that would be produced with infinite levels of subdivision (smoothest possible shape) (default True)

      :type: bool

   .. attribute:: uv_smooth

      Controls how smoothing is applied to UVs (default ``'PRESERVE_BOUNDARIES'``)

      :type: Literal[:ref:`rna_enum_subdivision_uv_smooth_items`]

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

