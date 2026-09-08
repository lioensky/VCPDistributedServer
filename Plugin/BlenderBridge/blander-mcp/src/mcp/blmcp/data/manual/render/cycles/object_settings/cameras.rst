
*******
Cameras
*******

.. _bpy.types.Camera.panorama_type:

Panoramic Cameras
=================

Cycles supports several types of panoramic cameras which are described in detail below.
Note that these cannot be displayed in non-rendered modes in the viewport,
i.e. *Solid* mode; they will only work for the final render.


Equirectangular
---------------

Render a panoramic view of the scenes from the camera location and use an equirectangular projection,
always rendering the full 360° over the X axis and 180° over the Y axis.

This projection is compatible with the environment texture as used for world shaders,
so it can be used to render an environment map. To match the default mapping,
set the camera object rotation to (90, 0, -90) or pointing along the positive X axis.
This corresponds to looking at the center of the image using the default environment texture mapping.

.. _bpy.types.Camera.latitude:

Latitude Min, Max
   Limits of the vertical field of view angles.

.. _bpy.types.Camera.longitude:

Longitude Min, Max
   Limits of the horizontal field of view angles.


Equiangular Cubemap Face
------------------------

Improves on *Equirectangular* by providing a more uniform distribution of rendered pixel of the spherical environment.
This results in an image that has little variation in visual resolution for the entire spherical projection.
This is in contrast to *Equirectangular* which can lose detail in the poles of the image.
This is also in contrast to cube map projections which lose detail near the edges of each face.

This panorama type is great for virtual reality use cases
where providing as much visual detail for a limited resolution is important.

A limitation over *Equirectangular* is that this method does not have longitude or latitude limits.


Fisheye
-------

Fisheye lenses are typically wide angle lenses with strong distortion,
useful for creating panoramic images for e.g. dome projection, or as an artistic effect.

The *Fisheye Equisolid* lens will best match real cameras.
It provides a lens focal length and field of view angle,
and will also take the sensor dimensions into account.

The *Fisheye Equidistant* lens does not correspond to any real lens model;
it will give a circular fisheye that does not take any sensor information into account
but rather uses the whole sensor. This is a good lens for full-dome projections.

.. _bpy.types.Camera.fisheye_lens:

Lens
   Lens focal length in millimeters.

.. _bpy.types.Camera.fisheye_fov:

Field of View
   Field of view angle, going to 360 and more to capture the whole environment.


Fisheye Lens Polynomial
-----------------------

Match a real world camera by specifying the coordinates of a 4th degree polynomial.

The projection works as follows.
Pixels in the image are mapped to positions :math:`(x, y)` on the camera sensor in mm.
A position on the sensor is mapped to a direction with spherical coordinates
:math:`(1, \theta, \phi)` in radians as follows:

.. math::

  & r = \sqrt{x^2 + y^2}\\
  & \theta = k_0 + k_1 r + k_2 r^2 + k_3 r^3 + k_4 r^4\\
  & \phi = acos(x/r)

Incoming light from this direction is then projected onto the corresponding pixel.

This can be used to model both fisheye and perspective cameras.


Mirror Ball
-----------

Render as if taking a photo of a reflective mirror ball.
This can be useful in rare cases to compare with a similar photo taken to capture an environment.
