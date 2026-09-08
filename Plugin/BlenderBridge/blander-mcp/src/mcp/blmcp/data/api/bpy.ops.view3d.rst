View3D Operators
================

.. module:: bpy.ops.view3d

.. function:: bone_select_menu(*, name='', extend=False, deselect=False, toggle=False)

   Menu bone selection

   :param name: Bone Name, (optional)
   :type name: str
   :param extend: Extend, (optional)
   :type extend: bool
   :param deselect: Deselect, (optional)
   :type deselect: bool
   :param toggle: Toggle, (optional)
   :type toggle: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: camera_background_image_add(*, filepath="", relative_path=True, name="", session_uid=0)

   Add a new background image to the active camera

   :param filepath: Filepath, Path to image file (optional, never None, blend relative ``//`` prefix supported)
   :type filepath: str
   :param relative_path: Relative Path, Select the file relative to the blend file (optional)
   :type relative_path: bool
   :param name: Name, Name of the data-block to use by the operator (optional, never None)
   :type name: str
   :param session_uid: Session UID, Session UID of the data-block to use by the operator (in [-inf, inf], optional)
   :type session_uid: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: camera_background_image_remove(*, index=0)

   Remove a background image from the camera

   :param index: Index, Background image index to remove (in [0, inf], optional)
   :type index: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: camera_to_view()

   Set camera view to active view

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: camera_to_view_selected()

   Move the camera so selected objects are framed

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: clear_render_border()

   Clear the boundaries of the border render and disable border render

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: clip_border(*, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True)

   Set the view clipping region

   :param xmin: X Min, (in [-inf, inf], optional)
   :type xmin: int
   :param xmax: X Max, (in [-inf, inf], optional)
   :type xmax: int
   :param ymin: Y Min, (in [-inf, inf], optional)
   :type ymin: int
   :param ymax: Y Max, (in [-inf, inf], optional)
   :type ymax: int
   :param wait_for_input: Wait for Input, (optional)
   :type wait_for_input: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: copybuffer()

   Copy the selected objects to the internal clipboard

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: cursor3d(*, use_depth=True, orientation='VIEW')

   Set the location of the 3D cursor

   :param use_depth: Surface Project, Project onto the surface (optional)
   :type use_depth: bool
   :param orientation: Orientation, Preset viewpoint to use (optional)

      - ``NONE``
        None -- Leave orientation unchanged.
      - ``VIEW``
        View -- Orient to the viewport.
      - ``XFORM``
        Transform -- Orient to the current transform setting.
      - ``GEOM``
        Geometry -- Match the surface normal.
   :type orientation: Literal['NONE', 'VIEW', 'XFORM', 'GEOM']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: dolly(*, mx=0, my=0, delta=0, use_cursor_init=True)

   Dolly in/out in the view

   :param mx: Region Position X, (in [0, inf], optional)
   :type mx: int
   :param my: Region Position Y, (in [0, inf], optional)
   :type my: int
   :param delta: Delta, (in [-inf, inf], optional)
   :type delta: int
   :param use_cursor_init: Use Mouse Position, Allow the initial mouse position to be used (optional)
   :type use_cursor_init: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: drop_world(*, name="", session_uid=0)

   Drop a world into the scene

   :param name: Name, Name of the data-block to use by the operator (optional, never None)
   :type name: str
   :param session_uid: Session UID, Session UID of the data-block to use by the operator (in [-inf, inf], optional)
   :type session_uid: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: edit_mesh_extrude_individual_move()

   Extrude each individual face separately along local normals

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/view3d.py\:30 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/view3d.py#L30>`__

.. function:: edit_mesh_extrude_manifold_normal()

   Extrude manifold region along normals

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/view3d.py\:198 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/view3d.py#L198>`__

.. function:: edit_mesh_extrude_move_normal(*, dissolve_and_intersect=False)

   Extrude region together along the average normal

   :param dissolve_and_intersect: Dissolve and Intersect, Dissolves adjacent faces and intersects new geometry (optional)
   :type dissolve_and_intersect: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/view3d.py\:166 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/view3d.py#L166>`__


.. function:: edit_mesh_extrude_move_shrink_fatten()

   Extrude region together along local normals

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/view3d.py\:182 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/view3d.py#L182>`__

.. function:: fly()

   Interactively fly around the scene

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: interactive_add(*, primitive_type='CUBE', plane_origin_base='EDGE', plane_origin_depth='EDGE', plane_aspect_base='FREE', plane_aspect_depth='FREE', wait_for_input=True)

   Interactively add an object

   :param primitive_type: Primitive, (optional)
   :type primitive_type: Literal['CUBE', 'CYLINDER', 'CONE', 'SPHERE_UV', 'SPHERE_ICO']
   :param plane_origin_base: Origin, The initial position for placement (optional)

      - ``EDGE``
        Edge -- Start placing the edge position.
      - ``CENTER``
        Center -- Start placing the center position.
   :type plane_origin_base: Literal['EDGE', 'CENTER']
   :param plane_origin_depth: Origin, The initial position for placement (optional)

      - ``EDGE``
        Edge -- Start placing the edge position.
      - ``CENTER``
        Center -- Start placing the center position.
   :type plane_origin_depth: Literal['EDGE', 'CENTER']
   :param plane_aspect_base: Aspect, The initial aspect setting (optional)

      - ``FREE``
        Free -- Use an unconstrained aspect.
      - ``FIXED``
        Fixed -- Use a fixed 1:1 aspect.
   :type plane_aspect_base: Literal['FREE', 'FIXED']
   :param plane_aspect_depth: Aspect, The initial aspect setting (optional)

      - ``FREE``
        Free -- Use an unconstrained aspect.
      - ``FIXED``
        Fixed -- Use a fixed 1:1 aspect.
   :type plane_aspect_depth: Literal['FREE', 'FIXED']
   :param wait_for_input: Wait for Input, (optional)
   :type wait_for_input: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: localview(*, frame_selected=True)

   Toggle display of selected object(s) separately and centered in view

   :param frame_selected: Frame Selected, Move the view to frame the selected objects (optional)
   :type frame_selected: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: localview_remove_from()

   Move selected objects out of local view

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: move(*, use_cursor_init=True)

   Move the view

   :param use_cursor_init: Use Mouse Position, Allow the initial mouse position to be used (optional)
   :type use_cursor_init: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: navigate()

   Interactively navigate around the scene (uses the mode (walk/fly) preference)

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: object_as_camera()

   Set the active object as the active camera for this view or scene

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: object_mode_pie_or_toggle()

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: pastebuffer(*, autoselect=True, active_collection=True)

   Paste objects from the internal clipboard

   :param autoselect: Select, Select pasted objects (optional)
   :type autoselect: bool
   :param active_collection: Active Collection, Put pasted objects in the active collection (optional)
   :type active_collection: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: render_border(*, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True)

   Set the boundaries of the border render and enable border render

   :param xmin: X Min, (in [-inf, inf], optional)
   :type xmin: int
   :param xmax: X Max, (in [-inf, inf], optional)
   :type xmax: int
   :param ymin: Y Min, (in [-inf, inf], optional)
   :type ymin: int
   :param ymax: Y Max, (in [-inf, inf], optional)
   :type ymax: int
   :param wait_for_input: Wait for Input, (optional)
   :type wait_for_input: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: rotate(*, use_cursor_init=True)

   Rotate the view

   :param use_cursor_init: Use Mouse Position, Allow the initial mouse position to be used (optional)
   :type use_cursor_init: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: ruler_add()

   Add ruler

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: ruler_remove()

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select(*, extend=False, deselect=False, toggle=False, deselect_all=False, select_passthrough=False, center=False, enumerate=False, object=False, location=(0, 0))

   Select and activate item(s)

   :param extend: Extend, Extend selection instead of deselecting everything first (optional)
   :type extend: bool
   :param deselect: Deselect, Remove from selection (optional)
   :type deselect: bool
   :param toggle: Toggle Selection, Toggle the selection (optional)
   :type toggle: bool
   :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor (optional)
   :type deselect_all: bool
   :param select_passthrough: Only Select Unselected, Ignore the select action when the element is already selected (optional)
   :type select_passthrough: bool
   :param center: Center, Use the object center when selecting, in edit mode used to extend object selection (optional)
   :type center: bool
   :param enumerate: Enumerate, List objects under the mouse (object mode only) (optional)
   :type enumerate: bool
   :param object: Object, Use object selection (edit mode only) (optional)
   :type object: bool
   :param location: Location, Mouse location (array of 2 items, in [-inf, inf], optional)
   :type location: Sequence[int]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_box(*, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, mode='SET')

   Select items using box selection

   :param xmin: X Min, (in [-inf, inf], optional)
   :type xmin: int
   :param xmax: X Max, (in [-inf, inf], optional)
   :type xmax: int
   :param ymin: Y Min, (in [-inf, inf], optional)
   :type ymin: int
   :param ymax: Y Max, (in [-inf, inf], optional)
   :type ymax: int
   :param wait_for_input: Wait for Input, (optional)
   :type wait_for_input: bool
   :param mode: Mode, (optional)

      - ``SET``
        Set -- Set a new selection.
      - ``ADD``
        Extend -- Extend existing selection.
      - ``SUB``
        Subtract -- Subtract existing selection.
      - ``XOR``
        Difference -- Invert existing selection.
      - ``AND``
        Intersect -- Intersect existing selection.
   :type mode: Literal['SET', 'ADD', 'SUB', 'XOR', 'AND']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_circle(*, x=0, y=0, radius=25, wait_for_input=True, mode='SET')

   Select items using circle selection

   :param x: X, (in [-inf, inf], optional)
   :type x: int
   :param y: Y, (in [-inf, inf], optional)
   :type y: int
   :param radius: Radius, (in [1, inf], optional)
   :type radius: int
   :param wait_for_input: Wait for Input, (optional)
   :type wait_for_input: bool
   :param mode: Mode, (optional)

      - ``SET``
        Set -- Set a new selection.
      - ``ADD``
        Extend -- Extend existing selection.
      - ``SUB``
        Subtract -- Subtract existing selection.
   :type mode: Literal['SET', 'ADD', 'SUB']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_lasso(*, path=None, use_smooth_stroke=False, smooth_stroke_factor=0.75, smooth_stroke_radius=35, mode='SET')

   Select items using lasso selection

   :param path: Path, (optional)
   :type path: :class:`bpy_prop_collection`\ [:class:`OperatorMousePath`] | None
   :param use_smooth_stroke: Stabilize Stroke, Selection lags behind mouse and follows a smoother path (optional)
   :type use_smooth_stroke: bool
   :param smooth_stroke_factor: Smooth Stroke Factor, Higher values give a smoother stroke (in [0.5, 0.99], optional)
   :type smooth_stroke_factor: float
   :param smooth_stroke_radius: Smooth Stroke Radius, Minimum distance from last point before selection continues (in [10, 200], optional)
   :type smooth_stroke_radius: int
   :param mode: Mode, (optional)

      - ``SET``
        Set -- Set a new selection.
      - ``ADD``
        Extend -- Extend existing selection.
      - ``SUB``
        Subtract -- Subtract existing selection.
      - ``XOR``
        Difference -- Invert existing selection.
      - ``AND``
        Intersect -- Intersect existing selection.
   :type mode: Literal['SET', 'ADD', 'SUB', 'XOR', 'AND']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_menu(*, name='', extend=False, deselect=False, toggle=False)

   Menu object selection

   :param name: Object Name, (optional)
   :type name: str
   :param extend: Extend, (optional)
   :type extend: bool
   :param deselect: Deselect, (optional)
   :type deselect: bool
   :param toggle: Toggle, (optional)
   :type toggle: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: smoothview()

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: snap_cursor_to_active()

   Snap 3D cursor to the active item

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: snap_cursor_to_center()

   Snap 3D cursor to the world origin

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: snap_cursor_to_grid()

   Snap 3D cursor to the nearest grid division

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: snap_cursor_to_selected()

   Snap 3D cursor to the middle of the selected item(s)

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: snap_selected_to_active()

   Snap selected item(s) to the active item

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: snap_selected_to_cursor(*, use_offset=True, use_rotation=False)

   Snap selected item(s) to the 3D cursor

   :param use_offset: Offset, If the selection should be snapped as a whole or by each object center (optional)
   :type use_offset: bool
   :param use_rotation: Rotation, If the selection should be rotated to match the cursor (optional)
   :type use_rotation: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: snap_selected_to_grid()

   Snap selected item(s) to their nearest grid division

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: toggle_matcap_flip()

   Flip MatCap

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: toggle_shading(*, type='WIREFRAME')

   Toggle shading type in 3D viewport

   :param type: Type, Shading type to toggle (optional)

      - ``WIREFRAME``
        Wireframe -- Toggle wireframe shading.
      - ``SOLID``
        Solid -- Toggle solid shading.
      - ``MATERIAL``
        Material Preview -- Toggle material preview shading.
      - ``RENDERED``
        Rendered -- Toggle rendered shading.
   :type type: Literal['WIREFRAME', 'SOLID', 'MATERIAL', 'RENDERED']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: toggle_xray()

   Transparent scene display. Allow selecting through items

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: transform_gizmo_set(*, extend=False, type=set())

   Set the current transform gizmo

   :param extend: Extend, (optional)
   :type extend: bool
   :param type: Type, (optional)
   :type type: set[Literal['TRANSLATE', 'ROTATE', 'SCALE']]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/view3d.py\:245 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/view3d.py#L245>`__


.. function:: view_all(*, use_all_regions=False, center=False)

   View all objects in scene

   :param use_all_regions: All Regions, View selected for all regions (optional)
   :type use_all_regions: bool
   :param center: Center, (optional)
   :type center: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: view_axis(*, type='LEFT', align_active=False, relative=False)

   Use a preset viewpoint

   :param type: View, Preset viewpoint to use (optional)

      - ``LEFT``
        Left -- View from the left.
      - ``RIGHT``
        Right -- View from the right.
      - ``BOTTOM``
        Bottom -- View from the bottom.
      - ``TOP``
        Top -- View from the top.
      - ``FRONT``
        Front -- View from the front.
      - ``BACK``
        Back -- View from the back.
   :type type: Literal['LEFT', 'RIGHT', 'BOTTOM', 'TOP', 'FRONT', 'BACK']
   :param align_active: Align Active, Align to the active object's axis (optional)
   :type align_active: bool
   :param relative: Relative, Rotate relative to the current orientation (optional)
   :type relative: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: view_camera()

   Toggle the camera view

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: view_center_camera()

   Center the camera view, resizing the view to fit its bounds

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: view_center_cursor()

   Center the view so that the cursor is in the middle of the view

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: view_center_lock()

   Center the view lock offset

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: view_center_pick()

   Center the view to the Z-depth position under the mouse cursor

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: view_lock_clear()

   Clear all view locking

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: view_lock_to_active()

   Lock the view to the active object/bone

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: view_orbit(*, angle=0.0, type='ORBITLEFT')

   Orbit the view

   :param angle: Roll, (in [-inf, inf], optional)
   :type angle: float
   :param type: Orbit, Direction of View Orbit (optional)

      - ``ORBITLEFT``
        Orbit Left -- Orbit the view around to the left.
      - ``ORBITRIGHT``
        Orbit Right -- Orbit the view around to the right.
      - ``ORBITUP``
        Orbit Up -- Orbit the view up.
      - ``ORBITDOWN``
        Orbit Down -- Orbit the view down.
   :type type: Literal['ORBITLEFT', 'ORBITRIGHT', 'ORBITUP', 'ORBITDOWN']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: view_pan(*, type='PANLEFT')

   Pan the view in a given direction

   :param type: Pan, Direction of View Pan (optional)

      - ``PANLEFT``
        Pan Left -- Pan the view to the left.
      - ``PANRIGHT``
        Pan Right -- Pan the view to the right.
      - ``PANUP``
        Pan Up -- Pan the view up.
      - ``PANDOWN``
        Pan Down -- Pan the view down.
   :type type: Literal['PANLEFT', 'PANRIGHT', 'PANUP', 'PANDOWN']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: view_persportho()

   Switch the current view from perspective/orthographic projection

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: view_roll(*, angle=0.0, type='ANGLE')

   Roll the view

   :param angle: Roll, (in [-inf, inf], optional)
   :type angle: float
   :param type: Roll Angle Source, How roll angle is calculated (optional)

      - ``ANGLE``
        Roll Angle -- Roll the view using an angle value.
      - ``LEFT``
        Roll Left -- Roll the view around to the left.
      - ``RIGHT``
        Roll Right -- Roll the view around to the right.
   :type type: Literal['ANGLE', 'LEFT', 'RIGHT']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: view_selected(*, use_all_regions=False)

   Move the view to the selection center

   :param use_all_regions: All Regions, View selected for all regions (optional)
   :type use_all_regions: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: walk()

   Interactively walk around the scene

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: zoom(*, mx=0, my=0, delta=0, use_cursor_init=True)

   Zoom in/out in the view

   :param mx: Region Position X, (in [0, inf], optional)
   :type mx: int
   :param my: Region Position Y, (in [0, inf], optional)
   :type my: int
   :param delta: Delta, (in [-inf, inf], optional)
   :type delta: int
   :param use_cursor_init: Use Mouse Position, Allow the initial mouse position to be used (optional)
   :type use_cursor_init: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: zoom_border(*, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, zoom_out=False)

   Zoom in the view to the nearest object contained in the border

   :param xmin: X Min, (in [-inf, inf], optional)
   :type xmin: int
   :param xmax: X Max, (in [-inf, inf], optional)
   :type xmax: int
   :param ymin: Y Min, (in [-inf, inf], optional)
   :type ymin: int
   :param ymax: Y Max, (in [-inf, inf], optional)
   :type ymax: int
   :param wait_for_input: Wait for Input, (optional)
   :type wait_for_input: bool
   :param zoom_out: Zoom Out, (optional)
   :type zoom_out: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: zoom_camera_1_to_1()

   Match the camera to 1:1 to the render output

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
