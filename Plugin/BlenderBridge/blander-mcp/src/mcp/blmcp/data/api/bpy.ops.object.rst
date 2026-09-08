Object Operators
================

.. module:: bpy.ops.object

.. function:: add(*, radius=1.0, type='EMPTY', enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Add an object to the scene

   :param radius: Radius, (in [0, inf], optional)
   :type radius: float
   :param type: Type, (optional)
   :type type: Literal[:ref:`rna_enum_object_type_items`]
   :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object (optional)
   :type enter_editmode: bool
   :param align: Align, The alignment of the new object (optional)

      - ``WORLD``
        World -- Align the new object to the world.
      - ``VIEW``
        View -- Align the new object to the view.
      - ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: Literal['WORLD', 'VIEW', 'CURSOR']
   :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type rotation: :class:`mathutils.Euler` | Sequence[float]
   :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type scale: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: add_modifier_menu()

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_ui/properties_data_modifier.py\:303 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_ui/properties_data_modifier.py#L303>`__

.. function:: add_named(*, linked=False, name="", session_uid=0, matrix=((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)), drop_x=0, drop_y=0)

   Add named object

   :param linked: Linked, Duplicate object but not object data, linking to the original data (optional)
   :type linked: bool
   :param name: Name, Name of the data-block to use by the operator (optional, never None)
   :type name: str
   :param session_uid: Session UID, Session UID of the data-block to use by the operator (in [-inf, inf], optional)
   :type session_uid: int
   :param matrix: Matrix, (multi-dimensional array of 4 * 4 items, in [-inf, inf], optional)
   :type matrix: :class:`mathutils.Matrix` | Sequence[Sequence[float]]
   :param drop_x: Drop X, X-coordinate (screen space) to place the new object under (in [-inf, inf], optional)
   :type drop_x: int
   :param drop_y: Drop Y, Y-coordinate (screen space) to place the new object under (in [-inf, inf], optional)
   :type drop_y: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: align(*, bb_quality=True, align_mode='OPT_2', relative_to='OPT_4', align_axis=set())

   Align objects

   :param bb_quality: High Quality, Enables high quality but slow calculation of the bounding box for perfect results on complex shape meshes with rotation/scale (optional)
   :type bb_quality: bool
   :param align_mode: Align Mode, Side of object to use for alignment (optional)
   :type align_mode: Literal['OPT_1', 'OPT_2', 'OPT_3']
   :param relative_to: Relative To, Reference location to align to (optional)

      - ``OPT_1``
        Scene Origin -- Use the scene origin as the position for the selected objects to align to.
      - ``OPT_2``
        3D Cursor -- Use the 3D cursor as the position for the selected objects to align to.
      - ``OPT_3``
        Selection -- Use the selected objects as the position for the selected objects to align to.
      - ``OPT_4``
        Active -- Use the active object as the position for the selected objects to align to.
   :type relative_to: Literal['OPT_1', 'OPT_2', 'OPT_3', 'OPT_4']
   :param align_axis: Align, Align to axis (optional)
   :type align_axis: set[Literal['X', 'Y', 'Z']]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/object_align.py\:386 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object_align.py#L386>`__


.. function:: anim_transforms_to_deltas()

   Convert object animation for normal transforms to delta transforms

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/object.py\:839 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L839>`__

.. function:: armature_add(*, radius=1.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Add an armature object to the scene

   :param radius: Radius, (in [0, inf], optional)
   :type radius: float
   :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object (optional)
   :type enter_editmode: bool
   :param align: Align, The alignment of the new object (optional)

      - ``WORLD``
        World -- Align the new object to the world.
      - ``VIEW``
        View -- Align the new object to the view.
      - ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: Literal['WORLD', 'VIEW', 'CURSOR']
   :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type rotation: :class:`mathutils.Euler` | Sequence[float]
   :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type scale: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: assign_property_defaults(*, process_data=True, process_bones=True)

   Assign the current values of custom properties as their defaults, for use as part of the rest pose state in NLA track mixing

   :param process_data: Process data properties, (optional)
   :type process_data: bool
   :param process_bones: Process bone properties, (optional)
   :type process_bones: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/object.py\:1001 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L1001>`__


.. function:: bake(*, type='COMBINED', pass_filter=set(), filepath="", width=512, height=512, margin=16, margin_type='EXTEND', use_selected_to_active=False, max_ray_distance=0.0, cage_extrusion=0.0, cage_object="", normal_space='TANGENT', normal_r='POS_X', normal_g='POS_Y', normal_b='POS_Z', target='IMAGE_TEXTURES', save_mode='INTERNAL', use_clear=False, use_cage=False, use_split_materials=False, use_automatic_name=False, uv_layer="")

   Bake image textures of selected objects

   :param type: Type, Type of pass to bake, some of them may not be supported by the current render engine (optional)
   :type type: Literal[:ref:`rna_enum_bake_pass_type_items`]
   :param pass_filter: Pass Filter, Filter to combined, diffuse, glossy, transmission and subsurface passes (optional)
   :type pass_filter: set[Literal[:ref:`rna_enum_bake_pass_filter_type_items`]]
   :param filepath: File Path, Image filepath to use when saving externally (optional, never None)
   :type filepath: str
   :param width: Width, Horizontal dimension of the baking map (external only) (in [1, inf], optional)
   :type width: int
   :param height: Height, Vertical dimension of the baking map (external only) (in [1, inf], optional)
   :type height: int
   :param margin: Margin, Extends the baked result as a post process filter (in [0, inf], optional)
   :type margin: int
   :param margin_type: Margin Type, Which algorithm to use to generate the margin (optional)
   :type margin_type: Literal[:ref:`rna_enum_bake_margin_type_items`]
   :param use_selected_to_active: Selected to Active, Bake shading on the surface of selected objects to the active object (optional)
   :type use_selected_to_active: bool
   :param max_ray_distance: Max Ray Distance, The maximum ray distance for matching points between the active and selected objects. If zero, there is no limit (in [0, inf], optional)
   :type max_ray_distance: float
   :param cage_extrusion: Cage Extrusion, Inflate the active object by the specified distance for baking. This helps matching to points nearer to the outside of the selected object meshes (in [0, inf], optional)
   :type cage_extrusion: float
   :param cage_object: Cage Object, Object to use as cage, instead of calculating the cage from the active object with cage extrusion (optional, never None)
   :type cage_object: str
   :param normal_space: Normal Space, Choose normal space for baking (optional)
   :type normal_space: Literal[:ref:`rna_enum_normal_space_items`]
   :param normal_r: R, Axis to bake in red channel (optional)
   :type normal_r: Literal[:ref:`rna_enum_normal_swizzle_items`]
   :param normal_g: G, Axis to bake in green channel (optional)
   :type normal_g: Literal[:ref:`rna_enum_normal_swizzle_items`]
   :param normal_b: B, Axis to bake in blue channel (optional)
   :type normal_b: Literal[:ref:`rna_enum_normal_swizzle_items`]
   :param target: Target, Where to output the baked map (optional)
   :type target: Literal[:ref:`rna_enum_bake_target_items`]
   :param save_mode: Save Mode, Where to save baked image textures (optional)
   :type save_mode: Literal[:ref:`rna_enum_bake_save_mode_items`]
   :param use_clear: Clear, Clear images before baking (only for internal saving) (optional)
   :type use_clear: bool
   :param use_cage: Cage, Cast rays to active object from a cage (optional)
   :type use_cage: bool
   :param use_split_materials: Split Materials, Split baked maps per material, using material name in output file (external only) (optional)
   :type use_split_materials: bool
   :param use_automatic_name: Automatic Name, Automatically name the output file with the pass type (optional)
   :type use_automatic_name: bool
   :param uv_layer: UV Layer, UV layer to override active (optional, never None)
   :type uv_layer: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: bake_image()

   Bake image textures of selected objects

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: camera_add(*, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Add a camera object to the scene

   :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object (optional)
   :type enter_editmode: bool
   :param align: Align, The alignment of the new object (optional)

      - ``WORLD``
        World -- Align the new object to the world.
      - ``VIEW``
        View -- Align the new object to the view.
      - ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: Literal['WORLD', 'VIEW', 'CURSOR']
   :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type rotation: :class:`mathutils.Euler` | Sequence[float]
   :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type scale: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: camera_custom_update()

   Update custom camera with new parameters from the shader

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: clear_override_library()

   Delete the selected local overrides and relink their usages to the linked data-blocks if possible, else reset them and mark them as non editable

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: collection_add()

   Add an object to a new collection

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: collection_external_asset_drop(*, session_uid=0, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0), use_instance=True, drop_x=0, drop_y=0, collection='')

   Add the dragged collection to the scene

   :param session_uid: Session UID, Session UID of the data-block to use by the operator (in [-inf, inf], optional)
   :type session_uid: int
   :param align: Align, The alignment of the new object (optional)

      - ``WORLD``
        World -- Align the new object to the world.
      - ``VIEW``
        View -- Align the new object to the view.
      - ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: Literal['WORLD', 'VIEW', 'CURSOR']
   :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type rotation: :class:`mathutils.Euler` | Sequence[float]
   :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type scale: :class:`mathutils.Vector` | Sequence[float]
   :param use_instance: Instance, Add the dropped collection as collection instance (optional)
   :type use_instance: bool
   :param drop_x: Drop X, X-coordinate (screen space) to place the new object under (in [-inf, inf], optional)
   :type drop_x: int
   :param drop_y: Drop Y, Y-coordinate (screen space) to place the new object under (in [-inf, inf], optional)
   :type drop_y: int
   :param collection: Collection, (optional)
   :type collection: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: collection_instance_add(*, name="Collection", collection='', align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0), session_uid=0, drop_x=0, drop_y=0)

   Add a collection instance

   :param name: Name, Collection name to add (optional, never None)
   :type name: str
   :param collection: Collection, (optional)
   :type collection: str
   :param align: Align, The alignment of the new object (optional)

      - ``WORLD``
        World -- Align the new object to the world.
      - ``VIEW``
        View -- Align the new object to the view.
      - ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: Literal['WORLD', 'VIEW', 'CURSOR']
   :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type rotation: :class:`mathutils.Euler` | Sequence[float]
   :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type scale: :class:`mathutils.Vector` | Sequence[float]
   :param session_uid: Session UID, Session UID of the data-block to use by the operator (in [-inf, inf], optional)
   :type session_uid: int
   :param drop_x: Drop X, X-coordinate (screen space) to place the new object under (in [-inf, inf], optional)
   :type drop_x: int
   :param drop_y: Drop Y, Y-coordinate (screen space) to place the new object under (in [-inf, inf], optional)
   :type drop_y: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: collection_link(*, collection='')

   Add an object to an existing collection

   :param collection: Collection, (optional)
   :type collection: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: collection_objects_select()

   Select all objects in collection

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: collection_remove()

   Remove the active object from this collection

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: collection_unlink()

   Unlink the collection from all objects

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: constraint_add(*, type='')

   Add a constraint to the active object

   :param type: Type, (optional)
   :type type: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: constraint_add_with_targets(*, type='')

   Add a constraint to the active object, with target (where applicable) set to the selected objects/bones

   :param type: Type, (optional)
   :type type: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: constraints_clear()

   Clear all constraints from the selected objects

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: constraints_copy()

   Copy constraints to other selected objects

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: convert(*, target='MESH', keep_original=False, merge_customdata=True, thickness=5, faces=True, offset=0.01)

   Convert selected objects to another type

   :param target: Target, Type of object to convert to (optional)

      - ``CURVE``
        Curve -- Curve from Mesh or Text objects.
      - ``MESH``
        Mesh -- Mesh from Curve, Surface, Metaball, Text, or Point Cloud objects.
      - ``POINTCLOUD``
        Point Cloud -- Point Cloud from Mesh objects.
      - ``CURVES``
        Curves -- Curves from evaluated curve data.
      - ``GREASEPENCIL``
        Grease Pencil -- Grease Pencil from Curve or Mesh objects.
   :type target: Literal['CURVE', 'MESH', 'POINTCLOUD', 'CURVES', 'GREASEPENCIL']
   :param keep_original: Keep Original, Keep original objects instead of replacing them (optional)
   :type keep_original: bool
   :param merge_customdata: Merge UVs, Merge UV coordinates that share a vertex to account for imprecision in some modifiers (optional)
   :type merge_customdata: bool
   :param thickness: Thickness, (in [1, 100], optional)
   :type thickness: int
   :param faces: Export Faces, Export faces as filled strokes (optional)
   :type faces: bool
   :param offset: Stroke Offset, Offset strokes from fill (in [0, inf], optional)
   :type offset: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: copy_global_transform()

   Copies the matrix of the currently active object or pose bone to the clipboard. Uses world-space matrices

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/copy_global_transform.py\:150 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/copy_global_transform.py#L150>`__

