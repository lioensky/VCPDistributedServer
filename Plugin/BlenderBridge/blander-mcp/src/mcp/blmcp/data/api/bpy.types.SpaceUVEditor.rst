SpaceUVEditor(bpy_struct)
=========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: SpaceUVEditor(bpy_struct)

   UV editor data for the image editor space

   .. attribute:: custom_grid_subdivisions

      Number of grid units in UV space that make one UV Unit (array of 2 items, in [1, 5000], default (0, 0))

      :type: :class:`bpy_prop_array`\ [int]

   .. attribute:: display_stretch_type

      Type of stretch to display (default ``'ANGLE'``)

      - ``ANGLE``
        Angle -- Angular distortion between UV and 3D angles.
      - ``AREA``
        Area -- Area distortion between UV and 3D faces.

      :type: Literal['ANGLE', 'AREA']

   .. attribute:: edge_display_type

      Display style for UV edges (default ``'OUTLINE'``)

      - ``OUTLINE``
        Outline -- Display white edges with black outline.
      - ``DASH``
        Dash -- Display dashed black-white edges.
      - ``BLACK``
        Black -- Display black edges.
      - ``WHITE``
        White -- Display white edges.

      :type: Literal['OUTLINE', 'DASH', 'BLACK', 'WHITE']

   .. attribute:: grid_shape_source

      Specify source for the grid shape (default ``'DYNAMIC'``)

      - ``DYNAMIC``
        Dynamic -- Dynamic grid.
      - ``FIXED``
        Fixed -- Manually set grid divisions.
      - ``PIXEL``
        Pixel -- Grid aligns with pixels from image.

      :type: Literal['DYNAMIC', 'FIXED', 'PIXEL']

   .. attribute:: lock_bounds

      Constraint to stay within the image bounds while editing (default False)

      :type: bool

   .. attribute:: pixel_round_mode

      Round UVs to pixels while editing (default ``'DISABLED'``)

      - ``DISABLED``
        Disabled -- Don't round to pixels.
      - ``CORNER``
        Corner -- Round to pixel corners.
      - ``CENTER``
        Center -- Round to pixel centers.

      :type: Literal['DISABLED', 'CORNER', 'CENTER']

   .. attribute:: show_faces

      Display faces over the image (default True)

      :type: bool

   .. attribute:: show_grid_over_image

      Show the grid over the image (default True)

      :type: bool

   .. attribute:: show_metadata

      Display metadata properties of the image (default False)

      :type: bool

   .. attribute:: show_modified_edges

      Display edges after modifiers are applied (default False)

      :type: bool

   .. attribute:: show_pixel_coords

      Display UV coordinates in pixels rather than from 0.0 to 1.0 (default True)

      :type: bool

   .. attribute:: show_stretch

      Display faces colored according to the difference in shape between UVs and their 3D coordinates (blue for low distortion, red for high distortion) (default False)

      :type: bool

   .. attribute:: show_uv

      Display overlay of UV layer (default True)

      :type: bool

   .. attribute:: stretch_opacity

      Opacity of the UV Stretch overlay (in [0, 1], default 0.0)

      :type: float

   .. attribute:: tile_grid_shape

      How many tiles will be shown in the background (array of 2 items, in [1, 100], default (0, 0))

      :type: :class:`bpy_prop_array`\ [int]

   .. attribute:: use_live_unwrap

      Continuously unwrap the selected UV island while transforming pinned vertices (default False)

      :type: bool

   .. attribute:: uv_edge_opacity

      Opacity of edges in UV overlays (in [0, 1], default 0.0)

      :type: float

   .. attribute:: uv_face_opacity

      Opacity of faces in UV overlays (in [0, 1], default 0.0)

      :type: float

   .. attribute:: uv_opacity

      Opacity of UV overlays (in [0, 1], default 0.0)

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

   - :class:`SpaceImageEditor.uv_editor`

