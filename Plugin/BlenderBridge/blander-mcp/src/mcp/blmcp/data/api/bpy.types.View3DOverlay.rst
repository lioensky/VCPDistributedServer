View3DOverlay(bpy_struct)
=========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: View3DOverlay(bpy_struct)

   Settings for display of overlays in the 3D viewport

   .. attribute:: bone_wire_alpha

      Maximum opacity of bones in wireframe display mode (in [0, inf], default 1.0)

      :type: float

   .. attribute:: display_handle

      Limit the display of curve handles in Edit Mode (default ``'SELECTED'``)

      :type: Literal['NONE', 'SELECTED', 'ALL']

   .. attribute:: fade_inactive_alpha

      Strength of the fade effect (in [0, 1], default 0.4)

      :type: float

   .. attribute:: gpencil_fade_layer

      Fade layer opacity for Grease Pencil layers except the active one (in [0, 1], default 0.5)

      :type: float

   .. attribute:: gpencil_fade_objects

      Fade factor (in [0, 1], default 0.5)

      :type: float

   .. attribute:: gpencil_grid_color

      Canvas grid color (array of 3 items, in [0, 1], default (0.5, 0.5, 0.5))

      :type: :class:`mathutils.Color`

   .. attribute:: gpencil_grid_offset

      Canvas grid offset (array of 2 items, in [-inf, inf], default (0.0, 0.0))

      :type: :class:`bpy_prop_array`\ [float]

   .. attribute:: gpencil_grid_opacity

      Canvas grid opacity (in [0.1, 1], default 0.9)

      :type: float

   .. attribute:: gpencil_grid_scale

      Canvas grid scale (array of 2 items, in [0, inf], default (1.0, 1.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: gpencil_grid_subdivisions

      Canvas grid subdivisions (in [1, 100], default 4)

      :type: int

   .. attribute:: gpencil_vertex_paint_opacity

      Vertex Paint mix factor (in [0, 1], default 1.0)

      :type: float

   .. attribute:: grid_lines

      Number of grid lines to display in perspective view (in [0, 1024], default 16)

      :type: int

   .. attribute:: grid_scale

      Multiplier for the distance between 3D View grid lines (in [0, inf], default 1.0)

      :type: float

   .. data:: grid_scale_unit

      Grid cell size scaled by scene unit system settings (in [-inf, inf], default 0.0, readonly)

      :type: float

   .. attribute:: grid_subdivisions

      Number of subdivisions between grid lines (in [1, 1024], default 10)

      :type: int

   .. attribute:: normals_constant_screen_size

      Screen size for normals in the 3D view (in [0, 100000], default 7.0)

      :type: float

   .. attribute:: normals_length

      Display size for normals in the 3D view (in [1e-05, 100000], default 0.1)

      :type: float

   .. attribute:: retopology_offset

      Offset used to draw edit mesh in front of other geometry (in [0, inf], default 0.01)

      :type: float

   .. attribute:: sculpt_curves_cage_opacity

      Opacity of the cage overlay in curves sculpt mode (in [0, 1], default 0.0)

      :type: float

   .. attribute:: sculpt_mode_face_sets_opacity

      (in [0, 1], default 1.0)

      :type: float

   .. attribute:: sculpt_mode_mask_opacity

      (in [0, 1], default 0.75)

      :type: float

   .. attribute:: show_annotation

      Show annotations for this view (default True)

      :type: bool

   .. attribute:: show_axis_x

      Show the X axis line (default True)

      :type: bool

   .. attribute:: show_axis_y

      Show the Y axis line (default True)

      :type: bool

   .. attribute:: show_axis_z

      Show the Z axis line (default False)

      :type: bool

   .. attribute:: show_bones

      Display bones (disable to show motion paths only) (default True)

      :type: bool

   .. attribute:: show_camera_guides

      Show camera composition guides (default True)

      :type: bool

   .. attribute:: show_camera_passepartout

      Show camera passepartout (default True)

      :type: bool

   .. attribute:: show_cursor

      Display 3D Cursor Overlay (default True)

      :type: bool

   .. attribute:: show_curve_normals

      Display 3D curve normals in Edit Mode (default False)

      :type: bool

   .. attribute:: show_edge_bevel_weight

      Display weights created for the Bevel modifier (default True)

      :type: bool

   .. attribute:: show_edge_crease

      Display creases created for Subdivision Surface modifier (default True)

      :type: bool

   .. attribute:: show_edge_seams

      Display UV unwrapping seams (default True)

      :type: bool

   .. attribute:: show_edge_sharp

      Display sharp edges, used with the Edge Split modifier (default True)

      :type: bool

   .. attribute:: show_extra_edge_angle

      Display selected edge angle, using global values when set in the transform panel (default False)

      :type: bool

   .. attribute:: show_extra_edge_length

      Display selected edge lengths, using global values when set in the transform panel (default False)

      :type: bool

   .. attribute:: show_extra_face_angle

      Display the angles in the selected edges, using global values when set in the transform panel (default False)

      :type: bool

   .. attribute:: show_extra_face_area

      Display the area of selected faces, using global values when set in the transform panel (default False)

      :type: bool

   .. attribute:: show_extra_indices

      Display the index numbers of selected vertices, edges, and faces (default False)

      :type: bool

   .. attribute:: show_extras

      Object details, including empty wire, cameras and other visual guides (default True)

      :type: bool

   .. attribute:: show_face_center

      Display face center when face selection is enabled in solid shading modes (default False)

      :type: bool

   .. attribute:: show_face_normals

      Display face normals as lines (default False)

      :type: bool

   .. attribute:: show_face_orientation

      Show the Face Orientation Overlay (default False)

      :type: bool

   .. attribute:: show_faces

      Display a face selection overlay (default True)

      :type: bool

   .. attribute:: show_fade_inactive

      Fade inactive geometry using the viewport background color (default False)

      :type: bool

   .. attribute:: show_floor

      Show the ground plane grid (default True)

      :type: bool

   .. attribute:: show_freestyle_edge_marks

      Display Freestyle edge marks, used with the Freestyle renderer (default True)

      :type: bool

   .. attribute:: show_freestyle_face_marks

      Display Freestyle face marks, used with the Freestyle renderer (default True)

      :type: bool

   .. attribute:: show_light_colors

      Show light colors (default False)

      :type: bool

   .. attribute:: show_look_dev

      Show reference spheres with neutral shading that react to lighting to assist in look development (default False)

      :type: bool

   .. attribute:: show_motion_paths

      Show the Motion Paths Overlay (default True)

      :type: bool

   .. attribute:: show_object_origins

      Show object center dots (default True)

      :type: bool

   .. attribute:: show_object_origins_all

      Show the object origin center dot for all (selected and unselected) objects (default False)

      :type: bool

   .. attribute:: show_onion_skins

      Show the Onion Skinning Overlay (default False)

      :type: bool

   .. attribute:: show_ortho_grid

      Show grid in orthographic side view (default True)

      :type: bool

   .. attribute:: show_outline_selected

      Show an outline highlight around selected objects (default True)

      :type: bool

   .. attribute:: show_overlays

      Display overlays like gizmos and outlines (default True)

      :type: bool

   .. attribute:: show_paint_wire

      Use wireframe display in painting modes (default False)

      :type: bool

   .. attribute:: show_performance

      Display viewport performance timings:
       • Evaluation: Time to evaluate the dependency graph.
       • Synchronization: Time to build the GPU buffers.
      
      (default False)

      :type: bool

   .. attribute:: show_relationship_lines

      Show dashed lines indicating parent or constraint relationships (default True)

      :type: bool

   .. attribute:: show_retopology

      Hide the solid mesh and offset the overlay towards the view. Selection is occluded by inactive geometry, unless X-Ray is enabled (default False)

      :type: bool

   .. attribute:: show_sculpt_curves_cage

      Show original curves that are currently being edited (default False)

      :type: bool

   .. attribute:: show_sculpt_face_sets

      (default True)

      :type: bool

   .. attribute:: show_sculpt_mask

      (default True)

      :type: bool

   .. attribute:: show_split_normals

      Display vertex-per-face normals as lines (default False)

      :type: bool

   .. attribute:: show_stats

      Display scene statistics overlay text (default False)

      :type: bool

   .. attribute:: show_statvis

      Display statistical information about the mesh (default False)

      :type: bool

   .. attribute:: show_text

      Display overlay text (default True)

      :type: bool

   .. attribute:: show_vertex_normals

      Display vertex normals as lines (default False)

      :type: bool

   .. attribute:: show_viewer_attribute

      Show attribute overlay for active viewer node (default True)

      :type: bool

   .. attribute:: show_viewer_text

      Show attribute values as text in viewport (default False)

      :type: bool

   .. attribute:: show_weight

      Display weights in editmode (default False)

      :type: bool

   .. attribute:: show_wireframes

      Show face edges wires (default False)

      :type: bool

   .. attribute:: show_wpaint_contours

      Show contour lines formed by points with the same interpolated weight (default False)

      :type: bool

   .. attribute:: show_xray_bone

      Show the bone selection overlay (default False)

      :type: bool

   .. attribute:: texture_paint_mode_opacity

      Opacity of the texture paint mode stencil mask overlay (in [0, 1], default 1.0)

      :type: float

   .. attribute:: use_debug_freeze_view_culling

      Freeze view culling bounds (default False)

      :type: bool

   .. attribute:: use_gpencil_canvas_xray

      Show Canvas grid in front (default False)

      :type: bool

   .. attribute:: use_gpencil_edit_lines

      Show Edit Lines when editing strokes (default True)

      :type: bool

   .. attribute:: use_gpencil_fade_gp_objects

      Fade Grease Pencil Objects, except the active one (default False)

      :type: bool

   .. attribute:: use_gpencil_fade_layers

      Toggle fading of Grease Pencil layers except the active one (default False)

      :type: bool

   .. attribute:: use_gpencil_fade_objects

      Fade all viewport objects with a full color layer to improve visibility (default False)

      :type: bool

   .. attribute:: use_gpencil_grid

      Display a grid over Grease Pencil paper (default False)

      :type: bool

   .. attribute:: use_gpencil_multiedit_line_only

      Show Edit Lines only in multiframe (default False)

      :type: bool

   .. attribute:: use_gpencil_onion_skin

      Show ghosts of the keyframes before and after the current frame (default False)

      :type: bool

   .. attribute:: use_gpencil_onion_skin_active_object

      Show only the onion skins of the active object (default False)

      :type: bool

   .. attribute:: use_gpencil_show_directions

      Show stroke drawing direction with a bigger green dot (start) and smaller red dot (end) points (default False)

      :type: bool

   .. attribute:: use_gpencil_show_material_name

      Show material name assigned to each stroke (default False)

      :type: bool

   .. attribute:: use_normals_constant_screen_size

      Keep size of normals constant in relation to 3D view (default False)

      :type: bool

   .. attribute:: vertex_opacity

      Opacity for edit vertices (in [0, 1], default 1.0)

      :type: float

   .. attribute:: vertex_paint_mode_opacity

      Opacity of the texture paint mode stencil mask overlay (in [0, 1], default 1.0)

      :type: float

   .. attribute:: viewer_attribute_opacity

      Opacity of the attribute that is currently visualized (in [0, 1], default 1.0)

      :type: float

   .. attribute:: weight_paint_mode_opacity

      Opacity of the weight paint mode overlay (in [0, 1], default 1.0)

      :type: float

   .. attribute:: wireframe_opacity

      Opacity of the displayed edges (1.0 for opaque) (in [0, 1], default 1.0)

      :type: float

   .. attribute:: wireframe_threshold

      Adjust the angle threshold for displaying edges (1.0 for all) (in [0, 1], default 1.0)

      :type: float

   .. attribute:: xray_alpha_bone

      Opacity to use for bone selection (in [0, 1], default 0.5)

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

   - :class:`SpaceView3D.overlay`

