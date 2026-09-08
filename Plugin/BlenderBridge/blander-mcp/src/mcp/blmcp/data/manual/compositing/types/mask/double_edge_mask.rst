.. index:: Compositor Nodes; Double Edge Mask
.. _bpy.types.CompositorNodeDoubleEdgeMask:

*********************
Double Edge Mask Node
*********************

.. figure:: /images/node-types_CompositorNodeDoubleEdgeMask.webp
   :align: right
   :alt: Double Edge Mask Node.

The *Double Edge Mask* node creates a gradient between two masks.


Inputs
======

Outer Mask
   A mask representing the outside shape, which will fade from black at its edges
   to white at the *Inner Mask*.
Inner Mask
   A mask representing the inside shape, which will be fully white.
Images Edges
   The edges of the image that intersects the outer mask will be considered edges
   of the outer mask. Otherwise, the outer mask will be considered open-ended.

   .. list-table::

      * - .. figure:: /images/compositing_types_matte_double-edge-mask_in.png

             Disabled.

        - .. figure:: /images/compositing_types_matte_double-edge-mask_bleed.png

             Enabled.

Only Inside Outer
   Only edges of the inner mask that lie inside the outer mask will be considered.
   Otherwise, all edges of the inner mask will be considered.

   .. list-table::

      * - .. figure:: /images/compositing_types_matte_double-edge-mask_all.png

             Disabled.

        - .. figure:: /images/compositing_types_matte_double-edge-mask_adjacent.png

             Enabled.


Outputs
=======

Mask
   Standard mask output.


Example
=======

`Double Edge Mask Example Video <https://www.youtube.com/watch?v=VcjEfoNIHZs>`__
