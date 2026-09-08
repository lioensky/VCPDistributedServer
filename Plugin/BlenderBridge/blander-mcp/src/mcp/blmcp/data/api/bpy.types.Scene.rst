Scene(ID)
=========

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: Scene(ID)

   Scene data-block, consisting in objects and defining time and render related settings

   .. attribute:: active_clip

      Active Movie Clip that can be used by motion tracking constraints or as a camera's background image

      :type: :class:`MovieClip` | None

   .. data:: animation_data

      Animation data for this data-block (readonly)

      :type: :class:`AnimData` | None

   .. attribute:: annotation

      Data-block used for annotations in the 3D view

      :type: :class:`Annotation` | None

   .. attribute:: audio_distance_model

      Distance model for distance attenuation calculation (default ``'INVERSE_CLAMPED'``)

      - ``NONE``
        None -- No distance attenuation.
      - ``INVERSE``
        Inverse -- Inverse distance model.
      - ``INVERSE_CLAMPED``
        Inverse Clamped -- Inverse distance model with clamping.
      - ``LINEAR``
        Linear -- Linear distance model.
      - ``LINEAR_CLAMPED``
        Linear Clamped -- Linear distance model with clamping.
      - ``EXPONENT``
        Exponential -- Exponential distance model.
      - ``EXPONENT_CLAMPED``
        Exponential Clamped -- Exponential distance model with clamping.

      :type: Literal['NONE', 'INVERSE', 'INVERSE_CLAMPED', 'LINEAR', 'LINEAR_CLAMPED', 'EXPONENT', 'EXPONENT_CLAMPED']

   .. attribute:: audio_doppler_factor

      Pitch factor for Doppler effect calculation (in [0, inf], default 1.0)

      :type: float

   .. attribute:: audio_doppler_speed

      Speed of sound for Doppler effect calculation (in [0.01, inf], default 343.3)

      :type: float

   .. attribute:: audio_volume

      Audio volume (in [0, 100], default 1.0)

      :type: float

   .. attribute:: background_set

      Background set scene

      :type: :class:`Scene` | None

   .. attribute:: camera

      Active camera, used for rendering the scene

      :type: :class:`Object` | None

   .. data:: collection

      Scene root collection that owns all the objects and other collections instantiated in the scene (readonly, never None)

      :type: :class:`Collection`

   .. attribute:: compositing_node_group

      Compositor Nodes

      :type: :class:`NodeTree` | None

   .. data:: cursor

      (readonly, never None)

      :type: :class:`View3DCursor`

   .. data:: display

      Scene display settings for 3D viewport (readonly)

      :type: :class:`SceneDisplay` | None

   .. data:: display_settings

      Settings of device saved image would be displayed on (readonly)

      :type: :class:`ColorManagedDisplaySettings` | None

   .. data:: eevee

      EEVEE settings for the scene (readonly)

      :type: :class:`SceneEEVEE` | None

   .. attribute:: frame_current

      Current frame, to update animation data from Python frame_set() instead (in [-1048574, 1048574], default 1)

      :type: int

   .. data:: frame_current_final

      Current frame with subframe and time remapping applied (in [-1.04857e+06, 1.04857e+06], default 0.0, readonly)

      :type: float

   .. attribute:: frame_end

      Final frame of the playback/rendering range (in [0, 1048574], default 250)

      :type: int

   .. attribute:: frame_float

      (in [-1.04857e+06, 1.04857e+06], default 0.0)

      :type: float

   .. attribute:: frame_preview_end

      Alternative end frame for UI playback (in [-inf, inf], default 0)

      :type: int

   .. attribute:: frame_preview_start

      Alternative start frame for UI playback (in [-inf, inf], default 0)

      :type: int

   .. attribute:: frame_start

      First frame of the playback/rendering range (in [0, 1048574], default 1)

      :type: int

   .. attribute:: frame_step

      Number of frames to skip forward while rendering/playing back each frame (in [0, 1048574], default 1)

      :type: int

   .. attribute:: frame_subframe

      (in [0, 1], default 0.0)

      :type: float

   .. attribute:: gravity

      Constant acceleration in a given direction (array of 3 items, in [-inf, inf], default (0.0, 0.0, -9.81))

      :type: :class:`mathutils.Vector`

   .. data:: grease_pencil_settings

      Grease Pencil settings for the scene (readonly)

      :type: :class:`SceneGpencil` | None

   .. data:: hydra

      Hydra settings for the scene (readonly)

      :type: :class:`SceneHydra` | None

   .. data:: is_nla_tweakmode

      Whether there is any action referenced by NLA being edited (strictly read-only) (default False, readonly)

      :type: bool

   .. data:: keying_sets

      Absolute Keying Sets for this Scene (default None, readonly)

      :type: :class:`KeyingSets`\ [:class:`KeyingSet`]

   .. data:: keying_sets_all

      All Keying Sets available for use (Builtins and Absolute Keying Sets for this Scene) (default None, readonly)

      :type: :class:`KeyingSetsAll`\ [:class:`KeyingSet`]

   .. attribute:: lock_frame_selection_to_range

      Don't allow frame to be selected with mouse outside of frame range (default False)

      :type: bool

   .. data:: objects

      (default None, readonly)

      :type: :class:`SceneObjects`\ [:class:`Object`]

   .. data:: render

      (readonly, never None)

      :type: :class:`RenderSettings`

   .. data:: rigidbody_world

      (readonly)

      :type: :class:`RigidBodyWorld` | None

   .. data:: safe_areas

      (readonly, never None)

      :type: :class:`DisplaySafeAreas`

   .. data:: sequence_editor

      (readonly)

      :type: :class:`SequenceEditor` | None

   .. data:: sequencer_colorspace_settings

      Settings of color space sequencer is working in (readonly)

      :type: :class:`ColorManagedSequencerColorspaceSettings` | None

   .. attribute:: show_keys_from_selected_only

      Only include channels relating to selected objects and data (default True)

      :type: bool

   .. attribute:: show_subframe

      Display and allow setting fractional frame values for the current frame (default False)

      :type: bool

   .. attribute:: simulation_frame_end

      Frame at which simulations end (in [-inf, inf], default 250)

      :type: int

   .. attribute:: simulation_frame_start

      Frame at which simulations start (in [-inf, inf], default 1)

      :type: int

   .. attribute:: sync_mode

      How to sync playback (default ``'AUDIO_SYNC'``)

      - ``NONE``
        Play Every Frame -- Do not sync, play every frame.
      - ``FRAME_DROP``
        Frame Dropping -- Drop frames if playback is too slow.
      - ``AUDIO_SYNC``
        Sync to Audio -- Sync to audio playback, dropping frames.

      :type: Literal['NONE', 'FRAME_DROP', 'AUDIO_SYNC']

   .. attribute:: time_jump_delta

      Number of frames or seconds to jump forward or backward (in [0.1, inf], default 1.0)

      :type: float

   .. attribute:: time_jump_unit

      Which unit to use for time jumps in the timeline (default ``'SECOND'``)

      - ``FRAME``
        Frame -- Jump by frames.
      - ``SECOND``
        Second -- Jump by seconds.

      :type: Literal['FRAME', 'SECOND']

   .. data:: timeline_markers

      Markers used in all timelines for the current scene (default None, readonly)

      :type: :class:`TimelineMarkers`\ [:class:`TimelineMarker`]

   .. data:: tool_settings

      (readonly, never None)

      :type: :class:`ToolSettings`

   .. data:: transform_orientation_slots

      (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`TransformOrientationSlot`]

   .. data:: unit_settings

      Unit editing settings (readonly, never None)

      :type: :class:`UnitSettings`

   .. attribute:: use_audio

      Play back of audio from Sequence Editor, otherwise mute audio (default False)

      :type: bool

   .. attribute:: use_audio_scrub

      Play audio from Sequence Editor while scrubbing (default False)

      :type: bool

   .. attribute:: use_custom_simulation_range

      Use a simulation range that is different from the scene range for simulation nodes that don't override the frame range themselves (default False)

      :type: bool

   .. attribute:: use_gravity

      Use global gravity for all dynamics (default True)

      :type: bool

   .. attribute:: use_nodes

      Enable the compositing node group. (default False)

      .. deprecated:: 5.0 removal planned in version 6.0

         Unused but kept for compatibility reasons. Setting the property has no effect, and getting it always returns True. Use #scene.render.use_compositing to turn compositing to enable or disable compositing.

      :type: bool

   .. attribute:: use_preview_range

      Use an alternative start/end frame range for animation playback and view renders (default False)

      :type: bool

   .. attribute:: use_stamp_note

      User defined note for the render stamping (default "", never None)

      :type: str

   .. data:: view_layers

      (default None, readonly)

      :type: :class:`ViewLayers`\ [:class:`ViewLayer`]

   .. data:: view_settings

      Color management settings applied on image before saving (readonly)

      :type: :class:`ColorManagedViewSettings` | None

   .. attribute:: world

      World used for rendering the scene

      :type: :class:`World` | None

   .. classmethod:: update_render_engine()

      Trigger a render engine update


   .. method:: statistics(view_layer)

      statistics

      :param view_layer: View Layer, (never None)
      :type view_layer: :class:`ViewLayer` | None
      :return: Statistics, (never None)
      :rtype: str

   .. method:: frame_set(frame, *, subframe=0.0)

      Set scene frame updating all objects and view layers immediately

      :param frame: Frame number to set (in [-1048574, 1048574])
      :type frame: int
      :param subframe: Subframe time, between 0.0 and 1.0 (in [0, 1], optional)
      :type subframe: float

   .. method:: uvedit_aspect(object)

      Get uv aspect for current object

      :param object: Object (never None)
      :type object: :class:`Object` | None
      :return: aspect (array of 2 items, in [0, inf])
      :rtype: :class:`mathutils.Vector`

   .. method:: ray_cast(depsgraph, origin, direction, *, distance=1.70141e+38)

      Cast a ray onto evaluated geometry in world-space

      :param depsgraph: The current dependency graph (never None)
      :type depsgraph: :class:`Depsgraph` | None
      :param origin: (array of 3 items, in [-inf, inf])
      :type origin: :class:`mathutils.Vector` | Sequence[float]
      :param direction: (array of 3 items, in [-inf, inf])
      :type direction: :class:`mathutils.Vector` | Sequence[float]
      :param distance: Maximum distance (in [0, inf], optional)
      :type distance: float
      :return:
         ``result``, bool

         ``location``, The hit location of this ray cast, :class:`mathutils.Vector`

         ``normal``, The face normal at the ray cast hit location, :class:`mathutils.Vector`

         ``index``, The face index, -1 when original data isn't available, int

         ``object``, Ray cast object, :class:`Object`

         ``matrix``, Matrix, :class:`mathutils.Matrix`

      :rtype: tuple[bool, :class:`mathutils.Vector`, :class:`mathutils.Vector`, int, :class:`Object`, :class:`mathutils.Matrix`]

   .. method:: sequence_editor_create()

      Ensure sequence editor is valid in this scene

      :return: New sequence editor data or None
      :rtype: :class:`SequenceEditor`

   .. method:: sequence_editor_clear()

      Clear sequence editor in this scene


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
   - :class:`ID.name`
   - :class:`ID.name_full`
   - :class:`ID.id_type`
   - :class:`ID.session_uid`
   - :class:`ID.is_evaluated`
   - :class:`ID.original`
   - :class:`ID.users`
   - :class:`ID.use_fake_user`
   - :class:`ID.use_extra_user`
   - :class:`ID.is_embedded_data`
   - :class:`ID.is_linked_packed`
   - :class:`ID.is_missing`
   - :class:`ID.is_runtime_data`
   - :class:`ID.is_editable`
   - :class:`ID.tag`
   - :class:`ID.is_library_indirect`
   - :class:`ID.library`
   - :class:`ID.library_weak_reference`
   - :class:`ID.asset_data`
   - :class:`ID.override_library`
   - :class:`ID.preview`

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
   - :class:`ID.bl_system_properties_get`
   - :class:`ID.rename`
   - :class:`ID.evaluated_get`
   - :class:`ID.copy`
   - :class:`ID.asset_mark`
   - :class:`ID.asset_clear`
   - :class:`ID.asset_generate_preview`
   - :class:`ID.override_create`
   - :class:`ID.override_hierarchy_create`
   - :class:`ID.user_clear`
   - :class:`ID.user_remap`
   - :class:`ID.make_local`
   - :class:`ID.user_of_id`
   - :class:`ID.animation_data_create`
   - :class:`ID.animation_data_clear`
   - :class:`ID.update_tag`
   - :class:`ID.preview_ensure`
   - :class:`ID.bl_rna_get_subclass`
   - :class:`ID.bl_rna_get_subclass_py`

