.. _bpy.types.Camera:
.. _bpy.ops.camera:

*******
Cameras
*******

A camera is an object that provides a means of rendering images from Blender.
It defines which portion of a scene is visible in the rendered image.

Cameras are invisible in renders, so they do not have any material or texture settings.
However, they do have *Object* and *Editing* setting panels available which are displayed
when a camera is the active object.

.. seealso::

   :doc:`3D Viewport Camera Navigation </editors/3dview/navigate/camera_view>`
   for documentation about managing cameras in the viewport.


Properties
==========

.. reference::

   :Mode:      Object Mode
   :Editor:    :menuselection:`Properties --> Camera`


.. _camera-lens-type:

Lens
----

.. rubric:: Type

The camera lens options control the way 3D objects are represented in a 2D image.

Perspective
   This matches how you view things in the real world.
   Objects in the distance will appear smaller than objects in the foreground,
   and parallel lines (such as the rails on a railroad) will appear to converge as they get farther away.

   Focal Length/Field of View
      The :term:`Focal Length` controls the amount of zoom, i.e.
      the amount of the scene which is visible all at once.
      Longer focal lengths result in a smaller :abbr:`FOV (Field of View)` (more zoom),
      while short focal lengths allow you to see more of the scene at once
      (larger :abbr:`FOV (Field of View)`, less zoom).

      .. list-table::

         * - .. figure:: /images/render_cameras_traintracks-perspective-BI.jpg

                Perspective camera with 35 mm focal length.

           - .. figure:: /images/render_cameras_traintracks-perspective-telephoto-BI.jpg

                Perspective camera with 210 mm focal length instead of 35 mm.

      Lens Unit
         The focal length can be set either in terms of millimeters or the actual :term:`Field of View` as an angle.

         .. figure:: /images/render_cameras_perspective.svg
            :align: center
            :width: 50%

      .. hint::

         While the camera is moving towards an object the *Focal Length* property can be decreased
         to produce a *Dolly Zoom* camera effect, or vice versa.

         `This video <https://vimeo.com/15837189>`__ demonstrates the *Dolly Zoom* camera effect.

Orthographic
   With *Orthographic* perspective objects always appear at their actual size, regardless of distance.
   This means that parallel lines appear parallel, and do not converge like they do with *Perspective*.

   .. figure:: /images/render_cameras_traintracks-orthographic-BI.jpg
      :width: 50%

      Render from the same camera angle as the previous examples, but with orthographic perspective.

   Orthographic Scale
      This controls the apparent size of objects projected on the image.

      Note that this is effectively the only setting which applies to orthographic perspective.
      Since parallel lines do not converge in orthographic mode (no vanishing points),
      the lens shift settings are equivalent to translating the camera in the 3D Viewport.

      .. figure:: /images/render_cameras_orthographic.svg
         :align: center
         :width: 50%

Panoramic
   :guilabel:`Cycles Only`

   This type covers a variety of panoramic projections.
   See the Cycles :ref:`panoramic camera <bpy.types.Camera.panorama_type>` settings for more information.

Custom
   :guilabel:`Cycles Only`

   Custom cameras enable user-defined behavior through the use of OSL code.
   See the :doc:`Cycles custom camera documentation </render/cycles/osl/camera>` for more information.

Shift
   Allows for the adjustment of *vanishing points*.
   *Vanishing points* refer to the positions to which parallel lines converge.
   In these render examples, the most obvious vanishing point is at the end of the railroad.

   .. list-table::

      * - .. figure:: /images/render_cameras_traintracks-perspective-lens-shift-BI.jpg

             Horizontal lens shift of 0.330.

        - .. figure:: /images/render_cameras_traintracks-perspective-rotate-BI.jpg

             Rotation of the camera object instead of a lens shift.

   Notice how the horizontal lines remain perfectly horizontal when using the lens shift,
   but do get skewed when rotating the camera object.

   .. note::

      Using lens shift is equivalent to rendering an image with a larger
      :abbr:`FOV (Field of View)` and cropping it off-center.

.. _camera-clipping:

Clip Start and End
   The interval in which objects are directly visible.
   Any objects outside this range still influence the image indirectly,
   as further light bounces are not clipped.

   .. note::

      For viewport rendering, setting clipping distances to limited values
      is important to ensure sufficient rasterization precision.
      Ray tracing renders do not suffer from this issue so much,
      and as such more extreme values can safely be set.

   .. tip::

      When *Limits* in the *Viewport Display* panel is enabled,
      the clip bounds will be visible as two yellow connected dots on the camera's line of sight.

   .. seealso::

      - :doc:`3D Viewport clipping </editors/3dview/sidebar>`


.. _bpy.types.CameraDOFSettings:

Depth of Field
--------------

Real-world cameras transmit light through a lens that bends and focuses it onto the sensor.
Because of this, objects that are a certain distance away are in focus,
but objects in front and behind that are blurred.

.. figure:: /images/render_cameras_dof-bokeh.jpg
   :align: center
   :width: 50%

   Example of DOF bokeh effect.

