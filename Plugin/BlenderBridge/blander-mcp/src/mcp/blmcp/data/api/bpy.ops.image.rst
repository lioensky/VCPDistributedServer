Image Operators
===============

.. module:: bpy.ops.image

.. function:: add_render_slot()

   Add a new render slot

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: change_frame(*, frame=0)

   Interactively change the current frame number

   :param frame: Frame, (in [-1048574, 1048574], optional)
   :type frame: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: clear_render_border()

   Clear the boundaries of the render region and disable render region

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: clear_render_slot()

   Clear the currently selected render slot

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: clipboard_copy()

   Copy the image to the clipboard

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: clipboard_paste()

   Paste new image from the clipboard

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: convert_to_mesh_plane(*, interpolation='Linear', extension='CLIP', use_auto_refresh=True, relative=True, shader='PRINCIPLED', emit_strength=1.0, use_transparency=True, render_method='DITHERED', use_backface_culling=False, show_transparent_back=True, overwrite_material=True, name_from='OBJECT', delete_ref=True)

   Convert selected reference images to textured mesh plane

   :param interpolation: Interpolation, Texture interpolation (optional)

      - ``Linear``
        Linear -- Linear interpolation.
      - ``Closest``
        Closest -- No interpolation (sample closest texel).
      - ``Cubic``
        Cubic -- Cubic interpolation.
      - ``Smart``
        Smart -- Bicubic when magnifying, else bilinear (OSL only).
   :type interpolation: Literal['Linear', 'Closest', 'Cubic', 'Smart']
   :param extension: Extension, How the image is extrapolated past its original bounds (optional)

      - ``CLIP``
        Clip -- Clip to image size and set exterior pixels as transparent.
      - ``EXTEND``
        Extend -- Extend by repeating edge pixels of the image.
      - ``REPEAT``
        Repeat -- Cause the image to repeat horizontally and vertically.
   :type extension: Literal['CLIP', 'EXTEND', 'REPEAT']
   :param use_auto_refresh: Auto Refresh, Always refresh image on frame changes (optional)
   :type use_auto_refresh: bool
   :param relative: Relative Paths, Use relative file paths (optional)
   :type relative: bool
   :param shader: Shader, Node shader to use (optional)

      - ``PRINCIPLED``
        Principled -- Principled shader.
      - ``SHADELESS``
        Shadeless -- Only visible to camera and reflections.
      - ``EMISSION``
        Emission -- Emission shader.
   :type shader: Literal['PRINCIPLED', 'SHADELESS', 'EMISSION']
   :param emit_strength: Emission Strength, Strength of emission (in [0, inf], optional)
   :type emit_strength: float
   :param use_transparency: Use Alpha, Use alpha channel for transparency (optional)
   :type use_transparency: bool
   :param render_method: Render Method, (optional)

      - ``DITHERED``
        Dithered -- Allows for grayscale hashed transparency, and compatible with render passes and ray-tracing. Also known as deferred rendering..
      - ``BLENDED``
        Blended -- Allows for colored transparency, but incompatible with render passes and ray-tracing. Also known as forward rendering..
   :type render_method: Literal['DITHERED', 'BLENDED']
   :param use_backface_culling: Backface Culling, Use backface culling to hide the back side of faces (optional)
   :type use_backface_culling: bool
   :param show_transparent_back: Show Backface, Render multiple transparent layers (may introduce transparency sorting problems) (optional)
   :type show_transparent_back: bool
   :param overwrite_material: Overwrite Material, Overwrite existing material with the same name (optional)
   :type overwrite_material: bool
   :param name_from: Name After, Name for new mesh object and material (optional)

      - ``OBJECT``
        Source Object -- Name after object source with a suffix.
      - ``IMAGE``
        Source Image -- Name from loaded image.
   :type name_from: Literal['OBJECT', 'IMAGE']
   :param delete_ref: Delete Reference Object, Delete empty image object once mesh plane is created (optional)
   :type delete_ref: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/image_as_planes.py\:1133 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/image_as_planes.py#L1133>`__


