Mesh Operators
==============

.. module:: bpy.ops.mesh

.. function:: attribute_set(*, value_float=0.0, value_float_vector_2d=(0.0, 0.0), value_float_vector_3d=(0.0, 0.0, 0.0), value_int=0, value_int_vector_2d=(0, 0), value_color=(1.0, 1.0, 1.0, 1.0), value_bool=False)

   Set values of the active attribute for selected elements

   :param value_float: Value, (in [-inf, inf], optional)
   :type value_float: float
   :param value_float_vector_2d: Value, (array of 2 items, in [-inf, inf], optional)
   :type value_float_vector_2d: Sequence[float]
   :param value_float_vector_3d: Value, (array of 3 items, in [-inf, inf], optional)
   :type value_float_vector_3d: Sequence[float]
   :param value_int: Value, (in [-inf, inf], optional)
   :type value_int: int
   :param value_int_vector_2d: Value, (array of 2 items, in [-inf, inf], optional)
   :type value_int_vector_2d: Sequence[int]
   :param value_color: Value, (array of 4 items, in [-inf, inf], optional)
   :type value_color: Sequence[float]
   :param value_bool: Value, (optional)
   :type value_bool: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: average_normals(*, average_type='CUSTOM_NORMAL', weight=50, threshold=0.01)

   Average custom normals of selected vertices

   :param average_type: Type, Averaging method (optional)

      - ``CUSTOM_NORMAL``
        Custom Normal -- Take average of vertex normals.
      - ``FACE_AREA``
        Face Area -- Set all vertex normals by face area.
      - ``CORNER_ANGLE``
        Corner Angle -- Set all vertex normals by corner angle.
   :type average_type: Literal['CUSTOM_NORMAL', 'FACE_AREA', 'CORNER_ANGLE']
   :param weight: Weight, Weight applied per face (in [1, 100], optional)
   :type weight: int
   :param threshold: Threshold, Threshold value for different weights to be considered equal (in [0, 10], optional)
   :type threshold: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: beautify_fill(*, angle_limit=3.14159)

   Rearrange some faces to try to get less degenerated geometry

   :param angle_limit: Max Angle, Angle limit (in [0, 3.14159], optional)
   :type angle_limit: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: bevel(*, offset_type='OFFSET', offset=0.0, profile_type='SUPERELLIPSE', offset_pct=0.0, segments=1, profile=0.5, affect='EDGES', clamp_overlap=False, loop_slide=True, mark_seam=False, mark_sharp=False, material=-1, harden_normals=False, face_strength_mode='NONE', miter_outer='SHARP', miter_inner='SHARP', spread=0.1, vmesh_method='ADJ', release_confirm=False)

   Cut into selected items at an angle to create bevel or chamfer

   :param offset_type: Width Type, The method for determining the size of the bevel (optional)

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
   :type offset_type: Literal['OFFSET', 'WIDTH', 'DEPTH', 'PERCENT', 'ABSOLUTE']
   :param offset: Width, Bevel amount (in [0, 1e+06], optional)
   :type offset: float
   :param profile_type: Profile Type, The type of shape used to rebuild a beveled section (optional)

      - ``SUPERELLIPSE``
        Superellipse -- The profile can be a concave or convex curve.
      - ``CUSTOM``
        Custom -- The profile can be any arbitrary path between its endpoints.
   :type profile_type: Literal['SUPERELLIPSE', 'CUSTOM']
   :param offset_pct: Width Percent, Bevel amount for percentage method (in [0, 100], optional)
   :type offset_pct: float
   :param segments: Segments, Segments for curved edge (in [1, 1000], optional)
   :type segments: int
   :param profile: Profile, Controls profile shape (0.5 = round) (in [0, 1], optional)
   :type profile: float
   :param affect: Affect, Affect edges or vertices (optional)

      - ``VERTICES``
        Vertices -- Affect only vertices.
      - ``EDGES``
        Edges -- Affect only edges.
   :type affect: Literal['VERTICES', 'EDGES']
   :param clamp_overlap: Clamp Overlap, Do not allow beveled edges/vertices to overlap each other (optional)
   :type clamp_overlap: bool
   :param loop_slide: Loop Slide, Prefer sliding along edges to even widths (optional)
   :type loop_slide: bool
   :param mark_seam: Mark Seams, Preserve seams along beveled edges (optional)
   :type mark_seam: bool
   :param mark_sharp: Mark Sharp, Preserve sharp edges along beveled edges (optional)
   :type mark_sharp: bool
   :param material: Material Index, Material for bevel faces (-1 means use adjacent faces) (in [-1, inf], optional)
   :type material: int
   :param harden_normals: Harden Normals, Match normals of new faces to adjacent faces (optional)
   :type harden_normals: bool
   :param face_strength_mode: Face Strength Mode, Whether to set face strength, and which faces to set face strength on (optional)

      - ``NONE``
        None -- Do not set face strength.
      - ``NEW``
        New -- Set face strength on new faces only.
      - ``AFFECTED``
        Affected -- Set face strength on new and modified faces only.
      - ``ALL``
        All -- Set face strength on all faces.
   :type face_strength_mode: Literal['NONE', 'NEW', 'AFFECTED', 'ALL']
   :param miter_outer: Outer Miter, Pattern to use for outside of miters (optional)

      - ``SHARP``
        Sharp -- Outside of miter is sharp.
      - ``PATCH``
        Patch -- Outside of miter is squared-off patch.
      - ``ARC``
        Arc -- Outside of miter is arc.
   :type miter_outer: Literal['SHARP', 'PATCH', 'ARC']
   :param miter_inner: Inner Miter, Pattern to use for inside of miters (optional)

      - ``SHARP``
        Sharp -- Inside of miter is sharp.
      - ``ARC``
        Arc -- Inside of miter is arc.
   :type miter_inner: Literal['SHARP', 'ARC']
   :param spread: Spread, Amount to spread arcs for arc inner miters (in [0, 1e+06], optional)
   :type spread: float
   :param vmesh_method: Vertex Mesh Method, The method to use to create meshes at intersections (optional)

      - ``ADJ``
        Grid Fill -- Default patterned fill.
      - ``CUTOFF``
        Cutoff -- A cutoff at each profile's end before the intersection.
   :type vmesh_method: Literal['ADJ', 'CUTOFF']
   :param release_confirm: Confirm on Release, (optional)
   :type release_confirm: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: bisect(*, plane_co=(0.0, 0.0, 0.0), plane_no=(0.0, 0.0, 0.0), use_fill=False, clear_inner=False, clear_outer=False, threshold=0.0001, xstart=0, xend=0, ystart=0, yend=0, flip=False, cursor=5)

   Cut geometry along a plane (click-drag to define plane)

   :param plane_co: Plane Point, A point on the plane (array of 3 items, in [-inf, inf], optional)
   :type plane_co: :class:`mathutils.Vector` | Sequence[float]
   :param plane_no: Plane Normal, The direction the plane points (array of 3 items, in [-1, 1], optional)
   :type plane_no: :class:`mathutils.Vector` | Sequence[float]
   :param use_fill: Fill, Fill in the cut (optional)
   :type use_fill: bool
   :param clear_inner: Clear Inner, Remove geometry behind the plane (optional)
   :type clear_inner: bool
   :param clear_outer: Clear Outer, Remove geometry in front of the plane (optional)
   :type clear_outer: bool
   :param threshold: Axis Threshold, Preserves the existing geometry along the cut plane (in [0, 10], optional)
   :type threshold: float
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
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: blend_from_shape(*, shape='', blend=1.0, add=True)

   Blend in shape from a shape key

   :param shape: Shape, Shape key to use for blending (optional)
   :type shape: str
   :param blend: Blend, Blending factor (in [-1000, 1000], optional)
   :type blend: float
   :param add: Add, Add rather than blend between shapes (optional)
   :type add: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: bridge_edge_loops(*, type='SINGLE', use_merge=False, merge_factor=0.5, twist_offset=0, number_cuts=0, interpolation='PATH', smoothness=1.0, profile_shape_factor=0.0, profile_shape='SMOOTH')

   Create a bridge of faces between two or more selected edge loops

   :param type: Connect Loops, Method of bridging multiple loops (optional)
   :type type: Literal['SINGLE', 'CLOSED', 'PAIRS']
   :param use_merge: Merge, Merge rather than creating faces (optional)
   :type use_merge: bool
   :param merge_factor: Merge Factor, (in [0, 1], optional)
   :type merge_factor: float
   :param twist_offset: Twist, Twist offset for closed loops (in [-1000, 1000], optional)
   :type twist_offset: int
   :param number_cuts: Number of Cuts, (in [0, 1000], optional)
   :type number_cuts: int
   :param interpolation: Interpolation, Interpolation method (optional)
   :type interpolation: Literal['LINEAR', 'PATH', 'SURFACE']
   :param smoothness: Smoothness, Smoothness factor (in [0, 1000], optional)
   :type smoothness: float
   :param profile_shape_factor: Profile Factor, How much intermediary new edges are shrunk/expanded (in [-1000, 1000], optional)
   :type profile_shape_factor: float
   :param profile_shape: Profile Shape, Shape of the profile (optional)
   :type profile_shape: Literal[:ref:`rna_enum_proportional_falloff_curve_only_items`]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: colors_reverse()

   Flip direction of face corner color attribute inside faces

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: colors_rotate(*, use_ccw=False)

   Rotate face corner color attribute inside faces

   :param use_ccw: Counter Clockwise, (optional)
   :type use_ccw: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: customdata_custom_splitnormals_add()

   Add a custom normals layer, if none exists yet

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: customdata_custom_splitnormals_clear()

   Remove the custom normals layer, if it exists

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: customdata_mask_clear()

   Clear vertex sculpt masking data from the mesh

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: customdata_skin_add()

   Add a vertex skin layer

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: customdata_skin_clear()

   Clear vertex skin layer

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: decimate(*, ratio=1.0, use_vertex_group=False, vertex_group_factor=1.0, invert_vertex_group=False, use_symmetry=False, symmetry_axis='Y')

   Simplify geometry by collapsing edges

   :param ratio: Ratio, (in [0, 1], optional)
   :type ratio: float
   :param use_vertex_group: Vertex Group, Use active vertex group as an influence (optional)
   :type use_vertex_group: bool
   :param vertex_group_factor: Weight, Vertex group strength (in [0, 1000], optional)
   :type vertex_group_factor: float
   :param invert_vertex_group: Invert, Invert vertex group influence (optional)
   :type invert_vertex_group: bool
   :param use_symmetry: Symmetry, Maintain symmetry on an axis (optional)
   :type use_symmetry: bool
   :param symmetry_axis: Axis, Axis of symmetry (optional)
   :type symmetry_axis: Literal[:ref:`rna_enum_axis_xyz_items`]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: delete(*, type='VERT')

   Delete selected vertices, edges or faces

   :param type: Type, Method used for deleting mesh data (optional)
   :type type: Literal['VERT', 'EDGE', 'FACE', 'EDGE_FACE', 'ONLY_FACE']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: delete_edgeloop(*, use_face_split=True)

   Delete an edge loop by merging the faces on each side

   :param use_face_split: Face Split, Split off face corners to maintain surrounding geometry (optional)
   :type use_face_split: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: delete_loose(*, use_verts=True, use_edges=True, use_faces=False)

   Delete loose vertices, edges or faces

   :param use_verts: Vertices, Remove loose vertices (optional)
   :type use_verts: bool
   :param use_edges: Edges, Remove loose edges (optional)
   :type use_edges: bool
   :param use_faces: Faces, Remove loose faces (optional)
   :type use_faces: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: dissolve_degenerate(*, threshold=0.0001)

   Dissolve zero area faces and zero length edges

   :param threshold: Merge Distance, Maximum distance between elements to merge (in [1e-06, 50], optional)
   :type threshold: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: dissolve_edges(*, use_verts=True, angle_threshold=3.14159, use_face_split=False)

   Dissolve edges, merging faces

   :param use_verts: Dissolve Vertices, Dissolve remaining vertices which connect to only two edges (optional)
   :type use_verts: bool
   :param angle_threshold: Angle Threshold, Remaining vertices which separate edge pairs are preserved if their edge angle exceeds this threshold. (in [0, 3.14159], optional)
   :type angle_threshold: float
   :param use_face_split: Face Split, Split off face corners to maintain surrounding geometry (optional)
   :type use_face_split: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: dissolve_faces(*, use_verts=False)

   Dissolve faces

   :param use_verts: Dissolve Vertices, Dissolve remaining vertices which connect to only two edges (optional)
   :type use_verts: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: dissolve_limited(*, angle_limit=0.0872665, use_dissolve_boundaries=False, delimit={'NORMAL'})

   Dissolve selected edges and vertices, limited by the angle of surrounding geometry

   :param angle_limit: Max Angle, Angle limit (in [0, 3.14159], optional)
   :type angle_limit: float
   :param use_dissolve_boundaries: All Boundaries, Dissolve all vertices in between face boundaries (optional)
   :type use_dissolve_boundaries: bool
   :param delimit: Delimit, Delimit dissolve operation (optional)
   :type delimit: set[Literal[:ref:`rna_enum_mesh_delimit_mode_items`]]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: dissolve_mode(*, use_verts=False, angle_threshold=3.14159, use_face_split=False, use_boundary_tear=False)

   Dissolve geometry based on the selection mode

   :param use_verts: Dissolve Vertices, Dissolve remaining vertices which connect to only two edges (optional)
   :type use_verts: bool
   :param angle_threshold: Angle Threshold, Remaining vertices which separate edge pairs are preserved if their edge angle exceeds this threshold. (in [0, 3.14159], optional)
   :type angle_threshold: float
   :param use_face_split: Face Split, Split off face corners to maintain surrounding geometry (optional)
   :type use_face_split: bool
   :param use_boundary_tear: Tear Boundary, Split off face corners instead of merging faces (optional)
   :type use_boundary_tear: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: dissolve_verts(*, use_face_split=False, use_boundary_tear=False)

   Dissolve vertices, merge edges and faces

   :param use_face_split: Face Split, Split off face corners to maintain surrounding geometry (optional)
   :type use_face_split: bool
   :param use_boundary_tear: Tear Boundary, Split off face corners instead of merging faces (optional)
   :type use_boundary_tear: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: dupli_extrude_cursor(*, rotate_source=True)

   Duplicate and extrude selected vertices, edges or faces towards the mouse cursor

   :param rotate_source: Rotate Source, Rotate initial selection giving better shape (optional)
   :type rotate_source: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: duplicate(*, mode=1)

   Duplicate selected vertices, edges or faces

   :param mode: Mode, (in [0, inf], optional)
   :type mode: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: duplicate_move(*, MESH_OT_duplicate={}, TRANSFORM_OT_translate={})

   Duplicate mesh and move

   :param MESH_OT_duplicate: Duplicate, Duplicate selected vertices, edges or faces (optional, :func:`bpy.ops.mesh.duplicate` keyword arguments)
   :type MESH_OT_duplicate: dict[str, Any]
   :param TRANSFORM_OT_translate: Move, Move selected items (optional, :func:`bpy.ops.transform.translate` keyword arguments)
   :type TRANSFORM_OT_translate: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: edge_collapse()

   Collapse isolated edge and face regions, merging data such as UVs and color attributes. This can collapse edge-rings as well as regions of connected faces into vertices

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: edge_face_add()

   Add an edge or face to selected

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: edge_rotate(*, use_ccw=False)

   Rotate selected edge or adjoining faces

   :param use_ccw: Counter Clockwise, (optional)
   :type use_ccw: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: edge_split(*, type='EDGE')

   Split selected edges so that each neighbor face gets its own copy

   :param type: Type, Method to use for splitting (optional)

      - ``EDGE``
        Faces by Edges -- Split faces along selected edges.
      - ``VERT``
        Faces & Edges by Vertices -- Split faces and edges connected to selected vertices.
   :type type: Literal['EDGE', 'VERT']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: edgering_select(*, delimit_edge_ring={'NGONS'}, extend=False, deselect=False, toggle=False, object_index=-1, edge_index=-1, vert_index=-1, face_index=-1)

   Select an edge ring

   :param delimit_edge_ring: Edge Ring Delimit, Delimit edge ring selection (optional)
   :type delimit_edge_ring: set[Literal[:ref:`rna_enum_mesh_walk_delimit_edge_ring_items`]]
   :param extend: Extend Select, Extend the selection (optional)
   :type extend: bool
   :param deselect: Deselect, Remove from the selection (optional)
   :type deselect: bool
   :param toggle: Toggle Select, Toggle the selection (optional)
   :type toggle: bool
   :param object_index: (in [-1, inf], optional)
   :type object_index: int
   :param edge_index: (in [-1, inf], optional)
   :type edge_index: int
   :param vert_index: (in [-1, inf], optional)
   :type vert_index: int
   :param face_index: (in [-1, inf], optional)
   :type face_index: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: edges_select_sharp(*, sharpness=0.523599)

   Select all sharp enough edges

   :param sharpness: Sharpness, (in [0.000174533, 3.14159], optional)
   :type sharpness: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: extrude_context(*, use_normal_flip=False, use_dissolve_ortho_edges=False, mirror=False)

   Extrude selection

   :param use_normal_flip: Flip Normals, (optional)
   :type use_normal_flip: bool
   :param use_dissolve_ortho_edges: Dissolve Orthogonal Edges, (optional)
   :type use_dissolve_ortho_edges: bool
   :param mirror: Mirror Editing, (optional)
   :type mirror: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: extrude_context_move(*, MESH_OT_extrude_context={}, TRANSFORM_OT_translate={})

   Extrude region together along the average normal

   :param MESH_OT_extrude_context: Extrude Context, Extrude selection (optional, :func:`bpy.ops.mesh.extrude_context` keyword arguments)
   :type MESH_OT_extrude_context: dict[str, Any]
   :param TRANSFORM_OT_translate: Move, Move selected items (optional, :func:`bpy.ops.transform.translate` keyword arguments)
   :type TRANSFORM_OT_translate: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: extrude_edges_indiv(*, use_normal_flip=False, mirror=False)

   Extrude individual edges only

   :param use_normal_flip: Flip Normals, (optional)
   :type use_normal_flip: bool
   :param mirror: Mirror Editing, (optional)
   :type mirror: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: extrude_edges_move(*, MESH_OT_extrude_edges_indiv={}, TRANSFORM_OT_translate={})

   Extrude edges and move result

   :param MESH_OT_extrude_edges_indiv: Extrude Only Edges, Extrude individual edges only (optional, :func:`bpy.ops.mesh.extrude_edges_indiv` keyword arguments)
   :type MESH_OT_extrude_edges_indiv: dict[str, Any]
   :param TRANSFORM_OT_translate: Move, Move selected items (optional, :func:`bpy.ops.transform.translate` keyword arguments)
   :type TRANSFORM_OT_translate: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: extrude_faces_indiv(*, mirror=False)

   Extrude individual faces only

   :param mirror: Mirror Editing, (optional)
   :type mirror: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: extrude_faces_move(*, MESH_OT_extrude_faces_indiv={}, TRANSFORM_OT_shrink_fatten={})

   Extrude each individual face separately along local normals

   :param MESH_OT_extrude_faces_indiv: Extrude Individual Faces, Extrude individual faces only (optional, :func:`bpy.ops.mesh.extrude_faces_indiv` keyword arguments)
   :type MESH_OT_extrude_faces_indiv: dict[str, Any]
   :param TRANSFORM_OT_shrink_fatten: Shrink/Fatten, Shrink/fatten selected vertices along normals (optional, :func:`bpy.ops.transform.shrink_fatten` keyword arguments)
   :type TRANSFORM_OT_shrink_fatten: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: extrude_manifold(*, MESH_OT_extrude_region={}, TRANSFORM_OT_translate={})

   Extrude, dissolves edges whose faces form a flat surface and intersect new edges

   :param MESH_OT_extrude_region: Extrude Region, Extrude region of faces (optional, :func:`bpy.ops.mesh.extrude_region` keyword arguments)
   :type MESH_OT_extrude_region: dict[str, Any]
   :param TRANSFORM_OT_translate: Move, Move selected items (optional, :func:`bpy.ops.transform.translate` keyword arguments)
   :type TRANSFORM_OT_translate: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: extrude_region(*, use_normal_flip=False, use_dissolve_ortho_edges=False, mirror=False)

   Extrude region of faces

   :param use_normal_flip: Flip Normals, (optional)
   :type use_normal_flip: bool
   :param use_dissolve_ortho_edges: Dissolve Orthogonal Edges, (optional)
   :type use_dissolve_ortho_edges: bool
   :param mirror: Mirror Editing, (optional)
   :type mirror: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: extrude_region_move(*, MESH_OT_extrude_region={}, TRANSFORM_OT_translate={})

   Extrude region and move result

   :param MESH_OT_extrude_region: Extrude Region, Extrude region of faces (optional, :func:`bpy.ops.mesh.extrude_region` keyword arguments)
   :type MESH_OT_extrude_region: dict[str, Any]
   :param TRANSFORM_OT_translate: Move, Move selected items (optional, :func:`bpy.ops.transform.translate` keyword arguments)
   :type TRANSFORM_OT_translate: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: extrude_region_shrink_fatten(*, MESH_OT_extrude_region={}, TRANSFORM_OT_shrink_fatten={})

   Extrude region together along local normals

   :param MESH_OT_extrude_region: Extrude Region, Extrude region of faces (optional, :func:`bpy.ops.mesh.extrude_region` keyword arguments)
   :type MESH_OT_extrude_region: dict[str, Any]
   :param TRANSFORM_OT_shrink_fatten: Shrink/Fatten, Shrink/fatten selected vertices along normals (optional, :func:`bpy.ops.transform.shrink_fatten` keyword arguments)
   :type TRANSFORM_OT_shrink_fatten: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: extrude_repeat(*, steps=10, offset=(0.0, 0.0, 0.0), scale_offset=1.0)

   Extrude selected vertices, edges or faces repeatedly

   :param steps: Steps, (in [0, 1000000], optional)
   :type steps: int
   :param offset: Offset, Offset vector (array of 3 items, in [-100000, 100000], optional)
   :type offset: :class:`mathutils.Vector` | Sequence[float]
   :param scale_offset: Scale Offset, (in [0, inf], optional)
   :type scale_offset: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: extrude_vertices_move(*, MESH_OT_extrude_verts_indiv={}, TRANSFORM_OT_translate={})

   Extrude vertices and move result

   :param MESH_OT_extrude_verts_indiv: Extrude Only Vertices, Extrude individual vertices only (optional, :func:`bpy.ops.mesh.extrude_verts_indiv` keyword arguments)
   :type MESH_OT_extrude_verts_indiv: dict[str, Any]
   :param TRANSFORM_OT_translate: Move, Move selected items (optional, :func:`bpy.ops.transform.translate` keyword arguments)
   :type TRANSFORM_OT_translate: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: extrude_verts_indiv(*, mirror=False)

   Extrude individual vertices only

   :param mirror: Mirror Editing, (optional)
   :type mirror: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: face_make_planar(*, factor=1.0, repeat=1)

   Flatten selected faces

   :param factor: Factor, (in [-10, 10], optional)
   :type factor: float
   :param repeat: Iterations, (in [1, 10000], optional)
   :type repeat: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: face_split_by_edges()

   Weld loose edges into faces (splitting them into new faces)

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: faces_select_linked_flat(*, sharpness=0.0174533)

   Select linked faces by angle

   :param sharpness: Sharpness, (in [0.000174533, 3.14159], optional)
   :type sharpness: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: faces_shade_flat()

   Display faces flat

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: faces_shade_smooth()

   Display faces smooth (using vertex normals)

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: fill(*, use_beauty=True)

   Fill a selected edge loop with faces

   :param use_beauty: Beauty, Use best triangulation division (optional)
   :type use_beauty: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: fill_grid(*, span=1, offset=0, use_interp_simple=False)

   Fill grid from two loops

   :param span: Span, Number of grid columns (in [1, 1000], optional)
   :type span: int
   :param offset: Offset, Vertex that is the corner of the grid (in [-1000, 1000], optional)
   :type offset: int
   :param use_interp_simple: Simple Blending, Use simple interpolation of grid vertices (optional)
   :type use_interp_simple: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: fill_holes(*, sides=4)

   Fill in holes (boundary edge loops)

   :param sides: Sides, Number of sides in hole required to fill (zero fills all holes) (in [0, 1000], optional)
   :type sides: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: flip_normals(*, only_clnors=False)

   Flip the direction of selected faces' normals (and of their vertices)

   :param only_clnors: Custom Normals Only, Only flip the custom loop normals of the selected elements (optional)
   :type only_clnors: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: flip_quad_tessellation()

   Flips the tessellation of selected quads

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: hide(*, unselected=False)

   Hide (un)selected vertices, edges or faces

   :param unselected: Unselected, Hide unselected rather than selected (optional)
   :type unselected: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: inset(*, use_boundary=True, use_even_offset=True, use_relative_offset=False, use_edge_rail=False, thickness=0.0, depth=0.0, use_outset=False, use_select_inset=False, use_individual=False, use_interpolate=True, release_confirm=False)

   Inset new faces into selected faces

   :param use_boundary: Boundary, Inset face boundaries (optional)
   :type use_boundary: bool
   :param use_even_offset: Offset Even, Scale the offset to give more even thickness (optional)
   :type use_even_offset: bool
   :param use_relative_offset: Offset Relative, Scale the offset by surrounding geometry (optional)
   :type use_relative_offset: bool
   :param use_edge_rail: Edge Rail, Inset the region along existing edges (optional)
   :type use_edge_rail: bool
   :param thickness: Thickness, (in [0, inf], optional)
   :type thickness: float
   :param depth: Depth, (in [-inf, inf], optional)
   :type depth: float
   :param use_outset: Outset, Outset rather than inset (optional)
   :type use_outset: bool
   :param use_select_inset: Select Outer, Select the new inset faces (optional)
   :type use_select_inset: bool
   :param use_individual: Individual, Individual face inset (optional)
   :type use_individual: bool
   :param use_interpolate: Interpolate, Blend face data across the inset (optional)
   :type use_interpolate: bool
   :param release_confirm: Confirm on Release, (optional)
   :type release_confirm: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: intersect(*, mode='SELECT_UNSELECT', separate_mode='CUT', threshold=1e-06, solver='EXACT')

   Cut an intersection into faces

   :param mode: Source, (optional)

      - ``SELECT``
        Self Intersect -- Self intersect selected faces.
      - ``SELECT_UNSELECT``
        Selected/Unselected -- Intersect selected with unselected faces.
   :type mode: Literal['SELECT', 'SELECT_UNSELECT']
   :param separate_mode: Separate Mode, (optional)

      - ``ALL``
        All -- Separate all geometry from intersections.
      - ``CUT``
        Cut -- Cut into geometry keeping each side separate (Selected/Unselected only).
      - ``NONE``
        Merge -- Merge all geometry from the intersection.
   :type separate_mode: Literal['ALL', 'CUT', 'NONE']
   :param threshold: Merge Threshold, (in [0, 0.01], optional)
   :type threshold: float
   :param solver: Solver, Which Intersect solver to use (optional)

      - ``FLOAT``
        Float -- Simple solver with good performance, without support for overlapping geometry.
      - ``EXACT``
        Exact -- Slower solver with the best results for coplanar faces.
   :type solver: Literal['FLOAT', 'EXACT']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: intersect_boolean(*, operation='DIFFERENCE', use_swap=False, use_self=False, threshold=1e-06, solver='EXACT')

   Cut solid geometry from selected to unselected

   :param operation: Boolean Operation, Which boolean operation to apply (optional)
   :type operation: Literal['INTERSECT', 'UNION', 'DIFFERENCE']
   :param use_swap: Swap, Use with difference intersection to swap which side is kept (optional)
   :type use_swap: bool
   :param use_self: Self Intersection, Do self-union or self-intersection (optional)
   :type use_self: bool
   :param threshold: Merge Threshold, (in [0, 0.01], optional)
   :type threshold: float
   :param solver: Solver, Which Boolean solver to use (optional)

      - ``FLOAT``
        Float -- Faster solver, some limitations.
      - ``EXACT``
        Exact -- Exact solver, slower, handles more cases.
   :type solver: Literal['FLOAT', 'EXACT']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: knife_project(*, cut_through=False)

   Use other objects outlines and boundaries to project knife cuts

   :param cut_through: Cut Through, Cut through all faces, not just visible ones (optional)
   :type cut_through: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: knife_tool(*, use_occlude_geometry=True, only_selected=False, xray=True, visible_measurements='NONE', angle_snapping='NONE', angle_snapping_increment=0.523599, wait_for_input=True)

   Cut new topology

   :param use_occlude_geometry: Occlude Geometry, Only cut the front most geometry (optional)
   :type use_occlude_geometry: bool
   :param only_selected: Only Selected, Only cut selected geometry (optional)
   :type only_selected: bool
   :param xray: X-Ray, Show cuts hidden by geometry (optional)
   :type xray: bool
   :param visible_measurements: Measurements, Visible distance and angle measurements (optional)

      - ``NONE``
        None -- Show no measurements.
      - ``BOTH``
        Both -- Show both distances and angles.
      - ``DISTANCE``
        Distance -- Show just distance measurements.
      - ``ANGLE``
        Angle -- Show just angle measurements.
   :type visible_measurements: Literal['NONE', 'BOTH', 'DISTANCE', 'ANGLE']
   :param angle_snapping: Angle Snapping, Angle snapping mode (optional)

      - ``NONE``
        None -- No angle snapping.
      - ``SCREEN``
        Screen -- Screen space angle snapping.
      - ``RELATIVE``
        Relative -- Angle snapping relative to the previous cut edge.
   :type angle_snapping: Literal['NONE', 'SCREEN', 'RELATIVE']
   :param angle_snapping_increment: Angle Snap Increment, The angle snap increment used when in constrained angle mode (in [0, 3.14159], optional)
   :type angle_snapping_increment: float
   :param wait_for_input: Wait for Input, (optional)
   :type wait_for_input: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: loop_select(*, delimit_edge_loop={'NGONS', 'OUTER_CORNERS'}, delimit_face_loop=set(), extend=False, deselect=False, toggle=False, object_index=-1, edge_index=-1, vert_index=-1, face_index=-1)

   Select a loop of connected edges

   :param delimit_edge_loop: Delimit, Delimit edge loop selection (optional)
   :type delimit_edge_loop: set[Literal[:ref:`rna_enum_mesh_walk_delimit_edge_loop_items`]]
   :param delimit_face_loop: Face Loop Delimit, Delimit face loop selection (optional)
   :type delimit_face_loop: set[Literal[:ref:`rna_enum_mesh_walk_delimit_face_loop_items`]]
   :param extend: Extend Select, Extend the selection (optional)
   :type extend: bool
   :param deselect: Deselect, Remove from the selection (optional)
   :type deselect: bool
   :param toggle: Toggle Select, Toggle the selection (optional)
   :type toggle: bool
   :param object_index: (in [-1, inf], optional)
   :type object_index: int
   :param edge_index: (in [-1, inf], optional)
   :type edge_index: int
   :param vert_index: (in [-1, inf], optional)
   :type vert_index: int
   :param face_index: (in [-1, inf], optional)
   :type face_index: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: loop_to_region(*, select_bigger=False)

   Select region of faces inside of a selected loop of edges

   :param select_bigger: Select Bigger, Select bigger regions instead of smaller ones (optional)
   :type select_bigger: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: loopcut(*, number_cuts=1, smoothness=0.0, falloff='INVERSE_SQUARE', object_index=-1, edge_index=-1, mesh_select_mode_init=(False, False, False))

   Add a new loop between existing loops

   :param number_cuts: Number of Cuts, (in [1, 1000000], optional)
   :type number_cuts: int
   :param smoothness: Smoothness, Smoothness factor (in [-1000, 1000], optional)
   :type smoothness: float
   :param falloff: Falloff, Falloff type of the feather (optional)
   :type falloff: Literal[:ref:`rna_enum_proportional_falloff_curve_only_items`]
   :param object_index: Object Index, (in [-1, inf], optional)
   :type object_index: int
   :param edge_index: Edge Index, (in [-1, inf], optional)
   :type edge_index: int
   :param mesh_select_mode_init: (array of 3 items, optional)
   :type mesh_select_mode_init: Sequence[bool]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: loopcut_slide(*, MESH_OT_loopcut={}, TRANSFORM_OT_edge_slide={})

   Cut mesh loop and slide it

   :param MESH_OT_loopcut: Loop Cut, Add a new loop between existing loops (optional, :func:`bpy.ops.mesh.loopcut` keyword arguments)
   :type MESH_OT_loopcut: dict[str, Any]
   :param TRANSFORM_OT_edge_slide: Edge Slide, Slide an edge loop along a mesh (optional, :func:`bpy.ops.transform.edge_slide` keyword arguments)
   :type TRANSFORM_OT_edge_slide: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: mark_seam(*, clear=False)

   (Un)mark selected edges as a seam

   :param clear: Clear, (optional)
   :type clear: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: mark_sharp(*, clear=False, use_verts=False)

   (Un)mark selected edges as sharp

   :param clear: Clear, (optional)
   :type clear: bool
   :param use_verts: Vertices, Consider vertices instead of edges to select which edges to (un)tag as sharp (optional)
   :type use_verts: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: merge(*, type='CENTER', uvs=False)

   Merge selected vertices

   :param type: Type, Merge method to use (optional)
   :type type: Literal['CENTER', 'CURSOR', 'COLLAPSE', 'FIRST', 'LAST']
   :param uvs: UVs, Move UVs according to merge (optional)
   :type uvs: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: merge_normals()

   Merge custom normals of selected vertices

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: mod_weighted_strength(*, set=False, face_strength='MEDIUM')

   Set/Get strength of face (used in Weighted Normal modifier)

   :param set: Set Value, Set value of faces (optional)
   :type set: bool
   :param face_strength: Face Strength, Strength to use for assigning or selecting face influence for weighted normal modifier (optional)
   :type face_strength: Literal['WEAK', 'MEDIUM', 'STRONG']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: normals_make_consistent(*, inside=False)

   Make face and vertex normals point either outside or inside the mesh

   :param inside: Inside, (optional)
   :type inside: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: normals_tools(*, mode='COPY', absolute=False)

   Custom normals tools using Normal Vector of UI

   :param mode: Mode, Mode of tools taking input from interface (optional)

      - ``COPY``
        Copy Normal -- Copy normal to the internal clipboard.
      - ``PASTE``
        Paste Normal -- Paste normal from the internal clipboard.
      - ``ADD``
        Add Normal -- Add normal vector with selection.
      - ``MULTIPLY``
        Multiply Normal -- Multiply normal vector with selection.
      - ``RESET``
        Reset Normal -- Reset the internal clipboard and/or normal of selected element.
   :type mode: Literal['COPY', 'PASTE', 'ADD', 'MULTIPLY', 'RESET']
   :param absolute: Absolute Coordinates, Copy Absolute coordinates of Normal vector (optional)
   :type absolute: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: offset_edge_loops(*, use_cap_endpoint=False)

   Create offset edge loop from the current selection

   :param use_cap_endpoint: Cap Endpoint, Extend loop around end-points (optional)
   :type use_cap_endpoint: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: offset_edge_loops_slide(*, MESH_OT_offset_edge_loops={}, TRANSFORM_OT_edge_slide={})

   Offset edge loop slide

   :param MESH_OT_offset_edge_loops: Offset Edge Loop, Create offset edge loop from the current selection (optional, :func:`bpy.ops.mesh.offset_edge_loops` keyword arguments)
   :type MESH_OT_offset_edge_loops: dict[str, Any]
   :param TRANSFORM_OT_edge_slide: Edge Slide, Slide an edge loop along a mesh (optional, :func:`bpy.ops.transform.edge_slide` keyword arguments)
   :type TRANSFORM_OT_edge_slide: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: point_normals(*, mode='COORDINATES', invert=False, align=False, target_location=(0.0, 0.0, 0.0), spherize=False, spherize_strength=0.1)

   Point selected custom normals to specified Target

   :param mode: Mode, How to define coordinates to point custom normals to (optional)

      - ``COORDINATES``
        Coordinates -- Use static coordinates (defined by various means).
      - ``MOUSE``
        Mouse -- Follow mouse cursor.
   :type mode: Literal['COORDINATES', 'MOUSE']
   :param invert: Invert, Invert affected normals (optional)
   :type invert: bool
   :param align: Align, Make all affected normals parallel (optional)
   :type align: bool
   :param target_location: Target, Target location to which normals will point (array of 3 items, in [-inf, inf], optional)
   :type target_location: :class:`mathutils.Vector` | Sequence[float]
   :param spherize: Spherize, Interpolate between original and new normals (optional)
   :type spherize: bool
   :param spherize_strength: Spherize Strength, Ratio of spherized normal to original normal (in [0, 1], optional)
   :type spherize_strength: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: poke(*, offset=0.0, use_relative_offset=False, center_mode='MEDIAN_WEIGHTED')

   Split a face into a fan

   :param offset: Poke Offset, Poke Offset (in [-1000, 1000], optional)
   :type offset: float
   :param use_relative_offset: Offset Relative, Scale the offset by surrounding geometry (optional)
   :type use_relative_offset: bool
   :param center_mode: Poke Center, Poke face center calculation (optional)

      - ``MEDIAN_WEIGHTED``
        Weighted Median -- Weighted median face center.
      - ``MEDIAN``
        Median -- Median face center.
      - ``BOUNDS``
        Bounds -- Face bounds center.
   :type center_mode: Literal['MEDIAN_WEIGHTED', 'MEDIAN', 'BOUNDS']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: polybuild_delete_at_cursor(*, mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1.0, use_proportional_connected=False, use_proportional_projected=False, release_confirm=False, use_accurate=False)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :param mirror: Mirror Editing, (optional)
   :type mirror: bool
   :param use_proportional_edit: Proportional Editing, (optional)
   :type use_proportional_edit: bool
   :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode (optional)
   :type proportional_edit_falloff: Literal[:ref:`rna_enum_proportional_falloff_items`]
   :param proportional_size: Proportional Size, (in [1e-06, inf], optional)
   :type proportional_size: float
   :param use_proportional_connected: Connected, (optional)
   :type use_proportional_connected: bool
   :param use_proportional_projected: Projected (2D), (optional)
   :type use_proportional_projected: bool
   :param release_confirm: Confirm on Release, Always confirm operation when releasing button (optional)
   :type release_confirm: bool
   :param use_accurate: Accurate, Use accurate transformation (optional)
   :type use_accurate: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: polybuild_dissolve_at_cursor()

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: polybuild_extrude_at_cursor_move(*, MESH_OT_polybuild_transform_at_cursor={}, MESH_OT_extrude_edges_indiv={}, TRANSFORM_OT_translate={})

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :param MESH_OT_polybuild_transform_at_cursor: Poly Build Transform at Cursor, (optional, :func:`bpy.ops.mesh.polybuild_transform_at_cursor` keyword arguments)
   :type MESH_OT_polybuild_transform_at_cursor: dict[str, Any]
   :param MESH_OT_extrude_edges_indiv: Extrude Only Edges, Extrude individual edges only (optional, :func:`bpy.ops.mesh.extrude_edges_indiv` keyword arguments)
   :type MESH_OT_extrude_edges_indiv: dict[str, Any]
   :param TRANSFORM_OT_translate: Move, Move selected items (optional, :func:`bpy.ops.transform.translate` keyword arguments)
   :type TRANSFORM_OT_translate: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: polybuild_face_at_cursor(*, create_quads=True, mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1.0, use_proportional_connected=False, use_proportional_projected=False, release_confirm=False, use_accurate=False)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :param create_quads: Create Quads, Automatically split edges in triangles to maintain quad topology (optional)
   :type create_quads: bool
   :param mirror: Mirror Editing, (optional)
   :type mirror: bool
   :param use_proportional_edit: Proportional Editing, (optional)
   :type use_proportional_edit: bool
   :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode (optional)
   :type proportional_edit_falloff: Literal[:ref:`rna_enum_proportional_falloff_items`]
   :param proportional_size: Proportional Size, (in [1e-06, inf], optional)
   :type proportional_size: float
   :param use_proportional_connected: Connected, (optional)
   :type use_proportional_connected: bool
   :param use_proportional_projected: Projected (2D), (optional)
   :type use_proportional_projected: bool
   :param release_confirm: Confirm on Release, Always confirm operation when releasing button (optional)
   :type release_confirm: bool
   :param use_accurate: Accurate, Use accurate transformation (optional)
   :type use_accurate: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: polybuild_face_at_cursor_move(*, MESH_OT_polybuild_face_at_cursor={}, TRANSFORM_OT_translate={})

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :param MESH_OT_polybuild_face_at_cursor: Poly Build Face at Cursor, (optional, :func:`bpy.ops.mesh.polybuild_face_at_cursor` keyword arguments)
   :type MESH_OT_polybuild_face_at_cursor: dict[str, Any]
   :param TRANSFORM_OT_translate: Move, Move selected items (optional, :func:`bpy.ops.transform.translate` keyword arguments)
   :type TRANSFORM_OT_translate: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: polybuild_split_at_cursor(*, mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1.0, use_proportional_connected=False, use_proportional_projected=False, release_confirm=False, use_accurate=False)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :param mirror: Mirror Editing, (optional)
   :type mirror: bool
   :param use_proportional_edit: Proportional Editing, (optional)
   :type use_proportional_edit: bool
   :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode (optional)
   :type proportional_edit_falloff: Literal[:ref:`rna_enum_proportional_falloff_items`]
   :param proportional_size: Proportional Size, (in [1e-06, inf], optional)
   :type proportional_size: float
   :param use_proportional_connected: Connected, (optional)
   :type use_proportional_connected: bool
   :param use_proportional_projected: Projected (2D), (optional)
   :type use_proportional_projected: bool
   :param release_confirm: Confirm on Release, Always confirm operation when releasing button (optional)
   :type release_confirm: bool
   :param use_accurate: Accurate, Use accurate transformation (optional)
   :type use_accurate: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: polybuild_split_at_cursor_move(*, MESH_OT_polybuild_split_at_cursor={}, TRANSFORM_OT_translate={})

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :param MESH_OT_polybuild_split_at_cursor: Poly Build Split at Cursor, (optional, :func:`bpy.ops.mesh.polybuild_split_at_cursor` keyword arguments)
   :type MESH_OT_polybuild_split_at_cursor: dict[str, Any]
   :param TRANSFORM_OT_translate: Move, Move selected items (optional, :func:`bpy.ops.transform.translate` keyword arguments)
   :type TRANSFORM_OT_translate: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: polybuild_transform_at_cursor(*, mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1.0, use_proportional_connected=False, use_proportional_projected=False, release_confirm=False, use_accurate=False)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :param mirror: Mirror Editing, (optional)
   :type mirror: bool
   :param use_proportional_edit: Proportional Editing, (optional)
   :type use_proportional_edit: bool
   :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode (optional)
   :type proportional_edit_falloff: Literal[:ref:`rna_enum_proportional_falloff_items`]
   :param proportional_size: Proportional Size, (in [1e-06, inf], optional)
   :type proportional_size: float
   :param use_proportional_connected: Connected, (optional)
   :type use_proportional_connected: bool
   :param use_proportional_projected: Projected (2D), (optional)
   :type use_proportional_projected: bool
   :param release_confirm: Confirm on Release, Always confirm operation when releasing button (optional)
   :type release_confirm: bool
   :param use_accurate: Accurate, Use accurate transformation (optional)
   :type use_accurate: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: polybuild_transform_at_cursor_move(*, MESH_OT_polybuild_transform_at_cursor={}, TRANSFORM_OT_translate={})

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :param MESH_OT_polybuild_transform_at_cursor: Poly Build Transform at Cursor, (optional, :func:`bpy.ops.mesh.polybuild_transform_at_cursor` keyword arguments)
   :type MESH_OT_polybuild_transform_at_cursor: dict[str, Any]
   :param TRANSFORM_OT_translate: Move, Move selected items (optional, :func:`bpy.ops.transform.translate` keyword arguments)
   :type TRANSFORM_OT_translate: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: primitive_circle_add(*, vertices=32, radius=1.0, fill_type='NOTHING', calc_uvs=True, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Construct a circle mesh

   :param vertices: Vertices, (in [3, 10000000], optional)
   :type vertices: int
   :param radius: Radius, (in [0, inf], optional)
   :type radius: float
   :param fill_type: Fill Type, (optional)

      - ``NOTHING``
        Nothing -- Don't fill at all.
      - ``NGON``
        N-Gon -- Use n-gons.
      - ``TRIFAN``
        Triangle Fan -- Use triangle fans.
   :type fill_type: Literal['NOTHING', 'NGON', 'TRIFAN']
   :param calc_uvs: Generate UVs, Generate a default UV map (optional)
   :type calc_uvs: bool
   :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object (optional)
   :type enter_editmode: bool
   :param align: Align, The alignment of the new object (optional)

      - ``WORLD``
        World -- Align the new object to the world.
      - ``VIEW``
        View -- Align the new object to the view.
      - ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: Literal['WORLD', 'VIEW', 'CURSOR']
   :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type rotation: :class:`mathutils.Euler` | Sequence[float]
   :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type scale: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: primitive_cone_add(*, vertices=32, radius1=1.0, radius2=0.0, depth=2.0, end_fill_type='NGON', calc_uvs=True, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Construct a conic mesh

   :param vertices: Vertices, (in [3, 10000000], optional)
   :type vertices: int
   :param radius1: Radius 1, (in [0, inf], optional)
   :type radius1: float
   :param radius2: Radius 2, (in [0, inf], optional)
   :type radius2: float
   :param depth: Depth, (in [0, inf], optional)
   :type depth: float
   :param end_fill_type: Base Fill Type, (optional)

      - ``NOTHING``
        Nothing -- Don't fill at all.
      - ``NGON``
        N-Gon -- Use n-gons.
      - ``TRIFAN``
        Triangle Fan -- Use triangle fans.
   :type end_fill_type: Literal['NOTHING', 'NGON', 'TRIFAN']
   :param calc_uvs: Generate UVs, Generate a default UV map (optional)
   :type calc_uvs: bool
   :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object (optional)
   :type enter_editmode: bool
   :param align: Align, The alignment of the new object (optional)

      - ``WORLD``
        World -- Align the new object to the world.
      - ``VIEW``
        View -- Align the new object to the view.
      - ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: Literal['WORLD', 'VIEW', 'CURSOR']
   :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type rotation: :class:`mathutils.Euler` | Sequence[float]
   :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type scale: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: primitive_cube_add(*, size=2.0, calc_uvs=True, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Construct a cube mesh that consists of six square faces

   :param size: Size, (in [0, inf], optional)
   :type size: float
   :param calc_uvs: Generate UVs, Generate a default UV map (optional)
   :type calc_uvs: bool
   :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object (optional)
   :type enter_editmode: bool
   :param align: Align, The alignment of the new object (optional)

      - ``WORLD``
        World -- Align the new object to the world.
      - ``VIEW``
        View -- Align the new object to the view.
      - ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: Literal['WORLD', 'VIEW', 'CURSOR']
   :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type rotation: :class:`mathutils.Euler` | Sequence[float]
   :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type scale: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: primitive_cube_add_gizmo(*, calc_uvs=True, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0), matrix=((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)))

   Construct a cube mesh

   :param calc_uvs: Generate UVs, Generate a default UV map (optional)
   :type calc_uvs: bool
   :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object (optional)
   :type enter_editmode: bool
   :param align: Align, The alignment of the new object (optional)

      - ``WORLD``
        World -- Align the new object to the world.
      - ``VIEW``
        View -- Align the new object to the view.
      - ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: Literal['WORLD', 'VIEW', 'CURSOR']
   :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type rotation: :class:`mathutils.Euler` | Sequence[float]
   :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type scale: :class:`mathutils.Vector` | Sequence[float]
   :param matrix: Matrix, (multi-dimensional array of 4 * 4 items, in [-inf, inf], optional)
   :type matrix: :class:`mathutils.Matrix` | Sequence[Sequence[float]]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: primitive_cylinder_add(*, vertices=32, radius=1.0, depth=2.0, end_fill_type='NGON', calc_uvs=True, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Construct a cylinder mesh

   :param vertices: Vertices, (in [3, 10000000], optional)
   :type vertices: int
   :param radius: Radius, (in [0, inf], optional)
   :type radius: float
   :param depth: Depth, (in [0, inf], optional)
   :type depth: float
   :param end_fill_type: Cap Fill Type, (optional)

      - ``NOTHING``
        Nothing -- Don't fill at all.
      - ``NGON``
        N-Gon -- Use n-gons.
      - ``TRIFAN``
        Triangle Fan -- Use triangle fans.
   :type end_fill_type: Literal['NOTHING', 'NGON', 'TRIFAN']
   :param calc_uvs: Generate UVs, Generate a default UV map (optional)
   :type calc_uvs: bool
   :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object (optional)
   :type enter_editmode: bool
   :param align: Align, The alignment of the new object (optional)

      - ``WORLD``
        World -- Align the new object to the world.
      - ``VIEW``
        View -- Align the new object to the view.
      - ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: Literal['WORLD', 'VIEW', 'CURSOR']
   :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type rotation: :class:`mathutils.Euler` | Sequence[float]
   :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type scale: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: primitive_grid_add(*, x_subdivisions=10, y_subdivisions=10, size=2.0, calc_uvs=True, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Construct a subdivided plane mesh

   :param x_subdivisions: X Subdivisions, (in [1, 10000000], optional)
   :type x_subdivisions: int
   :param y_subdivisions: Y Subdivisions, (in [1, 10000000], optional)
   :type y_subdivisions: int
   :param size: Size, (in [0, inf], optional)
   :type size: float
   :param calc_uvs: Generate UVs, Generate a default UV map (optional)
   :type calc_uvs: bool
   :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object (optional)
   :type enter_editmode: bool
   :param align: Align, The alignment of the new object (optional)

      - ``WORLD``
        World -- Align the new object to the world.
      - ``VIEW``
        View -- Align the new object to the view.
      - ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: Literal['WORLD', 'VIEW', 'CURSOR']
   :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type rotation: :class:`mathutils.Euler` | Sequence[float]
   :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type scale: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: primitive_ico_sphere_add(*, subdivisions=2, radius=1.0, calc_uvs=True, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Construct a spherical mesh that consists of equally sized triangles

   :param subdivisions: Subdivisions, (in [1, 10], optional)
   :type subdivisions: int
   :param radius: Radius, (in [0, inf], optional)
   :type radius: float
   :param calc_uvs: Generate UVs, Generate a default UV map (optional)
   :type calc_uvs: bool
   :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object (optional)
   :type enter_editmode: bool
   :param align: Align, The alignment of the new object (optional)

      - ``WORLD``
        World -- Align the new object to the world.
      - ``VIEW``
        View -- Align the new object to the view.
      - ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: Literal['WORLD', 'VIEW', 'CURSOR']
   :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type rotation: :class:`mathutils.Euler` | Sequence[float]
   :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type scale: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: primitive_monkey_add(*, size=2.0, calc_uvs=True, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Construct a Suzanne mesh

   :param size: Size, (in [0, inf], optional)
   :type size: float
   :param calc_uvs: Generate UVs, Generate a default UV map (optional)
   :type calc_uvs: bool
   :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object (optional)
   :type enter_editmode: bool
   :param align: Align, The alignment of the new object (optional)

      - ``WORLD``
        World -- Align the new object to the world.
      - ``VIEW``
        View -- Align the new object to the view.
      - ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: Literal['WORLD', 'VIEW', 'CURSOR']
   :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type rotation: :class:`mathutils.Euler` | Sequence[float]
   :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type scale: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: primitive_plane_add(*, size=2.0, calc_uvs=True, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Construct a filled planar mesh with 4 vertices

   :param size: Size, (in [0, inf], optional)
   :type size: float
   :param calc_uvs: Generate UVs, Generate a default UV map (optional)
   :type calc_uvs: bool
   :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object (optional)
   :type enter_editmode: bool
   :param align: Align, The alignment of the new object (optional)

      - ``WORLD``
        World -- Align the new object to the world.
      - ``VIEW``
        View -- Align the new object to the view.
      - ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: Literal['WORLD', 'VIEW', 'CURSOR']
   :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type rotation: :class:`mathutils.Euler` | Sequence[float]
   :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type scale: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: primitive_torus_add(*, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), major_segments=48, minor_segments=12, mode='MAJOR_MINOR', major_radius=1.0, minor_radius=0.25, abso_major_rad=1.25, abso_minor_rad=0.75, generate_uvs=True)

   Construct a torus mesh

   :param align: Align, (optional)

      - ``WORLD``
        World -- Align the new object to the world.
      - ``VIEW``
        View -- Align the new object to the view.
      - ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: Literal['WORLD', 'VIEW', 'CURSOR']
   :param location: Location, (array of 3 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :param rotation: Rotation, (array of 3 items, in [-inf, inf], optional)
   :type rotation: :class:`mathutils.Euler` | Sequence[float]
   :param major_segments: Major Segments, Number of segments for the main ring of the torus (in [3, 256], optional)
   :type major_segments: int
   :param minor_segments: Minor Segments, Number of segments for the minor ring of the torus (in [3, 256], optional)
   :type minor_segments: int
   :param mode: Dimensions Mode, (optional)

      - ``MAJOR_MINOR``
        Major/Minor -- Use the major/minor radii for torus dimensions.
      - ``EXT_INT``
        Exterior/Interior -- Use the exterior/interior radii for torus dimensions.
   :type mode: Literal['MAJOR_MINOR', 'EXT_INT']
   :param major_radius: Major Radius, Radius from the origin to the center of the cross sections (in [0, 10000], optional)
   :type major_radius: float
   :param minor_radius: Minor Radius, Radius of the torus's cross section (in [0, 10000], optional)
   :type minor_radius: float
   :param abso_major_rad: Exterior Radius, Total Exterior Radius of the torus (in [0, 10000], optional)
   :type abso_major_rad: float
   :param abso_minor_rad: Interior Radius, Total Interior Radius of the torus (in [0, 10000], optional)
   :type abso_minor_rad: float
   :param generate_uvs: Generate UVs, Generate a default UV map (optional)
   :type generate_uvs: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/add_mesh_torus.py\:222 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/add_mesh_torus.py#L222>`__


.. function:: primitive_uv_sphere_add(*, segments=32, ring_count=16, radius=1.0, calc_uvs=True, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Construct a spherical mesh with quad faces, except for triangle faces at the top and bottom

   :param segments: Segments, (in [3, 100000], optional)
   :type segments: int
   :param ring_count: Rings, (in [3, 100000], optional)
   :type ring_count: int
   :param radius: Radius, (in [0, inf], optional)
   :type radius: float
   :param calc_uvs: Generate UVs, Generate a default UV map (optional)
   :type calc_uvs: bool
   :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object (optional)
   :type enter_editmode: bool
   :param align: Align, The alignment of the new object (optional)

      - ``WORLD``
        World -- Align the new object to the world.
      - ``VIEW``
        View -- Align the new object to the view.
      - ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: Literal['WORLD', 'VIEW', 'CURSOR']
   :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type rotation: :class:`mathutils.Euler` | Sequence[float]
   :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type scale: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: quads_convert_to_tris(*, quad_method='BEAUTY', ngon_method='BEAUTY')

   Triangulate selected faces

   :param quad_method: Quad Method, Method for splitting the quads into triangles (optional)
   :type quad_method: Literal[:ref:`rna_enum_modifier_triangulate_quad_method_items`]
   :param ngon_method: N-gon Method, Method for splitting the n-gons into triangles (optional)
   :type ngon_method: Literal[:ref:`rna_enum_modifier_triangulate_ngon_method_items`]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: region_to_loop()

   Select boundary edges around the selected faces

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: remove_doubles(*, threshold=0.0001, use_centroid=True, use_unselected=False, use_sharp_edge_from_normals=False)

   Merge vertices based on their proximity

   :param threshold: Merge Distance, Maximum distance between elements to merge (in [1e-06, 50], optional)
   :type threshold: float
   :param use_centroid: Centroid Merge, Move vertices to the centroid of the duplicate cluster, otherwise the vertex closest to the centroid is used. (optional)
   :type use_centroid: bool
   :param use_unselected: Unselected, Merge selected to other unselected vertices (optional)
   :type use_unselected: bool
   :param use_sharp_edge_from_normals: Sharp Edges, Calculate sharp edges using custom normal data (when available) (optional)
   :type use_sharp_edge_from_normals: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: reorder_vertices_spatial()

   Reorder mesh faces and vertices based on their spatial position for better BVH building and sculpting performance.

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: reveal(*, select=True)

   Reveal all hidden vertices, edges and faces

   :param select: Select, (optional)
   :type select: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: rip(*, mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1.0, use_proportional_connected=False, use_proportional_projected=False, release_confirm=False, use_accurate=False, use_fill=False)

   Disconnect vertices or edges from connected geometry

   :param mirror: Mirror Editing, (optional)
   :type mirror: bool
   :param use_proportional_edit: Proportional Editing, (optional)
   :type use_proportional_edit: bool
   :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode (optional)
   :type proportional_edit_falloff: Literal[:ref:`rna_enum_proportional_falloff_items`]
   :param proportional_size: Proportional Size, (in [1e-06, inf], optional)
   :type proportional_size: float
   :param use_proportional_connected: Connected, (optional)
   :type use_proportional_connected: bool
   :param use_proportional_projected: Projected (2D), (optional)
   :type use_proportional_projected: bool
   :param release_confirm: Confirm on Release, Always confirm operation when releasing button (optional)
   :type release_confirm: bool
   :param use_accurate: Accurate, Use accurate transformation (optional)
   :type use_accurate: bool
   :param use_fill: Fill, Fill the ripped region (optional)
   :type use_fill: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: rip_edge(*, location=(0.0, 0.0, 0.0), direction=(0.0, 0.0, 0.0))

   Extend vertices along the edge closest to the cursor

   :param location: Location, World-space ray origin for extending vertices (array of 3 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :param direction: Direction, World-space direction vector for extending vertices (array of 3 items, in [-inf, inf], optional)
   :type direction: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: rip_edge_move(*, MESH_OT_rip_edge={}, TRANSFORM_OT_translate={})

   Extend vertices and move the result

   :param MESH_OT_rip_edge: Extend Vertices, Extend vertices along the edge closest to the cursor (optional, :func:`bpy.ops.mesh.rip_edge` keyword arguments)
   :type MESH_OT_rip_edge: dict[str, Any]
   :param TRANSFORM_OT_translate: Move, Move selected items (optional, :func:`bpy.ops.transform.translate` keyword arguments)
   :type TRANSFORM_OT_translate: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: rip_move(*, MESH_OT_rip={}, TRANSFORM_OT_translate={})

   Rip polygons and move the result

   :param MESH_OT_rip: Rip, Disconnect vertices or edges from connected geometry (optional, :func:`bpy.ops.mesh.rip` keyword arguments)
   :type MESH_OT_rip: dict[str, Any]
   :param TRANSFORM_OT_translate: Move, Move selected items (optional, :func:`bpy.ops.transform.translate` keyword arguments)
   :type TRANSFORM_OT_translate: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: screw(*, steps=9, turns=1, center=(0.0, 0.0, 0.0), axis=(0.0, 0.0, 0.0))

   Extrude selected vertices in screw-shaped rotation around the cursor in indicated viewport

   :param steps: Steps, Steps (in [1, 100000], optional)
   :type steps: int
   :param turns: Turns, Turns (in [1, 100000], optional)
   :type turns: int
   :param center: Center, Center in global view space (array of 3 items, in [-inf, inf], optional)
   :type center: :class:`mathutils.Vector` | Sequence[float]
   :param axis: Axis, Axis in global view space (array of 3 items, in [-1, 1], optional)
   :type axis: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_all(*, action='TOGGLE')

   (De)select all vertices, edges or faces

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

.. function:: select_axis(*, orientation='LOCAL', sign='POS', axis='X', threshold=0.0001)

   Select all data in the mesh on a single axis

   :param orientation: Axis Mode, Axis orientation (optional)
   :type orientation: Literal[:ref:`rna_enum_transform_orientation_items`]
   :param sign: Axis Sign, Side to select (optional)
   :type sign: Literal['POS', 'NEG', 'ALIGN']
   :param axis: Axis, Select the axis to compare each vertex on (optional)
   :type axis: Literal[:ref:`rna_enum_axis_xyz_items`]
   :param threshold: Threshold, (in [1e-06, 50], optional)
   :type threshold: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_by_attribute()

   Select elements based on the active boolean attribute

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select_by_pole_count(*, pole_count=4, type='NOTEQUAL', extend=False, exclude_nonmanifold=True)

   Select vertices at poles by the number of connected edges. In edge and face mode the geometry connected to the vertices is selected

   :param pole_count: Pole Count, (in [0, inf], optional)
   :type pole_count: int
   :param type: Type, Type of comparison to make (optional)
   :type type: Literal['LESS', 'EQUAL', 'GREATER', 'NOTEQUAL']
   :param extend: Extend, Extend the selection (optional)
   :type extend: bool
   :param exclude_nonmanifold: Exclude Non Manifold, Exclude non-manifold poles (optional)
   :type exclude_nonmanifold: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_edge_loop_multi(*, delimit_edge_loop={'NGONS', 'OUTER_CORNERS'})

   Select loops of connected edges from each selected edge

   :param delimit_edge_loop: Delimit, Delimit edge loop selection (optional)
   :type delimit_edge_loop: set[Literal[:ref:`rna_enum_mesh_walk_delimit_edge_loop_items`]]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_edge_ring_multi(*, delimit_edge_ring={'NGONS'})

   Select rings of connected edges from each selected edge

   :param delimit_edge_ring: Edge Ring Delimit, Delimit edge ring selection (optional)
   :type delimit_edge_ring: set[Literal[:ref:`rna_enum_mesh_walk_delimit_edge_ring_items`]]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_face_by_sides(*, number=4, type='EQUAL', extend=True)

   Select vertices or faces by the number of face sides

   :param number: Number of Vertices, (in [3, inf], optional)
   :type number: int
   :param type: Type, Type of comparison to make (optional)
   :type type: Literal['LESS', 'EQUAL', 'GREATER', 'NOTEQUAL']
   :param extend: Extend, Extend the selection (optional)
   :type extend: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_interior_faces()

   Select faces where all edges have more than 2 face users

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select_less(*, use_face_step=True)

   Deselect vertices, edges or faces at the boundary of each selection region

   :param use_face_step: Face Step, Connected faces (instead of edges) (optional)
   :type use_face_step: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_linked(*, delimit={'SEAM'})

   Select all vertices connected to the current selection

   :param delimit: Delimit, Delimit selected region (optional)
   :type delimit: set[Literal[:ref:`rna_enum_mesh_delimit_mode_items`]]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_linked_pick(*, deselect=False, delimit={'SEAM'}, object_index=-1, index=-1)

   (De)select all vertices linked to the edge under the mouse cursor

   :param deselect: Deselect, (optional)
   :type deselect: bool
   :param delimit: Delimit, Delimit selected region (optional)
   :type delimit: set[Literal[:ref:`rna_enum_mesh_delimit_mode_items`]]
   :param object_index: (in [-1, inf], optional)
   :type object_index: int
   :param index: (in [-1, inf], optional)
   :type index: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_loose(*, extend=False)

   Select loose geometry based on the selection mode

   :param extend: Extend, Extend the selection (optional)
   :type extend: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_mirror(*, axis={'X'}, extend=False)

   Select mesh items at mirrored locations

   :param axis: Axis, (optional)
   :type axis: set[Literal[:ref:`rna_enum_axis_flag_xyz_items`]]
   :param extend: Extend, Extend the existing selection (optional)
   :type extend: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_mode(*, use_extend=False, use_expand=False, type='VERT', action='TOGGLE')

   Change selection mode

   :param use_extend: Extend, (optional)
   :type use_extend: bool
   :param use_expand: Expand, (optional)
   :type use_expand: bool
   :param type: Type, (optional)
   :type type: Literal[:ref:`rna_enum_mesh_select_mode_items`]
   :param action: Action, Selection action to execute (optional)

      - ``DISABLE``
        Disable -- Disable the selection mode.
      - ``ENABLE``
        Enable -- Enable the selection mode.
      - ``TOGGLE``
        Toggle -- Toggle the selection mode.
   :type action: Literal['DISABLE', 'ENABLE', 'TOGGLE']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_more(*, use_face_step=True)

   Select more vertices, edges or faces connected to initial selection

   :param use_face_step: Face Step, Connected faces (instead of edges) (optional)
   :type use_face_step: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_next_item()

   Select the next element (using selection order)

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/mesh.py\:18 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/mesh.py#L18>`__

.. function:: select_non_manifold(*, extend=True, use_wire=True, use_boundary=True, use_multi_face=True, use_non_contiguous=True, use_verts=True)

   Select all non-manifold vertices or edges

   :param extend: Extend, Extend the selection (optional)
   :type extend: bool
   :param use_wire: Wire, Wire edges (optional)
   :type use_wire: bool
   :param use_boundary: Boundaries, Boundary edges (optional)
   :type use_boundary: bool
   :param use_multi_face: Multiple Faces, Edges shared by more than two faces (optional)
   :type use_multi_face: bool
   :param use_non_contiguous: Non Contiguous, Edges between faces pointing in alternate directions (optional)
   :type use_non_contiguous: bool
   :param use_verts: Vertices, Vertices connecting multiple face regions (optional)
   :type use_verts: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_nth(*, skip=1, nth=1, offset=0)

   Deselect every Nth element starting from the active vertex, edge or face

   :param skip: Deselected, Number of deselected elements in the repetitive sequence (in [1, inf], optional)
   :type skip: int
   :param nth: Selected, Number of selected elements in the repetitive sequence (in [1, inf], optional)
   :type nth: int
   :param offset: Offset, Offset from the starting point (in [-inf, inf], optional)
   :type offset: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_prev_item()

   Select the previous element (using selection order)

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/mesh.py\:43 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/mesh.py#L43>`__

.. function:: select_random(*, ratio=0.5, seed=0, action='SELECT')

   Randomly select vertices

   :param ratio: Ratio, Portion of items to select randomly (in [0, 1], optional)
   :type ratio: float
   :param seed: Random Seed, Seed for the random number generator (in [0, inf], optional)
   :type seed: int
   :param action: Action, Selection action to execute (optional)

      - ``SELECT``
        Select -- Select all elements.
      - ``DESELECT``
        Deselect -- Deselect all elements.
   :type action: Literal['SELECT', 'DESELECT']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_similar(*, type='VERT_NORMAL', compare='EQUAL', threshold=0.0)

   Select similar vertices, edges or faces by property types

   :param type: Type, (optional)
   :type type: Literal['VERT_NORMAL', 'VERT_FACES', 'VERT_GROUPS', 'VERT_EDGES', 'VERT_CREASE', 'EDGE_LENGTH', 'EDGE_DIR', 'EDGE_FACES', 'EDGE_FACE_ANGLE', 'EDGE_CREASE', 'EDGE_BEVEL', 'EDGE_SEAM', 'EDGE_SHARP', 'FACE_MATERIAL', 'FACE_AREA', 'FACE_SIDES', 'FACE_PERIMETER', 'FACE_NORMAL', 'FACE_COPLANAR', 'FACE_SMOOTH']
   :param compare: Compare, (optional)
   :type compare: Literal['EQUAL', 'GREATER', 'LESS']
   :param threshold: Threshold, (in [0, 100000], optional)
   :type threshold: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_similar_region()

   Select similar face regions to the current selection

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select_ungrouped(*, extend=False)

   Select vertices without a group

   :param extend: Extend, Extend the selection (optional)
   :type extend: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: separate(*, type='SELECTED')

   Separate selected geometry into a new mesh

   :param type: Type, (optional)
   :type type: Literal['SELECTED', 'MATERIAL', 'LOOSE']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: set_normals_from_faces(*, keep_sharp=False)

   Set the custom normals from the selected faces ones

   :param keep_sharp: Keep Sharp Edges, Do not set sharp edges to face (optional)
   :type keep_sharp: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: set_sharpness_by_angle(*, angle=0.523599, extend=False)

   Set edge sharpness based on the angle between neighboring faces

   :param angle: Angle, (in [0.000174533, 3.14159], optional)
   :type angle: float
   :param extend: Extend, Add new sharp edges without clearing existing sharp edges (optional)
   :type extend: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: shape_propagate_to_all()

   Apply selected vertex locations to all other shape keys

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: shortest_path_pick(*, edge_mode='SELECT', use_face_step=False, use_topology_distance=False, use_fill=False, skip=0, nth=1, offset=0, index=-1)

   Select shortest path between two selections

   :param edge_mode: Edge Tag, The edge flag to tag when selecting the shortest path (optional)
   :type edge_mode: Literal['SELECT', 'SEAM', 'SHARP', 'CREASE', 'BEVEL', 'FREESTYLE']
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
   :param index: (in [-1, inf], optional)
   :type index: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: shortest_path_select(*, edge_mode='SELECT', use_face_step=False, use_topology_distance=False, use_fill=False, skip=0, nth=1, offset=0)

   Select shortest path between two vertices/edges/faces

   :param edge_mode: Edge Tag, The edge flag to tag when selecting the shortest path (optional)
   :type edge_mode: Literal['SELECT', 'SEAM', 'SHARP', 'CREASE', 'BEVEL', 'FREESTYLE']
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

.. function:: smooth_normals(*, factor=0.5)

   Smooth custom normals based on adjacent vertex normals

   :param factor: Factor, Specifies weight of smooth vs original normal (in [0, 1], optional)
   :type factor: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: solidify(*, thickness=0.01)

   Create a solid skin by extruding, compensating for sharp angles

   :param thickness: Thickness, (in [-10000, 10000], optional)
   :type thickness: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: sort_elements(*, type='VIEW_ZAXIS', elements={'VERT'}, reverse=False, seed=0)

   The order of selected vertices/edges/faces is modified, based on a given method

   :param type: Type, Type of reordering operation to apply (optional)

      - ``VIEW_ZAXIS``
        View Z Axis -- Sort selected elements from farthest to nearest one in current view.
      - ``VIEW_XAXIS``
        View X Axis -- Sort selected elements from left to right one in current view.
      - ``CURSOR_DISTANCE``
        Cursor Distance -- Sort selected elements from nearest to farthest from 3D cursor.
      - ``MATERIAL``
        Material -- Sort selected faces from smallest to greatest material index.
      - ``SELECTED``
        Selected -- Move all selected elements in first places, preserving their relative order.
        Warning: This will affect unselected elements' indices as well.
      - ``RANDOMIZE``
        Randomize -- Randomize order of selected elements.
      - ``REVERSE``
        Reverse -- Reverse current order of selected elements.
   :type type: Literal['VIEW_ZAXIS', 'VIEW_XAXIS', 'CURSOR_DISTANCE', 'MATERIAL', 'SELECTED', 'RANDOMIZE', 'REVERSE']
   :param elements: Elements, Which elements to affect (vertices, edges and/or faces) (optional)
   :type elements: set[Literal['VERT', 'EDGE', 'FACE']]
   :param reverse: Reverse, Reverse the sorting effect (optional)
   :type reverse: bool
   :param seed: Seed, Seed for random-based operations (in [0, inf], optional)
   :type seed: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: spin(*, steps=12, dupli=False, angle=1.5708, use_auto_merge=True, use_normal_flip=False, center=(0.0, 0.0, 0.0), axis=(0.0, 0.0, 0.0))

   Extrude selected vertices in a circle around the cursor in indicated viewport

   :param steps: Steps, Steps (in [0, 1000000], optional)
   :type steps: int
   :param dupli: Use Duplicates, (optional)
   :type dupli: bool
   :param angle: Angle, Rotation for each step (in [-inf, inf], optional)
   :type angle: float
   :param use_auto_merge: Auto Merge, Merge first/last when the angle is a full revolution (optional)
   :type use_auto_merge: bool
   :param use_normal_flip: Flip Normals, (optional)
   :type use_normal_flip: bool
   :param center: Center, Center in global view space (array of 3 items, in [-inf, inf], optional)
   :type center: :class:`mathutils.Vector` | Sequence[float]
   :param axis: Axis, Axis in global view space (array of 3 items, in [-1, 1], optional)
   :type axis: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: split()

   Split off selected geometry from connected unselected geometry

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: split_normals()

   Split custom normals of selected vertices

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: subdivide(*, number_cuts=1, smoothness=0.0, ngon=True, quadcorner='STRAIGHT_CUT', fractal=0.0, fractal_along_normal=0.0, seed=0)

   Subdivide selected edges

   :param number_cuts: Number of Cuts, (in [1, 100], optional)
   :type number_cuts: int
   :param smoothness: Smoothness, Smoothness factor (in [0, 1000], optional)
   :type smoothness: float
   :param ngon: Create N-Gons, When disabled, newly created faces are limited to 3 and 4 sided faces (optional)
   :type ngon: bool
   :param quadcorner: Quad Corner Type, How to subdivide quad corners (anything other than Straight Cut will prevent n-gons) (optional)
   :type quadcorner: Literal['INNERVERT', 'PATH', 'STRAIGHT_CUT', 'FAN']
   :param fractal: Fractal, Fractal randomness factor (in [0, 1e+06], optional)
   :type fractal: float
   :param fractal_along_normal: Along Normal, Apply fractal displacement along normal only (in [0, 1], optional)
   :type fractal_along_normal: float
   :param seed: Random Seed, Seed for the random number generator (in [0, inf], optional)
   :type seed: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: subdivide_edgering(*, number_cuts=10, interpolation='PATH', smoothness=1.0, profile_shape_factor=0.0, profile_shape='SMOOTH')

   Subdivide perpendicular edges to the selected edge-ring

   :param number_cuts: Number of Cuts, (in [0, 1000], optional)
   :type number_cuts: int
   :param interpolation: Interpolation, Interpolation method (optional)
   :type interpolation: Literal['LINEAR', 'PATH', 'SURFACE']
   :param smoothness: Smoothness, Smoothness factor (in [0, 1000], optional)
   :type smoothness: float
   :param profile_shape_factor: Profile Factor, How much intermediary new edges are shrunk/expanded (in [-1000, 1000], optional)
   :type profile_shape_factor: float
   :param profile_shape: Profile Shape, Shape of the profile (optional)
   :type profile_shape: Literal[:ref:`rna_enum_proportional_falloff_curve_only_items`]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: symmetrize(*, direction='NEGATIVE_X', threshold=0.0001)

   Enforce symmetry (both form and topological) across an axis

   :param direction: Direction, Which sides to copy from and to (optional)
   :type direction: Literal[:ref:`rna_enum_symmetrize_direction_items`]
   :param threshold: Threshold, Limit for snap middle vertices to the axis center (in [0, 10], optional)
   :type threshold: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: symmetry_snap(*, direction='NEGATIVE_X', threshold=0.05, factor=0.5, use_center=True)

   Snap vertex pairs to their mirrored locations

   :param direction: Direction, Which sides to copy from and to (optional)
   :type direction: Literal[:ref:`rna_enum_symmetrize_direction_items`]
   :param threshold: Threshold, Distance within which matching vertices are searched (in [0, 10], optional)
   :type threshold: float
   :param factor: Factor, Mix factor of the locations of the vertices (in [0, 1], optional)
   :type factor: float
   :param use_center: Center, Snap middle vertices to the axis center (optional)
   :type use_center: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: tris_convert_to_quads(*, face_threshold=0.698132, shape_threshold=0.698132, topology_influence=0.0, uvs=False, vcols=False, seam=False, sharp=False, materials=False, deselect_joined=False)

   Merge triangles into four sided polygons where possible

   :param face_threshold: Max Face Angle, Face angle limit (in [0, 3.14159], optional)
   :type face_threshold: float
   :param shape_threshold: Max Shape Angle, Shape angle limit (in [0, 3.14159], optional)
   :type shape_threshold: float
   :param topology_influence: Topology Influence, How much to prioritize regular grids of quads as well as quads that touch existing quads (in [0, 2], optional)
   :type topology_influence: float
   :param uvs: Compare UVs, (optional)
   :type uvs: bool
   :param vcols: Compare Color Attributes, (optional)
   :type vcols: bool
   :param seam: Compare Seam, (optional)
   :type seam: bool
   :param sharp: Compare Sharp, (optional)
   :type sharp: bool
   :param materials: Compare Materials, (optional)
   :type materials: bool
   :param deselect_joined: Deselect Joined, Only select remaining triangles that were not merged (optional)
   :type deselect_joined: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: unsubdivide(*, iterations=2)

   Un-subdivide selected edges and faces

   :param iterations: Iterations, Number of times to un-subdivide (in [1, 1000], optional)
   :type iterations: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: uv_texture_add()

   Add UV map

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: uv_texture_remove()

   Remove UV map

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: uvs_reverse()

   Flip direction of UV coordinates inside faces

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: uvs_rotate(*, use_ccw=False)

   Rotate UV coordinates inside faces

   :param use_ccw: Counter Clockwise, (optional)
   :type use_ccw: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: vert_connect()

   Connect selected vertices of faces, splitting the face

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: vert_connect_concave()

   Split concave faces by connecting vertices to make them convex

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: vert_connect_nonplanar(*, angle_limit=0.0872665)

   Split non-planar faces that exceed the angle threshold

   :param angle_limit: Max Angle, Angle limit (in [0, 3.14159], optional)
   :type angle_limit: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: vert_connect_path()

   Connect vertices by their selection order, creating edges, splitting faces

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: vertices_smooth(*, factor=0.0, repeat=1, xaxis=True, yaxis=True, zaxis=True, wait_for_input=True)

   Flatten angles of selected vertices

   :param factor: Smoothing, Smoothing factor (in [-10, 10], optional)
   :type factor: float
   :param repeat: Repeat, Number of times to smooth the mesh (in [1, 1000], optional)
   :type repeat: int
   :param xaxis: X-Axis, Smooth along the X axis (optional)
   :type xaxis: bool
   :param yaxis: Y-Axis, Smooth along the Y axis (optional)
   :type yaxis: bool
   :param zaxis: Z-Axis, Smooth along the Z axis (optional)
   :type zaxis: bool
   :param wait_for_input: Wait for Input, (optional)
   :type wait_for_input: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: vertices_smooth_laplacian(*, repeat=1, lambda_factor=1.0, lambda_border=5e-05, use_x=True, use_y=True, use_z=True, preserve_volume=True)

   Laplacian smooth of selected vertices

   :param repeat: Number of iterations to smooth the mesh, (in [1, 1000], optional)
   :type repeat: int
   :param lambda_factor: Lambda factor, (in [1e-07, 1000], optional)
   :type lambda_factor: float
   :param lambda_border: Lambda factor in border, (in [1e-07, 1000], optional)
   :type lambda_border: float
   :param use_x: Smooth X Axis, Smooth object along X axis (optional)
   :type use_x: bool
   :param use_y: Smooth Y Axis, Smooth object along Y axis (optional)
   :type use_y: bool
   :param use_z: Smooth Z Axis, Smooth object along Z axis (optional)
   :type use_z: bool
   :param preserve_volume: Preserve Volume, Apply volume preservation after smooth (optional)
   :type preserve_volume: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: wireframe(*, use_boundary=True, use_even_offset=True, use_relative_offset=False, use_replace=True, thickness=0.01, offset=0.01, use_crease=False, crease_weight=0.01)

   Create a solid wireframe from faces

   :param use_boundary: Boundary, Inset face boundaries (optional)
   :type use_boundary: bool
   :param use_even_offset: Offset Even, Scale the offset to give more even thickness (optional)
   :type use_even_offset: bool
   :param use_relative_offset: Offset Relative, Scale the offset by surrounding geometry (optional)
   :type use_relative_offset: bool
   :param use_replace: Replace, Remove original faces (optional)
   :type use_replace: bool
   :param thickness: Thickness, (in [0, 10000], optional)
   :type thickness: float
   :param offset: Offset, (in [0, 10000], optional)
   :type offset: float
   :param use_crease: Crease, Crease hub edges for an improved subdivision surface (optional)
   :type use_crease: bool
   :param crease_weight: Crease Weight, (in [0, 1000], optional)
   :type crease_weight: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

