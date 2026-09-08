RenderEngine(bpy_struct)
========================

.. currentmodule:: bpy.types


Simple Render Engine
++++++++++++++++++++

.. literalinclude:: ./examples/bpy.types.RenderEngine.1.py
   :lines: 6-


GPU Render Engine
+++++++++++++++++

.. literalinclude:: ./examples/bpy.types.RenderEngine.2.py
   :lines: 6-

base class --- :class:`bpy_struct`

subclasses --- 
:class:`HydraRenderEngine`

.. class:: RenderEngine(bpy_struct)

   Render engine

   .. attribute:: bl_idname

      (default "", never None)

      :type: str

   .. attribute:: bl_label

      (default "", never None)

      :type: str

   .. attribute:: bl_use_custom_freestyle

      Handles freestyle rendering on its own, instead of delegating it to EEVEE (default False)

      :type: bool

   .. attribute:: bl_use_eevee_viewport

      Uses EEVEE for viewport shading in Material Preview shading mode (default False)

      :type: bool

   .. attribute:: bl_use_gpu_context

      Enable OpenGL context for the render method, for engines that render using OpenGL (default False)

      :type: bool

   .. attribute:: bl_use_image_save

      Save images/movie to disk while rendering an animation. Disabling image saving is only supported when bl_use_postprocess is also disabled. (default True)

      :type: bool

   .. attribute:: bl_use_materialx

      Use MaterialX for exporting materials to Hydra (default False)

      :type: bool

   .. attribute:: bl_use_postprocess

      Apply compositing on render results (default False)

      :type: bool

   .. attribute:: bl_use_preview

      Render engine supports being used for rendering previews of materials, lights and worlds (default False)

      :type: bool

   .. attribute:: bl_use_shading_nodes_custom

      Don't expose Cycles and EEVEE shading nodes in the node editor user interface, so separate nodes can be used instead (default True)

      :type: bool

   .. attribute:: bl_use_spherical_stereo

      Support spherical stereo camera models (default False)

      :type: bool

   .. attribute:: bl_use_stereo_viewport

      Support rendering stereo 3D viewport (default False)

      :type: bool

   .. data:: camera_override

      (readonly)

      :type: :class:`Object` | None

   .. attribute:: is_animation

      (default False)

      :type: bool

   .. attribute:: is_preview

      (default False)

      :type: bool

   .. attribute:: layer_override

      (array of 20 items, default (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))

      :type: :class:`bpy_prop_array`\ [bool]

   .. data:: render
      :noindex:

      (readonly)

      :type: :class:`RenderSettings` | None

   .. data:: resolution_x

      (in [-inf, inf], default 0, readonly)

      :type: int

   .. data:: resolution_y

      (in [-inf, inf], default 0, readonly)

      :type: int

   .. data:: temporary_directory

      (default "", readonly, never None)

      :type: str

   .. attribute:: use_highlight_tiles

      (default False)

      :type: bool

   .. method:: update(*, data=None, depsgraph=None)

      Export scene data for render

      :param data: (optional)
      :type data: :class:`BlendData` | None
      :param depsgraph: (optional)
      :type depsgraph: :class:`Depsgraph` | None

   .. method:: render(depsgraph)

      Render scene into an image

      :type depsgraph: :class:`Depsgraph` | None

   .. method:: render_frame_finish()

      Perform finishing operations after all view layers in a frame were rendered


   .. method:: draw(context, depsgraph)

      Draw render image

      :type context: :class:`Context` | None
      :type depsgraph: :class:`Depsgraph` | None

   .. method:: bake(depsgraph, object, pass_type, pass_filter, width, height)

      Bake passes

      :type depsgraph: :class:`Depsgraph` | None
      :type object: :class:`Object` | None
      :param pass_type: Pass, Pass to bake
      :type pass_type: Literal[:ref:`rna_enum_bake_pass_type_items`]
      :param pass_filter: Pass Filter, Filter to combined, diffuse, glossy and transmission passes (in [0, inf])
      :type pass_filter: int
      :param width: Width, Image width (in [0, inf])
      :type width: int
      :param height: Height, Image height (in [0, inf])
      :type height: int

   .. method:: view_update(context, depsgraph)

      Update on data changes for viewport render

      :type context: :class:`Context` | None
      :type depsgraph: :class:`Depsgraph` | None

   .. method:: view_draw(context, depsgraph)

      Draw viewport render

      :type context: :class:`Context` | None
      :type depsgraph: :class:`Depsgraph` | None

   .. method:: update_script_node(*, node=None)

      Compile shader script node

      :param node: (optional)
      :type node: :class:`Node` | None

   .. method:: update_render_passes(*, scene=None, renderlayer=None)

      Update the render passes that will be generated

      :param scene: (optional)
      :type scene: :class:`Scene` | None
      :param renderlayer: (optional)
      :type renderlayer: :class:`ViewLayer` | None

   .. method:: update_custom_camera(*, cam=None)

      Compile custom camera

      :param cam: (optional)
      :type cam: :class:`Camera` | None

   .. method:: tag_redraw()

      Request redraw for viewport rendering


   .. method:: tag_update()

      Request update call for viewport rendering


   .. method:: begin_result(x, y, w, h, *, layer="", view="")

      Create render result to write linear floating-point render layers and passes

      :param x: X, (in [0, inf])
      :type x: int
      :param y: Y, (in [0, inf])
      :type y: int
      :param w: Width, (in [0, inf])
      :type w: int
      :param h: Height, (in [0, inf])
      :type h: int
      :param layer: Layer, Single layer to get render result for (optional, never None)
      :type layer: str
      :param view: View, Single view to get render result for (optional, never None)
      :type view: str
      :return: Result
      :rtype: :class:`RenderResult`

   .. method:: update_result(result)

      Signal that pixels have been updated and can be redrawn in the user interface

      :param result: Result
      :type result: :class:`RenderResult` | None

   .. method:: end_result(result, *, cancel=False, highlight=False, do_merge_results=False)

      All pixels in the render result have been set and are final

      :param result: Result
      :type result: :class:`RenderResult` | None
      :param cancel: Cancel, Don't mark tile as done, don't merge results unless forced (optional)
      :type cancel: bool
      :param highlight: Highlight, Don't mark tile as done yet (optional)
      :type highlight: bool
      :param do_merge_results: Merge Results, Merge results even if cancel=true (optional)
      :type do_merge_results: bool

   .. method:: add_pass(name, channels, chan_id, *, layer="")

      Add a pass to the render layer

      :param name: Name, Name of the Pass, without view or channel tag (never None)
      :type name: str
      :param channels: Channels, (in [0, inf])
      :type channels: int
      :param chan_id: Channel IDs, Channel names, one character per channel (never None)
      :type chan_id: str
      :param layer: Layer, Single layer to add render pass to (optional, never None)
      :type layer: str

   .. method:: get_result()

      Get final result for non-pixel operations

      :return: Result
      :rtype: :class:`RenderResult`

   .. method:: test_break()

      Test if the render operation should been canceled, this is a fast call that should be used regularly for responsiveness

      :return: Break
      :rtype: bool

   .. method:: pass_by_index_get(layer, index)

      pass_by_index_get

      :param layer: Layer, Name of render layer to get pass for (never None)
      :type layer: str
      :param index: Index, Index of pass to get (in [0, inf])
      :type index: int
      :return: Index, Index of pass to get
      :rtype: :class:`RenderPass`

   .. method:: active_view_get()

      active_view_get

      :return: View, Single view active (never None)
      :rtype: str

   .. method:: active_view_set(view)

      active_view_set

      :param view: View, Single view to set as active (never None)
      :type view: str

   .. method:: camera_shift_x(camera, *, use_spherical_stereo=False)

      camera_shift_x

      :type camera: :class:`Object` | None
      :param use_spherical_stereo: Spherical Stereo, (optional)
      :type use_spherical_stereo: bool
      :return: Shift X, (in [0, inf])
      :rtype: float

   .. method:: camera_model_matrix(camera, *, use_spherical_stereo=False)

      camera_model_matrix

      :type camera: :class:`Object` | None
      :param use_spherical_stereo: Spherical Stereo, (optional)
      :type use_spherical_stereo: bool
      :return: Model Matrix, Normalized camera model matrix (multi-dimensional array of 4 * 4 items, in [-inf, inf])
      :rtype: :class:`mathutils.Matrix`

   .. method:: use_spherical_stereo(camera)

      use_spherical_stereo

      :type camera: :class:`Object` | None
      :return: Spherical Stereo
      :rtype: bool

   .. method:: update_stats(stats, info)

      Update and signal to redraw render status text

      :param stats: Stats, (never None)
      :type stats: str
      :param info: Info, (never None)
      :type info: str

   .. method:: frame_set(frame, subframe)

      Evaluate scene at a different frame (for motion blur)

      :param frame: Frame, (in [-inf, inf])
      :type frame: int
      :param subframe: Subframe, (in [0, 1])
      :type subframe: float

   .. method:: update_progress(progress)

      Update progress percentage of render

      :param progress: Percentage of render that's done (in [0, 1])
      :type progress: float

   .. method:: update_memory_stats(*, memory_used=0.0, memory_peak=0.0)

      Update memory usage statistics

      :param memory_used: Current memory usage in megabytes (in [0, inf], optional)
      :type memory_used: float
      :param memory_peak: Peak memory usage in megabytes (in [0, inf], optional)
      :type memory_peak: float

   .. method:: report(type, message)

      Report info, warning or error messages

      :param type: Type
      :type type: set[Literal[:ref:`rna_enum_wm_report_items`]]
      :param message: Report Message, (never None)
      :type message: str

   .. method:: error_set(message)

      Set error message displaying after the render is finished

      :param message: Report Message, (never None)
      :type message: str

   .. method:: bind_display_space_shader(scene)

      Bind GLSL fragment shader that converts linear colors to display space colors using scene color management settings

      :type scene: :class:`Scene` | None

   .. method:: unbind_display_space_shader()

      Unbind GLSL display space shader, must always be called after binding the shader


   .. method:: support_display_space_shader(scene)

      Test if GLSL display space shader is supported for the combination of graphics card and scene settings

      :type scene: :class:`Scene` | None
      :return: Supported
      :rtype: bool

   .. method:: get_preview_pixel_size(scene)

      Get the pixel size that should be used for preview rendering

      :type scene: :class:`Scene` | None
      :return: Pixel Size, (in [1, 8])
      :rtype: int

   .. method:: free_blender_memory()

      Free Blender side memory of render engine


   .. method:: tile_highlight_set(x, y, width, height, highlight)

      Set highlighted state of the given tile

      :param x: X, (in [0, inf])
      :type x: int
      :param y: Y, (in [0, inf])
      :type y: int
      :param width: Width, (in [0, inf])
      :type width: int
      :param height: Height, (in [0, inf])
      :type height: int
      :param highlight: Highlight
      :type highlight: bool

   .. method:: tile_highlight_clear_all()

      The temp directory used by Blender


   .. method:: register_pass(scene, view_layer, name, channels, chanid, type)

      Register a render pass that will be part of the render with the current settings

      :type scene: :class:`Scene` | None
      :type view_layer: :class:`ViewLayer` | None
      :param name: Name, (never None)
      :type name: str
      :param channels: Channels, (in [1, 8])
      :type channels: int
      :param chanid: Channel IDs, (never None)
      :type chanid: str
      :param type: Type
      :type type: Literal['VALUE', 'VECTOR', 'COLOR']

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

