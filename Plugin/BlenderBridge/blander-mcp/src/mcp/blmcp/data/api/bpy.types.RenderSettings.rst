RenderSettings(bpy_struct)
==========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: RenderSettings(bpy_struct)

   Rendering settings for a Scene data-block

   .. data:: bake

      (readonly, never None)

      :type: :class:`BakeSettings`

   .. attribute:: border_max_x

      Maximum X value for the render region (in [0, 1], default 1.0)

      :type: float

   .. attribute:: border_max_y

      Maximum Y value for the render region (in [0, 1], default 1.0)

      :type: float

   .. attribute:: border_min_x

      Minimum X value for the render region (in [0, 1], default 0.0)

      :type: float

   .. attribute:: border_min_y

      Minimum Y value for the render region (in [0, 1], default 0.0)

      :type: float

   .. attribute:: compositor_denoise_device

      The device to use to process the denoise nodes in the compositor (default ``'AUTO'``)

      - ``AUTO``
        Auto -- Use the same device used by the compositor to process the denoise node.
      - ``CPU``
        CPU -- Use the CPU to process the denoise node.
      - ``GPU``
        GPU -- Use the GPU to process the denoise node if available, otherwise fallback to CPU.

      :type: Literal['AUTO', 'CPU', 'GPU']

   .. attribute:: compositor_denoise_final_quality

      The quality used by denoise nodes during the compositing of final renders if the nodes' quality option is set to Follow Scene (default ``'HIGH'``)

      - ``HIGH``
        High -- High quality.
      - ``BALANCED``
        Balanced -- Balanced between performance and quality.
      - ``FAST``
        Fast -- High performance.

      :type: Literal['HIGH', 'BALANCED', 'FAST']

   .. attribute:: compositor_denoise_preview_quality

      The quality used by denoise nodes during viewport and interactive compositing if the nodes' quality option is set to Follow Scene (default ``'BALANCED'``)

      - ``HIGH``
        High -- High quality.
      - ``BALANCED``
        Balanced -- Balanced between performance and quality.
      - ``FAST``
        Fast -- High performance.

      :type: Literal['HIGH', 'BALANCED', 'FAST']

   .. attribute:: compositor_device

      Set how compositing is executed (default ``'CPU'``)

      :type: Literal['CPU', 'GPU']

   .. attribute:: compositor_precision

      The precision of compositor intermediate result (default ``'AUTO'``)

      - ``AUTO``
        Auto -- Full precision for final renders, half precision otherwise.
      - ``FULL``
        Full -- Full precision.

      :type: Literal['AUTO', 'FULL']

   .. attribute:: dither_intensity

      Amount of dithering noise added to the rendered image to break up banding (in [0, inf], default 1.0)

      :type: float

   .. attribute:: engine

      Engine to use for rendering (default ``'BLENDER_EEVEE'``)

      :type: Literal['BLENDER_EEVEE']

   .. data:: ffmpeg

      FFmpeg related settings for the scene (readonly)

      :type: :class:`FFmpegSettings` | None

   .. data:: file_extension

      The file extension used for saving renders (default "", readonly, never None)

      :type: str

   .. attribute:: filepath

      Directory/name to save animations, # characters define the position and padding of frame numbers (default "", never None, blend relative ``//`` prefix supported, Supports `template expressions <https://docs.blender.org/manual/en/5.1/files/file_paths.html#path-templates>`_)

      :type: str

   .. attribute:: film_transparent

      World background is transparent, for compositing the render over another background (default False)

      :type: bool

   .. attribute:: filter_size

      Width over which the reconstruction filter combines samples (in [0, 500], default 1.5)

      :type: float

   .. attribute:: fps

      Framerate, expressed in frames per second (in [1, 32767], default 24)

      :type: int

   .. attribute:: fps_base

      Framerate base (in [1e-05, 1e+06], default 1.0)

      :type: float

   .. attribute:: frame_map_new

      How many frames the Map Old will last (in [1, 900], default 100)

      :type: int

   .. attribute:: frame_map_old

      Old mapping value in frames (in [1, 900], default 100)

      :type: int

   .. attribute:: hair_subdiv

      Additional subdivision along the curves (in [0, 3], default 0)

      :type: int

   .. attribute:: hair_type

      Curves shape type (default ``'STRAND'``)

      :type: Literal['STRAND', 'STRIP', 'CYLINDER']

   .. data:: has_multiple_engines

      More than one rendering engine is available (default False, readonly)

      :type: bool

   .. data:: image_settings

      (readonly, never None)

      :type: :class:`ImageFormatSettings`

   .. data:: is_movie_format

      When true the format is a movie (default False, readonly)

      :type: bool

   .. attribute:: line_thickness

      Line thickness in pixels (in [0, 10000], default 1.0)

      :type: float

   .. attribute:: line_thickness_mode

      Line thickness mode for Freestyle line drawing (default ``'ABSOLUTE'``)

      - ``ABSOLUTE``
        Absolute -- Specify unit line thickness in pixels.
      - ``RELATIVE``
        Relative -- Unit line thickness is scaled by the proportion of the present vertical image resolution to 480 pixels.

      :type: Literal['ABSOLUTE', 'RELATIVE']

   .. attribute:: metadata_input

      Where to take the metadata from (default ``'SCENE'``)

      - ``SCENE``
        Scene -- Use metadata from the current scene.
      - ``STRIPS``
        Sequencer Strips -- Use metadata from the strips in the sequencer.

      :type: Literal['SCENE', 'STRIPS']

   .. attribute:: motion_blur_position

      Offset for the shutter's time interval, allows to change the motion blur trails (default ``'CENTER'``)

      - ``START``
        Start on Frame -- The shutter opens at the current frame.
      - ``CENTER``
        Center on Frame -- The shutter is open during the current frame.
      - ``END``
        End on Frame -- The shutter closes at the current frame.

      :type: Literal['START', 'CENTER', 'END']

   .. attribute:: motion_blur_shutter

      Time taken in frames between shutter open and close (in [0, inf], default 0.5)

      :type: float

   .. data:: motion_blur_shutter_curve

      Curve defining the shutter's openness over time (readonly)

      :type: :class:`CurveMapping` | None

   .. attribute:: pixel_aspect_x

      Horizontal aspect ratio - for anamorphic or non-square pixel output (in [1, 200], default 1.0)

      :type: float

   .. attribute:: pixel_aspect_y

      Vertical aspect ratio - for anamorphic or non-square pixel output (in [1, 200], default 1.0)

      :type: float

   .. attribute:: ppm_base

      The base unit for pixels per meter. (in [1e-05, 1e+06], default 0.0254)

      :type: float

   .. attribute:: ppm_factor

      The pixel density meta-data written to supported image formats. This value is multiplied by the PPM-base which defines the unit (typically inches or meters) (in [1e-05, 1e+06], default 72.0)

      :type: float

   .. attribute:: preview_pixel_size

      Pixel size for viewport rendering (default ``'AUTO'``)

      - ``AUTO``
        Automatic -- Automatic pixel size, depends on the user interface scale.
      - ``1``
        1× -- Render at full resolution.
      - ``2``
        2× -- Render at 50% resolution.
      - ``4``
        4× -- Render at 25% resolution.
      - ``8``
        8× -- Render at 12.5% resolution.

      :type: Literal['AUTO', '1', '2', '4', '8']

   .. attribute:: resolution_percentage

      Percentage scale for render resolution (in [1, 32767], default 100)

      :type: int

   .. attribute:: resolution_x

      Number of horizontal pixels in the rendered image (in [4, 65536], default 1920)

      :type: int

   .. attribute:: resolution_y

      Number of vertical pixels in the rendered image (in [4, 65536], default 1080)

      :type: int

   .. attribute:: sequencer_gl_preview

      Display method used in the sequencer view (default ``'SOLID'``)

      :type: Literal[:ref:`rna_enum_shading_type_items`]

   .. attribute:: simplify_child_particles

      Global child particles percentage (in [0, 1], default 1.0)

      :type: float

   .. attribute:: simplify_child_particles_render

      Global child particles percentage during rendering (in [0, 1], default 0.0)

      :type: float

   .. attribute:: simplify_gpencil

      Simplify Grease Pencil drawing (default False)

      :type: bool

   .. attribute:: simplify_gpencil_antialiasing

      Use Antialiasing to smooth stroke edges (default True)

      :type: bool

   .. attribute:: simplify_gpencil_modifier

      Display modifiers (default True)

      :type: bool

   .. attribute:: simplify_gpencil_onplay

      Simplify Grease Pencil only during animation playback (default False)

      :type: bool

   .. attribute:: simplify_gpencil_shader_fx

      Display Shader Effects (default True)

      :type: bool

   .. attribute:: simplify_gpencil_tint

      Display layer tint (default True)

      :type: bool

   .. attribute:: simplify_gpencil_view_fill

      Display fill strokes in the viewport (default True)

      :type: bool

   .. attribute:: simplify_subdivision

      Global maximum subdivision level (in [0, 32767], default 6)

      :type: int

   .. attribute:: simplify_subdivision_render

      Global maximum subdivision level during rendering (in [0, 32767], default 0)

      :type: int

   .. attribute:: simplify_volumes

      Resolution percentage of volume objects in viewport (in [0, 1], default 1.0)

      :type: float

   .. attribute:: stamp_background

      Color to use behind stamp text (array of 4 items, in [0, 1], default (0.0, 0.0, 0.0, 0.25))

      :type: :class:`bpy_prop_array`\ [float]

   .. attribute:: stamp_font_size

      Size of the font used when rendering stamp text (in [8, 64], default 12)

      :type: int

   .. attribute:: stamp_foreground

      Color to use for stamp text (array of 4 items, in [0, 1], default (0.8, 0.8, 0.8, 1.0))

      :type: :class:`bpy_prop_array`\ [float]

   .. attribute:: stamp_note_text

      Custom text to appear in the stamp note (default "", never None)

      :type: str

   .. data:: stereo_views

      (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`SceneRenderView`]

   .. attribute:: threads

      Maximum number of CPU cores to use simultaneously while rendering (for multi-core/CPU systems) (in [1, 1024], default 1)

      :type: int

   .. attribute:: threads_mode

      Determine the amount of render threads used (default ``'AUTO'``)

      - ``AUTO``
        Auto-Detect -- Automatically determine the number of threads, based on CPUs.
      - ``FIXED``
        Fixed -- Manually determine the number of threads.

      :type: Literal['AUTO', 'FIXED']

   .. attribute:: use_border

      Render a user-defined render region, within the frame size (default False)

      :type: bool

   .. attribute:: use_compositing

      Process the render result through the compositing pipeline, if a compositing node group is assigned to the scene (default True)

      :type: bool

   .. attribute:: use_crop_to_border

      Crop the rendered frame to the defined render region size (default False)

      :type: bool

   .. attribute:: use_file_extension

      Add the file format extensions to the rendered file name (eg: filename + .jpg) (default True)

      :type: bool

   .. attribute:: use_freestyle

      Draw stylized strokes using Freestyle (default False)

      :type: bool

   .. attribute:: use_high_quality_normals

      Use high quality tangent space at the cost of lower performance (default False)

      :type: bool

   .. attribute:: use_lock_interface

      Lock interface during rendering in favor of giving more memory to the renderer (default False)

      :type: bool

   .. attribute:: use_motion_blur

      Use multi-sampled 3D scene motion blur (default False)

      :type: bool

   .. attribute:: use_multiview

      Use multiple views in the scene (default False)

      :type: bool

   .. attribute:: use_overwrite

      Overwrite existing files while rendering (default True)

      :type: bool

   .. attribute:: use_persistent_data

      Keep render data around for faster re-renders and animation renders, at the cost of increased memory usage (default False)

      :type: bool

   .. attribute:: use_placeholder

      Create empty placeholder files while rendering frames (similar to Unix 'touch') (default False)

      :type: bool

   .. attribute:: use_render_cache

      Save render cache to EXR files (useful for heavy compositing, Note: affects indirectly rendered scenes) (default False)

      :type: bool

   .. attribute:: use_sequencer

      Process the render (and composited) result through the video sequence editor pipeline, if sequencer strips exist (default True)

      :type: bool

   .. attribute:: use_sequencer_override_scene_strip

      Use workbench render settings from the sequencer scene, instead of each individual scene used in the strip (default False)

      :type: bool

   .. attribute:: use_simplify

      Enable simplification of scene for quicker preview renders (default False)

      :type: bool

   .. attribute:: use_simplify_normals

      Skip computing custom normals and face corner normals for displaying meshes in the viewport (default False)

      :type: bool

   .. attribute:: use_single_layer

      Only render the active layer. Only affects rendering from the interface, ignored for rendering from command line. (default False)

      :type: bool

   .. data:: use_spherical_stereo

      Active render engine supports spherical stereo rendering (default False, readonly)

      :type: bool

   .. attribute:: use_stamp

      Render the stamp info text in the rendered image (default False)

      :type: bool

   .. attribute:: use_stamp_camera

      Include the name of the active camera in image metadata (default True)

      :type: bool

   .. attribute:: use_stamp_date

      Include the current date in image/video metadata (default True)

      :type: bool

   .. attribute:: use_stamp_filename

      Include the .blend filename in image/video metadata (default True)

      :type: bool

   .. attribute:: use_stamp_frame

      Include the frame number in image metadata (default True)

      :type: bool

   .. attribute:: use_stamp_frame_range

      Include the rendered frame range in image/video metadata (default False)

      :type: bool

   .. attribute:: use_stamp_hostname

      Include the hostname of the machine that rendered the frame (default False)

      :type: bool

   .. attribute:: use_stamp_labels

      Display stamp labels ("Camera" in front of camera name, etc.) (default True)

      :type: bool

   .. attribute:: use_stamp_lens

      Include the active camera's lens in image metadata (default False)

      :type: bool

   .. attribute:: use_stamp_marker

      Include the name of the last marker in image metadata (default False)

      :type: bool

   .. attribute:: use_stamp_memory

      Include the peak memory usage in image metadata (default True)

      :type: bool

   .. attribute:: use_stamp_note

      Include a custom note in image/video metadata (default False)

      :type: bool

   .. attribute:: use_stamp_render_time

      Include the render time in image metadata (default True)

      :type: bool

   .. attribute:: use_stamp_scene

      Include the name of the active scene in image/video metadata (default True)

      :type: bool

   .. attribute:: use_stamp_sequencer_strip

      Include the name of the foreground sequence strip in image metadata (default False)

      :type: bool

   .. attribute:: use_stamp_time

      Include the rendered frame timecode as HH:MM:SS.FF in image metadata (default True)

      :type: bool

   .. data:: views

      (default None, readonly)

      :type: :class:`RenderViews`\ [:class:`SceneRenderView`]

   .. attribute:: views_format

      (default ``'STEREO_3D'``)

      - ``STEREO_3D``
        Stereo 3D -- Single stereo camera system, adjust the stereo settings in the camera panel.
      - ``MULTIVIEW``
        Multi-View -- Multi camera system, adjust the cameras individually.

      :type: Literal['STEREO_3D', 'MULTIVIEW']

   .. method:: frame_path(*, frame=-2147483648, preview=False, view="")

      Return the absolute path to the filename to be written for a given frame

      :param frame: Frame number to use, if unset the current frame will be used (in [-inf, inf], optional)
      :type frame: int
      :param preview: Preview, Use preview range (optional)
      :type preview: bool
      :param view: View, The name of the view to use to replace the "%" chars (optional, never None)
      :type view: str
      :return: File Path, The resulting filepath from the scenes render settings (never None)
      :rtype: str

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

References
----------

.. hlist::
   :columns: 2

   - :class:`RenderEngine.render`
   - :class:`Scene.render`

