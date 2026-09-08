FreestyleLineStyle(ID)
======================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: FreestyleLineStyle(ID)

   Freestyle line style, reusable by multiple line sets

   .. attribute:: active_texture

      Active texture slot being displayed

      :type: :class:`Texture` | None

   .. attribute:: active_texture_index

      Index of active texture slot (in [0, 17], default 0)

      :type: int

   .. attribute:: alpha

      Base alpha transparency, possibly modified by alpha transparency modifiers (in [0, 1], default 1.0)

      :type: float

   .. data:: alpha_modifiers

      List of alpha transparency modifiers (default None, readonly)

      :type: :class:`LineStyleAlphaModifiers`\ [:class:`LineStyleAlphaModifier`]

   .. attribute:: angle_max

      Maximum 2D angle for splitting chains (in [0, 3.14159], default 0.0)

      :type: float

   .. attribute:: angle_min

      Minimum 2D angle for splitting chains (in [0, 3.14159], default 0.0)

      :type: float

   .. data:: animation_data

      Animation data for this data-block (readonly)

      :type: :class:`AnimData` | None

   .. attribute:: caps

      Select the shape of both ends of strokes (default ``'BUTT'``)

      - ``BUTT``
        Butt -- Butt cap (flat).
      - ``ROUND``
        Round -- Round cap (half-circle).
      - ``SQUARE``
        Square -- Square cap (flat and extended).

      :type: Literal['BUTT', 'ROUND', 'SQUARE']

   .. attribute:: chain_count

      Chain count for the selection of first N chains (in [0, inf], default 10)

      :type: int

   .. attribute:: chaining

      Select the way how feature edges are jointed to form chains (default ``'PLAIN'``)

      - ``PLAIN``
        Plain -- Plain chaining.
      - ``SKETCHY``
        Sketchy -- Sketchy chaining with a multiple touch.

      :type: Literal['PLAIN', 'SKETCHY']

   .. attribute:: color

      Base line color, possibly modified by line color modifiers (array of 3 items, in [0, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. data:: color_modifiers

      List of line color modifiers (default None, readonly)

      :type: :class:`LineStyleColorModifiers`\ [:class:`LineStyleColorModifier`]

   .. attribute:: dash1

      Length of the 1st dash for dashed lines (in [0, 65535], default 0)

      :type: int

   .. attribute:: dash2

      Length of the 2nd dash for dashed lines (in [0, 65535], default 0)

      :type: int

   .. attribute:: dash3

      Length of the 3rd dash for dashed lines (in [0, 65535], default 0)

      :type: int

   .. attribute:: gap1

      Length of the 1st gap for dashed lines (in [0, 65535], default 0)

      :type: int

   .. attribute:: gap2

      Length of the 2nd gap for dashed lines (in [0, 65535], default 0)

      :type: int

   .. attribute:: gap3

      Length of the 3rd gap for dashed lines (in [0, 65535], default 0)

      :type: int

   .. data:: geometry_modifiers

      List of stroke geometry modifiers (default None, readonly)

      :type: :class:`LineStyleGeometryModifiers`\ [:class:`LineStyleGeometryModifier`]

   .. attribute:: integration_type

      Select the way how the sort key is computed for each chain (default ``'MEAN'``)

      - ``MEAN``
        Mean -- The value computed for the chain is the mean of the values obtained for chain vertices.
      - ``MIN``
        Min -- The value computed for the chain is the minimum of the values obtained for chain vertices.
      - ``MAX``
        Max -- The value computed for the chain is the maximum of the values obtained for chain vertices.
      - ``FIRST``
        First -- The value computed for the chain is the value obtained for the first chain vertex.
      - ``LAST``
        Last -- The value computed for the chain is the value obtained for the last chain vertex.

      :type: Literal['MEAN', 'MIN', 'MAX', 'FIRST', 'LAST']

   .. attribute:: length_max

      Maximum curvilinear 2D length for the selection of chains (in [0, 10000], default 10000.0)

      :type: float

   .. attribute:: length_min

      Minimum curvilinear 2D length for the selection of chains (in [0, 10000], default 0.0)

      :type: float

   .. attribute:: material_boundary

      If true, chains of feature edges are split at material boundaries (default False)

      :type: bool

   .. data:: node_tree

      Node tree for node-based shaders (readonly)

      :type: :class:`NodeTree` | None

   .. attribute:: panel

      Select the property panel to be shown (default ``'STROKES'``)

      - ``STROKES``
        Strokes -- Show the panel for stroke construction.
      - ``COLOR``
        Color -- Show the panel for line color options.
      - ``ALPHA``
        Alpha -- Show the panel for alpha transparency options.
      - ``THICKNESS``
        Thickness -- Show the panel for line thickness options.
      - ``GEOMETRY``
        Geometry -- Show the panel for stroke geometry options.
      - ``TEXTURE``
        Texture -- Show the panel for stroke texture options.

      :type: Literal['STROKES', 'COLOR', 'ALPHA', 'THICKNESS', 'GEOMETRY', 'TEXTURE']

   .. attribute:: rounds

      Number of rounds in a sketchy multiple touch (in [1, 1000], default 3)

      :type: int

   .. attribute:: sort_key

      Select the sort key to determine the stacking order of chains (default ``'DISTANCE_FROM_CAMERA'``)

      - ``DISTANCE_FROM_CAMERA``
        Distance from Camera -- Sort by distance from camera (closer lines lie on top of further lines).
      - ``2D_LENGTH``
        2D Length -- Sort by curvilinear 2D length (longer lines lie on top of shorter lines).
      - ``PROJECTED_X``
        Projected X -- Sort by the projected X value in the image coordinate system.
      - ``PROJECTED_Y``
        Projected Y -- Sort by the projected Y value in the image coordinate system.

      :type: Literal['DISTANCE_FROM_CAMERA', '2D_LENGTH', 'PROJECTED_X', 'PROJECTED_Y']

   .. attribute:: sort_order

      Select the sort order (default ``'DEFAULT'``)

      - ``DEFAULT``
        Default -- Default order of the sort key.
      - ``REVERSE``
        Reverse -- Reverse order.

      :type: Literal['DEFAULT', 'REVERSE']

   .. attribute:: split_dash1

      Length of the 1st dash for splitting (in [0, 65535], default 0)

      :type: int

   .. attribute:: split_dash2

      Length of the 2nd dash for splitting (in [0, 65535], default 0)

      :type: int

   .. attribute:: split_dash3

      Length of the 3rd dash for splitting (in [0, 65535], default 0)

      :type: int

   .. attribute:: split_gap1

      Length of the 1st gap for splitting (in [0, 65535], default 0)

      :type: int

   .. attribute:: split_gap2

      Length of the 2nd gap for splitting (in [0, 65535], default 0)

      :type: int

   .. attribute:: split_gap3

      Length of the 3rd gap for splitting (in [0, 65535], default 0)

      :type: int

   .. attribute:: split_length

      Curvilinear 2D length for chain splitting (in [0, 10000], default 100.0)

      :type: float

   .. data:: texture_slots

      Texture slots defining the mapping and influence of textures (default None, readonly)

      :type: :class:`LineStyleTextureSlots`\ [:class:`LineStyleTextureSlot`]

   .. attribute:: texture_spacing

      Spacing for textures along stroke length (in [0.01, 100], default 1.0)

      :type: float

   .. attribute:: thickness

      Base line thickness, possibly modified by line thickness modifiers (in [0, 10000], default 3.0)

      :type: float

   .. data:: thickness_modifiers

      List of line thickness modifiers (default None, readonly)

      :type: :class:`LineStyleThicknessModifiers`\ [:class:`LineStyleThicknessModifier`]

   .. attribute:: thickness_position

      Thickness position of silhouettes and border edges (applicable when plain chaining is used with the Same Object option) (default ``'CENTER'``)

      - ``CENTER``
        Center -- Silhouettes and border edges are centered along stroke geometry.
      - ``INSIDE``
        Inside -- Silhouettes and border edges are drawn inside of stroke geometry.
      - ``OUTSIDE``
        Outside -- Silhouettes and border edges are drawn outside of stroke geometry.
      - ``RELATIVE``
        Relative -- Silhouettes and border edges are shifted by a user-defined ratio.

      :type: Literal['CENTER', 'INSIDE', 'OUTSIDE', 'RELATIVE']

   .. attribute:: thickness_ratio

      A number between 0 (inside) and 1 (outside) specifying the relative position of stroke thickness (in [0, 1], default 0.5)

      :type: float

   .. attribute:: use_angle_max

      Split chains at points with angles larger than the maximum 2D angle (default False)

      :type: bool

   .. attribute:: use_angle_min

      Split chains at points with angles smaller than the minimum 2D angle (default False)

      :type: bool

   .. attribute:: use_chain_count

      Enable the selection of first N chains (default False)

      :type: bool

   .. attribute:: use_chaining

      Enable chaining of feature edges (default True)

      :type: bool

   .. attribute:: use_dashed_line

      Enable or disable dashed line (default False)

      :type: bool

   .. attribute:: use_length_max

      Enable the selection of chains by a maximum 2D length (default False)

      :type: bool

   .. attribute:: use_length_min

      Enable the selection of chains by a minimum 2D length (default False)

      :type: bool

   .. attribute:: use_nodes

      Use shader nodes for the line style (default False)

      :type: bool

   .. attribute:: use_same_object

      If true, only feature edges of the same object are joined (default True)

      :type: bool

   .. attribute:: use_sorting

      Arrange the stacking order of strokes (default False)

      :type: bool

   .. attribute:: use_split_length

      Enable chain splitting by curvilinear 2D length (default False)

      :type: bool

   .. attribute:: use_split_pattern

      Enable chain splitting by dashed line patterns (default False)

      :type: bool

   .. attribute:: use_texture

      Enable or disable textured strokes (default True)

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
   - :class:`ID.name`
   - :class:`ID.name_full`
   - :class:`ID.id_type`
   - :class:`ID.session_uid`
   - :class:`ID.is_evaluated`
   - :class:`ID.original`
   - :class:`ID.users`
   - :class:`ID.use_fake_user`
   - :class:`ID.use_extra_user`
   - :class:`ID.is_embedded_data`
   - :class:`ID.is_linked_packed`
   - :class:`ID.is_missing`
   - :class:`ID.is_runtime_data`
   - :class:`ID.is_editable`
   - :class:`ID.tag`
   - :class:`ID.is_library_indirect`
   - :class:`ID.library`
   - :class:`ID.library_weak_reference`
   - :class:`ID.asset_data`
   - :class:`ID.override_library`
   - :class:`ID.preview`

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
   - :class:`ID.bl_system_properties_get`
   - :class:`ID.rename`
   - :class:`ID.evaluated_get`
   - :class:`ID.copy`
   - :class:`ID.asset_mark`
   - :class:`ID.asset_clear`
   - :class:`ID.asset_generate_preview`
   - :class:`ID.override_create`
   - :class:`ID.override_hierarchy_create`
   - :class:`ID.user_clear`
   - :class:`ID.user_remap`
   - :class:`ID.make_local`
   - :class:`ID.user_of_id`
   - :class:`ID.animation_data_create`
   - :class:`ID.animation_data_clear`
   - :class:`ID.update_tag`
   - :class:`ID.preview_ensure`
   - :class:`ID.bl_rna_get_subclass`
   - :class:`ID.bl_rna_get_subclass_py`

References
----------

.. hlist::
   :columns: 2

   - :mod:`bpy.context.line_style`
   - :class:`BlendData.linestyles`
   - :class:`BlendDataLineStyles.new`
   - :class:`BlendDataLineStyles.remove`
   - :class:`FreestyleLineSet.linestyle`

