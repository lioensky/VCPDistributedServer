BevelModifier(Modifier)
=======================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: BevelModifier(Modifier)

   Bevel modifier to make edges and vertices more rounded

   .. attribute:: affect

      Affect edges or vertices (default ``'EDGES'``)

      - ``VERTICES``
        Vertices -- Affect only vertices.
      - ``EDGES``
        Edges -- Affect only edges.

      :type: Literal['VERTICES', 'EDGES']

   .. attribute:: angle_limit

      Angle above which to bevel edges (in [0, 3.14159], default 0.523599)

      :type: float

   .. data:: custom_profile

      The path for the custom profile (readonly)

      :type: :class:`CurveProfile` | None

   .. attribute:: edge_weight

      Attribute name for edge weight (default "", never None)

      :type: str

   .. attribute:: face_strength_mode

      Whether to set face strength, and which faces to set it on (default ``'FSTR_NONE'``)

      - ``FSTR_NONE``
        None -- Do not set face strength.
      - ``FSTR_NEW``
        New -- Set face strength on new faces only.
      - ``FSTR_AFFECTED``
        Affected -- Set face strength on new and affected faces only.
      - ``FSTR_ALL``
        All -- Set face strength on all faces.

      :type: Literal['FSTR_NONE', 'FSTR_NEW', 'FSTR_AFFECTED', 'FSTR_ALL']

   .. attribute:: harden_normals

      Match normals of new faces to adjacent faces (default False)

      :type: bool

   .. attribute:: invert_vertex_group

      Invert vertex group influence (default False)

      :type: bool

   .. attribute:: limit_method

      (default ``'ANGLE'``)

      - ``NONE``
        None -- Bevel the entire mesh by a constant amount.
      - ``ANGLE``
        Angle -- Only bevel edges with sharp enough angles between faces.
      - ``WEIGHT``
        Weight -- Use bevel weights to determine how much bevel is applied in edge mode.
      - ``VGROUP``
        Vertex Group -- Use vertex group weights to select whether vertex or edge is beveled.

      :type: Literal['NONE', 'ANGLE', 'WEIGHT', 'VGROUP']

   .. attribute:: loop_slide

      Prefer sliding along edges to having even widths (default True)

      :type: bool

   .. attribute:: mark_seam

      Mark Seams along beveled edges (default False)

      :type: bool

   .. attribute:: mark_sharp

      Mark beveled edges as sharp (default False)

      :type: bool

   .. attribute:: material

      Material index of generated faces, -1 for automatic (in [-1, 32767], default -1)

      :type: int

   .. attribute:: miter_inner

      Pattern to use for inside of miters (default ``'MITER_SHARP'``)

      - ``MITER_SHARP``
        Sharp -- Inside of miter is sharp.
      - ``MITER_ARC``
        Arc -- Inside of miter is arc.

      :type: Literal['MITER_SHARP', 'MITER_ARC']

   .. attribute:: miter_outer

      Pattern to use for outside of miters (default ``'MITER_SHARP'``)

      - ``MITER_SHARP``
        Sharp -- Outside of miter is sharp.
      - ``MITER_PATCH``
        Patch -- Outside of miter is squared-off patch.
      - ``MITER_ARC``
        Arc -- Outside of miter is arc.

      :type: Literal['MITER_SHARP', 'MITER_PATCH', 'MITER_ARC']

   .. attribute:: offset_type

      What distance Width measures (default ``'OFFSET'``)

      - ``OFFSET``
        Offset -- Amount is offset of new edges from original.
      - ``WIDTH``
        Width -- Amount is width of new face.
      - ``DEPTH``
        Depth -- Amount is perpendicular distance from original edge to bevel face.
      - ``PERCENT``
        Percent -- Amount is percent of adjacent edge length.
      - ``ABSOLUTE``
        Absolute -- Amount is absolute distance along adjacent edge.

      :type: Literal['OFFSET', 'WIDTH', 'DEPTH', 'PERCENT', 'ABSOLUTE']

   .. attribute:: profile

      The profile shape (0.5 = round) (in [0, 1], default 0.5)

      :type: float

   .. attribute:: profile_type

      The type of shape used to rebuild a beveled section (default ``'SUPERELLIPSE'``)

      - ``SUPERELLIPSE``
        Superellipse -- The profile can be a concave or convex curve.
      - ``CUSTOM``
        Custom -- The profile can be any arbitrary path between its endpoints.

      :type: Literal['SUPERELLIPSE', 'CUSTOM']

   .. attribute:: segments

      Number of segments for round edges/verts (in [1, 1000], default 1)

      :type: int

   .. attribute:: spread

      Spread distance for inner miter arcs (in [0, inf], default 0.1)

      :type: float

   .. attribute:: use_clamp_overlap

      Clamp the width to avoid overlap (default True)

      :type: bool

   .. attribute:: vertex_group

      Vertex group name (default "", never None)

      :type: str

   .. attribute:: vertex_weight

      Attribute name for vertex weight (default "", never None)

      :type: str

   .. attribute:: vmesh_method

      The method to use to create the mesh at intersections (default ``'ADJ'``)

      - ``ADJ``
        Grid Fill -- Default patterned fill.
      - ``CUTOFF``
        Cutoff -- A cut-off at the end of each profile before the intersection.

      :type: Literal['ADJ', 'CUTOFF']

   .. attribute:: width

      Bevel amount (in [0, inf], default 0.1)

      :type: float

   .. attribute:: width_pct

      Bevel amount for percentage method (in [0, inf], default 0.1)

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

