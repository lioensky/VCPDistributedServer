
*******************
Directory Structure
*******************

A video project is most likely a combination of several different assets.
You can separate them into three broad categories.

- Video files: video clips (or movies in Blender-talk), photos, graphic files (charts, logos, ...),
  and Visual Effects (VFX) such as masks, lens flares, animation.
- Audio files: recorded dialog, voice-over, music, and Sound Effects (SFX) such as environmental sounds, swooshes, ...
- Project files: the blend files and backups, (partial) render results, documentation such as scripts and storyboards.

Together they can form rapidly an intangible heap of files.
It's good practice to collect all those assets in *one* project directory with appropriate subdirectories.
Why? It will lower the probability that you accidentally delete a file
(which will result in a 'file not found' error) or that you forget
to include a necessary file when transferring the project ('file is missing' error).
And most of all, an appropriate directory structure, will help you to keep a clear overview of your assets.

.. seealso::

   Blender can incorporate some files within the Blend file (see :doc:`Packed Data </files/blend/packed_data>`).
   However, this doesn't work with video files, which can have very huge file sizes.
   So, it's better to assure that your project directory contains all necessary files.

It's also good practice to use some kind of naming convention and add metadata.
Figure 1 shows a possible example, based on our categorization of the assets above.
The directories are numbered so that they mimic a normal workflow.

.. figure:: /images/vse_setup_project_dir-structure-example.png
   :alt: Organizing your project

   Figure 1: Organizing your project.
