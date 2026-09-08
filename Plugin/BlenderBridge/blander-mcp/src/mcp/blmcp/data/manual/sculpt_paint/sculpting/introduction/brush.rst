
*********
The Brush
*********

Sculpt Mode is very recognizable by the behavior and visualization of the brush.
All the usual brush controls still apply, yet the brush for sculpting is displayed in 3D.
This means that the brush will follow the curvature of the surface
by orienting the radius to match the topology :term:`Normal`.

The inner ring of the brush cursor is used to visualize the strength of the brush.

.. figure:: /images/sculpt-paint_sculpting_introduction_brush.jpg

.. note::

    How closely the cursor follows the curvature of the mesh can be changed in
    the :doc:`Brush Settings </sculpt_paint/sculpting/tool_settings/brush_settings>` with "Normal Radius".
    This can make hard surface sculpting easier, for example with the
    :doc:`Plane </sculpt_paint/sculpting/brushes/plane>` brush.

The brush is also used for other :doc:`tools </sculpt_paint/sculpting/tools/index>` in the toolbar
to better display how that tool works. For example, the :ref:`Box Trim <tool-box-trim>`
and :ref:`Lasso Trim <tool-lasso-trim>` tools are able to use the current brush radius
for how deep geometry is trimmed or added.


Common Brushes
==============

There are many brushes to choose from but these are the most common brushes to be used during sculpting.
More information on sculpting brushes in the :doc:`Toolbar </sculpt_paint/sculpting/toolbar>`.

.. figure:: /images/sculpt-paint_sculpting_introduction_common_brushes.png
    :align: left

:doc:`Clay Strips </sculpt_paint/sculpting/brushes/clay_strips>`
    Block out broad shapes and build up volumes before refining them further.

:doc:`Grab </sculpt_paint/sculpting/brushes/grab>`
    Move geometry across the screen for general shaping.

:doc:`Smooth </sculpt_paint/sculpting/brushes/smooth>`
    Smooth and shrink surfaces to remove noise or flatten shapes.

:doc:`Draw </sculpt_paint/sculpting/brushes/draw>`
    Generic adding and subtracting on surfaces.
    This brush is often customized with different stroke methods and textures for various effects.

:doc:`Plane </sculpt_paint/sculpting/brushes/plane>`
    Scrape and fill surfaces either for hard surface sculpting or more aggressive smoothing.

:doc:`Inflate </sculpt_paint/sculpting/brushes/inflate>`
    Inflate or shrink volumes or surfaces.
    Especially useful for controlling the thickness of cylindrical shapes.

:doc:`Draw Sharp </sculpt_paint/sculpting/brushes/draw_sharp>`
    Same as *Draw* but with a much sharper falloff. Useful for adding creases, cracks and other sharp edges.

:doc:`Crease </sculpt_paint/sculpting/brushes/crease>`
    A mix of the *Draw* and *Pinch* brushes.
    Useful for creating detailed creases or sharpening existing creases for additional polish.

:doc:`Snake Hook </sculpt_paint/sculpting/brushes/snake_hook>`.
    Similar to *Grab* but this brush will dynamically let go and pick up geometry during the stroke.
    The dragged geometry is also following the angle of the stroke, making it very useful for
    pulling geometry out.
    Ideally used together with :ref:`dyntopo_introduction`.
