BMesh Types (bmesh.types)
=========================

.. module:: bmesh.types

.. |UV_STICKY_SELECT_MODE_REF| replace:: (:class:`bpy.types.ToolSettings.uv_sticky_select_mode` which may be passed in directly).

.. |UV_STICKY_SELECT_MODE_TYPE| replace:: Literal['SHARED_LOCATION', 'DISABLED', 'SHARED_VERTEX']

.. |UV_SELECT_FLUSH_MODE_NEEDED| replace:: This function is selection-mode independent, typically :meth:`bmesh.types.BMesh.uv_select_flush_mode` should be called afterwards.

.. |UV_SELECT_SYNC_TO_MESH_NEEDED| replace:: This function doesn't flush the selection to the mesh, typically :meth:`bmesh.types.BMesh.uv_select_sync_to_mesh` should be called afterwards.

Base Mesh Type
--------------

.. class:: BMesh

   The BMesh data structure

   .. method:: calc_loop_triangles()
   
      Calculate triangle tessellation from quads/ngons.
   
      :return: The triangulated faces.
      :rtype: list[tuple[:class:`bmesh.types.BMLoop`, :class:`bmesh.types.BMLoop`, :class:`bmesh.types.BMLoop`]]


   .. method:: calc_volume(*, signed=False)
   
      Calculate mesh volume based on face normals.
   
      :param signed: when signed is true, negative values may be returned.
      :type signed: bool
      :return: The volume of the mesh.
      :rtype: float


   .. method:: clear()
   
      Clear all mesh data.


   .. method:: copy()
   
      :return: A copy of this BMesh.
      :rtype: :class:`bmesh.types.BMesh`


   .. method:: free()
   
      Explicitly free the BMesh data from memory, causing exceptions on further access.
   
      .. note::
   
         The BMesh is freed automatically, typically when the script finishes executing.
         However in some cases it's hard to predict when this will be and it's useful to
         explicitly free the data.


   .. method:: from_mesh(mesh, *, face_normals=True, vertex_normals=True, use_shape_key=False, shape_key_index=0)
   
      Initialize this bmesh from existing mesh data-block.
   
      :param mesh: The mesh data to load.
      :type mesh: :class:`bpy.types.Mesh`
      :param face_normals: Calculate face normals.
      :type face_normals: bool
      :param vertex_normals: Calculate vertex normals.
      :type vertex_normals: bool
      :param use_shape_key: Use the locations from a shape key.
      :type use_shape_key: bool
      :param shape_key_index: The shape key index to use.
      :type shape_key_index: int
   
      .. note::
   
         Multiple calls can be used to join multiple meshes.
   
         Custom-data layers are only copied from ``mesh`` on initialization.
         Further calls will copy custom-data to matching layers, layers missing on the target mesh won't be added.


   .. method:: from_object(object, depsgraph, *, cage=False, face_normals=True, vertex_normals=True)
   
      Initialize this bmesh from existing object data-block (only meshes are currently supported).
   
      :param object: The object data to load.
      :type object: :class:`bpy.types.Object`
      :param depsgraph: The dependency graph for evaluated data.
      :type depsgraph: :class:`bpy.types.Depsgraph`
      :param cage: Get the mesh as a deformed cage.
      :type cage: bool
      :param face_normals: Calculate face normals.
      :type face_normals: bool
      :param vertex_normals: Calculate vertex normals.
      :type vertex_normals: bool


   .. method:: normal_update()
   
      Update normals of mesh faces and verts.
   
      .. note::
   
         The normal of any vertex where :attr:`is_wire` is True will be a zero vector.


   .. method:: select_flush(select)
   
      Flush selection from vertices, independent of the current selection mode.
   
      :param select: flush selection or de-selected elements.
      :type select: bool


   .. method:: select_flush_mode(*, flush_down=False)
   
      Flush selection based on the current mode :attr:`bmesh.types.BMesh.select_mode`.
   
      :param flush_down: Flush selection down from faces to edges & verts or from edges to verts. This option is ignored when vertex selection mode is enabled.
      :type flush_down: bool


   .. method:: to_mesh(mesh)
   
      Writes this BMesh data into an existing Mesh data-block.
   
      :param mesh: The mesh data to write into.
      :type mesh: :class:`bpy.types.Mesh`


   .. method:: transform(matrix, *, filter=None)
   
      Transform the mesh (optionally filtering flagged data only).
   
      :param matrix: 4x4 transform matrix.
      :type matrix: :class:`mathutils.Matrix`
      :param filter: Flag to filter vertices.
      :type filter: set[Literal['SELECT', 'HIDE', 'SEAM', 'SMOOTH', 'TAG']] | None


   .. method:: uv_select_flush(select)
   
      Flush selection from UV vertices to edges & faces independent of the selection mode.
   
      :param select: Flush selection or de-selected elements.
      :type select: bool
   
      .. note::
   
         - |UV_SELECT_SYNC_TO_MESH_NEEDED|


   .. method:: uv_select_flush_mode(*, flush_down=False)
   
      Flush UV selection based on the current mode :attr:`bmesh.types.BMesh.select_mode`.
   
      :param flush_down: Flush selection down from faces to edges & verts or from edges to verts. This option is ignored when vertex selection mode is enabled.
      :type flush_down: bool


   .. method:: uv_select_flush_shared(select)
   
      Flush selection from UV vertices to contiguous UV's independent of the selection mode.
   
      :param select: Flush selection or de-selected elements.
      :type select: bool
   
      .. note::
   
         - |UV_SELECT_SYNC_TO_MESH_NEEDED|


   .. method:: uv_select_foreach_set(select, /, *, loop_verts=(), loop_edges=(), faces=(), sticky_select_mode='SHARED_LOCATION')
   
      Set the UV selection state for loop-vertices, loop-edges & faces.
   
      This is a close equivalent to selecting in the UV editor.
   
      :param select: The selection state to set.
      :type select: bool
      :param loop_verts: Loop verts to operate on.
      :type loop_verts: Iterable[:class:`bmesh.types.BMLoop`]
      :param loop_edges: Loop edges to operate on.
      :type loop_edges: Iterable[:class:`bmesh.types.BMLoop`]
      :param faces: Faces to operate on.
      :type faces: Iterable[:class:`bmesh.types.BMFace`]
      :param sticky_select_mode: See |UV_STICKY_SELECT_MODE_REF|.
      :type sticky_select_mode: |UV_STICKY_SELECT_MODE_TYPE|
   
      .. note::
   
         - |UV_SELECT_FLUSH_MODE_NEEDED|
         - |UV_SELECT_SYNC_TO_MESH_NEEDED|


   .. method:: uv_select_foreach_set_from_mesh(select, /, *, verts=(), edges=(), faces=(), sticky_select_mode='SHARED_LOCATION')
   
      Select or de-select mesh elements, updating the UV selection.
   
      An equivalent to selecting from the 3D viewport for selection operations that support maintaining a synchronized UV selection.
   
      :param select: The selection state to set.
      :type select: bool
      :param verts: Verts to operate on.
      :type verts: Iterable[:class:`bmesh.types.BMVert`]
      :param edges: Edges to operate on.
      :type edges: Iterable[:class:`bmesh.types.BMEdge`]
      :param faces: Faces to operate on.
      :type faces: Iterable[:class:`bmesh.types.BMFace`]
      :param sticky_select_mode: See |UV_STICKY_SELECT_MODE_REF|.
      :type sticky_select_mode: |UV_STICKY_SELECT_MODE_TYPE|


   .. method:: uv_select_sync_from_mesh(*, sticky_select_mode='SHARED_LOCATION')
   
      Sync selection from mesh to UVs.
   
      :param sticky_select_mode: Behavior when flushing from the mesh to UV selection |UV_STICKY_SELECT_MODE_REF|. This should only be used when preparing to create a UV selection.
      :type sticky_select_mode: |UV_STICKY_SELECT_MODE_TYPE|
   
      .. note::
   
         - |UV_SELECT_SYNC_TO_MESH_NEEDED|


   .. method:: uv_select_sync_to_mesh()
   
      Sync selection from UVs to the mesh.


   .. attribute:: edges

      This mesh's edge sequence (read-only).
      
      :type: :class:`bmesh.types.BMEdgeSeq`


   .. attribute:: faces

      This mesh's face sequence (read-only).
      
      :type: :class:`bmesh.types.BMFaceSeq`


   .. attribute:: is_valid

      True when this element is valid (hasn't been freed or removed).
      
      :type: bool


   .. attribute:: is_wrapped

      True when this mesh is owned by blender (typically the editmode BMesh).
      
      :type: bool


   .. attribute:: loops

      This mesh's loops (read-only).
      
      :type: :class:`bmesh.types.BMLoopSeq`
      
      .. note::
      
         Loops must be accessed via faces, this is only exposed for layer access.


   .. attribute:: select_history

      Sequence of selected items (the last is displayed as active).
      
      :type: :class:`bmesh.types.BMEditSelSeq`


   .. attribute:: select_mode

      The selection mode, cannot be assigned an empty set.
      
      :type: set[Literal['VERT', 'EDGE', 'FACE']]


   .. attribute:: uv_select_sync_valid

      When true, the UV selection has been synchronized. Setting to False means the UV selection will be ignored. While setting to true is supported it is up to the script author to ensure a correct selection state before doing so.
      
      :type: bool


   .. attribute:: verts

      This mesh's vert sequence (read-only).
      
      :type: :class:`bmesh.types.BMVertSeq`




Mesh Elements
-------------

.. class:: BMVert

   The BMesh vertex type

   .. method:: calc_edge_angle(fallback=None)
   
      Return the angle between this vert's two connected edges.
   
      :param fallback: return this when the vert doesn't have 2 edges
         (instead of raising a :exc:`ValueError`).
      :type fallback: Any
      :return: Angle between edges in radians.
      :rtype: float


   .. method:: calc_shell_factor()
   
      Return a multiplier calculated based on the sharpness of the vertex.
      Where a flat surface gives 1.0, and higher values sharper edges.
      This is used to maintain shell thickness when offsetting verts along their normals.
   
      :return: offset multiplier
      :rtype: float


   .. method:: copy_from(other)
   
      Copy values from another element of matching type.
   
      :param other: Another element of the same type to copy from.
      :type other: Self


   .. method:: copy_from_face_interp(face)
   
      Interpolate the customdata from a face onto this vert (the vert should overlap the face).
   
      :param face: The face to interpolate data from.
      :type face: :class:`bmesh.types.BMFace`


   .. method:: copy_from_vert_interp(vert_pair, fac)
   
      Interpolate the customdata from a vert between 2 other verts.
   
      :param vert_pair: The verts between which to interpolate data from.
      :type vert_pair: Sequence[:class:`bmesh.types.BMVert`]
      :param fac: The interpolation factor.
      :type fac: float


   .. method:: hide_set(hide)
   
      Set the hide state.
      This is different from the *hide* attribute because it updates the selection and hide state of associated geometry.
   
      :param hide: Hidden or visible.
      :type hide: bool


   .. method:: normal_update()
   
      Update vertex normal.
      This does not update the normals of adjoining faces.
   
      .. note::
   
         The vertex normal will be a zero vector if vertex :attr:`is_wire` is True.


   .. method:: select_set(select)
   
      Set the selection.
      This is different from the *select* attribute because it updates the selection state of associated geometry.
   
      :param select: Select or de-select.
      :type select: bool
   
      .. note::
   
         This flushes selection down (e.g. selecting a face also selects its edges and vertices), but not up (e.g. de-selecting a vertex won't de-select faces that use it). Before finishing with a mesh, flushing is typically still needed.


   .. attribute:: co

      The coordinates for this vertex as a 3D, wrapped vector.
      
      :type: :class:`mathutils.Vector`


   .. attribute:: hide

      Hidden state of this element.
      
      :type: bool


   .. attribute:: index

      Index of this element.
      
      :type: int
      
      .. note::
      
         This value is not necessarily valid, while editing the mesh it can become *dirty*.
      
         It's also possible to assign any number to this attribute for a scripts internal logic.
      
         To ensure the value is up to date - see :meth:`bmesh.types.BMElemSeq.index_update`.


   .. attribute:: is_boundary

      True when this vertex is connected to boundary edges (read-only).
      
      :type: bool


   .. attribute:: is_manifold

      True when this vertex is manifold (read-only).
      
      :type: bool


   .. attribute:: is_valid

      True when this element is valid (hasn't been freed or removed).
      
      :type: bool


   .. attribute:: is_wire

      True when this vertex is not connected to any faces (read-only).
      
      :type: bool


   .. attribute:: link_edges

      Edges connected to this vertex (read-only).
      
      :type: :class:`bmesh.types.BMElemSeq`\ [:class:`bmesh.types.BMEdge`]


   .. attribute:: link_faces

      Faces connected to this vertex (read-only).
      
      :type: :class:`bmesh.types.BMElemSeq`\ [:class:`bmesh.types.BMFace`]


   .. attribute:: link_loops

      Loops that use this vertex (read-only).
      
      :type: :class:`bmesh.types.BMElemSeq`\ [:class:`bmesh.types.BMLoop`]


   .. attribute:: normal

      The normal for this vertex as a 3D, wrapped vector.
      
      :type: :class:`mathutils.Vector`


   .. attribute:: select

      Selected state of this element.
      
      :type: bool


   .. attribute:: tag

      Generic attribute scripts can use for own logic
      
      :type: bool




.. class:: BMEdge

   The BMesh edge connecting 2 verts

   .. method:: calc_face_angle(fallback=None)
   
      Return the angle between this edge's two connected faces.
   
      :param fallback: return this when the edge doesn't have 2 faces
         (instead of raising a :exc:`ValueError`).
      :type fallback: Any
      :return: The angle between 2 connected faces in radians.
      :rtype: float


   .. method:: calc_face_angle_signed(fallback=None)
   
      Return the signed angle between this edge's two connected faces.
   
      :param fallback: return this when the edge doesn't have 2 faces
         (instead of raising a :exc:`ValueError`).
      :type fallback: Any
      :return: The angle between 2 connected faces in radians (negative for concave join).
      :rtype: float


   .. method:: calc_length()
   
      Return the length of the edge.
   
      :return: The length between both verts.
      :rtype: float


   .. method:: calc_tangent(loop)
   
      Return the tangent at this edge relative to a face (pointing inward into the face).
      This uses the face normal for calculation.
   
      :param loop: The loop used for tangent calculation.
      :type loop: :class:`bmesh.types.BMLoop`
      :return: a normalized vector.
      :rtype: :class:`mathutils.Vector`


   .. method:: copy_from(other)
   
      Copy values from another element of matching type.
   
      :param other: Another element of the same type to copy from.
      :type other: Self


   .. method:: hide_set(hide)
   
      Set the hide state.
      This is different from the *hide* attribute because it updates the selection and hide state of associated geometry.
   
      :param hide: Hidden or visible.
      :type hide: bool


   .. method:: normal_update()
   
      Update normals of all connected faces and the edge verts.
   
      .. note::
   
         The normal of edge vertex will be a zero vector if vertex :attr:`is_wire` is True.


   .. method:: other_vert(vert)
   
      Return the other vertex on this edge or None if the vertex is not used by this edge.
   
      :param vert: a vert in this edge.
      :type vert: :class:`bmesh.types.BMVert`
      :return: The edge's other vert.
      :rtype: :class:`bmesh.types.BMVert` | None


   .. method:: select_set(select)
   
      Set the selection.
      This is different from the *select* attribute because it updates the selection state of associated geometry.
   
      :param select: Select or de-select.
      :type select: bool
   
      .. note::
   
         This flushes selection down (e.g. selecting a face also selects its edges and vertices), but not up (e.g. de-selecting a vertex won't de-select faces that use it). Before finishing with a mesh, flushing is typically still needed.


   .. attribute:: hide

      Hidden state of this element.
      
      :type: bool


   .. attribute:: index

      Index of this element.
      
      :type: int
      
      .. note::
      
         This value is not necessarily valid, while editing the mesh it can become *dirty*.
      
         It's also possible to assign any number to this attribute for a scripts internal logic.
      
         To ensure the value is up to date - see :meth:`bmesh.types.BMElemSeq.index_update`.


   .. attribute:: is_boundary

      True when this edge is at the boundary of a face (read-only).
      
      :type: bool


   .. attribute:: is_contiguous

      True when this edge is manifold, between two faces with the same winding (read-only).
      
      :type: bool


   .. attribute:: is_convex

      True when this edge joins two convex faces, depends on a valid face normal (read-only).
      
      :type: bool


   .. attribute:: is_manifold

      True when this edge is manifold (read-only).
      
      :type: bool


   .. attribute:: is_valid

      True when this element is valid (hasn't been freed or removed).
      
      :type: bool


   .. attribute:: is_wire

      True when this edge is not connected to any faces (read-only).
      
      :type: bool


   .. attribute:: link_faces

      Faces connected to this edge, (read-only).
      
      :type: :class:`bmesh.types.BMElemSeq`\ [:class:`bmesh.types.BMFace`]


   .. attribute:: link_loops

      Loops connected to this edge, (read-only).
      
      :type: :class:`bmesh.types.BMElemSeq`\ [:class:`bmesh.types.BMLoop`]


   .. attribute:: seam

      Seam for UV unwrapping.
      
      :type: bool


   .. attribute:: select

      Selected state of this element.
      
      :type: bool


   .. attribute:: smooth

      Smooth state of this element.
      
      :type: bool


   .. attribute:: tag

      Generic attribute scripts can use for own logic
      
      :type: bool


   .. attribute:: verts

      Verts this edge uses (always 2), (read-only).
      
      :type: :class:`bmesh.types.BMElemSeq`\ [:class:`bmesh.types.BMVert`]




.. class:: BMFace

   The BMesh face with 3 or more sides

   .. method:: calc_area()
   
      Return the area of the face.
   
      :return: The area of the face.
      :rtype: float


   .. method:: calc_center_bounds()
   
      Return bounds center of the face.
   
      :return: a 3D vector.
      :rtype: :class:`mathutils.Vector`


   .. method:: calc_center_median()
   
      Return median center of the face.
   
      :return: a 3D vector.
      :rtype: :class:`mathutils.Vector`


   .. method:: calc_center_median_weighted()
   
      Return median center of the face weighted by edge lengths.
   
      :return: a 3D vector.
      :rtype: :class:`mathutils.Vector`


   .. method:: calc_perimeter()
   
      Return the perimeter of the face.
   
      :return: The perimeter of the face.
      :rtype: float


   .. method:: calc_tangent_edge()
   
      Return face tangent based on longest edge.
   
      :return: a normalized vector.
      :rtype: :class:`mathutils.Vector`


   .. method:: calc_tangent_edge_diagonal()
   
      Return face tangent based on the edge farthest from any vertex.
   
      :return: a normalized vector.
      :rtype: :class:`mathutils.Vector`


   .. method:: calc_tangent_edge_pair()
   
      Return face tangent based on the two longest disconnected edges.
   
      - Tris: Use the edge pair with the most similar lengths.
      - Quads: Use the longest edge pair.
      - NGons: Use the two longest disconnected edges.
   
      :return: a normalized vector.
      :rtype: :class:`mathutils.Vector`


   .. method:: calc_tangent_vert_diagonal()
   
      Return face tangent based on the two most distant vertices.
   
      :return: a normalized vector.
      :rtype: :class:`mathutils.Vector`


   .. method:: copy(*, verts=True, edges=True)
   
      Make a copy of this face.
   
      :param verts: When set, the faces verts will be duplicated too.
      :type verts: bool
      :param edges: When set, the faces edges will be duplicated too.
      :type edges: bool
      :return: The newly created face.
      :rtype: :class:`bmesh.types.BMFace`


   .. method:: copy_from(other)
   
      Copy values from another element of matching type.
   
      :param other: Another element of the same type to copy from.
      :type other: Self


   .. method:: copy_from_face_interp(face, vert=True)
   
      Interpolate the customdata from another face onto this one (faces should overlap).
   
      :param face: The face to interpolate data from.
      :type face: :class:`bmesh.types.BMFace`
      :param vert: When True, also copy vertex data.
      :type vert: bool


   .. method:: hide_set(hide)
   
      Set the hide state.
      This is different from the *hide* attribute because it updates the selection and hide state of associated geometry.
   
      :param hide: Hidden or visible.
      :type hide: bool


   .. method:: normal_flip()
   
      Reverses winding of a face, which flips its normal.


   .. method:: normal_update()
   
      Update face normal based on the positions of the face verts.
      This does not update the normals of face verts.


   .. method:: select_set(select)
   
      Set the selection.
      This is different from the *select* attribute because it updates the selection state of associated geometry.
   
      :param select: Select or de-select.
      :type select: bool
   
      .. note::
   
         This flushes selection down (e.g. selecting a face also selects its edges and vertices), but not up (e.g. de-selecting a vertex won't de-select faces that use it). Before finishing with a mesh, flushing is typically still needed.


   .. method:: uv_select_set(select)
   
      Set the UV face selection state.
   
      :param select: Select or de-select.
      :type select: bool
   
      .. note::
   
         This flushes selection down (selecting a face also selects its edges and vertices), but not up. Before finishing with a mesh, flushing with :meth:`bmesh.types.BMesh.uv_select_flush_mode` is still needed.


   .. attribute:: edges

      Edges of this face, (read-only).
      
      :type: :class:`bmesh.types.BMElemSeq`\ [:class:`bmesh.types.BMEdge`]


   .. attribute:: hide

      Hidden state of this element.
      
      :type: bool


   .. attribute:: index

      Index of this element.
      
      :type: int
      
      .. note::
      
         This value is not necessarily valid, while editing the mesh it can become *dirty*.
      
         It's also possible to assign any number to this attribute for a scripts internal logic.
      
         To ensure the value is up to date - see :meth:`bmesh.types.BMElemSeq.index_update`.


   .. attribute:: is_valid

      True when this element is valid (hasn't been freed or removed).
      
      :type: bool


   .. attribute:: loops

      Loops of this face, (read-only).
      
      :type: :class:`bmesh.types.BMElemSeq`\ [:class:`bmesh.types.BMLoop`]


   .. attribute:: material_index

      The face's material index.
      
      :type: int


   .. attribute:: normal

      The normal for this face as a 3D, wrapped vector.
      
      :type: :class:`mathutils.Vector`


   .. attribute:: select

      Selected state of this element.
      
      :type: bool


   .. attribute:: smooth

      Smooth state of this element.
      
      :type: bool


   .. attribute:: tag

      Generic attribute scripts can use for own logic
      
      :type: bool


   .. attribute:: uv_select

      UV selected state of this element.
      
      :type: bool


   .. attribute:: verts

      Verts of this face, (read-only).
      
      :type: :class:`bmesh.types.BMElemSeq`\ [:class:`bmesh.types.BMVert`]




.. class:: BMLoop

   This is normally accessed from :class:`bmesh.types.BMFace.loops` where each face loop represents a corner of the face.

   .. method:: calc_angle()
   
      Return the angle at this loops corner of the face.
      This is calculated so sharper corners give lower angles.
   
      :return: The angle in radians.
      :rtype: float


   .. method:: calc_normal()
   
      Return normal at this loops corner of the face.
      Falls back to the face normal for straight lines.
   
      :return: a normalized vector.
      :rtype: :class:`mathutils.Vector`


   .. method:: calc_tangent()
   
      Return the tangent at this loops corner of the face (pointing inward into the face).
      Falls back to the face normal for straight lines.
   
      :return: a normalized vector.
      :rtype: :class:`mathutils.Vector`


   .. method:: copy_from(other)
   
      Copy values from another element of matching type.
   
      :param other: Another element of the same type to copy from.
      :type other: Self


   .. method:: copy_from_face_interp(face, vert=True, multires=True)
   
      Interpolate the customdata from a face onto this loop (the loop's vert should overlap the face).
   
      :param face: The face to interpolate data from.
      :type face: :class:`bmesh.types.BMFace`
      :param vert: When enabled, interpolate the loop's vertex data (optional).
      :type vert: bool
      :param multires: When enabled, interpolate the loop's multires data (optional).
      :type multires: bool


   .. method:: uv_select_edge_set(select)
   
      Set the UV edge selection state.
   
      :param select: Select or de-select.
      :type select: bool
   
      .. note::
   
         This flushes selection down (selecting an edge also selects its vertices), but not up (de-selecting a vertex won't de-select the edges & faces that use it). Before finishing with a mesh, flushing with :meth:`bmesh.types.BMesh.uv_select_flush_mode` is still needed.


   .. method:: uv_select_vert_set(select)
   
      Set the UV vertex selection state.
   
      :param select: Select or de-select.
      :type select: bool
   
      .. note::
   
         This does not flush selection, so selecting a vertex won't select the edges & faces that use it. Before finishing with a mesh, flushing with :meth:`bmesh.types.BMesh.uv_select_flush_mode` is still needed.


   .. attribute:: edge

      The loop's edge (between this loop and the next), (read-only).
      
      :type: :class:`bmesh.types.BMEdge`


   .. attribute:: face

      The face this loop belongs to (read-only).
      
      :type: :class:`bmesh.types.BMFace`


   .. attribute:: index

      Index of this element.
      
      :type: int
      
      .. note::
      
         This value is not necessarily valid, while editing the mesh it can become *dirty*.
      
         It's also possible to assign any number to this attribute for a scripts internal logic.
      
         To ensure the value is up to date - see :meth:`bmesh.types.BMElemSeq.index_update`.


   .. attribute:: is_convex

      True when this loop is at the convex corner of a face, depends on a valid face normal (read-only).
      
      :type: bool


   .. attribute:: is_valid

      True when this element is valid (hasn't been freed or removed).
      
      :type: bool


   .. attribute:: link_loop_next

      The next face corner (read-only).
      
      :type: :class:`bmesh.types.BMLoop`


   .. attribute:: link_loop_prev

      The previous face corner (read-only).
      
      :type: :class:`bmesh.types.BMLoop`


   .. attribute:: link_loop_radial_next

      The next loop around the edge (read-only).
      
      :type: :class:`bmesh.types.BMLoop`


   .. attribute:: link_loop_radial_prev

      The previous loop around the edge (read-only).
      
      :type: :class:`bmesh.types.BMLoop`


   .. attribute:: link_loops

      Loops connected to this loop, (read-only).
      
      :type: :class:`bmesh.types.BMElemSeq`\ [:class:`bmesh.types.BMLoop`]


   .. attribute:: tag

      Generic attribute scripts can use for own logic
      
      :type: bool


   .. attribute:: uv_select_edge

      UV edge selected state of this loop.
      
      :type: bool


   .. attribute:: uv_select_vert

      UV vertex selected state of this loop.
      
      :type: bool


   .. attribute:: vert

      The loop's vertex (read-only).
      
      :type: :class:`bmesh.types.BMVert`




Sequence Accessors
------------------

.. class:: BMElemSeq

   General sequence type used for accessing any sequence of
   :class:`bmesh.types.BMVert`, :class:`bmesh.types.BMEdge`, :class:`bmesh.types.BMFace`, :class:`bmesh.types.BMLoop`.
   
   When accessed via :class:`bmesh.types.BMesh.verts`, :class:`bmesh.types.BMesh.edges`, :class:`bmesh.types.BMesh.faces`
   there are also functions to create/remove items.

   .. method:: index_update()
   
      Initialize the index values of this sequence.
   
      This is the equivalent of looping over all elements and assigning the index values.
   
      .. code-block:: python
   
         for index, ele in enumerate(sequence):
             ele.index = index
   
      .. note::
   
         Running this on sequences besides :class:`bmesh.types.BMesh.verts`, :class:`bmesh.types.BMesh.edges`, :class:`bmesh.types.BMesh.faces`
         works but won't result in each element having a valid index, instead its order in the sequence will be set.




.. class:: BMVertSeq


   .. method:: ensure_lookup_table()
   
      Ensure internal data needed for int subscript access is initialized with verts/edges/faces, eg ``bm.verts[index]``.
   
      This needs to be called again after adding/removing data in this sequence.


   .. method:: index_update()
   
      Initialize the index values of this sequence.
   
      This is the equivalent of looping over all elements and assigning the index values.
   
      .. code-block:: python
   
         for index, ele in enumerate(sequence):
             ele.index = index
   
      .. note::
   
         Running this on sequences besides :class:`bmesh.types.BMesh.verts`, :class:`bmesh.types.BMesh.edges`, :class:`bmesh.types.BMesh.faces`
         works but won't result in each element having a valid index, instead its order in the sequence will be set.


   .. method:: new(co=(0.0, 0.0, 0.0), source=None)
   
      Create a new vertex.
   
      :param co: The initial location of the vertex (optional argument).
      :type co: tuple[float, float, float] | Sequence[float]
      :param source: Existing vert to initialize settings.
      :type source: :class:`bmesh.types.BMVert` | None
      :return: The newly created vertex.
      :rtype: :class:`bmesh.types.BMVert`


   .. method:: remove(vert)
   
      Remove a vert.
   
      :param vert: The vert to remove.
      :type vert: :class:`bmesh.types.BMVert`


   .. method:: sort(*, key=None, reverse=False)
   
      Sort the elements of this sequence, using an optional custom sort key.
      Indices of elements are not changed, :meth:`bmesh.types.BMElemSeq.index_update` can be used for that.
   
      :param key: The key that sets the ordering of the elements.
      :type key: Callable[[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`], int] | None
      :param reverse: Reverse the order of the elements
      :type reverse: bool
   
      .. note::
   
         When the 'key' argument is not provided, the elements are reordered following their current index value.
         In particular this can be used by setting indices manually before calling this method.
   
      .. warning::
   
         Existing references to the N'th element, will continue to point the data at that index.


   .. attribute:: layers

      custom-data layers (read-only).
      
      :type: :class:`bmesh.types.BMLayerAccessVert`




.. class:: BMEdgeSeq


   .. method:: ensure_lookup_table()
   
      Ensure internal data needed for int subscript access is initialized with verts/edges/faces, eg ``bm.verts[index]``.
   
      This needs to be called again after adding/removing data in this sequence.


   .. method:: get(verts, fallback=None)
   
      Return an edge which uses the **verts** passed.
   
      :param verts: Pair of verts (exactly 2).
      :type verts: Sequence[:class:`bmesh.types.BMVert`]
      :param fallback: Return this value if nothing is found.
      :type fallback: Any
      :return: The edge found or the fallback value.
      :rtype: :class:`bmesh.types.BMEdge` | None


   .. method:: index_update()
   
      Initialize the index values of this sequence.
   
      This is the equivalent of looping over all elements and assigning the index values.
   
      .. code-block:: python
   
         for index, ele in enumerate(sequence):
             ele.index = index
   
      .. note::
   
         Running this on sequences besides :class:`bmesh.types.BMesh.verts`, :class:`bmesh.types.BMesh.edges`, :class:`bmesh.types.BMesh.faces`
         works but won't result in each element having a valid index, instead its order in the sequence will be set.


   .. method:: new(verts, source=None)
   
      Create a new edge from a given pair of verts.
   
      :param verts: Vertex pair.
      :type verts: Sequence[:class:`bmesh.types.BMVert`]
      :param source: Existing edge to initialize settings (optional argument).
      :type source: :class:`bmesh.types.BMEdge` | None
      :return: The newly created edge.
      :rtype: :class:`bmesh.types.BMEdge`


   .. method:: remove(edge)
   
      Remove an edge.
   
      :param edge: The edge to remove.
      :type edge: :class:`bmesh.types.BMEdge`


   .. method:: sort(*, key=None, reverse=False)
   
      Sort the elements of this sequence, using an optional custom sort key.
      Indices of elements are not changed, :meth:`bmesh.types.BMElemSeq.index_update` can be used for that.
   
      :param key: The key that sets the ordering of the elements.
      :type key: Callable[[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`], int] | None
      :param reverse: Reverse the order of the elements
      :type reverse: bool
   
      .. note::
   
         When the 'key' argument is not provided, the elements are reordered following their current index value.
         In particular this can be used by setting indices manually before calling this method.
   
      .. warning::
   
         Existing references to the N'th element, will continue to point the data at that index.


   .. attribute:: layers

      custom-data layers (read-only).
      
      :type: :class:`bmesh.types.BMLayerAccessEdge`




.. class:: BMFaceSeq


   .. method:: ensure_lookup_table()
   
      Ensure internal data needed for int subscript access is initialized with verts/edges/faces, eg ``bm.verts[index]``.
   
      This needs to be called again after adding/removing data in this sequence.


   .. method:: get(verts, fallback=None)
   
      Return a face which uses the **verts** passed.
   
      :param verts: Sequence of verts.
      :type verts: Sequence[:class:`bmesh.types.BMVert`]
      :param fallback: Return this value if nothing is found.
      :type fallback: Any
      :return: The face found or the fallback value.
      :rtype: :class:`bmesh.types.BMFace` | None


   .. method:: index_update()
   
      Initialize the index values of this sequence.
   
      This is the equivalent of looping over all elements and assigning the index values.
   
      .. code-block:: python
   
         for index, ele in enumerate(sequence):
             ele.index = index
   
      .. note::
   
         Running this on sequences besides :class:`bmesh.types.BMesh.verts`, :class:`bmesh.types.BMesh.edges`, :class:`bmesh.types.BMesh.faces`
         works but won't result in each element having a valid index, instead its order in the sequence will be set.


   .. method:: new(verts, source=None)
   
      Create a new face from a given set of verts.
   
      :param verts: Sequence of 3 or more verts.
      :type verts: Sequence[:class:`bmesh.types.BMVert`]
      :param source: Existing face to initialize settings (optional argument).
      :type source: :class:`bmesh.types.BMFace` | None
      :return: The newly created face.
      :rtype: :class:`bmesh.types.BMFace`


   .. method:: remove(face)
   
      Remove a face.
   
      :param face: The face to remove.
      :type face: :class:`bmesh.types.BMFace`


   .. method:: sort(*, key=None, reverse=False)
   
      Sort the elements of this sequence, using an optional custom sort key.
      Indices of elements are not changed, :meth:`bmesh.types.BMElemSeq.index_update` can be used for that.
   
      :param key: The key that sets the ordering of the elements.
      :type key: Callable[[:class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace`], int] | None
      :param reverse: Reverse the order of the elements
      :type reverse: bool
   
      .. note::
   
         When the 'key' argument is not provided, the elements are reordered following their current index value.
         In particular this can be used by setting indices manually before calling this method.
   
      .. warning::
   
         Existing references to the N'th element, will continue to point the data at that index.


   .. attribute:: active

      active face.
      
      :type: :class:`bmesh.types.BMFace` | None


   .. attribute:: layers

      custom-data layers (read-only).
      
      :type: :class:`bmesh.types.BMLayerAccessFace`




.. class:: BMLoopSeq


   .. attribute:: layers

      custom-data layers (read-only).
      
      :type: :class:`bmesh.types.BMLayerAccessLoop`




.. class:: BMIter

   Internal BMesh type for looping over verts/faces/edges,
   used for iterating over :class:`bmesh.types.BMElemSeq` types.



Selection History
-----------------

.. class:: BMEditSelSeq


   .. method:: add(element)
   
      Add an element to the selection history (no action taken if its already added).
   
      :param element: The element to add.
      :type element: :class:`BMVert` | :class:`BMEdge` | :class:`BMFace`


   .. method:: clear()
   
      Empties the selection history.


   .. method:: discard(element)
   
      Discard an element from the selection history.
   
      Like remove but doesn't raise an error when the element is not in the selection list.
   
      :param element: The element to discard.
      :type element: :class:`BMVert` | :class:`BMEdge` | :class:`BMFace`


   .. method:: remove(element)
   
      Remove an element from the selection history.
   
      :param element: The element to remove.
      :type element: :class:`BMVert` | :class:`BMEdge` | :class:`BMFace`


   .. method:: validate()
   
      Ensures all elements in the selection history are selected.


   .. attribute:: active

      The last selected element or None (read-only).
      
      :type: :class:`bmesh.types.BMVert` | :class:`bmesh.types.BMEdge` | :class:`bmesh.types.BMFace` | None




.. class:: BMEditSelIter




Custom-Data Layer Access
------------------------

.. class:: BMLayerAccessVert

   Exposes custom-data layer attributes.

   .. attribute:: bool

      Generic boolean custom-data layer.
      
      :type: :class:`bmesh.types.BMLayerCollection`\ [bool]


   .. attribute:: color

      Generic RGBA color with 8-bit precision custom-data layer.
      
      :type: :class:`bmesh.types.BMLayerCollection`\ [:class:`mathutils.Vector`]


   .. attribute:: deform

      Vertex deform weight :class:`bmesh.types.BMDeformVert` (TODO).
      
      :type: :class:`bmesh.types.BMLayerCollection`\ [:class:`bmesh.types.BMDeformVert`]


   .. attribute:: float

      Generic float custom-data layer.
      
      :type: :class:`bmesh.types.BMLayerCollection`\ [float]


   .. attribute:: float_color

      Generic RGBA color with float precision custom-data layer.
      
      :type: :class:`bmesh.types.BMLayerCollection`\ [:class:`mathutils.Vector`]


   .. attribute:: float_vector

      Generic 3D vector with float precision custom-data layer.
      
      :type: :class:`bmesh.types.BMLayerCollection`\ [:class:`mathutils.Vector`]


   .. attribute:: int

      Generic int custom-data layer.
      
      :type: :class:`bmesh.types.BMLayerCollection`\ [int]


   .. attribute:: shape

      Vertex shape-key absolute location (as a 3D Vector).
      
      :type: :class:`bmesh.types.BMLayerCollection`\ [:class:`mathutils.Vector`]


   .. attribute:: skin

      Accessor for skin layer.
      
      :type: :class:`bmesh.types.BMLayerCollection`\ [:class:`bmesh.types.BMVertSkin`]


   .. attribute:: string

      Generic string custom-data layer (exposed as bytes, 255 max length).
      
      :type: :class:`bmesh.types.BMLayerCollection`\ [bytes]




.. class:: BMLayerAccessEdge

   Exposes custom-data layer attributes.

   .. attribute:: bool

      Generic boolean custom-data layer.
      
      :type: :class:`bmesh.types.BMLayerCollection`\ [bool]


   .. attribute:: color

      Generic RGBA color with 8-bit precision custom-data layer.
      
      :type: :class:`bmesh.types.BMLayerCollection`\ [:class:`mathutils.Vector`]


   .. attribute:: float

      Generic float custom-data layer.
      
      :type: :class:`bmesh.types.BMLayerCollection`\ [float]


   .. attribute:: float_color

      Generic RGBA color with float precision custom-data layer.
      
      :type: :class:`bmesh.types.BMLayerCollection`\ [:class:`mathutils.Vector`]


   .. attribute:: float_vector

      Generic 3D vector with float precision custom-data layer.
      
      :type: :class:`bmesh.types.BMLayerCollection`\ [:class:`mathutils.Vector`]


   .. attribute:: int

      Generic int custom-data layer.
      
      :type: :class:`bmesh.types.BMLayerCollection`\ [int]


   .. attribute:: string

      Generic string custom-data layer (exposed as bytes, 255 max length).
      
      :type: :class:`bmesh.types.BMLayerCollection`\ [bytes]




.. class:: BMLayerAccessFace

   Exposes custom-data layer attributes.

   .. attribute:: bool

      Generic boolean custom-data layer.
      
      :type: :class:`bmesh.types.BMLayerCollection`\ [bool]


   .. attribute:: color

      Generic RGBA color with 8-bit precision custom-data layer.
      
      :type: :class:`bmesh.types.BMLayerCollection`\ [:class:`mathutils.Vector`]


   .. attribute:: float

      Generic float custom-data layer.
      
      :type: :class:`bmesh.types.BMLayerCollection`\ [float]


   .. attribute:: float_color

      Generic RGBA color with float precision custom-data layer.
      
      :type: :class:`bmesh.types.BMLayerCollection`\ [:class:`mathutils.Vector`]


   .. attribute:: float_vector

      Generic 3D vector with float precision custom-data layer.
      
      :type: :class:`bmesh.types.BMLayerCollection`\ [:class:`mathutils.Vector`]


   .. attribute:: int

      Generic int custom-data layer.
      
      :type: :class:`bmesh.types.BMLayerCollection`\ [int]


   .. attribute:: string

      Generic string custom-data layer (exposed as bytes, 255 max length).
      
      :type: :class:`bmesh.types.BMLayerCollection`\ [bytes]




.. class:: BMLayerAccessLoop

   Exposes custom-data layer attributes.

   .. attribute:: bool

      Generic boolean custom-data layer.
      
      :type: :class:`bmesh.types.BMLayerCollection`\ [bool]


   .. attribute:: color

      Generic RGBA color with 8-bit precision custom-data layer.
      
      :type: :class:`bmesh.types.BMLayerCollection`\ [:class:`mathutils.Vector`]


   .. attribute:: float

      Generic float custom-data layer.
      
      :type: :class:`bmesh.types.BMLayerCollection`\ [float]


   .. attribute:: float_color

      Generic RGBA color with float precision custom-data layer.
      
      :type: :class:`bmesh.types.BMLayerCollection`\ [:class:`mathutils.Vector`]


   .. attribute:: float_vector

      Generic 3D vector with float precision custom-data layer.
      
      :type: :class:`bmesh.types.BMLayerCollection`\ [:class:`mathutils.Vector`]


   .. attribute:: int

      Generic int custom-data layer.
      
      :type: :class:`bmesh.types.BMLayerCollection`\ [int]


   .. attribute:: string

      Generic string custom-data layer (exposed as bytes, 255 max length).
      
      :type: :class:`bmesh.types.BMLayerCollection`\ [bytes]


   .. attribute:: uv

      Accessor for :class:`bmesh.types.BMLoopUV` UV (as a 2D Vector).
      
      :type: :class:`bmesh.types.BMLayerCollection`\ [:class:`bmesh.types.BMLoopUV`]




.. class:: BMLayerCollection

   Gives access to a collection of custom-data layers of the same type and behaves like Python dictionaries, except for the ability to do list like index access.

   .. method:: get(key, default=None)
   
      Returns the value of the layer matching the key or default
      when not found (matches Python's dictionary function of the same name).
   
      :param key: The key associated with the layer.
      :type key: str
      :param default: Optional argument for the value to return if
         *key* is not found.
      :type default: Any
      :return: The layer matching the key or the default value.
      :rtype: :class:`bmesh.types.BMLayerItem` | Any


   .. method:: items()
   
      Return the (key, value) pairs of collection members
      (matching Python's dict.items() functionality).
   
      :return: (key, value) pairs for each member of this collection.
      :rtype: list[tuple[str, :class:`bmesh.types.BMLayerItem`]]


   .. method:: keys()
   
      Return the identifiers of collection members
      (matching Python's dict.keys() functionality).
   
      :return: the identifiers for each member of this collection.
      :rtype: list[str]


   .. method:: new(name="")
   
      Create a new layer
   
      :param name: Optional name argument (will be made unique).
      :type name: str
      :return: The newly created layer.
      :rtype: :class:`bmesh.types.BMLayerItem`


   .. method:: remove(layer)
   
      Remove a layer
   
      :param layer: The layer to remove.
      :type layer: :class:`bmesh.types.BMLayerItem`


   .. method:: values()
   
      Return the values of collection
      (matching Python's dict.values() functionality).
   
      :return: the members of this collection.
      :rtype: list[:class:`bmesh.types.BMLayerItem`]


   .. method:: verify()
   
      Create a new layer or return an existing active layer
   
      :return: The newly created layer, or the existing active layer.
      :rtype: :class:`bmesh.types.BMLayerItem`


   .. attribute:: active

      The active layer of this type (read-only).
      
      :type: :class:`bmesh.types.BMLayerItem` | None


   .. attribute:: is_singleton

      True if there can exist only one layer of this type (read-only).
      
      :type: bool




.. class:: BMLayerItem

   Exposes a single custom data layer, its main purpose is for use as an item accessor to custom-data when used with vert/edge/face/loop data.

   .. method:: copy_from(other)
   
      Copy data from another layer.
   
      :param other: Another layer to copy from.
      :type other: :class:`bmesh.types.BMLayerItem`


   .. attribute:: name

      The layer's unique name (read-only).
      
      :type: str




Custom-Data Layer Types
-----------------------

.. class:: BMLoopUV


   .. attribute:: pin_uv

      UV pin state.
      
      :type: bool


   .. attribute:: uv

      Loop UV (as a 2D Vector).
      
      :type: :class:`mathutils.Vector`




.. class:: BMDeformVert


   .. method:: clear()
   
      Clears all weights.


   .. method:: get(key, default=None)
   
      Returns the deform weight matching the key or default
      when not found (matches Python's dictionary function of the same name).
   
      :param key: The vertex group index.
      :type key: int
      :param default: Optional argument for the value to return if
         *key* is not found.
      :type default: Any
      :return: The deform weight or the default when not found.
      :rtype: float | Any


   .. method:: items()
   
      Return (group, weight) pairs for this vertex
      (matching Python's dict.items() functionality).
   
      :return: (key, value) pairs for each deform weight of this vertex.
      :rtype: list[tuple[int, float]]


   .. method:: keys()
   
      Return the group indices used by this vertex
      (matching Python's dict.keys() functionality).
   
      :return: The deform group indices this vertex uses.
      :rtype: list[int]


   .. method:: values()
   
      Return the weights of the deform vertex
      (matching Python's dict.values() functionality).
   
      :return: The weights that influence this vertex
      :rtype: list[float]




