
************
Introduction
************

Scenes are a way to organize your work. Each blend-file can contain multiple scenes,
which may share other data such as objects, materials, and collections.

A scene defines the visible objects, camera view, lighting setup,
and render settings that make up a specific part of a project.
For example, a single blend-file may include multiple scenes for different shots,
lighting setups, or stages of a production pipeline.

Scene management and library linking are based on Blender's
:doc:`Library and Data System </files/index>`.
If you are not familiar with the concepts of data-blocks, linking, and appending,
it is recommended to read that page first.


Scenes as Assets
================

Scenes can also be marked and used as :doc:`Assets </files/asset_libraries/index>`.
This allows them to appear in the :doc:`Asset Browser </editors/asset_browser>` for reuse across projects.

Scene assets are a convenient way to manage prebuilt scene templates, lighting rigs, or shot setups.
They store all relevant data (such as cameras, lights, and render settings) and can be dragged into any open Blender
file.

When a scene asset is dragged into another window (except the Asset Browser itself),
Blender performs one of the following actions:

- **Link or Append:** Imports the scene into the current blend-file as a linked or appended data-block.
- **Activate:** Sets the imported (or linked) scene as the *active* one in the window.

Scene assets generate preview images automatically by rendering from the active camera in *Solid View* mode.
For this to work, the scene must contain an active camera.

Typical uses for scene assets include:

- Creating reusable lighting or studio setups.
- Storing shot layouts for multi-shot projects.
- Maintaining consistent render settings across files.
- Building base templates for new projects or departments.


Scenes in the Video Sequencer
=============================

Scenes can also be used as :doc:`Scene Strips </video_editing/edit/montage/strips/scene>` in the
:doc:`Video Sequencer </editors/video_sequencer/index>`.
This allows you to composite or edit multiple scenes together in one timeline.

For example, each shot of an animation can be stored in its own scene,
and then combined in a master scene that uses scene strips to sequence them in order.
This workflow is useful for multi-shot projects, trailers,
or layout editing without the need to render intermediate files.

When used as strips, scenes are rendered dynamically during playback or rendering,
and they share the same data-blocks unless they were created as full copies.


Controls
========

.. reference::

   :Menu:      :menuselection:`Topbar --> Scene`

You can select and create scenes with the *Scene* data-block menu in the
:doc:`Topbar </interface/window_system/topbar>`.

.. figure:: /images/scene-layout_scene_introduction_menu.png
   :align: right
   :alt: Scene data-block menu

   Scene data-block menu.


Scenes
   A list of available scenes in the current blend-file.

Add
   New
      Creates an empty scene with default values.
   Copy Settings
      Creates an empty scene but copies render and world settings from the active scene.
   Linked Copy
      Creates a new scene that shares all data with the current one.
      The new scene contains links to the same collections, objects, and data-blocks as the original.
      Changes made in one scene automatically affect the other, since they reference the same data.
   Full Copy
      Creates a fully independent scene with unique copies of all objects and their data.
      This is useful for variations or alternate versions of a scene that should not affect the original.

   .. note::

      The *Add Scene* options determine which data are copied and which are shared (linked).
      Objects reference *Object Data* such as meshes or lights, and scenes can share or duplicate this relationship.

.. _bpy.ops.scene.delete:

:bl-icon:`x` (Delete Scene)
   Deletes the current scene data-block.
   Note that Blender always requires at least one scene in a file; you cannot delete the last remaining one.
