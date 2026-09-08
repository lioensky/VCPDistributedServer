
*******
Strokes
*******

Strokes are the final rendered lines. Yet you can tweak them, for example,
by removing the ones longer/shorter than some threshold,
chaining lines into a single stroke or breaking a stroke into several ones based on angles,
dashed pattern, etc.

.. figure:: /images/render_freestyle_parameter-editor_line-style_strokes_tab.png
   :align: center
   :width: 50%

   Line Style: Strokes.

.. _bpy.types.FreestyleLineStyle.caps:

Caps
   You can choose between three types of line caps:

   :Butt:
      Flat cap, exactly at the point the line ends.
   :Round:
      A half circle centered on the end point of the line.
   :Square:
      A square centered on the end point of the line
      (hence, like the circle, the drawn end of the line is slightly extended compared to its computed value).

   .. figure:: /images/render_freestyle_parameter-editor_line-style_strokes_caps-example.png
      :align: center

      Line caps example.


.. _bpy.types.FreestyleLineStyle.use_chaining:

Chaining
========

By default all retrieved lines from the line set are chained together.
There are two basic chaining methods:

.. _bpy.types.FreestyleLineStyle.chaining:

Method
   :Plain:
      The default chaining method; it creates simple chains.
   :Sketchy:
      This chaining option allows for generating chains of feature edges with sketchy multiple strokes.
      Basically, it generates *Round* strokes instead of a single one.
      It is only really useful if you use some random-driven modifiers in the line style!

      .. _bpy.types.FreestyleLineStyle.rounds:

      Rounds
         It specifies the number of rounds in sketchy strokes.

.. _bpy.types.FreestyleLineStyle.use_same_object:

Same Object
   If true, only feature edges of the same object are joined.

Chaining can also be turned off to render each line separately,
which can be useful for line styles which depend on accurate representation of the line set.


Splitting
=========

You can split up chains of Freestyle lines by enabling one of the following:

.. _bpy.types.FreestyleLineStyle.use_angle_min:
.. _bpy.types.FreestyleLineStyle.use_angle_max:
.. _bpy.types.FreestyleLineStyle.angle_min:
.. _bpy.types.FreestyleLineStyle.angle_max:

Min/Max 2D Angle
   Splits chains of feature edges when they make a 2D angle above (or below) a minimum (or maximum) threshold.

.. _bpy.types.FreestyleLineStyle.use_split_length:
.. _bpy.types.FreestyleLineStyle.split_length:

2D Length
   Splits chains when they are longer than the given value.

.. _bpy.types.FreestyleLineStyle.material_boundary:

Material Boundary
   Splits chains of feature edges if they cross from one material to another.


.. _bpy.types.FreestyleLineStyle.use_split_pattern:

Split Pattern
-------------

Splits the chains using the given dashed pattern (see also `Dashed Line`_).

.. _bpy.types.FreestyleLineStyle.split_dash:

Dash 1, 2, 3
   Length of the specified dash for splitting.

.. _bpy.types.FreestyleLineStyle.split_gap:

Gap 1, 2, 3
   Length of the specified gap for splitting.


.. _bpy.types.FreestyleLineStyle.use_sorting:

Sorting
=======

You can sort the order of your strokes, allowing the lines to stack in the order given.

.. _bpy.types.FreestyleLineStyle.sort_key:

Sort Key
   A sort key is used to determine the stacking order of lines.

   :Distance from Camera:
      Lines closer to the camera lie on top of further lines.
   :2D Length:
      Longer lines lie on top of shorter lines.
   :Projected X/Y:
      Sort by the projected X or Y value in the image coordinate system.

.. _bpy.types.FreestyleLineStyle.integration_type:

Integration Type
   Use in tandem with the Sort Key to determine the range for sorting.
   Since the distance of a line from the camera may vary over vertices,
   this option computes the sort key for a line from the values computed at
   individual vertices. The value computed for the line is:

   :Mean: The mean of the values obtained for the vertices.
   :Min: The minimum of the values obtained for the vertices.
   :Max: The maximum of the values obtained for the vertices.
   :First: The value obtained for the first vertex.
   :Last: The value obtained for the last vertex.

.. _bpy.types.FreestyleLineStyle.sort_order:

Sort Order
   With the given result you can choose to "Reverse" the sort order.


Selection
=========

You can also choose to only render selected chains.

.. _bpy.types.FreestyleLineStyle.use_length_min:
.. _bpy.types.FreestyleLineStyle.use_length_max:
.. _bpy.types.FreestyleLineStyle.length_min:
.. _bpy.types.FreestyleLineStyle.length_max:

Min/Max 2D Length
   Chains longer and/or shorter than *2D Length*.

.. _bpy.types.FreestyleLineStyle.use_chain_count:
.. _bpy.types.FreestyleLineStyle.chain_count:

Chain Count
   Allows the selection of first N chains.


.. _bpy.types.FreestyleLineStyle.use_dashed_line:

Dashed Line
===========

By enabling the *Dashed Line* checkbox,
you can specify three pairs of dash and gap lengths.
Dash values define the lengths of dash strokes,
while gap values specify intervals between two dashes.

If a zero gap is specified,
then the corresponding dash is ignored even if it has a nonzero value.

Dashes are treated as separate strokes, meaning that you can apply line caps,
as well as color, alpha and thickness modifiers.

.. _bpy.types.FreestyleLineStyle.dash:

Dash 1, 2, 3
   Length of the specified dash for dashed lines.

.. _bpy.types.FreestyleLineStyle.gap:

Gap 1, 2, 3
   Length of the specified gap for dashed lines.
