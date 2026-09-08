PointCacheItem(bpy_struct)
==========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: PointCacheItem(bpy_struct)

   Point cache for physics simulations

   .. attribute:: filepath

      Cache file path (default "", never None, blend relative ``//`` prefix supported)

      :type: str

   .. attribute:: frame_end

      Frame on which the simulation stops (in [1, 1048574], default 0)

      :type: int

   .. attribute:: frame_start

      Frame on which the simulation starts (in [-1048574, 1048574], default 0)

      :type: int

   .. attribute:: frame_step

      Number of frames between cached frames (in [1, 20], default 0)

      :type: int

   .. attribute:: index

      Index number of cache files (in [-1, 100], default 0)

      :type: int

   .. data:: info

      Info on current cache status (default "", readonly, never None)

      :type: str

   .. data:: is_baked

      The cache is baked (default False, readonly)

      :type: bool

   .. data:: is_baking

      The cache is being baked (default False, readonly)

      :type: bool

   .. data:: is_frame_skip

      Some frames were skipped while baking/saving that cache (default False, readonly)

      :type: bool

   .. data:: is_outdated

      (default False, readonly)

      :type: bool

   .. attribute:: name

      Cache name (default "", never None)

      :type: str

   .. attribute:: use_disk_cache

      Save cache files to disk (.blend file must be saved first) (default False)

      :type: bool

   .. attribute:: use_external

      Read cache from an external location (default False)

      :type: bool

   .. attribute:: use_library_path

      Use this file's path for the disk cache when library linked into another file (for local bakes per scene file, disable this option) (default True)

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

   - :class:`PointCache.point_caches`

