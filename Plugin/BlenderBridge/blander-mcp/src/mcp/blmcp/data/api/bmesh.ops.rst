
BMesh Operators (bmesh.ops)
===========================

.. module:: bmesh.ops

This module gives access to low level bmesh operations.

Most operators take input and return output, they can be chained together
to perform useful operations.


Operator Example
++++++++++++++++
This script shows how operators can be used to model a link of a chain.

.. literalinclude:: __/examples/bmesh.ops.1.py

.. function:: smooth_vert(bm, verts=[], factor=0, mirror_clip_x=False, mirror_clip_y=False, mirror_clip_z=False, clip_dist=0, use_axis_x=False, use_axis_y=False, use_axis_z=False)

   Vertex Smooth.

   Smooths vertices by using a basic vertex averaging scheme.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param verts:
      Input vertices.
   :type verts: list[:class:`bmesh.types.BMVert`]
   :param factor:
      Smoothing factor.
   :type factor: float
   :param mirror_clip_x:
      Set vertices close to the x axis before the operation to 0.
   :type mirror_clip_x: bool
   :param mirror_clip_y:
      Set vertices close to the y axis before the operation to 0.
   :type mirror_clip_y: bool
   :param mirror_clip_z:
      Set vertices close to the z axis before the operation to 0.
   :type mirror_clip_z: bool
   :param clip_dist:
      Clipping threshold for the above three slots.
   :type clip_dist: float
   :param use_axis_x:
      Smooth vertices along X axis.
   :type use_axis_x: bool
   :param use_axis_y:
      Smooth vertices along Y axis.
   :type use_axis_y: bool
   :param use_axis_z:
      Smooth vertices along Z axis.
   :type use_axis_z: bool


.. function:: smooth_laplacian_vert(bm, verts=[], lambda_factor=0, lambda_border=0, use_x=False, use_y=False, use_z=False, preserve_volume=False)

   Vertex Smooth Laplacian.

   Smooths vertices by using Laplacian smoothing proposed by
   Desbrun, et al. Implicit Fairing of Irregular Meshes using Diffusion and Curvature Flow.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param verts:
      Input vertices.
   :type verts: list[:class:`bmesh.types.BMVert`]
   :param lambda_factor:
      Lambda parameter.
   :type lambda_factor: float
   :param lambda_border:
      Lambda param in border.
   :type lambda_border: float
   :param use_x:
      Smooth object along X axis.
   :type use_x: bool
   :param use_y:
      Smooth object along Y axis.
   :type use_y: bool
   :param use_z:
      Smooth object along Z axis.
   :type use_z: bool
   :param preserve_volume:
      Apply volume preservation after smooth.
   :type preserve_volume: bool


.. function:: recalc_face_normals(bm, faces=[])

   Right-Hand Faces.

   Computes an "outside" normal for the specified input faces.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param faces:
      Input faces.
   :type faces: list[:class:`bmesh.types.BMFace`]


