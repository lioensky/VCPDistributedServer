Sculpt Operators
================

.. module:: bpy.ops.sculpt

.. function:: brush_stroke(*, stroke=None, mode='NORMAL', brush_toggle='None', pen_flip=False, override_location=False, ignore_background_click=False)

   Sculpt a stroke into the geometry

   :param stroke: Stroke, (optional)
   :type stroke: :class:`bpy_prop_collection`\ [:class:`OperatorStrokeElement`] | None
   :param mode: Stroke Mode, Action taken when a paint stroke is made (optional)

      - ``NORMAL``
        Regular -- Apply brush normally.
      - ``INVERT``
        Invert -- Invert action of brush for duration of stroke.
   :type mode: Literal['NORMAL', 'INVERT']
   :param brush_toggle: Temporary Brush Toggle Type, Brush to use for duration of stroke (optional)

      - ``None``
        None -- Apply brush normally.
      - ``SMOOTH``
        Smooth -- Switch to smooth brush for duration of stroke.
      - ``ERASE``
        Erase -- Switch to erase brush for duration of stroke.
      - ``MASK``
        Mask -- Switch to mask brush for duration of stroke.
   :type brush_toggle: Literal['None', 'SMOOTH', 'ERASE', 'MASK']
   :param pen_flip: Pen Flip, Whether a tablet's eraser mode is being used (optional)
   :type pen_flip: bool
   :param override_location: Override Location, Override the given "location" array by recalculating object space positions from the provided "mouse_event" positions (optional)
   :type override_location: bool
   :param ignore_background_click: Ignore Background Click, Clicks on the background do not start the stroke (optional)
   :type ignore_background_click: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: cloth_filter(*, start_mouse=(0, 0), area_normal_radius=0.25, strength=1.0, iteration_count=1, event_history=None, type='GRAVITY', force_axis={'X', 'Y', 'Z'}, orientation='LOCAL', cloth_mass=1.0, cloth_damping=0.0, use_face_sets=False, use_collisions=False)

   Applies a cloth simulation deformation to the entire mesh

   :param start_mouse: Starting Mouse, (array of 2 items, in [0, 16384], optional)
   :type start_mouse: Sequence[int]
   :param area_normal_radius: Normal Radius, Radius used for calculating area normal on initial click,in percentage of brush radius(in [0.001, 5], optional)
   :type area_normal_radius: float
   :param strength: Strength, Filter strength (in [-10, 10], optional)
   :type strength: float
   :param iteration_count: Repeat, How many times to repeat the filter (in [1, 10000], optional)
   :type iteration_count: int
   :param event_history: (optional)
   :type event_history: :class:`bpy_prop_collection`\ [:class:`OperatorStrokeElement`] | None
   :param type: Filter Type, Operation that is going to be applied to the mesh (optional)

      - ``GRAVITY``
        Gravity -- Applies gravity to the simulation.
      - ``INFLATE``
        Inflate -- Inflates the cloth.
      - ``EXPAND``
        Expand -- Expands the cloth's dimensions.
      - ``PINCH``
        Pinch -- Pulls the cloth to the cursor's start position.
      - ``SCALE``
        Scale -- Scales the mesh as a soft body using the origin of the object as scale.
   :type type: Literal['GRAVITY', 'INFLATE', 'EXPAND', 'PINCH', 'SCALE']
   :param force_axis: Force Axis, Apply the force in the selected axis (optional)

      - ``X``
        X -- Apply force in the X axis.
      - ``Y``
        Y -- Apply force in the Y axis.
      - ``Z``
        Z -- Apply force in the Z axis.
   :type force_axis: set[Literal['X', 'Y', 'Z']]
   :param orientation: Orientation, Orientation of the axis to limit the filter force (optional)

      - ``LOCAL``
        Local -- Use the local axis to limit the force and set the gravity direction.
      - ``WORLD``
        World -- Use the global axis to limit the force and set the gravity direction.
      - ``VIEW``
        View -- Use the view axis to limit the force and set the gravity direction.
   :type orientation: Literal['LOCAL', 'WORLD', 'VIEW']
   :param cloth_mass: Cloth Mass, Mass of each simulation particle (in [0, 2], optional)
   :type cloth_mass: float
   :param cloth_damping: Cloth Damping, How much the applied forces are propagated through the cloth (in [0, 1], optional)
   :type cloth_damping: float
   :param use_face_sets: Use Face Sets, Apply the filter only to the face set under the cursor (optional)
   :type use_face_sets: bool
   :param use_collisions: Use Collisions, Collide with other collider objects in the scene (optional)
   :type use_collisions: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: color_filter(*, start_mouse=(0, 0), area_normal_radius=0.25, strength=1.0, iteration_count=1, event_history=None, type='FILL', fill_color=(1.0, 1.0, 1.0))

   Applies a filter to modify the active color attribute

   :param start_mouse: Starting Mouse, (array of 2 items, in [0, 16384], optional)
   :type start_mouse: Sequence[int]
   :param area_normal_radius: Normal Radius, Radius used for calculating area normal on initial click,in percentage of brush radius(in [0.001, 5], optional)
   :type area_normal_radius: float
   :param strength: Strength, Filter strength (in [-10, 10], optional)
   :type strength: float
   :param iteration_count: Repeat, How many times to repeat the filter (in [1, 10000], optional)
   :type iteration_count: int
   :param event_history: (optional)
   :type event_history: :class:`bpy_prop_collection`\ [:class:`OperatorStrokeElement`] | None
   :param type: Filter Type, (optional)

      - ``FILL``
        Fill -- Fill with a specific color.
      - ``HUE``
        Hue -- Change hue.
      - ``SATURATION``
        Saturation -- Change saturation.
      - ``VALUE``
        Value -- Change value.
      - ``BRIGHTNESS``
        Brightness -- Change brightness.
      - ``CONTRAST``
        Contrast -- Change contrast.
      - ``SMOOTH``
        Smooth -- Smooth colors.
      - ``RED``
        Red -- Change red channel.
      - ``GREEN``
        Green -- Change green channel.
      - ``BLUE``
        Blue -- Change blue channel.
   :type type: Literal['FILL', 'HUE', 'SATURATION', 'VALUE', 'BRIGHTNESS', 'CONTRAST', 'SMOOTH', 'RED', 'GREEN', 'BLUE']
   :param fill_color: Fill Color, (array of 3 items, in [0, inf], optional)
   :type fill_color: :class:`mathutils.Color` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: detail_flood_fill()

   Flood fill the mesh with the selected detail setting

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: dynamic_topology_toggle()

   Dynamic topology alters the mesh topology while sculpting

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: dyntopo_detail_size_edit()

   Modify the detail size of dyntopo interactively

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: expand(*, target='MASK', falloff_type='GEODESIC', invert=False, use_mask_preserve=False, use_falloff_gradient=False, use_modify_active=False, use_reposition_pivot=True, max_geodesic_move_preview=10000, use_auto_mask=False, normal_falloff_smooth=2)

   Generic sculpt expand operator

   :param target: Data Target, Data that is going to be modified in the expand operation (optional)
   :type target: Literal['MASK', 'FACE_SETS', 'COLOR']
   :param falloff_type: Falloff Type, Initial falloff of the expand operation (optional)
   :type falloff_type: Literal['GEODESIC', 'TOPOLOGY', 'TOPOLOGY_DIAGONALS', 'NORMALS', 'SPHERICAL', 'BOUNDARY_TOPOLOGY', 'BOUNDARY_FACE_SET', 'ACTIVE_FACE_SET']
   :param invert: Invert, Invert the expand active elements (optional)
   :type invert: bool
   :param use_mask_preserve: Preserve Previous, Preserve the previous state of the target data (optional)
   :type use_mask_preserve: bool
   :param use_falloff_gradient: Falloff Gradient, Expand Using a linear falloff (optional)
   :type use_falloff_gradient: bool
   :param use_modify_active: Modify Active, Modify the active face set instead of creating a new one (optional)
   :type use_modify_active: bool
   :param use_reposition_pivot: Reposition Pivot, Reposition the sculpt transform pivot to the boundary of the expand active area (optional)
   :type use_reposition_pivot: bool
   :param max_geodesic_move_preview: Max Vertex Count for Geodesic Move Preview, Maximum number of vertices in the mesh for using geodesic falloff when moving the origin of expand. If the total number of vertices is greater than this value, the falloff will be set to spherical when moving (in [0, inf], optional)
   :type max_geodesic_move_preview: int
   :param use_auto_mask: Auto Create, Fill in mask if nothing is already masked (optional)
   :type use_auto_mask: bool
   :param normal_falloff_smooth: Normal Smooth, Blurring steps for normal falloff (in [0, 10], optional)
   :type normal_falloff_smooth: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: face_set_box_gesture(*, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, use_front_faces_only=False)

   Add a face set in a rectangle defined by the cursor

   :param xmin: X Min, (in [-inf, inf], optional)
   :type xmin: int
   :param xmax: X Max, (in [-inf, inf], optional)
   :type xmax: int
   :param ymin: Y Min, (in [-inf, inf], optional)
   :type ymin: int
   :param ymax: Y Max, (in [-inf, inf], optional)
   :type ymax: int
   :param wait_for_input: Wait for Input, (optional)
   :type wait_for_input: bool
   :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view (optional)
   :type use_front_faces_only: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: face_set_change_visibility(*, mode='TOGGLE', active_face_set=0)

   Change the visibility of the face sets of the sculpt

   :param mode: Mode, (optional)

      - ``TOGGLE``
        Toggle Visibility -- Hide all face sets except for the active one.
      - ``SHOW_ACTIVE``
        Show Active Face Set -- Show the active face set.
      - ``HIDE_ACTIVE``
        Hide Active Face Set -- Hide the active face set.
   :type mode: Literal['TOGGLE', 'SHOW_ACTIVE', 'HIDE_ACTIVE']
   :param active_face_set: Active Face Set, (in [0, inf], optional)
   :type active_face_set: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: face_set_edit(*, active_face_set=1, mode='GROW', strength=1.0, modify_hidden=False)

   Edits the current active face set

   :param active_face_set: Active Face Set, (in [0, inf], optional)
   :type active_face_set: int
   :param mode: Mode, (optional)

      - ``GROW``
        Grow Face Set -- Grows the face set boundary by one face based on mesh topology.
      - ``SHRINK``
        Shrink Face Set -- Shrinks the face set boundary by one face based on mesh topology.
      - ``DELETE_GEOMETRY``
        Delete Geometry -- Deletes the faces that are assigned to the face set.
      - ``FAIR_POSITIONS``
        Fair Positions -- Creates the smoothest possible geometry patch from the face set minimizing changes in vertex positions.
      - ``FAIR_TANGENCY``
        Fair Tangency -- Creates the smoothest possible geometry patch from the face set minimizing changes in vertex tangents.
   :type mode: Literal['GROW', 'SHRINK', 'DELETE_GEOMETRY', 'FAIR_POSITIONS', 'FAIR_TANGENCY']
   :param strength: Strength, (in [0, 1], optional)
   :type strength: float
   :param modify_hidden: Modify Hidden, Apply the edit operation to hidden geometry (optional)
   :type modify_hidden: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: face_set_extract(*, add_boundary_loop=True, smooth_iterations=4, apply_shrinkwrap=True, add_solidify=True)

   Create a new mesh object from the selected face set

   :param add_boundary_loop: Add Boundary Loop, Add an extra edge loop to better preserve the shape when applying a subdivision surface modifier (optional)
   :type add_boundary_loop: bool
   :param smooth_iterations: Smooth Iterations, Smooth iterations applied to the extracted mesh (in [0, inf], optional)
   :type smooth_iterations: int
   :param apply_shrinkwrap: Project to Sculpt, Project the extracted mesh into the original sculpt (optional)
   :type apply_shrinkwrap: bool
   :param add_solidify: Extract as Solid, Extract the mask as a solid object with a solidify modifier (optional)
   :type add_solidify: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: face_set_lasso_gesture(*, path=None, use_smooth_stroke=False, smooth_stroke_factor=0.75, smooth_stroke_radius=35, use_front_faces_only=False)

   Add a face set in a shape defined by the cursor

   :param path: Path, (optional)
   :type path: :class:`bpy_prop_collection`\ [:class:`OperatorMousePath`] | None
   :param use_smooth_stroke: Stabilize Stroke, Selection lags behind mouse and follows a smoother path (optional)
   :type use_smooth_stroke: bool
   :param smooth_stroke_factor: Smooth Stroke Factor, Higher values give a smoother stroke (in [0.5, 0.99], optional)
   :type smooth_stroke_factor: float
   :param smooth_stroke_radius: Smooth Stroke Radius, Minimum distance from last point before selection continues (in [10, 200], optional)
   :type smooth_stroke_radius: int
   :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view (optional)
   :type use_front_faces_only: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: face_set_line_gesture(*, xstart=0, xend=0, ystart=0, yend=0, flip=False, cursor=5, use_front_faces_only=False, use_limit_to_segment=False)

   Add a face set to one side of a line defined by the cursor

   :param xstart: X Start, (in [-inf, inf], optional)
   :type xstart: int
   :param xend: X End, (in [-inf, inf], optional)
   :type xend: int
   :param ystart: Y Start, (in [-inf, inf], optional)
   :type ystart: int
   :param yend: Y End, (in [-inf, inf], optional)
   :type yend: int
   :param flip: Flip, (optional)
   :type flip: bool
   :param cursor: Cursor, Mouse cursor style to use during the modal operator (in [0, inf], optional)
   :type cursor: int
   :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view (optional)
   :type use_front_faces_only: bool
   :param use_limit_to_segment: Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line (optional)
   :type use_limit_to_segment: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: face_set_polyline_gesture(*, path=None, use_front_faces_only=False)

   Add a face set in a shape defined by the cursor

   :param path: Path, (optional)
   :type path: :class:`bpy_prop_collection`\ [:class:`OperatorMousePath`] | None
   :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view (optional)
   :type use_front_faces_only: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: face_sets_create(*, mode='MASKED')

   Create a new face set

   :param mode: Mode, (optional)

      - ``MASKED``
        Face Set from Masked -- Create a new face set from the masked faces.
      - ``VISIBLE``
        Face Set from Visible -- Create a new face set from the visible vertices.
      - ``ALL``
        Face Set Full Mesh -- Create a unique face set with all faces in the sculpt.
      - ``SELECTION``
        Face Set from Edit Mode Selection -- Create a face set corresponding to the Edit Mode face selection.
   :type mode: Literal['MASKED', 'VISIBLE', 'ALL', 'SELECTION']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: face_sets_init(*, mode='LOOSE_PARTS', threshold=0.5)

   Initializes all face sets in the mesh

   :param mode: Mode, (optional)

      - ``LOOSE_PARTS``
        Face Sets from Loose Parts -- Create a face set per loose part in the mesh.
      - ``MATERIALS``
        Face Sets from Material Slots -- Create a face set per material slot.
      - ``NORMALS``
        Face Sets from Mesh Normals -- Create face sets for faces that have similar normal.
      - ``UV_SEAMS``
        Face Sets from UV Seams -- Create face sets using UV seams as boundaries.
      - ``CREASES``
        Face Sets from Edge Creases -- Create face sets using edge creases as boundaries.
      - ``BEVEL_WEIGHT``
        Face Sets from Bevel Weight -- Create face sets using bevel weights as boundaries.
      - ``SHARP_EDGES``
        Face Sets from Sharp Edges -- Create face sets using sharp edges as boundaries.
      - ``FACE_SET_BOUNDARIES``
        Face Sets from Face Set Boundaries -- Create a face set per isolated face set.
   :type mode: Literal['LOOSE_PARTS', 'MATERIALS', 'NORMALS', 'UV_SEAMS', 'CREASES', 'BEVEL_WEIGHT', 'SHARP_EDGES', 'FACE_SET_BOUNDARIES']
   :param threshold: Threshold, Minimum value to consider a certain attribute a boundary when creating the face sets (in [0, 1], optional)
   :type threshold: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: face_sets_randomize_colors()

   Generates a new set of random colors to render the face sets in the viewport

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: mask_by_color(*, contiguous=False, invert=False, preserve_previous_mask=False, threshold=0.35, location=(0, 0))

   Creates a mask based on the active color attribute

   :param contiguous: Contiguous, Mask only contiguous color areas (optional)
   :type contiguous: bool
   :param invert: Invert, Invert the generated mask (optional)
   :type invert: bool
   :param preserve_previous_mask: Preserve Previous Mask, Preserve the previous mask and add or subtract the new one generated by the colors (optional)
   :type preserve_previous_mask: bool
   :param threshold: Threshold, How much changes in color affect the mask generation (in [0, 1], optional)
   :type threshold: float
   :param location: Location, Region coordinates of sampling (array of 2 items, in [0, 32767], optional)
   :type location: Sequence[int]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: mask_filter(*, filter_type='SMOOTH', iterations=1, auto_iteration_count=True)

   Applies a filter to modify the current mask

   :param filter_type: Type, Filter that is going to be applied to the mask (optional)
   :type filter_type: Literal['SMOOTH', 'SHARPEN', 'GROW', 'SHRINK', 'CONTRAST_INCREASE', 'CONTRAST_DECREASE']
   :param iterations: Iterations, Number of times that the filter is going to be applied (in [1, 100], optional)
   :type iterations: int
   :param auto_iteration_count: Auto Iteration Count, Use an automatic number of iterations based on the number of vertices of the sculpt (optional)
   :type auto_iteration_count: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: mask_from_boundary(*, mix_mode='MIX', mix_factor=1.0, settings_source='OPERATOR', boundary_mode='MESH', propagation_steps=1)

   Creates a mask based on the boundaries of the surface

   :param mix_mode: Mode, Mix mode (optional)
   :type mix_mode: Literal['MIX', 'MULTIPLY', 'DIVIDE', 'ADD', 'SUBTRACT']
   :param mix_factor: Mix Factor, (in [0, 5], optional)
   :type mix_factor: float
   :param settings_source: Settings, Use settings from here (optional)

      - ``OPERATOR``
        Operator -- Use settings from operator properties.
      - ``BRUSH``
        Brush -- Use settings from brush.
      - ``SCENE``
        Scene -- Use settings from scene.
   :type settings_source: Literal['OPERATOR', 'BRUSH', 'SCENE']
   :param boundary_mode: Mode, Boundary type to mask (optional)

      - ``MESH``
        Mesh -- Calculate the boundary mask based on disconnected mesh topology islands.
      - ``FACE_SETS``
        Face Sets -- Calculate the boundary mask between face sets.
   :type boundary_mode: Literal['MESH', 'FACE_SETS']
   :param propagation_steps: Propagation Steps, (in [1, 20], optional)
   :type propagation_steps: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: mask_from_cavity(*, mix_mode='MIX', mix_factor=1.0, settings_source='OPERATOR', factor=0.5, blur_steps=2, use_curve=False, invert=False)

   Creates a mask based on the curvature of the surface

   :param mix_mode: Mode, Mix mode (optional)
   :type mix_mode: Literal['MIX', 'MULTIPLY', 'DIVIDE', 'ADD', 'SUBTRACT']
   :param mix_factor: Mix Factor, (in [0, 5], optional)
   :type mix_factor: float
   :param settings_source: Settings, Use settings from here (optional)

      - ``OPERATOR``
        Operator -- Use settings from operator properties.
      - ``BRUSH``
        Brush -- Use settings from brush.
      - ``SCENE``
        Scene -- Use settings from scene.
   :type settings_source: Literal['OPERATOR', 'BRUSH', 'SCENE']
   :param factor: Factor, The contrast of the cavity mask (in [0, 5], optional)
   :type factor: float
   :param blur_steps: Blur, The number of times the cavity mask is blurred (in [0, 25], optional)
   :type blur_steps: int
   :param use_curve: Custom Curve, (optional)
   :type use_curve: bool
   :param invert: Cavity (Inverted), (optional)
   :type invert: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: mask_init(*, mode='RANDOM_PER_VERTEX')

   Creates a new mask for the entire mesh

   :param mode: Mode, (optional)
   :type mode: Literal['RANDOM_PER_VERTEX', 'RANDOM_PER_FACE_SET', 'RANDOM_PER_LOOSE_PART']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: mesh_filter(*, start_mouse=(0, 0), area_normal_radius=0.25, strength=1.0, iteration_count=1, event_history=None, type='INFLATE', deform_axis={'X', 'Y', 'Z'}, orientation='LOCAL', surface_smooth_shape_preservation=0.5, surface_smooth_current_vertex=0.5, sharpen_smooth_ratio=0.35, sharpen_intensify_detail_strength=0.0, sharpen_curvature_smooth_iterations=0)

   Applies a filter to modify the current mesh

   :param start_mouse: Starting Mouse, (array of 2 items, in [0, 16384], optional)
   :type start_mouse: Sequence[int]
   :param area_normal_radius: Normal Radius, Radius used for calculating area normal on initial click,in percentage of brush radius(in [0.001, 5], optional)
   :type area_normal_radius: float
   :param strength: Strength, Filter strength (in [-10, 10], optional)
   :type strength: float
   :param iteration_count: Repeat, How many times to repeat the filter (in [1, 10000], optional)
   :type iteration_count: int
   :param event_history: (optional)
   :type event_history: :class:`bpy_prop_collection`\ [:class:`OperatorStrokeElement`] | None
   :param type: Filter Type, Operation that is going to be applied to the mesh (optional)

      - ``SMOOTH``
        Smooth -- Smooth mesh.
      - ``SCALE``
        Scale -- Scale mesh.
      - ``INFLATE``
        Inflate -- Inflate mesh.
      - ``SPHERE``
        Sphere -- Morph into sphere.
      - ``RANDOM``
        Random -- Randomize vertex positions.
      - ``RELAX``
        Relax -- Relax mesh.
      - ``RELAX_FACE_SETS``
        Relax Face Sets -- Smooth the edges of all the face sets.
      - ``SURFACE_SMOOTH``
        Surface Smooth -- Smooth the surface of the mesh, preserving the volume.
      - ``SHARPEN``
        Sharpen -- Sharpen the cavities of the mesh.
      - ``ENHANCE_DETAILS``
        Enhance Details -- Enhance the high frequency surface detail.
      - ``ERASE_DISPLACEMENT``
        Erase Displacement -- Deletes the displacement of the Multires Modifier.
   :type type: Literal['SMOOTH', 'SCALE', 'INFLATE', 'SPHERE', 'RANDOM', 'RELAX', 'RELAX_FACE_SETS', 'SURFACE_SMOOTH', 'SHARPEN', 'ENHANCE_DETAILS', 'ERASE_DISPLACEMENT']
   :param deform_axis: Deform Axis, Apply the deformation in the selected axis (optional)

      - ``X``
        X -- Deform in the X axis.
      - ``Y``
        Y -- Deform in the Y axis.
      - ``Z``
        Z -- Deform in the Z axis.
   :type deform_axis: set[Literal['X', 'Y', 'Z']]
   :param orientation: Orientation, Orientation of the axis to limit the filter displacement (optional)

      - ``LOCAL``
        Local -- Use the local axis to limit the displacement.
      - ``WORLD``
        World -- Use the global axis to limit the displacement.
      - ``VIEW``
        View -- Use the view axis to limit the displacement.
   :type orientation: Literal['LOCAL', 'WORLD', 'VIEW']
   :param surface_smooth_shape_preservation: Shape Preservation, How much of the original shape is preserved when smoothing (in [0, 1], optional)
   :type surface_smooth_shape_preservation: float
   :param surface_smooth_current_vertex: Per Vertex Displacement, How much the position of each individual vertex influences the final result (in [0, 1], optional)
   :type surface_smooth_current_vertex: float
   :param sharpen_smooth_ratio: Smooth Ratio, How much smoothing is applied to polished surfaces (in [0, 1], optional)
   :type sharpen_smooth_ratio: float
   :param sharpen_intensify_detail_strength: Intensify Details, How much creases and valleys are intensified (in [0, 10], optional)
   :type sharpen_intensify_detail_strength: float
   :param sharpen_curvature_smooth_iterations: Curvature Smooth Iterations, How much smooth the resulting shape is, ignoring high frequency details (in [0, 10], optional)
   :type sharpen_curvature_smooth_iterations: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: optimize()

   Recalculate the sculpt BVH to improve performance

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: paint_mask_extract(*, mask_threshold=0.5, add_boundary_loop=True, smooth_iterations=4, apply_shrinkwrap=True, add_solidify=True)

   Create a new mesh object from the current paint mask

   :param mask_threshold: Threshold, Minimum mask value to consider the vertex valid to extract a face from the original mesh (in [0, 1], optional)
   :type mask_threshold: float
   :param add_boundary_loop: Add Boundary Loop, Add an extra edge loop to better preserve the shape when applying a subdivision surface modifier (optional)
   :type add_boundary_loop: bool
   :param smooth_iterations: Smooth Iterations, Smooth iterations applied to the extracted mesh (in [0, inf], optional)
   :type smooth_iterations: int
   :param apply_shrinkwrap: Project to Sculpt, Project the extracted mesh into the original sculpt (optional)
   :type apply_shrinkwrap: bool
   :param add_solidify: Extract as Solid, Extract the mask as a solid object with a solidify modifier (optional)
   :type add_solidify: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: paint_mask_slice(*, mask_threshold=0.5, fill_holes=True, new_object=True)

   Slices the paint mask from the mesh

   :param mask_threshold: Threshold, Minimum mask value to consider the vertex valid to extract a face from the original mesh (in [0, 1], optional)
   :type mask_threshold: float
   :param fill_holes: Fill Holes, Fill holes after slicing the mask (optional)
   :type fill_holes: bool
   :param new_object: Slice to New Object, Create a new object from the sliced mask (optional)
   :type new_object: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: project_line_gesture(*, xstart=0, xend=0, ystart=0, yend=0, flip=False, cursor=5, use_front_faces_only=False, use_limit_to_segment=False)

   Project the geometry onto a plane defined by a line

   :param xstart: X Start, (in [-inf, inf], optional)
   :type xstart: int
   :param xend: X End, (in [-inf, inf], optional)
   :type xend: int
   :param ystart: Y Start, (in [-inf, inf], optional)
   :type ystart: int
   :param yend: Y End, (in [-inf, inf], optional)
   :type yend: int
   :param flip: Flip, (optional)
   :type flip: bool
   :param cursor: Cursor, Mouse cursor style to use during the modal operator (in [0, inf], optional)
   :type cursor: int
   :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view (optional)
   :type use_front_faces_only: bool
   :param use_limit_to_segment: Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line (optional)
   :type use_limit_to_segment: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: sample_detail_size(*, location=(0, 0), mode='DYNTOPO')

   Sample the mesh detail on clicked point

   :param location: Location, Screen coordinates of sampling (array of 2 items, in [0, 32767], optional)
   :type location: Sequence[int]
   :param mode: Detail Mode, Target sculpting workflow that is going to use the sampled size (optional)

      - ``DYNTOPO``
        Dyntopo -- Sample dyntopo detail.
      - ``VOXEL``
        Voxel -- Sample mesh voxel size.
   :type mode: Literal['DYNTOPO', 'VOXEL']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: sculptmode_toggle()

   Toggle sculpt mode in 3D view

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: set_persistent_base()

   Reset the copy of the mesh that is being sculpted on

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: set_pivot_position(*, mode='UNMASKED', mouse_x=0.0, mouse_y=0.0)

   Sets the sculpt transform pivot position

   :param mode: Mode, (optional)

      - ``ORIGIN``
        Origin -- Sets the pivot to the origin of the sculpt.
      - ``UNMASKED``
        Unmasked -- Sets the pivot position to the average position of the unmasked vertices.
      - ``BORDER``
        Mask Border -- Sets the pivot position to the center of the border of the mask.
      - ``ACTIVE``
        Active Vertex -- Sets the pivot position to the active vertex position.
      - ``SURFACE``
        Surface -- Sets the pivot position to the surface under the cursor.
   :type mode: Literal['ORIGIN', 'UNMASKED', 'BORDER', 'ACTIVE', 'SURFACE']
   :param mouse_x: Mouse Position X, Position of the mouse used for "Surface" and "Active Vertex" mode (in [0, inf], optional)
   :type mouse_x: float
   :param mouse_y: Mouse Position Y, Position of the mouse used for "Surface" and "Active Vertex" mode (in [0, inf], optional)
   :type mouse_y: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: symmetrize(*, merge_tolerance=0.0005)

   Symmetrize the topology modifications

   :param merge_tolerance: Merge Distance, Distance within which symmetrical vertices are merged (in [0, inf], optional)
   :type merge_tolerance: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: trim_box_gesture(*, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, use_front_faces_only=False, location=(0, 0), trim_mode='DIFFERENCE', use_cursor_depth=False, trim_orientation='VIEW', trim_extrude_mode='FIXED', trim_solver='MANIFOLD')

   Execute a boolean operation on the mesh and a rectangle defined by the cursor

   :param xmin: X Min, (in [-inf, inf], optional)
   :type xmin: int
   :param xmax: X Max, (in [-inf, inf], optional)
   :type xmax: int
   :param ymin: Y Min, (in [-inf, inf], optional)
   :type ymin: int
   :param ymax: Y Max, (in [-inf, inf], optional)
   :type ymax: int
   :param wait_for_input: Wait for Input, (optional)
   :type wait_for_input: bool
   :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view (optional)
   :type use_front_faces_only: bool
   :param location: Location, Mouse location (array of 2 items, in [-inf, inf], optional)
   :type location: Sequence[int]
   :param trim_mode: Trim Mode, (optional)

      - ``DIFFERENCE``
        Difference -- Use a difference boolean operation.
      - ``UNION``
        Union -- Use a union boolean operation.
      - ``JOIN``
        Join -- Join the new mesh as separate geometry, without performing any boolean operation.
   :type trim_mode: Literal['DIFFERENCE', 'UNION', 'JOIN']
   :param use_cursor_depth: Use Cursor for Depth, Use cursor location and radius for the dimensions and position of the trimming shape (optional)
   :type use_cursor_depth: bool
   :param trim_orientation: Shape Orientation, (optional)

      - ``VIEW``
        View -- Use the view to orientate the trimming shape.
      - ``SURFACE``
        Surface -- Use the surface normal to orientate the trimming shape.
   :type trim_orientation: Literal['VIEW', 'SURFACE']
   :param trim_extrude_mode: Extrude Mode, (optional)

      - ``PROJECT``
        Project -- Align trim geometry with the perspective of the current view for a tapered shape.
      - ``FIXED``
        Fixed -- Align trim geometry orthogonally for a shape with 90 degree angles.
   :type trim_extrude_mode: Literal['PROJECT', 'FIXED']
   :param trim_solver: Solver, (optional)

      - ``EXACT``
        Exact -- Slower solver with the best results for coplanar faces.
      - ``FLOAT``
        Float -- Simple solver with good performance, without support for overlapping geometry.
      - ``MANIFOLD``
        Manifold -- Fastest solver that works only on manifold meshes but gives better results.
   :type trim_solver: Literal['EXACT', 'FLOAT', 'MANIFOLD']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: trim_lasso_gesture(*, path=None, use_smooth_stroke=False, smooth_stroke_factor=0.75, smooth_stroke_radius=35, use_front_faces_only=False, location=(0, 0), trim_mode='DIFFERENCE', use_cursor_depth=False, trim_orientation='VIEW', trim_extrude_mode='FIXED', trim_solver='MANIFOLD')

   Execute a boolean operation on the mesh and a shape defined by the cursor

   :param path: Path, (optional)
   :type path: :class:`bpy_prop_collection`\ [:class:`OperatorMousePath`] | None
   :param use_smooth_stroke: Stabilize Stroke, Selection lags behind mouse and follows a smoother path (optional)
   :type use_smooth_stroke: bool
   :param smooth_stroke_factor: Smooth Stroke Factor, Higher values give a smoother stroke (in [0.5, 0.99], optional)
   :type smooth_stroke_factor: float
   :param smooth_stroke_radius: Smooth Stroke Radius, Minimum distance from last point before selection continues (in [10, 200], optional)
   :type smooth_stroke_radius: int
   :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view (optional)
   :type use_front_faces_only: bool
   :param location: Location, Mouse location (array of 2 items, in [-inf, inf], optional)
   :type location: Sequence[int]
   :param trim_mode: Trim Mode, (optional)

      - ``DIFFERENCE``
        Difference -- Use a difference boolean operation.
      - ``UNION``
        Union -- Use a union boolean operation.
      - ``JOIN``
        Join -- Join the new mesh as separate geometry, without performing any boolean operation.
   :type trim_mode: Literal['DIFFERENCE', 'UNION', 'JOIN']
   :param use_cursor_depth: Use Cursor for Depth, Use cursor location and radius for the dimensions and position of the trimming shape (optional)
   :type use_cursor_depth: bool
   :param trim_orientation: Shape Orientation, (optional)

      - ``VIEW``
        View -- Use the view to orientate the trimming shape.
      - ``SURFACE``
        Surface -- Use the surface normal to orientate the trimming shape.
   :type trim_orientation: Literal['VIEW', 'SURFACE']
   :param trim_extrude_mode: Extrude Mode, (optional)

      - ``PROJECT``
        Project -- Align trim geometry with the perspective of the current view for a tapered shape.
      - ``FIXED``
        Fixed -- Align trim geometry orthogonally for a shape with 90 degree angles.
   :type trim_extrude_mode: Literal['PROJECT', 'FIXED']
   :param trim_solver: Solver, (optional)

      - ``EXACT``
        Exact -- Slower solver with the best results for coplanar faces.
      - ``FLOAT``
        Float -- Simple solver with good performance, without support for overlapping geometry.
      - ``MANIFOLD``
        Manifold -- Fastest solver that works only on manifold meshes but gives better results.
   :type trim_solver: Literal['EXACT', 'FLOAT', 'MANIFOLD']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: trim_line_gesture(*, xstart=0, xend=0, ystart=0, yend=0, flip=False, cursor=5, use_front_faces_only=False, use_limit_to_segment=False, location=(0, 0), trim_mode='DIFFERENCE', use_cursor_depth=False, trim_orientation='VIEW', trim_extrude_mode='FIXED', trim_solver='MANIFOLD')

   Remove a portion of the mesh on one side of a line

   :param xstart: X Start, (in [-inf, inf], optional)
   :type xstart: int
   :param xend: X End, (in [-inf, inf], optional)
   :type xend: int
   :param ystart: Y Start, (in [-inf, inf], optional)
   :type ystart: int
   :param yend: Y End, (in [-inf, inf], optional)
   :type yend: int
   :param flip: Flip, (optional)
   :type flip: bool
   :param cursor: Cursor, Mouse cursor style to use during the modal operator (in [0, inf], optional)
   :type cursor: int
   :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view (optional)
   :type use_front_faces_only: bool
   :param use_limit_to_segment: Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line (optional)
   :type use_limit_to_segment: bool
   :param location: Location, Mouse location (array of 2 items, in [-inf, inf], optional)
   :type location: Sequence[int]
   :param trim_mode: Trim Mode, (optional)

      - ``DIFFERENCE``
        Difference -- Use a difference boolean operation.
      - ``UNION``
        Union -- Use a union boolean operation.
      - ``JOIN``
        Join -- Join the new mesh as separate geometry, without performing any boolean operation.
   :type trim_mode: Literal['DIFFERENCE', 'UNION', 'JOIN']
   :param use_cursor_depth: Use Cursor for Depth, Use cursor location and radius for the dimensions and position of the trimming shape (optional)
   :type use_cursor_depth: bool
   :param trim_orientation: Shape Orientation, (optional)

      - ``VIEW``
        View -- Use the view to orientate the trimming shape.
      - ``SURFACE``
        Surface -- Use the surface normal to orientate the trimming shape.
   :type trim_orientation: Literal['VIEW', 'SURFACE']
   :param trim_extrude_mode: Extrude Mode, (optional)

      - ``PROJECT``
        Project -- Align trim geometry with the perspective of the current view for a tapered shape.
      - ``FIXED``
        Fixed -- Align trim geometry orthogonally for a shape with 90 degree angles.
   :type trim_extrude_mode: Literal['PROJECT', 'FIXED']
   :param trim_solver: Solver, (optional)

      - ``EXACT``
        Exact -- Slower solver with the best results for coplanar faces.
      - ``FLOAT``
        Float -- Simple solver with good performance, without support for overlapping geometry.
      - ``MANIFOLD``
        Manifold -- Fastest solver that works only on manifold meshes but gives better results.
   :type trim_solver: Literal['EXACT', 'FLOAT', 'MANIFOLD']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: trim_polyline_gesture(*, path=None, use_front_faces_only=False, location=(0, 0), trim_mode='DIFFERENCE', use_cursor_depth=False, trim_orientation='VIEW', trim_extrude_mode='FIXED', trim_solver='MANIFOLD')

   Execute a boolean operation on the mesh and a polygonal shape defined by the cursor

   :param path: Path, (optional)
   :type path: :class:`bpy_prop_collection`\ [:class:`OperatorMousePath`] | None
   :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view (optional)
   :type use_front_faces_only: bool
   :param location: Location, Mouse location (array of 2 items, in [-inf, inf], optional)
   :type location: Sequence[int]
   :param trim_mode: Trim Mode, (optional)

      - ``DIFFERENCE``
        Difference -- Use a difference boolean operation.
      - ``UNION``
        Union -- Use a union boolean operation.
      - ``JOIN``
        Join -- Join the new mesh as separate geometry, without performing any boolean operation.
   :type trim_mode: Literal['DIFFERENCE', 'UNION', 'JOIN']
   :param use_cursor_depth: Use Cursor for Depth, Use cursor location and radius for the dimensions and position of the trimming shape (optional)
   :type use_cursor_depth: bool
   :param trim_orientation: Shape Orientation, (optional)

      - ``VIEW``
        View -- Use the view to orientate the trimming shape.
      - ``SURFACE``
        Surface -- Use the surface normal to orientate the trimming shape.
   :type trim_orientation: Literal['VIEW', 'SURFACE']
   :param trim_extrude_mode: Extrude Mode, (optional)

      - ``PROJECT``
        Project -- Align trim geometry with the perspective of the current view for a tapered shape.
      - ``FIXED``
        Fixed -- Align trim geometry orthogonally for a shape with 90 degree angles.
   :type trim_extrude_mode: Literal['PROJECT', 'FIXED']
   :param trim_solver: Solver, (optional)

      - ``EXACT``
        Exact -- Slower solver with the best results for coplanar faces.
      - ``FLOAT``
        Float -- Simple solver with good performance, without support for overlapping geometry.
      - ``MANIFOLD``
        Manifold -- Fastest solver that works only on manifold meshes but gives better results.
   :type trim_solver: Literal['EXACT', 'FLOAT', 'MANIFOLD']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: uv_sculpt_grab(*, use_invert=False)

   Grab UVs

   :param use_invert: Invert, Invert action for the duration of the stroke (optional)
   :type use_invert: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: uv_sculpt_pinch(*, use_invert=False)

   Pinch UVs

   :param use_invert: Invert, Invert action for the duration of the stroke (optional)
   :type use_invert: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: uv_sculpt_relax(*, use_invert=False, relax_method='LAPLACIAN')

   Relax UVs

   :param use_invert: Invert, Invert action for the duration of the stroke (optional)
   :type use_invert: bool
   :param relax_method: Relax Method, Algorithm used for UV relaxation (optional)

      - ``LAPLACIAN``
        Laplacian -- Use Laplacian method for relaxation.
      - ``HC``
        HC -- Use HC method for relaxation.
      - ``COTAN``
        Geometry -- Use Geometry (cotangent) relaxation, making UVs follow the underlying 3D geometry.
   :type relax_method: Literal['LAPLACIAN', 'HC', 'COTAN']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

