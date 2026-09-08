.. index:: Compositor Nodes; Time Curve
.. _bpy.types.CompositorNodeTime:

.. --- copy below this line ---

***************
Time Curve Node
***************

.. figure:: /images/node-types_CompositorNodeTime.webp
   :align: right
   :alt: Time Curve Node.

The *Time Curve node* generates a factor value (from 0.0 to 1.0)
between the scene start and end time, using a curve mapping.


Inputs
======

Start/End Frame
   Start frame and End frame of the range of time specifying the values
   the output should last. This range becomes the X axis of the graph.
   The time input could be reversed by specifying a start frame greater than the end frame.


Properties
==========

Curve
   The Y value defined by the curve is the factor output.
   For the curve controls, see :ref:`Curve widget <ui-curve-widget>`.

   .. tip::

      Flipping the curve around reverses the time input, but
      doing so is easily overlooked in the node setup.


Outputs
=======

Factor
   The Y value of the curve at the current frame.

.. hint::

   The :doc:`/compositing/types/utilities/math/map_range`
   can be used to map the output to a more appropriate value.
   With some curves, it is possible that the Time Curve node
   may output a number larger than one or less than zero.
   To be safe, use the Min/Max clamping function of the Map Value node to limit output.


Example
=======

.. figure:: /images/compositing_types_input_time_curve_example.png

   Time controls from left to right: no effect, slow down, freeze, accelerate, reverse.