.. function:: planar_faces(bm, faces=[], iterations=0, factor=0)

   Planar Faces.

   Iteratively flatten faces.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param faces:
      Input geometry.
   :type faces: list[:class:`bmesh.types.BMFace`]
   :param iterations:
      Number of times to flatten faces (for when connected faces are used)
   :type iterations: int
   :param factor:
      Influence for making planar each iteration
   :type factor: float
   :return:

      - ``geom``:
        Output slot, computed boundary geometry.

        **type** list[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`]

   :rtype: dict[str, Any]


.. function:: region_extend(bm, geom=[], use_contract=False, use_faces=False, use_face_step=False)

   Region Extend.

   Used to implement the select more/less tools.
   Puts geometry surrounding regions of geometry in ``geom`` into ``geom.out``.

   If ``use_faces`` is 0 then ``geom.out`` spits out verts and edges,
   otherwise it spits out faces.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param geom:
      Input geometry.
   :type geom: list[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`]
   :param use_contract:
      Find boundary inside the regions, not outside.
   :type use_contract: bool
   :param use_faces:
      Extend from faces instead of edges.
   :type use_faces: bool
   :param use_face_step:
      Step over connected faces.
   :type use_face_step: bool
   :return:

      - ``geom``:
        Output slot, computed boundary geometry.

        **type** list[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`]

   :rtype: dict[str, Any]


.. function:: rotate_edges(bm, edges=[], use_ccw=False)

   Edge Rotate.

   Rotates edges topologically. Also known as "spin edge" to some people.
   Simple example: ``[/] becomes [|] then [\]``.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param edges:
      Input edges.
   :type edges: list[:class:`bmesh.types.BMEdge`]
   :param use_ccw:
      Rotate edge counter-clockwise if true, otherwise clockwise.
   :type use_ccw: bool
   :return:

      - ``edges``:
        Newly spun edges.

        **type** list[:class:`bmesh.types.BMEdge`]

   :rtype: dict[str, Any]


.. function:: reverse_faces(bm, faces=[], flip_multires=False)

   Reverse Faces.

   Reverses the winding (vertex order) of faces.
   This has the effect of flipping the normal.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param faces:
      Input faces.
   :type faces: list[:class:`bmesh.types.BMFace`]
   :param flip_multires:
      Maintain multi-res offset.
   :type flip_multires: bool


.. function:: flip_quad_tessellation(bm, faces=[])

   Flip Quad Tessellation

   Flip the tessellation direction of the selected quads.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param faces:
      Input faces.
   :type faces: list[:class:`bmesh.types.BMFace`]


.. function:: bisect_edges(bm, edges=[], cuts=0, edge_percents={})

   Edge Bisect.

   Splits input edges (but doesn't do anything else).
   This creates a 2-valence vert.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param edges:
      Input edges.
   :type edges: list[:class:`bmesh.types.BMEdge`]
   :param cuts:
      Number of cuts.
   :type cuts: int
   :param edge_percents:
      Undocumented.
   :type edge_percents: dict[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`, float]
   :return:

      - ``geom_split``:
        Newly created vertices and edges.

        **type** list[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`]

   :rtype: dict[str, Any]


.. function:: mirror(bm, geom=[], matrix=mathutils.Matrix.Identity(4), merge_dist=0, axis='X', mirror_u=False, mirror_v=False, mirror_udim=False, use_shapekey=False)

   Mirror.

   Mirrors geometry along an axis. The resulting geometry is welded on using
   ``merge_dist``. Pairs of original/mirrored vertices are welded using the ``merge_dist``
   parameter (which defines the minimum distance for welding to happen).

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param geom:
      Input geometry.
   :type geom: list[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`]
   :param matrix:
      Matrix defining the mirror transformation.
   :type matrix: :class:`mathutils.Matrix`
   :param merge_dist:
      Maximum distance for merging. does no merging if 0.
   :type merge_dist: float
   :param axis:
      The axis to use.
   :type axis: Literal['X', 'Y', 'Z']
   :param mirror_u:
      Mirror UVs across the u axis.
   :type mirror_u: bool
   :param mirror_v:
      Mirror UVs across the v axis.
   :type mirror_v: bool
   :param mirror_udim:
      Mirror UVs in each tile.
   :type mirror_udim: bool
   :param use_shapekey:
      Transform shape keys too.
   :type use_shapekey: bool
   :return:

      - ``geom``:
        Output geometry, mirrored.

        **type** list[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`]

   :rtype: dict[str, Any]


.. function:: find_doubles(bm, verts=[], keep_verts=[], use_connected=False, dist=0)

   Find Doubles.

   Takes input verts and finds vertices they should weld to.
   Outputs a mapping slot suitable for use with the weld verts BMOP.

   If ``keep_verts`` is used, vertices outside that set can only be merged
   with vertices in that set.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param verts:
      Input vertices.
   :type verts: list[:class:`bmesh.types.BMVert`]
   :param keep_verts:
      List of verts to keep.
   :type keep_verts: list[:class:`bmesh.types.BMVert`]
   :param use_connected:
      Limit the search for doubles by connected geometry.
   :type use_connected: bool
   :param dist:
      Maximum distance.
   :type dist: float
   :return:

      - ``targetmap``:

        **type** dict[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`, :class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`]

   :rtype: dict[str, Any]


.. function:: remove_doubles(bm, verts=[], use_connected=False, dist=0)

   Remove Doubles.

   Finds groups of vertices closer than dist and merges them together,
   using the weld verts BMOP.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param verts:
      Input verts.
   :type verts: list[:class:`bmesh.types.BMVert`]
   :param use_connected:
      Limit the search for doubles by connected geometry.
   :type use_connected: bool
   :param dist:
      Maximum distance.
   :type dist: float


.. function:: collapse(bm, edges=[], uvs=False)

   Collapse Connected.

   Collapses connected vertices

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param edges:
      Input edges.
   :type edges: list[:class:`bmesh.types.BMEdge`]
   :param uvs:
      Also collapse UVs and such.
   :type uvs: bool


.. function:: pointmerge_facedata(bm, verts=[], vert_snap=None)

   Face-Data Point Merge.

   Merge uv/vcols at a specific vertex.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param verts:
      Input vertices.
   :type verts: list[:class:`bmesh.types.BMVert`]
   :param vert_snap:
      Snap vertex.
   :type vert_snap: :class:`bmesh.types.BMVert` | None


.. function:: average_vert_facedata(bm, verts=[])

   Average Vertices Face-vert Data.

   Merge uv/vcols associated with the input vertices at
   the bounding box center.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param verts:
      Input vertices.
   :type verts: list[:class:`bmesh.types.BMVert`]


.. function:: pointmerge(bm, verts=[], merge_co=mathutils.Vector())

   Point Merge.

   Merge verts together at a point.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param verts:
      Input vertices (all verts will be merged into the first).
   :type verts: list[:class:`bmesh.types.BMVert`]
   :param merge_co:
      Position to merge at.
   :type merge_co: Sequence[float]


.. function:: collapse_uvs(bm, edges=[])

   Collapse Connected UVs.

   Collapses connected UV vertices.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param edges:
      Input edges.
   :type edges: list[:class:`bmesh.types.BMEdge`]


.. function:: weld_verts(bm, targetmap={}, use_centroid=False)

   Weld Verts.

   Welds verts together (kind-of like remove doubles, merge, etc, all of which
   use or will use this BMOP). You pass in mappings from vertices to the vertices
   they weld with.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param targetmap:
      Maps welded vertices to verts they should weld to.
   :type targetmap: dict[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`, :class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`]
   :param use_centroid:
      Merge vertices to their centroid position,
      otherwise use the position of the target vertex.
   :type use_centroid: bool


.. function:: create_vert(bm, co=mathutils.Vector())

   Make Vertex.

   Creates a single vertex; this BMOP was necessary
   for click-create-vertex.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param co:
      The coordinate of the new vert.
   :type co: Sequence[float]
   :return:

      - ``vert``:
        The new vert.

        **type** list[:class:`bmesh.types.BMVert`]

   :rtype: dict[str, Any]


.. function:: join_triangles(bm, faces=[], cmp_seam=False, cmp_sharp=False, cmp_uvs=False, cmp_vcols=False, cmp_materials=False, angle_face_threshold=0, angle_shape_threshold=0, topology_influence=0, deselect_joined=False, merge_limit=0, neighbor_debug=0)

   Join Triangles.

   Tries to intelligently join triangles according
   to angle threshold and delimiters.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param faces:
      Input geometry.
   :type faces: list[:class:`bmesh.types.BMFace`]
   :param cmp_seam:
      Compare seam
   :type cmp_seam: bool
   :param cmp_sharp:
      Compare sharp
   :type cmp_sharp: bool
   :param cmp_uvs:
      Compare UVs
   :type cmp_uvs: bool
   :param cmp_vcols:
      Compare VCols.
   :type cmp_vcols: bool
   :param cmp_materials:
      Compare materials.
   :type cmp_materials: bool
   :param angle_face_threshold:
      Undocumented.
   :type angle_face_threshold: float
   :param angle_shape_threshold:
      Undocumented.
   :type angle_shape_threshold: float
   :param topology_influence:
      Undocumented.
   :type topology_influence: float
   :param deselect_joined:
      Undocumented.
   :type deselect_joined: bool
   :param merge_limit:
      Undocumented.
   :type merge_limit: int
   :param neighbor_debug:
      Undocumented.
   :type neighbor_debug: int
   :return:

      - ``faces``:
        Joined faces.

        **type** list[:class:`bmesh.types.BMFace`]

   :rtype: dict[str, Any]


.. function:: contextual_create(bm, geom=[], mat_nr=0, use_smooth=False)

   Contextual Create.

   This is basically F-key, it creates
   new faces from vertices, makes stuff from edge nets,
   makes wire edges, etc. It also dissolves faces.

   Three verts become a triangle, four become a quad. Two
   become a wire edge.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param geom:
      Input geometry.
   :type geom: list[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`]
   :param mat_nr:
      Material to use.
   :type mat_nr: int
   :param use_smooth:
      Set smooth shading on newly created faces.
   :type use_smooth: bool
   :return:

      - ``faces``:
        Newly-made face(s).

        **type** list[:class:`bmesh.types.BMFace`]
      - ``edges``:
        Newly-made edge(s).

        **type** list[:class:`bmesh.types.BMEdge`]

   :rtype: dict[str, Any]


.. function:: bridge_loops(bm, edges=[], use_pairs=False, use_cyclic=False, use_merge=False, merge_factor=0, twist_offset=0)

   Bridge edge loops with faces.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param edges:
      Input edges.
   :type edges: list[:class:`bmesh.types.BMEdge`]
   :param use_pairs:
      Undocumented.
   :type use_pairs: bool
   :param use_cyclic:
      Undocumented.
   :type use_cyclic: bool
   :param use_merge:
      Merge rather than creating faces.
   :type use_merge: bool
   :param merge_factor:
      Merge factor.
   :type merge_factor: float
   :param twist_offset:
      Twist offset for closed loops.
   :type twist_offset: int
   :return:

      - ``faces``:
        New faces.

        **type** list[:class:`bmesh.types.BMFace`]
      - ``edges``:
        New edges.

        **type** list[:class:`bmesh.types.BMEdge`]

   :rtype: dict[str, Any]


.. function:: grid_fill(bm, edges=[], mat_nr=0, use_smooth=False, use_interp_simple=False)

   Grid Fill.

   Create faces defined by 2 disconnected edge loops (which share edges).

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param edges:
      Input edges.
   :type edges: list[:class:`bmesh.types.BMEdge`]
   :param mat_nr:
      Material to use.
   :type mat_nr: int
   :param use_smooth:
      Smooth state to use.
   :type use_smooth: bool
   :param use_interp_simple:
      Use simple interpolation.
   :type use_interp_simple: bool
   :return:

      - ``faces``:
        New faces.

        **type** list[:class:`bmesh.types.BMFace`]

   :rtype: dict[str, Any]


