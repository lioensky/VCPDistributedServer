.. index:: Compositor Nodes; Kuwahara
.. _bpy.types.CompositorNodeKuwahara:

*************
Kuwahara Node
*************

.. figure:: /images/node-types_CompositorNodeKuwahara.webp
   :align: right
   :alt: Kuwahara Node.

The Kuwahara node implements the Kuwahara filter as well as its anisotropic
variant. The Kuwahara filter is a smoothing filter that tries to preserve the
edges in the image. The smoothing effect of the anisotropic variant is similar
to brush strokes, so the node can be used to create stylized painting effects.


Inputs
======

Image
   Standard color input.

Size
   Controls the size of the smoothing neighborhood. Large values may introduce
   artifacts for highly detailed areas. For the anisotropic method, the larger
   the size, the slower the filter.

   .. list-table::

      * - .. figure:: /images/compositing_types_filter_kuwahara-node_original.webp

             Original.

        - .. figure:: /images/compositing_types_filter_kuwahara-node_size3.webp

             Size: 3.

      * - .. figure:: /images/compositing_types_filter_kuwahara-node_size6.webp

             Size: 6.

        - .. figure:: /images/compositing_types_filter_kuwahara-node_size9.webp

             Size: 9.

Type
   :Classic: A simple smoothing method that averages the local square
      neighborhood of the image while preserving edges. Produces blocky results
      due to the square neighborhood and provides no tuning parameters, but is
      faster to compute.
   :Anisotropic: A complex smoothing method that averages the local
      neighborhood of the image in the direction of the flow of the edges,
      thus preserving the edges in the output. Produces painterly-like results
      and provides multiple turning parameters, while being slower to compute.

Uniformity
   Controls the uniformity of the directions of the edges of the image. Non
   uniform directions are nearly never desirable, so this should typically be
   increased until the user notices the result is no longer changing in a
   significant way. Further increases would produces worst results and increase
   compute time.

Sharpness
   Controls the sharpness of the edges of the image.

   .. list-table::

      * - .. figure:: /images/compositing_types_filter_kuwahara-node_original.webp

             Original.

        - .. figure:: /images/compositing_types_filter_kuwahara-node_sharpness0.webp

             Sharpness: 0.

      * - .. figure:: /images/compositing_types_filter_kuwahara-node_sharpness05.webp

             Sharpness: 0.5.

        - .. figure:: /images/compositing_types_filter_kuwahara-node_sharpness1.webp

             Sharpness: 1.

Eccentricity
   Controls how thin and directional the filter is. Low eccentricity corresponds
   to circular omnidirectional features while high eccentricity corresponds to
   thin directional features.

   .. list-table::

      * - .. figure:: /images/compositing_types_filter_kuwahara-node_original.webp

             Original.

        - .. figure:: /images/compositing_types_filter_kuwahara-node_eccentricity0.webp

             Eccentricity: 0.

      * - .. figure:: /images/compositing_types_filter_kuwahara-node_eccentricity1.webp

             Eccentricity: 1.

        - .. figure:: /images/compositing_types_filter_kuwahara-node_eccentricity2.webp

             Eccentricity: 2.

High Precision :guilabel:`Classic`
   Uses a more precise but slower method. Use if the output contains undesirable noise.


Outputs
=======

Image
   Standard color output.


Notes
=====

Iterations
   The filter can be applied multiple times by chaining the node multiple times.
   This chaining can produce more flat filtering.

   .. list-table::

      * - .. figure:: /images/compositing_types_filter_kuwahara-node_original.webp

             Original.

        - .. figure:: /images/compositing_types_filter_kuwahara-node_iterations1.webp

             Iterations: 1.

      * - .. figure:: /images/compositing_types_filter_kuwahara-node_iterations2.webp

             Iterations: 2.

        - .. figure:: /images/compositing_types_filter_kuwahara-node_iterations3.webp

             Iterations: 3.

Performance
   The filter can be expensive to compute for high size input and high resolution
   images. To improve performance, consider scaling down the image, applying the
   filter, then scaling it up again. This can work well because the filter
   already attenuates low frequency details.