.. function:: curves_point_set(*, point='BLACK_POINT', size=1)

   Set black point or white point for curves

   :param point: Point, Set black point or white point for curves (optional)
   :type point: Literal['BLACK_POINT', 'WHITE_POINT']
   :param size: Sample Size, (in [1, 128], optional)
   :type size: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: cycle_render_slot(*, reverse=False)

   Cycle through all non-void render slots

   :param reverse: Cycle in Reverse, (optional)
   :type reverse: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: external_edit(*, filepath="")

   Edit image in an external application

   :param filepath: filepath, (optional, never None)
   :type filepath: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/image.py\:54 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/image.py#L54>`__


.. function:: file_browse(*, filepath="", hide_props_region=True, check_existing=False, filter_blender=False, filter_backup=False, filter_image=True, filter_movie=True, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='')

   Open an image file browser, hold Shift to open the file, Alt to browse containing directory

   :param filepath: File Path, Path to file (optional, never None)
   :type filepath: str
   :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings (optional)
   :type hide_props_region: bool
   :param check_existing: Check Existing, Check and warn on overwriting existing files (optional)
   :type check_existing: bool
   :param filter_blender: Filter .blend files, (optional)
   :type filter_blender: bool
   :param filter_backup: Filter backup .blend files, (optional)
   :type filter_backup: bool
   :param filter_image: Filter image files, (optional)
   :type filter_image: bool
   :param filter_movie: Filter movie files, (optional)
   :type filter_movie: bool
   :param filter_python: Filter Python files, (optional)
   :type filter_python: bool
   :param filter_font: Filter font files, (optional)
   :type filter_font: bool
   :param filter_sound: Filter sound files, (optional)
   :type filter_sound: bool
   :param filter_text: Filter text files, (optional)
   :type filter_text: bool
   :param filter_archive: Filter archive files, (optional)
   :type filter_archive: bool
   :param filter_btx: Filter btx files, (optional)
   :type filter_btx: bool
   :param filter_alembic: Filter Alembic files, (optional)
   :type filter_alembic: bool
   :param filter_usd: Filter USD files, (optional)
   :type filter_usd: bool
   :param filter_obj: Filter OBJ files, (optional)
   :type filter_obj: bool
   :param filter_volume: Filter OpenVDB volume files, (optional)
   :type filter_volume: bool
   :param filter_folder: Filter folders, (optional)
   :type filter_folder: bool
   :param filter_blenlib: Filter Blender IDs, (optional)
   :type filter_blenlib: bool
   :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file (in [1, 9], optional)
   :type filemode: int
   :param relative_path: Relative Path, Select the file relative to the blend file (optional)
   :type relative_path: bool
   :param show_multiview: Enable Multi-View, (optional)
   :type show_multiview: bool
   :param use_multiview: Use Multi-View, (optional)
   :type use_multiview: bool
   :param display_type: Display Type, (optional)

      - ``DEFAULT``
        Default -- Automatically determine display type for files.
      - ``LIST_VERTICAL``
        Short List -- Display files as short list.
      - ``LIST_HORIZONTAL``
        Long List -- Display files as a detailed list.
      - ``THUMBNAIL``
        Thumbnails -- Display files as thumbnails.
   :type display_type: Literal['DEFAULT', 'LIST_VERTICAL', 'LIST_HORIZONTAL', 'THUMBNAIL']
   :param sort_method: File sorting mode, (optional)
   :type sort_method: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: flip(*, use_flip_x=False, use_flip_y=False)

   Flip the image

   :param use_flip_x: Horizontal, Flip the image horizontally (optional)
   :type use_flip_x: bool
   :param use_flip_y: Vertical, Flip the image vertically (optional)
   :type use_flip_y: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: import_as_mesh_planes(*, interpolation='Linear', extension='CLIP', use_auto_refresh=True, relative=True, shader='PRINCIPLED', emit_strength=1.0, use_transparency=True, render_method='DITHERED', use_backface_culling=False, show_transparent_back=True, overwrite_material=True, filepath="", align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), files=None, directory="", filter_image=True, filter_movie=True, filter_folder=True, force_reload=False, image_sequence=False, offset=True, offset_axis='+X', offset_amount=0.1, align_axis='CAM_AX', prev_align_axis='NONE', align_track=False, size_mode='ABSOLUTE', fill_mode='FILL', height=1.0, factor=600.0)

   Create mesh plane(s) from image files with the appropriate aspect ratio

   :param interpolation: Interpolation, Texture interpolation (optional)

      - ``Linear``
        Linear -- Linear interpolation.
      - ``Closest``
        Closest -- No interpolation (sample closest texel).
      - ``Cubic``
        Cubic -- Cubic interpolation.
      - ``Smart``
        Smart -- Bicubic when magnifying, else bilinear (OSL only).
   :type interpolation: Literal['Linear', 'Closest', 'Cubic', 'Smart']
   :param extension: Extension, How the image is extrapolated past its original bounds (optional)

      - ``CLIP``
        Clip -- Clip to image size and set exterior pixels as transparent.
      - ``EXTEND``
        Extend -- Extend by repeating edge pixels of the image.
      - ``REPEAT``
        Repeat -- Cause the image to repeat horizontally and vertically.
   :type extension: Literal['CLIP', 'EXTEND', 'REPEAT']
   :param use_auto_refresh: Auto Refresh, Always refresh image on frame changes (optional)
   :type use_auto_refresh: bool
   :param relative: Relative Paths, Use relative file paths (optional)
   :type relative: bool
   :param shader: Shader, Node shader to use (optional)

      - ``PRINCIPLED``
        Principled -- Principled shader.
      - ``SHADELESS``
        Shadeless -- Only visible to camera and reflections.
      - ``EMISSION``
        Emission -- Emission shader.
   :type shader: Literal['PRINCIPLED', 'SHADELESS', 'EMISSION']
   :param emit_strength: Emission Strength, Strength of emission (in [0, inf], optional)
   :type emit_strength: float
   :param use_transparency: Use Alpha, Use alpha channel for transparency (optional)
   :type use_transparency: bool
   :param render_method: Render Method, (optional)

      - ``DITHERED``
        Dithered -- Allows for grayscale hashed transparency, and compatible with render passes and ray-tracing. Also known as deferred rendering..
      - ``BLENDED``
        Blended -- Allows for colored transparency, but incompatible with render passes and ray-tracing. Also known as forward rendering..
   :type render_method: Literal['DITHERED', 'BLENDED']
   :param use_backface_culling: Backface Culling, Use backface culling to hide the back side of faces (optional)
   :type use_backface_culling: bool
   :param show_transparent_back: Show Backface, Render multiple transparent layers (may introduce transparency sorting problems) (optional)
   :type show_transparent_back: bool
   :param overwrite_material: Overwrite Material, Overwrite existing material with the same name (optional)
   :type overwrite_material: bool
   :param filepath: File Path, Filepath used for importing the file (optional, never None)
   :type filepath: str
   :param align: Align, (optional)

      - ``WORLD``
        World -- Align the new object to the world.
      - ``VIEW``
        View -- Align the new object to the view.
      - ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: Literal['WORLD', 'VIEW', 'CURSOR']
   :param location: Location, (array of 3 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :param rotation: Rotation, (array of 3 items, in [-inf, inf], optional)
   :type rotation: :class:`mathutils.Euler` | Sequence[float]
   :param files: files, (optional)
   :type files: :class:`bpy_prop_collection`\ [:class:`OperatorFileListElement`] | None
   :param directory: directory, (optional, never None)
   :type directory: str
   :param filter_image: filter_image, (optional)
   :type filter_image: bool
   :param filter_movie: filter_movie, (optional)
   :type filter_movie: bool
   :param filter_folder: filter_folder, (optional)
   :type filter_folder: bool
   :param force_reload: Force Reload, Force reload the image if it is already opened elsewhere in Blender (optional)
   :type force_reload: bool
   :param image_sequence: Detect Image Sequences, Import sequentially numbered images as an animated image sequence instead of separate planes (optional)
   :type image_sequence: bool
   :param offset: Offset Planes, Offset planes from each other. If disabled, multiple planes will be created at the same location (optional)
   :type offset: bool
   :param offset_axis: Offset Direction, How planes are oriented relative to each others' local axis (optional)

      - ``+X``
        +X -- Side by Side to the Left.
      - ``+Y``
        +Y -- Side by Side, Downward.
      - ``+Z``
        +Z -- Stacked Above.
      - ``-X``
        -X -- Side by Side to the Right.
      - ``-Y``
        -Y -- Side by Side, Upward.
      - ``-Z``
        -Z -- Stacked Below.
   :type offset_axis: Literal['+X', '+Y', '+Z', '-X', '-Y', '-Z']
   :param offset_amount: Offset Distance, Set distance between each plane (in [-inf, inf], optional)
   :type offset_amount: float
   :param align_axis: Align, How to align the planes (optional)

      - ``+X``
        +X -- Facing positive X.
      - ``+Y``
        +Y -- Facing positive Y.
      - ``+Z``
        +Z -- Facing positive Z.
      - ``-X``
        -X -- Facing negative X.
      - ``-Y``
        -Y -- Facing negative Y.
      - ``-Z``
        -Z -- Facing negative Z.
      - ``CAM``
        Face Camera -- Facing camera.
      - ``CAM_AX``
        Camera's Main Axis -- Facing the camera's dominant axis.
   :type align_axis: Literal['+X', '+Y', '+Z', '-X', '-Y', '-Z', 'CAM', 'CAM_AX']
   :param prev_align_axis: prev_align_axis, (optional)

      - ``+X``
        +X -- Facing positive X.
      - ``+Y``
        +Y -- Facing positive Y.
      - ``+Z``
        +Z -- Facing positive Z.
      - ``-X``
        -X -- Facing negative X.
      - ``-Y``
        -Y -- Facing negative Y.
      - ``-Z``
        -Z -- Facing negative Z.
      - ``CAM``
        Face Camera -- Facing camera.
      - ``CAM_AX``
        Camera's Main Axis -- Facing the camera's dominant axis.
      - ``NONE``
        Undocumented.
   :type prev_align_axis: Literal['+X', '+Y', '+Z', '-X', '-Y', '-Z', 'CAM', 'CAM_AX', 'NONE']
   :param align_track: Track Camera, Add a constraint to make the planes track the camera (optional)
   :type align_track: bool
   :param size_mode: Size Mode, Method for computing the plane size (optional)

      - ``ABSOLUTE``
        Absolute -- Use absolute size.
      - ``CAMERA``
        Scale to Camera Frame -- Scale to fit or fill the camera frame.
      - ``DPI``
        Pixels per Inch -- Scale based on pixels per inch.
      - ``DPBU``
        Pixels per Blender Unit -- Scale based on pixels per Blender Unit.
   :type size_mode: Literal['ABSOLUTE', 'CAMERA', 'DPI', 'DPBU']
   :param fill_mode: Scale, Method to scale the plane with the camera frame (optional)

      - ``FILL``
        Fill -- Fill camera frame, spilling outside the frame.
      - ``FIT``
        Fit -- Fit entire image within the camera frame.
   :type fill_mode: Literal['FILL', 'FIT']
   :param height: Height, Height of the created plane (in [0.001, inf], optional)
   :type height: float
   :param factor: Definition, Number of pixels per inch or Blender Unit (in [1, inf], optional)
   :type factor: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/image_as_planes.py\:857 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/image_as_planes.py#L857>`__


.. function:: invert(*, invert_r=False, invert_g=False, invert_b=False, invert_a=False)

   Invert image's channels

   :param invert_r: Red, Invert red channel (optional)
   :type invert_r: bool
   :param invert_g: Green, Invert green channel (optional)
   :type invert_g: bool
   :param invert_b: Blue, Invert blue channel (optional)
   :type invert_b: bool
   :param invert_a: Alpha, Invert alpha channel (optional)
   :type invert_a: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: match_movie_length()

   Set the image's frame range to match the video's duration

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: new(*, name="Untitled", width=1024, height=1024, color=(0.0, 0.0, 0.0, 1.0), alpha=True, generated_type='BLANK', float=False, use_stereo_3d=False, tiled=False)

   Create a new image

   :param name: Name, Image data-block name (optional, never None)
   :type name: str
   :param width: Width, Image width (in [1, inf], optional)
   :type width: int
   :param height: Height, Image height (in [1, inf], optional)
   :type height: int
   :param color: Color, Default fill color (array of 4 items, in [0, inf], optional)
   :type color: Sequence[float]
   :param alpha: Alpha, Create an image with an alpha channel (optional)
   :type alpha: bool
   :param generated_type: Generated Type, Fill the image with a grid for UV map testing (optional)
   :type generated_type: Literal[:ref:`rna_enum_image_generated_type_items`]
   :param float: 32-bit Float, Create image with 32-bit floating-point bit depth (optional)
   :type float: bool
   :param use_stereo_3d: Stereo 3D, Create an image with left and right views (optional)
   :type use_stereo_3d: bool
   :param tiled: Tiled, Create a tiled image (optional)
   :type tiled: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: open(*, allow_path_tokens=True, filepath="", directory="", files=None, hide_props_region=True, check_existing=False, filter_blender=False, filter_backup=False, filter_image=True, filter_movie=True, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='', use_sequence_detection=True, use_udim_detecting=True)

   Open image

   :param allow_path_tokens: Allow the path to contain substitution tokens (optional)
   :type allow_path_tokens: bool
   :param filepath: File Path, Path to file (optional, never None)
   :type filepath: str
   :param directory: Directory, Directory of the file (optional, never None)
   :type directory: str
   :param files: Files, (optional)
   :type files: :class:`bpy_prop_collection`\ [:class:`OperatorFileListElement`] | None
   :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings (optional)
   :type hide_props_region: bool
   :param check_existing: Check Existing, Check and warn on overwriting existing files (optional)
   :type check_existing: bool
   :param filter_blender: Filter .blend files, (optional)
   :type filter_blender: bool
   :param filter_backup: Filter backup .blend files, (optional)
   :type filter_backup: bool
   :param filter_image: Filter image files, (optional)
   :type filter_image: bool
   :param filter_movie: Filter movie files, (optional)
   :type filter_movie: bool
   :param filter_python: Filter Python files, (optional)
   :type filter_python: bool
   :param filter_font: Filter font files, (optional)
   :type filter_font: bool
   :param filter_sound: Filter sound files, (optional)
   :type filter_sound: bool
   :param filter_text: Filter text files, (optional)
   :type filter_text: bool
   :param filter_archive: Filter archive files, (optional)
   :type filter_archive: bool
   :param filter_btx: Filter btx files, (optional)
   :type filter_btx: bool
   :param filter_alembic: Filter Alembic files, (optional)
   :type filter_alembic: bool
   :param filter_usd: Filter USD files, (optional)
   :type filter_usd: bool
   :param filter_obj: Filter OBJ files, (optional)
   :type filter_obj: bool
   :param filter_volume: Filter OpenVDB volume files, (optional)
   :type filter_volume: bool
   :param filter_folder: Filter folders, (optional)
   :type filter_folder: bool
   :param filter_blenlib: Filter Blender IDs, (optional)
   :type filter_blenlib: bool
   :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file (in [1, 9], optional)
   :type filemode: int
   :param relative_path: Relative Path, Select the file relative to the blend file (optional)
   :type relative_path: bool
   :param show_multiview: Enable Multi-View, (optional)
   :type show_multiview: bool
   :param use_multiview: Use Multi-View, (optional)
   :type use_multiview: bool
   :param display_type: Display Type, (optional)

      - ``DEFAULT``
        Default -- Automatically determine display type for files.
      - ``LIST_VERTICAL``
        Short List -- Display files as short list.
      - ``LIST_HORIZONTAL``
        Long List -- Display files as a detailed list.
      - ``THUMBNAIL``
        Thumbnails -- Display files as thumbnails.
   :type display_type: Literal['DEFAULT', 'LIST_VERTICAL', 'LIST_HORIZONTAL', 'THUMBNAIL']
   :param sort_method: File sorting mode, (optional)
   :type sort_method: str
   :param use_sequence_detection: Detect Sequences, Automatically detect animated sequences in selected images (based on file names) (optional)
   :type use_sequence_detection: bool
   :param use_udim_detecting: Detect UDIMs, Detect selected UDIM files and load all matching tiles (optional)
   :type use_udim_detecting: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: open_images(*, directory="", files=None, relative_path=True, use_sequence_detection=True, use_udim_detection=True)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :param directory: directory, (optional, never None)
   :type directory: str
   :param files: files, (optional)
   :type files: :class:`bpy_prop_collection`\ [:class:`OperatorFileListElement`] | None
   :param relative_path: Use relative path, (optional)
   :type relative_path: bool
   :param use_sequence_detection: Use sequence detection, (optional)
   :type use_sequence_detection: bool
   :param use_udim_detection: Use UDIM detection, (optional)
   :type use_udim_detection: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/image.py\:238 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/image.py#L238>`__


.. function:: pack()

   Pack an image as embedded data into the .blend file

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: project_apply()

   Project edited image back onto the object

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/image.py\:192 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/image.py#L192>`__

.. function:: project_edit()

   Edit a snapshot of the 3D Viewport in an external image editor

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/image.py\:122 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/image.py#L122>`__

.. function:: read_viewlayers()

   Read all the current scene's view layers from cache, as needed

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: reload()

   Reload current image from disk

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: remove_render_slot()

   Remove the current render slot

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: render_border(*, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True)

   Set the boundaries of the render region and enable render region

   :param xmin: X Min, (in [-inf, inf], optional)
   :type xmin: int
   :param xmax: X Max, (in [-inf, inf], optional)
   :type xmax: int
   :param ymin: Y Min, (in [-inf, inf], optional)
   :type ymin: int
   :param ymax: Y Max, (in [-inf, inf], optional)
   :type ymax: int
   :param wait_for_input: Wait for Input, (optional)
   :type wait_for_input: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: replace(*, filepath="", hide_props_region=True, check_existing=False, filter_blender=False, filter_backup=False, filter_image=True, filter_movie=True, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='')

   Replace current image by another one from disk

   :param filepath: File Path, Path to file (optional, never None)
   :type filepath: str
   :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings (optional)
   :type hide_props_region: bool
   :param check_existing: Check Existing, Check and warn on overwriting existing files (optional)
   :type check_existing: bool
   :param filter_blender: Filter .blend files, (optional)
   :type filter_blender: bool
   :param filter_backup: Filter backup .blend files, (optional)
   :type filter_backup: bool
   :param filter_image: Filter image files, (optional)
   :type filter_image: bool
   :param filter_movie: Filter movie files, (optional)
   :type filter_movie: bool
   :param filter_python: Filter Python files, (optional)
   :type filter_python: bool
   :param filter_font: Filter font files, (optional)
   :type filter_font: bool
   :param filter_sound: Filter sound files, (optional)
   :type filter_sound: bool
   :param filter_text: Filter text files, (optional)
   :type filter_text: bool
   :param filter_archive: Filter archive files, (optional)
   :type filter_archive: bool
   :param filter_btx: Filter btx files, (optional)
   :type filter_btx: bool
   :param filter_alembic: Filter Alembic files, (optional)
   :type filter_alembic: bool
   :param filter_usd: Filter USD files, (optional)
   :type filter_usd: bool
   :param filter_obj: Filter OBJ files, (optional)
   :type filter_obj: bool
   :param filter_volume: Filter OpenVDB volume files, (optional)
   :type filter_volume: bool
   :param filter_folder: Filter folders, (optional)
   :type filter_folder: bool
   :param filter_blenlib: Filter Blender IDs, (optional)
   :type filter_blenlib: bool
   :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file (in [1, 9], optional)
   :type filemode: int
   :param relative_path: Relative Path, Select the file relative to the blend file (optional)
   :type relative_path: bool
   :param show_multiview: Enable Multi-View, (optional)
   :type show_multiview: bool
   :param use_multiview: Use Multi-View, (optional)
   :type use_multiview: bool
   :param display_type: Display Type, (optional)

      - ``DEFAULT``
        Default -- Automatically determine display type for files.
      - ``LIST_VERTICAL``
        Short List -- Display files as short list.
      - ``LIST_HORIZONTAL``
        Long List -- Display files as a detailed list.
      - ``THUMBNAIL``
        Thumbnails -- Display files as thumbnails.
   :type display_type: Literal['DEFAULT', 'LIST_VERTICAL', 'LIST_HORIZONTAL', 'THUMBNAIL']
   :param sort_method: File sorting mode, (optional)
   :type sort_method: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: resize(*, size=(0, 0), all_udims=False)

   Resize the image

   :param size: Size, (array of 2 items, in [1, inf], optional)
   :type size: Sequence[int]
   :param all_udims: All UDIM Tiles, Scale all the image's UDIM tiles (optional)
   :type all_udims: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: rotate_orthogonal(*, degrees='90')

   Rotate the image

   :param degrees: Degrees, Amount of rotation in degrees (90, 180, 270) (optional)

      - ``90``
        90 Degrees -- Rotate 90 degrees clockwise.
      - ``180``
        180 Degrees -- Rotate 180 degrees clockwise.
      - ``270``
        270 Degrees -- Rotate 270 degrees clockwise.
   :type degrees: Literal['90', '180', '270']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: sample(*, size=1)

   Use mouse to sample a color in current image

   :param size: Sample Size, (in [1, 128], optional)
   :type size: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: sample_line(*, xstart=0, xend=0, ystart=0, yend=0, flip=False, cursor=5)

   Sample a line and show it in Scope panels

   :param xstart: X Start, (in [-inf, inf], optional)
   :type xstart: int
   :param xend: X End, (in [-inf, inf], optional)
   :type xend: int
   :param ystart: Y Start, (in [-inf, inf], optional)
   :type ystart: int
   :param yend: Y End, (in [-inf, inf], optional)
   :type yend: int
   :param flip: Flip, (optional)
   :type flip: bool
   :param cursor: Cursor, Mouse cursor style to use during the modal operator (in [0, inf], optional)
   :type cursor: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: save()

   Save the image with current name and settings

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: save_all_modified()

   Save all modified images

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: save_as(*, save_as_render=False, copy=False, allow_path_tokens=True, filepath="", check_existing=True, filter_blender=False, filter_backup=False, filter_image=True, filter_movie=True, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='')

   Save the image with another name and/or settings

   :param save_as_render: Save As Render, Save image with render color management.For display image formats like PNG, apply view and display transform.For intermediate image formats like OpenEXR, use the default render output color space(optional)
   :type save_as_render: bool
   :param copy: Copy, Create a new image file without modifying the current image in Blender (optional)
   :type copy: bool
   :param allow_path_tokens: Allow the path to contain substitution tokens (optional)
   :type allow_path_tokens: bool
   :param filepath: File Path, Path to file (optional, never None)
   :type filepath: str
   :param check_existing: Check Existing, Check and warn on overwriting existing files (optional)
   :type check_existing: bool
   :param filter_blender: Filter .blend files, (optional)
   :type filter_blender: bool
   :param filter_backup: Filter backup .blend files, (optional)
   :type filter_backup: bool
   :param filter_image: Filter image files, (optional)
   :type filter_image: bool
   :param filter_movie: Filter movie files, (optional)
   :type filter_movie: bool
   :param filter_python: Filter Python files, (optional)
   :type filter_python: bool
   :param filter_font: Filter font files, (optional)
   :type filter_font: bool
   :param filter_sound: Filter sound files, (optional)
   :type filter_sound: bool
   :param filter_text: Filter text files, (optional)
   :type filter_text: bool
   :param filter_archive: Filter archive files, (optional)
   :type filter_archive: bool
   :param filter_btx: Filter btx files, (optional)
   :type filter_btx: bool
   :param filter_alembic: Filter Alembic files, (optional)
   :type filter_alembic: bool
   :param filter_usd: Filter USD files, (optional)
   :type filter_usd: bool
   :param filter_obj: Filter OBJ files, (optional)
   :type filter_obj: bool
   :param filter_volume: Filter OpenVDB volume files, (optional)
   :type filter_volume: bool
   :param filter_folder: Filter folders, (optional)
   :type filter_folder: bool
   :param filter_blenlib: Filter Blender IDs, (optional)
   :type filter_blenlib: bool
   :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file (in [1, 9], optional)
   :type filemode: int
   :param relative_path: Relative Path, Select the file relative to the blend file (optional)
   :type relative_path: bool
   :param show_multiview: Enable Multi-View, (optional)
   :type show_multiview: bool
   :param use_multiview: Use Multi-View, (optional)
   :type use_multiview: bool
   :param display_type: Display Type, (optional)

      - ``DEFAULT``
        Default -- Automatically determine display type for files.
      - ``LIST_VERTICAL``
        Short List -- Display files as short list.
      - ``LIST_HORIZONTAL``
        Long List -- Display files as a detailed list.
      - ``THUMBNAIL``
        Thumbnails -- Display files as thumbnails.
   :type display_type: Literal['DEFAULT', 'LIST_VERTICAL', 'LIST_HORIZONTAL', 'THUMBNAIL']
   :param sort_method: File sorting mode, (optional)
   :type sort_method: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: save_sequence()

   Save a sequence of images

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: tile_add(*, number=1002, count=1, label="", fill=True, color=(0.0, 0.0, 0.0, 1.0), generated_type='BLANK', width=1024, height=1024, float=False, alpha=True)

   Adds a tile to the image

   :param number: Number, UDIM number of the tile (in [1001, 2000], optional)
   :type number: int
   :param count: Count, How many tiles to add (in [1, inf], optional)
   :type count: int
   :param label: Label, Optional tile label (optional, never None)
   :type label: str
   :param fill: Fill, Fill new tile with a generated image (optional)
   :type fill: bool
   :param color: Color, Default fill color (array of 4 items, in [0, inf], optional)
   :type color: Sequence[float]
   :param generated_type: Generated Type, Fill the image with a grid for UV map testing (optional)
   :type generated_type: Literal[:ref:`rna_enum_image_generated_type_items`]
   :param width: Width, Image width (in [1, inf], optional)
   :type width: int
   :param height: Height, Image height (in [1, inf], optional)
   :type height: int
   :param float: 32-bit Float, Create image with 32-bit floating-point bit depth (optional)
   :type float: bool
   :param alpha: Alpha, Create an image with an alpha channel (optional)
   :type alpha: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: tile_fill(*, color=(0.0, 0.0, 0.0, 1.0), generated_type='BLANK', width=1024, height=1024, float=False, alpha=True)

   Fill the current tile with a generated image

   :param color: Color, Default fill color (array of 4 items, in [0, inf], optional)
   :type color: Sequence[float]
   :param generated_type: Generated Type, Fill the image with a grid for UV map testing (optional)
   :type generated_type: Literal[:ref:`rna_enum_image_generated_type_items`]
   :param width: Width, Image width (in [1, inf], optional)
   :type width: int
   :param height: Height, Image height (in [1, inf], optional)
   :type height: int
   :param float: 32-bit Float, Create image with 32-bit floating-point bit depth (optional)
   :type float: bool
   :param alpha: Alpha, Create an image with an alpha channel (optional)
   :type alpha: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: tile_remove()

   Removes a tile from the image

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: unpack(*, method='USE_LOCAL', id="")

   Save an image packed in the .blend file to disk

   :param method: Method, How to unpack (optional)
   :type method: Literal[:ref:`rna_enum_unpack_method_items`]
   :param id: Image Name, Image data-block name to unpack (optional, never None)
   :type id: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: view_all(*, fit_view=False)

   View the entire image

   :param fit_view: Fit View, Fit frame to the viewport (optional)
   :type fit_view: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: view_center_cursor()

   Center the view so that the cursor is in the middle of the view

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: view_cursor_center(*, fit_view=False)

   Set 2D cursor to center view location

   :param fit_view: Fit View, Fit frame to the viewport (optional)
   :type fit_view: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: view_pan(*, offset=(0.0, 0.0))

   Pan the view

   :param offset: Offset, Offset in floating-point units, 1.0 is the width and height of the image (array of 2 items, in [-inf, inf], optional)
   :type offset: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: view_selected()

   View all selected UVs

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: view_zoom(*, factor=0.0, use_cursor_init=True)

   Zoom in/out the image

   :param factor: Factor, Zoom factor, values higher than 1.0 zoom in, lower values zoom out (in [-inf, inf], optional)
   :type factor: float
   :param use_cursor_init: Use Mouse Position, Allow the initial mouse position to be used (optional)
   :type use_cursor_init: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: view_zoom_border(*, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, zoom_out=False)

   Zoom in the view to the nearest item contained in the border

   :param xmin: X Min, (in [-inf, inf], optional)
   :type xmin: int
   :param xmax: X Max, (in [-inf, inf], optional)
   :type xmax: int
   :param ymin: Y Min, (in [-inf, inf], optional)
   :type ymin: int
   :param ymax: Y Max, (in [-inf, inf], optional)
   :type ymax: int
   :param wait_for_input: Wait for Input, (optional)
   :type wait_for_input: bool
   :param zoom_out: Zoom Out, (optional)
   :type zoom_out: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: view_zoom_in(*, location=(0.0, 0.0))

   Zoom in the image (centered around 2D cursor)

   :param location: Location, Cursor location in screen coordinates (array of 2 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: view_zoom_out(*, location=(0.0, 0.0))

   Zoom out the image (centered around 2D cursor)

   :param location: Location, Cursor location in screen coordinates (array of 2 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: view_zoom_ratio(*, ratio=0.0)

   Set zoom ratio of the view

   :param ratio: Ratio, Zoom ratio, 1.0 is 1:1, higher is zoomed in, lower is zoomed out (in [-inf, inf], optional)
   :type ratio: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