.. function:: holes_fill(bm, edges=[], sides=0)

   Fill Holes.

   Fill boundary edges with faces, copying surrounding custom-data.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param edges:
      Input edges.
   :type edges: list[:class:`bmesh.types.BMEdge`]
   :param sides:
      Maximum number of sides for holes to fill (holes with more edges are skipped).
   :type sides: int
   :return:

      - ``faces``:
        New faces.

        **type** list[:class:`bmesh.types.BMFace`]

   :rtype: dict[str, Any]


.. function:: face_attribute_fill(bm, faces=[], use_normals=False, use_data=False)

   Face Attribute Fill.

   Fill in faces with data from adjacent faces.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param faces:
      Input faces.
   :type faces: list[:class:`bmesh.types.BMFace`]
   :param use_normals:
      Copy face winding.
   :type use_normals: bool
   :param use_data:
      Copy face data.
   :type use_data: bool
   :return:

      - ``faces_fail``:
        Faces that could not be handled.

        **type** list[:class:`bmesh.types.BMFace`]

   :rtype: dict[str, Any]


.. function:: edgeloop_fill(bm, edges=[], mat_nr=0, use_smooth=False)

   Edge Loop Fill.

   Create faces defined by one or more non overlapping edge loops.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param edges:
      Input edges.
   :type edges: list[:class:`bmesh.types.BMEdge`]
   :param mat_nr:
      Material to use.
   :type mat_nr: int
   :param use_smooth:
      Smooth state to use.
   :type use_smooth: bool
   :return:

      - ``faces``:
        New faces.

        **type** list[:class:`bmesh.types.BMFace`]

   :rtype: dict[str, Any]


.. function:: edgenet_fill(bm, edges=[], mat_nr=0, use_smooth=False, sides=0)

   Edge Net Fill.

   Create faces defined by enclosed edges.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param edges:
      Input edges.
   :type edges: list[:class:`bmesh.types.BMEdge`]
   :param mat_nr:
      Material to use.
   :type mat_nr: int
   :param use_smooth:
      Smooth state to use.
   :type use_smooth: bool
   :param sides:
      Maximum number of sides for created faces.
   :type sides: int
   :return:

      - ``faces``:
        New faces.

        **type** list[:class:`bmesh.types.BMFace`]

   :rtype: dict[str, Any]


.. function:: edgenet_prepare(bm, edges=[])

   Edge-net Prepare.

   Identifies several useful edge loop cases and modifies them so
   they'll become a face when edgenet_fill is called. The cases covered are:

   - One single loop; an edge is added to connect the ends
   - Two loops; two edges are added to connect the endpoints (based on the
     shortest distance between each endpoint).

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param edges:
      Input edges.
   :type edges: list[:class:`bmesh.types.BMEdge`]
   :return:

      - ``edges``:
        New edges.

        **type** list[:class:`bmesh.types.BMEdge`]

   :rtype: dict[str, Any]


.. function:: rotate(bm, cent=mathutils.Vector(), matrix=mathutils.Matrix.Identity(4), verts=[], space=mathutils.Matrix.Identity(4), use_shapekey=False)

   Rotate.

   Rotate vertices around a center, using a 3x3 rotation matrix.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param cent:
      Center of rotation.
   :type cent: Sequence[float]
   :param matrix:
      Matrix defining rotation.
   :type matrix: :class:`mathutils.Matrix`
   :param verts:
      Input vertices.
   :type verts: list[:class:`bmesh.types.BMVert`]
   :param space:
      Matrix to define the space (typically object matrix).
   :type space: :class:`mathutils.Matrix`
   :param use_shapekey:
      Transform shape keys too.
   :type use_shapekey: bool


.. function:: translate(bm, vec=mathutils.Vector(), space=mathutils.Matrix.Identity(4), verts=[], use_shapekey=False)

   Translate.

   Translate vertices by an offset.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param vec:
      Translation offset.
   :type vec: Sequence[float]
   :param space:
      Matrix to define the space (typically object matrix).
   :type space: :class:`mathutils.Matrix`
   :param verts:
      Input vertices.
   :type verts: list[:class:`bmesh.types.BMVert`]
   :param use_shapekey:
      Transform shape keys too.
   :type use_shapekey: bool


.. function:: scale(bm, vec=mathutils.Vector(), space=mathutils.Matrix.Identity(4), verts=[], use_shapekey=False)

   Scale.

   Scales vertices by a factor.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param vec:
      Scale factor.
   :type vec: Sequence[float]
   :param space:
      Matrix to define the space (typically object matrix).
   :type space: :class:`mathutils.Matrix`
   :param verts:
      Input vertices.
   :type verts: list[:class:`bmesh.types.BMVert`]
   :param use_shapekey:
      Transform shape keys too.
   :type use_shapekey: bool


.. function:: transform(bm, matrix=mathutils.Matrix.Identity(4), space=mathutils.Matrix.Identity(4), verts=[], use_shapekey=False)

   Transform.

   Transforms a set of vertices by a matrix. Multiplies
   the vertex coordinates with the matrix.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param matrix:
      Transform matrix.
   :type matrix: :class:`mathutils.Matrix`
   :param space:
      Matrix to define the space (typically object matrix).
   :type space: :class:`mathutils.Matrix`
   :param verts:
      Input vertices.
   :type verts: list[:class:`bmesh.types.BMVert`]
   :param use_shapekey:
      Transform shape keys too.
   :type use_shapekey: bool


.. function:: object_load_bmesh(bm, scene, object)

   Object Load BMesh.

   Loads a bmesh into an object/mesh. This is a "private"
   BMOP.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param scene:
      The scene.
   :type scene: :class:`bpy.types.Scene`
   :param object:
      The object.
   :type object: :class:`bpy.types.Object`


.. function:: bmesh_to_mesh(bm, mesh, object)

   BMesh to Mesh.

   Converts a bmesh to a Mesh. This is reserved for exiting edit-mode.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param mesh:
      The mesh to write into.
   :type mesh: :class:`bpy.types.Mesh`
   :param object:
      The object.
   :type object: :class:`bpy.types.Object`


.. function:: mesh_to_bmesh(bm, mesh, object, use_shapekey=False)

   Mesh to BMesh.

   Load the contents of a mesh into the bmesh. this BMOP is private, it's
   reserved exclusively for entering edit-mode.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param mesh:
      The mesh to read from.
   :type mesh: :class:`bpy.types.Mesh`
   :param object:
      The object.
   :type object: :class:`bpy.types.Object`
   :param use_shapekey:
      Load active shapekey coordinates into verts.
   :type use_shapekey: bool


.. function:: extrude_discrete_faces(bm, faces=[], use_normal_flip=False, use_select_history=False)

   Individual Face Extrude.

   Extrudes faces individually.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param faces:
      Input faces.
   :type faces: list[:class:`bmesh.types.BMFace`]
   :param use_normal_flip:
      Create faces with reversed direction.
   :type use_normal_flip: bool
   :param use_select_history:
      Preserve the selection history in the extruded geometry.
   :type use_select_history: bool
   :return:

      - ``faces``:
        Output faces.

        **type** list[:class:`bmesh.types.BMFace`]

   :rtype: dict[str, Any]


