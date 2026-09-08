
################
  Keying Nodes
################

These nodes give you the essential tools for creating a :term:`Matte` for images
that do not already have their own :term:`Alpha Channel`.
One usage scenario is blue-screen or green-screen footage,
where live action is shot in front of a blue or green backdrop for replacement by
a matte painting or virtual background.

In general, hook up these nodes to a viewer, set your Image Editor to show the Viewer node,
and play with the sliders in real-time using a sample image from the footage,
to get the settings right. In some cases,
small adjustments can eliminate artifacts or foreground image degradation.
Taking out too much green can result in foreground actors looking flat or bluish/purplish.

You can and should chain these nodes together,
improving your masking and color correction in successive refinements,
using each node's strengths to operate on the previous node's output.
:doc:`Keying Node </compositing/types/keying/keying>` is the closest to a "does-it-all" node
for green screens, but the best results stem from a combination of techniques.

.. note::

   Garbage Matte is not a node, but a technique selecting what to
   exclude from an image. It is a :term:`Mask` used to identify content to be
   removed from an image that cannot be removed by an automatic process like
   chroma keying. It is used either to select specific content to be removed, or
   it is the inverse of a rough selection of the subject; removing everything else.

   Some nodes accept a garbage matte directly. For those that don't, you can
   still apply one by subtracting the garbage matte from the matte generated
   by the node.

   Simple garbage mattes can be created with
   the :doc:`Box Mask </compositing/types/mask/box_mask>` or
   the :doc:`Ellipse Mask </compositing/types/mask/ellipse_mask>`.
   More complicated matte shapes using
   a :doc:`Double Edge Mask </compositing/types/mask/double_edge_mask>` or
   using a :doc:`Mask </compositing/types/input/mask>`.

.. toctree::
   :maxdepth: 1

   channel_key.rst
   chroma_key.rst
   color_key.rst
   color_spill.rst
   difference_key.rst
   distance_key.rst
   keying.rst
   keying_screen.rst
   luminance_key.rst
