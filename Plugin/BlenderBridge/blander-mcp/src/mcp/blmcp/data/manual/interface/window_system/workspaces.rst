.. _bpy.ops.workspace:
.. _bpy.types.Window.workspace:

**********
Workspaces
**********

Workspaces are essentially predefined window layouts.
Each Workspace consists of a set of :doc:`Areas </interface/window_system/areas>`
containing :doc:`Editors </editors/index>`, and is geared towards a specific task such as
modeling, animating, or scripting. You'll typically switch between
multiple Workspaces while working on a project.

.. figure:: /images/interface_window-system_workspaces_screen.png
   :align: center

   Workspaces are located at the Topbar.


.. _workspaces-controls:

Controls
========

Tabs
   Click on the tabs to switch between workspaces.
   Double-click a tab to rename the workspace.

.. _bpy.ops.workspace.add:

:bl-icon:`add` Add Workspace
   Adds a new workspace from a predefined template (e.g. *Modeling*, *Sculpting*, *Compositing*).

.. rubric:: Context Menu :kbd:`RMB`

.. _bpy.ops.workspace.duplicate:

Duplicate
   Makes a copy of the selected workspace, including its screen layout and editors.

.. _bpy.ops.workspace.delete:

Delete
   Deletes the selected workspace.
   If it is the last workspace, it cannot be removed.

.. _bpy.ops.workspace.reorder_to_front:
.. _bpy.ops.workspace.reorder_to_back:

Reorder to Front/Back
   Moves the workspace tab to the first (front) or last (back) position in the tab list.

.. _bpy.ops.screen.workspace_cycle:

Previous Workspace :kbd:`Ctrl-PageUp`
   Activates the workspace immediately to the left of the current one.

Next Workspace :kbd:`Ctrl-PageDown`
   Activates the workspace immediately to the right of the current one.

.. _bpy.ops.workspace.delete_all_others:

Delete Other Workspaces
   Removes all workspaces except the one that was right-clicked on.


Default Workspaces
==================

Blender's default startup shows the "Layout" workspace in the main area.
This workspace is a general workspace to preview your scene
and contains the following Editors:

- :doc:`3D Viewport </editors/3dview/introduction>` on top left.
- :doc:`Outliner </editors/outliner/introduction>` on top right.
- :doc:`Properties </editors/properties_editor>` on bottom right.
- :doc:`Timeline </editors/timeline>` on bottom left.

.. figure:: /images/interface_window-system_workspaces_layout.png
   :align: center

   Blender's 'Layout' Workspace with four editors.

   3D Viewport (yellow), Outliner (green), Properties (blue) and Timeline (red).

Blender also has several other workspaces added by default:

:Modeling: For modification of geometry by modeling tools.
:Sculpting: For modification of meshes by sculpting tools.
:UV Editing: For mapping of image texture coordinates to 3D surfaces.
:Texture Paint: For coloring image textures in the 3D Viewport.
:Shading: For specifying material properties for rendering.
:Animation: For making properties of objects dependent on time.
:Rendering: For viewing and analyzing rendering results.
:Compositing: For combining and post-processing of images and rendering information.
:Geometry Nodes: For procedural modeling using :doc:`/modeling/geometry_nodes/index`.
:Scripting: For interacting with Blender's Python API and writing scripts.


Additional Workspaces
---------------------

Blender has a couple additional Workspaces to choose from when adding a new Workspace:


.. rubric:: 2D Animation

:2D Animation: General workspace to work with Grease Pencil.
:2D Full Canvas: Similar to "2D Animation" but contains a larger canvas.


.. rubric:: VFX

:Masking: For creating 2D masks for compositing or video editing.
:Motion Tracking: For calculating camera motion and stabilizing video footage.


.. rubric:: Video Editing

:Video Editing: For sequencing together media into one video.


Save and Override
=================

The workspaces are saved in the blend-file.
When you open a file, enabling :ref:`Load UI <file-load-ui>` in the File Browser indicates that Blender should
use the file's screen layout rather than the current one.

A custom set of workspaces can be saved as a part of the :doc:`/getting_started/configuration/defaults`.


Workspace Settings
==================

.. reference::

   :Editor:    :doc:`/editors/properties_editor`
   :Panel:     :menuselection:`Tool tab --> Workspace`

.. _bpy.types.WorkSpace.use_pin_scene:

Pin Scene
   When enabled, the current workspace will remember the currently selected scene.
   Then, whenever you activate the workspace, it'll automatically switch back to that scene.

.. _bpy.types.WorkSpace.object_mode:

Mode
   Switch to this :doc:`Mode </editors/3dview/modes>` when activating the workspace.

.. _bpy.types.WorkSpace.sequencer_scene:

Sequencer Scene
   The scene containing the edit that is used by the video sequence editor.
   See :doc:`/video_editing/sequencer_scene`.

.. _bpy.types.WorkSpace.use_scene_time_sync:

Sync Scene Time
   Sync the active scene and time based on the current :ref:`scene strip <bpy.types.SceneStrip>` in the video sequence
   editor.
   See :doc:`/video_editing/sequencer_scene`.

.. _bpy.ops.wm.owner_enable:
.. _bpy.ops.wm.owner_disable:
.. _bpy.types.WorkSpace.use_filter_by_owner:

Filter Add-ons
   Determines which :doc:`add-ons </addons/index>` are enabled in the active workspace.
   When unchecked, the global add-ons will be used.
   When checked, you can enable individual add-ons in the list below.
