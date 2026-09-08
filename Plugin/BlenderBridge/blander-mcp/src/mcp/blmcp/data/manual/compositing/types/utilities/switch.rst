.. index:: Compositor Nodes; Switch
.. _bpy.types.CompositorNodeSwitch:

***********
Switch Node
***********

.. figure:: /images/node-types_CompositorNodeSwitch.webp
   :align: right
   :alt: Switch Node.

Switch between two images using a checkbox.

.. tip::

   Switch state may be animated by adding a :doc:`keyframe </animation/keyframes/introduction>`.
   This makes the Switch node useful for bypassing nodes which are not wanted during part of a sequence.


Inputs
======

Switch
   - When it is unchecked, the first input labeled "Off" is passed to the output.
   - When checked, the second input labeled "On" is passed to the output.
Off
   First image input.
On
   Second image input.


Outputs
=======

Image
   Standard color output.
