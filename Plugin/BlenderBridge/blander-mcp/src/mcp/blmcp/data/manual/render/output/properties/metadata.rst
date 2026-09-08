
********
Metadata
********

.. figure:: /images/render_output_properties_metadata_panel.png

   Metadata panel.

The *Metadata* panel includes options for writing metadata into render output.

.. note::

   Only some image formats support metadata:
   See :doc:`image formats </files/media/image_formats>`.

Metadata Input
   Where to grab metadata from.

   :Scene: Use metadata from the current scene.
   :Sequencer Strips: Use metadata from the strips in the Sequencer.

Include
   Date
      Includes the current date and time.
   Time
      Includes the current scene time and render frame at ``HH:MM:SS.FF``.
   Render Time
      Includes the render time.
   Frame
      Includes the frame number.
   Frame Range
      Includes the start and end frame numbers.
   Memory
      Includes the peak memory usage.
   Hostname
      Includes the rendering machine's `hostname <https://en.wikipedia.org/wiki/Hostname>`__.
   Camera
      Includes the name of the active camera.
   Lens
      Includes the name of the active camera's lens value.
   Scene
      Includes the name of the active scene.
   Marker
      Includes the name of the last marker.
   Filename
      Includes the filename of the blend-file.
   Strip Name
      Includes the name of the foreground sequence strip.


Note
====

Includes a custom note.

.. hint::

   It can be useful to use the *Note* field if you are setting up a render farm.
   Since you can script any information you like into it,
   such as an identifier for the render node or the job number.
   For details on stamping arbitrary values,
   see: `this page <https://blender.stackexchange.com/questions/26643>`__.


Burn into Image
===============

Add metadata as text to the render.

Font Size
   Set the size of the text.
Text Color
   Set the color and alpha of the stamp text.
Background
   Set the color and alpha of the color behind the text.
Include Labels
   Displays the labels before the metadata text. For example,
   "Camera" in front of the camera name, etc.
