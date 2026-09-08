BlendDataLibraries(bpy_prop_collection)
=======================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_prop`, :class:`bpy_prop_collection`

.. class:: BlendDataLibraries(bpy_prop_collection)

   Collection of libraries

   .. method:: tag(value)

      tag

      :param value: Value
      :type value: bool

   .. method:: remove(library, *, do_unlink=True, do_id_user=True, do_ui_user=True)

      Remove a library from the current blendfile

      :param library: Library to remove (never None)
      :type library: :class:`Library` | None
      :param do_unlink: Unlink all usages of this library before deleting it (optional)
      :type do_unlink: bool
      :param do_id_user: Decrement user counter of all data-blocks used by this library (optional)
      :type do_id_user: bool
      :param do_ui_user: Make sure interface does not reference this library (optional)
      :type do_ui_user: bool

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


   .. method:: load(filepath, *, link=False, pack=False, relative=False, set_fake=False, recursive=False, reuse_local_id=False, assets_only=False, clear_asset_data=False, create_liboverrides=False, reuse_liboverrides=False, create_liboverrides_runtime=False)
   
      Returns a context manager which exposes 2 library objects on entering.
      Each object has attributes matching bpy.data which are lists of strings to be linked.
   
      :param filepath: The path to a blend file.
      :type filepath: str | bytes
      :param link: When False reference to the original file is lost.
      :type link: bool
      :param pack: If True, and ``link`` is also True, pack linked data-blocks into the current blend-file.
      :type pack: bool
      :param relative: When True the path is stored relative to the open blend file.
      :type relative: bool
      :param set_fake: If True, set fake user on appended IDs.
      :type set_fake: bool
      :param recursive: If True, also make indirect dependencies of appended libraries local.
      :type recursive: bool
      :param reuse_local_id: If True,try to re-use previously appended matching ID on new append.
      :type reuse_local_id: bool
      :param assets_only: If True, only list data-blocks marked as assets.
      :type assets_only: bool
      :param clear_asset_data: If True, clear the asset data on append (it is always kept for linked data).
      :type clear_asset_data: bool
      :param create_liboverrides: If True and ``link`` is True, liboverrides will
         be created for linked data.
      :type create_liboverrides: bool
      :param reuse_liboverrides: If True and ``create_liboverride`` is True,
         search for existing liboverride first.
      :type reuse_liboverrides: bool
      :param create_liboverrides_runtime: If True and ``create_liboverride`` is True,
         create (or search for existing) runtime liboverride.
      :type create_liboverrides_runtime: bool


      .. literalinclude:: ./examples/bpy.types.BlendDataLibraries.load.0.py


   .. method:: write(filepath, datablocks, *, path_remap='NONE', fake_user=False, compress=False)
   
      Write data-blocks into a blend file.
   
      .. note::
   
         Indirectly referenced data-blocks will be expanded and written too.
   
      :param filepath: The path to write the blend-file.
      :type filepath: str | bytes
      :param datablocks: set of data-blocks.
      :type datablocks: set[:class:`bpy.types.ID`]
      :param path_remap: Optionally remap paths when writing the file:
   
         - ``NONE`` No path manipulation (default).
         - ``RELATIVE`` Remap paths that are already relative to the new location.
         - ``RELATIVE_ALL`` Remap all paths to be relative to the new location.
         - ``ABSOLUTE`` Make all paths absolute on writing.
   
      :type path_remap: str
      :param fake_user: When True, data-blocks will be written with fake-user flag enabled.
      :type fake_user: bool
      :param compress: When True, write a compressed blend file.
      :type compress: bool


      .. literalinclude:: ./examples/bpy.types.BlendDataLibraries.write.0.py


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

   - :class:`BlendData.libraries`