References
----------

.. hlist::
   :columns: 2

   - :mod:`bpy.context.scene`
   - :mod:`bpy.context.sequencer_scene`
   - :class:`BlendData.scenes`
   - :class:`BlendDataScenes.new`
   - :class:`BlendDataScenes.remove`
   - :class:`Camera.view_frame`
   - :class:`CompositorNodeCryptomatteV2.scene`
   - :class:`CompositorNodeDefocus.scene`
   - :class:`CompositorNodeRLayers.scene`
   - :class:`Context.scene`
   - :class:`Depsgraph.scene`
   - :class:`Depsgraph.scene_eval`
   - :class:`ID.override_hierarchy_create`
   - :class:`IDOverrideLibrary.resync`
   - :class:`Image.save_render`
   - :class:`NodeSocketScene.default_value`
   - :class:`NodeTreeInterfaceSocketScene.default_value`
   - :class:`Object.crazyspace_eval`
   - :class:`Object.is_deform_modified`
   - :class:`Object.is_modified`
   - :class:`RenderEngine.bind_display_space_shader`
   - :class:`RenderEngine.get_preview_pixel_size`
   - :class:`RenderEngine.register_pass`
   - :class:`RenderEngine.support_display_space_shader`
   - :class:`RenderEngine.update_render_passes`
   - :class:`Scene.background_set`
   - :class:`SceneStrip.scene`
   - :class:`StripsMeta.new_scene`
   - :class:`StripsTopLevel.new_scene`
   - :class:`Window.find_playing_scene`
   - :class:`Window.scene`
   - :class:`WorkSpace.sequencer_scene`