.. function:: extrude_edge_only(bm, edges=[], use_normal_flip=False, use_select_history=False)

   Extrude Only Edges.

   Extrudes Edges into faces, note that this is very simple, there's no fancy
   winged extrusion.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param edges:
      Input edges.
   :type edges: list[:class:`bmesh.types.BMEdge`]
   :param use_normal_flip:
      Create faces with reversed direction.
   :type use_normal_flip: bool
   :param use_select_history:
      Preserve the selection history in the extruded geometry.
   :type use_select_history: bool
   :return:

      - ``geom``:
        Output geometry.

        **type** list[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`]

   :rtype: dict[str, Any]


.. function:: extrude_vert_indiv(bm, verts=[], use_select_history=False)

   Individual Vertex Extrude.

   Extrudes individual vertices, creating new vertices connected by wire edges.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param verts:
      Input vertices.
   :type verts: list[:class:`bmesh.types.BMVert`]
   :param use_select_history:
      Preserve the selection history in the extruded geometry.
   :type use_select_history: bool
   :return:

      - ``edges``:
        Output wire edges.

        **type** list[:class:`bmesh.types.BMEdge`]
      - ``verts``:
        Output vertices.

        **type** list[:class:`bmesh.types.BMVert`]

   :rtype: dict[str, Any]


.. function:: connect_verts(bm, verts=[], faces_exclude=[], check_degenerate=False)

   Connect Verts.

   Split faces by adding edges that connect ``verts``.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param verts:
      Input vertices.
   :type verts: list[:class:`bmesh.types.BMVert`]
   :param faces_exclude:
      Input faces to explicitly exclude from connecting.
   :type faces_exclude: list[:class:`bmesh.types.BMFace`]
   :param check_degenerate:
      Prevent splits with overlaps & intersections.
   :type check_degenerate: bool
   :return:

      - ``edges``:

        **type** list[:class:`bmesh.types.BMEdge`]

   :rtype: dict[str, Any]


.. function:: connect_verts_concave(bm, faces=[])

   Connect Verts to form Convex Faces.

   Splits concave faces into convex faces.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param faces:
      Input faces.
   :type faces: list[:class:`bmesh.types.BMFace`]
   :return:

      - ``edges``:

        **type** list[:class:`bmesh.types.BMEdge`]
      - ``faces``:

        **type** list[:class:`bmesh.types.BMFace`]

   :rtype: dict[str, Any]


.. function:: connect_verts_nonplanar(bm, angle_limit=0, faces=[])

   Connect Verts Across non Planar Faces.

   Split faces by connecting edges along non planar ``faces``.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param angle_limit:
      Maximum angle of non-planarity before splitting (radians).
   :type angle_limit: float
   :param faces:
      Input faces.
   :type faces: list[:class:`bmesh.types.BMFace`]
   :return:

      - ``edges``:

        **type** list[:class:`bmesh.types.BMEdge`]
      - ``faces``:

        **type** list[:class:`bmesh.types.BMFace`]

   :rtype: dict[str, Any]


.. function:: connect_vert_pair(bm, verts=[], verts_exclude=[], faces_exclude=[])

   Connect Vert Pair.

   Connect a pair of vertices by splitting faces along the shortest path between them.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param verts:
      Input vertices.
   :type verts: list[:class:`bmesh.types.BMVert`]
   :param verts_exclude:
      Input vertices to explicitly exclude from connecting.
   :type verts_exclude: list[:class:`bmesh.types.BMVert`]
   :param faces_exclude:
      Input faces to explicitly exclude from connecting.
   :type faces_exclude: list[:class:`bmesh.types.BMFace`]
   :return:

      - ``edges``:

        **type** list[:class:`bmesh.types.BMEdge`]

   :rtype: dict[str, Any]


.. function:: extrude_face_region(bm, geom=[], edges_exclude=set(), use_keep_orig=False, use_normal_flip=False, use_normal_from_adjacent=False, use_dissolve_ortho_edges=False, use_select_history=False, skip_input_flip=False)

   Extrude Faces.

   Extrude operator (does not transform)

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param geom:
      Edges and faces.
   :type geom: list[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`]
   :param edges_exclude:
      Input edges to explicitly exclude from extrusion.
   :type edges_exclude: set[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`]
   :param use_keep_orig:
      Keep original geometry (requires `geom` to include edges).
   :type use_keep_orig: bool
   :param use_normal_flip:
      Create faces with reversed direction.
   :type use_normal_flip: bool
   :param use_normal_from_adjacent:
      Use winding from surrounding faces instead of this region.
   :type use_normal_from_adjacent: bool
   :param use_dissolve_ortho_edges:
      Dissolve edges whose faces form a flat surface.
   :type use_dissolve_ortho_edges: bool
   :param use_select_history:
      Preserve the selection history in the extruded geometry.
   :type use_select_history: bool
   :param skip_input_flip:
      Skip flipping of input faces to preserve original orientation.
   :type skip_input_flip: bool
   :return:

      - ``geom``:

        **type** list[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`]

   :rtype: dict[str, Any]


.. function:: dissolve_verts(bm, verts=[], use_face_split=False, use_boundary_tear=False)

   Dissolve Verts.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param verts:
      Input vertices.
   :type verts: list[:class:`bmesh.types.BMVert`]
   :param use_face_split:
      Split off face corners to maintain surrounding geometry.
   :type use_face_split: bool
   :param use_boundary_tear:
      Split off face corners instead of merging faces.
   :type use_boundary_tear: bool


.. function:: dissolve_edges(bm, edges=[], use_verts=False, use_face_split=False, angle_threshold=0)

   Dissolve Edges.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param edges:
      Input edges.
   :type edges: list[:class:`bmesh.types.BMEdge`]
   :param use_verts:
      Dissolve verts left between only 2 edges.
   :type use_verts: bool
   :param use_face_split:
      Split off face corners to maintain surrounding geometry.
   :type use_face_split: bool
   :param angle_threshold:
      Do not dissolve verts between 2 edges when their angle exceeds this threshold.
      Disabled by default.
   :type angle_threshold: float
   :return:

      - ``region``:

        **type** list[:class:`bmesh.types.BMFace`]

   :rtype: dict[str, Any]


.. function:: dissolve_faces(bm, faces=[], use_verts=False)

   Dissolve Faces.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param faces:
      Input faces.
   :type faces: list[:class:`bmesh.types.BMFace`]
   :param use_verts:
      Dissolve verts left between only 2 edges.
   :type use_verts: bool
   :return:

      - ``region``:

        **type** list[:class:`bmesh.types.BMFace`]

   :rtype: dict[str, Any]


.. function:: dissolve_limit(bm, angle_limit=0, use_dissolve_boundaries=False, verts=[], edges=[], delimit=set())

   Limited Dissolve.

   Dissolve planar faces and co-linear edges.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param angle_limit:
      Maximum angle (radians) between face normals for dissolving.
   :type angle_limit: float
   :param use_dissolve_boundaries:
      Dissolve all vertices in between face boundaries.
   :type use_dissolve_boundaries: bool
   :param verts:
      Input vertices.
   :type verts: list[:class:`bmesh.types.BMVert`]
   :param edges:
      Input edges.
   :type edges: list[:class:`bmesh.types.BMEdge`]
   :param delimit:
      Delimit dissolve operation.
   :type delimit: set[Literal['NORMAL', 'MATERIAL', 'SEAM', 'SHARP', 'UV']]
   :return:

      - ``region``:

        **type** list[:class:`bmesh.types.BMFace`]

   :rtype: dict[str, Any]