.. function:: copy_relative_transform()

   Copies the matrix of the currently active object or pose bone to the clipboard. Uses matrices relative to a specific object or the active scene camera

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/copy_global_transform.py\:180 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/copy_global_transform.py#L180>`__

.. function:: correctivesmooth_bind(*, modifier="")

   Bind base pose in Corrective Smooth modifier

   :param modifier: Modifier, Name of the modifier to edit (optional, never None)
   :type modifier: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: curves_empty_hair_add(*, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Add an empty curve object to the scene with the selected mesh as surface

   :param align: Align, The alignment of the new object (optional)

      - ``WORLD``
        World -- Align the new object to the world.
      - ``VIEW``
        View -- Align the new object to the view.
      - ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: Literal['WORLD', 'VIEW', 'CURSOR']
   :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type rotation: :class:`mathutils.Euler` | Sequence[float]
   :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type scale: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: curves_random_add(*, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Add a curves object with random curves to the scene

   :param align: Align, The alignment of the new object (optional)

      - ``WORLD``
        World -- Align the new object to the world.
      - ``VIEW``
        View -- Align the new object to the view.
      - ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: Literal['WORLD', 'VIEW', 'CURSOR']
   :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type rotation: :class:`mathutils.Euler` | Sequence[float]
   :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type scale: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: data_instance_add(*, name="", session_uid=0, type='ACTION', align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0), drop_x=0, drop_y=0)

   Add an object data instance

   :param name: Name, Name of the data-block to use by the operator (optional, never None)
   :type name: str
   :param session_uid: Session UID, Session UID of the data-block to use by the operator (in [-inf, inf], optional)
   :type session_uid: int
   :param type: Type, (optional)
   :type type: Literal[:ref:`rna_enum_id_type_items`]
   :param align: Align, The alignment of the new object (optional)

      - ``WORLD``
        World -- Align the new object to the world.
      - ``VIEW``
        View -- Align the new object to the view.
      - ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: Literal['WORLD', 'VIEW', 'CURSOR']
   :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type rotation: :class:`mathutils.Euler` | Sequence[float]
   :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type scale: :class:`mathutils.Vector` | Sequence[float]
   :param drop_x: Drop X, X-coordinate (screen space) to place the new object under (in [-inf, inf], optional)
   :type drop_x: int
   :param drop_y: Drop Y, Y-coordinate (screen space) to place the new object under (in [-inf, inf], optional)
   :type drop_y: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: data_transfer(*, use_reverse_transfer=False, use_freeze=False, data_type='VGROUP_WEIGHTS', use_create=True, vert_mapping='NEAREST', edge_mapping='NEAREST', loop_mapping='NEAREST_POLYNOR', poly_mapping='NEAREST', use_auto_transform=False, use_object_transform=True, use_max_distance=False, max_distance=1.0, ray_radius=0.0, islands_precision=0.1, layers_select_src='ACTIVE', layers_select_dst='ACTIVE', mix_mode='REPLACE', mix_factor=1.0)

   Transfer data layer(s) (weights, edge sharp, etc.) from active to selected meshes

   :param use_reverse_transfer: Reverse Transfer, Transfer from selected objects to active one (optional)
   :type use_reverse_transfer: bool
   :param use_freeze: Freeze Operator, Prevent changes to settings to re-run the operator, handy to change several things at once with heavy geometry (optional)
   :type use_freeze: bool
   :param data_type: Data Type, Which data to transfer (optional)

      - ``VGROUP_WEIGHTS``
        Vertex Group(s) -- Transfer active or all vertex groups.
      - ``BEVEL_WEIGHT_VERT``
        Bevel Weight -- Transfer bevel weights.
      - ``COLOR_VERTEX``
        Colors -- Color Attributes.
      - ``SHARP_EDGE``
        Sharp -- Transfer sharp mark.
      - ``SEAM``
        UV Seam -- Transfer UV seam mark.
      - ``CREASE``
        Subdivision Crease -- Transfer crease values.
      - ``BEVEL_WEIGHT_EDGE``
        Bevel Weight -- Transfer bevel weights.
      - ``FREESTYLE_EDGE``
        Freestyle Mark -- Transfer Freestyle edge mark.
      - ``CUSTOM_NORMAL``
        Custom Normals -- Transfer custom normals.
      - ``COLOR_CORNER``
        Colors -- Color Attributes.
      - ``UV``
        UVs -- Transfer UV layers.
      - ``SMOOTH``
        Smooth -- Transfer flat/smooth mark.
      - ``FREESTYLE_FACE``
        Freestyle Mark -- Transfer Freestyle face mark.
   :type data_type: Literal['VGROUP_WEIGHTS', 'BEVEL_WEIGHT_VERT', 'COLOR_VERTEX', 'SHARP_EDGE', 'SEAM', 'CREASE', 'BEVEL_WEIGHT_EDGE', 'FREESTYLE_EDGE', 'CUSTOM_NORMAL', 'COLOR_CORNER', 'UV', 'SMOOTH', 'FREESTYLE_FACE']
   :param use_create: Create Data, Add data layers on destination meshes if needed (optional)
   :type use_create: bool
   :param vert_mapping: Vertex Mapping, Method used to map source vertices to destination ones (optional)
   :type vert_mapping: Literal[:ref:`rna_enum_dt_method_vertex_items`]
   :param edge_mapping: Edge Mapping, Method used to map source edges to destination ones (optional)
   :type edge_mapping: Literal[:ref:`rna_enum_dt_method_edge_items`]
   :param loop_mapping: Face Corner Mapping, Method used to map source faces' corners to destination ones (optional)
   :type loop_mapping: Literal[:ref:`rna_enum_dt_method_loop_items`]
   :param poly_mapping: Face Mapping, Method used to map source faces to destination ones (optional)
   :type poly_mapping: Literal[:ref:`rna_enum_dt_method_poly_items`]
   :param use_auto_transform: Auto Transform, Automatically compute transformation to get the best possible match between source and destination meshes.Warning: Results will never be as good as manual matching of objects(optional)
   :type use_auto_transform: bool
   :param use_object_transform: Object Transform, Evaluate source and destination meshes in global space (optional)
   :type use_object_transform: bool
   :param use_max_distance: Only Neighbor Geometry, Source elements must be closer than given distance from destination one (optional)
   :type use_max_distance: bool
   :param max_distance: Max Distance, Maximum allowed distance between source and destination element, for non-topology mappings (in [0, inf], optional)
   :type max_distance: float
   :param ray_radius: Ray Radius, 'Width' of rays (especially useful when raycasting against vertices or edges) (in [0, inf], optional)
   :type ray_radius: float
   :param islands_precision: Islands Precision, Factor controlling precision of islands handling (the higher, the better the results) (in [0, 10], optional)
   :type islands_precision: float
   :param layers_select_src: Source Layers Selection, Which layers to transfer, in case of multi-layers types (optional)
   :type layers_select_src: Literal[:ref:`rna_enum_dt_layers_select_src_items`]
   :param layers_select_dst: Destination Layers Matching, How to match source and destination layers (optional)
   :type layers_select_dst: Literal[:ref:`rna_enum_dt_layers_select_dst_items`]
   :param mix_mode: Mix Mode, How to affect destination elements with source values (optional)
   :type mix_mode: Literal[:ref:`rna_enum_dt_mix_mode_items`]
   :param mix_factor: Mix Factor, Factor to use when applying data to destination (exact behavior depends on mix mode) (in [0, 1], optional)
   :type mix_factor: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: datalayout_transfer(*, modifier="", data_type='', use_delete=False, layers_select_src='ACTIVE', layers_select_dst='ACTIVE')

   Transfer layout of data layer(s) from active to selected meshes

   :param modifier: Modifier, Name of the modifier to edit (optional, never None)
   :type modifier: str
   :param data_type: Data Type, Which data to transfer (optional)

      - ``VGROUP_WEIGHTS``
        Vertex Group(s) -- Transfer active or all vertex groups.
      - ``BEVEL_WEIGHT_VERT``
        Bevel Weight -- Transfer bevel weights.
      - ``COLOR_VERTEX``
        Colors -- Color Attributes.
      - ``SHARP_EDGE``
        Sharp -- Transfer sharp mark.
      - ``SEAM``
        UV Seam -- Transfer UV seam mark.
      - ``CREASE``
        Subdivision Crease -- Transfer crease values.
      - ``BEVEL_WEIGHT_EDGE``
        Bevel Weight -- Transfer bevel weights.
      - ``FREESTYLE_EDGE``
        Freestyle Mark -- Transfer Freestyle edge mark.
      - ``CUSTOM_NORMAL``
        Custom Normals -- Transfer custom normals.
      - ``COLOR_CORNER``
        Colors -- Color Attributes.
      - ``UV``
        UVs -- Transfer UV layers.
      - ``SMOOTH``
        Smooth -- Transfer flat/smooth mark.
      - ``FREESTYLE_FACE``
        Freestyle Mark -- Transfer Freestyle face mark.
   :type data_type: Literal['', 'VGROUP_WEIGHTS', 'BEVEL_WEIGHT_VERT', 'COLOR_VERTEX', 'SHARP_EDGE', 'SEAM', 'CREASE', 'BEVEL_WEIGHT_EDGE', 'FREESTYLE_EDGE', 'CUSTOM_NORMAL', 'COLOR_CORNER', 'UV', 'SMOOTH', 'FREESTYLE_FACE']
   :param use_delete: Exact Match, Also delete some data layers from destination if necessary, so that it matches exactly source (optional)
   :type use_delete: bool
   :param layers_select_src: Source Layers Selection, Which layers to transfer, in case of multi-layers types (optional)
   :type layers_select_src: Literal[:ref:`rna_enum_dt_layers_select_src_items`]
   :param layers_select_dst: Destination Layers Matching, How to match source and destination layers (optional)
   :type layers_select_dst: Literal[:ref:`rna_enum_dt_layers_select_dst_items`]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: delete(*, use_global=False, confirm=True)

   Delete selected objects

   :param use_global: Delete Globally, Remove object from all scenes (optional)
   :type use_global: bool
   :param confirm: Confirm, Prompt for confirmation (optional)
   :type confirm: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: delete_fix_to_camera_keys()

   Delete all keys that were generated by the 'Fix to Scene Camera' operator

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/copy_global_transform.py\:639 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/copy_global_transform.py#L639>`__

.. function:: drop_geometry_nodes(*, session_uid=0, show_datablock_in_modifier=True)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :param session_uid: Session UID, Session UID of the geometry node group being dropped (in [-inf, inf], optional)
   :type session_uid: int
   :param show_datablock_in_modifier: Show the data-block selector in the modifier, (optional)
   :type show_datablock_in_modifier: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: drop_named_material(*, name="", session_uid=0)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :param name: Name, Name of the data-block to use by the operator (optional, never None)
   :type name: str
   :param session_uid: Session UID, Session UID of the data-block to use by the operator (in [-inf, inf], optional)
   :type session_uid: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: duplicate(*, linked=False, mode='TRANSLATION')

   Duplicate selected objects

   :param linked: Linked, Duplicate object but not object data, linking to the original data (optional)
   :type linked: bool
   :param mode: Mode, (optional)
   :type mode: Literal[:ref:`rna_enum_transform_mode_type_items`]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: duplicate_move(*, OBJECT_OT_duplicate={}, TRANSFORM_OT_translate={})

   Duplicate the selected objects and move them

   :param OBJECT_OT_duplicate: Duplicate Objects, Duplicate selected objects (optional, :func:`bpy.ops.object.duplicate` keyword arguments)
   :type OBJECT_OT_duplicate: dict[str, Any]
   :param TRANSFORM_OT_translate: Move, Move selected items (optional, :func:`bpy.ops.transform.translate` keyword arguments)
   :type TRANSFORM_OT_translate: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: duplicate_move_linked(*, OBJECT_OT_duplicate={}, TRANSFORM_OT_translate={})

   Duplicate the selected objects, but not their object data, and move them

   :param OBJECT_OT_duplicate: Duplicate Objects, Duplicate selected objects (optional, :func:`bpy.ops.object.duplicate` keyword arguments)
   :type OBJECT_OT_duplicate: dict[str, Any]
   :param TRANSFORM_OT_translate: Move, Move selected items (optional, :func:`bpy.ops.transform.translate` keyword arguments)
   :type TRANSFORM_OT_translate: dict[str, Any]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: duplicates_make_real(*, use_base_parent=False, use_hierarchy=False)

   Make instanced objects attached to this object real

   :param use_base_parent: Parent, Parent newly created objects to the original instancer (optional)
   :type use_base_parent: bool
   :param use_hierarchy: Keep Hierarchy, Maintain parent child relationships (optional)
   :type use_hierarchy: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: editmode_toggle()

   Toggle object's edit mode

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: effector_add(*, type='FORCE', radius=1.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Add an empty object with a physics effector to the scene

   :param type: Type, (optional)
   :type type: Literal['FORCE', 'WIND', 'VORTEX', 'MAGNET', 'HARMONIC', 'CHARGE', 'LENNARDJ', 'TEXTURE', 'GUIDE', 'BOID', 'TURBULENCE', 'DRAG', 'FLUID']
   :param radius: Radius, (in [0, inf], optional)
   :type radius: float
   :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object (optional)
   :type enter_editmode: bool
   :param align: Align, The alignment of the new object (optional)

      - ``WORLD``
        World -- Align the new object to the world.
      - ``VIEW``
        View -- Align the new object to the view.
      - ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: Literal['WORLD', 'VIEW', 'CURSOR']
   :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type rotation: :class:`mathutils.Euler` | Sequence[float]
   :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type scale: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: empty_add(*, type='PLAIN_AXES', radius=1.0, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Add an empty object to the scene

   :param type: Type, (optional)
   :type type: Literal[:ref:`rna_enum_object_empty_drawtype_items`]
   :param radius: Radius, (in [0, inf], optional)
   :type radius: float
   :param align: Align, The alignment of the new object (optional)

      - ``WORLD``
        World -- Align the new object to the world.
      - ``VIEW``
        View -- Align the new object to the view.
      - ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: Literal['WORLD', 'VIEW', 'CURSOR']
   :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type rotation: :class:`mathutils.Euler` | Sequence[float]
   :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type scale: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: empty_image_add(*, filepath="", hide_props_region=True, check_existing=False, filter_blender=False, filter_backup=False, filter_image=True, filter_movie=True, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='', name="", session_uid=0, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0), background=False)

   Add an empty image type to scene with data

   :param filepath: File Path, Path to file (optional, never None)
   :type filepath: str
   :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings (optional)
   :type hide_props_region: bool
   :param check_existing: Check Existing, Check and warn on overwriting existing files (optional)
   :type check_existing: bool
   :param filter_blender: Filter .blend files, (optional)
   :type filter_blender: bool
   :param filter_backup: Filter backup .blend files, (optional)
   :type filter_backup: bool
   :param filter_image: Filter image files, (optional)
   :type filter_image: bool
   :param filter_movie: Filter movie files, (optional)
   :type filter_movie: bool
   :param filter_python: Filter Python files, (optional)
   :type filter_python: bool
   :param filter_font: Filter font files, (optional)
   :type filter_font: bool
   :param filter_sound: Filter sound files, (optional)
   :type filter_sound: bool
   :param filter_text: Filter text files, (optional)
   :type filter_text: bool
   :param filter_archive: Filter archive files, (optional)
   :type filter_archive: bool
   :param filter_btx: Filter btx files, (optional)
   :type filter_btx: bool
   :param filter_alembic: Filter Alembic files, (optional)
   :type filter_alembic: bool
   :param filter_usd: Filter USD files, (optional)
   :type filter_usd: bool
   :param filter_obj: Filter OBJ files, (optional)
   :type filter_obj: bool
   :param filter_volume: Filter OpenVDB volume files, (optional)
   :type filter_volume: bool
   :param filter_folder: Filter folders, (optional)
   :type filter_folder: bool
   :param filter_blenlib: Filter Blender IDs, (optional)
   :type filter_blenlib: bool
   :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file (in [1, 9], optional)
   :type filemode: int
   :param relative_path: Relative Path, Select the file relative to the blend file (optional)
   :type relative_path: bool
   :param show_multiview: Enable Multi-View, (optional)
   :type show_multiview: bool
   :param use_multiview: Use Multi-View, (optional)
   :type use_multiview: bool
   :param display_type: Display Type, (optional)

      - ``DEFAULT``
        Default -- Automatically determine display type for files.
      - ``LIST_VERTICAL``
        Short List -- Display files as short list.
      - ``LIST_HORIZONTAL``
        Long List -- Display files as a detailed list.
      - ``THUMBNAIL``
        Thumbnails -- Display files as thumbnails.
   :type display_type: Literal['DEFAULT', 'LIST_VERTICAL', 'LIST_HORIZONTAL', 'THUMBNAIL']
   :param sort_method: File sorting mode, (optional)

      - ``DEFAULT``
        Default -- Automatically determine sort method for files.
      - ``FILE_SORT_ALPHA``
        Name -- Sort the file list alphabetically.
      - ``FILE_SORT_EXTENSION``
        Extension -- Sort the file list by extension/type.
      - ``FILE_SORT_TIME``
        Modified Date -- Sort files by modification time.
      - ``FILE_SORT_SIZE``
        Size -- Sort files by size.
      - ``ASSET_CATALOG``
        Asset Catalog -- Sort the asset list so that assets in the same catalog are kept together. Within a single catalog, assets are ordered by name. The catalogs are in order of the flattened catalog hierarchy..
   :type sort_method: Literal['', 'DEFAULT', 'FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE', 'ASSET_CATALOG']
   :param name: Name, Name of the data-block to use by the operator (optional, never None)
   :type name: str
   :param session_uid: Session UID, Session UID of the data-block to use by the operator (in [-inf, inf], optional)
   :type session_uid: int
   :param align: Align, The alignment of the new object (optional)

      - ``WORLD``
        World -- Align the new object to the world.
      - ``VIEW``
        View -- Align the new object to the view.
      - ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: Literal['WORLD', 'VIEW', 'CURSOR']
   :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type rotation: :class:`mathutils.Euler` | Sequence[float]
   :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type scale: :class:`mathutils.Vector` | Sequence[float]
   :param background: Put in Background, Make the image render behind all objects (optional)
   :type background: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: explode_refresh(*, modifier="")

   Refresh data in the Explode modifier

   :param modifier: Modifier, Name of the modifier to edit (optional, never None)
   :type modifier: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: fix_to_camera(*, use_location=True, use_rotation=True, use_scale=True)

   Generate new keys to fix the selected object/bone to the camera on unkeyed frames

   :param use_location: Location, Create Location keys when fixing to the scene camera (optional)
   :type use_location: bool
   :param use_rotation: Rotation, Create Rotation keys when fixing to the scene camera (optional)
   :type use_rotation: bool
   :param use_scale: Scale, Create Scale keys when fixing to the scene camera (optional)
   :type use_scale: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/copy_global_transform.py\:639 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/copy_global_transform.py#L639>`__


.. function:: forcefield_toggle()

   Toggle object's force field

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: geometry_node_bake_delete_single(*, session_uid=0, modifier_name="", bake_id=0)

   Delete baked data of a single bake node or simulation

   :param session_uid: Session UID, Session UID of the data-block to use by the operator (in [-inf, inf], optional)
   :type session_uid: int
   :param modifier_name: Modifier Name, Name of the modifier that contains the node (optional, never None)
   :type modifier_name: str
   :param bake_id: Bake ID, Nested node id of the node (in [0, inf], optional)
   :type bake_id: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: geometry_node_bake_pack_single(*, session_uid=0, modifier_name="", bake_id=0)

   Pack baked data from disk into the .blend file

   :param session_uid: Session UID, Session UID of the data-block to use by the operator (in [-inf, inf], optional)
   :type session_uid: int
   :param modifier_name: Modifier Name, Name of the modifier that contains the node (optional, never None)
   :type modifier_name: str
   :param bake_id: Bake ID, Nested node id of the node (in [0, inf], optional)
   :type bake_id: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: geometry_node_bake_single(*, session_uid=0, modifier_name="", bake_id=0)

   Bake a single bake node or simulation

   :param session_uid: Session UID, Session UID of the data-block to use by the operator (in [-inf, inf], optional)
   :type session_uid: int
   :param modifier_name: Modifier Name, Name of the modifier that contains the node (optional, never None)
   :type modifier_name: str
   :param bake_id: Bake ID, Nested node id of the node (in [0, inf], optional)
   :type bake_id: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: geometry_node_bake_unpack_single(*, session_uid=0, modifier_name="", bake_id=0, method='USE_LOCAL')

   Unpack baked data from the .blend file to disk

   :param session_uid: Session UID, Session UID of the data-block to use by the operator (in [-inf, inf], optional)
   :type session_uid: int
   :param modifier_name: Modifier Name, Name of the modifier that contains the node (optional, never None)
   :type modifier_name: str
   :param bake_id: Bake ID, Nested node id of the node (in [0, inf], optional)
   :type bake_id: int
   :param method: Method, How to unpack (optional)
   :type method: Literal['USE_LOCAL', 'WRITE_LOCAL', 'USE_ORIGINAL', 'WRITE_ORIGINAL']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: geometry_node_tree_copy_assign()

   Duplicate the active geometry node group and assign it to the active modifier

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: geometry_nodes_input_attribute_toggle(*, input_name="", modifier_name="")

   Switch between an attribute and a single value to define the data for every element

   :param input_name: Input Name, (optional, never None)
   :type input_name: str
   :param modifier_name: Modifier Name, (optional, never None)
   :type modifier_name: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: geometry_nodes_move_to_nodes(*, use_selected_objects=False)

   Move inputs and outputs from in the modifier to a new node group

   :param use_selected_objects: Selected Objects, Affect all selected objects instead of just the active object (optional)
   :type use_selected_objects: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/geometry_nodes.py\:285 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/geometry_nodes.py#L285>`__


.. function:: grease_pencil_add(*, type='EMPTY', use_in_front=True, stroke_depth_offset=0.05, use_lights=True, stroke_depth_order='3D', radius=1.0, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Add a Grease Pencil object to the scene

   :param type: Type, (optional)
   :type type: Literal[:ref:`rna_enum_object_gpencil_type_items`]
   :param use_in_front: Show In Front, Show Line Art Grease Pencil in front of everything (optional)
   :type use_in_front: bool
   :param stroke_depth_offset: Stroke Offset, Stroke offset for the Line Art modifier (in [0, inf], optional)
   :type stroke_depth_offset: float
   :param use_lights: Use Lights, Use lights for this Grease Pencil object (optional)
   :type use_lights: bool
   :param stroke_depth_order: Stroke Depth Order, Defines how the strokes are ordered in 3D space (for objects not displayed 'In Front') (optional)

      - ``2D``
        2D Layers -- Display strokes using Grease Pencil layers to define order.
      - ``3D``
        3D Location -- Display strokes using real 3D position in 3D space.
   :type stroke_depth_order: Literal['2D', '3D']
   :param radius: Radius, (in [0, inf], optional)
   :type radius: float
   :param align: Align, The alignment of the new object (optional)

      - ``WORLD``
        World -- Align the new object to the world.
      - ``VIEW``
        View -- Align the new object to the view.
      - ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: Literal['WORLD', 'VIEW', 'CURSOR']
   :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type rotation: :class:`mathutils.Euler` | Sequence[float]
   :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type scale: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: grease_pencil_dash_modifier_segment_add(*, modifier="")

   Add a segment to the dash modifier

   :param modifier: Modifier, Name of the modifier to edit (optional, never None)
   :type modifier: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: grease_pencil_dash_modifier_segment_move(*, modifier="", type='UP')

   Move the active dash segment up or down

   :param modifier: Modifier, Name of the modifier to edit (optional, never None)
   :type modifier: str
   :param type: Type, (optional)
   :type type: Literal['UP', 'DOWN']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: grease_pencil_dash_modifier_segment_remove(*, modifier="", index=0)

   Remove the active segment from the dash modifier

   :param modifier: Modifier, Name of the modifier to edit (optional, never None)
   :type modifier: str
   :param index: Index, Index of the segment to remove (in [0, inf], optional)
   :type index: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: grease_pencil_time_modifier_segment_add(*, modifier="")

   Add a segment to the time modifier

   :param modifier: Modifier, Name of the modifier to edit (optional, never None)
   :type modifier: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: grease_pencil_time_modifier_segment_move(*, modifier="", type='UP')

   Move the active time segment up or down

   :param modifier: Modifier, Name of the modifier to edit (optional, never None)
   :type modifier: str
   :param type: Type, (optional)
   :type type: Literal['UP', 'DOWN']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: grease_pencil_time_modifier_segment_remove(*, modifier="", index=0)

   Remove the active segment from the time modifier

   :param modifier: Modifier, Name of the modifier to edit (optional, never None)
   :type modifier: str
   :param index: Index, Index of the segment to remove (in [0, inf], optional)
   :type index: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: hide_collection(*, collection_index=-1, toggle=False, extend=False)

   Show only objects in collection (Shift to extend)

   :param collection_index: Collection Index, Index of the collection to change visibility (in [-1, inf], optional)
   :type collection_index: int
   :param toggle: Toggle, Toggle visibility (optional)
   :type toggle: bool
   :param extend: Extend, Extend visibility (optional)
   :type extend: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: hide_render_clear_all()

   Reveal all render objects by setting the hide render flag

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/object.py\:743 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L743>`__

.. function:: hide_view_clear(*, select=True)

   Reveal temporarily hidden objects

   :param select: Select, Select revealed objects (optional)
   :type select: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: hide_view_set(*, unselected=False)

   Temporarily hide objects from the viewport

   :param unselected: Unselected, Hide unselected rather than selected objects (optional)
   :type unselected: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: hook_add_newob()

   Hook selected vertices to a newly created object

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: hook_add_selob(*, use_bone=False)

   Hook selected vertices to the first selected object

   :param use_bone: Active Bone, Assign the hook to the hook object's active bone (optional)
   :type use_bone: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: hook_assign(*, modifier='')

   Assign the selected vertices to a hook

   :param modifier: Modifier, Modifier number to assign to (optional)
   :type modifier: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: hook_recenter(*, modifier='')

   Set hook center to cursor position

   :param modifier: Modifier, Modifier number to assign to (optional)
   :type modifier: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: hook_remove(*, modifier='')

   Remove a hook from the active object

   :param modifier: Modifier, Modifier number to remove (optional)
   :type modifier: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: hook_reset(*, modifier='')

   Recalculate and clear offset transformation

   :param modifier: Modifier, Modifier number to assign to (optional)
   :type modifier: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: hook_select(*, modifier='')

   Select affected vertices on mesh

   :param modifier: Modifier, Modifier number to remove (optional)
   :type modifier: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: instance_offset_from_cursor()

   Set offset used for collection instances based on cursor position

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/object.py\:936 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L936>`__

.. function:: instance_offset_from_object()

   Set offset used for collection instances based on the active object position

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/object.py\:968 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L968>`__

.. function:: instance_offset_to_cursor()

   Set cursor position to the offset used for collection instances

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/object.py\:951 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L951>`__

.. function:: isolate_type_render()

   Hide unselected render objects of same type as active by setting the hide render flag

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/object.py\:723 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L723>`__

.. function:: join()

   Join selected objects into active object

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: join_shapes(*, use_mirror=False)

   Add the vertex positions of selected objects as shape keys or update existing shape keys with matching names

   :param use_mirror: Mirror, Mirror the new shape key values (optional)
   :type use_mirror: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: join_uvs()

   Transfer UV Maps from active to selected objects (needs matching geometry)

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/object.py\:623 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L623>`__

.. function:: laplaciandeform_bind(*, modifier="")

   Bind mesh to system in laplacian deform modifier

   :param modifier: Modifier, Name of the modifier to edit (optional, never None)
   :type modifier: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: lattice_add_to_selected(*, fit_to_selected=True, radius=1.0, margin=0.0, add_modifiers=True, resolution_u=2, resolution_v=2, resolution_w=2, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Add a lattice and use it to deform selected objects

   :param fit_to_selected: Fit to Selected, Resize lattice to fit selected deformable objects (optional)
   :type fit_to_selected: bool
   :param radius: Radius, (in [0, inf], optional)
   :type radius: float
   :param margin: Margin, Add margin to lattice dimensions (in [0, inf], optional)
   :type margin: float
   :param add_modifiers: Add Modifiers, Automatically add lattice modifiers to selected objects (optional)
   :type add_modifiers: bool
   :param resolution_u: Resolution U, Lattice resolution in U direction (in [1, 64], optional)
   :type resolution_u: int
   :param resolution_v: V, Lattice resolution in V direction (in [1, 64], optional)
   :type resolution_v: int
   :param resolution_w: W, Lattice resolution in W direction (in [1, 64], optional)
   :type resolution_w: int
   :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object (optional)
   :type enter_editmode: bool
   :param align: Align, The alignment of the new object (optional)

      - ``WORLD``
        World -- Align the new object to the world.
      - ``VIEW``
        View -- Align the new object to the view.
      - ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: Literal['WORLD', 'VIEW', 'CURSOR']
   :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type rotation: :class:`mathutils.Euler` | Sequence[float]
   :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type scale: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: light_add(*, type='POINT', radius=1.0, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Add a light object to the scene

   :param type: Type, (optional)
   :type type: Literal[:ref:`rna_enum_light_type_items`]
   :param radius: Radius, (in [0, inf], optional)
   :type radius: float
   :param align: Align, The alignment of the new object (optional)

      - ``WORLD``
        World -- Align the new object to the world.
      - ``VIEW``
        View -- Align the new object to the view.
      - ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: Literal['WORLD', 'VIEW', 'CURSOR']
   :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type rotation: :class:`mathutils.Euler` | Sequence[float]
   :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type scale: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: light_linking_blocker_collection_new()

   Create new light linking collection used by the active emitter

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: light_linking_blockers_link(*, link_state='INCLUDE')

   Light link selected blockers to the active emitter object

   :param link_state: Link State, State of the shadow linking (optional)

      - ``INCLUDE``
        Include -- Include selected blockers to cast shadows from the active emitter.
      - ``EXCLUDE``
        Exclude -- Exclude selected blockers from casting shadows from the active emitter.
   :type link_state: Literal['INCLUDE', 'EXCLUDE']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: light_linking_blockers_select()

   Select all objects which block light from this emitter

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: light_linking_receiver_collection_new()

   Create new light linking collection used by the active emitter

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: light_linking_receivers_link(*, link_state='INCLUDE')

   Light link selected receivers to the active emitter object

   :param link_state: Link State, State of the light linking (optional)

      - ``INCLUDE``
        Include -- Include selected receivers to receive light from the active emitter.
      - ``EXCLUDE``
        Exclude -- Exclude selected receivers from receiving light from the active emitter.
   :type link_state: Literal['INCLUDE', 'EXCLUDE']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: light_linking_receivers_select()

   Select all objects which receive light from this emitter

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: light_linking_unlink_from_collection()

   Remove this object or collection from the light linking collection

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: lightprobe_add(*, type='SPHERE', radius=1.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Add a light probe object

   :param type: Type, (optional)

      - ``SPHERE``
        Sphere -- Light probe that captures precise lighting from all directions at a single point in space.
      - ``PLANE``
        Plane -- Light probe that captures incoming light from a single direction on a plane.
      - ``VOLUME``
        Volume -- Light probe that captures low frequency lighting inside a volume.
   :type type: Literal['SPHERE', 'PLANE', 'VOLUME']
   :param radius: Radius, (in [0, inf], optional)
   :type radius: float
   :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object (optional)
   :type enter_editmode: bool
   :param align: Align, The alignment of the new object (optional)

      - ``WORLD``
        World -- Align the new object to the world.
      - ``VIEW``
        View -- Align the new object to the view.
      - ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: Literal['WORLD', 'VIEW', 'CURSOR']
   :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type rotation: :class:`mathutils.Euler` | Sequence[float]
   :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type scale: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: lightprobe_cache_bake(*, subset='ALL')

   Bake irradiance volume light cache

   :param subset: Subset, Subset of probes to update (optional)

      - ``ALL``
        All Volumes -- Bake all light probe volumes.
      - ``SELECTED``
        Selected Only -- Only bake selected light probe volumes.
      - ``ACTIVE``
        Active Only -- Only bake the active light probe volume.
   :type subset: Literal['ALL', 'SELECTED', 'ACTIVE']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: lightprobe_cache_free(*, subset='SELECTED')

   Delete cached indirect lighting

   :param subset: Subset, Subset of probes to update (optional)

      - ``ALL``
        All Light Probes -- Delete all light probes' baked lighting data.
      - ``SELECTED``
        Selected Only -- Only delete selected light probes' baked lighting data.
      - ``ACTIVE``
        Active Only -- Only delete the active light probe's baked lighting data.
   :type subset: Literal['ALL', 'SELECTED', 'ACTIVE']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: lineart_bake_strokes(*, bake_all=False)

   Bake Line Art for current Grease Pencil object

   :param bake_all: Bake All, Bake all Line Art modifiers (optional)
   :type bake_all: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: lineart_clear(*, clear_all=False)

   Clear all strokes in current Grease Pencil object

   :param clear_all: Clear All, Clear all Line Art modifier bakes (optional)
   :type clear_all: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: link_to_collection(*, collection_uid=-1, is_new=False, new_collection_name="")

   Link objects to a collection

   :param collection_uid: Collection UID, Session UID of the collection to link to (in [-1, inf], optional)
   :type collection_uid: int
   :param is_new: New, Link objects to a new collection (optional)
   :type is_new: bool
   :param new_collection_name: Name, Name of the newly added collection (optional, never None)
   :type new_collection_name: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: location_clear(*, clear_delta=False)

   Clear the object's location

   :param clear_delta: Clear Delta, Clear delta location in addition to clearing the normal location transform (optional)
   :type clear_delta: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: make_dupli_face()

   Convert objects into instanced faces

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/object.py\:706 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L706>`__

.. function:: make_links_data(*, type='OBDATA')

   Transfer data from active object to selected objects

   :param type: Type, (optional)

      - ``OBDATA``
        Link Object Data -- Replace assigned Object Data.
      - ``MATERIAL``
        Link Materials -- Replace assigned Materials.
      - ``ANIMATION``
        Link Animation Data -- Replace assigned Animation Data.
      - ``GROUPS``
        Link Collections -- Replace assigned Collections.
      - ``DUPLICOLLECTION``
        Link Instance Collection -- Replace assigned Collection Instance.
      - ``FONTS``
        Link Fonts to Text -- Replace Text object Fonts.
      - ``MODIFIERS``
        Copy Modifiers -- Replace Modifiers.
      - ``EFFECTS``
        Copy Grease Pencil Effects -- Replace Grease Pencil Effects.
   :type type: Literal['OBDATA', 'MATERIAL', 'ANIMATION', 'GROUPS', 'DUPLICOLLECTION', 'FONTS', 'MODIFIERS', 'EFFECTS']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: make_links_scene(*, scene='')

   Link selection to another scene

   :param scene: Scene, (optional)
   :type scene: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: make_local(*, type='SELECT_OBJECT')

   Make library linked data-blocks local to this file

   :param type: Type, (optional)
   :type type: Literal['SELECT_OBJECT', 'SELECT_OBDATA', 'SELECT_OBDATA_MATERIAL', 'ALL']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: make_override_library(*, collection=0)

   Create a local override of the selected linked objects, and their hierarchy of dependencies

   :param collection: Override Collection, Session UID of the directly linked collection containing the selected object, to make an override from (in [-inf, inf], optional)
   :type collection: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: make_single_user(*, type='SELECTED_OBJECTS', object=False, obdata=False, material=False, animation=False, obdata_animation=False)

   Make linked data local to each object

   :param type: Type, (optional)
   :type type: Literal['SELECTED_OBJECTS', 'ALL']
   :param object: Object, Make single user objects (optional)
   :type object: bool
   :param obdata: Object Data, Make single user object data (optional)
   :type obdata: bool
   :param material: Materials, Make materials local to each data-block (optional)
   :type material: bool
   :param animation: Object Animation, Make object animation data local to each object (optional)
   :type animation: bool
   :param obdata_animation: Object Data Animation, Make object data (mesh, curve etc.) animation data local to each object (optional)
   :type obdata_animation: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: material_slot_add()

   Add a new material slot

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: material_slot_assign()

   Assign active material slot to selection

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: material_slot_copy()

   Copy material to selected objects

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: material_slot_deselect()

   Deselect by active material slot

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: material_slot_move(*, direction='UP')

   Move the active material up/down in the list

   :param direction: Direction, Direction to move the active material towards (optional)
   :type direction: Literal['UP', 'DOWN']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: material_slot_remove()

   Remove the selected material slot

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: material_slot_remove_all()

   Remove all materials

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: material_slot_remove_unused()

   Remove unused material slots

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: material_slot_select()

   Select by active material slot

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: meshdeform_bind(*, modifier="")

   Bind mesh to cage in mesh deform modifier

   :param modifier: Modifier, Name of the modifier to edit (optional, never None)
   :type modifier: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: metaball_add(*, type='BALL', radius=2.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Add a metaball object to the scene

   :param type: Primitive, (optional)
   :type type: Literal[:ref:`rna_enum_metaelem_type_items`]
   :param radius: Radius, (in [0, inf], optional)
   :type radius: float
   :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object (optional)
   :type enter_editmode: bool
   :param align: Align, The alignment of the new object (optional)

      - ``WORLD``
        World -- Align the new object to the world.
      - ``VIEW``
        View -- Align the new object to the view.
      - ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: Literal['WORLD', 'VIEW', 'CURSOR']
   :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type rotation: :class:`mathutils.Euler` | Sequence[float]
   :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type scale: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: mode_set(*, mode='OBJECT', toggle=False)

   Sets the object interaction mode

   :param mode: Mode, (optional)
   :type mode: Literal[:ref:`rna_enum_object_mode_items`]
   :param toggle: Toggle, (optional)
   :type toggle: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: mode_set_with_submode(*, mode='OBJECT', toggle=False, mesh_select_mode=set())

   Sets the object interaction mode

   :param mode: Mode, (optional)
   :type mode: Literal[:ref:`rna_enum_object_mode_items`]
   :param toggle: Toggle, (optional)
   :type toggle: bool
   :param mesh_select_mode: Mesh Mode, (optional)
   :type mesh_select_mode: set[Literal[:ref:`rna_enum_mesh_select_mode_items`]]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: modifier_add(*, type='SUBSURF', use_selected_objects=False)

   Add a procedural operation/effect to the active object

   :param type: Type, (optional)
   :type type: Literal[:ref:`rna_enum_object_modifier_type_items`]
   :param use_selected_objects: Selected Objects, Affect all selected objects instead of just the active object (optional)
   :type use_selected_objects: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: modifier_add_node_group(*, asset_library_type='LOCAL', asset_library_identifier="", relative_asset_identifier="", session_uid=0, use_selected_objects=False)

   Add a procedural operation/effect to the active object

   :param asset_library_type: Asset Library Type, (optional)
   :type asset_library_type: Literal[:ref:`rna_enum_asset_library_type_items`]
   :param asset_library_identifier: Asset Library Identifier, (optional, never None)
   :type asset_library_identifier: str
   :param relative_asset_identifier: Relative Asset Identifier, (optional, never None)
   :type relative_asset_identifier: str
   :param session_uid: Session UID, Session UID of the data-block to use by the operator (in [-inf, inf], optional)
   :type session_uid: int
   :param use_selected_objects: Selected Objects, Affect all selected objects instead of just the active object (optional)
   :type use_selected_objects: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: modifier_apply(*, modifier="", report=False, merge_customdata=True, single_user=False, all_keyframes=False, use_selected_objects=False)

   Apply modifier and remove from the stack

   :param modifier: Modifier, Name of the modifier to edit (optional, never None)
   :type modifier: str
   :param report: Report, Create a notification after the operation (optional)
   :type report: bool
   :param merge_customdata: Merge UVs, For mesh objects, merge UV coordinates that share a vertex to account for imprecision in some modifiers (optional)
   :type merge_customdata: bool
   :param single_user: Make Data Single User, Make the object's data single user if needed (optional)
   :type single_user: bool
   :param all_keyframes: Apply to all keyframes, For Grease Pencil objects, apply the modifier to all the keyframes (optional)
   :type all_keyframes: bool
   :param use_selected_objects: Selected Objects, Affect all selected objects instead of just the active object (optional)
   :type use_selected_objects: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: modifier_apply_as_shapekey(*, keep_modifier=False, modifier="", report=False, use_selected_objects=False)

   Apply modifier as a new shape key and remove from the stack

   :param keep_modifier: Keep Modifier, Do not remove the modifier from stack (optional)
   :type keep_modifier: bool
   :param modifier: Modifier, Name of the modifier to edit (optional, never None)
   :type modifier: str
   :param report: Report, Create a notification after the operation (optional)
   :type report: bool
   :param use_selected_objects: Selected Objects, Affect all selected objects instead of just the active object (optional)
   :type use_selected_objects: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: modifier_convert(*, modifier="")

   Convert particles to a mesh object

   :param modifier: Modifier, Name of the modifier to edit (optional, never None)
   :type modifier: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: modifier_copy(*, modifier="", use_selected_objects=False)

   Duplicate modifier at the same position in the stack

   :param modifier: Modifier, Name of the modifier to edit (optional, never None)
   :type modifier: str
   :param use_selected_objects: Selected Objects, Affect all selected objects instead of just the active object (optional)
   :type use_selected_objects: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: modifier_copy_to_selected(*, modifier="")

   Copy the modifier from the active object to all selected objects

   :param modifier: Modifier, Name of the modifier to edit (optional, never None)
   :type modifier: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: modifier_move_down(*, modifier="")

   Move modifier down in the stack

   :param modifier: Modifier, Name of the modifier to edit (optional, never None)
   :type modifier: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: modifier_move_to_index(*, modifier="", index=0, use_selected_objects=False)

   Change the modifier's index in the stack so it evaluates after the set number of others

   :param modifier: Modifier, Name of the modifier to edit (optional, never None)
   :type modifier: str
   :param index: Index, The index to move the modifier to (in [0, inf], optional)
   :type index: int
   :param use_selected_objects: Selected Objects, Affect all selected objects instead of just the active object (optional)
   :type use_selected_objects: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: modifier_move_up(*, modifier="")

   Move modifier up in the stack

   :param modifier: Modifier, Name of the modifier to edit (optional, never None)
   :type modifier: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: modifier_remove(*, modifier="", report=False, use_selected_objects=False)

   Remove a modifier from the active object

   :param modifier: Modifier, Name of the modifier to edit (optional, never None)
   :type modifier: str
   :param report: Report, Create a notification after the operation (optional)
   :type report: bool
   :param use_selected_objects: Selected Objects, Affect all selected objects instead of just the active object (optional)
   :type use_selected_objects: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: modifier_set_active(*, modifier="")

   Activate the modifier to use as the context

   :param modifier: Modifier, Name of the modifier to edit (optional, never None)
   :type modifier: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: modifiers_clear()

   Clear all modifiers from the selected objects

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: modifiers_copy_to_selected()

   Copy modifiers to other selected objects

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: move_to_collection(*, collection_uid=-1, is_new=False, new_collection_name="")

   Move objects to a collection

   :param collection_uid: Collection UID, Session UID of the collection to move to (in [-1, inf], optional)
   :type collection_uid: int
   :param is_new: New, Move objects to a new collection (optional)
   :type is_new: bool
   :param new_collection_name: Name, Name of the newly added collection (optional, never None)
   :type new_collection_name: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: multires_base_apply(*, modifier="", apply_heuristic=True)

   Modify the base mesh to conform to the displaced mesh

   :param modifier: Modifier, Name of the modifier to edit (optional, never None)
   :type modifier: str
   :param apply_heuristic: Apply Subdivision Heuristic, Whether or not the final base mesh positions will be slightly altered to account for a new subdivision modifier being added (optional)
   :type apply_heuristic: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: multires_external_pack()

   Pack displacements from an external file

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: multires_external_save(*, filepath="", hide_props_region=True, check_existing=True, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=True, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, display_type='DEFAULT', sort_method='', modifier="")

   Save displacements to an external file

   :param filepath: File Path, Path to file (optional, never None)
   :type filepath: str
   :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings (optional)
   :type hide_props_region: bool
   :param check_existing: Check Existing, Check and warn on overwriting existing files (optional)
   :type check_existing: bool
   :param filter_blender: Filter .blend files, (optional)
   :type filter_blender: bool
   :param filter_backup: Filter backup .blend files, (optional)
   :type filter_backup: bool
   :param filter_image: Filter image files, (optional)
   :type filter_image: bool
   :param filter_movie: Filter movie files, (optional)
   :type filter_movie: bool
   :param filter_python: Filter Python files, (optional)
   :type filter_python: bool
   :param filter_font: Filter font files, (optional)
   :type filter_font: bool
   :param filter_sound: Filter sound files, (optional)
   :type filter_sound: bool
   :param filter_text: Filter text files, (optional)
   :type filter_text: bool
   :param filter_archive: Filter archive files, (optional)
   :type filter_archive: bool
   :param filter_btx: Filter btx files, (optional)
   :type filter_btx: bool
   :param filter_alembic: Filter Alembic files, (optional)
   :type filter_alembic: bool
   :param filter_usd: Filter USD files, (optional)
   :type filter_usd: bool
   :param filter_obj: Filter OBJ files, (optional)
   :type filter_obj: bool
   :param filter_volume: Filter OpenVDB volume files, (optional)
   :type filter_volume: bool
   :param filter_folder: Filter folders, (optional)
   :type filter_folder: bool
   :param filter_blenlib: Filter Blender IDs, (optional)
   :type filter_blenlib: bool
   :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file (in [1, 9], optional)
   :type filemode: int
   :param relative_path: Relative Path, Select the file relative to the blend file (optional)
   :type relative_path: bool
   :param display_type: Display Type, (optional)

      - ``DEFAULT``
        Default -- Automatically determine display type for files.
      - ``LIST_VERTICAL``
        Short List -- Display files as short list.
      - ``LIST_HORIZONTAL``
        Long List -- Display files as a detailed list.
      - ``THUMBNAIL``
        Thumbnails -- Display files as thumbnails.
   :type display_type: Literal['DEFAULT', 'LIST_VERTICAL', 'LIST_HORIZONTAL', 'THUMBNAIL']
   :param sort_method: File sorting mode, (optional)
   :type sort_method: str
   :param modifier: Modifier, Name of the modifier to edit (optional, never None)
   :type modifier: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: multires_higher_levels_delete(*, modifier="")

   Deletes the higher resolution mesh, potential loss of detail

   :param modifier: Modifier, Name of the modifier to edit (optional, never None)
   :type modifier: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: multires_rebuild_subdiv(*, modifier="")

   Rebuilds all possible subdivisions levels to generate a lower resolution base mesh

   :param modifier: Modifier, Name of the modifier to edit (optional, never None)
   :type modifier: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: multires_reshape(*, modifier="")

   Copy vertex coordinates from other object

   :param modifier: Modifier, Name of the modifier to edit (optional, never None)
   :type modifier: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: multires_subdivide(*, modifier="", mode='CATMULL_CLARK')

   Add a new level of subdivision

   :param modifier: Modifier, Name of the modifier to edit (optional, never None)
   :type modifier: str
   :param mode: Subdivision Mode, How the mesh is going to be subdivided to create a new level (optional)

      - ``CATMULL_CLARK``
        Catmull-Clark -- Create a new level using Catmull-Clark subdivisions.
      - ``SIMPLE``
        Simple -- Create a new level using simple subdivisions.
      - ``LINEAR``
        Linear -- Create a new level using linear interpolation of the sculpted displacement.
   :type mode: Literal['CATMULL_CLARK', 'SIMPLE', 'LINEAR']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: multires_unsubdivide(*, modifier="")

   Rebuild a lower subdivision level of the current base mesh

   :param modifier: Modifier, Name of the modifier to edit (optional, never None)
   :type modifier: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: ocean_bake(*, modifier="", free=False)

   Bake an image sequence of ocean data

   :param modifier: Modifier, Name of the modifier to edit (optional, never None)
   :type modifier: str
   :param free: Free, Free the bake, rather than generating it (optional)
   :type free: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: origin_clear()

   Clear the object's origin

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: origin_set(*, type='GEOMETRY_ORIGIN', center='MEDIAN')

   Set the object's origin, by either moving the data, or set to center of data, or use 3D cursor

   :param type: Type, (optional)

      - ``GEOMETRY_ORIGIN``
        Geometry to Origin -- Move object geometry to object origin.
      - ``ORIGIN_GEOMETRY``
        Origin to Geometry -- Calculate the center of geometry based on the current pivot point (median, otherwise bounding box).
      - ``ORIGIN_CURSOR``
        Origin to 3D Cursor -- Move object origin to position of the 3D cursor.
      - ``ORIGIN_CENTER_OF_MASS``
        Origin to Center of Mass (Surface) -- Calculate the center of mass from the surface area.
      - ``ORIGIN_CENTER_OF_VOLUME``
        Origin to Center of Mass (Volume) -- Calculate the center of mass from the volume (must be manifold geometry with consistent normals).
   :type type: Literal['GEOMETRY_ORIGIN', 'ORIGIN_GEOMETRY', 'ORIGIN_CURSOR', 'ORIGIN_CENTER_OF_MASS', 'ORIGIN_CENTER_OF_VOLUME']
   :param center: Center, (optional)
   :type center: Literal['MEDIAN', 'BOUNDS']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: parent_clear(*, type='CLEAR')

   Clear the object's parenting

   :param type: Type, (optional)

      - ``CLEAR``
        Clear Parent -- Completely clear the parenting relationship, including involved modifiers if any.
      - ``CLEAR_KEEP_TRANSFORM``
        Clear and Keep Transformation -- As 'Clear Parent', but keep the current visual transformations of the object.
      - ``CLEAR_INVERSE``
        Clear Parent Inverse -- Reset the transform corrections applied to the parenting relationship, does not remove parenting itself.
   :type type: Literal['CLEAR', 'CLEAR_KEEP_TRANSFORM', 'CLEAR_INVERSE']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: parent_inverse_apply()

   Apply the object's parent inverse to its data

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: parent_no_inverse_set(*, keep_transform=False)

   Set the object's parenting without setting the inverse parent correction

   :param keep_transform: Keep Transform, Preserve the world transform throughout parenting (optional)
   :type keep_transform: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: parent_set(*, type='OBJECT', xmirror=False, keep_transform=False)

   Set the object's parenting

   :param type: Type, (optional)
   :type type: Literal['OBJECT', 'ARMATURE', 'ARMATURE_NAME', 'ARMATURE_AUTO', 'ARMATURE_ENVELOPE', 'BONE', 'BONE_RELATIVE', 'CURVE', 'FOLLOW', 'PATH_CONST', 'LATTICE', 'VERTEX', 'VERTEX_TRI']
   :param xmirror: X Mirror, Apply weights symmetrically along X axis, for Envelope/Automatic vertex groups creation (optional)
   :type xmirror: bool
   :param keep_transform: Keep Transform, Apply transformation before parenting (optional)
   :type keep_transform: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: particle_system_add()

   Add a particle system

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: particle_system_remove()

   Remove the selected particle system

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: paste_transform(*, method='CURRENT', bake_step=0, use_mirror=False, mirror_axis_loc='x', mirror_axis_rot='z', use_relative=False)

   Pastes the matrix from the clipboard to the currently active pose bone or object. Uses world-space matrices

   :param method: Paste Method, Update the current transform, selected keyframes, or even create new keys (optional)

      - ``CURRENT``
        Current Transform -- Paste onto the current values only, only manipulating the animation data if auto-keying is enabled.
      - ``EXISTING_KEYS``
        Selected Keys -- Paste onto frames that have a selected key, potentially creating new keys on those frames.
      - ``BAKE``
        Bake on Key Range -- Paste onto all frames between the first and last selected key, creating new keyframes if necessary.
   :type method: Literal['CURRENT', 'EXISTING_KEYS', 'BAKE']
   :param bake_step: Frame Step, Only used for baking. Step=1 creates a key on every frame, step=2 bakes on 2s, etc (in [1, inf], optional)
   :type bake_step: int
   :param use_mirror: Mirror Transform, When pasting, mirror the transform relative to a specific object or bone (optional)
   :type use_mirror: bool
   :param mirror_axis_loc: Location Axis, Coordinate axis used to mirror the location part of the transform (optional)
   :type mirror_axis_loc: Literal['x', 'y', 'z']
   :param mirror_axis_rot: Rotation Axis, Coordinate axis used to mirror the rotation part of the transform (optional)
   :type mirror_axis_rot: Literal['x', 'y', 'z']
   :param use_relative: Use Relative Paste, When pasting, assume the pasted matrix is relative to another object (set in the user interface) (optional)
   :type use_relative: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/copy_global_transform.py\:325 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/copy_global_transform.py#L325>`__


.. function:: paths_calculate(*, display_type='RANGE', range='SCENE')

   Generate motion paths for the selected objects

   :param display_type: Display Type, (optional)
   :type display_type: Literal[:ref:`rna_enum_motionpath_display_type_items`]
   :param range: Computation Range, (optional)
   :type range: Literal[:ref:`rna_enum_motionpath_range_items`]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: paths_clear(*, only_selected=False)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :param only_selected: Only Selected, Only clear motion paths of selected objects (optional)
   :type only_selected: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: paths_update()

   Recalculate motion paths for selected objects

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: paths_update_visible()

   Recalculate all visible motion paths for objects and poses

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: pointcloud_random_add(*, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Add a point cloud object to the scene

   :param align: Align, The alignment of the new object (optional)

      - ``WORLD``
        World -- Align the new object to the world.
      - ``VIEW``
        View -- Align the new object to the view.
      - ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: Literal['WORLD', 'VIEW', 'CURSOR']
   :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type rotation: :class:`mathutils.Euler` | Sequence[float]
   :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type scale: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: posemode_toggle()

   Enable or disable posing/selecting bones

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: quadriflow_remesh(*, use_mesh_symmetry=True, use_preserve_sharp=False, use_preserve_boundary=False, preserve_attributes=False, smooth_normals=False, mode='FACES', target_ratio=1.0, target_edge_length=0.1, target_faces=4000, mesh_area=-1.0, seed=0)

   Create a new quad based mesh using the surface data of the current mesh. All data layers will be lost

   :param use_mesh_symmetry: Use Mesh Symmetry, Generates a symmetrical mesh using the mesh symmetry configuration (optional)
   :type use_mesh_symmetry: bool
   :param use_preserve_sharp: Preserve Sharp, Try to preserve sharp features on the mesh (optional)
   :type use_preserve_sharp: bool
   :param use_preserve_boundary: Preserve Mesh Boundary, Try to preserve mesh boundary on the mesh (optional)
   :type use_preserve_boundary: bool
   :param preserve_attributes: Preserve Attributes, Reproject attributes onto the new mesh (optional)
   :type preserve_attributes: bool
   :param smooth_normals: Smooth Normals, Set the output mesh normals to smooth (optional)
   :type smooth_normals: bool
   :param mode: Mode, How to specify the amount of detail for the new mesh (optional)

      - ``RATIO``
        Ratio -- Specify target number of faces relative to the current mesh.
      - ``EDGE``
        Edge Length -- Input target edge length in the new mesh.
      - ``FACES``
        Faces -- Input target number of faces in the new mesh.
   :type mode: Literal['RATIO', 'EDGE', 'FACES']
   :param target_ratio: Ratio, Relative number of faces compared to the current mesh (in [0, inf], optional)
   :type target_ratio: float
   :param target_edge_length: Edge Length, Target edge length in the new mesh (in [1e-07, inf], optional)
   :type target_edge_length: float
   :param target_faces: Number of Faces, Approximate number of faces (quads) in the new mesh (in [1, inf], optional)
   :type target_faces: int
   :param mesh_area: Old Object Face Area, This property is only used to cache the object area for later calculations (in [-inf, inf], optional)
   :type mesh_area: float
   :param seed: Seed, Random seed to use with the solver. Different seeds will cause the remesher to come up with different quad layouts on the mesh (in [0, inf], optional)
   :type seed: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: quick_explode(*, style='EXPLODE', amount=100, frame_duration=50, frame_start=1, frame_end=10, velocity=1.0, fade=True)

   Make selected objects explode

   :param style: Explode Style, (optional)
   :type style: Literal['EXPLODE', 'BLEND']
   :param amount: Number of Pieces, (in [2, 10000], optional)
   :type amount: int
   :param frame_duration: Duration, (in [1, 300000], optional)
   :type frame_duration: int
   :param frame_start: Start Frame, (in [1, 300000], optional)
   :type frame_start: int
   :param frame_end: End Frame, (in [1, 300000], optional)
   :type frame_end: int
   :param velocity: Outwards Velocity, (in [0, 300000], optional)
   :type velocity: float
   :param fade: Fade, Fade the pieces over time (optional)
   :type fade: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/object_quick_effects.py\:273 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object_quick_effects.py#L273>`__


.. function:: quick_fur(*, density='MEDIUM', length=0.1, radius=0.001, view_percentage=1.0, apply_hair_guides=True, use_noise=True, use_frizz=True)

   Add a fur setup to the selected objects

   :param density: Density, (optional)
   :type density: Literal['LOW', 'MEDIUM', 'HIGH']
   :param length: Length, (in [0.001, 100], optional)
   :type length: float
   :param radius: Hair Radius, (in [0, 10], optional)
   :type radius: float
   :param view_percentage: View Percentage, (in [0, 1], optional)
   :type view_percentage: float
   :param apply_hair_guides: Apply Hair Guides, (optional)
   :type apply_hair_guides: bool
   :param use_noise: Noise, (optional)
   :type use_noise: bool
   :param use_frizz: Frizz, (optional)
   :type use_frizz: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/object_quick_effects.py\:92 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object_quick_effects.py#L92>`__


.. function:: quick_liquid(*, show_flows=False)

   Make selected objects liquid

   :param show_flows: Render Liquid Objects, Keep the liquid objects visible during rendering (optional)
   :type show_flows: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/object_quick_effects.py\:553 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object_quick_effects.py#L553>`__


.. function:: quick_smoke(*, style='SMOKE', show_flows=False)

   Use selected objects as smoke emitters

   :param style: Smoke Style, (optional)
   :type style: Literal['SMOKE', 'FIRE', 'BOTH']
   :param show_flows: Render Smoke Objects, Keep the smoke objects visible during rendering (optional)
   :type show_flows: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/object_quick_effects.py\:447 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object_quick_effects.py#L447>`__


.. function:: randomize_transform(*, random_seed=0, use_delta=False, use_loc=True, loc=(0.0, 0.0, 0.0), use_rot=True, rot=(0.0, 0.0, 0.0), use_scale=True, scale_even=False, scale=(1.0, 1.0, 1.0))

   Randomize objects location, rotation, and scale

   :param random_seed: Random Seed, Seed value for the random generator (in [0, 10000], optional)
   :type random_seed: int
   :param use_delta: Transform Delta, Randomize delta transform values instead of regular transform (optional)
   :type use_delta: bool
   :param use_loc: Randomize Location, Randomize the location values (optional)
   :type use_loc: bool
   :param loc: Location, Maximum distance the objects can spread over each axis (array of 3 items, in [-100, 100], optional)
   :type loc: :class:`mathutils.Vector` | Sequence[float]
   :param use_rot: Randomize Rotation, Randomize the rotation values (optional)
   :type use_rot: bool
   :param rot: Rotation, Maximum rotation over each axis (array of 3 items, in [-3.14159, 3.14159], optional)
   :type rot: :class:`mathutils.Euler` | Sequence[float]
   :param use_scale: Randomize Scale, Randomize the scale values (optional)
   :type use_scale: bool
   :param scale_even: Scale Even, Use the same scale value for all axis (optional)
   :type scale_even: bool
   :param scale: Scale, Maximum scale randomization over each axis (array of 3 items, in [-100, 100], optional)
   :type scale: Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/object_randomize_transform.py\:163 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object_randomize_transform.py#L163>`__


.. function:: reset_override_library()

   Reset the selected local overrides to their linked references values

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: rotation_clear(*, clear_delta=False)

   Clear the object's rotation

   :param clear_delta: Clear Delta, Clear delta rotation in addition to clearing the normal rotation transform (optional)
   :type clear_delta: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: scale_clear(*, clear_delta=False)

   Clear the object's scale

   :param clear_delta: Clear Delta, Clear delta scale in addition to clearing the normal scale transform (optional)
   :type clear_delta: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_all(*, action='TOGGLE')

   Change selection of all visible objects in scene

   :param action: Action, Selection action to execute (optional)

      - ``TOGGLE``
        Toggle -- Toggle selection for all elements.
      - ``SELECT``
        Select -- Select all elements.
      - ``DESELECT``
        Deselect -- Deselect all elements.
      - ``INVERT``
        Invert -- Invert selection of all elements.
   :type action: Literal['TOGGLE', 'SELECT', 'DESELECT', 'INVERT']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_by_type(*, extend=False, type='MESH')

   Select all visible objects that are of a type

   :param extend: Extend, Extend selection instead of deselecting everything first (optional)
   :type extend: bool
   :param type: Type, (optional)
   :type type: Literal[:ref:`rna_enum_object_type_items`]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_camera(*, extend=False)

   Select the active camera

   :param extend: Extend, Extend the selection (optional)
   :type extend: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/object.py\:124 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L124>`__


.. function:: select_grouped(*, extend=False, type='CHILDREN_RECURSIVE')

   Select all visible objects grouped by various properties

   :param extend: Extend, Extend selection instead of deselecting everything first (optional)
   :type extend: bool
   :param type: Type, (optional)

      - ``CHILDREN_RECURSIVE``
        Children.
      - ``CHILDREN``
        Immediate Children.
      - ``PARENT``
        Parent.
      - ``SIBLINGS``
        Siblings -- Shared parent.
      - ``TYPE``
        Type -- Shared object type.
      - ``COLLECTION``
        Collection -- Shared collection.
      - ``HOOK``
        Hook.
      - ``PASS``
        Pass -- Render pass index.
      - ``COLOR``
        Color -- Object color.
      - ``KEYINGSET``
        Keying Set -- Objects included in active Keying Set.
      - ``LIGHT_TYPE``
        Light Type -- Matching light types.
   :type type: Literal['CHILDREN_RECURSIVE', 'CHILDREN', 'PARENT', 'SIBLINGS', 'TYPE', 'COLLECTION', 'HOOK', 'PASS', 'COLOR', 'KEYINGSET', 'LIGHT_TYPE']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_hierarchy(*, direction='PARENT', extend=False)

   Select object relative to the active object's position in the hierarchy

   :param direction: Direction, Direction to select in the hierarchy (optional)
   :type direction: Literal['PARENT', 'CHILD']
   :param extend: Extend, Extend the existing selection (optional)
   :type extend: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/object.py\:174 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L174>`__


.. function:: select_less()

   Deselect objects at the boundaries of parent/child relationships

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select_linked(*, extend=False, type='OBDATA')

   Select all visible objects that are linked

   :param extend: Extend, Extend selection instead of deselecting everything first (optional)
   :type extend: bool
   :param type: Type, (optional)
   :type type: Literal['OBDATA', 'MATERIAL', 'DUPGROUP', 'PARTICLE', 'LIBRARY', 'LIBRARY_OBDATA']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_mirror(*, extend=False)

   Select the mirror objects of the selected object e.g. "L.sword" and "R.sword"

   :param extend: Extend, Extend selection instead of deselecting everything first (optional)
   :type extend: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_more()

   Select connected parent/child objects

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select_pattern(*, pattern="*", case_sensitive=False, extend=True)

   Select objects matching a naming pattern

   :param pattern: Pattern, Name filter using '*', '?' and '[abc]' unix style wildcards (optional, never None)
   :type pattern: str
   :param case_sensitive: Case Sensitive, Do a case sensitive compare (optional)
   :type case_sensitive: bool
   :param extend: Extend, Extend the existing selection (optional)
   :type extend: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/object.py\:45 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L45>`__


.. function:: select_random(*, ratio=0.5, seed=0, action='SELECT')

   Select or deselect random visible objects

   :param ratio: Ratio, Portion of items to select randomly (in [0, 1], optional)
   :type ratio: float
   :param seed: Random Seed, Seed for the random number generator (in [0, inf], optional)
   :type seed: int
   :param action: Action, Selection action to execute (optional)

      - ``SELECT``
        Select -- Select all elements.
      - ``DESELECT``
        Deselect -- Deselect all elements.
   :type action: Literal['SELECT', 'DESELECT']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_same_collection(*, collection="")

   Select object in the same collection

   :param collection: Collection, Name of the collection to select (optional, never None)
   :type collection: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: shade_auto_smooth(*, use_auto_smooth=True, angle=0.523599)

   Add modifier to automatically set the sharpness of mesh edges based on the angle between the neighboring faces

   :param use_auto_smooth: Auto Smooth, Add modifier to set edge sharpness automatically (optional)
   :type use_auto_smooth: bool
   :param angle: Angle, Maximum angle between face normals that will be considered as smooth (in [0, 3.14159], optional)
   :type angle: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: shade_flat(*, keep_sharp_edges=True)

   Render and display faces uniform, using face normals

   :param keep_sharp_edges: Keep Sharp Edges, Don't remove sharp edges, which are redundant with faces shaded smooth (optional)
   :type keep_sharp_edges: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: shade_smooth(*, keep_sharp_edges=True)

   Render and display faces smooth, using interpolated vertex normals

   :param keep_sharp_edges: Keep Sharp Edges, Don't remove sharp edges. Tagged edges will remain sharp (optional)
   :type keep_sharp_edges: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: shade_smooth_by_angle(*, angle=0.523599, keep_sharp_edges=True)

   Set the sharpness of mesh edges based on the angle between the neighboring faces

   :param angle: Angle, Maximum angle between face normals that will be considered as smooth (in [0, 3.14159], optional)
   :type angle: float
   :param keep_sharp_edges: Keep Sharp Edges, Only add sharp edges instead of clearing existing tags first (optional)
   :type keep_sharp_edges: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: shaderfx_add(*, type='FX_BLUR')

   Add a visual effect to the active object

   :param type: Type, (optional)
   :type type: Literal[:ref:`rna_enum_object_shaderfx_type_items`]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: shaderfx_copy(*, shaderfx="")

   Duplicate effect at the same position in the stack

   :param shaderfx: Shader, Name of the shaderfx to edit (optional, never None)
   :type shaderfx: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: shaderfx_move_down(*, shaderfx="")

   Move effect down in the stack

   :param shaderfx: Shader, Name of the shaderfx to edit (optional, never None)
   :type shaderfx: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: shaderfx_move_to_index(*, shaderfx="", index=0)

   Change the effect's position in the list so it evaluates after the set number of others

   :param shaderfx: Shader, Name of the shaderfx to edit (optional, never None)
   :type shaderfx: str
   :param index: Index, The index to move the effect to (in [0, inf], optional)
   :type index: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: shaderfx_move_up(*, shaderfx="")

   Move effect up in the stack

   :param shaderfx: Shader, Name of the shaderfx to edit (optional, never None)
   :type shaderfx: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: shaderfx_remove(*, shaderfx="", report=False)

   Remove a effect from the active Grease Pencil object

   :param shaderfx: Shader, Name of the shaderfx to edit (optional, never None)
   :type shaderfx: str
   :param report: Report, Create a notification after the operation (optional)
   :type report: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: shape_key_add(*, from_mix=True)

   Add shape key to the object

   :param from_mix: From Mix, Create the new shape key from the existing mix of keys (optional)
   :type from_mix: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: shape_key_apply_to_basis()

   Apply deformations of selected shape keys to the basis key, removing them

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: shape_key_clear()

   Reset the weights of all shape keys to 0 or to the closest value respecting the limits

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: shape_key_copy()

   Duplicate the active shape key

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: shape_key_lock(*, action='LOCK')

   Change the lock state of all shape keys of active object

   :param action: Action, Lock action to execute on vertex groups (optional)

      - ``LOCK``
        Lock -- Lock all shape keys.
      - ``UNLOCK``
        Unlock -- Unlock all shape keys.
   :type action: Literal['LOCK', 'UNLOCK']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: shape_key_make_basis()

   Make this shape key the new basis key, effectively applying it to the mesh. Note that this applies the shape key at its 100% value

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: shape_key_mirror(*, use_topology=False)

   Mirror the current shape key along the local X axis

   :param use_topology: Topology Mirror, Use topology based mirroring (for when both sides of mesh have matching, unique topology) (optional)
   :type use_topology: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: shape_key_move(*, type='TOP')

   Move selected shape keys up/down in the list

   :param type: Type, (optional)

      - ``TOP``
        Top -- Top of the list.
      - ``UP``
        Up.
      - ``DOWN``
        Down.
      - ``BOTTOM``
        Bottom -- Bottom of the list.
   :type type: Literal['TOP', 'UP', 'DOWN', 'BOTTOM']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: shape_key_remove(*, all=False, apply_mix=False)

   Remove shape key from the object

   :param all: All, Remove all shape keys (optional)
   :type all: bool
   :param apply_mix: Apply Mix, Apply current mix of shape keys to the geometry before removing them (optional)
   :type apply_mix: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: shape_key_retime()

   Resets the timing for absolute shape keys

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: shape_key_transfer(*, mode='OFFSET', use_clamp=False)

   Copy the active shape key of another selected object to this one

   :param mode: Transformation Mode, Relative shape positions to the new shape method (optional)

      - ``OFFSET``
        Offset -- Apply the relative positional offset.
      - ``RELATIVE_FACE``
        Relative Face -- Calculate relative position (using faces).
      - ``RELATIVE_EDGE``
        Relative Edge -- Calculate relative position (using edges).
   :type mode: Literal['OFFSET', 'RELATIVE_FACE', 'RELATIVE_EDGE']
   :param use_clamp: Clamp Offset, Clamp the transformation to the distance each vertex moves in the original shape (optional)
   :type use_clamp: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/object.py\:515 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L515>`__


.. function:: simulation_nodes_cache_bake(*, selected=False)

   Bake simulations in geometry nodes modifiers

   :param selected: Selected, Bake cache on all selected objects (optional)
   :type selected: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: simulation_nodes_cache_calculate_to_frame(*, selected=False)

   Calculate simulations in geometry nodes modifiers from the start to current frame

   :param selected: Selected, Calculate all selected objects instead of just the active object (optional)
   :type selected: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: simulation_nodes_cache_delete(*, selected=False)

   Delete cached/baked simulations in geometry nodes modifiers

   :param selected: Selected, Delete cache on all selected objects (optional)
   :type selected: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: skin_armature_create(*, modifier="")

   Create an armature that parallels the skin layout

   :param modifier: Modifier, Name of the modifier to edit (optional, never None)
   :type modifier: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: skin_loose_mark_clear(*, action='MARK')

   Mark/clear selected vertices as loose

   :param action: Action, (optional)

      - ``MARK``
        Mark -- Mark selected vertices as loose.
      - ``CLEAR``
        Clear -- Set selected vertices as not loose.
   :type action: Literal['MARK', 'CLEAR']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: skin_radii_equalize()

   Make skin radii of selected vertices equal on each axis

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: skin_root_mark()

   Mark selected vertices as roots

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: speaker_add(*, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Add a speaker object to the scene

   :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object (optional)
   :type enter_editmode: bool
   :param align: Align, The alignment of the new object (optional)

      - ``WORLD``
        World -- Align the new object to the world.
      - ``VIEW``
        View -- Align the new object to the view.
      - ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: Literal['WORLD', 'VIEW', 'CURSOR']
   :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type rotation: :class:`mathutils.Euler` | Sequence[float]
   :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type scale: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: subdivision_set(*, level=1, relative=False, ensure_modifier=True)

   Sets a Subdivision Surface level (1 to 5)

   :param level: Level, (in [-100, 100], optional)
   :type level: int
   :param relative: Relative, Apply the subdivision surface level as an offset relative to the current level (optional)
   :type relative: bool
   :param ensure_modifier: Ensure Modifier, Create the corresponding modifier if it does not exist (optional)
   :type ensure_modifier: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/object.py\:242 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L242>`__


.. function:: surfacedeform_bind(*, modifier="")

   Bind mesh to target in surface deform modifier

   :param modifier: Modifier, Name of the modifier to edit (optional, never None)
   :type modifier: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: text_add(*, radius=1.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Add a text object to the scene

   :param radius: Radius, (in [0, inf], optional)
   :type radius: float
   :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object (optional)
   :type enter_editmode: bool
   :param align: Align, The alignment of the new object (optional)

      - ``WORLD``
        World -- Align the new object to the world.
      - ``VIEW``
        View -- Align the new object to the view.
      - ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: Literal['WORLD', 'VIEW', 'CURSOR']
   :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type rotation: :class:`mathutils.Euler` | Sequence[float]
   :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type scale: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: track_clear(*, type='CLEAR')

   Clear tracking constraint or flag from object

   :param type: Type, (optional)
   :type type: Literal['CLEAR', 'CLEAR_KEEP_TRANSFORM']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: track_set(*, type='DAMPTRACK')

   Make the object track another object, using various methods/constraints

   :param type: Type, (optional)
   :type type: Literal['DAMPTRACK', 'TRACKTO', 'LOCKTRACK']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: transfer_mode(*, use_flash_on_transfer=True)

   Switches the active object and assigns the same mode to a new one under the mouse cursor, leaving the active mode in the current one

   :param use_flash_on_transfer: Flash On Transfer, Flash the target object when transferring the mode (optional)
   :type use_flash_on_transfer: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: transform_apply(*, location=True, rotation=True, scale=True, properties=True, corrective_flip_normals=True, isolate_users=False)

   Apply the object's transformation to its data

   :param location: Location, (optional)
   :type location: bool
   :param rotation: Rotation, (optional)
   :type rotation: bool
   :param scale: Scale, (optional)
   :type scale: bool
   :param properties: Apply Properties, Modify properties such as curve vertex radius, font size and bone envelope (optional)
   :type properties: bool
   :param corrective_flip_normals: Corrective Flip Normals, Invert normals for negative scaled objects. (optional)
   :type corrective_flip_normals: bool
   :param isolate_users: Isolate Multi User Data, Create new object-data users if needed (optional)
   :type isolate_users: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: transform_axis_target()

   Interactively point cameras and lights to a location (Ctrl translates)

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: transform_to_mouse(*, name="", session_uid=0, matrix=((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)), drop_x=0, drop_y=0)

   Snap selected item(s) to the mouse location

   :param name: Name, Object name to place (uses the active object when this and 'session_uid' are unset) (optional, never None)
   :type name: str
   :param session_uid: Session UUID, Session UUID of the object to place (uses the active object when this and 'name' are unset) (in [-inf, inf], optional)
   :type session_uid: int
   :param matrix: Matrix, (multi-dimensional array of 4 * 4 items, in [-inf, inf], optional)
   :type matrix: :class:`mathutils.Matrix` | Sequence[Sequence[float]]
   :param drop_x: Drop X, X-coordinate (screen space) to place the new object under (in [-inf, inf], optional)
   :type drop_x: int
   :param drop_y: Drop Y, Y-coordinate (screen space) to place the new object under (in [-inf, inf], optional)
   :type drop_y: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: transforms_to_deltas(*, mode='ALL', reset_values=True)

   Convert normal object transforms to delta transforms, any existing delta transforms will be included as well

   :param mode: Mode, Which transforms to transfer (optional)

      - ``ALL``
        All Transforms -- Transfer location, rotation, and scale transforms.
      - ``LOC``
        Location -- Transfer location transforms only.
      - ``ROT``
        Rotation -- Transfer rotation transforms only.
      - ``SCALE``
        Scale -- Transfer scale transforms only.
   :type mode: Literal['ALL', 'LOC', 'ROT', 'SCALE']
   :param reset_values: Reset Values, Clear transform values after transferring to deltas (optional)
   :type reset_values: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/object.py\:777 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L777>`__


.. function:: unlink_data()

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: update_shapes(*, use_mirror=False)

   Update existing shape keys with the vertex positions of selected objects with matching names

   :param use_mirror: Mirror, Mirror the new shape key values (optional)
   :type use_mirror: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: vertex_group_add()

   Add a new vertex group to the active object

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: vertex_group_assign()

   Assign the selected vertices to the active vertex group

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: vertex_group_assign_new()

   Assign the selected vertices to a new vertex group

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: vertex_group_clean(*, group_select_mode='', limit=0.0, keep_single=False)

   Remove vertex group assignments which are not required

   :param group_select_mode: Subset, Define which subset of groups shall be used (optional)
   :type group_select_mode: str
   :param limit: Limit, Remove vertices which weight is below or equal to this limit (in [0, 1], optional)
   :type limit: float
   :param keep_single: Keep Single, Keep verts assigned to at least one group when cleaning (optional)
   :type keep_single: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: vertex_group_copy()

   Make a copy of the active vertex group

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: vertex_group_copy_to_selected()

   Replace vertex groups of selected objects by vertex groups of active object

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: vertex_group_deselect()

   Deselect all selected vertices assigned to the active vertex group

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: vertex_group_invert(*, group_select_mode='', auto_assign=True, auto_remove=True)

   Invert active vertex group's weights

   :param group_select_mode: Subset, Define which subset of groups shall be used (optional)
   :type group_select_mode: str
   :param auto_assign: Add Weights, Add vertices from groups that have zero weight before inverting (optional)
   :type auto_assign: bool
   :param auto_remove: Remove Weights, Remove vertices from groups that have zero weight after inverting (optional)
   :type auto_remove: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: vertex_group_levels(*, group_select_mode='', offset=0.0, gain=1.0)

   Add some offset and multiply with some gain the weights of the active vertex group

   :param group_select_mode: Subset, Define which subset of groups shall be used (optional)
   :type group_select_mode: str
   :param offset: Offset, Value to add to weights (in [-1, 1], optional)
   :type offset: float
   :param gain: Gain, Value to multiply weights by (in [0, inf], optional)
   :type gain: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: vertex_group_limit_total(*, group_select_mode='', limit=4)

   Limit deform weights associated with a vertex to a specified number by removing lowest weights

   :param group_select_mode: Subset, Define which subset of groups shall be used (optional)
   :type group_select_mode: str
   :param limit: Limit, Maximum number of deform weights (in [1, 32], optional)
   :type limit: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: vertex_group_lock(*, action='TOGGLE', mask='ALL')

   Change the lock state of all or some vertex groups of active object

   :param action: Action, Lock action to execute on vertex groups (optional)

      - ``TOGGLE``
        Toggle -- Unlock all vertex groups if there is at least one locked group, lock all in other case.
      - ``LOCK``
        Lock -- Lock all vertex groups.
      - ``UNLOCK``
        Unlock -- Unlock all vertex groups.
      - ``INVERT``
        Invert -- Invert the lock state of all vertex groups.
   :type action: Literal['TOGGLE', 'LOCK', 'UNLOCK', 'INVERT']
   :param mask: Mask, Apply the action based on vertex group selection (optional)

      - ``ALL``
        All -- Apply action to all vertex groups.
      - ``SELECTED``
        Selected -- Apply to selected vertex groups.
      - ``UNSELECTED``
        Unselected -- Apply to unselected vertex groups.
      - ``INVERT_UNSELECTED``
        Invert Unselected -- Apply the opposite of Lock/Unlock to unselected vertex groups.
   :type mask: Literal['ALL', 'SELECTED', 'UNSELECTED', 'INVERT_UNSELECTED']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: vertex_group_mirror(*, mirror_weights=True, flip_group_names=True, all_groups=False, use_topology=False)

   Mirror vertex group, flip weights and/or names, editing only selected vertices, flipping when both sides are selected otherwise copy from unselected

   :param mirror_weights: Mirror Weights, Mirror weights (optional)
   :type mirror_weights: bool
   :param flip_group_names: Flip Group Names, Flip vertex group names (optional)
   :type flip_group_names: bool
   :param all_groups: All Groups, Mirror all vertex groups weights (optional)
   :type all_groups: bool
   :param use_topology: Topology Mirror, Use topology based mirroring (for when both sides of mesh have matching, unique topology) (optional)
   :type use_topology: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: vertex_group_move(*, direction='UP')

   Move the active vertex group up/down in the list

   :param direction: Direction, Direction to move the active vertex group towards (optional)
   :type direction: Literal['UP', 'DOWN']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: vertex_group_normalize()

   Normalize weights of the active vertex group, so that the highest ones are now 1.0

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: vertex_group_normalize_all(*, group_select_mode='', lock_active=True)

   Normalize all weights of all vertex groups, so that for each vertex, the sum of all weights is 1.0

   :param group_select_mode: Subset, Define which subset of groups shall be used (optional)
   :type group_select_mode: str
   :param lock_active: Lock Active, Keep the values of the active group while normalizing others (optional)
   :type lock_active: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: vertex_group_quantize(*, group_select_mode='', steps=4)

   Set weights to a fixed number of steps

   :param group_select_mode: Subset, Define which subset of groups shall be used (optional)
   :type group_select_mode: str
   :param steps: Steps, Number of steps between 0 and 1 (in [1, 1000], optional)
   :type steps: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: vertex_group_remove(*, all=False, all_unlocked=False)

   Delete the active or all vertex groups from the active object

   :param all: All, Remove all vertex groups (optional)
   :type all: bool
   :param all_unlocked: All Unlocked, Remove all unlocked vertex groups (optional)
   :type all_unlocked: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: vertex_group_remove_from(*, use_all_groups=False, use_all_verts=False)

   Remove the selected vertices from active or all vertex group(s)

   :param use_all_groups: All Groups, Remove from all groups (optional)
   :type use_all_groups: bool
   :param use_all_verts: All Vertices, Clear the active group (optional)
   :type use_all_verts: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: vertex_group_select()

   Select all the vertices assigned to the active vertex group

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: vertex_group_set_active(*, group='')

   Set the active vertex group

   :param group: Group, Vertex group to set as active (optional)
   :type group: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: vertex_group_smooth(*, group_select_mode='', factor=0.5, repeat=1, expand=0.0)

   Smooth weights for selected vertices

   :param group_select_mode: Subset, Define which subset of groups shall be used (optional)
   :type group_select_mode: str
   :param factor: Factor, (in [0, 1], optional)
   :type factor: float
   :param repeat: Iterations, (in [1, 10000], optional)
   :type repeat: int
   :param expand: Expand/Contract, Expand/contract weights (in [-1, 1], optional)
   :type expand: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: vertex_group_sort(*, sort_type='NAME')

   Sort vertex groups

   :param sort_type: Sort Type, Sort type (optional)
   :type sort_type: Literal['NAME', 'BONE_HIERARCHY']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: vertex_parent_set()

   Parent selected objects to the selected vertices

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: vertex_weight_copy()

   Copy weights from active to selected

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: vertex_weight_delete(*, weight_group=-1)

   Delete this weight from the vertex (disabled if vertex group is locked)

   :param weight_group: Weight Index, Index of source weight in active vertex group (in [-1, inf], optional)
   :type weight_group: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: vertex_weight_normalize_active_vertex()

   Normalize active vertex's weights

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: vertex_weight_paste(*, weight_group=-1)

   Copy this group's weight to other selected vertices (disabled if vertex group is locked)

   :param weight_group: Weight Index, Index of source weight in active vertex group (in [-1, inf], optional)
   :type weight_group: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: vertex_weight_set_active(*, weight_group=-1)

   Set as active vertex group

   :param weight_group: Weight Index, Index of source weight in active vertex group (in [-1, inf], optional)
   :type weight_group: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: visual_geometry_to_objects()

   Convert geometry and instances into editable objects and collections

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: visual_transform_apply()

   Apply the object's visual transformation to its data

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: volume_add(*, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Add a volume object to the scene

   :param align: Align, The alignment of the new object (optional)

      - ``WORLD``
        World -- Align the new object to the world.
      - ``VIEW``
        View -- Align the new object to the view.
      - ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: Literal['WORLD', 'VIEW', 'CURSOR']
   :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type rotation: :class:`mathutils.Euler` | Sequence[float]
   :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type scale: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: volume_import(*, filepath="", directory="", files=None, hide_props_region=True, check_existing=False, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=True, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, display_type='DEFAULT', sort_method='', use_sequence_detection=True, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Import OpenVDB volume file

   :param filepath: File Path, Path to file (optional, never None)
   :type filepath: str
   :param directory: Directory, Directory of the file (optional, never None)
   :type directory: str
   :param files: Files, (optional)
   :type files: :class:`bpy_prop_collection`\ [:class:`OperatorFileListElement`] | None
   :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings (optional)
   :type hide_props_region: bool
   :param check_existing: Check Existing, Check and warn on overwriting existing files (optional)
   :type check_existing: bool
   :param filter_blender: Filter .blend files, (optional)
   :type filter_blender: bool
   :param filter_backup: Filter backup .blend files, (optional)
   :type filter_backup: bool
   :param filter_image: Filter image files, (optional)
   :type filter_image: bool
   :param filter_movie: Filter movie files, (optional)
   :type filter_movie: bool
   :param filter_python: Filter Python files, (optional)
   :type filter_python: bool
   :param filter_font: Filter font files, (optional)
   :type filter_font: bool
   :param filter_sound: Filter sound files, (optional)
   :type filter_sound: bool
   :param filter_text: Filter text files, (optional)
   :type filter_text: bool
   :param filter_archive: Filter archive files, (optional)
   :type filter_archive: bool
   :param filter_btx: Filter btx files, (optional)
   :type filter_btx: bool
   :param filter_alembic: Filter Alembic files, (optional)
   :type filter_alembic: bool
   :param filter_usd: Filter USD files, (optional)
   :type filter_usd: bool
   :param filter_obj: Filter OBJ files, (optional)
   :type filter_obj: bool
   :param filter_volume: Filter OpenVDB volume files, (optional)
   :type filter_volume: bool
   :param filter_folder: Filter folders, (optional)
   :type filter_folder: bool
   :param filter_blenlib: Filter Blender IDs, (optional)
   :type filter_blenlib: bool
   :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file (in [1, 9], optional)
   :type filemode: int
   :param relative_path: Relative Path, Select the file relative to the blend file (optional)
   :type relative_path: bool
   :param display_type: Display Type, (optional)

      - ``DEFAULT``
        Default -- Automatically determine display type for files.
      - ``LIST_VERTICAL``
        Short List -- Display files as short list.
      - ``LIST_HORIZONTAL``
        Long List -- Display files as a detailed list.
      - ``THUMBNAIL``
        Thumbnails -- Display files as thumbnails.
   :type display_type: Literal['DEFAULT', 'LIST_VERTICAL', 'LIST_HORIZONTAL', 'THUMBNAIL']
   :param sort_method: File sorting mode, (optional)
   :type sort_method: str
   :param use_sequence_detection: Detect Sequences, Automatically detect animated sequences in selected volume files (based on file names) (optional)
   :type use_sequence_detection: bool
   :param align: Align, The alignment of the new object (optional)

      - ``WORLD``
        World -- Align the new object to the world.
      - ``VIEW``
        View -- Align the new object to the view.
      - ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: Literal['WORLD', 'VIEW', 'CURSOR']
   :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type rotation: :class:`mathutils.Euler` | Sequence[float]
   :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type scale: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: voxel_remesh()

   Calculates a new manifold mesh based on the volume of the current mesh. All data layers will be lost

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: voxel_size_edit()

   Modify the mesh voxel size interactively used in the voxel remesher

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
