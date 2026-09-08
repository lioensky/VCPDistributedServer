Import Scene Operators
======================

.. module:: bpy.ops.import_scene

.. function:: fbx(*, filepath="", directory="", filter_glob="*.fbx", files=None, ui_tab='MAIN', use_manual_orientation=False, global_scale=1.0, bake_space_transform=False, use_custom_normals=True, colors_type='SRGB', use_image_search=True, use_alpha_decals=False, decal_offset=0.0, use_anim=True, anim_offset=1.0, use_subsurf=False, use_custom_props=True, use_custom_props_enum_as_string=True, ignore_leaf_bones=False, force_connect_children=False, automatic_bone_orientation=False, primary_bone_axis='Y', secondary_bone_axis='X', use_prepost_rot=True, mtl_name_collision_mode='MAKE_UNIQUE', axis_forward='-Z', axis_up='Y')

   Load a FBX file

   :param filepath: File Path, Filepath used for importing the file (optional, never None)
   :type filepath: str
   :param directory: directory, (optional, never None)
   :type directory: str
   :param filter_glob: filter_glob, (optional, never None)
   :type filter_glob: str
   :param files: File Path, (optional)
   :type files: :class:`bpy_prop_collection`\ [:class:`OperatorFileListElement`] | None
   :param ui_tab: ui_tab, Import options categories (optional)

      - ``MAIN``
        Main -- Main basic settings.
      - ``ARMATURE``
        Armatures -- Armature-related settings.
   :type ui_tab: Literal['MAIN', 'ARMATURE']
   :param use_manual_orientation: Manual Orientation, Specify orientation and scale, instead of using embedded data in FBX file (optional)
   :type use_manual_orientation: bool
   :param global_scale: Scale, (in [0.001, 1000], optional)
   :type global_scale: float
   :param bake_space_transform: Apply Transform, Bake space transform into object data, avoids getting unwanted rotations to objects when target space is not aligned with Blender's space (WARNING! experimental option, use at own risk, known to be broken with armatures/animations) (optional)
   :type bake_space_transform: bool
   :param use_custom_normals: Custom Normals, Import custom normals, if available (otherwise Blender will recompute them) (optional)
   :type use_custom_normals: bool
   :param colors_type: Vertex Colors, Import vertex color attributes (optional)

      - ``NONE``
        None -- Do not import color attributes.
      - ``SRGB``
        sRGB -- Expect file colors in sRGB color space.
      - ``LINEAR``
        Linear -- Expect file colors in linear color space.
   :type colors_type: Literal['NONE', 'SRGB', 'LINEAR']
   :param use_image_search: Image Search, Search subdirs for any associated images (WARNING: may be slow) (optional)
   :type use_image_search: bool
   :param use_alpha_decals: Alpha Decals, Treat materials with alpha as decals (no shadow casting) (optional)
   :type use_alpha_decals: bool
   :param decal_offset: Decal Offset, Displace geometry of alpha meshes (in [0, 1], optional)
   :type decal_offset: float
   :param use_anim: Import Animation, Import FBX animation (optional)
   :type use_anim: bool
   :param anim_offset: Animation Offset, Offset to apply to animation during import, in frames (in [-inf, inf], optional)
   :type anim_offset: float
   :param use_subsurf: Subdivision Data, Import FBX subdivision information as subdivision surface modifiers (optional)
   :type use_subsurf: bool
   :param use_custom_props: Custom Properties, Import user properties as custom properties (optional)
   :type use_custom_props: bool
   :param use_custom_props_enum_as_string: Import Enums As Strings, Store enumeration values as strings (optional)
   :type use_custom_props_enum_as_string: bool
   :param ignore_leaf_bones: Ignore Leaf Bones, Ignore the last bone at the end of each chain (used to mark the length of the previous bone) (optional)
   :type ignore_leaf_bones: bool
   :param force_connect_children: Force Connect Children, Force connection of children bones to their parent, even if their computed head/tail positions do not match (can be useful with pure-joints-type armatures) (optional)
   :type force_connect_children: bool
   :param automatic_bone_orientation: Automatic Bone Orientation, Try to align the major bone axis with the bone children (optional)
   :type automatic_bone_orientation: bool
   :param primary_bone_axis: Primary Bone Axis, (optional)
   :type primary_bone_axis: Literal['X', 'Y', 'Z', '-X', '-Y', '-Z']
   :param secondary_bone_axis: Secondary Bone Axis, (optional)
   :type secondary_bone_axis: Literal['X', 'Y', 'Z', '-X', '-Y', '-Z']
   :param use_prepost_rot: Use Pre/Post Rotation, Use pre/post rotation from FBX transform (you may have to disable that in some cases) (optional)
   :type use_prepost_rot: bool
   :param mtl_name_collision_mode: Material Name Collision, Behavior when the name of an imported material conflicts with an existing material (optional)

      - ``MAKE_UNIQUE``
        Make Unique -- Import each FBX material as a unique Blender material.
      - ``REFERENCE_EXISTING``
        Reference Existing -- If a material with the same name already exists, reference that instead of importing.
   :type mtl_name_collision_mode: Literal['MAKE_UNIQUE', 'REFERENCE_EXISTING']
   :param axis_forward: Forward, (optional)
   :type axis_forward: Literal['X', 'Y', 'Z', '-X', '-Y', '-Z']
   :param axis_up: Up, (optional)
   :type axis_up: Literal['X', 'Y', 'Z', '-X', '-Y', '-Z']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `addons_core/io_scene_fbx/__init__.py\:222 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/io_scene_fbx/__init__.py#L222>`__


