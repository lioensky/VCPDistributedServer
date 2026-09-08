
************
Introduction
************

Drivers are a way to control values of properties by means of a function,
or a mathematical expression.

Effectively, drivers consist of:

- A **driver configuration** that specifies zero, one, or more input values using
  other properties or object transformation channels, and combines them using
  a predefined mathematical function or a custom Python expression.
- An **animation** :doc:`F-Curve </editors/graph_editor/fcurves/introduction>`
  that maps the output of the driver configuration to the final value to apply
  to the driven property.

As an example, the rotation of Object 1 can be controlled by the scale of Object 2.
It is then said that the scale of Object 2 *drives* the rotation of Object 1.

Not only can drivers directly set the value of a property to the value of a different one,
they can also combine multiple values using a fixed function or a Python expression
and further modulate it with a manually defined curve and/or a modifier stack.

Drivers are an extremely powerful tool for building rigs and are typically used
to drive bone transforms and the influence of shape keys, action constraints and
modifiers, often using custom properties as inputs.


Graph View
==========

.. figure:: /images/animation_drivers_introduction_fcurve.png
   :align: right

   Driver curve in the Drivers editor.

The main area of the :doc:`Drivers editor </editors/drivers_editor>`
shows an :doc:`F-Curve </editors/graph_editor/fcurves/introduction>` that
represents the driver function.

The **X axis** maps to the output value of the driver configuration. The units depend on the setup.

The **Y axis** shows the value applied to the target property. The units depend on the property.

In the example image, if the driver value is 2.0 the property value will be 0.5.

The default F-Curve is an identity map, i.e. the value produced by the driver configuration
is applied to the driven property unchanged. If the driver output value is 2.0,
the property will be 2.0.

The driver function can be defined artistically with Bézier curve handles or
mathematically with trigonometric functions or polynomial expressions such as :math:`y = a + bx`.
Furthermore, the function can also be procedurally modulated with noise or cyclic repetitions.
See :doc:`Modifiers </editors/graph_editor/fcurves/modifiers>` for more details.


Driver Configuration
====================

The :doc:`Drivers panel </animation/drivers/drivers_panel>` shows the setup for a driver.

A driver can have zero, one, or more **variables**. Variables specify which properties,
object transformation channels, or relative distances between objects, are used as inputs
by the driver.

The driver **type** determines how the variables are used. The type can be:

- a built-in function: for example, the sum of the variables' values, or
- a scripted expression: an arbitrary Python expression that refers to the variables by their names.

This driver configuration outputs a single value which changes when the variables change.
This value is then evaluated through the driver function curve to produce the result
to be applied to the driven property.


Notes on Scripted Expressions
=============================

When a driver uses a *Scripted Expression*, Blender can evaluate it without using
the fully featured Python interpreter if it is simple enough.
This means that drivers are fast to evaluate with simple divisions, additions and other "simple" expressions.
The built-in functions are always evaluated natively.

See :ref:`Simple Expressions <drivers-simple-expressions>`
for a comprehensive list of expressions that can be evaluated natively.

When the expression is not simple, it will be evaluated using Python.
As a consequence, the driver will be slower and there is a security risk
if the author of the Python code is unknown.
This is an important thing to take into consideration for heavy scenes and
when sharing files with other people.
See also: :doc:`Auto run </advanced/scripting/security>`.
