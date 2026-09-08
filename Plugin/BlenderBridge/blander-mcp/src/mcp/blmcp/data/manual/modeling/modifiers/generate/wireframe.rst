.. index:: Modeling Modifiers; Wireframe Modifier
.. _bpy.types.WireframeModifier:

******************
Wireframe Modifier
******************

The *Wireframe* modifier transforms a mesh into a wireframe by iterating over its
faces, collecting all edges and turning those edges into four-sided polygons.
Be aware of the fact that your mesh needs to have faces to be wireframed.
You can define the thickness, the material and several other parameters of the generated
wireframe dynamically via the given modifier options.


Options
=======

.. figure:: /images/modeling_modifiers_generate_wireframe_panel.png
   :align: right
   :width: 300px

   The Wireframe modifier.

Thickness
   The depth or size of the wireframes.

Offset
   A value between (-1 to 1) to change whether the wireframes are
   generated inside or outside of the original mesh.
   Set to zero, *Offset* will center the wireframes around the original edges.

Boundary
   Creates wireframes on mesh island boundaries.
Replace Original
   If this option is enabled, the original mesh is replaced by the generated wireframe.
   If not, the wireframe is generated on top of it.

Thickness
   Even
      Maintain thickness by adjusting for sharp corners.
      Sometimes improves quality but also increases computation time.
   Relative
      Determines the edge thickness by the length of the edge. Longer edges will be thicker.

Crease Edges
   This option is intended for usage with
   the :doc:`Subdivision </modeling/modifiers/generate/subdivision_surface>` modifier.
   Enable this option to crease edges on their junctions and prevent large curved intersections.

   Crease Weight
      Define how much crease (0 to 1, nothing to full) the junctions should receive.

Material Offset
   Uses the chosen material index as the material for the wireframe;
   this is applied as an offset from the first material.

.. warning::

   Wireframe thickness is an approximation. While *Even Thickness* should yield good results in many cases,
   skinny faces can cause ugly spikes. In this case you can either reduce the extreme angles in the geometry
   or disable the *Even Thickness* option.


Vertex Group
------------

The weights of the selected vertex group are multiplied onto the *Thickness*,
so vertices with lower weights will be less thick. The vertices which are not part
of the vertex group will be used as if their weight was zero.

Invert
   Reverses the vertex group weights, so that the used weight is one minus the actual weight.
Factor
   How much the vertex weights are taken into account.

   - On 0.0 , vertices with zero weight will have no thickness at all.
   - On 0.5 , vertices with zero weight will be half as thick as those with full weight.
   - On 1.0 , the weights are ignored and the *Thickness* value is used for every vertex.

.. note::

   If the final thickness of a vertex is zero, it will still generate a wireframe.
   Therefore creating duplicate geometry, which sometimes needs extra care.


Examples
========

.. figure:: /images/modeling_modifiers_generate_wireframe_result.jpg
   :width: 420px

   Wireframes on a displaced plane.

In this example, the wireframes carry a second (dark) material while the displaced plane uses its original one.

.. figure:: /images/modeling_modifiers_generate_wireframe_example-weights.png
   :width: 420px

   Vertex group weighting.

The weights of the vertex group gradually change from 0 to 1.

.. figure:: /images/modeling_modifiers_generate_wireframe_example-crease.png
   :width: 420px

   Wireframe and Subdivision Surface modifier.

Cube with enabled *Crease Edges* option. The *Crease Weight* is set to 0, 0.5 and 1.
