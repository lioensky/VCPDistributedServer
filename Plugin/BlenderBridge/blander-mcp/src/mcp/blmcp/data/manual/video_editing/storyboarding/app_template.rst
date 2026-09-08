
**************************
Storyboarding App Template
**************************

The *Storyboarding* app template provides a ready-to-use setup for creating storyboards
in Blender, combining 2D drawing and scene management tools in one workspace.

It is based on the *2D Animation* template, but adds a configured Video Sequence Editor (VSE)
for organizing shots using the *Sync Scene* feature.

.. figure:: /images/video_editing-storyboarding-app_template.webp

   The default Storyboarding App template.


Overview
========

This template streamlines the process of planning and sketching shots for animation or film
projects. Each shot is represented as its own scene, allowing independent Grease Pencil drawings,
camera settings, and timing, while the Sequencer serves as a master timeline to organize shots.


Features
========

- **Based on the 2D Animation Template:**
  Includes the familiar 2D drawing workspace with a *Grease Pencil* object for sketching.

- **Sequencer with Sync Scene Enabled:**
  The Sequencer editor is set to *Sync Scene*, allowing each strip in the timeline to automatically
  switch and display its corresponding scene when selected. This makes it easy to jump between
  shots during editing.

- **Preconfigured Scenes:**

  - **Edit Scene:** A master scene used in the Sequencer to assemble all shots.
  - **Shot.000 (Asset):** A pre-made *Scene Asset* that serves as a blueprint for new shots.
    Users can duplicate this asset in the Sequencer to create new shots quickly.
  - **Shot.001 and Shot.002:** Example shot scenes created from the *Shot.000* asset.


Default Settings
================

- The **Edit** scene has a default length of **10 seconds**, providing a concise overview of
  the full storyboard sequence.
- Each **shot scene** is set to **2 seconds** by default, offering a shorter duration that makes
  it easier to visualize pacing in the Sequencer.
- Frame ranges are shortened compared to typical defaults (e.g., 250 frames) to make timeline
  navigation more practical for storyboard editing.


Usage
=====

#. Open the *Storyboarding* template from the **File → New → Storyboarding** menu.
#. Use the **Edit** scene's Sequencer to organize shots.
#. Duplicate the **Shot.000** asset in the Sequencer to create new shots.
#. Draw storyboards in each shot's 2D workspace using *Grease Pencil*.
#. Adjust timing or order of scenes directly in the Sequencer to refine the flow.

This setup allows artists and directors to plan visual storytelling sequences efficiently,
with a clean link between individual drawings and the master storyboard timeline.
