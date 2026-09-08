AnnotationLayer(bpy_struct)
===========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: AnnotationLayer(bpy_struct)

   Collection of related sketches

   .. data:: active_frame

      Frame currently being displayed for this layer (readonly)

      :type: :class:`AnnotationFrame` | None

   .. attribute:: annotation_hide

      Set annotation Visibility (default False)

      :type: bool

   .. attribute:: annotation_onion_after_color

      Base color for ghosts after the active frame (array of 3 items, in [0, 1], default (0.25, 0.1, 1.0))

      :type: :class:`mathutils.Color`

   .. attribute:: annotation_onion_after_range

      Maximum number of frames to show after current frame (in [-1, 120], default 0)

      :type: int

   .. attribute:: annotation_onion_before_color

      Base color for ghosts before the active frame (array of 3 items, in [0, 1], default (0.302, 0.851, 0.302))

      :type: :class:`mathutils.Color`

   .. attribute:: annotation_onion_before_range

      Maximum number of frames to show before current frame (in [-1, 120], default 0)

      :type: int

   .. attribute:: annotation_onion_use_custom_color

      Use custom colors for onion skinning instead of the theme (default False)

      :type: bool

   .. attribute:: annotation_opacity

      Annotation Layer Opacity (in [0, 1], default 0.0)

      :type: float

   .. attribute:: color

      Color for all strokes in this layer (array of 3 items, in [0, 1], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. data:: frames

      Sketches for this layer on different frames (default None, readonly)

      :type: :class:`AnnotationFrames`\ [:class:`AnnotationFrame`]

   .. attribute:: info

      Layer name (default "", never None)

      :type: str

   .. data:: is_ruler

      This is a special ruler layer (default False, readonly)

      :type: bool

   .. attribute:: lock

      Protect layer from further editing and/or frame changes (default False)

      :type: bool

   .. attribute:: lock_frame

      Lock current frame displayed by layer (default False)

      :type: bool

   .. attribute:: select

      Layer is selected for editing in the Dope Sheet (default False)

      :type: bool

   .. attribute:: show_in_front

      Make the layer display in front of objects (default True)

      :type: bool

   .. attribute:: thickness

      Thickness of annotation strokes (in [1, 10], default 0)

      :type: int

   .. attribute:: use_annotation_onion_skinning

      Display annotation onion skins before and after the current frame (default False)

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

   - :mod:`bpy.context.active_annotation_layer`
   - :class:`Annotation.layers`
   - :class:`AnnotationLayers.new`
   - :class:`AnnotationLayers.remove`

