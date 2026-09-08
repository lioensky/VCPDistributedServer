.. index:: Geometry Nodes; String to Curves
.. _bpy.types.GeometryNodeStringToCurves:

*********************
String to Curves Node
*********************

.. figure:: /images/node-types_GeometryNodeStringToCurves.webp
   :align: right
   :alt: String to Curves node.

The *String to Curves* node converts a string to curve instances. Each unique character used in the string
is converted to a curve once, and further uses of that character are instances of the same geometry.
The name of each instance geometry is the character it represents.

This makes processing the output geometry very efficient, because each unique character
only has to be processed once. However, it means that the result will be the same
for every instance of the same character. To process each character individually,
the :doc:`/modeling/geometry_nodes/instances/realize_instances` can be used.

.. tip::

   :doc:`Socket inspection </modeling/geometry_nodes/inspection>` can be used to see the value
   of the string input used when the node was evaluated, by holding the mouse over the socket.


Inputs
======

String
   Standard string input.

Size
   The size of each character. The values of the other inputs are scaled by this value.

Font
   Font glyph used to generate the curve.


Alignment
---------

Align X
   Controls horizontal alignment of text on each line.

   :Left: Aligns the text to the left.
   :Center: Aligns the text to the center.
   :Right: Aligns the text to the right.
   :Justify: Aligns the text to the left and right.
   :Flush: Aligns the text to the left and right with equal character spacing.

Align Y
   Controls vertical alignment of the block of text.

   :Top: Aligns the text to the top.
   :Top Baseline: Aligns the text to the top baseline.
   :Middle: Aligns the text to the middle.
   :Bottom Baseline: Aligns the text to the bottom baseline.
   :Bottom: Aligns the text to the bottom.

Pivot Point
   Controls where on each character the output *Pivot Point* is placed.

   :Midpoint: Place the pivot points at the center of each character's bounds.
   :Top Left: Place the pivot points at the top left of each character's bounds.
   :Top Center: Place the pivot points at the middle of the top of each character's bounds.
   :Top Right: Place the pivot points at the top right of each character's bounds.
   :Bottom Left: Place the pivot points at the bottom left of each character's bounds.
   :Bottom Center: Place the pivot points at the middle of bottom of each character's bounds.
   :Bottom Right: Place the pivot points at the bottom right of each character's bounds.


Spacing
-------


Character Spacing
   A factor by which the space between each character (kerning) is scaled on the X axis.

Word Spacing
   A factor by which whitespace between words is scaled on the X axis.

Line Spacing
   The distance between separate lines in the output. Scaled by the *Size* input.


Text Box
--------

Overflow
   Controls how the text fits inside the text box.

   :Overflow:
      Wraps the text at the *Text Box Width*.
   :Scale To Fit:
      Scales the text size to fit the *Text Box Width* and *Text Box Height*.
   :Truncate:
      Only outputs text characters that fit within the width and height, based on the *Size* input.
      Any part of the string that did not fit is moved to the *Remainder* output.

Text Box Width
   The maximum width of each line, though individual words will not be wrapped.

Text Box Height
   The maximum height for all the lines of the text.


Outputs
=======

Curve Instances
   Geometry output containing one instance per character.

Remainder
   The part of the text that did not fit in the box described by the *Text Box Height* and
   *Text Box Width* inputs. Only used in the *Truncate* overflow mode.

Line
   An attribute field containing the line index of each character
   (on the :ref:`instance domain <attribute-domains>`).

Pivot Point
   Outputs the position described by the *Pivot Point* drop-down in the local space of each instance.


Examples
========

.. figure:: /images/modeling_geometry-nodes_text_string-to-curves_example.png
   :align: center

The node can be used to make overflowing text boxes. Here, the text that does not fit into
the first node's fixed-size text box is passed to a separate *String to Curves* node,
then scaled with a *Scale to Fit* node.
