.. _composite-nodes-input-index:

###############
  Input Nodes
###############

Input nodes produce information from a data source.
For instance, an input can be:

- Taken directly from the active camera in a selected scene.
- A static image.
- A movie clip (such as an image sequence or video).
- A color or value.

These nodes generate the information that is passed to other nodes.
As such, they have no input sockets; only outputs.

.. toctree::
   :maxdepth: 1

   constant/index.rst

----------

.. toctree::
   :maxdepth: 1

   group_input.rst
   bokeh_image.rst
   image.rst
   image_info.rst
   image_coordinates.rst
   mask.rst
   movie_clip.rst
   sequencer_strip_info.rst

----------

.. toctree::
   :maxdepth: 1

   scene/index.rst
