.. index:: Modeling Modifiers; Vertex Weight Mix Modifier
.. _bpy.types.VertexWeightMixModifier:

**************************
Vertex Weight Mix Modifier
**************************

This modifier mixes a second vertex group (or a simple value) into the affected vertex group,
using different operations.

.. important::

   This modifier does implicit clamping of weight values in the standard (0.0 to 1.0) range.
   All values below 0.0 will be set to 0.0, and all values above 1.0 will be set to 1.0.

.. note::

   You can view the modified weights in Weight Paint Mode.
   This also implies that you will have to disable the *Vertex Weight Mix* modifier
   if you want to see the original weights of the vertex group you are editing.


Options
=======

.. figure:: /images/modeling_modifiers_modify_weight-mix_panel.png
   :align: right
   :width: 300px

   The Vertex Weight Mix modifier panel.

Vertex Group A, B
   - **A**: The vertex group to affect.
   - **B**: The second vertex group to mix into the affected one.
     Leave it empty if you only want to mix in a simple value.

   Invert Weights A/B
      Invert the influence of the vertex group.

Default Weight A, B
   - **A**: The default weight to assign to all vertices not in the given vertex group.
   - **B**: The default weight to assign to all vertices not in the given second vertex group.

.. container:: lead

   .. clear

Vertex Set
   Choose which vertices will be affected.

   :All: Affects all vertices, disregarding the vertex groups content.
   :Vertex Group A: Affects only vertices belonging to the affected vertex group.
   :Vertex Group B: Affects only vertices belonging to the second vertex group.
   :Vertex Group A or B: Affects only vertices belonging to at least one of the vertex groups.
   :Vertex Group A and B: Affects only vertices belonging to both vertex groups.

   .. important::

      When using *All vertices*, *Vertices from group B* or *Vertices from one group*,
      vertices might be added to the affected vertex group.

Mix Mode
   How the vertex group weights are affected by the other vertex group's weights.

   :Replace: Replaces affected weights with the second group's weights.
   :Add: Adds the values of *Group B* to *Group A*.
   :Subtract: Subtracts the values of *Group B* from *Group A*.
   :Multiply: Multiplies the values of *Group B* with *Group A*.
   :Divide: Divides the values of *Group A* by *Group B*.
   :Difference: Subtracts the smaller of the two values from the larger.
   :Average: Adds the values together, then divides by 2.
   :Minimum: Uses the smallest weight value of VGroup A's or VGroup B's weights.
   :Maximum: Uses the largest weight value of VGroup A's or VGroup B's weights.

Normalize Weights
   Scale the weights in the vertex group to keep the relative weight
   but the lowest and highest values follow the full 0 - 1 range.


Influence
---------

Those settings are the same for the three *Vertex Weight* modifiers,
see the :ref:`Vertex Weight Edit modifier <modeling-modifiers-weight-edit-influence-mask-options>` page.


Example
=======

Here is and example of using a texture and the mapping curve to generate weights used by
the :doc:`Wave </modeling/modifiers/deform/wave>` modifier.

.. list-table:: Texture channel variations.

   * - .. figure:: /images/modeling_modifiers_modify_weight-mix_intensity.jpg
          :width: 200px

          Using intensity.

     - .. figure:: /images/modeling_modifiers_modify_weight-mix_red.jpg
          :width: 200px

          Using Red.

     - .. figure:: /images/modeling_modifiers_modify_weight-mix_saturation.jpg
          :width: 200px

          Using Saturation.

.. _fig-modifier-vertex-weight-custom:

.. list-table:: Custom mapping curve with a Vertex Weight Edit modifier.

   * - .. figure:: /images/modeling_modifiers_modify_weight-mix_map-curve.png
          :width: 200px

          A customized mapping curve.

     - .. figure:: /images/modeling_modifiers_modify_weight-mix_red.jpg
          :width: 200px

          Custom Mapping disabled.

     - .. figure:: /images/modeling_modifiers_modify_weight-mix_red-map.jpg
          :width: 200px

          Custom Mapping enabled.

.. peertube:: 40378a39-cd90-404a-89bf-64ee9a39310a

`The blend-file <https://archive.blender.org/wiki/2015/index.php/File:ManModifiersWeightVGroupEx.blend>`__,
TEST_4 scene.
