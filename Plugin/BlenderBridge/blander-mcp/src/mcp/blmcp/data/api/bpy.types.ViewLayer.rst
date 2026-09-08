ViewLayer(bpy_struct)
=====================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ViewLayer(bpy_struct)

   View layer

   .. data:: active_aov

      Active AOV (readonly)

      :type: :class:`AOV` | None

   .. attribute:: active_aov_index

      Index of active AOV (in [0, inf], default 0)

      :type: int

   .. attribute:: active_layer_collection

      Active layer collection in this view layer's hierarchy (never None)

      :type: :class:`LayerCollection`

   .. data:: active_lightgroup

      Active Lightgroup (readonly)

      :type: :class:`Lightgroup` | None

   .. attribute:: active_lightgroup_index

      Index of active lightgroup (in [0, inf], default 0)

      :type: int

   .. data:: aovs

      (default None, readonly)

      :type: :class:`AOVs`\ [:class:`AOV`]

   .. data:: depsgraph

      Dependencies in the scene data (readonly)

      :type: :class:`Depsgraph` | None

   .. data:: eevee

      View layer settings for EEVEE (readonly, never None)

      :type: :class:`ViewLayerEEVEE`

   .. data:: freestyle_settings

      (readonly, never None)

      :type: :class:`FreestyleSettings`

   .. data:: has_export_collections

      At least one Collection in this View Layer has an exporter (default False, readonly)

      :type: bool

   .. data:: layer_collection

      Root of collections hierarchy of this view layer, its 'collection' pointer property is the same as the scene's master collection (readonly, never None)

      :type: :class:`LayerCollection`

   .. data:: lightgroups

      (default None, readonly)

      :type: :class:`Lightgroups`\ [:class:`Lightgroup`]

   .. attribute:: material_override

      Material to override all other materials in this view layer

      :type: :class:`Material` | None

   .. attribute:: name

      View layer name (default "", never None)

      :type: str

   .. data:: objects

      All the objects in this layer (default None, readonly)

      :type: :class:`LayerObjects`\ [:class:`Object`]

   .. attribute:: pass_alpha_threshold

      Z, Index, normal, UV and vector passes are only affected by surfaces with alpha transparency equal to or higher than this threshold (in [0, 1], default 0.5)

      :type: float

   .. attribute:: pass_cryptomatte_depth

      Sets how many unique objects can be distinguished per pixel (in [2, 16], default 6)

      :type: int

   .. attribute:: samples

      Override number of render samples for this view layer, 0 will use the scene setting (in [0, inf], default 0)

      :type: int

   .. attribute:: use

      Enable or disable rendering of this View Layer (default True)

      :type: bool

   .. attribute:: use_ao

      Render Ambient Occlusion in this Layer (default True)

      :type: bool

   .. attribute:: use_freestyle

      Render stylized strokes in this Layer (default True)

      :type: bool

   .. attribute:: use_grease_pencil

      Render Grease Pencil on this layer (default True)

      :type: bool

   .. attribute:: use_motion_blur

      Render motion blur in this Layer, if enabled in the scene (default True)

      :type: bool

   .. attribute:: use_pass_ambient_occlusion

      Deliver Ambient Occlusion pass (default False)

      :type: bool

   .. attribute:: use_pass_combined

      Deliver full combined RGBA buffer (default True)

      :type: bool

   .. attribute:: use_pass_cryptomatte_accurate

      Generate a more accurate cryptomatte pass (default True)

      :type: bool

   .. attribute:: use_pass_cryptomatte_asset

      Render cryptomatte asset pass, for isolating groups of objects with the same parent (default False)

      :type: bool

   .. attribute:: use_pass_cryptomatte_material

      Render cryptomatte material pass, for isolating materials in compositing (default False)

      :type: bool

   .. attribute:: use_pass_cryptomatte_object

      Render cryptomatte object pass, for isolating objects in compositing (default False)

      :type: bool

   .. attribute:: use_pass_diffuse_color

      Deliver diffuse color pass (default False)

      :type: bool

   .. attribute:: use_pass_diffuse_direct

      Deliver diffuse direct pass (default False)

      :type: bool

   .. attribute:: use_pass_diffuse_indirect

      Deliver diffuse indirect pass (default False)

      :type: bool

   .. attribute:: use_pass_emit

      Deliver emission pass (default False)

      :type: bool

   .. attribute:: use_pass_environment

      Deliver environment lighting pass (default False)

      :type: bool

   .. attribute:: use_pass_glossy_color

      Deliver glossy color pass (default False)

      :type: bool

   .. attribute:: use_pass_glossy_direct

      Deliver glossy direct pass (default False)

      :type: bool

   .. attribute:: use_pass_glossy_indirect

      Deliver glossy indirect pass (default False)

      :type: bool

   .. attribute:: use_pass_grease_pencil

      Deliver Grease Pencil render result in a separate pass (default False)

      :type: bool

   .. attribute:: use_pass_material_index

      Deliver material index pass (default False)

      :type: bool

   .. attribute:: use_pass_mist

      Deliver mist factor pass (0.0 to 1.0) (default False)

      :type: bool

   .. attribute:: use_pass_normal

      Deliver normal pass (default False)

      :type: bool

   .. attribute:: use_pass_object_index

      Deliver object index pass (default False)

      :type: bool

   .. attribute:: use_pass_position

      Deliver position pass (default False)

      :type: bool

   .. attribute:: use_pass_shadow

      Deliver shadow pass (default False)

      :type: bool

   .. attribute:: use_pass_subsurface_color

      Deliver subsurface color pass (default False)

      :type: bool

   .. attribute:: use_pass_subsurface_direct

      Deliver subsurface direct pass (default False)

      :type: bool

   .. attribute:: use_pass_subsurface_indirect

      Deliver subsurface indirect pass (default False)

      :type: bool

   .. attribute:: use_pass_transmission_color

      Deliver transmission color pass (default False)

      :type: bool

   .. attribute:: use_pass_transmission_direct

      Deliver transmission direct pass (default False)

      :type: bool

   .. attribute:: use_pass_transmission_indirect

      Deliver transmission indirect pass (default False)

      :type: bool

   .. attribute:: use_pass_uv

      Deliver texture UV pass (default False)

      :type: bool

   .. attribute:: use_pass_vector

      Deliver speed vector pass (default False)

      :type: bool

   .. attribute:: use_pass_z

      Deliver depth values pass (default False)

      :type: bool

   .. attribute:: use_sky

      Render Sky in this Layer (default True)

      :type: bool

   .. attribute:: use_solid

      Render Solid faces in this Layer (default True)

      :type: bool

   .. attribute:: use_strand

      Render Strands in this Layer (default True)

      :type: bool

   .. attribute:: use_volumes

      Render volumes in this Layer (default True)

      :type: bool

   .. attribute:: world_override

      Override world in this view layer

      :type: :class:`World` | None

   .. method:: bl_system_properties_get(*, do_create=False)

      DEBUG ONLY. Internal access to runtime-defined RNA data storage, intended solely for testing and debugging purposes. Do not access it in regular scripting work, and in particular, do not assume that it contains writable data

      :param do_create: Ensure that system properties are created if they do not exist yet (optional)
      :type do_create: bool
      :return: The system properties root container, or None if there are no system properties stored in this data yet, and its creation was not requested
      :rtype: :class:`PropertyGroup`

   .. classmethod:: update_render_passes()

      Requery the enabled render passes from the render engine


   .. method:: update()

      Update data tagged to be updated from previous access to data or operators


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

   - :mod:`bpy.context.view_layer`
   - :class:`Context.view_layer`
   - :class:`Depsgraph.view_layer`
   - :class:`Depsgraph.view_layer_eval`
   - :class:`ID.override_hierarchy_create`
   - :class:`IDOverrideLibrary.resync`
   - :class:`LayerCollection.has_selected_objects`
   - :class:`Object.hide_get`
   - :class:`Object.hide_set`
   - :class:`Object.holdout_get`
   - :class:`Object.indirect_only_get`
   - :class:`Object.select_get`
   - :class:`Object.select_set`
   - :class:`Object.visible_get`
   - :class:`RenderEngine.register_pass`
   - :class:`RenderEngine.update_render_passes`
   - :class:`Scene.statistics`
   - :class:`Scene.view_layers`
   - :class:`ViewLayers.new`
   - :class:`ViewLayers.remove`
   - :class:`Window.view_layer`

