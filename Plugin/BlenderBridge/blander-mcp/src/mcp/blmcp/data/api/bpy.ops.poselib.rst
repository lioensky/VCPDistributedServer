Poselib Operators
=================

.. module:: bpy.ops.poselib

.. function:: apply_pose_asset(*, asset_library_type='LOCAL', asset_library_identifier="", relative_asset_identifier="", blend_factor=1.0, flipped=False)

   Apply the given Pose Action to the rig

   :param asset_library_type: Asset Library Type, (optional)
   :type asset_library_type: Literal[:ref:`rna_enum_asset_library_type_items`]
   :param asset_library_identifier: Asset Library Identifier, (optional, never None)
   :type asset_library_identifier: str
   :param relative_asset_identifier: Relative Asset Identifier, (optional, never None)
   :type relative_asset_identifier: str
   :param blend_factor: Blend Factor, Amount that the pose is applied on top of the existing poses. A negative value will subtract the pose instead of adding it (in [-inf, inf], optional)
   :type blend_factor: float
   :param flipped: Apply Flipped, When enabled, applies the pose flipped over the X-axis (optional)
   :type flipped: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: asset_delete()

   Delete the selected Pose Asset

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: asset_modify(*, mode='ADJUST')

   Update the selected pose asset in the asset library from the currently selected bones. The mode defines how the asset is updated

   :param mode: Overwrite Mode, Specify which parts of the pose asset are overwritten (optional)

      - ``ADJUST``
        Adjust -- Update existing channels in the pose asset but don't remove or add any channels.
      - ``REPLACE``
        Replace with Selection -- Completely replace all channels in the pose asset with the current selection.
      - ``ADD``
        Add Selected Bones -- Add channels of the selection to the pose asset. Existing channels will be updated.
      - ``REMOVE``
        Remove Selected Bones -- Remove channels of the selection from the pose asset.
   :type mode: Literal['ADJUST', 'REPLACE', 'ADD', 'REMOVE']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: blend_pose_asset(*, asset_library_type='LOCAL', asset_library_identifier="", relative_asset_identifier="", blend_factor=0.0, flipped=False, release_confirm=False)

   Blend the given Pose Action to the rig

   :param asset_library_type: Asset Library Type, (optional)
   :type asset_library_type: Literal[:ref:`rna_enum_asset_library_type_items`]
   :param asset_library_identifier: Asset Library Identifier, (optional, never None)
   :type asset_library_identifier: str
   :param relative_asset_identifier: Relative Asset Identifier, (optional, never None)
   :type relative_asset_identifier: str
   :param blend_factor: Blend Factor, Amount that the pose is applied on top of the existing poses. A negative value will subtract the pose instead of adding it (in [-inf, inf], optional)
   :type blend_factor: float
   :param flipped: Apply Flipped, When enabled, applies the pose flipped over the X-axis (optional)
   :type flipped: bool
   :param release_confirm: Confirm on Release, Always confirm operation when releasing button (optional)
   :type release_confirm: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: copy_as_asset()

   Create a new pose asset on the clipboard, to be pasted into an Asset Browser

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `addons_core/pose_library/operators.py\:116 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/pose_library/operators.py#L116>`__

.. function:: create_pose_asset(*, pose_name="", asset_library_reference='', catalog_path="")

   Create a new asset from the selected bones in the scene

   :param pose_name: Pose Name, Name for the new pose asset (optional, never None)
   :type pose_name: str
   :param asset_library_reference: Library, Asset library used to store the new pose (optional)
   :type asset_library_reference: str
   :param catalog_path: Catalog, Catalog to use for the new asset (optional, never None)
   :type catalog_path: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: paste_asset()

   Paste the Asset that was previously copied using Copy As Asset

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `addons_core/pose_library/operators.py\:190 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/pose_library/operators.py#L190>`__

.. function:: pose_asset_select_bones(*, select=True, flipped=False)

   Select those bones that are used in this pose

   :param select: Select, (optional)
   :type select: bool
   :param flipped: Flipped, (optional)
   :type flipped: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `addons_core/pose_library/operators.py\:228 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/pose_library/operators.py#L228>`__


.. function:: restore_previous_action()

   Switch back to the previous Action, after creating a pose asset

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `addons_core/pose_library/operators.py\:65 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/pose_library/operators.py#L65>`__