The area in focus is called the *focal point* and can be set using either an exact value,
or by using the distance between the camera and a chosen object:

Focus Object
   Choose an object which will determine the focal point. Linking an object will deactivate the distance parameter.
Focal Distance
   Sets the distance to the focal point when no *Focus Object* is specified.
   This distance can be visualized in the 3D Viewport by enabling *Limits* in the camera's
   :ref:`Viewport Display <bpy.types.Camera.show>` panel.

   .. hint::

      Use the eyedropper icon or hover the mouse over the *Focal Distance* property
      and press :kbd:`E` to enable the depth *Depth Picker*.
      Then :kbd:`LMB` on a point in the 3D Viewport to sample the distance from that point to the camera.


Aperture
^^^^^^^^

F-Stop
   F-Stop ratio that defines the amount of blurring.
   Lower values give a strong depth of field effect.
Blades
   Total number of polygonal blades used to alter the shape of the blurred objects
   in the render, and render preview. As with the viewport, the minimum amount of
   blades to enable the bokeh effect is 3, resulting in a triangular-shaped blur.
Rotation
   Rotate the polygonal blades along the facing axis, and will rotate in a clockwise,
   and counter-clockwise fashion.
Ratio
   Change the amount of distortion to simulate the anamorphic bokeh effect.
   A setting of 1.0 shows no distortion, where a number below 1.0 will cause a horizontal distortion,
   and a higher number will cause a vertical distortion.


Camera
------

These settings adjusts properties that relate to a physical camera body.
Several :ref:`Presets <ui-presets>` can be chosen to match real-world cameras.

.. _bpy.types.Camera.sensor_fit:

Sensor Fit
   Adjusts how the camera's sensor fits within the outputs dimension adjusting the angular field of view.

   :Auto:
      Calculates a square sensor size based on the larger of
      the :ref:`Resolution <bpy.types.RenderSettings.resolution_y>` dimensions.
   :Horizontal:
      Manually adjust the *Width* of the sensor, the *Height* is calculated based on
      the aspect ratio of the output's :ref:`Resolution <bpy.types.RenderSettings.resolution_y>`.
   :Vertical:
      Manually adjust the *Height* of the sensor, the *Width* is calculated based on
      the aspect ratio of the output's :ref:`Resolution <bpy.types.RenderSettings.resolution_y>`.

.. _bpy.types.Camera.sensor_height:
.. _bpy.types.Camera.sensor_width:

Size / Width, Height
   This setting is an alternative way to control the field of view, as opposed to modifying the focal length.
   It is useful to match a camera in Blender to a physical camera and lens combination,
   e.g. for :doc:`motion tracking </movie_clip/index>`.


.. _bpy.ops.camera.safe_areas:
.. _bpy.types.DisplaySafeAreas:

Safe Areas
----------

Safe areas are guides used to position elements to ensure that
the most important parts of the content can be seen across all screens.

Different screens have varying amounts of :term:`Overscan` (especially older TV sets).
That means that not all content will be visible to all viewers,
since parts of the image surrounding the edges are not shown.
To work around this problem TV producers defined two areas where content is guaranteed to be shown:
action safe and title safe.

Modern LCD/plasma screens with purely digital signals have no :term:`Overscan`,
yet safe areas are still considered best practice and may be legally required for broadcast.

In Blender, safe areas can be set from the Camera and Sequencer views.

.. figure:: /images/render_cameras_safe-areas-main-BI.png
   :align: center
   :width: 50%

   Red line: Action safe. Green line: Title safe.

The Safe Areas can be customized by their outer margin,
which is a percentage scale of the area between the center and the render size.
Values are shared between the Video Sequence editor and camera view.

Title Safe Margins X/Y
   Also known as *Graphics Safe*.
   Place all important information (graphics or text) inside this area to
   ensure it can be seen by the majority of viewers.
Action Safe Margins X/Y
   Make sure any significant action or characters in the shot are inside this area.
   This zone also doubles as a sort of "margin" for the screen which can be used
   to keep elements from piling up against the edges.

.. tip::

   Each country sets a legal standard for broadcasting.
   These include, among other things, specific values for safe areas.
   Blender defaults for safe areas follow the EBU (European Union) standard.
   Make sure you are using the correct values when working for broadcast to avoid any trouble.


Center-Cut Safe Areas
^^^^^^^^^^^^^^^^^^^^^

Center-cuts are a second set of safe areas to ensure content
is seen correctly on screens with a different aspect ratio.
Old TV sets receiving ``16:9`` or ``21:9`` video will cut off the sides.
Position content inside the center-cut areas to make sure the most important elements
of your composition can still be visible in these screens.

Blender defaults show a ``4:3`` (square) ratio inside ``16:9`` (widescreen).

.. figure:: /images/render_cameras_safe-areas-cuts-BI.png
   :align: center
   :width: 50%

   Cyan line: action center safe. Blue line: title center safe.


.. _bpy.types.CameraBackgroundImage:

