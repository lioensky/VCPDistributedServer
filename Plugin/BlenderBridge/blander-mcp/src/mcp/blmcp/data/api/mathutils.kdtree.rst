KDTree Utilities (mathutils.kdtree)
===================================

.. module:: mathutils.kdtree

Generic 3-dimensional kd-tree to perform spatial searches.


.. literalinclude:: ./examples/mathutils.kdtree.0.py

.. class:: KDTree(size)

   KDTree(size) -> new kd-tree initialized to hold up to ``size`` items.

   :param size: Maximum number of items.
   :type size: int

   .. note::

      :meth:`KDTree.balance` must have been called before using any of the ``find`` methods.

   .. method:: balance()
   
      Balance the tree.
   
      .. note::
   
         This builds the entire tree, avoid calling after each insertion.


   .. method:: find(co, *, filter=None)
   
      Find nearest point to ``co``.
   
      :param co: 3D coordinate.
      :type co: Sequence[float]
      :param filter: function which takes an index and returns True for indices to include in the search.
      :type filter: Callable[[int], bool] | None
      :return: Returns (position, index, distance),
         or (None, None, None) when no match is found.
      :rtype: tuple[:class:`Vector`, int, float] | tuple[None, None, None]


   .. method:: find_n(co, n)
   
      Find nearest ``n`` points to ``co``.
   
      :param co: 3D coordinate.
      :type co: Sequence[float]
      :param n: Number of points to find.
      :type n: int
      :return: Returns a list of tuples (position, index, distance).
      :rtype: list[tuple[:class:`Vector`, int, float]]


   .. method:: find_range(co, radius)
   
      Find all points within ``radius`` of ``co``.
   
      :param co: 3D coordinate.
      :type co: Sequence[float]
      :param radius: Maximum distance to search for points.
      :type radius: float
      :return: Returns a list of tuples (position, index, distance).
      :rtype: list[tuple[:class:`Vector`, int, float]]


   .. method:: insert(co, index)
   
      Insert a point into the KDTree.
   
      :param co: Point 3d position.
      :type co: Sequence[float]
      :param index: The index of the point (must be non-negative).
      :type index: int




