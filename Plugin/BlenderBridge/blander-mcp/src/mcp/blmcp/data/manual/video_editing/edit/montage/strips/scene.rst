.. _bpy.types.SceneStrip:

***********
Scene Strip
***********

Scene strips are a way to insert the render output of another scene into your sequence.
Instead of rendering out a video, then inserting the video file, you can insert the scene directly.

The strip length will be determined based on the animation settings in that scene.

.. note::

   Scene strips cannot be used to reference the sequence's own scene; a secondary scene must be used instead.


Adding Scene Strips
===================

Existing scenes can be added from the :menuselection:`Add --> Scene --> "Scene Name"`.
Additionally, any scene asset in the current file or in an :doc:`Asset Library </files/asset_libraries/introduction>`
will also show up in the :menuselection:`Add --> Scene`. If a scene asset is assigned to a :doc:`Catalog
</files/asset_libraries/catalogs>`, the catalog hierarchy will show up as a sub-menu. When adding a scene asset as a
strip, the scene is always appended/duplicated.

New scenes can also be created directly from the add menu with :menuselection:`Add --> Scene --> Empty Scene`.

.. rubric:: Options

Start Frame
   The first frame to start the scene strip.
Channel
   The channel to place the strip in.
Replace Selection
   Replace the active strip with the new scene strip.

When creating a new scene you have the following options:

Type
   How the new scene is created.

   :New: Add new Strip with a new empty Scene with default settings.
   :Copy Settings: Add a new Strip, with an empty scene, and copy settings from the current scene.
   :Linked Copy: Add a Strip and link in the collections from the current scene (shallow copy).
   :Full Copy: Add a Strip and make a full copy of the current scene.


Options
=======

Scene
   A :ref:`ui-data-block` to select or create the scene to render from.

Input
   Input type to use for the Scene strip.

   :Camera:
      Use the Scene's 3D camera as input.
   :Sequencer:
      Use the scene's Sequencer timeline as input, allowing one scene to reuse
      another scene's edit (instead of taking the render output from the scene).

      This is similar to how :doc:`Meta Strips </video_editing/edit/montage/meta>` work,
      with the added advantage of supporting multiple instances of the same data.

Camera
   This can be used to override the scene's camera with any other object.

   It is useful to support switching views within a single scene.

Show
   Annotations
      Shows :doc:`Annotations </interface/annotate_tool>` while in non-render
      :ref:`Preview Shading Modes <bpy.types.RenderSettings.sequencer_gl_preview>`
      i.e. *Solid* or *Wireframe* mode.
   Transparent
      Creates a transparent background.
      This is useful for doing overlays like rendering out Grease Pencil films via the Sequencer.


Sound
-----

.. _bpy.types.SceneStrip.volume:

Strip Volume
   Volume of the audio taken from the chosen scene.


Limitations
===========

Scene strips do not render individual :doc:`Render Passes </render/layers/passes>`;
only the *Combined* render pass will be used.