.. function:: dissolve_degenerate(bm, dist=0, edges=[])

   Degenerate Dissolve.

   Dissolve edges with no length, faces with no area.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param dist:
      Maximum distance to consider degenerate.
   :type dist: float
   :param edges:
      Input edges.
   :type edges: list[:class:`bmesh.types.BMEdge`]


.. function:: triangulate(bm, faces=[], quad_method='BEAUTY', ngon_method='BEAUTY')

   Triangulate.

   Triangulate faces, splitting quads and n-gons into triangles.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param faces:
      Input faces.
   :type faces: list[:class:`bmesh.types.BMFace`]
   :param quad_method:
      Method for splitting the quads into triangles.
   :type quad_method: Literal['BEAUTY', 'FIXED', 'ALTERNATE', 'SHORT_EDGE', 'LONG_EDGE']
   :param ngon_method:
      Method for splitting the polygons into triangles.
   :type ngon_method: Literal['BEAUTY', 'EAR_CLIP']
   :return:

      - ``edges``:

        **type** list[:class:`bmesh.types.BMEdge`]
      - ``faces``:

        **type** list[:class:`bmesh.types.BMFace`]
      - ``face_map``:

        **type** dict[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`, :class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`]
      - ``face_map_double``:
        Duplicate faces.

        **type** dict[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`, :class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`]

   :rtype: dict[str, Any]


.. function:: unsubdivide(bm, verts=[], iterations=0)

   Un-Subdivide.

   Reduce detail in geometry containing grids.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param verts:
      Input vertices.
   :type verts: list[:class:`bmesh.types.BMVert`]
   :param iterations:
      Number of times to unsubdivide.
   :type iterations: int


.. function:: subdivide_edges(bm, edges=[], smooth=0, smooth_falloff='SMOOTH', fractal=0, along_normal=0, cuts=0, seed=0, custom_patterns={}, edge_percents={}, quad_corner_type='STRAIGHT_CUT', use_grid_fill=False, use_single_edge=False, use_only_quads=False, use_sphere=False, use_smooth_even=False)

   Subdivide Edges.

   Advanced operator for subdividing edges
   with options for face patterns, smoothing and randomization.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param edges:
      Input edges.
   :type edges: list[:class:`bmesh.types.BMEdge`]
   :param smooth:
      Smoothness factor.
   :type smooth: float
   :param smooth_falloff:
      Smooth falloff type.
   :type smooth_falloff: Literal['SMOOTH', 'SPHERE', 'ROOT', 'SHARP', 'LINEAR', 'INVERSE_SQUARE']
   :param fractal:
      Fractal randomness factor.
   :type fractal: float
   :param along_normal:
      Factor (0 to 1) controlling how much fractal displacement is restricted to the normal.
   :type along_normal: float
   :param cuts:
      Number of cuts.
   :type cuts: int
   :param seed:
      Seed for the random number generator.
   :type seed: int
   :param custom_patterns:
      Internal use only, not accessible from Python.
   :type custom_patterns: dict
   :param edge_percents:
      Mapping of edges to a float (0 to 1) controlling the cut position along each edge.
   :type edge_percents: dict[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`, float]
   :param quad_corner_type:
      Quad corner type.
   :type quad_corner_type: Literal['STRAIGHT_CUT', 'INNER_VERT', 'PATH', 'FAN']
   :param use_grid_fill:
      Fill in fully-selected faces with a grid.
   :type use_grid_fill: bool
   :param use_single_edge:
      Tessellate the case of one edge selected in a quad or triangle.
   :type use_single_edge: bool
   :param use_only_quads:
      Only subdivide quads (for loop-cut).
   :type use_only_quads: bool
   :param use_sphere:
      Project new vertices onto a sphere (used for spherical primitives).
   :type use_sphere: bool
   :param use_smooth_even:
      Maintain even offset when smoothing.
   :type use_smooth_even: bool
   :return:

      - ``geom_inner``:

        **type** list[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`]
      - ``geom_split``:

        **type** list[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`]
      - ``geom``:
        Contains all output geometry.

        **type** list[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`]

   :rtype: dict[str, Any]


.. function:: subdivide_edgering(bm, edges=[], interp_mode='LINEAR', smooth=0, cuts=0, profile_shape='SMOOTH', profile_shape_factor=0)

   Subdivide Edge-Ring.

   Take an edge-ring, and subdivide with interpolation options.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param edges:
      Input edges.
   :type edges: list[:class:`bmesh.types.BMEdge`]
   :param interp_mode:
      Interpolation method.
   :type interp_mode: Literal['LINEAR', 'PATH', 'SURFACE']
   :param smooth:
      Smoothness factor.
   :type smooth: float
   :param cuts:
      Number of cuts.
   :type cuts: int
   :param profile_shape:
      Profile shape type.
   :type profile_shape: Literal['SMOOTH', 'SPHERE', 'ROOT', 'SHARP', 'LINEAR', 'INVERSE_SQUARE']
   :param profile_shape_factor:
      How much intermediary new edges are shrunk/expanded.
   :type profile_shape_factor: float
   :return:

      - ``faces``:
        Output faces.

        **type** list[:class:`bmesh.types.BMFace`]

   :rtype: dict[str, Any]


.. function:: bisect_plane(bm, geom=[], dist=0, plane_co=mathutils.Vector(), plane_no=mathutils.Vector(), use_snap_center=False, clear_outer=False, clear_inner=False)

   Bisect Plane.

   Bisects the mesh by a plane (cut the mesh in half).

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param geom:
      Input geometry.
   :type geom: list[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`]
   :param dist:
      Minimum distance when testing if a vert is exactly on the plane.
   :type dist: float
   :param plane_co:
      Point on the plane.
   :type plane_co: Sequence[float]
   :param plane_no:
      Normal of the plane.
   :type plane_no: Sequence[float]
   :param use_snap_center:
      Snap axis aligned verts to the center.
   :type use_snap_center: bool
   :param clear_outer:
      When enabled, remove all geometry on the positive side of the plane.
   :type clear_outer: bool
   :param clear_inner:
      When enabled, remove all geometry on the negative side of the plane.
   :type clear_inner: bool
   :return:

      - ``geom_cut``:
        Output geometry aligned with the plane (new and existing).

        **type** list[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge`]
      - ``geom``:
        Input and output geometry (result of cut).

        **type** list[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`]

   :rtype: dict[str, Any]


.. function:: delete(bm, geom=[], context='VERTS')

   Delete Geometry.

   Utility operator to delete geometry.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param geom:
      Input geometry.
   :type geom: list[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`]
   :param context:
      Geometry types to delete.
   :type context: Literal['VERTS', 'EDGES', 'FACES_ONLY', 'EDGES_FACES', 'FACES', 'FACES_KEEP_BOUNDARY', 'TAGGED_ONLY']


