
****
Pose
****

.. reference::

   :Mode:      Sculpt Mode
   :Brush:     :menuselection:`Sidebar --> Tool --> Brush Settings --> Advanced --> Brush Type`

Deform a model simulating armature-like workflow.
This can either be useful for posing a model without a rig,
adjusting the proportions of a mesh or other fast deformations.

The brush will automatically determine an origin point,
indicated with a while line on the brush cursor.

If the :ref:`Deformation Target <bpy.types.Brush.deform_target>`
is changed, the brush can also be used for cloth sculpting.


Brush Settings
==============

General
-------

Only Size and Auto-Masking has an impact on the brush behavior for this brush.

.. note::

   More info at :ref:`sculpt-tool-settings-brush-settings-general` brush settings
   and on :ref:`sculpt-tool-settings-brush-settings-advanced` brush settings.


Unique
------

.. _bpy.types.Brush.pose_deform_type:

Deformation
   Deformation type that is used by the brush.

   :Rotate/Twist:
      Rotates the mesh around the pose origin.
      When pressing :kbd:`Ctrl`, the brush applies a twist rotation
      instead (and disables any IK segments that are used).
   :Scale/Translate:
      Scale the mesh based on the pose origin.
      While holding :kbd:`Ctrl` the brush moves the mesh.
   :Squash/Stretch:
      Works similar to *Scale/Translate* however, it applies different
      scale values along different axes to achieve the stretching effect.

.. _bpy.types.Brush.pose_origin_type:

Rotation Origins
   Method to set the rotation origin for the pose origin or individual IK segments.

   :Topology:
      Sets the rotation origin automatically using the topology and shape of the mesh.
   :Face Sets:
      Creates a pose segment per :ref:`Face Set <sculpting-editing-facesets>`, starting from the active face set.
      This can lead to the most accurate and desirable results.
   :Face Sets FK:
      Simulates a :term:`Forward Kinematics` deformation using the :ref:`Face Set <sculpting-editing-facesets>`
      under the cursor as control.

.. _bpy.types.Brush.pose_offset:

Pose Origin Offset
   Offset of the pose origin in relation to the brush radius.
   This is useful to manipulate areas with a lot of complex shapes like fingers.

.. _bpy.types.Brush.pose_smooth_iterations:

Smooth Iterations
   Controls the smoothness of the falloff of the deformation.

.. _bpy.types.Brush.pose_ik_segments:

Pose IK Segments
   Controls how many :ref:`IK segments <bone-constraints-inverse-kinematics>`
   are going to be created for posing.
   This can be seen by a divided white line on the cursor.
   This is also useful for making curved deformations with the pose brush,
   like hair clumps and tails.

.. _bpy.types.Brush.use_pose_lock_rotation:

Lock Rotation when Scaling
   When using *Scale/Translate Deformation*, do not rotate the segment; only scaling is applied.

.. _bpy.types.Brush.use_pose_ik_anchored:

Keep Anchor Point
   Keeps the position of the last segment in the IK chain fixed.
   If this is disabled, the mesh can be dragged around more freely,
   creating snake like shapes.

.. _bpy.types.Brush.use_connected_only:

Connected Only
   The brush will only affect topologically connected elements.
   Disabling this will allow deforming multiple disconnected meshes at the same time,
   for example characters with clothing & shoes.

   Disabling this setting can have a big impact on performance,
   as neighboring elements will be merged internally.
   Keeping the *Max Element Distance* as low as possible
   will help counteract the performance impact.

.. _bpy.types.Brush.disconnected_distance_max:

Max Element Distance
   Maximum distance to search for disconnected loose parts in the mesh.
