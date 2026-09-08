.. _bpy.types.View3DOverlay:

*****************
Viewport Overlays
*****************

.. reference::

   :Mode:      All Modes
   :Location:  :menuselection:`Header --> Overlays`

Clicking :bl-icon:`overlay` (Show Overlays) toggles all overlays in the 3D Viewport.

.. note::

   Cameras outline & :ref:`passepartout <bpy.types.Camera.show_passepartout>` are not considered Viewport overlays.

The drop-down button displays a popover with more detailed settings, which are described below.

Depending on the current :doc:`object interaction mode </editors/3dview/modes>`,
there may be a second button with yet more settings, which are also described here.


General
=======

The following options are always present, independent of the current mode.
Some of the overlays can be customized in the
:doc:`Viewport Preferences </editors/preferences/viewport>`.


Guides
------

.. _bpy.types.View3DOverlay.show_ortho_grid:

Grid
   Show grid in orthographic side view.

.. _bpy.types.View3DOverlay.show_floor:

Floor
   Show the ground plane in perspective view.

.. _bpy.types.View3DOverlay.show_axis:

Axes
   Show the X, Y and/or Z axis lines.

.. _bpy.types.View3DOverlay.grid_scale:

Scale
   The distance between lines in the grid/floor.

.. _bpy.types.View3DOverlay.grid_subdivisions:

Subdivisions
   The number of subdivisions between grid lines.

.. _bpy.types.View3DOverlay.show_text:

Text Info
   Show various bits of information in the top left corner of the viewport.

   - **View Perspective** --
     Name of the :doc:`View Perspective </editors/3dview/navigate/projections>`,
     such as "Top Orthographic" or "User Perspective."
   - **Playback Frame Rate (FPS)** --
     Displays the Frames Per Second at which the animation is playing.
     By default, Blender goes through every single frame, which may result in an FPS that's lower than
     intended (and the animation playing slower than realtime); the FPS turns red in this case.
     You can change this behavior in the :ref:`Playback popover <animation-editors-playback>` within an editors
     playback controls.
   - **Object Info** --
     Shows the current frame in parentheses, followed by the names of the selected
     :doc:`Collection </scene_layout/collections/index>`,
     the :ref:`active object <object-active>`, and the active data-block's name.
     When applicable, also shows the selected :doc:`Shape Key </animation/shape_keys/introduction>`
     and (in angle brackets) the :doc:`Marker </animation/markers>` on the current frame.
     If the object has a keyframe on the current frame, the Object Info is displayed in yellow.
   - **Grid Resolution** --
     When the view is aligned to a world axis (see :doc:`/editors/3dview/navigate/viewpoint`),
     the Text Info additionally shows the smallest distance between two parallel grid lines.

.. _bpy.types.View3DOverlay.show_stats:

Statistics
   Show information about the amount of objects and geometry.
   Note that the counters depend on the current selection.
   For example, selecting a mesh gives info on the number of vertices, edges, and faces,
   while selecting a light shows the number of lights in the scene.

   - **Objects** -- Number of the selected objects and the total count.
   - **Geometry** -- Displays information about the current scene depending on the mode and object type.
     This can be the number of vertices, faces, triangles, or bones.

.. _bpy.types.View3DOverlay.show_cursor:

3D Cursor
   Show the :doc:`3D Cursor </editors/3dview/3d_cursor>`.

.. _bpy.types.View3DOverlay.show_annotation:

Annotations
   Show :doc:`annotations </interface/annotate_tool>`.

.. _bpy.types.View3DOverlay.show_camera_guides:

Camera Guides
   Show camera guides
   (:ref:`Safe Areas <bpy.types.DisplaySafeAreas>` & :ref:`Composition Guides <bpy.types.Camera.show_composition>`).
   Only available in :ref:`camera view <bpy.ops.view3d.view_camera>`.

.. _bpy.types.View3DOverlay.show_look_dev:

