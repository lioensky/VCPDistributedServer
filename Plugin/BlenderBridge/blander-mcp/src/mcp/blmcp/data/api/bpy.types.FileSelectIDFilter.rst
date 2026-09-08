FileSelectIDFilter(bpy_struct)
==============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: FileSelectIDFilter(bpy_struct)

   Which ID types to show/hide, when browsing a library

   .. attribute:: category_animation

      Show animation data (default False)

      :type: bool

   .. attribute:: category_environment

      Show worlds, lights, cameras and speakers (default False)

      :type: bool

   .. attribute:: category_geometry

      Show meshes, curves, lattice, armatures and metaballs data (default False)

      :type: bool

   .. attribute:: category_image

      Show images, movie clips, sounds and masks (default False)

      :type: bool

   .. attribute:: category_misc

      Show other data types (default False)

      :type: bool

   .. attribute:: category_object

      Show objects and collections (default False)

      :type: bool

   .. attribute:: category_scene

      Show scenes (default False)

      :type: bool

   .. attribute:: category_shading

      Show materials, node-trees, textures and Freestyle's line-styles (default False)

      :type: bool

   .. attribute:: filter_action

      Show Action data-blocks (default False)

      :type: bool

   .. attribute:: filter_annotations

      Show Annotation data-blocks (default False)

      :type: bool

   .. attribute:: filter_armature

      Show Armature data-blocks (default False)

      :type: bool

   .. attribute:: filter_brush

      Show Brushes data-blocks (default False)

      :type: bool

   .. attribute:: filter_cachefile

      Show Cache File data-blocks (default False)

      :type: bool

   .. attribute:: filter_camera

      Show Camera data-blocks (default False)

      :type: bool

   .. attribute:: filter_curve

      Show Curve data-blocks (default False)

      :type: bool

   .. attribute:: filter_curves

      Show/hide Curves data-blocks (default False)

      :type: bool

   .. attribute:: filter_font

      Show Font data-blocks (default False)

      :type: bool

   .. attribute:: filter_grease_pencil

      Show Grease Pencil data-blocks (default False)

      :type: bool

   .. attribute:: filter_group

      Show Collection data-blocks (default False)

      :type: bool

   .. attribute:: filter_image

      Show Image data-blocks (default False)

      :type: bool

   .. attribute:: filter_lattice

      Show Lattice data-blocks (default False)

      :type: bool

   .. attribute:: filter_light

      Show Light data-blocks (default False)

      :type: bool

   .. attribute:: filter_light_probe

      Show Light Probe data-blocks (default False)

      :type: bool

   .. attribute:: filter_linestyle

      Show Freestyle's Line Style data-blocks (default False)

      :type: bool

   .. attribute:: filter_mask

      Show Mask data-blocks (default False)

      :type: bool

   .. attribute:: filter_material

      Show Material data-blocks (default False)

      :type: bool

   .. attribute:: filter_mesh

      Show Mesh data-blocks (default False)

      :type: bool

   .. attribute:: filter_metaball

      Show Metaball data-blocks (default False)

      :type: bool

   .. attribute:: filter_movie_clip

      Show Movie Clip data-blocks (default False)

      :type: bool

   .. attribute:: filter_node_tree

      Show Node Tree data-blocks (default False)

      :type: bool

   .. attribute:: filter_object

      Show Object data-blocks (default False)

      :type: bool

   .. attribute:: filter_paint_curve

      Show Paint Curve data-blocks (default False)

      :type: bool

   .. attribute:: filter_palette

      Show Palette data-blocks (default False)

      :type: bool

   .. attribute:: filter_particle_settings

      Show Particle Settings data-blocks (default False)

      :type: bool

   .. attribute:: filter_pointcloud

      Show/hide Point Cloud data-blocks (default False)

      :type: bool

   .. attribute:: filter_scene

      Show Scene data-blocks (default False)

      :type: bool

   .. attribute:: filter_sound

      Show Sound data-blocks (default False)

      :type: bool

   .. attribute:: filter_speaker

      Show Speaker data-blocks (default False)

      :type: bool

   .. attribute:: filter_text

      Show Text data-blocks (default False)

      :type: bool

   .. attribute:: filter_texture

      Show Texture data-blocks (default False)

      :type: bool

   .. attribute:: filter_volume

      Show/hide Volume data-blocks (default False)

      :type: bool

   .. attribute:: filter_work_space

      Show workspace data-blocks (default False)

      :type: bool

   .. attribute:: filter_world

      Show World data-blocks (default False)

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

   - :class:`FileSelectParams.filter_id`

