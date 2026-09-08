
*************
Tool Settings
*************

Options
=======

.. reference::

   :Mode:      Edit Mode
   :Panel:     :menuselection:`Sidebar --> Tool tab --> Options panel`


Transform
---------

.. _bpy.types.ToolSettings.use_transform_correct_face_attributes:

Correct Face Attributes
   Adjust geometry attributes like :doc:`UVs </modeling/meshes/uv/index>`
   and :doc:`Color Attributes </sculpt_paint/vertex_paint/index>` while transforming.

.. _bpy.types.ToolSettings.use_transform_correct_keep_connected:

Keep Connected
   Merge attributes connected to the same vertex while using *Correct Face Attributes*.

   .. tip::

      Keeping UVs connected is useful for organic modeling, but not for architectural modeling.


.. _bpy.types.Mesh.use_mirror_x:
.. _bpy.types.Mesh.use_mirror_y:
.. _bpy.types.Mesh.use_mirror_z:
.. _modeling_meshes_tools-settings_mirror:

Mirror
^^^^^^

The *Mirror* options enable symmetric transformations
of mesh elements (vertices, edges, or faces) along the selected axis.
When an element is transformed, its exact mirrored counterpart (in local space),
if present, is transformed correspondingly to maintain symmetry.

For the *Mirror* tool to function correctly, mirrored vertices must be precisely aligned with their counterparts.
If vertices are not accurately positioned at their mirror locations,
the *Mirror Axis* will not recognize them as mirrored.
For meshes with visual symmetry but differing topology,
enabling :ref:`Topology Mirror <bpy.types.Mesh.use_mirror_topology>` can address this limitation.

.. note::

   Strict alignment requirements can make *Mirror* challenging to use.
   The :doc:`Mirror Modifier </modeling/modifiers/generate/mirror>` offers an alternative,
   automatically handling symmetry.


.. _bpy.types.Mesh.use_mirror_topology:

Topology Mirror
^^^^^^^^^^^^^^^

*Topology Mirror* determines mirrored vertices by analyzing their relationships with other vertices in the mesh,
rather than relying solely on vertex positions.
By evaluating the overall topology, this feature allows non-symmetrical vertices to be treated as mirrored.

*Topology Mirror* requires at least one *Mirror Axis* to be enabled.

.. tip::

   *Topology Mirror* is most effective with detailed geometry.
   Simple meshes, such as cubes or UV spheres, may produce inconsistent results.

.. rubric:: Example

This example demonstrates how to use *Topology Mirror* effectively:

#. Open a new Blender scene. Delete the default cube and add a Monkey object in the 3D Viewport.
#. Press :kbd:`Tab` to switch to *Edit Mode*.
#. Disable all *Mirror* axes and move one of the Monkey object's vertices slightly.
#. Enable the *X Axis Mirror* option but leave *Topology Mirror* disabled.
   Move the same vertex again. The *X Axis Mirror* will not affect the mirrored vertices, as they are not perfectly
   aligned.
#. Enable *Topology Mirror* and move the same vertex once more.
   The *X Axis Mirror* will now mirror the other vertex, even though they are not perfectly positioned.


.. _bpy.types.ToolSettings.use_mesh_automerge:

Auto Merge
^^^^^^^^^^

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Sidebar --> Tool --> Options --> Auto Merge`

When enabled, as soon as a vertex moves closer to another one
than the *Threshold* setting, they are automatically merged.
This option affects interactive operations only
(tweaks made in the :ref:`bpy.ops.screen.redo_last` panel are considered interactive too).
If the exact spot where a vertex is moved contains more than one vertex,
then the merge will be performed between the moved vertex and one of those.

.. _bpy.types.ToolSettings.use_mesh_automerge_and_split:

Split Edges & Faces
   Detects the intersection of each transformed edge, creating a new vertex in place
   and sectioning the edge and the face if any.

.. _bpy.types.ToolSettings.double_threshold:

Threshold
   Defines the maximum distance between vertices that are merged.


UVs
---

.. _bpy.types.ToolSettings.use_edge_path_live_unwrap:

Live Unwrap
   Automatically recalculates the UV unwrapping every time an edge has its seam property changed.
   Note, this is different than the :ref:`Live Unwrap <bpy.types.SpaceUVEditor.use_live_unwrap>`
   option in the UV Editor.
