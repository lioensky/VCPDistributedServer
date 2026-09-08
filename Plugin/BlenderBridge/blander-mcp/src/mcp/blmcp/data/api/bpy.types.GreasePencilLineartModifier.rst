GreasePencilLineartModifier(Modifier)
=====================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: GreasePencilLineartModifier(Modifier)

   Generate Line Art strokes from selected source

   .. attribute:: chaining_image_threshold

      Segments with an image distance smaller than this will be chained together (in [0, 0.3], default 0.001)

      :type: float

   .. attribute:: crease_threshold

      Angles smaller than this will be treated as creases. Crease angle priority: object Line Art crease override > mesh auto smooth angle > Line Art default crease. (in [0, 3.14159], default 2.44346)

      :type: float

   .. attribute:: invert_source_vertex_group

      Invert source vertex group values (default False)

      :type: bool

   .. attribute:: is_baked

      This modifier has baked data (default False)

      :type: bool

   .. attribute:: level_end

      Maximum number of occlusions for the generated strokes (in [0, 128], default 0)

      :type: int

   .. attribute:: level_start

      Minimum number of occlusions for the generated strokes (in [0, 128], default 0)

      :type: int

   .. attribute:: light_contour_object

      Use this light object to generate light contour

      :type: :class:`Object` | None

   .. attribute:: opacity

      The strength value for the generate strokes (in [0, 1], default 1.0)

      :type: float

   .. attribute:: overscan

      A margin to prevent strokes from ending abruptly at the edge of the image (in [0, 0.5], default 0.1)

      :type: float

   .. attribute:: radius

      The radius for the generated strokes (in [0, 1], default 0.0025)

      :type: float

   .. attribute:: shadow_camera_far

      Far clipping distance of shadow camera (in [0, 10000], default 200.0)

      :type: float

   .. attribute:: shadow_camera_near

      Near clipping distance of shadow camera (in [0, 10000], default 0.1)

      :type: float

   .. attribute:: shadow_camera_size

      Represents the "Orthographic Scale" of an orthographic camera. If the camera is positioned at the light's location with this scale, it will represent the coverage of the shadow "camera". (in [0, 10000], default 200.0)

      :type: float

   .. attribute:: shadow_region_filtering

      Select feature lines that comes from lit or shaded regions. Will not affect cast shadow and light contour since they are at the border. (default ``'NONE'``)

      - ``NONE``
        None -- Not filtering any lines based on illumination region.
      - ``ILLUMINATED``
        Illuminated -- Only selecting lines from illuminated regions.
      - ``SHADED``
        Shaded -- Only selecting lines from shaded regions.
      - ``ILLUMINATED_ENCLOSED``
        Illuminated (Enclosed Shapes) -- Selecting lines from lit regions, and make the combination of contour, light contour and shadow lines into enclosed shapes.

      :type: Literal['NONE', 'ILLUMINATED', 'SHADED', 'ILLUMINATED_ENCLOSED']

   .. attribute:: silhouette_filtering

      Select contour or silhouette (default ``'NONE'``)

      :type: Literal['NONE', 'GROUP', 'INDIVIDUAL']

   .. attribute:: smooth_tolerance

      Strength of smoothing applied on jagged chains (in [0, 30], default 0.0)

      :type: float

   .. attribute:: source_camera

      Use specified camera object for generating Line Art strokes

      :type: :class:`Object` | None

   .. attribute:: source_collection

      Generate strokes from the objects in this collection

      :type: :class:`Collection` | None

   .. attribute:: source_object

      Generate strokes from this object

      :type: :class:`Object` | None

   .. attribute:: source_type

      Line Art stroke source type (default ``'COLLECTION'``)

      :type: Literal['COLLECTION', 'OBJECT', 'SCENE']

   .. attribute:: source_vertex_group

      Match the beginning of vertex group names from mesh objects, match all when left empty (default "", never None)

      :type: str

   .. attribute:: split_angle

      Angle in screen space below which a stroke is split in two (in [0, 3.14159], default 0.0)

      :type: float

   .. attribute:: stroke_depth_offset

      Move strokes slightly towards the camera to avoid clipping while preserve depth for the viewport (in [-0.1, inf], default 0.05)

      :type: float

   .. attribute:: target_layer

      Grease Pencil layer to which assign the generated strokes (default "", never None)

      :type: str

   .. attribute:: target_material

      Grease Pencil material assigned to the generated strokes

      :type: :class:`Material` | None

   .. attribute:: use_back_face_culling

      Remove all back faces to speed up calculation, this will create edges in different occlusion levels than when disabled (default False)

      :type: bool

   .. attribute:: use_cache

      Use cached scene data from the first Line Art modifier in the stack. Certain settings will be unavailable. (default False)

      :type: bool

   .. attribute:: use_clip_plane_boundaries

      Allow lines generated by the near/far clipping plane to be shown (default True)

      :type: bool

   .. attribute:: use_contour

      Generate strokes from contours lines (default False)

      :type: bool

   .. attribute:: use_crease

      Generate strokes from creased edges (default False)

      :type: bool

   .. attribute:: use_crease_on_sharp

      Allow crease to show on sharp edges (default True)

      :type: bool

   .. attribute:: use_crease_on_smooth

      Allow crease edges to show inside smooth surfaces (default False)

      :type: bool

   .. attribute:: use_custom_camera

      Use custom camera instead of the active camera (default False)

      :type: bool

   .. attribute:: use_detail_preserve

      Keep the zig-zag "noise" in initial chaining (default False)

      :type: bool

   .. attribute:: use_edge_mark

      Generate strokes from Freestyle marked edges (default False)

      :type: bool

   .. attribute:: use_edge_overlap

      Allow edges in the same location (i.e. from edge split) to show properly. May run slower. (default False)

      :type: bool

   .. attribute:: use_face_mark

      Filter feature lines using Freestyle face marks (default False)

      :type: bool

   .. attribute:: use_face_mark_boundaries

      Filter feature lines based on face mark boundaries (default False)

      :type: bool

   .. attribute:: use_face_mark_invert

      Invert face mark filtering (default False)

      :type: bool

   .. attribute:: use_face_mark_keep_contour

      Preserve contour lines while filtering (default True)

      :type: bool

   .. attribute:: use_fuzzy_all

      Treat all lines as the same line type so they can be chained together (default False)

      :type: bool

   .. attribute:: use_fuzzy_intersections

      Treat intersection and contour lines as if they were the same type so they can be chained together (default False)

      :type: bool

   .. attribute:: use_geometry_space_chain

      Use geometry distance for chaining instead of image space (default False)

      :type: bool

   .. attribute:: use_image_boundary_trimming

      Trim all edges right at the boundary of image (including overscan region) (default False)

      :type: bool

   .. attribute:: use_intersection

      Generate strokes from intersections (default False)

      :type: bool

   .. attribute:: use_intersection_mask

      Mask bits to match from Collection Line Art settings (array of 8 items, default (False, False, False, False, False, False, False, False))

      :type: :class:`bpy_prop_array`\ [bool]

   .. attribute:: use_intersection_match

      Require matching all intersection masks instead of just one (default False)

      :type: bool

   .. attribute:: use_invert_collection

      Select everything except lines from specified collection (default False)

      :type: bool

   .. attribute:: use_invert_silhouette

      Select anti-silhouette lines (default False)

      :type: bool

   .. attribute:: use_light_contour

      Generate light/shadow separation lines from a reference light object (default False)

      :type: bool

   .. attribute:: use_loose

      Generate strokes from loose edges (default False)

      :type: bool

   .. attribute:: use_loose_as_contour

      Loose edges will have contour type (default False)

      :type: bool

   .. attribute:: use_loose_edge_chain

      Allow loose edges to be chained together (default False)

      :type: bool

   .. attribute:: use_material

      Generate strokes from borders between materials (default False)

      :type: bool

   .. attribute:: use_material_mask

      Use material masks to filter out occluded strokes (default False)

      :type: bool

   .. attribute:: use_material_mask_bits

      Mask bits to match from Material Line Art settings (array of 8 items, default (False, False, False, False, False, False, False, False))

      :type: :class:`bpy_prop_array`\ [bool]

   .. attribute:: use_material_mask_match

      Require matching all material masks instead of just one (default False)

      :type: bool

   .. attribute:: use_multiple_levels

      Generate strokes from a range of occlusion levels (default False)

      :type: bool

   .. attribute:: use_object_instances

      Allow particle objects and face/vertex instances to show in Line Art (default True)

      :type: bool

   .. attribute:: use_offset_towards_custom_camera

      Offset strokes towards selected camera instead of the active camera (default False)

      :type: bool

   .. attribute:: use_output_vertex_group_match_by_name

      Match output vertex group based on name (default True)

      :type: bool

   .. attribute:: use_overlap_edge_type_support

      Allow an edge to have multiple overlapping types. This will create a separate stroke for each overlapping type. (default False)

      :type: bool

   .. attribute:: use_shadow

      Project contour lines using a light source object (default False)

      :type: bool

   .. attribute:: vertex_group

      Vertex group name for selected strokes (default "", never None)

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