Reference Spheres
   Show two spheres, one glossy and one diffuse, that react to lighting to assist in look development.
   Only available in *Material Preview* shading :doc:`Shading Mode </editors/3dview/display/shading>`.
   The size of the spheres can be adjusted in the :doc:`Viewport Preferences </editors/preferences/viewport>`.


Objects
-------

.. _bpy.types.View3DOverlay.show_extras:

Extras
   Show objects that don't have geometry (such as empties, cameras and lights).

   This also influences the display of:

   - Rigid Body :ref:`Collision Shape <bpy.types.RigidBodyObject.collision_shape>`
   - Object :ref:`Texture Space <bpy.types.Object.show_texture_space>`

.. _bpy.types.View3DOverlay.show_light_colors:

Light Colors
   Shades the outline of light objects to the color the light produces.

.. _bpy.types.View3DOverlay.show_relationship_lines:

Relationship Lines
   Show dashed lines indicating parent or constraint relationships.

.. _bpy.types.View3DOverlay.show_outline_selected:

Outline Selected
   Show an outline around selected objects.

.. _bpy.types.View3DOverlay.show_bones:

Bones
   Show Bones.

.. _bpy.types.View3DOverlay.show_motion_paths:

Motion Paths
   Show the :doc:`motion path </animation/motion_paths>` overlay.

.. _bpy.types.View3DOverlay.show_object_origins:

Origin
   Show the :doc:`origins </scene_layout/object/origin>` of the selected objects.

.. _bpy.types.View3DOverlay.show_object_origins_all:

Origin (All)
   Show the origins of all objects.

.. _bpy.types.View3DOverlay.bone_wire_alpha:

Bone Wireframe Opacity
   The maximum opacity used for bones drawn in the *Wireframe*
   :doc:`shading mode </editors/3dview/display/shading>` (or in *Solid* shading mode with X-Ray active).
   This is helpful when it is necessary to reduce clutter and focus on the mesh rather than bones.


Geometry
--------

.. _bpy.types.View3DOverlay.wireframe_threshold:
.. _bpy.types.View3DOverlay.show_wireframes:

Wireframe
   Display mesh edges. Similar to :ref:`Wireframe Shading <3dview-shading-rendered>`,
   but displays edges on top of existing shading.
   The value slider adjusts which edges to display:
   lower values hide edges on surfaces that are almost flat, while a value of 1 shows all edges.

   .. _bpy.types.View3DOverlay.wireframe_opacity:

   Opacity
      The opacity of the displayed edges, from 0 (invisible) to 1 (fully opaque).

.. _bpy.types.View3DOverlay.fade_inactive_alpha:
.. _bpy.types.View3DOverlay.show_fade_inactive:

Fade Inactive Geometry
   In modes other than Object Mode, fade out objects that you're not working on.
   The slider controls how much they're faded out.

.. _bpy.types.View3DOverlay.show_face_orientation:

Face Orientation
   Highlights the backside of faces in red. In general, if a face is shown in red
   on the outside of a mesh, it's most likely oriented incorrectly and needs
   to have its normal flipped. This can be done with the :ref:`bpy.ops.mesh.flip_normals`
   or :ref:`bpy.ops.mesh.normals_make_consistent` operators for meshes,
   and with the :ref:`modeling_surfaces_editing_segments_switch-direction` operator
   for Surface objects.


.. _3dview-overlays-view_node:

Viewer Node
-----------

Visualizes :doc:`/modeling/geometry_nodes/attributes_reference`
connected to the :doc:`/modeling/geometry_nodes/output/viewer`.

.. _bpy.types.View3DOverlay.show_viewer_attribute:

Viewer Node
   Visualize the value of the attribute connected to the *Viewer Node* as a grayscale color.

   .. _bpy.types.View3DOverlay.viewer_attribute_opacity:

   Color Opacity
      Opacity of the attribute that is currently visualized.

.. _bpy.types.View3DOverlay.show_viewer_text:

Attribute Text
   Show attribute values as text in viewport.


.. _bpy.types.SpaceView3D.show_reconstruction:

Motion Tracking
---------------

