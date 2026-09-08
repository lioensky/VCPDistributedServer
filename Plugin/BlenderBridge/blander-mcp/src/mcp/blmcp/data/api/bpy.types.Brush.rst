Brush(ID)
=========

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: Brush(ID)

   Brush data-block for storing brush settings for painting and sculpting

   .. attribute:: area_radius_factor

      Ratio between the brush radius and the radius that is going to be used to sample the area center (in [0, 2], default 0.5)

      :type: float

   .. attribute:: auto_smooth_factor

      Amount of smoothing to automatically apply to each stroke (in [0, 1], default 0.0)

      :type: float

   .. attribute:: automasking_boundary_edges_propagation_steps

      Distance where boundary edge automasking is going to protect vertices from the fully masked edge (in [1, 20], default 1)

      :type: int

   .. attribute:: automasking_cavity_blur_steps

      The number of times the cavity mask is blurred (in [0, 25], default 0)

      :type: int

   .. data:: automasking_cavity_curve

      Curve used for the sensitivity (readonly)

      :type: :class:`CurveMapping` | None

   .. attribute:: automasking_cavity_factor

      The contrast of the cavity mask (in [0, 5], default 1.0)

      :type: float

   .. attribute:: automasking_start_normal_falloff

      Extend the angular range with a falloff gradient (in [0.0001, 1], default 0.25)

      :type: float

   .. attribute:: automasking_start_normal_limit

      The range of angles that will be affected (in [0.0001, 3.14159], default 0.349066)

      :type: float

   .. attribute:: automasking_view_normal_falloff

      Extend the angular range with a falloff gradient (in [0.0001, 1], default 0.25)

      :type: float

   .. attribute:: automasking_view_normal_limit

      The range of angles that will be affected (in [0.0001, 3.14159], default 1.5708)

      :type: float

   .. attribute:: blend

      Brush blending mode (default ``'MIX'``)

      - ``MIX``
        Mix -- Use Mix blending mode while painting.
      - ``DARKEN``
        Darken -- Use Darken blending mode while painting.
      - ``MUL``
        Multiply -- Use Multiply blending mode while painting.
      - ``COLORBURN``
        Color Burn -- Use Color Burn blending mode while painting.
      - ``LINEARBURN``
        Linear Burn -- Use Linear Burn blending mode while painting.
      - ``LIGHTEN``
        Lighten -- Use Lighten blending mode while painting.
      - ``SCREEN``
        Screen -- Use Screen blending mode while painting.
      - ``COLORDODGE``
        Color Dodge -- Use Color Dodge blending mode while painting.
      - ``ADD``
        Add -- Use Add blending mode while painting.
      - ``OVERLAY``
        Overlay -- Use Overlay blending mode while painting.
      - ``SOFTLIGHT``
        Soft Light -- Use Soft Light blending mode while painting.
      - ``HARDLIGHT``
        Hard Light -- Use Hard Light blending mode while painting.
      - ``VIVIDLIGHT``
        Vivid Light -- Use Vivid Light blending mode while painting.
      - ``LINEARLIGHT``
        Linear Light -- Use Linear Light blending mode while painting.
      - ``PINLIGHT``
        Pin Light -- Use Pin Light blending mode while painting.
      - ``DIFFERENCE``
        Difference -- Use Difference blending mode while painting.
      - ``EXCLUSION``
        Exclusion -- Use Exclusion blending mode while painting.
      - ``SUB``
        Subtract -- Use Subtract blending mode while painting.
      - ``HUE``
        Hue -- Use Hue blending mode while painting.
      - ``SATURATION``
        Saturation -- Use Saturation blending mode while painting.
      - ``COLOR``
        Color -- Use Color blending mode while painting.
      - ``LUMINOSITY``
        Value -- Use Value blending mode while painting.
      - ``ERASE_ALPHA``
        Erase Alpha -- Erase alpha while painting.
      - ``ADD_ALPHA``
        Add Alpha -- Add alpha while painting.

      :type: Literal['MIX', 'DARKEN', 'MUL', 'COLORBURN', 'LINEARBURN', 'LIGHTEN', 'SCREEN', 'COLORDODGE', 'ADD', 'OVERLAY', 'SOFTLIGHT', 'HARDLIGHT', 'VIVIDLIGHT', 'LINEARLIGHT', 'PINLIGHT', 'DIFFERENCE', 'EXCLUSION', 'SUB', 'HUE', 'SATURATION', 'COLOR', 'LUMINOSITY', 'ERASE_ALPHA', 'ADD_ALPHA']

   .. attribute:: blur_kernel_radius

      Radius of kernel used for soften and sharpen in pixels (in [1, 10000], default 2)

      :type: int

   .. attribute:: blur_mode

      (default ``'GAUSSIAN'``)

      :type: Literal['BOX', 'GAUSSIAN']

   .. attribute:: boundary_deform_type

      Deformation type that is used in the brush (default ``'BEND'``)

      :type: Literal['BEND', 'EXPAND', 'INFLATE', 'GRAB', 'TWIST', 'SMOOTH']

   .. attribute:: boundary_falloff_type

      How the brush falloff is applied across the boundary (default ``'CONSTANT'``)

      - ``CONSTANT``
        Constant -- Applies the same deformation in the entire boundary.
      - ``RADIUS``
        Brush Radius -- Applies the deformation in a localized area limited by the brush radius.
      - ``LOOP``
        Loop -- Applies the brush falloff in a loop pattern.
      - ``LOOP_INVERT``
        Loop and Invert -- Applies the falloff radius in a loop pattern, inverting the displacement direction in each pattern repetition.

      :type: Literal['CONSTANT', 'RADIUS', 'LOOP', 'LOOP_INVERT']

   .. attribute:: boundary_offset

      Offset of the boundary origin in relation to the brush radius (in [0, 30], default 0.0)

      :type: float

   .. data:: brush_capabilities

      Brush's capabilities (readonly, never None)

      :type: :class:`BrushCapabilities`

   .. attribute:: cloth_constraint_softbody_strength

      How much the cloth preserves the original shape, acting as a soft body (in [0, 1], default 0.0)

      :type: float

   .. attribute:: cloth_damping

      How much the applied forces are propagated through the cloth (in [0.01, 1], default 0.01)

      :type: float

   .. attribute:: cloth_deform_type

      Deformation type that is used in the brush (default ``'DRAG'``)

      :type: Literal['DRAG', 'PUSH', 'PINCH_POINT', 'PINCH_PERPENDICULAR', 'INFLATE', 'GRAB', 'EXPAND', 'SNAKE_HOOK']

   .. attribute:: cloth_force_falloff_type

      Shape used in the brush to apply force to the cloth (default ``'RADIAL'``)

      :type: Literal['RADIAL', 'PLANE']

   .. attribute:: cloth_mass

      Mass of each simulation particle (in [0.01, 2], default 1.0)

      :type: float

   .. attribute:: cloth_sim_falloff

      Area to apply deformation falloff to the effects of the simulation (in [0, 1], default 0.75)

      :type: float

   .. attribute:: cloth_sim_limit

      Factor added relative to the size of the radius to limit the cloth simulation effects (in [0.1, 10], default 2.5)

      :type: float

   .. attribute:: cloth_simulation_area_type

      Part of the mesh that is going to be simulated when the stroke is active (default ``'LOCAL'``)

      - ``LOCAL``
        Local -- Simulates only a specific area around the brush limited by a fixed radius.
      - ``GLOBAL``
        Global -- Simulates the entire mesh.
      - ``DYNAMIC``
        Dynamic -- The active simulation area moves with the brush.

      :type: Literal['LOCAL', 'GLOBAL', 'DYNAMIC']

   .. attribute:: color

      (array of 3 items, in [0, inf], default (1.0, 1.0, 1.0))

      :type: :class:`mathutils.Color`

   .. attribute:: color_type

      Use single color or gradient when painting (default ``'COLOR'``)

      - ``COLOR``
        Color -- Paint with a single color.
      - ``GRADIENT``
        Gradient -- Paint with a gradient.

      :type: Literal['COLOR', 'GRADIENT']

   .. attribute:: crease_pinch_factor

      How much the crease brush pinches (in [0, 1], default 0.5)

      :type: float

   .. attribute:: cursor_color_add

      Color of cursor when adding (array of 4 items, in [0, inf], default (1.0, 0.39, 0.39, 0.9))

      :type: :class:`bpy_prop_array`\ [float]

   .. attribute:: cursor_color_subtract

      Color of cursor when subtracting (array of 4 items, in [0, inf], default (0.39, 0.39, 1.0, 0.9))

      :type: :class:`bpy_prop_array`\ [float]

   .. attribute:: cursor_overlay_alpha

      (in [0, 100], default 33)

      :type: int

   .. data:: curve_distance_falloff

      Editable falloff curve (readonly, never None)

      :type: :class:`CurveMapping`

   .. attribute:: curve_distance_falloff_preset

      (default ``'CUSTOM'``)

      :type: Literal[:ref:`rna_enum_brush_curve_preset_items`]

   .. data:: curve_jitter

      Curve used to map pressure to brush jitter (readonly)

      :type: :class:`CurveMapping` | None

   .. data:: curve_random_hue

      Curve used for modulating effect (readonly)

      :type: :class:`CurveMapping` | None

   .. data:: curve_random_saturation

      Curve used for modulating effect (readonly)

      :type: :class:`CurveMapping` | None

   .. data:: curve_random_value

      Curve used for modulating effect (readonly)

      :type: :class:`CurveMapping` | None

   .. data:: curve_size

      Curve used to map pressure to brush size (readonly)

      :type: :class:`CurveMapping` | None

   .. data:: curve_strength

      Curve used to map pressure to brush strength (readonly)

      :type: :class:`CurveMapping` | None

   .. attribute:: curves_sculpt_brush_type

      (default ``'COMB'``)

      :type: Literal[:ref:`rna_enum_brush_curves_sculpt_brush_type_items`]

   .. data:: curves_sculpt_settings

      (readonly)

      :type: :class:`BrushCurvesSculptSettings` | None

   .. attribute:: dash_ratio

      Ratio of samples in a cycle that the brush is enabled (in [0, 1], default 1.0)

      :type: float

   .. attribute:: dash_samples

      Length of a dash cycle measured in stroke samples (in [1, 10000], default 20)

      :type: int

   .. attribute:: deform_target

      How the deformation of the brush will affect the object (default ``'GEOMETRY'``)

      - ``GEOMETRY``
        Geometry -- Brush deformation displaces the vertices of the mesh.
      - ``CLOTH_SIM``
        Cloth Simulation -- Brush deforms the mesh by deforming the constraints of a cloth simulation.

      :type: Literal['GEOMETRY', 'CLOTH_SIM']

   .. attribute:: density

      Amount of random elements that are going to be affected by the brush (in [0, 1], default 0.0)

      :type: float

   .. attribute:: direction

      (default ``'ADD'``)

      - ``ADD``
        Add -- Add effect of brush.
      - ``SUBTRACT``
        Subtract -- Subtract effect of brush.

      :type: Literal['ADD', 'SUBTRACT']

   .. attribute:: disconnected_distance_max

      Maximum distance to search for disconnected loose parts in the mesh (in [0, 10], default 0.1)

      :type: float

   .. attribute:: elastic_deform_type

      Deformation type that is used in the brush (default ``'GRAB'``)

      :type: Literal['GRAB', 'GRAB_BISCALE', 'GRAB_TRISCALE', 'SCALE', 'TWIST']

   .. attribute:: elastic_deform_volume_preservation

      Poisson ratio for elastic deformation. Higher values preserve volume more, but also lead to more bulging. (in [0, 0.9], default 0.0)

      :type: float

   .. attribute:: falloff_angle

      Paint most on faces pointing towards the view according to this angle (in [0, 1.5708], default 0.0)

      :type: float

   .. attribute:: falloff_shape

      Use projected or spherical falloff (default ``'SPHERE'``)

      - ``SPHERE``
        Sphere -- Apply brush influence in a Sphere, outwards from the center.
      - ``PROJECTED``
        Projected -- Apply brush influence in a 2D circle, projected from the view.

      :type: Literal['SPHERE', 'PROJECTED']

   .. attribute:: fill_threshold

      Threshold above which filling is not propagated (in [0, 100], default 0.2)

      :type: float

   .. attribute:: flow

      Amount of paint that is applied per stroke sample (in [0, 1], default 0.0)

      :type: float

   .. attribute:: gpencil_brush_type

      (default ``'DRAW'``)

      :type: Literal[:ref:`rna_enum_brush_gpencil_types_items`]

   .. attribute:: gpencil_sculpt_brush_type

      (default ``'SMOOTH'``)

      :type: Literal[:ref:`rna_enum_brush_gpencil_sculpt_types_items`]

   .. data:: gpencil_settings

      (readonly)

      :type: :class:`BrushGpencilSettings` | None

   .. attribute:: gpencil_vertex_brush_type

      (default ``'DRAW'``)

      :type: Literal[:ref:`rna_enum_brush_gpencil_vertex_types_items`]

   .. attribute:: gpencil_weight_brush_type

      (default ``'WEIGHT'``)

      :type: Literal[:ref:`rna_enum_brush_gpencil_weight_types_items`]

   .. attribute:: grad_spacing

      Spacing before brush gradient goes full circle (in [1, 10000], default 0)

      :type: int

   .. data:: gradient

      (readonly)

      :type: :class:`ColorRamp` | None

   .. attribute:: gradient_fill_mode

      (default ``'LINEAR'``)

      :type: Literal['LINEAR', 'RADIAL']

   .. attribute:: gradient_stroke_mode

      (default ``'PRESSURE'``)

      :type: Literal['PRESSURE', 'SPACING_REPEAT', 'SPACING_CLAMP']

   .. attribute:: hardness

      How close the brush falloff starts from the edge of the brush (in [0, 1], default 0.0)

      :type: float

   .. data:: has_unsaved_changes

      Indicates that there are any user visible changes since the brush has been imported or read from the file (default False, readonly)

      :type: bool

   .. attribute:: height

      Affectable height of brush (i.e. the layer height for the layer tool) (in [0, 1], default 0.5)

      :type: float

   .. attribute:: hue_jitter

      Color jitter effect on hue (in [0, 1], default 0.0)

      :type: float

   .. attribute:: image_brush_type

      (default ``'DRAW'``)

      :type: Literal[:ref:`rna_enum_brush_image_brush_type_items`]

   .. data:: image_paint_capabilities

      (readonly, never None)

      :type: :class:`BrushCapabilitiesImagePaint`

   .. attribute:: input_samples

      Number of input samples to average together to smooth the brush stroke (in [1, 64], default 1)

      :type: int

   .. attribute:: invert_density_pressure

      Invert the modulation of pressure in density (default False)

      :type: bool

   .. attribute:: invert_flow_pressure

      Invert the modulation of pressure in flow (default False)

      :type: bool

   .. attribute:: invert_hardness_pressure

      Invert the modulation of pressure in hardness (default False)

      :type: bool

   .. attribute:: invert_to_scrape_fill

      Use Scrape or Fill brush when inverting this brush instead of inverting its displacement direction (default False)

      :type: bool

   .. attribute:: invert_wet_mix_pressure

      Invert the modulation of pressure in wet mix (default False)

      :type: bool

   .. attribute:: invert_wet_persistence_pressure

      Invert the modulation of pressure in wet persistence (default False)

      :type: bool

   .. attribute:: jitter

      Jitter the position of the brush while painting (in [0, 1000], default 0.0)

      :type: float

   .. attribute:: jitter_absolute

      Jitter the position of the brush in pixels while painting (in [0, 1000000], default 0)

      :type: int

   .. attribute:: jitter_unit

      Jitter in screen space or relative to brush size (default ``'VIEW'``)

      - ``VIEW``
        View -- Jittering happens in screen space, in pixels.
      - ``BRUSH``
        Brush -- Jittering happens relative to the brush size.

      :type: Literal['VIEW', 'BRUSH']

   .. attribute:: mask_overlay_alpha

      (in [0, 100], default 33)

      :type: int

   .. attribute:: mask_stencil_dimension

      Dimensions of mask stencil in viewport (array of 2 items, in [-inf, inf], default (256.0, 256.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: mask_stencil_pos

      Position of mask stencil in viewport (array of 2 items, in [-inf, inf], default (256.0, 256.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: mask_texture

      :type: :class:`Texture` | None

   .. data:: mask_texture_slot

      (readonly)

      :type: :class:`BrushTextureSlot` | None

   .. attribute:: mask_tool

      (default ``'DRAW'``)

      :type: Literal['DRAW', 'SMOOTH']

   .. attribute:: multiplane_scrape_angle

      Angle between the planes of the crease (in [0, 160], default 0.0)

      :type: float

   .. attribute:: normal_radius_factor

      Ratio between the brush radius and the radius that is going to be used to sample the normal (in [0, 2], default 0.5)

      :type: float

   .. attribute:: normal_weight

      How much grab will pull vertices out of surface during a grab (in [0, 1], default 0.0)

      :type: float

   .. attribute:: paint_curve

      Active paint curve

      :type: :class:`PaintCurve` | None

   .. attribute:: plane_depth

      The maximum distance below the plane for affected vertices. Increasing the depth affects vertices farther below the plane. (in [0, 1], default 0.0)

      :type: float

   .. attribute:: plane_height

      The maximum distance above the plane for affected vertices. Increasing the height affects vertices farther above the plane. (in [0, 1], default 1.0)

      :type: float

   .. attribute:: plane_inversion_mode

      Inversion Mode (default ``'INVERT_DISPLACEMENT'``)

      - ``INVERT_DISPLACEMENT``
        Invert Displacement -- Displace the vertices away from the plane..
      - ``SWAP_DEPTH_AND_HEIGHT``
        Swap Height and Depth -- Swap the roles of Height and Depth..

      :type: Literal['INVERT_DISPLACEMENT', 'SWAP_DEPTH_AND_HEIGHT']

   .. attribute:: plane_offset

      Adjust plane on which the brush acts towards or away from the object surface (in [-2, 2], default 0.0)

      :type: float

   .. attribute:: plane_trim

      If a vertex is further away from offset plane than this, then it is not affected (in [0, 1], default 0.5)

      :type: float

   .. attribute:: pose_deform_type

      Deformation type that is used in the brush (default ``'ROTATE_TWIST'``)

      :type: Literal['ROTATE_TWIST', 'SCALE_TRANSLATE', 'SQUASH_STRETCH']

   .. attribute:: pose_ik_segments

      Number of segments of the inverse kinematics chain that will deform the mesh (in [1, 20], default 1)

      :type: int

   .. attribute:: pose_offset

      Offset of the pose origin in relation to the brush radius (in [0, 2], default 0.0)

      :type: float

   .. attribute:: pose_origin_type

      Method to set the rotation origins for the segments of the brush (default ``'TOPOLOGY'``)

      - ``TOPOLOGY``
        Topology -- Sets the rotation origin automatically using the topology and shape of the mesh as a guide.
      - ``FACE_SETS``
        Face Sets -- Creates a pose segment per face set, starting from the active face set.
      - ``FACE_SETS_FK``
        Face Sets FK -- Simulates an FK deformation using the face set under the cursor as control.

      :type: Literal['TOPOLOGY', 'FACE_SETS', 'FACE_SETS_FK']

   .. attribute:: pose_smooth_iterations

      Smooth iterations applied after calculating the pose factor of each vertex (in [0, 100], default 4)

      :type: int

   .. attribute:: rake_factor

      How much grab will follow cursor rotation (in [0, 10], default 0.0)

      :type: float

   .. attribute:: rate

      Interval between paints for Airbrush (in [0.0001, 10000], default 0.1)

      :type: float

   .. attribute:: saturation_jitter

      Color jitter effect on saturation (in [0, 1], default 0.0)

      :type: float

   .. attribute:: sculpt_brush_type

      (default ``'DRAW'``)

      :type: Literal[:ref:`rna_enum_brush_sculpt_brush_type_items`]

   .. data:: sculpt_capabilities

      (readonly, never None)

      :type: :class:`BrushCapabilitiesSculpt`

   .. attribute:: sculpt_plane

      (default ``'AREA'``)

      :type: Literal['AREA', 'VIEW', 'X', 'Y', 'Z']

   .. attribute:: secondary_color

      (array of 3 items, in [0, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. attribute:: sharp_threshold

      Threshold below which, no sharpening is done (in [0, 100], default 0.0)

      :type: float

   .. attribute:: show_multiplane_scrape_planes_preview

      Preview the scrape planes in the cursor during the stroke (default False)

      :type: bool

   .. attribute:: size

      Diameter of the brush in pixels (in [1, 10000], default 70)

      :type: int

   .. attribute:: slide_deform_type

      Deformation type that is used in the brush (default ``'DRAG'``)

      :type: Literal['DRAG', 'PINCH', 'EXPAND']

   .. attribute:: smear_deform_type

      Deformation type that is used in the brush (default ``'DRAG'``)

      :type: Literal['DRAG', 'PINCH', 'EXPAND']

   .. attribute:: smooth_deform_type

      Deformation type that is used in the brush (default ``'LAPLACIAN'``)

      - ``LAPLACIAN``
        Laplacian -- Smooths the surface and the volume.
      - ``SURFACE``
        Surface -- Smooths the surface of the mesh, preserving the volume.

      :type: Literal['LAPLACIAN', 'SURFACE']

   .. attribute:: smooth_stroke_factor

      Higher values give a smoother stroke (in [0.5, 0.99], default 0.9)

      :type: float

   .. attribute:: smooth_stroke_radius

      Minimum distance from last point before stroke continues (in [10, 200], default 75)

      :type: int

   .. attribute:: snake_hook_deform_type

      Deformation type that is used in the brush (default ``'FALLOFF'``)

      - ``FALLOFF``
        Radius Falloff -- Applies the brush falloff in the tip of the brush.
      - ``ELASTIC``
        Elastic -- Modifies the entire mesh using elastic deform.

      :type: Literal['FALLOFF', 'ELASTIC']

   .. attribute:: spacing

      Spacing between brush daubs as a percentage of brush diameter (in [1, 1000], default 10)

      :type: int

   .. attribute:: stabilize_normal

      How stable the plane normal is over the course of the stroke. A value of 0 corresponds to using the current normal, and a value of 1 corresponds to using the initial normal. (in [0, 1], default 0.0)

      :type: float

   .. attribute:: stabilize_plane

      How stable the plane center is over the course of the stroke. A value of 0 corresponds to using the current center, and a value of 1 corresponds to using the initial center. (in [0, 1], default 0.0)

      :type: float

   .. attribute:: stencil_dimension

      Dimensions of stencil in viewport (array of 2 items, in [-inf, inf], default (256.0, 256.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: stencil_pos

      Position of stencil in viewport (array of 2 items, in [-inf, inf], default (256.0, 256.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: strength

      How powerful the effect of the brush is when applied (in [0, 10], default 1.0)

      :type: float

   .. attribute:: stroke_method

      (default ``'DOTS'``)

      - ``DOTS``
        Dots -- Apply paint on each mouse move step.
      - ``DRAG_DOT``
        Drag Dot -- Allows a single dot to be carefully positioned.
      - ``SPACE``
        Space -- Limit brush application to the distance specified by spacing.
      - ``AIRBRUSH``
        Airbrush -- Keep applying paint effect while holding mouse (spray).
      - ``ANCHORED``
        Anchored -- Keep the brush anchored to the initial location.
      - ``LINE``
        Line -- Draw a line with dabs separated according to spacing.
      - ``CURVE``
        Curve -- Define the stroke curve with a Bézier curve (dabs are separated according to spacing).

      :type: Literal['DOTS', 'DRAG_DOT', 'SPACE', 'AIRBRUSH', 'ANCHORED', 'LINE', 'CURVE']

   .. attribute:: surface_smooth_current_vertex

      How much the position of each individual vertex influences the final result (in [0, 1], default 0.0)

      :type: float

   .. attribute:: surface_smooth_iterations

      Number of smoothing iterations per brush step (in [1, 10], default 0)

      :type: int

   .. attribute:: surface_smooth_shape_preservation

      How much of the original shape is preserved when smoothing (in [0, 1], default 0.0)

      :type: float

   .. attribute:: texture

      :type: :class:`Texture` | None

   .. attribute:: texture_overlay_alpha

      (in [0, 100], default 33)

      :type: int

   .. attribute:: texture_sample_bias

      Value added to texture samples (in [-1, 1], default 0.0)

      :type: float

   .. data:: texture_slot

      (readonly)

      :type: :class:`BrushTextureSlot` | None

   .. attribute:: tilt_strength_factor

      How much the tilt of the pen will affect the brush. Negative values indicate inverting the tilt directions. (in [-1, 1], default 0.0)

      :type: float

   .. attribute:: tip_roundness

      Roundness of the brush tip (in [0, 1], default 1.0)

      :type: float

   .. attribute:: tip_scale_x

      Scale of the brush tip in the X axis (in [0.0001, 1], default 1.0)

      :type: float

   .. attribute:: topology_rake_factor

      Automatically align edges to the brush direction to generate cleaner topology and define sharp features. Best used on low-poly meshes as it has a performance impact. (in [0, 1], default 0.0)

      :type: float

   .. attribute:: unprojected_size

      Diameter of brush in Blender units (in [0.001, inf], default 0.1)

      :type: float

   .. attribute:: use_accumulate

      Accumulate stroke daubs on top of each other (default False)

      :type: bool

   .. attribute:: use_adaptive_space

      Space daubs according to surface orientation instead of screen space (default False)

      :type: bool

   .. attribute:: use_alpha

      When this is disabled, lock alpha while painting (default True)

      :type: bool

   .. attribute:: use_automasking_boundary_edges

      Do not affect non manifold boundary edges (default False)

      :type: bool

   .. attribute:: use_automasking_boundary_face_sets

      Do not affect vertices that belong to a face set boundary (default False)

      :type: bool

   .. attribute:: use_automasking_cavity

      Do not affect vertices on peaks, based on the surface curvature (default False)

      :type: bool

   .. attribute:: use_automasking_cavity_inverted

      Do not affect vertices within crevices, based on the surface curvature (default False)

      :type: bool

   .. attribute:: use_automasking_custom_cavity_curve

      Use custom curve (default False)

      :type: bool

   .. attribute:: use_automasking_face_sets

      Affect only vertices that share face sets with the active vertex (default False)

      :type: bool

   .. attribute:: use_automasking_start_normal

      Affect only vertices with a similar normal to where the stroke starts (default False)

      :type: bool

   .. attribute:: use_automasking_topology

      Affect only vertices connected to the active vertex under the brush (default False)

      :type: bool

   .. attribute:: use_automasking_view_normal

      Affect only vertices with a normal that faces the viewer (default False)

      :type: bool

   .. attribute:: use_automasking_view_occlusion

      Only affect vertices that are not occluded by other faces (slower performance) (default False)

      :type: bool

   .. attribute:: use_cloth_collision

      Collide with objects during the simulation (default False)

      :type: bool

   .. attribute:: use_cloth_pin_simulation_boundary

      Lock the position of the vertices in the simulation falloff area to avoid artifacts and create a softer transition with unaffected areas (default False)

      :type: bool

   .. attribute:: use_color_as_displacement

      Handle each pixel color as individual vector for displacement (area plane mapping only) (default False)

      :type: bool

   .. attribute:: use_color_jitter

      Jitter brush color (default False)

      :type: bool

   .. attribute:: use_connected_only

      Affect only topologically connected elements (default False)

      :type: bool

   .. attribute:: use_cursor_overlay

      Show cursor in viewport (default False)

      :type: bool

   .. attribute:: use_cursor_overlay_override

      Don't show overlay during a stroke (default False)

      :type: bool

   .. attribute:: use_density_pressure

      Use pressure to modulate density (default False)

      :type: bool

   .. attribute:: use_edge_to_edge

      Drag anchor brush from edge-to-edge (default False)

      :type: bool

   .. attribute:: use_flow_pressure

      Use pressure to modulate flow (default False)

      :type: bool

   .. attribute:: use_frontface

      Brush only affects vertices that face the viewer (default False)

      :type: bool

   .. attribute:: use_frontface_falloff

      Blend brush influence by how much they face the front (default False)

      :type: bool

   .. attribute:: use_grab_active_vertex

      Apply the maximum grab strength to the active vertex instead of the cursor location (default False)

      :type: bool

   .. attribute:: use_grab_silhouette

      Grabs trying to automask the silhouette of the object (default False)

      :type: bool

   .. attribute:: use_hardness_pressure

      Use pressure to modulate hardness (default False)

      :type: bool

   .. attribute:: use_inverse_smooth_pressure

      Lighter pressure causes more smoothing to be applied (default False)

      :type: bool

   .. attribute:: use_locked_size

      Measure brush size relative to the view or the scene (default ``'VIEW'``)

      - ``VIEW``
        View -- Measure brush size relative to the view.
      - ``SCENE``
        Scene -- Measure brush size relative to the scene.

      :type: Literal['VIEW', 'SCENE']

   .. attribute:: use_multiplane_scrape_dynamic

      The angle between the planes changes during the stroke to fit the surface under the cursor (default False)

      :type: bool

   .. attribute:: use_offset_pressure

      Enable tablet pressure sensitivity for offset (default False)

      :type: bool

   .. attribute:: use_original_normal

      When locked keep using normal of surface where stroke was initiated (default False)

      :type: bool

   .. attribute:: use_original_plane

      When locked keep using the plane origin of surface where stroke was initiated (default False)

      :type: bool

   .. attribute:: use_paint_antialiasing

      Smooths the edges of the strokes (default True)

      :type: bool

   .. attribute:: use_paint_grease_pencil

      Use this brush in Grease Pencil drawing mode (default False)

      :type: bool

   .. attribute:: use_paint_image

      Use this brush in texture paint mode (default True)

      :type: bool

   .. attribute:: use_paint_sculpt

      Use this brush in sculpt mode (default True)

      :type: bool

   .. attribute:: use_paint_sculpt_curves

      Use this brush in sculpt curves mode (default False)

      :type: bool

   .. attribute:: use_paint_uv_sculpt

      Use this brush in UV sculpt mode (default False)

      :type: bool

   .. attribute:: use_paint_vertex

      Use this brush in vertex paint mode (default True)

      :type: bool

   .. attribute:: use_paint_weight

      Use this brush in weight paint mode (default True)

      :type: bool

   .. attribute:: use_persistent

      Sculpt on a persistent layer of the mesh (default False)

      :type: bool

   .. attribute:: use_plane_trim

      Limit the distance from the offset plane that a vertex can be affected (default False)

      :type: bool

   .. attribute:: use_pose_ik_anchored

      Keep the position of the last segment in the IK chain fixed (default False)

      :type: bool

   .. attribute:: use_pose_lock_rotation

      Do not rotate the segment when using the scale deform mode (default False)

      :type: bool

   .. attribute:: use_pressure_area_radius

      Enable tablet pressure sensitivity for area radius (default False)

      :type: bool

   .. attribute:: use_pressure_jitter

      Enable tablet pressure sensitivity for jitter (default False)

      :type: bool

   .. attribute:: use_pressure_masking

      Pen pressure makes texture influence smaller (default ``'NONE'``)

      :type: Literal['NONE', 'RAMP', 'CUTOFF']

   .. attribute:: use_pressure_size

      Enable tablet pressure sensitivity for size (default False)

      :type: bool

   .. attribute:: use_pressure_spacing

      Enable tablet pressure sensitivity for spacing (default False)

      :type: bool

   .. attribute:: use_pressure_strength

      Enable tablet pressure sensitivity for strength (default True)

      :type: bool

   .. attribute:: use_primary_overlay

      Show texture in viewport (default False)

      :type: bool

   .. attribute:: use_primary_overlay_override

      Don't show overlay during a stroke (default False)

      :type: bool

   .. attribute:: use_random_press_hue

      Use pressure to modulate randomness (default False)

      :type: bool

   .. attribute:: use_random_press_sat

      Use pressure to modulate randomness (default False)

      :type: bool

   .. attribute:: use_random_press_val

      Use pressure to modulate randomness (default False)

      :type: bool

   .. attribute:: use_scene_spacing

      Calculate the brush spacing using view or scene distance (default ``'VIEW'``)

      - ``VIEW``
        View -- Calculate brush spacing relative to the view.
      - ``SCENE``
        Scene -- Calculate brush spacing relative to the scene using the stroke location.

      :type: Literal['VIEW', 'SCENE']

   .. attribute:: use_secondary_overlay

      Show texture in viewport (default False)

      :type: bool

   .. attribute:: use_secondary_overlay_override

      Don't show overlay during a stroke (default False)

      :type: bool

   .. attribute:: use_smooth_stroke

      Brush lags behind mouse and follows a smoother path (default False)

      :type: bool

   .. attribute:: use_space_attenuation

      Automatically adjust strength to give consistent results for different spacings (default True)

      :type: bool

   .. attribute:: use_stroke_random_hue

      Use randomness at stroke level (default False)

      :type: bool

   .. attribute:: use_stroke_random_sat

      Use randomness at stroke level (default False)

      :type: bool

   .. attribute:: use_stroke_random_val

      Use randomness at stroke level (default False)

      :type: bool

   .. attribute:: use_vertex_grease_pencil

      Use this brush in Grease Pencil vertex color mode (default False)

      :type: bool

   .. attribute:: use_wet_mix_pressure

      Use pressure to modulate wet mix (default False)

      :type: bool

   .. attribute:: use_wet_persistence_pressure

      Use pressure to modulate wet persistence (default False)

      :type: bool

   .. attribute:: value_jitter

      Color jitter effect on value (in [0, 1], default 0.0)

      :type: float

   .. attribute:: vertex_brush_type

      (default ``'DRAW'``)

      :type: Literal[:ref:`rna_enum_brush_vertex_brush_type_items`]

   .. data:: vertex_paint_capabilities

      (readonly, never None)

      :type: :class:`BrushCapabilitiesVertexPaint`

   .. attribute:: weight

      Vertex weight when brush is applied (in [0, 1], default 1.0)

      :type: float

   .. attribute:: weight_brush_type

      (default ``'DRAW'``)

      :type: Literal[:ref:`rna_enum_brush_weight_brush_type_items`]

   .. data:: weight_paint_capabilities

      (readonly, never None)

      :type: :class:`BrushCapabilitiesWeightPaint`

   .. attribute:: wet_mix

      Amount of paint that is picked from the surface into the brush color (in [0, 1], default 0.0)

      :type: float

   .. attribute:: wet_paint_radius_factor

      Ratio between the brush radius and the radius that is going to be used to sample the color to blend in wet paint (in [0, 2], default 0.5)

      :type: float

   .. attribute:: wet_persistence

      Amount of wet paint that stays in the brush after applying paint to the surface (in [0, 1], default 0.0)

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

   - :mod:`bpy.context.brush`
   - :class:`BlendData.brushes`
   - :class:`BlendDataBrushes.create_gpencil_data`
   - :class:`BlendDataBrushes.new`
   - :class:`BlendDataBrushes.remove`
   - :class:`Paint.brush`
   - :class:`Paint.eraser_brush`

