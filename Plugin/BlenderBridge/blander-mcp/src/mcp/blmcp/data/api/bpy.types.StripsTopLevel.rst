StripsTopLevel(bpy_prop_collection)
===================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_prop`, :class:`bpy_prop_collection`

.. class:: StripsTopLevel(bpy_prop_collection)

   Collection of Strips

   .. method:: new_clip(name, clip, channel, frame_start)

      Add a new movie clip strip

      :param name: Name for the new strip (never None)
      :type name: str
      :param clip: Movie clip to add (never None)
      :type clip: :class:`MovieClip` | None
      :param channel: Channel, The channel for the new strip (in [1, 128])
      :type channel: int
      :param frame_start: The start frame for the new strip (in [-1048574, 1048574])
      :type frame_start: int
      :return: New Strip
      :rtype: :class:`Strip`

   .. method:: new_mask(name, mask, channel, frame_start)

      Add a new mask strip

      :param name: Name for the new strip (never None)
      :type name: str
      :param mask: Mask to add (never None)
      :type mask: :class:`Mask` | None
      :param channel: Channel, The channel for the new strip (in [1, 128])
      :type channel: int
      :param frame_start: The start frame for the new strip (in [-1048574, 1048574])
      :type frame_start: int
      :return: New Strip
      :rtype: :class:`Strip`

   .. method:: new_scene(name, scene, channel, frame_start)

      Add a new scene strip

      :param name: Name for the new strip (never None)
      :type name: str
      :param scene: Scene to add (never None)
      :type scene: :class:`Scene` | None
      :param channel: Channel, The channel for the new strip (in [1, 128])
      :type channel: int
      :param frame_start: The start frame for the new strip (in [-1048574, 1048574])
      :type frame_start: int
      :return: New Strip
      :rtype: :class:`Strip`

   .. method:: new_image(name, filepath, channel, frame_start, *, fit_method='ORIGINAL')

      Add a new image strip

      :param name: Name for the new strip (never None)
      :type name: str
      :param filepath: Filepath to image (never None)
      :type filepath: str
      :param channel: Channel, The channel for the new strip (in [1, 128])
      :type channel: int
      :param frame_start: The start frame for the new strip (in [-1048574, 1048574])
      :type frame_start: int
      :param fit_method: Image Fit Method, (optional)
      :type fit_method: Literal[:ref:`rna_enum_strip_scale_method_items`]
      :return: New Strip
      :rtype: :class:`Strip`

   .. method:: new_movie(name, filepath, channel, frame_start, *, fit_method='ORIGINAL')

      Add a new movie strip

      :param name: Name for the new strip (never None)
      :type name: str
      :param filepath: Filepath to movie (never None)
      :type filepath: str
      :param channel: Channel, The channel for the new strip (in [1, 128])
      :type channel: int
      :param frame_start: The start frame for the new strip (in [-1048574, 1048574])
      :type frame_start: int
      :param fit_method: Image Fit Method, (optional)
      :type fit_method: Literal[:ref:`rna_enum_strip_scale_method_items`]
      :return: New Strip
      :rtype: :class:`Strip`

   .. method:: new_sound(name, filepath, channel, frame_start)

      Add a new sound strip

      :param name: Name for the new strip (never None)
      :type name: str
      :param filepath: Filepath to movie (never None)
      :type filepath: str
      :param channel: Channel, The channel for the new strip (in [1, 128])
      :type channel: int
      :param frame_start: The start frame for the new strip (in [-1048574, 1048574])
      :type frame_start: int
      :return: New Strip
      :rtype: :class:`Strip`

   .. method:: new_meta(name, channel, frame_start)

      Add a new meta strip

      :param name: Name for the new strip (never None)
      :type name: str
      :param channel: Channel, The channel for the new strip (in [1, 128])
      :type channel: int
      :param frame_start: The start frame for the new strip (in [-1048574, 1048574])
      :type frame_start: int
      :return: New Strip
      :rtype: :class:`Strip`

   .. method:: new_effect(name, type, channel, frame_start, *, length=0, input1=None, input2=None)

      Add a new effect strip

      :param name: Name for the new strip (never None)
      :type name: str
      :param type: Type, type for the new strip

         - ``CROSS``
           Crossfade -- Fade out of one video, fading into another.
         - ``ADD``
           Add -- Add together color channels from two videos.
         - ``SUBTRACT``
           Subtract -- Subtract one strip's color from another.
         - ``ALPHA_OVER``
           Alpha Over -- Blend alpha on top of another video.
         - ``ALPHA_UNDER``
           Alpha Under -- Blend alpha below another video.
         - ``GAMMA_CROSS``
           Gamma Crossfade -- Crossfade with color correction.
         - ``MULTIPLY``
           Multiply -- Multiply color channels from two videos.
         - ``WIPE``
           Wipe -- Sweep a transition line across the frame.
         - ``GLOW``
           Glow -- Add blur and brightness to light areas.
         - ``COLOR``
           Color -- Add a simple color strip.
         - ``SPEED``
           Speed -- Timewarp video strips, modifying playback speed.
         - ``MULTICAM``
           Multicam Selector -- Control active camera angles.
         - ``ADJUSTMENT``
           Adjustment Layer -- Apply nondestructive effects.
         - ``GAUSSIAN_BLUR``
           Gaussian Blur -- Soften details along axes.
         - ``TEXT``
           Text -- Add a simple text strip.
         - ``COLORMIX``
           Color Mix -- Combine two strips using blend modes.
      :type type: Literal['CROSS', 'ADD', 'SUBTRACT', 'ALPHA_OVER', 'ALPHA_UNDER', 'GAMMA_CROSS', 'MULTIPLY', 'WIPE', 'GLOW', 'COLOR', 'SPEED', 'MULTICAM', 'ADJUSTMENT', 'GAUSSIAN_BLUR', 'TEXT', 'COLORMIX']
      :param channel: Channel, The channel for the new strip (in [1, 128])
      :type channel: int
      :param frame_start: The start frame for the new strip (in [-inf, inf])
      :type frame_start: int
      :param length: Length of the strip in frames, or the length of each strip if multiple are added (in [-inf, inf], optional)
      :type length: int
      :param input1: First input strip for effect (optional)
      :type input1: :class:`Strip` | None
      :param input2: Second input strip for effect (optional)
      :type input2: :class:`Strip` | None
      :return: New Strip
      :rtype: :class:`Strip`

   .. method:: remove(sequence)

      Remove a Strip

      :param sequence: Strip to remove (never None)
      :type sequence: :class:`Strip` | None

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

   - :class:`SequenceEditor.strips`

