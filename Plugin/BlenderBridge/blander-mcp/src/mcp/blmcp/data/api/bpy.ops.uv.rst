Uv Operators
============

.. module:: bpy.ops.uv

.. function:: align(*, axis='ALIGN_AUTO', position_mode='MEAN')

   Aligns selected UV vertices on a line

   :param axis: Axis, Axis to align UV locations on (optional)

      - ``ALIGN_S``
        Straighten -- Align UV vertices along the line defined by the endpoints.
      - ``ALIGN_T``
        Straighten X -- Align UV vertices, moving them horizontally to the line defined by the endpoints.
      - ``ALIGN_U``
        Straighten Y -- Align UV vertices, moving them vertically to the line defined by the endpoints.
      - ``ALIGN_AUTO``
        Align Auto -- Automatically choose the direction on which there is most alignment already.
      - ``ALIGN_X``
        Align Vertically -- Align UV vertices on a vertical line.
      - ``ALIGN_Y``
        Align Horizontally -- Align UV vertices on a horizontal line.
   :type axis: Literal['ALIGN_S', 'ALIGN_T', 'ALIGN_U', 'ALIGN_AUTO', 'ALIGN_X', 'ALIGN_Y']
   :param position_mode: Position Mode, Method of calculating the alignment position (optional)

      - ``MEAN``
        Mean -- Align UVs along the mean position.
      - ``MIN``
        Minimum -- Align UVs along the minimum position.
      - ``MAX``
        Maximum -- Align UVs along the maximum position.
   :type position_mode: Literal['MEAN', 'MIN', 'MAX']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: align_rotation(*, method='AUTO', axis='X', correct_aspect=False)

   Align the UV island's rotation

   :param method: Method, Method to calculate rotation angle (optional)

      - ``AUTO``
        Auto -- Align from all edges.
      - ``EDGE``
        Edge -- Only selected edges.
      - ``GEOMETRY``
        Geometry -- Align to Geometry axis.
   :type method: Literal['AUTO', 'EDGE', 'GEOMETRY']
   :param axis: Axis, Axis to align to (optional)

      - ``X``
        X -- X axis.
      - ``Y``
        Y -- Y axis.
      - ``Z``
        Z -- Z axis.
   :type axis: Literal['X', 'Y', 'Z']
   :param correct_aspect: Correct Aspect, Take image aspect ratio into account (optional)
   :type correct_aspect: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/uvcalc_transform.py\:360 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/uvcalc_transform.py#L360>`__


