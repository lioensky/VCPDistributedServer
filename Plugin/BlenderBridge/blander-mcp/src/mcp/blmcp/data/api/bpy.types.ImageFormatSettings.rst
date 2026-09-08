ImageFormatSettings(bpy_struct)
===============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ImageFormatSettings(bpy_struct)

   Settings for image formats

   .. attribute:: cineon_black

      Log conversion reference blackpoint (in [0, 1024], default 0)

      :type: int

   .. attribute:: cineon_gamma

      Log conversion gamma (in [0, 10], default 0.0)

      :type: float

   .. attribute:: cineon_white

      Log conversion reference whitepoint (in [0, 1024], default 0)

      :type: int

   .. attribute:: color_depth

      Bit depth per channel (default ``'8'``)

      :type: Literal[:ref:`rna_enum_image_color_depth_items`]

   .. attribute:: color_management

      Which color management settings to use for file saving (default ``'FOLLOW_SCENE'``)

      :type: Literal['FOLLOW_SCENE', 'OVERRIDE']

   .. attribute:: color_mode

      Choose BW for saving grayscale images, RGB for saving red, green and blue channels, and RGBA for saving red, green, blue and alpha channels (default ``'RGBA'``)

      :type: Literal[:ref:`rna_enum_image_color_mode_items`]

   .. attribute:: compression

      Amount of time to determine best compression: 0 = no compression with fast file output, 100 = maximum lossless compression with slow file output (in [0, 100], default 15)

      :type: int

   .. data:: display_settings

      Settings of device saved image would be displayed on (readonly)

      :type: :class:`ColorManagedDisplaySettings` | None

   .. attribute:: file_format

      File format to save the rendered images as (default ``'PNG'``)

      :type: Literal[:ref:`rna_enum_image_type_all_items`]

   .. data:: has_linear_colorspace

      File format expects linear color space (default False, readonly)

      :type: bool

   .. data:: linear_colorspace_settings

      Output color space settings (readonly)

      :type: :class:`ColorManagedInputColorspaceSettings` | None

   .. attribute:: media_type

      The type of media to save (default ``'IMAGE'``)

      :type: Literal['IMAGE', 'MULTI_LAYER_IMAGE', 'VIDEO']

   .. attribute:: quality

      Quality for image formats that support lossy compression (in [0, 100], default 90)

      :type: int

   .. data:: stereo_3d_format

      Settings for stereo 3D (readonly, never None)

      :type: :class:`Stereo3dFormat`

   .. attribute:: tiff_codec

      Compression mode for TIFF (default ``'DEFLATE'``)

      :type: Literal['NONE', 'DEFLATE', 'LZW', 'PACKBITS']

   .. attribute:: use_cineon_log

      Convert to logarithmic color space (default False)

      :type: bool

   .. attribute:: use_preview

      When rendering animations, save JPG preview images in same directory (default False)

      :type: bool

   .. data:: view_settings

      Color management settings applied on image before saving (readonly)

      :type: :class:`ColorManagedViewSettings` | None

   .. attribute:: views_format

      Format of multiview media (default ``'INDIVIDUAL'``)

      :type: Literal[:ref:`rna_enum_views_format_multiview_items`]

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

   - :class:`CompositorNodeOutputFile.format`
   - :class:`NodeCompositorFileOutputItem.format`
   - :class:`BakeSettings.image_settings`
   - :class:`RenderSettings.image_settings`
   - :class:`UILayout.template_image_settings`
   - :class:`UILayout.template_image_views`