Background Images
-----------------

A background picture in your camera can be very helpful in many situations:
modeling is obviously one, but it is also useful when painting
(e.g. you can have reference pictures of faces when painting textures directly on your model...),
or animation (when using a video as background), etc.

Background Source
   The source of the background image.

   :Image:
      Use an external image, image sequence, video file or generated texture.
   :Movie Clip:
      Use one of the Movie Clip data-blocks.

      Active Clip
         Display a Movie Clip from the scene's :ref:`Active Clip <bpy.types.Scene.active_clip>`.
      Render Undistorted
         Display the background image using undistorted proxies when available.
      Proxy Render Size
         Select between full (non-proxy) display or a proxy size to draw the background image.

         .. seealso::

            To build a proxy, the :ref:`Movie Clip Editor Proxy settings <bpy.types.MovieClipProxy>` have to be used.
            Otherwise the proxy settings here have no effect.

Color Space
   The color space the image or video file uses within Blender.

View as Render
   Apply the :ref:`color management <render-post-color-management>` settings when displaying this image on the screen.

Opacity
   Controls the transparency of the background image.

Depth
   Choose whether the image is shown behind all objects, or in front of everything.

Frame Method
   Controls how the image is placed in the camera view.

   :Stretch: Forces the image dimensions to match the camera bounds (may alter the aspect ratio).
   :Fit: Scales the image down to fit inside the camera view without altering the aspect ratio.
   :Crop:
      Scales the image up so that it fills the entire camera view,
      but without altering the aspect ratio (some of the image will be cropped).

Offset X, Y
   Positions the background image using these offsets.

   In orthographic views, this is measured in the normal scene units.
   In the camera view, this is measured relative to the camera bounds
   (0.1 will offset it by 10% of the view width/height).

Rotation
   Rotates the image around its center.

Scale
   Scales the image up or down from its center.

Flip
   X
      Swaps the image around, such that the left side is now on the right, and the right now on the left.
   Y
      Swaps the image around, such that the top side is now on the bottom, and the bottom now on the top.

.. note::

   Movie Clips or images with view as render are only visible behind objects
   when :ref:`film transparency <bpy.types.RenderSettings.film_transparent>`
   is enabled or the :ref:`scene world <bpy.types.View3DShading.use_scene_world>`
   is disabled in the viewport.

.. _bpy.types.Camera.show:
.. _bpy.types.Camera.display_size:

Viewport Display
----------------

.. figure:: /images/render_cameras_display-view-BI.png
   :align: center
   :width: 50%

   Camera view displaying safe areas, sensor and name.

Size
   Size of the camera visualization in the 3D Viewport. This setting has **no** effect on
   the render output of a camera. The camera visualization can also be scaled using
   the standard Scale :kbd:`S` transform key.

Show
   Limits
      Shows an orange line indicating the *Clip Start* and *End* values,
      as well as a yellow cross indicating the *Focus Distance*.
      If the *Focus Distance* gizmo is enabled in the 3D Viewport's
      :doc:`gizmo settings </editors/3dview/display/gizmo>`,
      this cross can also be dragged with the mouse to adjust the distance.
   Mist
      Toggles viewing of the mist limits on and off.
      The limits are shown as two connected white dots on the camera line of sight.
      The mist limits and other options are set in the *World* panel,
      in the :ref:`Mist section <bpy.types.WorldMistSettings>`.
   Sensor
      Displays a dotted frame in camera view.
   Name
      Toggle name display on and off in camera view.

.. _bpy.types.Camera.show_passepartout:
.. _bpy.types.Camera.passepartout_alpha:

Passepartout
   This option darkens the area outside of the camera's field of view.
   The opacity of the passepartout can be adjusted using the value slider.

   .. tip::

      If the Passepartout is fully opaque, Blender will make optimizations
      to speed up the rendering of areas inside the camera view.


.. _bpy.types.Camera.show_composition:

Composition Guides
^^^^^^^^^^^^^^^^^^

*Composition Guides* enable overlays onto the camera display that can help when framing a shot.

Thirds
   Adds lines dividing the frame in thirds vertically and horizontally.

Center
   Center
      Adds lines dividing the frame in half vertically and horizontally.
   Diagonal
      Adds lines connecting opposite corners.

Golden
   Ratio
      Divides the width and height into Golden proportions (about 0.618 of the size from all sides of the frame).
   Triangle A
      Displays a diagonal line from the lower left to upper right corners,
      then adds perpendicular lines that pass through the top left and bottom right corners.
   Triangle B
      Same as A, but with the opposite corners.

Harmony
   Triangle A
      Displays a diagonal line from the lower left to upper right corners,
      then lines from the top left and bottom right corners to 0.618 the lengths of the opposite side.
   Triangle B
      Same as A, but with the opposite corners.

.. _bpy.types.Camera.composition_guide_color:

Color
   Sets the display color and opacity (alpha) used for all composition guide overlays.
   Useful for adjusting visibility depending on the brightness or contrast of the underlying shot.
