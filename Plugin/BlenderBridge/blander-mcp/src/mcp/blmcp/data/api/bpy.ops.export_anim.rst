Export Anim Operators
=====================

.. module:: bpy.ops.export_anim

.. function:: bvh(*, filepath="", check_existing=True, filter_glob="*.bvh", global_scale=1.0, frame_start=0, frame_end=0, rotate_mode='NATIVE', root_transform_only=False, sort_children_by_names=False)

   Save a BVH motion capture file from an armature

   :param filepath: File Path, Filepath used for exporting the file (optional, never None)
   :type filepath: str
   :param check_existing: Check Existing, Check and warn on overwriting existing files (optional)
   :type check_existing: bool
   :param filter_glob: filter_glob, (optional, never None)
   :type filter_glob: str
   :param global_scale: Scale, Scale the BVH by this value (in [0.0001, 1e+06], optional)
   :type global_scale: float
   :param frame_start: Start Frame, Starting frame to export (in [-inf, inf], optional)
   :type frame_start: int
   :param frame_end: End Frame, End frame to export (in [-inf, inf], optional)
   :type frame_end: int
   :param rotate_mode: Rotation, Rotation conversion (optional)

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
   :type rotate_mode: Literal['NATIVE', 'XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX']
   :param root_transform_only: Root Translation Only, Only write out translation channels for the root bone (optional)
   :type root_transform_only: bool
   :param sort_children_by_names: Sort Children By Name, Sort the children of each bone alphabetically (optional)
   :type sort_children_by_names: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `addons_core/io_anim_bvh/__init__.py\:286 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/io_anim_bvh/__init__.py#L286>`__


