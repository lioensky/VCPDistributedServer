Object(ID)
==========

.. currentmodule:: bpy.types


Basic Object Operations Example
+++++++++++++++++++++++++++++++

This script demonstrates basic operations on object like creating new
object, placing it into a view layer, selecting it and making it active.

.. literalinclude:: ./examples/bpy.types.Object.0.py
   :lines: 9-

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: Object(ID)

   Object data-block defining an object in a scene

   .. attribute:: active_material

      Active material being displayed

      :type: :class:`Material` | None

   .. attribute:: active_material_index

      Index of active material slot (in [0, inf], default 0)

      :type: int

   .. attribute:: active_selection_set

      Index of the currently active selection set (in [-inf, inf], default 0)

      :type: int

   .. data:: active_shape_key

      Current shape key (readonly)

      :type: :class:`ShapeKey` | None

   .. attribute:: active_shape_key_index

      Current shape key index (in [-32768, 32767], default 0)

      :type: int

   .. attribute:: add_rest_position_attribute

      Add a "rest_position" attribute that is a copy of the position attribute before shape keys and modifiers are evaluated (default False)

      :type: bool

   .. data:: animation_data

      Animation data for this data-block (readonly)

      :type: :class:`AnimData` | None

   .. data:: animation_visualization

      Animation data for this data-block (readonly, never None)

      :type: :class:`AnimViz`

   .. data:: bound_box

      Object's bounding box in object-space coordinates, all values are -1.0 when not available (multi-dimensional array of 8 * 3 items, in [-inf, inf], default ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)), readonly)

      :type: :class:`bpy_prop_array`\ [float]

   .. data:: collision

      Settings for using the object as a collider in physics simulation (readonly)

      :type: :class:`CollisionSettings` | None

   .. attribute:: color

      Object color and alpha, used when the Object Color mode is enabled (array of 4 items, in [0, inf], default (1.0, 1.0, 1.0, 1.0))

      :type: :class:`bpy_prop_array`\ [float]

   .. data:: constraints

      Constraints affecting the transformation of the object (default None, readonly)

      :type: :class:`ObjectConstraints`\ [:class:`Constraint`]

   .. attribute:: data

      Object data

      :type: :class:`ID` | None

   .. attribute:: delta_location

      Extra translation added to the location of the object (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: delta_rotation_euler

      Extra rotation added to the rotation of the object (when using Euler rotations) (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Euler`

   .. attribute:: delta_rotation_quaternion

      Extra rotation added to the rotation of the object (when using Quaternion rotations) (array of 4 items, in [-inf, inf], default (1.0, 0.0, 0.0, 0.0))

      :type: :class:`mathutils.Quaternion`

   .. attribute:: delta_scale

      Extra scaling added to the scale of the object (array of 3 items, in [-inf, inf], default (1.0, 1.0, 1.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: dimensions

      Absolute bounding box dimensions of the object.
      Warning: Assigning to it or its members multiple consecutive times will not work correctly, as this needs up-to-date evaluated data
      
      (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. data:: display

      Object display settings for 3D viewport (readonly, never None)

      :type: :class:`ObjectDisplay`

   .. attribute:: display_bounds_type

      Object boundary display type (default ``'BOX'``)

      - ``BOX``
        Box -- Display bounds as box.
      - ``SPHERE``
        Sphere -- Display bounds as sphere.
      - ``CYLINDER``
        Cylinder -- Display bounds as cylinder.
      - ``CONE``
        Cone -- Display bounds as cone.
      - ``CAPSULE``
        Capsule -- Display bounds as capsule.

      :type: Literal['BOX', 'SPHERE', 'CYLINDER', 'CONE', 'CAPSULE']

   .. attribute:: display_type

      How to display object in viewport (default ``'TEXTURED'``)

      - ``BOUNDS``
        Bounds -- Display the bounds of the object.
      - ``WIRE``
        Wire -- Display the object as a wireframe.
      - ``SOLID``
        Solid -- Display the object as a solid (if solid drawing is enabled in the viewport).
      - ``TEXTURED``
        Textured -- Display the object with textures (if textures are enabled in the viewport).

      :type: Literal['BOUNDS', 'WIRE', 'SOLID', 'TEXTURED']

   .. attribute:: empty_display_size

      Size of display for empties in the viewport (in [0.0001, 1000], default 1.0)

      :type: float

   .. attribute:: empty_display_type

      Viewport display style for empties (default ``'PLAIN_AXES'``)

      :type: Literal[:ref:`rna_enum_object_empty_drawtype_items`]

   .. attribute:: empty_image_depth

      Determine which other objects will occlude the image (default ``'DEFAULT'``)

      :type: Literal['DEFAULT', 'FRONT', 'BACK']

   .. attribute:: empty_image_offset

      Origin offset distance (array of 2 items, in [-inf, inf], default (-0.5, -0.5))

      :type: :class:`bpy_prop_array`\ [float]

   .. attribute:: empty_image_side

      Show front/back side (default ``'DOUBLE_SIDED'``)

      :type: Literal['DOUBLE_SIDED', 'FRONT', 'BACK']

   .. data:: field

      Settings for using the object as a field in physics simulation (readonly)

      :type: :class:`FieldSettings` | None

   .. attribute:: hide_probe_plane

      Globally disable in planar light probes (default False)

      :type: bool

   .. attribute:: hide_probe_sphere

      Globally disable in spherical light probes (default False)

      :type: bool

   .. attribute:: hide_probe_volume

      Globally disable in volume probes (default False)

      :type: bool

   .. attribute:: hide_render

      Globally disable in renders (default False)

      :type: bool

   .. attribute:: hide_select

      Disable selection in viewport (default False)

      :type: bool

   .. attribute:: hide_surface_pick

      Disable surface influence during selection, snapping and depth-picking operators. Usually used to avoid semi-transparent objects to affect scene navigation (default False)

      :type: bool

   .. attribute:: hide_viewport

      Globally disable in viewports (default False)

      :type: bool

   .. data:: image_user

      Parameters defining which layer, pass and frame of the image is displayed (readonly, never None)

      :type: :class:`ImageUser`

   .. attribute:: instance_collection

      Instance an existing collection

      :type: :class:`Collection` | None

   .. attribute:: instance_faces_scale

      Scale the face instance objects (in [0.001, 10000], default 1.0)

      :type: float

   .. attribute:: instance_type

      If not None, object instancing method to use (default ``'NONE'``)

      - ``NONE``
        None.
      - ``VERTS``
        Vertices -- Instantiate child objects on all vertices.
      - ``FACES``
        Faces -- Instantiate child objects on all faces.
      - ``COLLECTION``
        Collection -- Enable collection instancing.

      :type: Literal['NONE', 'VERTS', 'FACES', 'COLLECTION']

   .. data:: is_from_instancer

      Object comes from a instancer (default False, readonly)

      :type: bool

   .. data:: is_from_set

      Object comes from a background set (default False, readonly)

      :type: bool

   .. attribute:: is_holdout

      Render objects as a holdout or matte, creating a hole in the image with zero alpha, to fill out in compositing with real footage or another render (default False)

      :type: bool

   .. data:: is_instancer

      (default False, readonly)

      :type: bool

   .. attribute:: is_shadow_catcher

      Only render shadows and reflections on this object, for compositing renders into real footage. Objects with this setting are considered to already exist in the footage, objects without it are synthetic objects being composited into it. (default False)

      :type: bool

   .. data:: light_linking

      Light linking settings (readonly, never None)

      :type: :class:`ObjectLightLinking`

   .. attribute:: lightgroup

      Lightgroup that the object belongs to (default "", never None)

      :type: str

   .. data:: lineart

      Line Art settings for the object (readonly)

      :type: :class:`ObjectLineArt` | None

   .. attribute:: location

      Location of the object (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: lock_location

      Lock editing of location when transforming (array of 3 items, default (False, False, False))

      :type: :class:`bpy_prop_array`\ [bool]

   .. attribute:: lock_rotation

      Lock editing of rotation when transforming (array of 3 items, default (False, False, False))

      :type: :class:`bpy_prop_array`\ [bool]

   .. attribute:: lock_rotation_w

      Lock editing of 'angle' component of four-component rotations when transforming (default False)

      :type: bool

   .. attribute:: lock_rotations_4d

      Lock editing of four component rotations by components (instead of as Eulers) (default True)

      :type: bool

   .. attribute:: lock_scale

      Lock editing of scale when transforming (array of 3 items, default (False, False, False))

      :type: :class:`bpy_prop_array`\ [bool]

   .. data:: material_slots

      Material slots in the object (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`MaterialSlot`]

   .. attribute:: matrix_basis

      Matrix access to location, rotation and scale (including deltas), before constraints and parenting are applied (multi-dimensional array of 4 * 4 items, in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)))

      :type: :class:`mathutils.Matrix`

   .. attribute:: matrix_local

      Parent relative transformation matrix.
      Warning: Only takes into account object parenting, so e.g. in case of bone parenting you get a matrix relative to the Armature object, not to the actual parent bone
      
      (multi-dimensional array of 4 * 4 items, in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)))

      :type: :class:`mathutils.Matrix`

   .. attribute:: matrix_parent_inverse

      Inverse of object's parent matrix at time of parenting (multi-dimensional array of 4 * 4 items, in [-inf, inf], default ((1.0, 0.0, 0.0, 0.0), (0.0, 1.0, 0.0, 0.0), (0.0, 0.0, 1.0, 0.0), (0.0, 0.0, 0.0, 1.0)))

      :type: :class:`mathutils.Matrix`

   .. attribute:: matrix_world

      Worldspace transformation matrix (multi-dimensional array of 4 * 4 items, in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)))

      :type: :class:`mathutils.Matrix`

   .. data:: mode

      Object interaction mode (default ``'OBJECT'``, readonly)

      :type: Literal[:ref:`rna_enum_object_mode_items`]

   .. data:: modifiers

      Modifiers affecting the geometric data of the object (default None, readonly)

      :type: :class:`ObjectModifiers`\ [:class:`Modifier`]

   .. data:: motion_path

      Motion Path for this element (readonly)

      :type: :class:`MotionPath` | None

   .. attribute:: parent

      Parent object

      :type: :class:`Object` | None

   .. attribute:: parent_bone

      Name of parent bone in case of a bone parenting relation (default "", never None)

      :type: str

   .. attribute:: parent_type

      Type of parent relation (default ``'OBJECT'``)

      - ``OBJECT``
        Object -- The object is parented to an object.
      - ``ARMATURE``
        Armature.
      - ``LATTICE``
        Lattice -- The object is parented to a lattice.
      - ``VERTEX``
        Vertex -- The object is parented to a vertex.
      - ``VERTEX_3``
        3 Vertices.
      - ``BONE``
        Bone -- The object is parented to a bone.

      :type: Literal['OBJECT', 'ARMATURE', 'LATTICE', 'VERTEX', 'VERTEX_3', 'BONE']

   .. attribute:: parent_vertices

      Indices of vertices in case of a vertex parenting relation (array of 3 items, in [0, inf], default (0, 0, 0))

      :type: :class:`bpy_prop_array`\ [int]

   .. data:: particle_systems

      Particle systems emitted from the object (default None, readonly)

      :type: :class:`ParticleSystems`\ [:class:`ParticleSystem`]

   .. attribute:: pass_index

      Index number for the "Object Index" render pass (in [0, 32767], default 0)

      :type: int

   .. data:: pose

      Current pose for armatures (readonly)

      :type: :class:`Pose` | None

   .. data:: rigid_body

      Settings for rigid body simulation (readonly)

      :type: :class:`RigidBodyObject` | None

   .. data:: rigid_body_constraint

      Constraint constraining rigid bodies (readonly)

      :type: :class:`RigidBodyConstraint` | None

   .. attribute:: rotation_axis_angle

      Angle of Rotation for Axis-Angle rotation representation (array of 4 items, in [-inf, inf], default (0.0, 0.0, 1.0, 0.0))

      :type: :class:`bpy_prop_array`\ [float]

   .. attribute:: rotation_euler

      Rotation in Eulers (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Euler`

   .. attribute:: rotation_mode

      The kind of rotation to apply, values from other rotation modes are not used (default ``'XYZ'``)

      :type: Literal[:ref:`rna_enum_object_rotation_mode_items`]

   .. attribute:: rotation_quaternion

      Rotation in Quaternions (array of 4 items, in [-inf, inf], default (1.0, 0.0, 0.0, 0.0))

      :type: :class:`mathutils.Quaternion`

   .. attribute:: scale

      Scaling of the object (array of 3 items, in [-inf, inf], default (1.0, 1.0, 1.0))

      :type: :class:`mathutils.Vector`

   .. data:: selection_sets

      List of groups of bones for easy selection (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`SelectionSet`]

   .. data:: shader_effects

      Effects affecting display of object (default None, readonly)

      :type: :class:`ObjectShaderFx`\ [:class:`ShaderFx`]

   .. attribute:: shadow_terminator_geometry_offset

      Offset rays from the surface to reduce shadow terminator artifact on low poly geometry. Only affects triangles at grazing angles to light (in [0, inf], default 0.1)

      :type: float

   .. attribute:: shadow_terminator_normal_offset

      Offset rays from the surface to reduce shadow terminator artifact on low poly geometry. Only affect triangles that are affected by the geometry offset (in [0, inf], default 0.0)

      :type: float

   .. attribute:: shadow_terminator_shading_offset

      Push the shadow terminator towards the light to hide artifacts on low poly geometry (in [0, inf], default 0.0)

      :type: float

   .. attribute:: show_all_edges

      Display all edges for mesh objects (default False)

      :type: bool

   .. attribute:: show_axis

      Display the object's origin and axes (default False)

      :type: bool

   .. attribute:: show_bounds

      Display the object's bounds (default False)

      :type: bool

   .. attribute:: show_empty_image_only_axis_aligned

      Only display the image when it is aligned with the view axis (default False)

      :type: bool

   .. attribute:: show_empty_image_orthographic

      Display image in orthographic mode (default True)

      :type: bool

   .. attribute:: show_empty_image_perspective

      Display image in perspective mode (default True)

      :type: bool

   .. attribute:: show_in_front

      Make the object display in front of others (default False)

      :type: bool

   .. attribute:: show_instancer_for_render

      Make instancer visible when rendering (default True)

      :type: bool

   .. attribute:: show_instancer_for_viewport

      Make instancer visible in the viewport (default True)

      :type: bool

   .. attribute:: show_name

      Display the object's name (default False)

      :type: bool

   .. attribute:: show_only_shape_key

      Only show the active shape key at full value (default False)

      :type: bool

   .. attribute:: show_texture_space

      Display the object's texture space (default False)

      :type: bool

   .. attribute:: show_transparent

      Display material transparency in the object (default False)

      :type: bool

   .. attribute:: show_wire

      Display the object's wireframe over solid shading (default False)

      :type: bool

   .. data:: soft_body

      Settings for soft body simulation (readonly)

      :type: :class:`SoftBodySettings` | None

   .. attribute:: track_axis

      Axis that points in the 'forward' direction (applies to Instance Vertices when Align to Vertex Normal is enabled) (default ``'POS_X'``)

      :type: Literal[:ref:`rna_enum_object_axis_items`]

   .. data:: type

      Type of object (default ``'EMPTY'``, readonly)

      :type: Literal[:ref:`rna_enum_object_type_items`]

   .. attribute:: up_axis

      Axis that points in the upward direction (applies to Instance Vertices when Align to Vertex Normal is enabled) (default ``'X'``)

      :type: Literal['X', 'Y', 'Z']

   .. attribute:: use_camera_lock_parent

      View Lock 3D viewport camera transformation affects the object's parent instead (default False)

      :type: bool

   .. data:: use_dynamic_topology_sculpting

      (default False, readonly)

      :type: bool

   .. attribute:: use_empty_image_alpha

      Use alpha blending instead of alpha test (can produce sorting artifacts) (default False)

      :type: bool

   .. attribute:: use_grease_pencil_lights

      Lights affect Grease Pencil object (default True)

      :type: bool

   .. attribute:: use_instance_faces_scale

      Scale instance based on face size (default False)

      :type: bool

   .. attribute:: use_instance_vertices_rotation

      Rotate instance according to vertex normal (default False)

      :type: bool

   .. attribute:: use_mesh_mirror_x

      Enable mesh symmetry in the X axis (default False)

      :type: bool

   .. attribute:: use_mesh_mirror_y

      Enable mesh symmetry in the Y axis (default False)

      :type: bool

   .. attribute:: use_mesh_mirror_z

      Enable mesh symmetry in the Z axis (default False)

      :type: bool

   .. attribute:: use_parent_final_indices

      Use the final evaluated indices rather than the original mesh indices (default False)

      :type: bool

   .. attribute:: use_shape_key_edit_mode

      Display shape keys in edit mode (for meshes only) (default False)

      :type: bool

   .. attribute:: use_simulation_cache

      Cache frames during simulation nodes playback (default True)

      :type: bool

   .. data:: vertex_groups

      Vertex groups of the object (default None, readonly)

      :type: :class:`VertexGroups`\ [:class:`VertexGroup`]

   .. attribute:: visible_camera

      Object visibility to camera rays (default True)

      :type: bool

   .. attribute:: visible_diffuse

      Object visibility to diffuse rays (default True)

      :type: bool

   .. attribute:: visible_glossy

      Object visibility to glossy rays (default True)

      :type: bool

   .. attribute:: visible_shadow

      Object visibility to shadow rays (default True)

      :type: bool

   .. attribute:: visible_transmission

      Object visibility to transmission rays (default True)

      :type: bool

   .. attribute:: visible_volume_scatter

      Object visibility to volume scattering rays (default True)

      :type: bool

   .. data:: children

      All the children of this object.
      
      :type: tuple[:class:`Object`, ...]
      
      .. note:: Takes ``O(len(bpy.data.objects))`` time.

      (readonly)

   .. data:: children_recursive

      A list of all children from this object.
      
      :type: list[:class:`Object`]
      
      .. note:: Takes ``O(len(bpy.data.objects))`` time.

      (readonly)

   .. data:: users_collection

      The collections this object is in.
      
      :type: tuple[:class:`Collection`, ...]
      
      .. note:: Takes ``O(len(bpy.data.collections) + len(bpy.data.scenes))`` time.

      (readonly)

   .. data:: users_scene

      The scenes this object is in.
      
      :type: tuple[:class:`Scene`, ...]
      
      .. note:: Takes ``O(len(bpy.data.scenes) * len(bpy.data.objects))`` time.

      (readonly)

   .. method:: select_get(*, view_layer=None)

      Test if the object is selected. The selection state is per view layer.

      :param view_layer: Use this instead of the active view layer (optional)
      :type view_layer: :class:`ViewLayer` | None
      :return: Object selected
      :rtype: bool

   .. method:: select_set(state, *, view_layer=None)

      Select or deselect the object. The selection state is per view layer.

      :param state: Selection state to define
      :type state: bool
      :param view_layer: Use this instead of the active view layer (optional)
      :type view_layer: :class:`ViewLayer` | None

   .. method:: hide_get(*, view_layer=None)

      Test if the object is hidden for viewport editing. This hiding state is per view layer.

      :param view_layer: Use this instead of the active view layer (optional)
      :type view_layer: :class:`ViewLayer` | None
      :return: Object hidden
      :rtype: bool

   .. method:: hide_set(state, *, view_layer=None)

      Hide the object for viewport editing. This hiding state is per view layer.

      :param state: Hide state to define
      :type state: bool
      :param view_layer: Use this instead of the active view layer (optional)
      :type view_layer: :class:`ViewLayer` | None

   .. method:: visible_get(*, view_layer=None, viewport=None)

      Test if the object is visible in the 3D viewport, taking into account all visibility settings

      :param view_layer: Use this instead of the active view layer (optional)
      :type view_layer: :class:`ViewLayer` | None
      :param viewport: Use this instead of the active 3D viewport (optional)
      :type viewport: :class:`SpaceView3D` | None
      :return: Object visible
      :rtype: bool

   .. method:: holdout_get(*, view_layer=None)

      Test if object is masked in the view layer

      :param view_layer: Use this instead of the active view layer (optional)
      :type view_layer: :class:`ViewLayer` | None
      :return: Object holdout
      :rtype: bool

   .. method:: indirect_only_get(*, view_layer=None)

      Test if object is set to contribute only indirectly (through shadows and reflections) in the view layer

      :param view_layer: Use this instead of the active view layer (optional)
      :type view_layer: :class:`ViewLayer` | None
      :return: Object indirect only
      :rtype: bool

   .. method:: local_view_get(viewport)

      Get the local view state for this object

      :param viewport: Viewport in local view (never None)
      :type viewport: :class:`SpaceView3D` | None
      :return: Object local view state
      :rtype: bool

   .. method:: local_view_set(viewport, state)

      Set the local view state for this object

      :param viewport: Viewport in local view (never None)
      :type viewport: :class:`SpaceView3D` | None
      :param state: Local view state to define
      :type state: bool

   .. method:: visible_in_viewport_get(viewport)

      Check for local view and local collections for this viewport and object

      :param viewport: Viewport in local collections (never None)
      :type viewport: :class:`SpaceView3D` | None
      :return: Object viewport visibility
      :rtype: bool

   .. method:: convert_space(*, pose_bone=None, matrix=((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)), from_space='WORLD', to_space='WORLD')

      Convert (transform) the given matrix from one space to another

      :param pose_bone: Bone to use to define spaces (may be None, in which case only the two 'WORLD' and 'LOCAL' spaces are usable) (optional)
      :type pose_bone: :class:`PoseBone` | None
      :param matrix: The matrix to transform (multi-dimensional array of 4 * 4 items, in [-inf, inf], optional)
      :type matrix: :class:`mathutils.Matrix` | Sequence[Sequence[float]]
      :param from_space: The space in which 'matrix' is currently (optional)

         - ``WORLD``
           World Space -- The most global space in Blender.
         - ``POSE``
           Pose Space -- The pose space of a bone (its armature's object space).
         - ``LOCAL_WITH_PARENT``
           Local With Parent -- The rest pose local space of a bone (this matrix includes parent transforms).
         - ``LOCAL``
           Local Space -- The local space of an object/bone.
      :type from_space: Literal['WORLD', 'POSE', 'LOCAL_WITH_PARENT', 'LOCAL']
      :param to_space: The space to which you want to transform 'matrix' (optional)

         - ``WORLD``
           World Space -- The most global space in Blender.
         - ``POSE``
           Pose Space -- The pose space of a bone (its armature's object space).
         - ``LOCAL_WITH_PARENT``
           Local With Parent -- The rest pose local space of a bone (this matrix includes parent transforms).
         - ``LOCAL``
           Local Space -- The local space of an object/bone.
      :type to_space: Literal['WORLD', 'POSE', 'LOCAL_WITH_PARENT', 'LOCAL']
      :return: The transformed matrix (multi-dimensional array of 4 * 4 items, in [-inf, inf])
      :rtype: :class:`mathutils.Matrix`

   .. method:: calc_matrix_camera(depsgraph, *, x=1, y=1, scale_x=1.0, scale_y=1.0)

      Generate the camera projection matrix of this object (mostly useful for Camera and Light types)

      :param depsgraph: Depsgraph to get evaluated data from
      :type depsgraph: :class:`Depsgraph` | None
      :param x: Width of the render area (in [0, inf], optional)
      :type x: int
      :param y: Height of the render area (in [0, inf], optional)
      :type y: int
      :param scale_x: Width scaling factor (in [1e-06, inf], optional)
      :type scale_x: float
      :param scale_y: Height scaling factor (in [1e-06, inf], optional)
      :type scale_y: float
      :return: The camera projection matrix (multi-dimensional array of 4 * 4 items, in [-inf, inf])
      :rtype: :class:`mathutils.Matrix`

   .. method:: camera_fit_coords(depsgraph, coordinates)

      Compute the coordinate (and scale for ortho cameras) given object should be to 'see' all given coordinates

      :param depsgraph: Depsgraph to get evaluated data from
      :type depsgraph: :class:`Depsgraph` | None
      :param coordinates: Coordinates to fit in (array of 1 items, in [-inf, inf], never None)
      :type coordinates: Sequence[float]
      :return:
         ``co_return``, The location to aim to be able to see all given points, :class:`mathutils.Vector`

         ``scale_return``, The ortho scale to aim to be able to see all given points (if relevant), float

      :rtype: tuple[:class:`mathutils.Vector`, float]

   .. method:: crazyspace_eval(depsgraph, scene)

      Compute orientation mapping between vertices of an original object and object with shape keys and deforming modifiers applied.The evaluation is to be freed with the crazyspace_eval_free function

      :param depsgraph: Dependency Graph, Evaluated dependency graph
      :type depsgraph: :class:`Depsgraph` | None
      :param scene: Scene, Scene of the object
      :type scene: :class:`Scene` | None

   .. method:: crazyspace_displacement_to_deformed(*, vertex_index=0, displacement=(0.0, 0.0, 0.0))

      Convert displacement vector from non-deformed object space to deformed object space

      :param vertex_index: vertex_index, (in [-inf, inf], optional)
      :type vertex_index: int
      :param displacement: displacement, (array of 3 items, in [-inf, inf], optional)
      :type displacement: :class:`mathutils.Vector` | Sequence[float]
      :return: displacement_deformed, (array of 3 items, in [-inf, inf])
      :rtype: :class:`mathutils.Vector`

   .. method:: crazyspace_displacement_to_original(*, vertex_index=0, displacement=(0.0, 0.0, 0.0))

      Free evaluated state of crazyspace

      :param vertex_index: vertex_index, (in [-inf, inf], optional)
      :type vertex_index: int
      :param displacement: displacement, (array of 3 items, in [-inf, inf], optional)
      :type displacement: :class:`mathutils.Vector` | Sequence[float]
      :return: displacement_original, (array of 3 items, in [-inf, inf])
      :rtype: :class:`mathutils.Vector`

   .. method:: crazyspace_eval_clear()

      crazyspace_eval_clear


   .. method:: to_mesh(*, preserve_all_data_layers=False, depsgraph=None)

      Create a Mesh data-block from the current state of the object. The object owns the data-block. To force free it use to_mesh_clear(). The result is temporary and cannot be used by objects from the main database.

      :param preserve_all_data_layers: Preserve all data layers in the mesh, like UV maps and vertex groups. By default Blender only computes the subset of data layers needed for viewport display and rendering, for better performance. (optional)
      :type preserve_all_data_layers: bool
      :param depsgraph: Dependency Graph, Evaluated dependency graph which is required when preserve_all_data_layers is true (optional)
      :type depsgraph: :class:`Depsgraph` | None
      :return: Mesh created from object
      :rtype: :class:`Mesh`

   .. method:: to_mesh_clear()

      Clears mesh data-block created by to_mesh()


   .. method:: to_curve(depsgraph, *, apply_modifiers=False)

      Create a Curve data-block from the current state of the object. This only works for curve and text objects. The object owns the data-block. To force free it, use to_curve_clear(). The result is temporary and cannot be used by objects from the main database.

      :param depsgraph: Dependency Graph, Evaluated dependency graph
      :type depsgraph: :class:`Depsgraph` | None
      :param apply_modifiers: Apply the deform modifiers on the control points of the curve. This is only supported for curve objects. (optional)
      :type apply_modifiers: bool
      :return: Curve created from object
      :rtype: :class:`Curve`

   .. method:: to_curve_clear()

      Clears curve data-block created by to_curve()


   .. method:: find_armature()

      Find armature influencing this object as a parent or via a modifier

      :return: Armature object influencing this object or nullptr
      :rtype: :class:`Object`

   .. method:: shape_key_add(*, name="Key", from_mix=True)

      Add shape key to this object

      :param name: Unique name for the new key-block (optional, never None)
      :type name: str
      :param from_mix: Create new shape from existing mix of shapes (optional)
      :type from_mix: bool
      :return: New shape key-block
      :rtype: :class:`ShapeKey`

   .. method:: shape_key_remove(key)

      Remove a Shape Key from this object

      :param key: Key-block to be removed (never None)
      :type key: :class:`ShapeKey` | None

   .. method:: shape_key_clear()

      Remove all Shape Keys from this object


   .. method:: shape_keys_selected()

      Return selected shape keys

      :return: keyblocks
      :rtype: :class:`bpy_prop_collection`\ [:class:`ShapeKey`]

   .. method:: ray_cast(origin, direction, *, distance=1.70141e+38, depsgraph=None)

      Cast a ray onto evaluated geometry, in object space (using context's or provided depsgraph to get evaluated mesh if needed)

      :param origin: Origin of the ray, in object space (array of 3 items, in [-inf, inf])
      :type origin: :class:`mathutils.Vector` | Sequence[float]
      :param direction: Direction of the ray, in object space (array of 3 items, in [-inf, inf])
      :type direction: :class:`mathutils.Vector` | Sequence[float]
      :param distance: Maximum distance (in [0, inf], optional)
      :type distance: float
      :param depsgraph: Depsgraph to use to get evaluated data, when called from original object (only needed if current Context's depsgraph is not suitable) (optional)
      :type depsgraph: :class:`Depsgraph` | None
      :return:
         ``result``, Whether the ray successfully hit the geometry, bool

         ``location``, The hit location of this ray cast, :class:`mathutils.Vector`

         ``normal``, The face normal at the ray cast hit location, :class:`mathutils.Vector`

         ``index``, The face index, -1 when original data isn't available, int

      :rtype: tuple[bool, :class:`mathutils.Vector`, :class:`mathutils.Vector`, int]

   .. method:: closest_point_on_mesh(origin, *, distance=1.84467e+19, depsgraph=None)

      Find the nearest point on evaluated geometry, in object space (using context's or provided depsgraph to get evaluated mesh if needed)

      :param origin: Point to find closest geometry from (in object space) (array of 3 items, in [-inf, inf])
      :type origin: :class:`mathutils.Vector` | Sequence[float]
      :param distance: Maximum distance (in [0, inf], optional)
      :type distance: float
      :param depsgraph: Depsgraph to use to get evaluated data, when called from original object (only needed if current Context's depsgraph is not suitable) (optional)
      :type depsgraph: :class:`Depsgraph` | None
      :return:
         ``result``, Whether closest point on geometry was found, bool

         ``location``, The location on the object closest to the point, :class:`mathutils.Vector`

         ``normal``, The face normal at the closest point, :class:`mathutils.Vector`

         ``index``, The face index, -1 when original data isn't available, int

      :rtype: tuple[bool, :class:`mathutils.Vector`, :class:`mathutils.Vector`, int]

   .. method:: is_modified(scene, settings)

      Determine if this object is modified from the base mesh data

      :param scene: Scene in which to check the object (never None)
      :type scene: :class:`Scene` | None
      :param settings: Modifier settings to apply

         - ``PREVIEW``
           Preview -- Apply modifier preview settings.
         - ``RENDER``
           Render -- Apply modifier render settings.
      :type settings: Literal['PREVIEW', 'RENDER']
      :return: Whether the object is modified
      :rtype: bool

   .. method:: is_deform_modified(scene, settings)

      Determine if this object is modified by a deformation from the base mesh data

      :param scene: Scene in which to check the object (never None)
      :type scene: :class:`Scene` | None
      :param settings: Modifier settings to apply

         - ``PREVIEW``
           Preview -- Apply modifier preview settings.
         - ``RENDER``
           Render -- Apply modifier render settings.
      :type settings: Literal['PREVIEW', 'RENDER']
      :return: Whether the object is deform-modified
      :rtype: bool

   .. method:: dm_info(type, *, depsgraph=None)

      Returns a string for original/evaluated mesh data (debug builds only, using context's or provided depsgraph to get evaluated mesh if needed)

      :param type: Modifier settings to apply

         - ``SOURCE``
           Source -- Source mesh.
         - ``DEFORM``
           Deform -- Objects deform mesh.
         - ``FINAL``
           Final -- Objects final mesh.
      :type type: Literal['SOURCE', 'DEFORM', 'FINAL']
      :param depsgraph: Depsgraph to use to get evaluated data, when called from original object (only needed if current Context's depsgraph is not suitable) (optional)
      :type depsgraph: :class:`Depsgraph` | None
      :return: Requested information (never None)
      :rtype: str

   .. method:: update_from_editmode()

      Load the objects edit-mode data into the object data

      :return: Success
      :rtype: bool

   .. method:: cache_release()

      Release memory used by caches associated with this object. Intended to be used by render engines only.


   .. method:: evaluated_geometry()

      Get the evaluated geometry set of this evaluated object. This only works for
      objects that contain geometry data like meshes and curves but not e.g. cameras.
      
      :return: The evaluated geometry.
      :rtype: :class:`bpy.types.GeometrySet`

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

   - :mod:`bpy.context.active_object`
   - :mod:`bpy.context.edit_object`
   - :mod:`bpy.context.editable_objects`
   - :mod:`bpy.context.image_paint_object`
   - :mod:`bpy.context.object`
   - :mod:`bpy.context.objects_in_mode`
   - :mod:`bpy.context.objects_in_mode_unique_data`
   - :mod:`bpy.context.particle_edit_object`
   - :mod:`bpy.context.pose_object`
   - :mod:`bpy.context.sculpt_object`
   - :mod:`bpy.context.selectable_objects`
   - :mod:`bpy.context.selected_editable_objects`
   - :mod:`bpy.context.selected_objects`
   - :mod:`bpy.context.vertex_paint_object`
   - :mod:`bpy.context.visible_objects`
   - :mod:`bpy.context.weight_paint_object`
   - :class:`Action.flip_with_pose`
   - :class:`ActionConstraint.target`
   - :class:`ArmatureModifier.object`
   - :class:`ArrayModifier.curve`
   - :class:`ArrayModifier.end_cap`
   - :class:`ArrayModifier.offset_object`
   - :class:`ArrayModifier.start_cap`
   - :class:`BlendData.objects`
   - :class:`BlendDataMeshes.new_from_object`
   - :class:`BlendDataObjects.new`
   - :class:`BlendDataObjects.remove`
   - :class:`BoidRuleAvoid.object`
   - :class:`BoidRuleFollowLeader.object`
   - :class:`BoidRuleGoal.object`
   - :class:`BooleanModifier.object`
   - :class:`CameraDOFSettings.focus_object`
   - :class:`CastModifier.object`
   - :class:`ChildOfConstraint.target`
   - :class:`ClampToConstraint.target`
   - :class:`Collection.all_objects`
   - :class:`Collection.objects`
   - :class:`CollectionObjects.link`
   - :class:`CollectionObjects.unlink`
   - :class:`Constraint.space_object`
   - :class:`ConstraintTarget.target`
   - :class:`ConstraintTargetBone.target`
   - :class:`CopyLocationConstraint.target`
   - :class:`CopyRotationConstraint.target`
   - :class:`CopyScaleConstraint.target`
   - :class:`CopyTransformsConstraint.target`
   - :class:`Curve.bevel_object`
   - :class:`Curve.taper_object`
   - :class:`CurveModifier.object`
   - :class:`Curves.surface`
   - :class:`DampedTrackConstraint.target`
   - :class:`DataTransferModifier.object`
   - :class:`Depsgraph.objects`
   - :class:`DepsgraphObjectInstance.instance_object`
   - :class:`DepsgraphObjectInstance.object`
   - :class:`DepsgraphObjectInstance.parent`
   - :class:`DisplaceModifier.texture_coords_object`
   - :class:`DynamicPaintSurface.output_exists`
   - :class:`FieldSettings.source_object`
   - :class:`FloorConstraint.target`
   - :class:`FluidDomainSettings.guide_parent`
   - :class:`FollowPathConstraint.target`
   - :class:`FollowTrackConstraint.camera`
   - :class:`FollowTrackConstraint.depth_object`
   - :class:`GPencilSculptGuide.reference_object`
   - :class:`GeometryAttributeConstraint.target`
   - :class:`GeometryNodeInputObject.object`
   - :class:`GreasePencilArmatureModifier.object`
   - :class:`GreasePencilArrayModifier.offset_object`
   - :class:`GreasePencilBuildModifier.object`
   - :class:`GreasePencilHookModifier.object`
   - :class:`GreasePencilLatticeModifier.object`
   - :class:`GreasePencilLayer.parent`
   - :class:`GreasePencilLineartModifier.light_contour_object`
   - :class:`GreasePencilLineartModifier.source_camera`
   - :class:`GreasePencilLineartModifier.source_object`
   - :class:`GreasePencilMirrorModifier.object`
   - :class:`GreasePencilOutlineModifier.object`
   - :class:`GreasePencilShrinkwrapModifier.auxiliary_target`
   - :class:`GreasePencilShrinkwrapModifier.target`
   - :class:`GreasePencilTintModifier.object`
   - :class:`GreasePencilWeightProximityModifier.object`
   - :class:`HookModifier.object`
   - :class:`KinematicConstraint.pole_target`
   - :class:`KinematicConstraint.target`
   - :class:`LatticeModifier.object`
   - :class:`LayerObjects.active`
   - :class:`LayerObjects.selected`
   - :class:`LimitDistanceConstraint.target`
   - :class:`LineStyleAlphaModifier_DistanceFromObject.target`
   - :class:`LineStyleColorModifier_DistanceFromObject.target`
   - :class:`LineStyleThicknessModifier_DistanceFromObject.target`
   - :class:`LockedTrackConstraint.target`
   - :class:`MaskModifier.armature`
   - :class:`MeshDeformModifier.object`
   - :class:`MeshToVolumeModifier.object`
   - :class:`MirrorModifier.mirror_object`
   - :class:`NodeSocketObject.default_value`
   - :class:`NodeTreeInterfaceSocketObject.default_value`
   - :class:`NormalEditModifier.target`
   - :class:`Object.find_armature`
   - :class:`Object.parent`
   - :class:`ObjectBase.object`
   - :class:`ObjectSolverConstraint.camera`
   - :class:`ParticleEdit.object`
   - :class:`ParticleEdit.shape_object`
   - :class:`ParticleHairKey.co_object`
   - :class:`ParticleHairKey.co_object_set`
   - :class:`ParticleInstanceModifier.object`
   - :class:`ParticleSettings.instance_object`
   - :class:`ParticleSettingsTextureSlot.object`
   - :class:`ParticleSystem.co_hair`
   - :class:`ParticleSystem.parent`
   - :class:`ParticleSystem.reactor_target_object`
   - :class:`ParticleTarget.object`
   - :class:`PivotConstraint.target`
   - :class:`PoseBone.custom_shape`
   - :class:`RenderEngine.bake`
   - :class:`RenderEngine.camera_model_matrix`
   - :class:`RenderEngine.camera_override`
   - :class:`RenderEngine.camera_shift_x`
   - :class:`RenderEngine.use_spherical_stereo`
   - :class:`RigidBodyConstraint.object1`
   - :class:`RigidBodyConstraint.object2`
   - :class:`RigidBodyWorld.convex_sweep_test`
   - :class:`BakeSettings.cage_object`
   - :class:`Scene.camera`
   - :class:`Scene.objects`
   - :class:`Scene.ray_cast`
   - :class:`Scene.uvedit_aspect`
   - :class:`SceneStrip.scene_camera`
   - :class:`ScrewModifier.object`
   - :class:`Sculpt.gravity_object`
   - :class:`ShaderFxShadow.object`
   - :class:`ShaderFxSwirl.object`
   - :class:`ShaderNodeTexCoord.object`
   - :class:`ShrinkwrapConstraint.target`
   - :class:`ShrinkwrapModifier.auxiliary_target`
   - :class:`ShrinkwrapModifier.target`
   - :class:`SimpleDeformModifier.origin`
   - :class:`SpaceView3D.camera`
   - :class:`SpaceView3D.lock_object`
   - :class:`SplineIKConstraint.target`
   - :class:`StretchToConstraint.target`
   - :class:`SurfaceDeformModifier.target`
   - :class:`TextCurve.follow_curve`
   - :class:`TimelineMarker.camera`
   - :class:`ToolSettings.anim_mirror_object`
   - :class:`ToolSettings.anim_relative_object`
   - :class:`TrackToConstraint.target`
   - :class:`TransformConstraint.target`
   - :class:`UVProjector.object`
   - :class:`UVWarpModifier.object_from`
   - :class:`UVWarpModifier.object_to`
   - :class:`VertexWeightEditModifier.mask_tex_map_object`
   - :class:`VertexWeightMixModifier.mask_tex_map_object`
   - :class:`VertexWeightProximityModifier.mask_tex_map_object`
   - :class:`VertexWeightProximityModifier.target`
   - :class:`ViewLayer.objects`
   - :class:`VolumeDisplaceModifier.texture_map_object`
   - :class:`VolumeToMeshModifier.object`
   - :class:`WarpModifier.object_from`
   - :class:`WarpModifier.object_to`
   - :class:`WarpModifier.texture_coords_object`
   - :class:`WaveModifier.start_position_object`
   - :class:`WaveModifier.texture_coords_object`
   - :class:`XrSessionSettings.base_pose_object`

