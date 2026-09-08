CameraBackgroundImage(bpy_struct)
=================================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: CameraBackgroundImage(bpy_struct)

   Image and settings for display in the 3D View background

   .. attribute:: alpha

      Image opacity to blend the image against the background color (in [0, 1], default 0.0)

      :type: float

   .. attribute:: clip

      Movie clip displayed and edited in this space

      :type: :class:`MovieClip` | None

   .. data:: clip_user

      Parameters defining which frame of the movie clip is displayed (readonly, never None)

      :type: :class:`MovieClipUser`

   .. attribute:: display_depth

      Display under or over everything (default ``'BACK'``)

      :type: Literal['BACK', 'FRONT']

   .. attribute:: frame_method

      How the image fits in the camera frame (default ``'FIT'``)

      :type: Literal['STRETCH', 'FIT', 'CROP']

   .. attribute:: image

      Image displayed and edited in this space

      :type: :class:`Image` | None

   .. data:: image_user

      Parameters defining which layer, pass and frame of the image is displayed (readonly, never None)

      :type: :class:`ImageUser`

   .. data:: is_override_data

      In a local override camera, whether this background image comes from the linked reference camera, or is local to the override (default True, readonly)

      :type: bool

   .. attribute:: offset

      (array of 2 items, in [-inf, inf], default (0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: rotation

      Rotation for the background image (ortho view only) (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: scale

      Scale the background image (in [0, inf], default 0.0)

      :type: float

   .. attribute:: show_background_image

      Show this image as background (default True)

      :type: bool

   .. attribute:: show_expanded

      Show the details in the user interface (default False)

      :type: bool

   .. attribute:: show_on_foreground

      Show this image in front of objects in viewport (default False)

      :type: bool

   .. attribute:: source

      Data source used for background (default ``'IMAGE'``)

      :type: Literal['IMAGE', 'MOVIE_CLIP']

   .. attribute:: use_camera_clip

      Use movie clip from active scene camera (default False)

      :type: bool

   .. attribute:: use_flip_x

      Flip the background image horizontally (default False)

      :type: bool

   .. attribute:: use_flip_y

      Flip the background image vertically (default False)

      :type: bool

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

   - :class:`Camera.background_images`
   - :class:`CameraBackgroundImages.new`
   - :class:`CameraBackgroundImages.remove`

