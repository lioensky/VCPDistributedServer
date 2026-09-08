Import Anim Operators
=====================

.. module:: bpy.ops.import_anim

.. function:: bvh(*, filepath="", filter_glob="*.bvh", target='ARMATURE', global_scale=1.0, frame_start=1, use_fps_scale=False, update_scene_fps=False, update_scene_duration=False, use_cyclic=False, rotate_mode='NATIVE', axis_forward='-Z', axis_up='Y')

   Load a BVH motion capture file

   :param filepath: File Path, Filepath used for importing the file (optional, never None)
   :type filepath: str
   :param filter_glob: filter_glob, (optional, never None)
   :type filter_glob: str
   :param target: Target, Import target type (optional)
   :type target: Literal['ARMATURE', 'OBJECT']
   :param global_scale: Scale, Scale the BVH by this value (in [0.0001, 1e+06], optional)
   :type global_scale: float
   :param frame_start: Start Frame, Starting frame for the animation (in [-inf, inf], optional)
   :type frame_start: int
   :param use_fps_scale: Scale FPS, Scale the frame-rate from the BVH to the current scenes, otherwise each BVH frame maps directly to a Blender frame (optional)
   :type use_fps_scale: bool
   :param update_scene_fps: Update Scene FPS, Set the scene frame-rate to that of the BVH file (note that this nullifies the 'Scale FPS' option, as the scale will be 1:1) (optional)
   :type update_scene_fps: bool
   :param update_scene_duration: Update Scene Duration, Extend the scene's duration to the BVH duration (never shortens the scene) (optional)
   :type update_scene_duration: bool
   :param use_cyclic: Loop, Loop the animation playback (optional)
   :type use_cyclic: bool
   :param rotate_mode: Rotation, Rotation conversion (optional)

      - ``QUATERNION``
        Quaternion -- Convert rotations to quaternions.
      - ``NATIVE``
        Euler (Native) -- Use the rotation order defined in the BVH file.
      - ``XYZ``
        Euler (XYZ) -- Convert rotations to euler XYZ.
      - ``XZY``
        Euler (XZY) -- Convert rotations to euler XZY.
      - ``YXZ``
        Euler (YXZ) -- Convert rotations to euler YXZ.
      - ``YZX``
        Euler (YZX) -- Convert rotations to euler YZX.
      - ``ZXY``
        Euler (ZXY) -- Convert rotations to euler ZXY.
      - ``ZYX``
        Euler (ZYX) -- Convert rotations to euler ZYX.
   :type rotate_mode: Literal['QUATERNION', 'NATIVE', 'XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX']
   :param axis_forward: Forward, (optional)
   :type axis_forward: Literal['X', 'Y', 'Z', '-X', '-Y', '-Z']
   :param axis_up: Up, (optional)
   :type axis_up: Literal['X', 'Y', 'Z', '-X', '-Y', '-Z']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `addons_core/io_anim_bvh/__init__.py\:118 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/io_anim_bvh/__init__.py#L118>`__


