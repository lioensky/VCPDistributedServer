.. index:: Compositor Nodes; Sequencer Strip Info
.. _bpy.types.CompositorNodeSequencerStripInfo:

*************************
Sequencer Strip Info Node
*************************

.. figure:: /images/node-types_CompositorNodeSequencerStripInfo.webp
   :align: right
   :alt: Sequencer Strip Info node.

Returns information about the Video Sequencer strip to which the
:ref:`Compositor modifier <bpy.types.SequencerCompositorModifierData>`
is applied. This includes timing and transform data such as frame range, position,
rotation, and scale.


.. note::

   This node is only supported when the Compositor is evaluated in the context of the
   Video Sequencer (for example, when using a *Compositor* modifier on a strip).
   When evaluated outside of the Sequencer context, the node outputs default values.


Inputs
======

This node has no input sockets.


Outputs
=======

Start Frame
   The start frame of the strip in the Sequencer timeline.

End Frame
   The end frame of the strip in the Sequencer timeline.

Location
   The strip's 2D position offset in the Sequencer, corresponding to its transform location.

Rotation
   The rotation of the strip, as defined by the strip's transform settings.

Scale
   The scale of the strip in the X and Y directions, as defined by the strip's transform settings.