Show the :doc:`motion tracking </movie_clip/tracking/introduction>` overlay.

.. _bpy.types.SpaceView3D.show_camera_path:

Camera Path
   Show the reconstructed camera path.

.. _bpy.types.SpaceView3D.show_bundle_names:

Marker Names
   Show the names of the reconstructed tracking markers.

.. _bpy.types.SpaceView3D.tracks_display_type:

Tracks
   Change the display of the tracking markers:
   plain axes, arrows and so on.

.. _bpy.types.SpaceView3D.tracks_display_size:

Size
   Change the display size of the tracking markers.


.. _3dview-overlay-mesh_edit_mode:

Mesh Edit Mode Overlays
=======================

The following options are available when in Mesh Edit Mode.

.. _bpy.types.View3DOverlay.show_faces:

Faces
   Highlight selected faces. Affects all selection modes.

.. _bpy.types.View3DOverlay.show_face_center:

Center
   Show face center points in solid shading modes. (They're always shown in wireframe shading mode.)

   Only affects face selection mode.

.. _bpy.types.View3DOverlay.show_edge_crease:

Creases
   Display edges marked with a crease
   for the :doc:`Subdivision Surface Modifier </modeling/modifiers/generate/subdivision_surface>`.

.. _bpy.types.View3DOverlay.show_edge_sharp:

Sharp
   Display sharp edges, used with the :doc:`Edge Split modifier </modeling/modifiers/generate/edge_split>`.

.. _bpy.types.View3DOverlay.show_edge_bevel_weight:

Bevel
   Display weights created for the :doc:`Bevel Modifier </modeling/modifiers/generate/bevel>`.

.. _bpy.types.View3DOverlay.show_edge_seams:

Seams
   Display the :doc:`UV unwrapping seams </modeling/meshes/uv/unwrapping/seams>`.

.. _bpy.types.View3DOverlay.show_extra_indices:

Indices
   Display the indices of selected vertices, edges, and faces.


Shading
-------

.. _bpy.types.View3DOverlay.show_retopology:

Retopology
   This overlay is useful when you have a sculpted mesh with the desired shape and
   want to recreate it with better topology. It makes the edited mesh see-through
   (so that you can see the sculpted mesh underneath it) and optionally renders it
   in front of nearby geometry (so that you can see it underneath the sculpted mesh).

   .. _bpy.types.View3DOverlay.retopology_offset:

   Offset
      Distance to "move the edited mesh towards the camera." Use this to display the
      mesh in front of other objects that would normally occlude it.

.. _bpy.types.View3DOverlay.show_weight:

Vertex Groups Weights
   Visualize the weights of the active vertex group,
   much like in :doc:`Weight Paint </sculpt_paint/weight_paint/introduction>` mode.

   .. _bpy.types.ToolSettings.vertex_group_user:

   Zero Weights
      Display unreferenced and zero-weighted areas in black.
      This helps to identify areas with very low weights that have been painted onto.

      :None: Vertices are displayed in the usual way.
      :Active: Vertices are shown in black if they have no weight in the active vertex group.
      :All: Vertices are shown in black if they have no weight in any vertex group.


Mesh Analysis
-------------

Show the :ref:`modeling-mesh-analysis` overlay.


Measurement
-----------

Show numerical measures of the selected elements.
The :ref:`bpy.types.UnitSettings` can be set in the Scene properties.

.. _bpy.types.View3DOverlay.show_extra_edge_length:

Edge Length
   Show the length of selected edges.

.. _bpy.types.View3DOverlay.show_extra_edge_angle:

Edge Angle
   Show the angle of selected edges between two faces.

.. _bpy.types.View3DOverlay.show_extra_face_area:

Face Area
   Show the area of selected faces.

.. _bpy.types.View3DOverlay.show_extra_face_angle:

Face Angle
   Show the angle of selected face corners.

.. tip::

   Geometry connected to the selection is shown while transforming,
   allowing you to move a vertex and see the connected edge lengths for example.

.. note::

   These values respect the :ref:`Transform Space <modeling-mesh-transform-panel>`
   in the Sidebar. Use *Global* if you want the object's scale to be applied to the measurements.

.. seealso::

   The :doc:`Measure </editors/3dview/toolbar/measure>` tool for measuring
   arbitrary distances and angles.


.. _mesh-display-normals:

Normals
-------

.. _bpy.types.View3DOverlay.show_vertex_normals:
.. _bpy.types.View3DOverlay.show_split_normals:
.. _bpy.types.View3DOverlay.show_face_normals:

- Display vertex normals
- Display face normals at vertices (split normals)
- Display face normals

.. _bpy.types.View3DOverlay.normals_length:

Size
   The size to show the selected normals.

   .. _bpy.types.View3DOverlay.use_normals_constant_screen_size:

   Constant Screen Size Normals
      Keep the size of normals constant in relation to the zoom level.


Freestyle
---------

These settings apply to the :doc:`Freestyle </render/freestyle/introduction>`
Line Art renderer.

.. _bpy.types.View3DOverlay.show_freestyle_edge_marks:

Edge Marks
   Display Freestyle edge marks.

.. _bpy.types.View3DOverlay.show_freestyle_face_marks:

Face Marks
   Display Freestyle face marks.


Sculpt Mode Overlays
====================

.. _bpy.types.View3DOverlay.show_sculpt_mask:
.. _bpy.types.View3DOverlay.sculpt_mode_mask_opacity:

Mask
   Show :ref:`Masks <sculpt-mask-menu>` as overlays on an object. The opacity of the overlay can be adjusted.

.. _bpy.types.View3DOverlay.show_sculpt_face_sets:
.. _bpy.types.View3DOverlay.sculpt_mode_face_sets_opacity:

Face Sets
   Show :ref:`Face Sets <sculpting-editing-facesets>` as overlays on an object.
   The opacity of the overlay can be adjusted.


Vertex Paint Overlays
=====================

.. _bpy.types.View3DOverlay.vertex_paint_mode_opacity:

Stencil Mask Opacity
   Does nothing. (Stencil masks are only available for texture painting.)

.. _bpy.types.View3DOverlay.show_paint_wire:

Show Wire
   Display mesh edges in white (unlike the *Wireframe* overlay which shows them in black).


.. _3dview-overlay-weight-paint:

Weight Paint Overlays
=====================

.. _bpy.types.View3DOverlay.weight_paint_mode_opacity:

Opacity
   The opacity of the overlay.

Zero Weights
   Display unreferenced and zero-weighted areas in black.
   This helps to identify areas with very low weights that have been painted onto.

   :None: Vertices are displayed in the usual way.
   :Active: Vertices are shown in black if they have no weight in the active vertex group.
   :All: Vertices are shown in black if they have no weight in any vertex group.

.. _bpy.types.View3DOverlay.show_wpaint_contours:

Show Weight Contours
   Show contour lines formed by points with the same interpolated weight.

   This visualizes weight variations too small to be seen from colors and can be useful for judging
   the smoothness and consistency of gradients, e.g. when using smoothing tools and brushes.

Show Wire
   Display mesh edges in white (unlike the *Wireframe* overlay which shows them in black).


Texture Paint Overlays
======================

.. _bpy.types.View3DOverlay.texture_paint_mode_opacity:

Stencil Mask Opacity
   Opacity of the :doc:`stencil mask </sculpt_paint/texture_paint/tool_settings/mask>` overlay.


Pose Mode Overlays
==================

.. _bpy.types.View3DOverlay.show_xray_bone:
.. _bpy.types.View3DOverlay.xray_alpha_bone:

Fade Geometry
   Show the bones on top and face other geometry to the back.
   The opacity can be controlled with the slider.
   Only available in Pose Mode.


.. _3dview-overlay-grease-pencil:

Grease Pencil
=============

These overlays are available when a :doc:`/grease_pencil/index` object is selected.

.. _bpy.types.View3DOverlay.use_gpencil_onion_skin:

Onion Skin
   Show ghosts of the keyframes before and after the current frame.
   If :doc:`Multiframe </grease_pencil/multiframe>` is enabled,
   ghosts of the selected keyframes are shown instead.
   See :doc:`/grease_pencil/properties/onion_skinning`.

.. _bpy.types.View3DOverlay.use_gpencil_onion_skin_active_object:

Active Object Only
   Show only the onion skins of the active object.

.. _bpy.types.View3DOverlay.use_gpencil_fade_layers:
.. _bpy.types.View3DOverlay.gpencil_fade_layer:

Fade Inactive Layers
   Decrease the opacity of all the layers in the object other than the active one.
   The opacity factor can be controlled with the slider.

.. _bpy.types.View3DOverlay.use_gpencil_fade_objects:
.. _bpy.types.View3DOverlay.gpencil_fade_objects:

Fade Inactive Objects
   Cover all of the viewport except the active Grease Pencil object with a full color layer to improve visibility
   while drawing over complex scenes.

   .. _bpy.types.View3DOverlay.use_gpencil_fade_gp_objects:

   Fade Grease Pencil Objects
      Include or exclude Grease Pencil objects.

.. _bpy.types.View3DOverlay.use_gpencil_edit_lines:

Edit Lines :guilabel:`Edit, Sculpt, Weight Paint, or Vertex Paint Modes` :kbd:`Shift-Q`
   Shows a line between points on top of other geometry when editing strokes.

.. _bpy.types.View3DOverlay.use_gpencil_multiedit_line_only:

Only in Multiframe :kbd:`Shift-Alt-Q`
   When Multiframe is enabled and keyframes other than the current frame are selected,
   strokes on those keyframes are displayed as just their edit lines -- the strokes themselves are hidden.
   Note that this does not affect Onion Skinning.

Handles
   Controls the visibility of Bézier curve handles in edit mode.

   :None: Hides all Bézier curve handles, providing an unobstructed view of the curve.
   :Selected: Displays the handles only for selected control points.
   :All: Displays the handles for all control points in the curve.

.. _bpy.types.View3DOverlay.use_gpencil_show_directions:

Stroke Direction :guilabel:`Edit`
   Toggle the display of the selected strokes' start points (green) and end points (red) to visualize their direction.

.. _bpy.types.View3DOverlay.use_gpencil_show_material_name:

Material Name :guilabel:`Edit`
   Show material name next to the selected strokes.

.. rubric:: Vertex Paint

.. Vertex Opacity :guilabel:`Vertex Paint`
..    Opacity for vertices (points) and edit lines in Edit and Sculpt Mode.

.. _bpy.types.View3DOverlay.gpencil_vertex_paint_opacity:

Vertex Paint Opacity :guilabel:`Vertex Paint`
   The opacity of the vertex color overlay in Vertex Paint Mode and Draw Mode.
   Note that in Draw Mode, vertex paint is only visible in the *Material Preview*
   and *Rendered* shading modes by default. To see it in *Solid* mode, you either
   need to use Vertex Paint Mode, or set the :doc:`Color </render/workbench/color>`
   shading setting to *Attribute*.


.. _bpy.types.View3DOverlay.use_gpencil_grid:

Canvas
------

Display a grid over the Grease Pencil drawing plane.

.. _bpy.types.View3DOverlay.gpencil_grid_opacity:

Canvas Grid Opacity
   The opacity of the grid.

.. _bpy.types.View3DOverlay.use_gpencil_canvas_xray:

Canvas X-Ray
   Objects are drawn behind the canvas grid.

.. _bpy.types.View3DOverlay.gpencil_grid_subdivisions:

Subdivisions
   The number of subdivisions between grid lines.

.. _bpy.types.View3DOverlay.gpencil_grid_color:

Grid Color
   The color of the grid lines.

.. _bpy.types.View3DOverlay.gpencil_grid_scale:

Scale X/Y
   The horizontal/vertical size of the grid.

.. _bpy.types.View3DOverlay.gpencil_grid_offset:

Offset X/Y
   The amount to shift the grid up/down and left/right.
