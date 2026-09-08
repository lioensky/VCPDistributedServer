BakeSettings(bpy_struct)
========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: BakeSettings(bpy_struct)

   Bake data for a Scene data-block

   .. attribute:: cage_extrusion

      Inflate the active object by the specified distance for baking. This helps matching to points nearer to the outside of the selected object meshes. (in [0, inf], default 0.0)

      :type: float

   .. attribute:: cage_object

      Object to use as cage instead of calculating the cage from the active object with cage extrusion

      :type: :class:`Object` | None

   .. attribute:: displacement_space

      Choose displacement space for baking (default ``'OBJECT'``)

      - ``OBJECT``
        Object -- Bake the displacement in object space.
      - ``TANGENT``
        Tangent -- Bake the displacement in tangent space.

      :type: Literal['OBJECT', 'TANGENT']

   .. attribute:: filepath

      Image filepath to use when saving externally (default "", never None, blend relative ``//`` prefix supported)

      :type: str

   .. attribute:: height

      Vertical dimension of the baking map (in [4, 10000], default 512)

      :type: int

   .. data:: image_settings

      (readonly, never None)

      :type: :class:`ImageFormatSettings`

   .. attribute:: margin

      Extends the baked result as a post process filter (in [0, 32767], default 16)

      :type: int

   .. attribute:: margin_type

      Algorithm to extend the baked result (default ``'ADJACENT_FACES'``)

      :type: Literal[:ref:`rna_enum_bake_margin_type_items`]

   .. attribute:: max_ray_distance

      The maximum ray distance for matching points between the active and selected objects. If zero, there is no limit. (in [0, inf], default 0.0)

      :type: float

   .. attribute:: normal_b

      Axis to bake in blue channel (default ``'POS_X'``)

      :type: Literal[:ref:`rna_enum_normal_swizzle_items`]

   .. attribute:: normal_g

      Axis to bake in green channel (default ``'POS_X'``)

      :type: Literal[:ref:`rna_enum_normal_swizzle_items`]

   .. attribute:: normal_r

      Axis to bake in red channel (default ``'POS_X'``)

      :type: Literal[:ref:`rna_enum_normal_swizzle_items`]

   .. attribute:: normal_space

      Choose normal space for baking (default ``'TANGENT'``)

      :type: Literal[:ref:`rna_enum_normal_space_items`]

   .. data:: pass_filter

      Passes to include in the active baking pass (default {``'COLOR'``, ``'DIFFUSE'``, ``'DIRECT'``, ``'EMIT'``, ``'GLOSSY'``, ``'INDIRECT'``, ``'TRANSMISSION'``}, readonly)

      :type: set[Literal[:ref:`rna_enum_bake_pass_filter_type_items`]]

   .. attribute:: save_mode

      Where to save baked image textures (default ``'INTERNAL'``)

      :type: Literal[:ref:`rna_enum_bake_save_mode_items`]

   .. attribute:: target

      Where to output the baked map (default ``'IMAGE_TEXTURES'``)

      :type: Literal[:ref:`rna_enum_bake_target_items`]

   .. attribute:: type

      Choose shading information to bake into the image (default ``'NORMALS'``)

      - ``NORMALS``
        Normals -- Bake normals.
      - ``DISPLACEMENT``
        Displacement -- Bake displacement.
      - ``VECTOR_DISPLACEMENT``
        Vector Displacement -- Bake vector displacement.

      :type: Literal['NORMALS', 'DISPLACEMENT', 'VECTOR_DISPLACEMENT']

   .. attribute:: use_automatic_name

      Automatically name the output file with the pass type (external only) (default False)

      :type: bool

   .. attribute:: use_cage

      Cast rays to active object from a cage (default False)

      :type: bool

   .. attribute:: use_clear

      Clear Images before baking (internal only) (default True)

      :type: bool

   .. attribute:: use_lores_mesh

      Calculate heights against unsubdivided low resolution mesh (default False)

      :type: bool

   .. attribute:: use_multires

      Bake directly from multires object (default False)

      :type: bool

   .. attribute:: use_pass_color

      Color the pass (default True)

      :type: bool

   .. attribute:: use_pass_diffuse

      Add diffuse contribution (default True)

      :type: bool

   .. attribute:: use_pass_direct

      Add direct lighting contribution (default True)

      :type: bool

   .. attribute:: use_pass_emit

      Add emission contribution (default True)

      :type: bool

   .. attribute:: use_pass_glossy

      Add glossy contribution (default True)

      :type: bool

   .. attribute:: use_pass_indirect

      Add indirect lighting contribution (default True)

      :type: bool

   .. attribute:: use_pass_transmission

      Add transmission contribution (default True)

      :type: bool

   .. attribute:: use_selected_to_active

      Bake shading on the surface of selected objects to the active object (default False)

      :type: bool

   .. attribute:: use_split_materials

      Split external images per material (external only) (default False)

      :type: bool

   .. attribute:: view_from

      Source of reflection ray directions (default ``'ABOVE_SURFACE'``)

      - ``ABOVE_SURFACE``
        Above Surface -- Cast rays from above the surface.
      - ``ACTIVE_CAMERA``
        Active Camera -- Use the active camera's position to cast rays.

      :type: Literal['ABOVE_SURFACE', 'ACTIVE_CAMERA']

   .. attribute:: width

      Horizontal dimension of the baking map (in [4, 10000], default 512)

      :type: int

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

   - :class:`RenderSettings.bake`

