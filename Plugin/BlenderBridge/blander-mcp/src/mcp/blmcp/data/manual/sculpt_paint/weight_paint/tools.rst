
******************
Weight Paint Tools
******************

Brush
   Tool to use for any of the weight paint :doc:`brushes <brushes>`.

Gradient
   Applies a linear/radial weight gradient;
   this is useful at times when painting gradual changes in weight becomes difficult.
   Blends the weights of selected vertices with unselected vertices.

   .. figure:: /images/sculpt-paint_weight-paint_tools_gradient.png

      Example of the Gradient tool being used with selected vertices.

   Weight
      The gradient starts at the current selected weight value, blending out to nothing.
   Strength
      Lower values can be used so the gradient mixes in with the existing weights (just like with the brush).
   Type
      The shape of the gradient.

      :Linear: Create gradient that forms a straight line.
      :Radial: Create gradient that forms a circle.

      .. note::
         These are also available via shortcuts as the :ref:`menu operators <bpy.ops.paint.weight_gradient>`.

Sample
   Weights
      Sets the brush *Weight* as the weight selected under the cursor.
      The sampled weight is displayed in the tool settings.
   Vertex Group
      Displays a list of possible vertex groups to select that are under the cursor.

:ref:`Annotate <tool-annotate-freehand>`
   Draw free-hand annotation.

   :ref:`Annotate Line <tool-annotate-line>`
      Draw straight line annotation.
   :ref:`Annotate Polygon <tool-annotate-polygon>`
      Draw a polygon annotation.
   :ref:`Annotate Eraser <tool-annotate-eraser>`
      Erase previous drawn annotations.
