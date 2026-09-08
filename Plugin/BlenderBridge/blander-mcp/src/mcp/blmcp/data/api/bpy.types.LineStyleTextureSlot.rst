LineStyleTextureSlot(TextureSlot)
=================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`TextureSlot`

.. class:: LineStyleTextureSlot(TextureSlot)

   Texture slot for textures in a LineStyle data-block

   .. attribute:: alpha_factor

      Amount texture affects alpha (in [-inf, inf], default 1.0)

      :type: float

   .. attribute:: diffuse_color_factor

      Amount texture affects diffuse color (in [-inf, inf], default 1.0)

      :type: float

   .. attribute:: mapping

      (default ``'FLAT'``)

      - ``FLAT``
        Flat -- Map X and Y coordinates directly.
      - ``CUBE``
        Cube -- Map using the normal vector.
      - ``TUBE``
        Tube -- Map with Z as central axis.
      - ``SPHERE``
        Sphere -- Map with Z as central axis.

      :type: Literal['FLAT', 'CUBE', 'TUBE', 'SPHERE']

   .. attribute:: mapping_x

      (default ``'X'``)

      :type: Literal['NONE', 'X', 'Y', 'Z']

   .. attribute:: mapping_y

      (default ``'Y'``)

      :type: Literal['NONE', 'X', 'Y', 'Z']

   .. attribute:: mapping_z

      (default ``'Z'``)

      :type: Literal['NONE', 'X', 'Y', 'Z']

   .. attribute:: texture_coords

      Texture coordinates used to map the texture onto the background (default ``'ALONG_STROKE'``)

      - ``WINDOW``
        Window -- Use screen coordinates as texture coordinates.
      - ``GLOBAL``
        Global -- Use global coordinates for the texture coordinates.
      - ``ALONG_STROKE``
        Along stroke -- Use stroke length for texture coordinates.
      - ``ORCO``
        Generated -- Use the original undeformed coordinates of the object.

      :type: Literal['WINDOW', 'GLOBAL', 'ALONG_STROKE', 'ORCO']

   .. attribute:: use_map_alpha

      The texture affects the alpha value (default False)

      :type: bool

   .. attribute:: use_map_color_diffuse

      The texture affects basic color of the stroke (default True)

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
   - :class:`TextureSlot.texture`
   - :class:`TextureSlot.name`
   - :class:`TextureSlot.offset`
   - :class:`TextureSlot.scale`
   - :class:`TextureSlot.color`
   - :class:`TextureSlot.blend_type`
   - :class:`TextureSlot.default_value`
   - :class:`TextureSlot.output_node`

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
   - :class:`TextureSlot.bl_rna_get_subclass`
   - :class:`TextureSlot.bl_rna_get_subclass_py`

References
----------

.. hlist::
   :columns: 2

   - :class:`FreestyleLineStyle.texture_slots`
   - :class:`LineStyleTextureSlots.add`
   - :class:`LineStyleTextureSlots.create`

