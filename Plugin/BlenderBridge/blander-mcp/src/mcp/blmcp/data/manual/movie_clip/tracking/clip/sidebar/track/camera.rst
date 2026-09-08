.. _bpy.types.MovieTrackingCamera:

******
Camera
******

This panel contains all settings of the camera used for filming the movie
which is currently being edited in the Clip editor.
Different predefined settings can be used here and can be chosen from the panel header.
But such settings as distortion coefficients and principal point are not included in the presets and
should be filled in even if camera presets are used.

.. _bpy.types.MovieTrackingCamera.sensor_width:

Sensor Width
   Is the width of the CCD sensor in the camera. This value can be found in camera specifications.

.. _bpy.types.MovieTrackingCamera.pixel_aspect:

Pixel Aspect
   Is the pixel aspect of the CCD sensor. This value can be found in camera specifications,
   but can also be guessed. For example, you know that the footage should be 1920×1080,
   but the images themselves are 1280×1080. In this case, the pixel aspect is: 1920 / 1280 = 1.5.


.. _motion_tracking-camera-lens:

Lens
====

.. _bpy.types.MovieTrackingCamera.focal_length:

Focal Length
   The focal length with which the movie was shot.
   It can be set in millimeters or pixels.

.. _bpy.types.MovieTrackingCamera.principal_point:

Optical Center
   Defines the optical center (also known as the *principal point*) of the lens used by the camera.
   In most cases this coincides with the center of the image, but certain lenses may have
   an offset optical center. Refer to the specifications of camera or lens used if needed.

   The values are given in normalized image coordinates.

.. _bpy.types.MovieTrackingCamera.distortion_model:

Lens Distortion
   Mathematical function to convert distorted to undistorted coordinates.

   :Polynomial:
      Polynomial radial distortion. Uses three distortion coefficients: K1, K2, and K3.
   :Division:
      It defines high distortions, which makes this model suitable much better for cameras with fisheye lenses.
      Use two distortion coefficients: K1, K2.
   :Nuke:
      Distortion model used by the Nuke compositor. Use two distortion coefficients K1, K2.
   :Brown:
      Brown-Conrady is one of most advanced mathematical lens distortion models.
      Used to model both radial and tangential distortion. Can use up to four
      radial distortion coefficients: K1 - K4 and up to two tangential distortion coefficients: P1 and P2.

Coefficients
   Coefficients are used to compensate for lens distortion when the movie was shot.
   Currently these values can be tweaked by hand only (there are no calibration tools yet)
   using tools available in Distortion mode. To do this tweak K1 until the solving is the closest to
   the known focal length (but also take grid and annotations into account
   to prevent "impossible" distortion).

   .. _bpy.types.MovieTrackingCamera.k:
   .. _bpy.types.MovieTrackingCamera.division_k:
   .. _bpy.types.MovieTrackingCamera.nuke_k:
   .. _bpy.types.MovieTrackingCamera.brown_k:

   Radial Distortion Coefficients (K1 - K4)
      The coefficients in lens distortion models work independent from each other.
      Positive values will give a barrel distortion while negative values give a pincushion distortion.
      With a mixture of both negative and positive coefficients you can define more complicated
      mustache distortions or other complex distortions, that are less common but not rare.

      .. figure:: /images/movie-clip_tracking_clip_sidebar_track_camera_lens-distortion-k.png

         Example of radial distortion for positive and negative K coefficients.

   .. _bpy.types.MovieTrackingCamera.brown_p:
   .. _bpy.types.MovieTrackingCamera.nuke_p:

   Tangential Distortion Coefficients (P1, P2)
      Works independent and allow to compensate for situations when the sensor is not
      perpendicular to a group of lens. The optical center (also called principal point)
      will be shifted (distorted) from the center of the sensor.
      P1 is used to compensate for sensor rotation in Z (vertical) axes,
      while P2 is for compensating sensor rotation in X (horizontal) axes.
      Such distortions can be found in sources from cameras with a sensor stabilization system.

      .. figure:: /images/movie-clip_tracking_clip_sidebar_track_camera_lens-distortions-p.png

         Example of tangential distortion for P coefficients.
