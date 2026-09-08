BVHTree Utilities (mathutils.bvhtree)
=====================================

.. module:: mathutils.bvhtree

BVH tree structures for proximity searches and ray casts on geometry.

.. class:: BVHTree


   .. classmethod:: FromBMesh(bmesh, *, epsilon=0.0)
   
      BVH tree based on :class:`BMesh` data.
   
      :param bmesh: BMesh data.
      :type bmesh: :class:`BMesh`
      :param epsilon: Increase the threshold for detecting overlap and raycast hits.
      :type epsilon: float
      :return: BVHTree from BMesh data.
      :rtype: :class:`BVHTree`


   .. classmethod:: FromObject(object, depsgraph, *, deform=True, cage=False, epsilon=0.0)
   
      BVH tree based on :class:`Object` data.
   
      :param object: Mesh object.
      :type object: :class:`Object`
      :param depsgraph: Depsgraph to use for evaluating the mesh.
      :type depsgraph: :class:`Depsgraph`
      :param deform: Use mesh with deformations.
      :type deform: bool
      :param cage: Use modifiers cage.
      :type cage: bool
      :param epsilon: Increase the threshold for detecting overlap and raycast hits.
      :type epsilon: float
      :return: BVHTree from Object data.
      :rtype: :class:`BVHTree`


   .. classmethod:: FromPolygons(vertices, polygons, *, all_triangles=False, epsilon=0.0)
   
      BVH tree constructed from geometry passed in as arguments.
   
      :param vertices: float triplets each representing ``(x, y, z)`` coordinates.
      :type vertices: Sequence[Sequence[float]]
      :param polygons: Sequence of polygons, each containing indices to the vertices argument.
      :type polygons: Sequence[Sequence[int]]
      :param all_triangles: Use when all **polygons** are triangles for more efficient conversion.
      :type all_triangles: bool
      :param epsilon: Increase the threshold for detecting overlap and raycast hits.
      :type epsilon: float
      :return: BVHTree from polygon data.
      :rtype: :class:`BVHTree`


   .. method:: find_nearest(origin, distance=1.84467e+19, /)
   
      Find the nearest element (typically face index) to a point.
   
      :param origin: Find nearest element to this point.
      :type origin: :class:`Vector`
      :param distance: Maximum distance threshold.
      :type distance: float
      :return: Returns a tuple: (position, normal, index, distance),
         Values will all be None if no hit is found.
      :rtype: tuple[:class:`Vector` | None, :class:`Vector` | None, int | None, float | None]


   .. method:: find_nearest_range(origin, distance=1.84467e+19, /)
   
      Find the nearest elements (typically face index) to a point in the distance range.
   
      :param origin: Find nearest elements to this point.
      :type origin: :class:`Vector`
      :param distance: Maximum distance threshold.
      :type distance: float
      :return: Returns a list of tuples (position, normal, index, distance)
      :rtype: list[tuple[:class:`Vector`, :class:`Vector`, int, float]]


   .. method:: overlap(other_tree, /)
   
      Find overlapping indices between 2 trees.
   
      :param other_tree: Other tree to perform overlap test on.
      :type other_tree: :class:`BVHTree`
      :return: Returns a list of unique index pairs, the first index referencing this tree, the second referencing the **other_tree**.
      :rtype: list[tuple[int, int]]


   .. method:: ray_cast(origin, direction, distance=sys.float_info.max, /)
   
      Cast a ray onto the geometry.
   
      :param origin: Start location of the ray.
      :type origin: :class:`Vector`
      :param direction: Direction of the ray (normalized internally).
      :type direction: :class:`Vector`
      :param distance: Maximum distance threshold.
      :type distance: float
      :return: Returns a tuple: (position, normal, index, distance),
         Values will all be None if no hit is found.
      :rtype: tuple[:class:`Vector` | None, :class:`Vector` | None, int | None, float | None]




