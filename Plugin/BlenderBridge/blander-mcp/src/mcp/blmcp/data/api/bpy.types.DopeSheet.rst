DopeSheet(bpy_struct)
=====================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: DopeSheet(bpy_struct)

   Settings for filtering the channels shown in animation editors

   .. attribute:: filter_collection

      Collection that included object should be a member of

      :type: :class:`Collection` | None

   .. attribute:: filter_fcurve_name

      F-Curve live filtering string (default "", never None)

      :type: str

   .. attribute:: filter_text

      Live filtering string (default "", never None)

      :type: str

   .. attribute:: show_armatures

      Include visualization of armature related animation data (default True)

      :type: bool

   .. attribute:: show_cache_files

      Include visualization of cache file related animation data (default True)

      :type: bool

   .. attribute:: show_cameras

      Include visualization of camera related animation data (default True)

      :type: bool

   .. attribute:: show_curves

      Include visualization of curve related animation data (default True)

      :type: bool

   .. attribute:: show_datablock_filters

      Show options for whether channels related to certain types of data are included (default False)

      :type: bool

   .. attribute:: show_driver_fallback_as_error

      Include drivers that relied on any fallback values for their evaluation in the Only Show Errors filter, even if the driver evaluation succeeded (default False)

      :type: bool

   .. attribute:: show_expanded_summary

      Collapse summary when shown, so all other channels get hidden (Dope Sheet editors only) (default True)

      :type: bool

   .. attribute:: show_gpencil

      Include visualization of Grease Pencil related animation data and frames (default True)

      :type: bool

   .. attribute:: show_hair_curves

      Include visualization of hair related animation data (default True)

      :type: bool

   .. attribute:: show_hidden

      Include channels from objects/bone that are not visible (default False)

      :type: bool

   .. attribute:: show_lattices

      Include visualization of lattice related animation data (default True)

      :type: bool

   .. attribute:: show_lightprobes

      Include visualization of lightprobe related animation data (default True)

      :type: bool

   .. attribute:: show_lights

      Include visualization of light related animation data (default True)

      :type: bool

   .. attribute:: show_linestyles

      Include visualization of Line Style related Animation data (default True)

      :type: bool

   .. attribute:: show_materials

      Include visualization of material related animation data (default True)

      :type: bool

   .. attribute:: show_meshes

      Include visualization of mesh related animation data (default True)

      :type: bool

   .. attribute:: show_metaballs

      Include visualization of metaball related animation data (default True)

      :type: bool

   .. attribute:: show_missing_nla

      Include animation data-blocks with no NLA data (NLA editor only) (default True)

      :type: bool

   .. attribute:: show_modifiers

      Include visualization of animation data related to data-blocks linked to modifiers (default True)

      :type: bool

   .. attribute:: show_movieclips

      Include visualization of movie clip related animation data (default True)

      :type: bool

   .. attribute:: show_nodes

      Include visualization of node related animation data (default True)

      :type: bool

   .. attribute:: show_only_errors

      Only include F-Curves and drivers that are disabled or have errors (default False)

      :type: bool

   .. attribute:: show_only_selected

      Only include channels relating to selected objects and data (default False)

      :type: bool

   .. attribute:: show_only_slot_of_active_object

      Only show the slot of the active Object. Otherwise show all the Action's Slots (default False)

      :type: bool

   .. attribute:: show_particles

      Include visualization of particle related animation data (default True)

      :type: bool

   .. attribute:: show_pointclouds

      Include visualization of point cloud related animation data (default True)

      :type: bool

   .. attribute:: show_scenes

      Include visualization of scene related animation data (default True)

      :type: bool

   .. attribute:: show_shapekeys

      Include visualization of shape key related animation data (default True)

      :type: bool

   .. attribute:: show_speakers

      Include visualization of speaker related animation data (default True)

      :type: bool

   .. attribute:: show_summary

      Display an additional 'summary' line (Dope Sheet editors only) (default False)

      :type: bool

   .. attribute:: show_textures

      Include visualization of texture related animation data (default True)

      :type: bool

   .. attribute:: show_transforms

      Include visualization of object-level animation data (mostly transforms) (default True)

      :type: bool

   .. attribute:: show_volumes

      Include visualization of volume related animation data (default True)

      :type: bool

   .. attribute:: show_worlds

      Include visualization of world related animation data (default True)

      :type: bool

   .. data:: source

      ID-Block representing source data, usually ID_SCE (i.e. Scene) (readonly)

      :type: :class:`ID` | None

   .. attribute:: use_datablock_sort

      Alphabetically sorts data-blocks - mainly objects in the scene (disable to increase viewport speed) (default True)

      :type: bool

   .. attribute:: use_filter_invert

      Invert filter search (default False)

      :type: bool

   .. attribute:: use_multi_word_filter

      Perform fuzzy/multi-word matching.
      Warning: May be slow
      
      (default False)

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

   - :class:`SpaceDopeSheetEditor.dopesheet`
   - :class:`SpaceGraphEditor.dopesheet`
   - :class:`SpaceNLA.dopesheet`

