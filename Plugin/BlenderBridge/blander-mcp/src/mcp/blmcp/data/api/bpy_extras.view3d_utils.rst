bpy_extras submodule (bpy_extras.view3d_utils)
==============================================

.. module:: bpy_extras.view3d_utils

.. function:: region_2d_to_vector_3d(region, rv3d, coord)

   Return a direction vector from the viewport at the specific 2D region
   coordinate.
   
   :param region: region of the 3D viewport, typically bpy.context.region.
   :type region: :class:`bpy.types.Region`
   :param rv3d: 3D region data, typically bpy.context.space_data.region_3d.
   :type rv3d: :class:`bpy.types.RegionView3D`
   :param coord: 2D coordinates relative to the region:
      (event.mouse_region_x, event.mouse_region_y) for example.
   :type coord: Sequence[float]
   :return: normalized 3D vector.
   :rtype: :class:`mathutils.Vector`

.. function:: region_2d_to_origin_3d(region, rv3d, coord, *, clamp=None)

   Return the 3D view origin from the region relative 2D coords.
   
   .. note::
   
      Orthographic views have a less obvious origin,
      the far clip is used to define the viewport near/far extents.
      Since far clip can be a very large value,
      the result may have numeric precision issues.
   
      To avoid this problem, you can optionally clamp the far clip to a
      smaller value based on the data you're operating on.
   
   :param region: region of the 3D viewport, typically bpy.context.region.
   :type region: :class:`bpy.types.Region`
   :param rv3d: 3D region data, typically bpy.context.space_data.region_3d.
   :type rv3d: :class:`bpy.types.RegionView3D`
   :param coord: 2D coordinates relative to the region;
      (event.mouse_region_x, event.mouse_region_y) for example.
   :type coord: Sequence[float]
   :param clamp: Clamp the maximum far-clip value used.
      (negative value will move the offset away from the view_location)
   :type clamp: float | None
   :return: The origin of the viewpoint in 3D space.
   :rtype: :class:`mathutils.Vector`

.. function:: region_2d_to_location_3d(region, rv3d, coord, depth_location)

   Return a 3D location from the region relative 2D coords, aligned with
   *depth_location*.
   
   :param region: region of the 3D viewport, typically bpy.context.region.
   :type region: :class:`bpy.types.Region`
   :param rv3d: 3D region data, typically bpy.context.space_data.region_3d.
   :type rv3d: :class:`bpy.types.RegionView3D`
   :param coord: 2D coordinates relative to the region;
      (event.mouse_region_x, event.mouse_region_y) for example.
   :type coord: Sequence[float]
   :param depth_location: the returned vectors depth is aligned with this since
      there is no defined depth with a 2D region input.
   :type depth_location: :class:`mathutils.Vector`
   :return: normalized 3D vector.
   :rtype: :class:`mathutils.Vector`

.. function:: location_3d_to_region_2d(region, rv3d, coord, *, default=None)

   Return the *region* relative 2D location of a 3D position.
   
   :param region: region of the 3D viewport, typically bpy.context.region.
   :type region: :class:`bpy.types.Region`
   :param rv3d: 3D region data, typically bpy.context.space_data.region_3d.
   :type rv3d: :class:`bpy.types.RegionView3D`
   :param coord: 3D world-space location.
   :type coord: :class:`mathutils.Vector`
   :param default: Return this value if ``coord``
      is behind the origin of a perspective view.
   :type default: Any
   :return: 2D location
   :rtype: :class:`mathutils.Vector` | Any