.. function:: gltf(*, filepath="", export_import_convert_lighting_mode='SPEC', filter_glob="*.glb;*.gltf", directory="", files=None, loglevel=0, import_pack_images=True, merge_vertices=False, import_shading='NORMALS', bone_heuristic='BLENDER', disable_bone_shape=False, bone_shape_scale_factor=1.0, guess_original_bind_pose=True, import_webp_texture=False, import_unused_materials=False, import_select_created_objects=True, import_scene_extras=True, import_scene_as_collection=True, import_merge_material_slots=True)

   Load a glTF 2.0 file

   :param filepath: File Path, Filepath used for importing the file (optional, never None)
   :type filepath: str
   :param export_import_convert_lighting_mode: Lighting Mode, Optional backwards compatibility for non-standard render engines. Applies to lights (optional)

      - ``SPEC``
        Standard -- Physically-based glTF lighting units (cd, lx, nt).
      - ``COMPAT``
        Unitless -- Non-physical, unitless lighting. Useful when exposure controls are not available.
      - ``RAW``
        Raw (Deprecated) -- Blender lighting strengths with no conversion.
   :type export_import_convert_lighting_mode: Literal['SPEC', 'COMPAT', 'RAW']
   :param filter_glob: filter_glob, (optional, never None)
   :type filter_glob: str
   :param directory: directory, (optional, never None)
   :type directory: str
   :param files: File Path, (optional)
   :type files: :class:`bpy_prop_collection`\ [:class:`OperatorFileListElement`] | None
   :param loglevel: Log Level, Log Level (in [-inf, inf], optional)
   :type loglevel: int
   :param import_pack_images: Pack Images, Pack all images into .blend file (optional)
   :type import_pack_images: bool
   :param merge_vertices: Merge Vertices, The glTF format requires discontinuous normals, UVs, and other vertex attributes to be stored as separate vertices, as required for rendering on typical graphics hardware. This option attempts to combine co-located vertices where possible. Currently cannot combine verts with different normals (optional)
   :type merge_vertices: bool
   :param import_shading: Shading, How normals are computed during import (optional)
   :type import_shading: Literal['NORMALS', 'FLAT', 'SMOOTH']
   :param bone_heuristic: Bone Dir, Heuristic for placing bones. Tries to make bones pretty (optional)

      - ``BLENDER``
        Blender (best for import/export round trip) -- Good for re-importing glTFs exported from Blender, and re-exporting glTFs to glTFs after Blender editing. Bone tips are placed on their local +Y axis (in glTF space).
      - ``TEMPERANCE``
        Temperance (average) -- Decent all-around strategy. A bone with one child has its tip placed on the local axis closest to its child.
      - ``FORTUNE``
        Fortune (may look better, less accurate) -- Might look better than Temperance, but also might have errors. A bone with one child has its tip placed at its child's root. Non-uniform scalings may get messed up though, so beware.
   :type bone_heuristic: Literal['BLENDER', 'TEMPERANCE', 'FORTUNE']
   :param disable_bone_shape: Disable Bone Shape, Do not create bone shapes (optional)
   :type disable_bone_shape: bool
   :param bone_shape_scale_factor: Bone Shape Scale, Scale factor for bone shapes (in [-inf, inf], optional)
   :type bone_shape_scale_factor: float
   :param guess_original_bind_pose: Guess Original Bind Pose, Try to guess the original bind pose for skinned meshes from the inverse bind matrices. When off, use default/rest pose as bind pose (optional)
   :type guess_original_bind_pose: bool
   :param import_webp_texture: Import WebP Textures, If a texture exists in WebP format, loads the WebP texture instead of the fallback PNG/JPEG one (optional)
   :type import_webp_texture: bool
   :param import_unused_materials: Import Unused Materials & Images, Import materials & Images not assigned to any mesh (optional)
   :type import_unused_materials: bool
   :param import_select_created_objects: Select Imported Objects, Select created objects at the end of the import (optional)
   :type import_select_created_objects: bool
   :param import_scene_extras: Import Scene Extras, Import scene extras as custom properties. Existing custom properties will be overwritten (optional)
   :type import_scene_extras: bool
   :param import_scene_as_collection: Import Scene as Collection, Import the scene as a collection (optional)
   :type import_scene_as_collection: bool
   :param import_merge_material_slots: Merge Material Slot when possible, Merge material slots when possible (optional)
   :type import_merge_material_slots: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `addons_core/io_scene_gltf2/__init__.py\:2013 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/io_scene_gltf2/__init__.py#L2013>`__


