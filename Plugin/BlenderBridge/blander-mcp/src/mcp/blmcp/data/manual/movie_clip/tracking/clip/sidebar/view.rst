
****
View
****

Annotations
===========

Annotation tool strokes can be enabled/disabled with the checkbox in the panel header.
It is a standard annotations panel where annotation layers and frames can be controlled.
There is one difference in the behavior of the annotation tools from other areas --
when a new layer is created "on-demand" (when making a stroke without adding a layer before this)
the default color for the layer is set to pink. This heightens the color contrast to make
the stroke more noticeable on all kinds of movies.

.. _bpy.types.SpaceClipEditor.annotation_source:

Data Source
   Determines the data-block type the current annotation layer is stored.

   :Clip: Store the current annotation layer with the active *Movie Clip* data-block.
   :Track: Store the current annotation layer with the active *Track* data-block.

.. seealso::

   :ref:`tool-annotate` for more information on general annotation layers.