.. function:: arrange_islands(*, initial_position='BOUNDING_BOX', axis='Y', align='MIN', order='LARGE_TO_SMALL', margin=0.05)

   Arrange selected UV islands on a line

   :param initial_position: Initial Position, Initial position to arrange islands from (optional)

      - ``BOUNDING_BOX``
        Bounding Box -- Initial alignment based on the islands bounding box.
      - ``UV_GRID``
        UV Grid -- Initial alignment based on UV Tile Grid.
      - ``ACTIVE_UDIM``
        Active UDIM -- Initial alignment based on Active UDIM.
      - ``CURSOR``
        2D Cursor -- Initial alignment based on 2D cursor.
   :type initial_position: Literal['BOUNDING_BOX', 'UV_GRID', 'ACTIVE_UDIM', 'CURSOR']
   :param axis: Axis, Axis to arrange UV islands on (optional)

      - ``X``
        X -- Align UV islands along the X axis.
      - ``Y``
        Y -- Align UV islands along the Y axis.
   :type axis: Literal['X', 'Y']
   :param align: Align, Location to align islands on (optional)

      - ``MIN``
        Min -- Align the islands to the min of the island.
      - ``MAX``
        Max -- Align the islands to the max side of the island.
      - ``CENTER``
        Center -- Align the islands to the center of the largest island.
      - ``NONE``
        None -- Preserve island alignment.
   :type align: Literal['MIN', 'MAX', 'CENTER', 'NONE']
   :param order: Order, Order of islands (optional)

      - ``LARGE_TO_SMALL``
        Largest to Smallest -- Sort islands from largest to smallest.
      - ``SMALL_TO_LARGE``
        Smallest to Largest -- Sort islands from smallest to largest.
      - ``Fixed``
        Fixed -- Preserve island order.
   :type order: Literal['LARGE_TO_SMALL', 'SMALL_TO_LARGE', 'Fixed']
   :param margin: Margin, Space between islands (in [0, 1], optional)
   :type margin: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: average_islands_scale(*, scale_uv=False, shear=False)

   Average the size of separate UV islands, based on their area in 3D space

   :param scale_uv: Non-Uniform, Scale U and V independently (optional)
   :type scale_uv: bool
   :param shear: Shear, Reduce shear within islands (optional)
   :type shear: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: copy()

   Copy selected UV vertices

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: copy_mirrored_faces(*, direction='POSITIVE', precision=3)

   Copy mirror UV coordinates on the X axis based on a mirrored mesh

   :param direction: Axis Direction, (optional)
   :type direction: Literal['POSITIVE', 'NEGATIVE']
   :param precision: Precision, Tolerance for finding vertex duplicates (in [1, 16], optional)
   :type precision: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: cube_project(*, cube_size=1.0, correct_aspect=True, clip_to_bounds=False, scale_to_bounds=False)

   Project the UV vertices of the mesh over the six faces of a cube

   :param cube_size: Cube Size, Size of the cube to project on (in [0, inf], optional)
   :type cube_size: float
   :param correct_aspect: Correct Aspect, Map UVs taking aspect ratio of the image associated with the material into account (optional)
   :type correct_aspect: bool
   :param clip_to_bounds: Clip to Bounds, Clip UV coordinates to bounds after unwrapping (optional)
   :type clip_to_bounds: bool
   :param scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping (optional)
   :type scale_to_bounds: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: cursor_set(*, location=(0.0, 0.0))

   Set 2D cursor location

   :param location: Location, Cursor location in normalized (0.0 to 1.0) coordinates (array of 2 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: custom_region_set(*, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True)

   Set the boundaries of the user region

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
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: cylinder_project(*, direction='VIEW_ON_EQUATOR', align='POLAR_ZX', pole='PINCH', seam=False, radius=1.0, correct_aspect=True, clip_to_bounds=False, scale_to_bounds=False)

   Project the UV vertices of the mesh over the curved wall of a cylinder

   :param direction: Direction, Direction of the sphere or cylinder (optional)

      - ``VIEW_ON_EQUATOR``
        View on Equator -- 3D view is on the equator.
      - ``VIEW_ON_POLES``
        View on Poles -- 3D view is on the poles.
      - ``ALIGN_TO_OBJECT``
        Align to Object -- Align according to object transform.
   :type direction: Literal['VIEW_ON_EQUATOR', 'VIEW_ON_POLES', 'ALIGN_TO_OBJECT']
   :param align: Align, How to determine rotation around the pole (optional)

      - ``POLAR_ZX``
        Polar ZX -- Polar 0 is X.
      - ``POLAR_ZY``
        Polar ZY -- Polar 0 is Y.
   :type align: Literal['POLAR_ZX', 'POLAR_ZY']
   :param pole: Pole, How to handle faces at the poles (optional)

      - ``PINCH``
        Pinch -- UVs are pinched at the poles.
      - ``FAN``
        Fan -- UVs are fanned at the poles.
   :type pole: Literal['PINCH', 'FAN']
   :param seam: Preserve Seams, Separate projections by islands isolated by seams (optional)
   :type seam: bool
   :param radius: Radius, Radius of the sphere or cylinder (in [0, inf], optional)
   :type radius: float
   :param correct_aspect: Correct Aspect, Map UVs taking aspect ratio of the image associated with the material into account (optional)
   :type correct_aspect: bool
   :param clip_to_bounds: Clip to Bounds, Clip UV coordinates to bounds after unwrapping (optional)
   :type clip_to_bounds: bool
   :param scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping (optional)
   :type scale_to_bounds: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: export_layout(*, filepath="", export_all=False, export_tiles='NONE', modified=False, mode='PNG', size=(1024, 1024), opacity=0.25, check_existing=True)

   Export UV layout to file

   :param filepath: filepath, (optional, never None)
   :type filepath: str
   :param export_all: All UVs, Export all UVs in this mesh (not just visible ones) (optional)
   :type export_all: bool
   :param export_tiles: Export Tiles, Choose whether to export only the [0, 1] range, or all UV tiles (optional)

      - ``NONE``
        None -- Export only UVs in the [0, 1] range.
      - ``UDIM``
        UDIM -- Export tiles in the UDIM numbering scheme: 1001 + u_tile + 10\*v_tile.
      - ``UV``
        UVTILE -- Export tiles in the UVTILE numbering scheme: u(u_tile + 1)_v(v_tile + 1).
   :type export_tiles: Literal['NONE', 'UDIM', 'UV']
   :param modified: Modified, Exports UVs from the modified mesh (optional)
   :type modified: bool
   :param mode: Format, File format to export the UV layout to (optional)

      - ``SVG``
        Scalable Vector Graphic (.svg) -- Export the UV layout to a vector SVG file.
      - ``EPS``
        Encapsulated PostScript (.eps) -- Export the UV layout to a vector EPS file.
      - ``PNG``
        PNG Image (.png) -- Export the UV layout to a bitmap image.
   :type mode: Literal['SVG', 'EPS', 'PNG']
   :param size: Size, Dimensions of the exported file (array of 2 items, in [8, 32768], optional)
   :type size: Sequence[int]
   :param opacity: Fill Opacity, Set amount of opacity for exported UV layout (in [0, 1], optional)
   :type opacity: float
   :param check_existing: check_existing, (optional)
   :type check_existing: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `addons_core/io_mesh_uv_layout/__init__.py\:139 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/io_mesh_uv_layout/__init__.py#L139>`__


.. function:: follow_active_quads(*, mode='LENGTH_AVERAGE')

   Follow UVs from active quads along continuous face loops

   :param mode: Edge Length Mode, Method to space UV edge loops (optional)

      - ``EVEN``
        Even -- Space all UVs evenly.
      - ``LENGTH``
        Length -- Average space UVs edge length of each loop.
      - ``LENGTH_AVERAGE``
        Length Average -- Average space UVs edge length of each loop.
   :type mode: Literal['EVEN', 'LENGTH', 'LENGTH_AVERAGE']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/uvcalc_follow_active.py\:302 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/uvcalc_follow_active.py#L302>`__


.. function:: hide(*, unselected=False)

   Hide (un)selected UV vertices

   :param unselected: Unselected, Hide unselected rather than selected (optional)
   :type unselected: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: lightmap_pack(*, PREF_CONTEXT='SEL_FACES', PREF_PACK_IN_ONE=True, PREF_NEW_UVLAYER=False, PREF_BOX_DIV=12, PREF_MARGIN_DIV=0.1)

   Pack each face's UVs into the UV bounds

   :param PREF_CONTEXT: Selection, (optional)

      - ``SEL_FACES``
        Selected Faces -- Pack only selected faces.
      - ``ALL_FACES``
        All Faces -- Pack all faces in the mesh.
   :type PREF_CONTEXT: Literal['SEL_FACES', 'ALL_FACES']
   :param PREF_PACK_IN_ONE: Share Texture Space, Objects share texture space, map all objects into a single UV map (optional)
   :type PREF_PACK_IN_ONE: bool
   :param PREF_NEW_UVLAYER: New UV Map, Create a new UV map for every mesh packed (optional)
   :type PREF_NEW_UVLAYER: bool
   :param PREF_BOX_DIV: Pack Quality, Quality of the packing. Higher values will be slower but waste less space (in [1, 48], optional)
   :type PREF_BOX_DIV: int
   :param PREF_MARGIN_DIV: Margin, Size of the margin as a division of the UV (in [0.001, 1], optional)
   :type PREF_MARGIN_DIV: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/uvcalc_lightmap.py\:664 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/uvcalc_lightmap.py#L664>`__


.. function:: mark_seam(*, clear=False)

   Mark selected UV edges as seams

   :param clear: Clear Seams, Clear instead of marking seams (optional)
   :type clear: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: minimize_stretch(*, fill_holes=True, blend=0.0, iterations=0)

   Reduce UV stretching by relaxing angles

   :param fill_holes: Fill Holes, Virtually fill holes in mesh before unwrapping, to better avoid overlaps and preserve symmetry (optional)
   :type fill_holes: bool
   :param blend: Blend, Blend factor between stretch minimized and original (in [0, 1], optional)
   :type blend: float
   :param iterations: Iterations, Number of iterations to run, 0 is unlimited when run interactively (in [0, inf], optional)
   :type iterations: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: move_on_axis(*, type='UDIM', axis='X', distance=1)

   Move UVs on an axis

   :param type: Type, Move Type (optional)

      - ``DYNAMIC``
        Dynamic -- Move by dynamic grid.
      - ``PIXEL``
        Pixel -- Move by pixel.
      - ``UDIM``
        UDIM -- Move by UDIM.
   :type type: Literal['DYNAMIC', 'PIXEL', 'UDIM']
   :param axis: Axis, Axis to move UVs on (optional)

      - ``X``
        X axis -- Move vertices on the X axis.
      - ``Y``
        Y axis -- Move vertices on the Y axis.
   :type axis: Literal['X', 'Y']
   :param distance: Distance, Distance to move UVs (in [-inf, inf], optional)
   :type distance: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: pack_islands(*, udim_source='CLOSEST_UDIM', rotate=True, rotate_method='ANY', scale=True, merge_overlap=False, margin_method='SCALED', margin=0.001, pin=False, pin_method='LOCKED', shape_method='CONCAVE')

   Transform all islands so that they fill up the UV/UDIM space as much as possible

   :param udim_source: Pack to, (optional)

      - ``CLOSEST_UDIM``
        Closest UDIM -- Pack islands to closest UDIM.
      - ``ACTIVE_UDIM``
        Active UDIM -- Pack islands to active UDIM image tile or UDIM grid tile where 2D cursor is located.
      - ``ORIGINAL_AABB``
        Original bounding box -- Pack to starting bounding box of islands.
      - ``CUSTOM_REGION``
        Custom Region -- Pack islands to custom region.
   :type udim_source: Literal['CLOSEST_UDIM', 'ACTIVE_UDIM', 'ORIGINAL_AABB', 'CUSTOM_REGION']
   :param rotate: Rotate, Rotate islands to improve layout (optional)
   :type rotate: bool
   :param rotate_method: Rotation Method, (optional)

      - ``ANY``
        Any -- Any angle is allowed for rotation.
      - ``CARDINAL``
        Cardinal -- Only 90 degree rotations are allowed.
      - ``AXIS_ALIGNED``
        Axis-aligned -- Rotated to a minimal rectangle, either vertical or horizontal.
      - ``AXIS_ALIGNED_X``
        Axis-aligned (Horizontal) -- Rotate islands to be aligned horizontally.
      - ``AXIS_ALIGNED_Y``
        Axis-aligned (Vertical) -- Rotate islands to be aligned vertically.
   :type rotate_method: Literal['ANY', 'CARDINAL', 'AXIS_ALIGNED', 'AXIS_ALIGNED_X', 'AXIS_ALIGNED_Y']
   :param scale: Scale, Scale islands to fill unit square (optional)
   :type scale: bool
   :param merge_overlap: Merge Overlapping, Overlapping islands stick together (optional)
   :type merge_overlap: bool
   :param margin_method: Margin Method, (optional)

      - ``SCALED``
        Scaled -- Use scale of existing UVs to multiply margin.
      - ``ADD``
        Add -- Just add the margin, ignoring any UV scale.
      - ``FRACTION``
        Fraction -- Specify a precise fraction of final UV output.
   :type margin_method: Literal['SCALED', 'ADD', 'FRACTION']
   :param margin: Margin, Space between islands (in [0, 1], optional)
   :type margin: float
   :param pin: Lock Pinned Islands, Constrain islands containing any pinned UV's (optional)
   :type pin: bool
   :param pin_method: Pin Method, (optional)

      - ``SCALE``
        Scale -- Pinned islands won't rescale.
      - ``ROTATION``
        Rotation -- Pinned islands won't rotate.
      - ``ROTATION_SCALE``
        Rotation and Scale -- Pinned islands will translate only.
      - ``LOCKED``
        All -- Pinned islands are locked in place.
   :type pin_method: Literal['SCALE', 'ROTATION', 'ROTATION_SCALE', 'LOCKED']
   :param shape_method: Shape Method, (optional)

      - ``CONCAVE``
        Exact Shape (Concave) -- Uses exact geometry.
      - ``CONVEX``
        Boundary Shape (Convex) -- Uses convex hull.
      - ``AABB``
        Bounding Box -- Uses bounding boxes.
   :type shape_method: Literal['CONCAVE', 'CONVEX', 'AABB']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: paste()

   Paste selected UV vertices

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: pin(*, clear=False, invert=False)

   Set/clear selected UV vertices as anchored between multiple unwrap operations

   :param clear: Clear, Clear pinning for the selection instead of setting it (optional)
   :type clear: bool
   :param invert: Invert, Invert pinning for the selection instead of setting it (optional)
   :type invert: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: project_from_view(*, orthographic=False, camera_bounds=True, correct_aspect=True, clip_to_bounds=False, scale_to_bounds=False)

   Project the UV vertices of the mesh as seen in current 3D view

   :param orthographic: Orthographic, Use orthographic projection (optional)
   :type orthographic: bool
   :param camera_bounds: Camera Bounds, Map UVs to the camera region taking resolution and aspect into account (optional)
   :type camera_bounds: bool
   :param correct_aspect: Correct Aspect, Map UVs taking aspect ratio of the image associated with the material into account (optional)
   :type correct_aspect: bool
   :param clip_to_bounds: Clip to Bounds, Clip UV coordinates to bounds after unwrapping (optional)
   :type clip_to_bounds: bool
   :param scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping (optional)
   :type scale_to_bounds: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: randomize_uv_transform(*, random_seed=0, use_loc=True, loc=(0.0, 0.0), use_rot=True, rot=0.0, use_scale=True, scale_even=False, scale=(1.0, 1.0))

   Randomize the UV island's location, rotation, and scale

   :param random_seed: Random Seed, Seed value for the random generator (in [0, 10000], optional)
   :type random_seed: int
   :param use_loc: Randomize Location, Randomize the location values (optional)
   :type use_loc: bool
   :param loc: Location, Maximum distance the objects can spread over each axis (array of 2 items, in [-100, 100], optional)
   :type loc: :class:`mathutils.Vector` | Sequence[float]
   :param use_rot: Randomize Rotation, Randomize the rotation value (optional)
   :type use_rot: bool
   :param rot: Rotation, Maximum rotation (in [-6.28319, 6.28319], optional)
   :type rot: float
   :param use_scale: Randomize Scale, Randomize the scale values (optional)
   :type use_scale: bool
   :param scale_even: Scale Even, Use the same scale value for both axes (optional)
   :type scale_even: bool
   :param scale: Scale, Maximum scale randomization over each axis (array of 2 items, in [-100, 100], optional)
   :type scale: Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/uvcalc_transform.py\:536 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/uvcalc_transform.py#L536>`__


.. function:: remove_doubles(*, threshold=0.02, use_unselected=False, use_shared_vertex=False)

   Selected UV vertices that are within a radius of each other are welded together

   :param threshold: Merge Distance, Maximum distance between welded vertices (in [0, 10], optional)
   :type threshold: float
   :param use_unselected: Unselected, Merge selected to other unselected vertices (optional)
   :type use_unselected: bool
   :param use_shared_vertex: Shared Vertex, Weld UVs based on shared vertices (optional)
   :type use_shared_vertex: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: reset()

   Reset UV projection

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: reveal(*, select=True)

   Reveal all hidden UV vertices

   :param select: Select, (optional)
   :type select: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: rip(*, mirror=False, release_confirm=False, use_accurate=False, location=(0.0, 0.0))

   Rip selected vertices or a selected region

   :param mirror: Mirror Editing, (optional)
   :type mirror: bool
   :param release_confirm: Confirm on Release, Always confirm operation when releasing button (optional)
   :type release_confirm: bool
   :param use_accurate: Accurate, Use accurate transformation (optional)
   :type use_accurate: bool
   :param location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds (array of 2 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: rip_move(*, UV_OT_rip={}, TRANSFORM_OT_translate={})

   Unstitch UVs and move the result

   :param UV_OT_rip: UV Rip, Rip selected vertices or a selected region (optional, :func:`bpy.ops.uv.rip` keyword arguments)
   :type UV_OT_rip: dict[str, Any]
   :param TRANSFORM_OT_translate: Move, Move selected items (optional, :func:`bpy.ops.transform.translate` keyword arguments)
   :type TRANSFORM_OT_translate: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: seams_from_islands(*, mark_seams=True, mark_sharp=False)

   Set mesh seams according to island setup in the UV editor

   :param mark_seams: Mark Seams, Mark boundary edges as seams (optional)
   :type mark_seams: bool
   :param mark_sharp: Mark Sharp, Mark boundary edges as sharp (optional)
   :type mark_sharp: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select(*, extend=False, deselect=False, toggle=False, deselect_all=False, select_passthrough=False, location=(0.0, 0.0))

   Select UV vertices

   :param extend: Extend, Extend selection instead of deselecting everything first (optional)
   :type extend: bool
   :param deselect: Deselect, Remove from selection (optional)
   :type deselect: bool
   :param toggle: Toggle Selection, Toggle the selection (optional)
   :type toggle: bool
   :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor (optional)
   :type deselect_all: bool
   :param select_passthrough: Only Select Unselected, Ignore the select action when the element is already selected (optional)
   :type select_passthrough: bool
   :param location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds (array of 2 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_all(*, action='TOGGLE')

   Change selection of all UV vertices

   :param action: Action, Selection action to execute (optional)

      - ``TOGGLE``
        Toggle -- Toggle selection for all elements.
      - ``SELECT``
        Select -- Select all elements.
      - ``DESELECT``
        Deselect -- Deselect all elements.
      - ``INVERT``
        Invert -- Invert selection of all elements.
   :type action: Literal['TOGGLE', 'SELECT', 'DESELECT', 'INVERT']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_box(*, pinned=False, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, mode='SET')

   Select UV vertices using box selection

   :param pinned: Pinned, Border select pinned UVs only (optional)
   :type pinned: bool
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
   :param mode: Mode, (optional)

      - ``SET``
        Set -- Set a new selection.
      - ``ADD``
        Extend -- Extend existing selection.
      - ``SUB``
        Subtract -- Subtract existing selection.
   :type mode: Literal['SET', 'ADD', 'SUB']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_circle(*, x=0, y=0, radius=25, wait_for_input=True, mode='SET')

   Select UV vertices using circle selection

   :param x: X, (in [-inf, inf], optional)
   :type x: int
   :param y: Y, (in [-inf, inf], optional)
   :type y: int
   :param radius: Radius, (in [1, inf], optional)
   :type radius: int
   :param wait_for_input: Wait for Input, (optional)
   :type wait_for_input: bool
   :param mode: Mode, (optional)

      - ``SET``
        Set -- Set a new selection.
      - ``ADD``
        Extend -- Extend existing selection.
      - ``SUB``
        Subtract -- Subtract existing selection.
   :type mode: Literal['SET', 'ADD', 'SUB']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_edge_ring(*, extend=False, location=(0.0, 0.0))

   Select an edge ring of connected UV vertices

   :param extend: Extend, Extend selection rather than clearing the existing selection (optional)
   :type extend: bool
   :param location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds (array of 2 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_lasso(*, path=None, use_smooth_stroke=False, smooth_stroke_factor=0.75, smooth_stroke_radius=35, mode='SET')

   Select UVs using lasso selection

   :param path: Path, (optional)
   :type path: :class:`bpy_prop_collection`\ [:class:`OperatorMousePath`] | None
   :param use_smooth_stroke: Stabilize Stroke, Selection lags behind mouse and follows a smoother path (optional)
   :type use_smooth_stroke: bool
   :param smooth_stroke_factor: Smooth Stroke Factor, Higher values give a smoother stroke (in [0.5, 0.99], optional)
   :type smooth_stroke_factor: float
   :param smooth_stroke_radius: Smooth Stroke Radius, Minimum distance from last point before selection continues (in [10, 200], optional)
   :type smooth_stroke_radius: int
   :param mode: Mode, (optional)

      - ``SET``
        Set -- Set a new selection.
      - ``ADD``
        Extend -- Extend existing selection.
      - ``SUB``
        Subtract -- Subtract existing selection.
   :type mode: Literal['SET', 'ADD', 'SUB']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_less()

   Deselect UV vertices at the boundary of each selection region

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select_linked()

   Select all UV vertices linked to the active UV map

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select_linked_pick(*, extend=False, deselect=False, location=(0.0, 0.0))

   Select all UV vertices linked under the mouse

   :param extend: Extend, Extend selection rather than clearing the existing selection (optional)
   :type extend: bool
   :param deselect: Deselect, Deselect linked UV vertices rather than selecting them (optional)
   :type deselect: bool
   :param location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds (array of 2 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_loop(*, extend=False, location=(0.0, 0.0))

   Select a loop of connected UV vertices

   :param extend: Extend, Extend selection rather than clearing the existing selection (optional)
   :type extend: bool
   :param location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds (array of 2 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_mode(*, type='VERTEX')

   Change UV selection mode

   :param type: Type, (optional)
   :type type: Literal[:ref:`rna_enum_mesh_select_mode_uv_items`]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_more()

   Select more UV vertices connected to initial selection

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select_overlap(*, extend=False)

   Select all UV faces which overlap each other

   :param extend: Extend, Extend selection rather than clearing the existing selection (optional)
   :type extend: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_pinned()

   Select all pinned UV vertices

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select_similar(*, type='PIN', compare='EQUAL', threshold=0.0)

   Select similar UVs by property types

   :param type: Type, (optional)

      - ``PIN``
        Pinned.
      - ``LENGTH``
        Length -- Edge length in UV space.
      - ``LENGTH_3D``
        Length 3D -- Length of edge in 3D space.
      - ``AREA``
        Area -- Face area in UV space.
      - ``AREA_3D``
        Area 3D -- Area of face in 3D space.
      - ``MATERIAL``
        Material.
      - ``OBJECT``
        Object.
      - ``SIDES``
        Polygon Sides.
      - ``WINDING``
        Winding -- Face direction defined by clockwise or anti-clockwise winding (facing up or facing down).
      - ``FACE``
        Amount of Faces in Island.
   :type type: Literal['PIN', 'LENGTH', 'LENGTH_3D', 'AREA', 'AREA_3D', 'MATERIAL', 'OBJECT', 'SIDES', 'WINDING', 'FACE']
   :param compare: Compare, (optional)
   :type compare: Literal['EQUAL', 'GREATER', 'LESS']
   :param threshold: Threshold, (in [0, 1], optional)
   :type threshold: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_split()

   Select only entirely selected faces

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select_tile(*, extend=False, tile=(0, 0))

   Select UVs in specified tile

   :param extend: Extend, Extend the selection (optional)
   :type extend: bool
   :param tile: Tile, Tile location to select UVs (array of 2 items, in [-inf, inf], optional)
   :type tile: Sequence[int]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: shortest_path_pick(*, use_face_step=False, use_topology_distance=False, use_fill=False, skip=0, nth=1, offset=0, object_index=-1, index=-1)

   Select shortest path between two selections

   :param use_face_step: Face Stepping, Traverse connected faces (includes diagonals and edge-rings) (optional)
   :type use_face_step: bool
   :param use_topology_distance: Topology Distance, Find the minimum number of steps, ignoring spatial distance (optional)
   :type use_topology_distance: bool
   :param use_fill: Fill Region, Select all paths between the source/destination elements (optional)
   :type use_fill: bool
   :param skip: Deselected, Number of deselected elements in the repetitive sequence (in [0, inf], optional)
   :type skip: int
   :param nth: Selected, Number of selected elements in the repetitive sequence (in [1, inf], optional)
   :type nth: int
   :param offset: Offset, Offset from the starting point (in [-inf, inf], optional)
   :type offset: int
   :param object_index: (in [-1, inf], optional)
   :type object_index: int
   :param index: (in [-1, inf], optional)
   :type index: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: shortest_path_select(*, use_face_step=False, use_topology_distance=False, use_fill=False, skip=0, nth=1, offset=0)

   Select shortest path between two vertices/edges/faces

   :param use_face_step: Face Stepping, Traverse connected faces (includes diagonals and edge-rings) (optional)
   :type use_face_step: bool
   :param use_topology_distance: Topology Distance, Find the minimum number of steps, ignoring spatial distance (optional)
   :type use_topology_distance: bool
   :param use_fill: Fill Region, Select all paths between the source/destination elements (optional)
   :type use_fill: bool
   :param skip: Deselected, Number of deselected elements in the repetitive sequence (in [0, inf], optional)
   :type skip: int
   :param nth: Selected, Number of selected elements in the repetitive sequence (in [1, inf], optional)
   :type nth: int
   :param offset: Offset, Offset from the starting point (in [-inf, inf], optional)
   :type offset: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: smart_project(*, angle_limit=1.15192, margin_method='SCALED', rotate_method='AXIS_ALIGNED_Y', island_margin=0.0, area_weight=0.0, correct_aspect=True, scale_to_bounds=False)

   Projection unwraps the selected faces of mesh objects

   :param angle_limit: Angle Limit, Lower for more projection groups, higher for less distortion (in [0, 1.5708], optional)
   :type angle_limit: float
   :param margin_method: Margin Method, (optional)

      - ``SCALED``
        Scaled -- Use scale of existing UVs to multiply margin.
      - ``ADD``
        Add -- Just add the margin, ignoring any UV scale.
      - ``FRACTION``
        Fraction -- Specify a precise fraction of final UV output.
   :type margin_method: Literal['SCALED', 'ADD', 'FRACTION']
   :param rotate_method: Rotation Method, (optional)

      - ``AXIS_ALIGNED``
        Axis-aligned -- Rotated to a minimal rectangle, either vertical or horizontal.
      - ``AXIS_ALIGNED_X``
        Axis-aligned (Horizontal) -- Rotate islands to be aligned horizontally.
      - ``AXIS_ALIGNED_Y``
        Axis-aligned (Vertical) -- Rotate islands to be aligned vertically.
   :type rotate_method: Literal['AXIS_ALIGNED', 'AXIS_ALIGNED_X', 'AXIS_ALIGNED_Y']
   :param island_margin: Island Margin, Margin to reduce bleed from adjacent islands (in [0, 1], optional)
   :type island_margin: float
   :param area_weight: Area Weight, Weight projection's vector by faces with larger areas (in [0, 1], optional)
   :type area_weight: float
   :param correct_aspect: Correct Aspect, Map UVs taking aspect ratio of the image associated with the material into account (optional)
   :type correct_aspect: bool
   :param scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping (optional)
   :type scale_to_bounds: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: snap_cursor(*, target='PIXELS')

   Snap cursor to target type

   :param target: Target, Target to snap the selected UVs to (optional)
   :type target: Literal['PIXELS', 'SELECTED', 'ORIGIN']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: snap_selected(*, target='PIXELS')

   Snap selected UV vertices to target type

   :param target: Target, Target to snap the selected UVs to (optional)
   :type target: Literal['PIXELS', 'CURSOR', 'CURSOR_OFFSET', 'ADJACENT_UNSELECTED']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: sphere_project(*, direction='VIEW_ON_EQUATOR', align='POLAR_ZX', pole='PINCH', seam=False, correct_aspect=True, clip_to_bounds=False, scale_to_bounds=False)

   Project the UV vertices of the mesh over the curved surface of a sphere

   :param direction: Direction, Direction of the sphere or cylinder (optional)

      - ``VIEW_ON_EQUATOR``
        View on Equator -- 3D view is on the equator.
      - ``VIEW_ON_POLES``
        View on Poles -- 3D view is on the poles.
      - ``ALIGN_TO_OBJECT``
        Align to Object -- Align according to object transform.
   :type direction: Literal['VIEW_ON_EQUATOR', 'VIEW_ON_POLES', 'ALIGN_TO_OBJECT']
   :param align: Align, How to determine rotation around the pole (optional)

      - ``POLAR_ZX``
        Polar ZX -- Polar 0 is X.
      - ``POLAR_ZY``
        Polar ZY -- Polar 0 is Y.
   :type align: Literal['POLAR_ZX', 'POLAR_ZY']
   :param pole: Pole, How to handle faces at the poles (optional)

      - ``PINCH``
        Pinch -- UVs are pinched at the poles.
      - ``FAN``
        Fan -- UVs are fanned at the poles.
   :type pole: Literal['PINCH', 'FAN']
   :param seam: Preserve Seams, Separate projections by islands isolated by seams (optional)
   :type seam: bool
   :param correct_aspect: Correct Aspect, Map UVs taking aspect ratio of the image associated with the material into account (optional)
   :type correct_aspect: bool
   :param clip_to_bounds: Clip to Bounds, Clip UV coordinates to bounds after unwrapping (optional)
   :type clip_to_bounds: bool
   :param scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping (optional)
   :type scale_to_bounds: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: stitch(*, use_limit=False, snap_islands=True, limit=0.01, static_island=0, active_object_index=0, midpoint_snap=False, clear_seams=True, mode='VERTEX', stored_mode='VERTEX', selection=None, objects_selection_count=(0, 0, 0, 0, 0, 0))

   Stitch selected UV vertices by proximity

   :param use_limit: Use Limit, Stitch UVs within a specified limit distance (optional)
   :type use_limit: bool
   :param snap_islands: Snap Islands, Snap islands together (on edge stitch mode, rotates the islands too) (optional)
   :type snap_islands: bool
   :param limit: Limit, Limit distance in normalized coordinates (in [0, inf], optional)
   :type limit: float
   :param static_island: Static Island, Island that stays in place when stitching islands (in [0, inf], optional)
   :type static_island: int
   :param active_object_index: Active Object, Index of the active object (in [0, inf], optional)
   :type active_object_index: int
   :param midpoint_snap: Snap at Midpoint, UVs are stitched at midpoint instead of at static island (optional)
   :type midpoint_snap: bool
   :param clear_seams: Clear Seams, Clear seams of stitched edges (optional)
   :type clear_seams: bool
   :param mode: Operation Mode, Use vertex or edge stitching (optional)
   :type mode: Literal['VERTEX', 'EDGE']
   :param stored_mode: Stored Operation Mode, Use vertex or edge stitching (optional)
   :type stored_mode: Literal['VERTEX', 'EDGE']
   :param selection: Selection, (optional)
   :type selection: :class:`bpy_prop_collection`\ [:class:`SelectedUvElement`] | None
   :param objects_selection_count: Objects Selection Count, (array of 6 items, in [0, inf], optional)
   :type objects_selection_count: Sequence[int]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: unwrap(*, method='CONFORMAL', fill_holes=False, correct_aspect=True, use_subsurf_data=False, margin_method='SCALED', margin=0.001, no_flip=False, iterations=10, use_weights=False, weight_group="uv_importance", weight_factor=1.0)

   Unwrap the mesh of the object being edited

   :param method: Method, Unwrapping method (Angle Based usually gives better results than Conformal, while being somewhat slower) (optional)
   :type method: Literal['ANGLE_BASED', 'CONFORMAL', 'MINIMUM_STRETCH']
   :param fill_holes: Fill Holes, Virtually fill holes in mesh before unwrapping, to better avoid overlaps and preserve symmetry (optional)
   :type fill_holes: bool
   :param correct_aspect: Correct Aspect, Map UVs taking aspect ratio of the image associated with the material into account (optional)
   :type correct_aspect: bool
   :param use_subsurf_data: Use Subdivision Surface, Map UVs taking vertex position after Subdivision Surface modifier has been applied (optional)
   :type use_subsurf_data: bool
   :param margin_method: Margin Method, (optional)

      - ``SCALED``
        Scaled -- Use scale of existing UVs to multiply margin.
      - ``ADD``
        Add -- Just add the margin, ignoring any UV scale.
      - ``FRACTION``
        Fraction -- Specify a precise fraction of final UV output.
   :type margin_method: Literal['SCALED', 'ADD', 'FRACTION']
   :param margin: Margin, Space between islands (in [0, 1], optional)
   :type margin: float
   :param no_flip: No Flip, Prevent flipping UV's, flipping may lower distortion depending on the position of pins (optional)
   :type no_flip: bool
   :param iterations: Iterations, Number of iterations when "Minimum Stretch" method is used (in [0, 10000], optional)
   :type iterations: int
   :param use_weights: Importance Weights, Whether to take into account per-vertex importance weights (optional)
   :type use_weights: bool
   :param weight_group: Weight Group, Vertex group name for importance weights (modulating the deform) (optional, never None)
   :type weight_group: str
   :param weight_factor: Weight Factor, How much influence the weightmap has for weighted parameterization, 0 being no influence (in [-10000, 10000], optional)
   :type weight_factor: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: weld()

   Weld selected UV vertices together

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
