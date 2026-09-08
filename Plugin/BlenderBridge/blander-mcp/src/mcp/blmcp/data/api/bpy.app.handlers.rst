Application Handlers (bpy.app.handlers)
=======================================

.. module:: bpy.app.handlers

This module contains callback lists


Basic Handler Example
+++++++++++++++++++++

This script shows the most simple example of adding a handler.

.. literalinclude:: ./examples/bpy.app.handlers.0.py
   :lines: 8-


Persistent Handler Example
++++++++++++++++++++++++++

By default handlers are freed when loading new files, in some cases you may
want the handler stay running across multiple files (when the handler is
part of an add-on for example).

For this the :data:`bpy.app.handlers.persistent` decorator needs to be used.

.. literalinclude:: ./examples/bpy.app.handlers.1.py
   :lines: 12-


Note on Altering Data
+++++++++++++++++++++

Altering data from handlers should be done carefully. While rendering the
``frame_change_pre`` and ``frame_change_post`` handlers are called from one
thread and the viewport updates from a different thread. If the handler changes
data that is accessed by the viewport, this can cause a crash of Blender. In
such cases, lock the interface (Render → Lock Interface or
:data:`bpy.types.RenderSettings.use_lock_interface`) before starting a render.

Below is an example of a mesh that is altered from a handler:

.. literalinclude:: ./examples/bpy.app.handlers.2.py
   :lines: 16-

.. data:: animation_playback_post

   on ending animation playback. Accepts one or two arguments: The scene data-block, and optionally the dependency graph being updated
   
   :type: list[Callable[[bpy.types.Scene, bpy.types.Depsgraph], None] | Callable[[bpy.types.Scene], None]]


.. data:: animation_playback_pre

   on starting animation playback. Accepts one or two arguments: The scene data-block, and optionally the dependency graph being updated
   
   :type: list[Callable[[bpy.types.Scene, bpy.types.Depsgraph], None] | Callable[[bpy.types.Scene], None]]


.. data:: annotation_post

   on drawing an annotation (after). Accepts two arguments: the annotation data-block and dependency graph
   
   :type: list[Callable[[bpy.types.GreasePencil, bpy.types.Depsgraph], None]]


.. data:: annotation_pre

   on drawing an annotation (before). Accepts two arguments: the annotation data-block and dependency graph
   
   :type: list[Callable[[bpy.types.GreasePencil, bpy.types.Depsgraph], None]]


.. data:: blend_import_post

   on linking or appending data (after). Accepts one argument: a BlendImportContext
   
   :type: list[Callable[[bpy.types.BlendImportContext], None]]


.. data:: blend_import_pre

   on linking or appending data (before). Accepts one argument: a BlendImportContext
   
   :type: list[Callable[[bpy.types.BlendImportContext], None]]


.. data:: composite_cancel

   on a compositing background job (cancel). Accepts one argument: the scene data-block
   
   :type: list[Callable[[bpy.types.Scene], None]]


.. data:: composite_post

   on a compositing background job (after). Accepts one argument: the scene data-block
   
   :type: list[Callable[[bpy.types.Scene], None]]


.. data:: composite_pre

   on a compositing background job (before). Accepts one argument: the scene data-block
   
   :type: list[Callable[[bpy.types.Scene], None]]


.. data:: depsgraph_update_post

   on depsgraph update (post). Accepts one or two arguments: The scene data-block, and optionally the dependency graph being updated
   
   :type: list[Callable[[bpy.types.Scene, bpy.types.Depsgraph], None] | Callable[[bpy.types.Scene], None]]


.. data:: depsgraph_update_pre

   on depsgraph update (pre). Accepts one or two arguments: The scene data-block, and optionally the dependency graph being updated
   
   :type: list[Callable[[bpy.types.Scene, bpy.types.Depsgraph], None] | Callable[[bpy.types.Scene], None]]


.. data:: exit_pre

   just before Blender shuts down, while all data is still valid. Accepts one boolean argument. True indicates either that a user has been using Blender and exited, or that Blender is exiting in a circumstance that should be treated as if that were the case. False indicates that Blender is running in background mode, or is exiting due to failed command line arguments, etc.
   
   :type: list[Callable[[bool], None]]


.. data:: frame_change_post

   Called after frame change for playback and rendering, after the data has been evaluated for the new frame. Accepts one or two arguments: The scene data-block, and optionally the dependency graph being updated
   
   :type: list[Callable[[bpy.types.Scene, bpy.types.Depsgraph], None] | Callable[[bpy.types.Scene], None]]