.. function:: duplicate(bm, geom=[], dest=None, use_select_history=False, use_edge_flip_from_face=False)

   Duplicate Geometry.

   Utility operator to duplicate geometry,
   optionally into a destination mesh.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param geom:
      Input geometry.
   :type geom: list[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`]
   :param dest:
      Destination bmesh, if None will use current one.
   :type dest: :class:`bmesh.types.BMesh` | None
   :param use_select_history:
      Preserve the selection history in the duplicated geometry.
   :type use_select_history: bool
   :param use_edge_flip_from_face:
      Copy edge flip state from connected faces.
   :type use_edge_flip_from_face: bool
   :return:

      - ``geom_orig``:

        **type** list[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`]
      - ``geom``:

        **type** list[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`]
      - ``vert_map``:

        **type** dict[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`, :class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`]
      - ``edge_map``:

        **type** dict[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`, :class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`]
      - ``face_map``:

        **type** dict[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`, :class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`]
      - ``boundary_map``:
        Boundary edges from the split geometry that maps edges from the original geometry
        to the destination edges.

        **type** dict[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`, :class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`]
      - ``isovert_map``:

        **type** dict[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`, :class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`]

   :rtype: dict[str, Any]


.. function:: split(bm, geom=[], dest=None, use_only_faces=False)

   Split Off Geometry.

   Disconnect geometry from adjacent edges and faces,
   optionally into a destination mesh.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param geom:
      Input geometry.
   :type geom: list[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`]
   :param dest:
      Destination bmesh, if None will use current one.
   :type dest: :class:`bmesh.types.BMesh` | None
   :param use_only_faces:
      When enabled, don't duplicate loose verts/edges.
   :type use_only_faces: bool
   :return:

      - ``geom``:

        **type** list[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`]
      - ``boundary_map``:
        Boundary edges from the split geometry that maps edges from the original geometry
        to the destination edges.

        When the source edges have been deleted, the destination edge will be used
        for both the key and the value.

        **type** dict[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`, :class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`]
      - ``isovert_map``:

        **type** dict[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`, :class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`]

   :rtype: dict[str, Any]


.. function:: spin(bm, geom=[], cent=mathutils.Vector(), axis=mathutils.Vector(), dvec=mathutils.Vector(), angle=0, space=mathutils.Matrix.Identity(4), steps=0, use_merge=False, use_normal_flip=False, use_duplicate=False)

   Spin.

   Extrude or duplicate geometry a number of times,
   rotating and possibly translating after each step

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param geom:
      Input geometry.
   :type geom: list[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`]
   :param cent:
      Rotation center.
   :type cent: Sequence[float]
   :param axis:
      Rotation axis.
   :type axis: Sequence[float]
   :param dvec:
      Translation delta per step.
   :type dvec: Sequence[float]
   :param angle:
      Total rotation angle (radians).
   :type angle: float
   :param space:
      Matrix to define the space (typically object matrix).
   :type space: :class:`mathutils.Matrix`
   :param steps:
      Number of steps.
   :type steps: int
   :param use_merge:
      Merge first/last when the angle is a full revolution.
   :type use_merge: bool
   :param use_normal_flip:
      Create faces with reversed direction.
   :type use_normal_flip: bool
   :param use_duplicate:
      Duplicate the geometry, otherwise extrude.
   :type use_duplicate: bool
   :return:

      - ``geom_last``:
        Result of last step.

        **type** list[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`]

   :rtype: dict[str, Any]


.. function:: rotate_uvs(bm, faces=[], use_ccw=False)

   UV Rotation.

   Cycle the loop UVs

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param faces:
      Input faces.
   :type faces: list[:class:`bmesh.types.BMFace`]
   :param use_ccw:
      Rotate counter-clockwise if true, otherwise clockwise.
   :type use_ccw: bool


.. function:: reverse_uvs(bm, faces=[])

   UV Reverse.

   Reverse the UVs

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param faces:
      Input faces.
   :type faces: list[:class:`bmesh.types.BMFace`]


.. function:: rotate_colors(bm, faces=[], use_ccw=False, color_index=0)

   Color Rotation.

   Cycle the loop colors

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param faces:
      Input faces.
   :type faces: list[:class:`bmesh.types.BMFace`]
   :param use_ccw:
      Rotate counter-clockwise if true, otherwise clockwise.
   :type use_ccw: bool
   :param color_index:
      Index into color attribute list.
   :type color_index: int


.. function:: reverse_colors(bm, faces=[], color_index=0)

   Color Reverse

   Reverse the loop colors.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param faces:
      Input faces.
   :type faces: list[:class:`bmesh.types.BMFace`]
   :param color_index:
      Index into color attribute list.
   :type color_index: int


.. function:: split_edges(bm, edges=[], verts=[], use_verts=False)

   Edge Split.

   Disconnects faces along input edges.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param edges:
      Input edges.
   :type edges: list[:class:`bmesh.types.BMEdge`]
   :param verts:
      Optional tag verts, use to have greater control of splits.
   :type verts: list[:class:`bmesh.types.BMVert`]
   :param use_verts:
      Use `verts` for splitting, else just find verts to split from edges.
   :type use_verts: bool
   :return:

      - ``edges``:
        The original edges that were disconnected.

        **type** list[:class:`bmesh.types.BMEdge`]

   :rtype: dict[str, Any]


.. function:: create_grid(bm, x_segments=0, y_segments=0, size=0, matrix=mathutils.Matrix.Identity(4), calc_uvs=False)

   Create Grid.

   Creates a grid with a variable number of subdivisions

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param x_segments:
      Number of x segments.
   :type x_segments: int
   :param y_segments:
      Number of y segments.
   :type y_segments: int
   :param size:
      Size of the grid.
   :type size: float
   :param matrix:
      Matrix to multiply the new geometry with.
   :type matrix: :class:`mathutils.Matrix`
   :param calc_uvs:
      Calculate default UVs.
   :type calc_uvs: bool
   :return:

      - ``verts``:
        Output verts.

        **type** list[:class:`bmesh.types.BMVert`]

   :rtype: dict[str, Any]


.. function:: create_uvsphere(bm, u_segments=0, v_segments=0, radius=0, matrix=mathutils.Matrix.Identity(4), calc_uvs=False)

   Create UV Sphere.

   Creates a UV sphere with a variable number of subdivisions.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param u_segments:
      Number of u segments.
   :type u_segments: int
   :param v_segments:
      Number of v segments.
   :type v_segments: int
   :param radius:
      Radius.
   :type radius: float
   :param matrix:
      Matrix to multiply the new geometry with.
   :type matrix: :class:`mathutils.Matrix`
   :param calc_uvs:
      Calculate default UVs.
   :type calc_uvs: bool
   :return:

      - ``verts``:
        Output verts.

        **type** list[:class:`bmesh.types.BMVert`]

   :rtype: dict[str, Any]


.. function:: create_icosphere(bm, subdivisions=0, radius=0, matrix=mathutils.Matrix.Identity(4), calc_uvs=False)

   Create Ico-Sphere.

   Creates an ico-sphere with a variable number of subdivisions.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param subdivisions:
      How many times to recursively subdivide the sphere.
   :type subdivisions: int
   :param radius:
      Radius.
   :type radius: float
   :param matrix:
      Matrix to multiply the new geometry with.
   :type matrix: :class:`mathutils.Matrix`
   :param calc_uvs:
      Calculate default UVs.
   :type calc_uvs: bool
   :return:

      - ``verts``:
        Output verts.

        **type** list[:class:`bmesh.types.BMVert`]

   :rtype: dict[str, Any]


.. function:: create_monkey(bm, matrix=mathutils.Matrix.Identity(4), calc_uvs=False)

   Create Suzanne.

   Creates a monkey (standard blender primitive).

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param matrix:
      Matrix to multiply the new geometry with.
   :type matrix: :class:`mathutils.Matrix`
   :param calc_uvs:
      Calculate default UVs.
   :type calc_uvs: bool
   :return:

      - ``verts``:
        Output verts.

        **type** list[:class:`bmesh.types.BMVert`]

   :rtype: dict[str, Any]


.. function:: create_cone(bm, cap_ends=False, cap_tris=False, segments=0, radius1=0, radius2=0, depth=0, matrix=mathutils.Matrix.Identity(4), calc_uvs=False)

   Create Cone.

   Creates a cone with variable radius at both ends

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param cap_ends:
      Whether or not to fill in the ends with faces.
   :type cap_ends: bool
   :param cap_tris:
      Fill ends with triangles instead of ngons.
   :type cap_tris: bool
   :param segments:
      Number of vertices in the base circle.
   :type segments: int
   :param radius1:
      Radius of one end.
   :type radius1: float
   :param radius2:
      Radius of the opposite end.
   :type radius2: float
   :param depth:
      Distance between ends.
   :type depth: float
   :param matrix:
      Matrix to multiply the new geometry with.
   :type matrix: :class:`mathutils.Matrix`
   :param calc_uvs:
      Calculate default UVs.
   :type calc_uvs: bool
   :return:

      - ``verts``:
        Output verts.

        **type** list[:class:`bmesh.types.BMVert`]

   :rtype: dict[str, Any]


.. function:: create_circle(bm, cap_ends=False, cap_tris=False, segments=0, radius=0, matrix=mathutils.Matrix.Identity(4), calc_uvs=False)

   Creates a Circle.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param cap_ends:
      Whether or not to fill in the circle with a face.
   :type cap_ends: bool
   :param cap_tris:
      Fill the circle with triangles instead of an n-gon.
   :type cap_tris: bool
   :param segments:
      Number of vertices in the circle.
   :type segments: int
   :param radius:
      Radius of the circle.
   :type radius: float
   :param matrix:
      Matrix to multiply the new geometry with.
   :type matrix: :class:`mathutils.Matrix`
   :param calc_uvs:
      Calculate default UVs.
   :type calc_uvs: bool
   :return:

      - ``verts``:
        Output verts.

        **type** list[:class:`bmesh.types.BMVert`]

   :rtype: dict[str, Any]


.. function:: create_cube(bm, size=0, matrix=mathutils.Matrix.Identity(4), calc_uvs=False)

   Create Cube

   Creates a cube.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param size:
      Size of the cube.
   :type size: float
   :param matrix:
      Matrix to multiply the new geometry with.
   :type matrix: :class:`mathutils.Matrix`
   :param calc_uvs:
      Calculate default UVs.
   :type calc_uvs: bool
   :return:

      - ``verts``:
        Output verts.

        **type** list[:class:`bmesh.types.BMVert`]

   :rtype: dict[str, Any]


.. function:: bevel(bm, geom=[], offset=0, offset_type='OFFSET', profile_type='SUPERELLIPSE', segments=0, profile=0, affect='VERTICES', clamp_overlap=False, material=0, loop_slide=False, mark_seam=False, mark_sharp=False, harden_normals=False, face_strength_mode='NONE', miter_outer='SHARP', miter_inner='SHARP', spread=0, custom_profile=None, vmesh_method='ADJ')

   Bevel.

   Bevels edges and vertices

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param geom:
      Input edges and vertices.
   :type geom: list[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`]
   :param offset:
      Amount to offset beveled edge.
   :type offset: float
   :param offset_type:
      How to measure the offset.
   :type offset_type: Literal['OFFSET', 'WIDTH', 'DEPTH', 'PERCENT', 'ABSOLUTE']
   :param profile_type:
      The profile type to use for bevel.
   :type profile_type: Literal['SUPERELLIPSE', 'CUSTOM']
   :param segments:
      Number of segments in bevel.
   :type segments: int
   :param profile:
      Profile shape, 0->1 (.5=>round).
   :type profile: float
   :param affect:
      Whether to bevel vertices or edges.
   :type affect: Literal['VERTICES', 'EDGES']
   :param clamp_overlap:
      Do not allow beveled edges/vertices to overlap each other.
   :type clamp_overlap: bool
   :param material:
      Material for bevel faces, -1 means get from adjacent faces.
   :type material: int
   :param loop_slide:
      Prefer to slide along edges to having even widths.
   :type loop_slide: bool
   :param mark_seam:
      Extend edge data to allow seams to run across bevels.
   :type mark_seam: bool
   :param mark_sharp:
      Extend edge data to allow sharp edges to run across bevels.
   :type mark_sharp: bool
   :param harden_normals:
      Harden normals.
   :type harden_normals: bool
   :param face_strength_mode:
      Whether to set face strength, and which faces to set if so.
   :type face_strength_mode: Literal['NONE', 'NEW', 'AFFECTED', 'ALL']
   :param miter_outer:
      Outer miter kind.
   :type miter_outer: Literal['SHARP', 'PATCH', 'ARC']
   :param miter_inner:
      Inner miter kind.
   :type miter_inner: Literal['SHARP', 'PATCH', 'ARC']
   :param spread:
      Amount to spread the miter.
   :type spread: float
   :param custom_profile:
      CurveProfile, if None ignored
   :type custom_profile: :class:`bpy.types.bpy_struct` | None
   :param vmesh_method:
      The method to use to create meshes at intersections.
   :type vmesh_method: Literal['ADJ', 'CUTOFF']
   :return:

      - ``faces``:
        Output faces.

        **type** list[:class:`bmesh.types.BMFace`]
      - ``edges``:
        Output edges.

        **type** list[:class:`bmesh.types.BMEdge`]
      - ``verts``:
        Output verts.

        **type** list[:class:`bmesh.types.BMVert`]

   :rtype: dict[str, Any]


