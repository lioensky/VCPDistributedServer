BlendData(bpy_struct)
=====================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: BlendData(bpy_struct)

   Main data structure representing a .blend file and all its data-blocks

   .. data:: actions

      Action data-blocks (default None, readonly)

      :type: :class:`BlendDataActions`\ [:class:`Action`]

   .. data:: annotations

      Annotation data-blocks (legacy Grease Pencil) (default None, readonly)

      :type: :class:`BlendDataAnnotations`\ [:class:`Annotation`]

   .. data:: armatures

      Armature data-blocks (default None, readonly)

      :type: :class:`BlendDataArmatures`\ [:class:`Armature`]

   .. data:: brushes

      Brush data-blocks (default None, readonly)

      :type: :class:`BlendDataBrushes`\ [:class:`Brush`]

   .. data:: cache_files

      Cache Files data-blocks (default None, readonly)

      :type: :class:`BlendDataCacheFiles`\ [:class:`CacheFile`]

   .. data:: cameras

      Camera data-blocks (default None, readonly)

      :type: :class:`BlendDataCameras`\ [:class:`Camera`]

   .. data:: collections

      Collection data-blocks (default None, readonly)

      :type: :class:`BlendDataCollections`\ [:class:`Collection`]

   .. data:: colorspace

      Information about the color space used for data-blocks in a blend file (readonly, never None)

      :type: :class:`BlendFileColorspace`

   .. data:: curves

      Curve data-blocks (default None, readonly)

      :type: :class:`BlendDataCurves`\ [:class:`Curve`]

   .. data:: filepath

      Path to the .blend file (default "", readonly, never None)

      :type: str

   .. data:: fonts

      Vector font data-blocks (default None, readonly)

      :type: :class:`BlendDataFonts`\ [:class:`VectorFont`]

   .. data:: grease_pencils

      Grease Pencil data-blocks (default None, readonly)

      :type: :class:`BlendDataGreasePencilsV3`\ [:class:`GreasePencil`]

   .. data:: hair_curves

      Hair curve data-blocks (default None, readonly)

      :type: :class:`BlendDataHairCurves`\ [:class:`Curves`]

   .. data:: images

      Image data-blocks (default None, readonly)

      :type: :class:`BlendDataImages`\ [:class:`Image`]

   .. data:: is_dirty

      Have recent edits been saved to disk (default False, readonly)

      :type: bool

   .. data:: is_saved

      Has the current session been saved to disk as a .blend file (default False, readonly)

      :type: bool

   .. data:: lattices

      Lattice data-blocks (default None, readonly)

      :type: :class:`BlendDataLattices`\ [:class:`Lattice`]

   .. data:: libraries

      Library data-blocks (default None, readonly)

      :type: :class:`BlendDataLibraries`\ [:class:`Library`]

   .. data:: lightprobes

      Light Probe data-blocks (default None, readonly)

      :type: :class:`BlendDataProbes`\ [:class:`LightProbe`]

   .. data:: lights

      Light data-blocks (default None, readonly)

      :type: :class:`BlendDataLights`\ [:class:`Light`]

   .. data:: linestyles

      Line Style data-blocks (default None, readonly)

      :type: :class:`BlendDataLineStyles`\ [:class:`FreestyleLineStyle`]

   .. data:: masks

      Masks data-blocks (default None, readonly)

      :type: :class:`BlendDataMasks`\ [:class:`Mask`]

   .. data:: materials

      Material data-blocks (default None, readonly)

      :type: :class:`BlendDataMaterials`\ [:class:`Material`]

   .. data:: meshes

      Mesh data-blocks (default None, readonly)

      :type: :class:`BlendDataMeshes`\ [:class:`Mesh`]

   .. data:: metaballs

      Metaball data-blocks (default None, readonly)

      :type: :class:`BlendDataMetaBalls`\ [:class:`MetaBall`]

   .. data:: movieclips

      Movie Clip data-blocks (default None, readonly)

      :type: :class:`BlendDataMovieClips`\ [:class:`MovieClip`]

   .. data:: node_groups

      Node group data-blocks (default None, readonly)

      :type: :class:`BlendDataNodeTrees`\ [:class:`NodeTree`]

   .. data:: objects

      Object data-blocks (default None, readonly)

      :type: :class:`BlendDataObjects`\ [:class:`Object`]

   .. data:: paint_curves

      Paint Curves data-blocks (default None, readonly)

      :type: :class:`BlendDataPaintCurves`\ [:class:`PaintCurve`]

   .. data:: palettes

      Palette data-blocks (default None, readonly)

      :type: :class:`BlendDataPalettes`\ [:class:`Palette`]

   .. data:: particles

      Particle data-blocks (default None, readonly)

      :type: :class:`BlendDataParticles`\ [:class:`ParticleSettings`]

   .. data:: pointclouds

      Point cloud data-blocks (default None, readonly)

      :type: :class:`BlendDataPointClouds`\ [:class:`PointCloud`]

   .. data:: scenes

      Scene data-blocks (default None, readonly)

      :type: :class:`BlendDataScenes`\ [:class:`Scene`]

   .. data:: screens

      Screen data-blocks (default None, readonly)

      :type: :class:`BlendDataScreens`\ [:class:`Screen`]

   .. data:: shape_keys

      Shape Key data-blocks (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`Key`]

   .. data:: sounds

      Sound data-blocks (default None, readonly)

      :type: :class:`BlendDataSounds`\ [:class:`Sound`]

   .. data:: speakers

      Speaker data-blocks (default None, readonly)

      :type: :class:`BlendDataSpeakers`\ [:class:`Speaker`]

   .. data:: texts

      Text data-blocks (default None, readonly)

      :type: :class:`BlendDataTexts`\ [:class:`Text`]

   .. data:: textures

      Texture data-blocks (default None, readonly)

      :type: :class:`BlendDataTextures`\ [:class:`Texture`]

   .. attribute:: use_autopack

      Automatically pack all external data into .blend file (default False)

      :type: bool

   .. data:: version

      File format version the .blend file was saved with (array of 3 items, in [0, inf], default (0, 0, 0), readonly)

      :type: :class:`bpy_prop_array`\ [int]

   .. data:: volumes

      Volume data-blocks (default None, readonly)

      :type: :class:`BlendDataVolumes`\ [:class:`Volume`]

   .. data:: window_managers

      Window manager data-blocks (default None, readonly)

      :type: :class:`BlendDataWindowManagers`\ [:class:`WindowManager`]

   .. data:: workspaces

      Workspace data-blocks (default None, readonly)

      :type: :class:`BlendDataWorkSpaces`\ [:class:`WorkSpace`]

   .. data:: worlds

      World data-blocks (default None, readonly)

      :type: :class:`BlendDataWorlds`\ [:class:`World`]

   .. method:: pack_linked_ids_hierarchy(root_id)

      Pack the given linked ID and its dependencies into current blendfile

      :param root_id: Root linked ID to pack
      :type root_id: :class:`ID` | None
      :return: The packed ID matching the given root ID
      :rtype: :class:`ID`

   .. method:: batch_remove(ids)
   
      Remove (delete) several IDs at once.
   
      Note that this function is quicker than individual calls to :func:`remove()` (from :class:`bpy.types.BlendData`
      ID collections), but less safe/versatile (it can break Blender, e.g. by removing all scenes...).
   
      :param ids: Sequence of IDs (types can be mixed).
      :type ids: Sequence[:class:`bpy.types.ID`]


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


   .. method:: file_path_foreach(visit_path_fn, *, subset=None, visit_types=None, flags={'SKIP_PACKED', 'SKIP_WEAK_REFERENCES'})
   
      Call ``visit_path_fn`` for the file paths used by all ID data-blocks in current ``bpy.data``.
   
      For list of valid set members for visit_types, see: :class:`bpy.types.KeyingSetPath.id_type`.
   
      :param visit_path_fn: function that takes three parameters: the data-block, a file path, and a placeholder for future use. The function should return either ``None`` or a ``str``. In the latter case, the visited file path will be replaced with the returned string.
      :type visit_path_fn: Callable[[:class:`bpy.types.ID`, str, Any], str|None]
      :param subset: When given, only these data-blocks and their used file paths will be visited.
      :type subset: set[str] | None
      :param visit_types: When given, only visit data-blocks of these types. Ignored if ``subset`` is also given.
      :type visit_types: set[str] | None
      :type flags: set[str]
      :param flags: Set of flags that influence which data-blocks are visited. See :ref:`rna_enum_file_path_foreach_flag_items`.


   .. method:: file_path_map(*, subset=None, key_types=None, include_libraries=False)
   
      Returns a mapping of all ID data-blocks in current ``bpy.data`` to a set of all file paths used by them.
   
      For list of valid set members for key_types, see: :class:`bpy.types.KeyingSetPath.id_type`.
   
      :param subset: When given, only these data-blocks and their used file paths will be included as keys/values in the map.
      :type subset: Sequence[:class:`bpy.types.ID`] | None
      :param key_types: When given, filter the keys mapped by ID types. Ignored if ``subset`` is also given.
      :type key_types: set[str] | None
      :param include_libraries: Include library file paths of linked data. False by default.
      :type include_libraries: bool
      :return: dictionary of :class:`bpy.types.ID` instances, with sets of file path strings as their values.
      :rtype: dict[:class:`bpy.types.ID`, set[str]]


   .. method:: orphans_purge()
   
      Remove (delete) all IDs with no user.
   
      :param do_local_ids: Include unused local IDs in the deletion, defaults to True
      :type do_local_ids: bool, optional
      :param do_linked_ids: Include unused linked IDs in the deletion, defaults to True
      :type do_linked_ids: bool, optional
      :param do_recursive: Recursively check for unused IDs, ensuring no orphaned one remain after a single run of that function, defaults to False
      :type do_recursive: bool, optional
      :return: The number of deleted IDs.
      :rtype: int


   .. staticmethod:: temp_data(*, filepath=None)
   
      A context manager that temporarily creates blender file data.
   
      :param filepath: The file path for the newly temporary data. When None, the path of the currently open file is used.
      :type filepath: str | bytes | None
   
      :return: Blend file data which is freed once the context exits.
      :rtype: :class:`bpy.types.BlendData`


   .. method:: user_map(*, subset=None, key_types=None, value_types=None)
   
      Returns a mapping of all ID data-blocks in current ``bpy.data`` to a set of all data-blocks using them.
   
      For list of valid set members for key_types & value_types, see: :class:`bpy.types.KeyingSetPath.id_type`.
   
      :param subset: When passed, only these data-blocks and their users will be included as keys/values in the map.
      :type subset: Sequence[:class:`bpy.types.ID`] | None
      :param key_types: Filter the keys mapped by ID types.
      :type key_types: set[str] | None
      :param value_types: Filter the values in the set by ID types.
      :type value_types: set[str] | None
      :return: dictionary that maps data-blocks ID's to their users.
      :rtype: dict[:class:`bpy.types.ID`, set[:class:`bpy.types.ID`]]


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

   - :class:`Context.blend_data`
   - :class:`RenderEngine.update`

