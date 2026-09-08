.. _bpy.ops.object.data_transfer:

******************
Transfer Mesh Data
******************

.. reference::

   :Mode:      Object Mode
   :Menu:      :menuselection:`Object --> Link/Transfer Data --> Transfer Mesh Data`

*Transfer Mesh Data* copies a certain type of data from the active mesh to the selected meshes.
This could be :doc:`UV maps </editors/uv/introduction>`,
:ref:`color attributes <modeling-meshes-properties-object_data-color-attributes>`,
:ref:`custom normals <modeling_meshes_normals_custom>`, and so on.

For each element (vertex/edge/face) in each destination mesh, the operator finds one
or more matching elements in the source mesh, then interpolates between those source
elements' values.

.. seealso::

   :doc:`/modeling/modifiers/modify/data_transfer`

The :ref:`bpy.ops.screen.redo_last` panel offers the following options.

Freeze Operator
   Prevent changes to the settings from re-running the data transfer.
   This is useful if you are editing several settings at once with heavy geometry.
Data Type
   Which data to transfer.

   .. figure:: /images/scene-layout_object_editing_link-transfer_transfer-mesh-data_menu.png

      Data types.

Create Data
   Add any missing data layers on the destination meshes (e.g. create missing vertex groups).
Mapping
   How to find the matching source element(s) for each destination element.
   The various options are explained in the `Mapping`_ section below.
Auto Transform
   If the source and destination meshes don't overlap in world space, you can enable this
   option to calculate a transformation automatically. While this is quick and easy, however,
   you may get better results by making them overlap by hand.
Object Transform
   Whether take into account the world space transformations of the source and destination objects.
   When unchecked, the operator acts like all objects are in the same position and have
   the default rotation and scale.
Only Neighbor Geometry
   Only consider source elements that are close enough to the destination one.

   Max Distance
      Maximum allowed distance between source and destination element (for non-topology mappings).

Ray Radius
   The starting radius to use when `ray casting <https://en.wikipedia.org/wiki/Ray_casting>`__.

   For certain mapping types, the operator performs a series of ray casts from each destination
   element to find matching source elements. These ray casts start with the specified radius and
   grow progressively larger until a match is found or a limit is reached.

   A low starting radius will give more accurate results, but has worse performance if it's too
   small and needs to be increased. A high starting radius has better performance,
   but may result in suboptimal matches.

   In general, use a low radius for dense source meshes and a high one for simple ones.

Islands Precision
   Controls the calculation that prevents a destination face from receiving UV coordinates from
   disparate source UV islands (areas bordered by :doc:`seams </modeling/meshes/uv/unwrapping/seams>`).
   Keeping this at 0.0 means no island handling at all, while higher numbers increase the correctness
   of the result at the cost of extra computation.

   Typically, small values like 0.02 are enough to get good results, but if you are mapping from
   a very high-poly source towards a very low-poly destination, you may have to raise it quite significantly.

Source Layers Selection
   Which source layers to copy to the destination meshes (e.g. only the active vertex group,
   all vertex groups, or a specific vertex group).

Destination Layers Matching
   How to find the destination layer for a given source layer: by name or by order.

Mix Mode
   How to combine the new data from the source mesh with the original data in the destination meshes.

   Replace
      Interpolate between the original and new value using *Mix Factor*.
   Above Threshold
      Replace the destination value if it's greater than or equal to *Mix Factor*.
      In the case of multi-component data like colors, the threshold is compared to the average of
      these components.

      For boolean *Data Types* like *Freestyle Mark*, you can use this to perform a logical AND:
      simply ensure the *Mix Factor* is 0.5 or greater, and the destination mesh will only have
      marked edges/faces that were already marked and are also marked in the source mesh.
   Below Threshold
      Replace the destination value if it's less than or equal to *Mix Factor*.
      In the case of multi-component data like colors, the threshold is compared to the average of
      these components.

      For boolean *Data Types* like *Freestyle Mark*, you can use this to perform a logical OR:
      simply ensure the *Mix Factor* is 0.5 or greater, and the destination mesh will have
      marked edges/faces that were already marked or are marked in the source mesh.
   Mix
      Mix the source value with the destination value, e.g. performing an alpha blend in the case
      of color attributes. Then, interpolate using *Mix Factor*.
   Add
      Add the source value to the destination value, then interpolate using *Mix Factor*.
   Subtract
      Subtract the source value from the destination value, then interpolate using *Mix Factor*.
   Multiply
      Multiply the source value by the destination value, then interpolate using *Mix Factor*.

Mix Factor
   Interpolation factor between the original destination value and the newly calculated value.
   If *Mix Mode* is *Above Threshold* or *Below Threshold*, this is a threshold value instead.


Mapping
=======

Topology
--------

Simply matches the elements based on their index. This requires all meshes to have the same
number of elements and those elements to be ordered in the same way. Best suited for
a destination mesh that's a deformed copy of the source.

.. seealso::

   :doc:`/modeling/meshes/editing/mesh/sort_elements` to ensure the objects have
   the same element ordering.


One-To-One Mappings
-------------------

These mappings always select only one source element for each destination one.

Vertex Data
   Nearest Vertex
      Use the nearest source vertex.
   Nearest Edge Vertex
      Use the nearest source vertex on the nearest (by midpoint distance) source edge.
   Nearest Face Vertex
      Use the nearest source vertex on the nearest (by midpoint distance) source face.
Edge Data
   Nearest Vertices
      Use the source edge whose vertices are nearest to the destination edge's.
   Nearest Edge
      Use the source edge whose midpoint is nearest to the destination edge's.
   Nearest Face Edge
      Use the nearest source edge on the nearest face (both by midpoint distance).
Face Corner Data
   A face corner is a vertex in the context of a face. This concept is most commonly used
   in UV maps: each face corner can have its own UV coordinate, or in other words, one 3D vertex
   can correspond to several UV vertices (one per face).

   Nearest Corner and Best Matching Normal
      Use the source corner that's nearest to the destination corner and has the most similar
      split normal.
   Nearest Corner and Best Matching Face Normal
      Use the source corner that's nearest to the destination corner and has the most similar
      face normal.
   Nearest Corner of Nearest Face
      Use the nearest source corner on the nearest source face.
Face Data
   Nearest Face
      Use the nearest source face (by midpoint distance).
   Best Normal-Matching
      Cast a ray from the destination face's centerpoint along the face's normal
      and use the source face found this way.


Interpolated Mappings
---------------------

These mappings can match several source elements and interpolate between their values.

Vertex Data
   Nearest Edge Interpolated
      Find the nearest point on the nearest source edge, then use that point to interpolate between
      the values of the edge's vertices.
   Nearest Face Interpolated
      Find the nearest point on the nearest source face, then use that point to interpolate between
      the values of the face's vertices.
   Projected Face Interpolated
      Project the destination vertex along its normal onto a source face,
      then use the projected point to interpolate between the values of the face's vertices.
Edge Data
   Projected Edge Interpolated
      Find source edges by projecting from a number of points on the destination edge
      (where each point is projected along the interpolated normals of the destination edge's vertices).
      Then, interpolate between the values of the source edges found this way.
Face Corner Data
   Nearest Face Interpolated
      Find the nearest point on the nearest source face, then use that point to interpolate between
      the values of the face's corners.
   Projected Face Interpolated
      Project the destination corner along its normal onto a source face,
      then use the projected point to interpolate between the values of the face's corners.
Face Data
   Projected Face Interpolated
      Find source faces by casting rays from a number of points on the destination face along the destination
      face's normal. Then, interpolate between the values of these source faces.