.. function:: beautify_fill(bm, faces=[], edges=[], use_restrict_tag=False, method='AREA')

   Beautify Fill.

   Rotate edges to create more evenly spaced triangles.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param faces:
      Input faces.
   :type faces: list[:class:`bmesh.types.BMFace`]
   :param edges:
      Edges that can be flipped.
   :type edges: list[:class:`bmesh.types.BMEdge`]
   :param use_restrict_tag:
      Restrict edge rotation to mixed tagged vertices.
   :type use_restrict_tag: bool
   :param method:
      Method to define what is beautiful.
   :type method: Literal['AREA', 'ANGLE']
   :return:

      - ``geom``:
        New flipped faces and edges.

        **type** list[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`]

   :rtype: dict[str, Any]


.. function:: triangle_fill(bm, use_beauty=False, use_dissolve=False, edges=[], normal=mathutils.Vector())

   Triangle Fill.

   Fill edges with triangles

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param use_beauty:
      Use best triangulation division.
   :type use_beauty: bool
   :param use_dissolve:
      Dissolve resulting faces.
   :type use_dissolve: bool
   :param edges:
      Input edges.
   :type edges: list[:class:`bmesh.types.BMEdge`]
   :param normal:
      Optionally pass the fill normal to use.
   :type normal: Sequence[float]
   :return:

      - ``geom``:
        New faces and edges.

        **type** list[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`]

   :rtype: dict[str, Any]