.. data:: frame_change_pre

   Called when a frame change is triggered for playback and rendering, before any data is evaluated for the new frame. This makes it possible to change data and relations (for example swap an object to another mesh) for the new frame. Note that this handler is **not** to be used as 'before the frame changes' event. The dependency graph is not available in this handler, as data and relations may have been altered and the dependency graph has not yet been updated for that. Accepts one or two arguments: The scene data-block, and optionally the dependency graph being updated
   
   :type: list[Callable[[bpy.types.Scene, bpy.types.Depsgraph], None] | Callable[[bpy.types.Scene], None]]


.. data:: load_factory_preferences_post

   on loading factory preferences (after)
   
   :type: list[Callable[[], None]]


.. data:: load_factory_startup_post

   on loading factory startup (after)
   
   :type: list[Callable[[], None]]


.. data:: load_post

   on loading a new blend file (after). Accepts one argument: the file being loaded, an empty string for the startup-file.
   
   :type: list[Callable[[str], None]]


.. data:: load_post_fail

   on failure to load a new blend file (after). Accepts one argument: the file being loaded, an empty string for the startup-file.
   
   :type: list[Callable[[str], None]]


.. data:: load_pre

   on loading a new blend file (before). Accepts one argument: the file being loaded, an empty string for the startup-file.
   
   :type: list[Callable[[str], None]]


.. data:: object_bake_cancel

   on canceling a bake job; will be called in the main thread. Accepts one argument: the object data-block being baked
   
   :type: list[Callable[[bpy.types.Object], None]]


.. data:: object_bake_complete

   on completing a bake job; will be called in the main thread. Accepts one argument: the object data-block being baked
   
   :type: list[Callable[[bpy.types.Object], None]]


.. data:: object_bake_pre

   before starting a bake job. Accepts one argument: the object data-block being baked
   
   :type: list[Callable[[bpy.types.Object], None]]


.. data:: redo_post

   on loading a redo step (after). Accepts one argument: the scene data-block
   
   :type: list[Callable[[bpy.types.Scene], None]]


.. data:: redo_pre

   on loading a redo step (before). Accepts one argument: the scene data-block
   
   :type: list[Callable[[bpy.types.Scene], None]]


.. data:: render_cancel

   on canceling a render job. Accepts one argument: the scene data-block being rendered
   
   :type: list[Callable[[bpy.types.Scene], None]]


.. data:: render_complete

   on completion of render job. Accepts one argument: the scene data-block being rendered
   
   :type: list[Callable[[bpy.types.Scene], None]]


.. data:: render_init

   on initialization of a render job. Accepts one argument: the scene data-block being rendered
   
   :type: list[Callable[[bpy.types.Scene], None]]


.. data:: render_post

   on render (after). Accepts one argument: the scene data-block being rendered
   
   :type: list[Callable[[bpy.types.Scene], None]]


.. data:: render_pre

   on render (before). Accepts one argument: the scene data-block being rendered
   
   :type: list[Callable[[bpy.types.Scene], None]]


.. data:: render_stats

   on printing render statistics. Accepts one argument: the render stats (render/saving time plus in background mode frame/used [peak] memory).
   
   :type: list[Callable[[str], None]]


.. data:: render_write

   on writing a render frame (directly after the frame is written). Accepts one argument: the scene data-block being rendered
   
   :type: list[Callable[[bpy.types.Scene], None]]


.. data:: save_post

   on saving a blend file (after). Accepts one argument: the file being saved, an empty string for the startup-file.
   
   :type: list[Callable[[str], None]]


.. data:: save_post_fail

   on failure to save a blend file (after). Accepts one argument: the file being saved, an empty string for the startup-file.
   
   :type: list[Callable[[str], None]]


.. data:: save_pre

   on saving a blend file (before). Accepts one argument: the file being saved, an empty string for the startup-file.
   
   :type: list[Callable[[str], None]]


.. data:: translation_update_post

   on translation settings update
   
   :type: list[Callable[[], None]]


.. data:: undo_post

   on loading an undo step (after). Accepts one argument: the scene data-block
   
   :type: list[Callable[[bpy.types.Scene], None]]


.. data:: undo_pre

   on loading an undo step (before). Accepts one argument: the scene data-block
   
   :type: list[Callable[[bpy.types.Scene], None]]


.. data:: version_update

   on ending the versioning code
   
   :type: list[Callable[[], None]]


.. data:: xr_session_start_pre

   on starting an xr session (before)
   
   :type: list[Callable[[], None]]


.. data:: persistent

   Function decorator for callback functions not to be removed when loading new files
   
   :type: type


