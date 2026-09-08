Mesh(ID)
========

.. currentmodule:: bpy.types


Mesh Data
+++++++++

The mesh data is accessed in object mode and intended for compact storage,
for more flexible mesh editing from Python see :mod:`bmesh`.

Blender stores 4 main arrays to define mesh geometry.

- :class:`Mesh.vertices` (3 points in space)
- :class:`Mesh.edges` (reference 2 vertices)
- :class:`Mesh.loops` (reference a single vertex and edge)
- :class:`Mesh.polygons`: (reference a range of loops)


Each polygon references a slice in the loop array, this way,
polygons do not store vertices or corner data such as UVs directly,
only a reference to loops that the polygon uses.

:class:`Mesh.loops`, :class:`Mesh.uv_layers` :class:`Mesh.vertex_colors` are all aligned so the same polygon loop
indices can be used to find the UVs and vertex colors as with as the vertices.

To compare mesh API options see: :ref:`NGons and Tessellation Faces <info_gotcha_mesh_faces>`


This example script prints the vertices and UVs for each polygon, assumes the active object is a mesh with UVs.

.. literalinclude:: ./examples/bpy.types.Mesh.0.py
   :lines: 29-

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: Mesh(ID)

   Mesh data-block defining geometric surfaces

   .. data:: animation_data

      Animation data for this data-block (readonly)

      :type: :class:`AnimData` | None

   .. data:: attributes

      Geometry attributes (default None, readonly)

      :type: :class:`AttributeGroupMesh`\ [:class:`Attribute`]

   .. attribute:: auto_texspace

      Adjust active object's texture space automatically when transforming object (default True)

      :type: bool

   .. data:: color_attributes

      Geometry color attributes (default None, readonly)

      :type: :class:`AttributeGroupMesh`\ [:class:`Attribute`]

   .. data:: corner_normals

      The "slit" normal direction of each face corner, influenced by vertex normals, sharp faces, sharp edges, and custom normals. May be empty. (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`MeshNormalValue`]

   .. data:: edges

      Edges of the mesh (default None, readonly)

      :type: :class:`MeshEdges`\ [:class:`MeshEdge`]

   .. data:: has_custom_normals

      True if there is custom normal data for this mesh (default False, readonly)

      :type: bool

   .. data:: is_editmode

      True when used in editmode (default False, readonly)

      :type: bool

   .. data:: loop_triangle_polygons

      The face index for each loop triangle (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`ReadOnlyInteger`]

   .. data:: loop_triangles

      Tessellation of mesh polygons into triangles (default None, readonly)

      :type: :class:`MeshLoopTriangles`\ [:class:`MeshLoopTriangle`]

   .. data:: loops

      Loops of the mesh (face corners) (default None, readonly)

      :type: :class:`MeshLoops`\ [:class:`MeshLoop`]

   .. data:: materials

      (default None, readonly)

      :type: :class:`IDMaterials`\ [:class:`Material`]

   .. data:: normals_domain

      The attribute domain that gives enough information to represent the mesh's normals (default ``'FACE'``, readonly)

      :type: Literal['POINT', 'FACE', 'CORNER']

   .. data:: polygon_normals

      The normal direction of each face, defined by the winding order and position of its vertices (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`MeshNormalValue`]

   .. data:: polygons

      Polygons of the mesh (default None, readonly)

      :type: :class:`MeshPolygons`\ [:class:`MeshPolygon`]

   .. attribute:: radial_symmetry

      Number of mirrored regions around a central axis (array of 3 items, in [1, 64], default (1, 1, 1))

      :type: :class:`bpy_prop_array`\ [int]

   .. attribute:: remesh_mode

      (default ``'VOXEL'``)

      - ``VOXEL``
        Voxel -- Use the voxel remesher.
      - ``QUAD``
        Quad -- Use the quad remesher.

      :type: Literal['VOXEL', 'QUAD']

   .. attribute:: remesh_voxel_adaptivity

      Reduces the final face count by simplifying geometry where detail is not needed, generating triangles. A value greater than 0 disables Fix Poles. (in [0, 1], default 0.0)

      :type: float

   .. attribute:: remesh_voxel_size

      Size of the voxel in object space used for volume evaluation. Lower values preserve finer details. (in [0, inf], default 0.1)

      :type: float

   .. data:: shape_keys

      (readonly)

      :type: :class:`Key` | None

   .. data:: skin_vertices

      All skin vertices (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`MeshSkinVertexLayer`]

   .. attribute:: texco_mesh

      Derive texture coordinates from another mesh

      :type: :class:`Mesh` | None

   .. attribute:: texspace_location

      Texture space location (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: texspace_size

      Texture space size (array of 3 items, in [-inf, inf], default (1.0, 1.0, 1.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: texture_mesh

      Use another mesh for texture indices (vertex indices must be aligned)

      :type: :class:`Mesh` | None

   .. data:: total_edge_sel

      Selected edge count in editmode (in [0, inf], default 0, readonly)

      :type: int

   .. data:: total_face_sel

      Selected face count in editmode (in [0, inf], default 0, readonly)

      :type: int

   .. data:: total_vert_sel

      Selected vertex count in editmode (in [0, inf], default 0, readonly)

      :type: int

   .. attribute:: use_auto_texspace

      Adjust active object's texture space automatically when transforming object (default True)

      :type: bool

   .. attribute:: use_mirror_topology

      Use topology based mirroring (for when both sides of mesh have matching, unique topology) (default False)

      :type: bool

   .. attribute:: use_mirror_vertex_groups

      Mirror the left/right vertex groups when painting. The symmetry axis is determined by the symmetry settings. (default True)

      :type: bool

   .. attribute:: use_mirror_x

      Enable symmetry in the X axis (default False)

      :type: bool

   .. attribute:: use_mirror_y

      Enable symmetry in the Y axis (default False)

      :type: bool

   .. attribute:: use_mirror_z

      Enable symmetry in the Z axis (default False)

      :type: bool

   .. attribute:: use_paint_bone_selection

      Bone selection during painting (default True)

      :type: bool

   .. attribute:: use_paint_mask

      Face selection masking for painting (default False)

      :type: bool

   .. attribute:: use_paint_mask_vertex

      Vertex selection masking for painting (default False)

      :type: bool

   .. attribute:: use_remesh_fix_poles

      Produces fewer poles and a better topology flow (default False)

      :type: bool

   .. attribute:: use_remesh_preserve_attributes

      Transfer all attributes to the new mesh (default False)

      :type: bool

   .. attribute:: use_remesh_preserve_volume

      Projects the mesh to preserve the volume and details of the original mesh (default False)

      :type: bool

   .. attribute:: uv_layer_clone

      UV loop layer to be used as cloning source

      :type: :class:`MeshUVLoopLayer` | None

   .. attribute:: uv_layer_clone_index

      Clone UV loop layer index (in [0, inf], default 0)

      :type: int

   .. attribute:: uv_layer_stencil

      UV loop layer to mask the painted area

      :type: :class:`MeshUVLoopLayer` | None

   .. attribute:: uv_layer_stencil_index

      Mask UV loop layer index (in [0, inf], default 0)

      :type: int

   .. data:: uv_layers

      All UV loop layers (default None, readonly)

      :type: :class:`UVLoopLayers`\ [:class:`MeshUVLoopLayer`]

   .. data:: vertex_colors

      Legacy vertex color layers. Deprecated, use color attributes instead. (default None, readonly)

      :type: :class:`LoopColors`\ [:class:`MeshLoopColorLayer`]

   .. data:: vertex_normals

      The normal direction of each vertex, defined as the average of the surrounding face normals (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`MeshNormalValue`]

   .. data:: vertices

      Vertices of the mesh (default None, readonly)

      :type: :class:`MeshVertices`\ [:class:`MeshVertex`]

   .. data:: edge_creases

      Edge crease values for subdivision surface, corresponding to the "crease_edge" attribute.

      (readonly)

   .. data:: edge_keys


      (readonly)

   .. data:: vertex_creases

      Vertex crease values for subdivision surface, corresponding to the "crease_vert" attribute.

      (readonly)

   .. data:: vertex_paint_mask

      Mask values for sculpting and painting, corresponding to the ".sculpt_mask" attribute.

      (readonly)

   .. method:: transform(matrix, *, shape_keys=False)

      Transform mesh vertices by a matrix (Warning: inverts normals if matrix is negative)

      :param matrix: Matrix (multi-dimensional array of 4 * 4 items, in [-inf, inf])
      :type matrix: :class:`mathutils.Matrix` | Sequence[Sequence[float]]
      :param shape_keys: Transform Shape Keys (optional)
      :type shape_keys: bool

   .. method:: flip_normals()

      Invert winding of all polygons (clears tessellation, does not handle custom normals)


   .. method:: set_sharp_from_angle(*, angle=3.14159)

      Reset and fill the "sharp_edge" attribute based on the angle of faces neighboring manifold edges

      :param angle: Angle, Angle between faces beyond which edges are marked sharp (in [0, 3.14159], optional)
      :type angle: float

   .. method:: split_faces()

      Split faces based on the edge angle


   .. method:: calc_tangents(*, uvmap="")

      Compute tangents and bitangent signs, to be used together with the custom normals to get a complete tangent space for normal mapping (custom normals are also computed if not yet present)

      :param uvmap: Name of the UV map to use for tangent space computation (optional, never None)
      :type uvmap: str

   .. method:: free_tangents()

      Free tangents


   .. method:: calc_loop_triangles()

      Calculate loop triangle tessellation (supports editmode too)


   .. method:: calc_smooth_groups(*, use_bitflags=False, use_boundary_vertices_for_bitflags=False)

      Calculate smooth groups from sharp edges

      :param use_bitflags: Produce bitflags groups instead of simple numeric values (optional)
      :type use_bitflags: bool
      :param use_boundary_vertices_for_bitflags: Also consider different smoothgroups sharing only vertices (but without any common edge) as neighbors, preventing them from sharing the same bitflag value. Only effective when ``use_bitflags`` is set. WARNING: Will overflow (run out of available bits) easily with some types of topology, e.g. large fans of sharp edges (optional)
      :type use_boundary_vertices_for_bitflags: bool
      :return:
         ``poly_groups``, Smooth Groups, :class:`bpy_prop_array`\ [int]

         ``groups``, Total number of groups, int

      :rtype: tuple[:class:`bpy_prop_array`\ [int], int]

   .. method:: normals_split_custom_set(normals)

      Define custom normals of this mesh (use zero-vectors to keep auto ones)

      :param normals: Normals (multi-dimensional array of 1 * 3 items, in [-1, 1])
      :type normals: Sequence[float]

   .. method:: normals_split_custom_set_from_vertices(normals)

      Define custom normals of this mesh, from vertices' normals (use zero-vectors to keep auto ones)

      :param normals: Normals (multi-dimensional array of 1 * 3 items, in [-1, 1])
      :type normals: Sequence[float]

   .. method:: update(*, calc_edges=False, calc_edges_loose=False)

      update

      :param calc_edges: Calculate Edges, Force recalculation of edges (optional)
      :type calc_edges: bool
      :param calc_edges_loose: Calculate Loose Edges, Calculate the loose state of each edge (optional)
      :type calc_edges_loose: bool

   .. method:: update_gpu_tag()

      update_gpu_tag


   .. method:: unit_test_compare(*, mesh=None, threshold=7.1526e-06)

      unit_test_compare

      :param mesh: Mesh to compare to (optional)
      :type mesh: :class:`Mesh` | None
      :param threshold: Threshold, Comparison tolerance threshold (in [0, inf], optional)
      :type threshold: float
      :return: Return value, String description of result of comparison (never None)
      :rtype: str

   .. method:: clear_geometry()

      Remove all geometry from the mesh. Note that this does not free shape keys or materials.


   .. method:: validate(*, verbose=False, clean_customdata=True)

      Validate geometry, return True when the mesh has had invalid geometry corrected/removed

      :param verbose: Verbose, Output information about the errors found (optional)
      :type verbose: bool
      :param clean_customdata: Clean Custom Data, Deprecated, has no effect (optional)
      :type clean_customdata: bool
      :return: Result
      :rtype: bool

   .. method:: validate_material_indices()

      Validate material indices of polygons, return True when the mesh has had invalid indices corrected (to default 0)

      :return: Result
      :rtype: bool

   .. method:: count_selected_items()

      Return the number of selected items (vert, edge, face)

      :return: Result, (array of 3 items, in [0, inf])
      :rtype: :class:`bpy_prop_array`\ [int]

   .. method:: edge_creases_ensure()

   .. method:: edge_creases_remove()

   .. method:: from_pydata(vertices, edges, faces, shade_flat=True)

      Make a mesh from a list of vertices/edges/faces
      Until we have a nicer way to make geometry, use this.
      
      :param vertices:
      
         float triplets each representing (X, Y, Z)
         eg: [(0.0, 1.0, 0.5), ...].
      
      :type vertices: Iterable[Sequence[float]]
      :param edges:
      
         int pairs, each pair contains two indices to the
         *vertices* argument. eg: [(1, 2), ...]
      
         When an empty iterable is passed in, the edges are inferred from the polygons.
      
      :type edges: Iterable[Sequence[int]]
      :param faces:
      
         iterator of faces, each faces contains three or more indices to
         the *vertices* argument. eg: [(5, 6, 8, 9), (1, 2, 3), ...]
      
      :type faces: Iterable[Sequence[int]]
      
      .. warning::
      
         Invalid mesh data
         *(out of range indices, edges with matching indices,
         2 sided faces... etc)* are **not** prevented.
         If the data used for mesh creation isn't known to be valid,
         run :class:`Mesh.validate` after this function.

   .. method:: shade_flat()

      Render and display faces uniform, using face normals,
      setting the "sharp_face" attribute true for every face

   .. method:: shade_smooth()

      Render and display faces smooth, using interpolated vertex normals,
      removing the "sharp_face" attribute

   .. method:: vertex_creases_ensure()

   .. method:: vertex_creases_remove()

   .. method:: vertex_paint_mask_ensure()

   .. method:: vertex_paint_mask_remove()

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

   - :mod:`bpy.context.mesh`
   - :class:`BlendData.meshes`
   - :class:`BlendDataMeshes.new`
   - :class:`BlendDataMeshes.new_from_object`
   - :class:`BlendDataMeshes.remove`
   - :class:`Mesh.texco_mesh`
   - :class:`Mesh.texture_mesh`
   - :class:`Mesh.unit_test_compare`
   - :class:`Object.to_mesh`