.. function:: solidify(bm, geom=[], thickness=0)

   Solidify.

   Turns a mesh into a shell with thickness

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param geom:
      Input geometry.
   :type geom: list[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`]
   :param thickness:
      Thickness of the solidified shell.
   :type thickness: float
   :return:

      - ``geom``:
        Output geometry (new shell faces, edges, and vertices).

        **type** list[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`]

   :rtype: dict[str, Any]


.. function:: inset_individual(bm, faces=[], thickness=0, depth=0, use_even_offset=False, use_interpolate=False, use_relative_offset=False)

   Face Inset (Individual).

   Insets individual faces.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param faces:
      Input faces.
   :type faces: list[:class:`bmesh.types.BMFace`]
   :param thickness:
      Inset distance from the boundary.
   :type thickness: float
   :param depth:
      Distance to raise or lower the inset face along its normal.
   :type depth: float
   :param use_even_offset:
      Scale the offset to give more even thickness.
   :type use_even_offset: bool
   :param use_interpolate:
      Blend face data across the inset.
   :type use_interpolate: bool
   :param use_relative_offset:
      Scale the offset by surrounding geometry.
   :type use_relative_offset: bool
   :return:

      - ``faces``:
        Output faces.

        **type** list[:class:`bmesh.types.BMFace`]

   :rtype: dict[str, Any]


.. function:: inset_region(bm, faces=[], faces_exclude=[], use_boundary=False, use_even_offset=False, use_interpolate=False, use_relative_offset=False, use_edge_rail=False, thickness=0, depth=0, use_outset=False)

   Face Inset (Regions).

   Inset or outset face regions.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param faces:
      Input faces.
   :type faces: list[:class:`bmesh.types.BMFace`]
   :param faces_exclude:
      Input faces to explicitly exclude from inset.
   :type faces_exclude: list[:class:`bmesh.types.BMFace`]
   :param use_boundary:
      Inset face boundaries.
   :type use_boundary: bool
   :param use_even_offset:
      Scale the offset to give more even thickness.
   :type use_even_offset: bool
   :param use_interpolate:
      Blend face data across the inset.
   :type use_interpolate: bool
   :param use_relative_offset:
      Scale the offset by surrounding geometry.
   :type use_relative_offset: bool
   :param use_edge_rail:
      Inset the region along existing edges.
   :type use_edge_rail: bool
   :param thickness:
      Inset distance from the boundary.
   :type thickness: float
   :param depth:
      Distance to raise or lower the inset face along its normal.
   :type depth: float
   :param use_outset:
      Outset rather than inset.
   :type use_outset: bool
   :return:

      - ``faces``:
        Output faces.

        **type** list[:class:`bmesh.types.BMFace`]

   :rtype: dict[str, Any]


.. function:: offset_edgeloops(bm, edges=[], use_cap_endpoint=False)

   Edge-loop Offset.

   Creates edge loops based on simple edge-outset method.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param edges:
      Input edges.
   :type edges: list[:class:`bmesh.types.BMEdge`]
   :param use_cap_endpoint:
      Extend loop around end-points.
   :type use_cap_endpoint: bool
   :return:

      - ``edges``:
        Output edges.

        **type** list[:class:`bmesh.types.BMEdge`]

   :rtype: dict[str, Any]


.. function:: wireframe(bm, faces=[], thickness=0, offset=0, use_replace=False, use_boundary=False, use_even_offset=False, use_crease=False, crease_weight=0, use_relative_offset=False, material_offset=0)

   Wire Frame.

   Makes a wire-frame copy of faces.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param faces:
      Input faces.
   :type faces: list[:class:`bmesh.types.BMFace`]
   :param thickness:
      Wire thickness.
   :type thickness: float
   :param offset:
      Offset the thickness from the center.
   :type offset: float
   :param use_replace:
      Remove original geometry.
   :type use_replace: bool
   :param use_boundary:
      Inset face boundaries.
   :type use_boundary: bool
   :param use_even_offset:
      Scale the offset to give more even thickness.
   :type use_even_offset: bool
   :param use_crease:
      Crease hub edges for improved subdivision surface.
   :type use_crease: bool
   :param crease_weight:
      The mean crease weight for resulting edges.
   :type crease_weight: float
   :param use_relative_offset:
      Scale the offset by surrounding geometry.
   :type use_relative_offset: bool
   :param material_offset:
      Offset material index of generated faces.
   :type material_offset: int
   :return:

      - ``faces``:
        Output faces.

        **type** list[:class:`bmesh.types.BMFace`]

   :rtype: dict[str, Any]


.. function:: poke(bm, faces=[], offset=0, center_mode='MEAN_WEIGHTED', use_relative_offset=False)

   Pokes a face.

   Splits a face into a triangle fan.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param faces:
      Input faces.
   :type faces: list[:class:`bmesh.types.BMFace`]
   :param offset:
      Center vertex offset along normal.
   :type offset: float
   :param center_mode:
      Calculation mode for center vertex.
   :type center_mode: Literal['MEAN_WEIGHTED', 'MEAN', 'BOUNDS']
   :param use_relative_offset:
      Apply offset.
   :type use_relative_offset: bool
   :return:

      - ``verts``:
        Output verts.

        **type** list[:class:`bmesh.types.BMVert`]
      - ``faces``:
        Output faces.

        **type** list[:class:`bmesh.types.BMFace`]

   :rtype: dict[str, Any]


.. function:: convex_hull(bm, input=[], use_existing_faces=False)

   Convex Hull

   Builds a convex hull from the vertices in ``input``.

   If ``use_existing_faces`` is true, the hull will not output triangles
   that are covered by a pre-existing face.

   All hull vertices, faces, and edges are added to ``geom.out``. Any
   input elements that end up inside the hull (i.e. are not used by an
   output face) are added to the ``geom_interior.out`` slot. The
   ``geom_unused.out`` slot will contain all interior geometry that is
   completely unused. Lastly, ``geom_holes.out`` contains edges and faces
   that were in the input and are part of the hull.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param input:
      Input geometry.
   :type input: list[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`]
   :param use_existing_faces:
      Skip hull triangles that are covered by a pre-existing face.
   :type use_existing_faces: bool
   :return:

      - ``geom``:

        **type** list[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`]
      - ``geom_interior``:

        **type** list[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`]
      - ``geom_unused``:

        **type** list[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`]
      - ``geom_holes``:

        **type** list[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`]

   :rtype: dict[str, Any]


.. function:: symmetrize(bm, input=[], direction='-X', dist=0, use_shapekey=False)

   Symmetrize.

   Makes the mesh elements in the ``input`` slot symmetrical. Unlike
   normal mirroring, it only copies in one direction, as specified by
   the ``direction`` slot. The edges and faces that cross the plane of
   symmetry are split as needed to enforce symmetry.

   All new vertices, edges, and faces are added to the ``geom.out`` slot.

   :param bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :param input:
      Input geometry.
   :type input: list[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`]
   :param direction:
      Axis to use.
   :type direction: Literal['-X', '-Y', '-Z', 'X', 'Y', 'Z']
   :param dist:
      Minimum distance.
   :type dist: float
   :param use_shapekey:
      Transform shape keys too.
   :type use_shapekey: bool
   :return:

      - ``geom``:

        **type** list[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`]

   :rtype: dict[str, Any]


