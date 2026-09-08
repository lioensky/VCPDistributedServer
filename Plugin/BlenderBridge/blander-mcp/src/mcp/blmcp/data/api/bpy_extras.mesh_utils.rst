bpy_extras submodule (bpy_extras.mesh_utils)
============================================

.. module:: bpy_extras.mesh_utils

.. function:: mesh_linked_uv_islands(mesh)

   Returns lists of polygon indices connected by UV islands.
   
   :param mesh: the mesh used to group with.
   :type mesh: :class:`bpy.types.Mesh`
   :return: list of lists containing polygon indices
   :rtype: list[list[int]]

.. function:: mesh_linked_triangles(mesh)

   Splits the mesh into connected triangles, use this for separating cubes from
   other mesh elements within 1 mesh data-block.
   
   :param mesh: the mesh used to group with.
   :type mesh: :class:`bpy.types.Mesh`
   :return: Lists of lists containing triangles.
   :rtype: list[list[:class:`bpy.types.MeshLoopTriangle`]]

.. function:: edge_face_count_dict(mesh)

   :param mesh: The mesh to count edges for.
   :type mesh: :class:`bpy.types.Mesh`
   :return: Dictionary of edge keys with their value set to the number of faces using each edge.
   :rtype: dict[tuple[int, int], int]

.. function:: edge_face_count(mesh)

   :param mesh: The mesh to count edges for.
   :type mesh: :class:`bpy.types.Mesh`
   :return: list of face users for each item in mesh.edges.
   :rtype: list[int]

.. function:: edge_loops_from_edges(mesh, edges=None)

   Edge loops defined by edges.
   
   Takes mesh.edges or a list of edges and returns the edge loops
   as a list of vertex indices.
   Closed loops have matching start and end values.
   
   :param mesh: The mesh to extract edge loops from.
   :type mesh: :class:`bpy.types.Mesh`
   :param edges: Edges to use, or None to use all edges in the mesh.
   :type edges: list[:class:`bpy.types.MeshEdge`] | None
   :return: A list of edge loops, each a list of vertex indices.
   :rtype: list[list[int]]

.. function:: ngon_tessellate(from_data, indices, fix_loops=True, debug_print=True)

   Takes a poly-line of indices (ngon) and returns a list of face
   index lists. Designed to be used for importers that need indices for an
   ngon to create from existing verts.
   
   :param from_data: Either a mesh, or a list/tuple of 3D vectors.
   :type from_data: :class:`bpy.types.Mesh` | list[Sequence[float]] | tuple[Sequence[float]]
   :param indices: a list of indices to use.
      This list is the ordered closed poly-line to fill, and can be a subset of the data given.
   :type indices: list[int]
   :param fix_loops: If this is enabled poly-lines
      that use loops to make multiple
      poly-lines are dealt with correctly.
   :type fix_loops: bool
   :param debug_print: Print debug information to the console.
   :type debug_print: bool
   :return: Tessellated faces as a list of triangle index tuples.
   :rtype: list[tuple[int, int, int]]

.. function:: triangle_random_points(num_points, loop_triangles)

   Generates a list of random points over mesh loop triangles.
   
   :param num_points: The number of random points to generate on each triangle.
   :type num_points: int
   :param loop_triangles: Sequence of the triangles to generate points on.
   :type loop_triangles: Sequence[:class:`bpy.types.MeshLoopTriangle`]
   :return: List of random points over all triangles.
   :rtype: list[:class:`mathutils.Vector`]

