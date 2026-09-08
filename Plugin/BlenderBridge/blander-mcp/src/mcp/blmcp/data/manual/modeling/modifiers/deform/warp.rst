.. index:: Modeling Modifiers; Warp Modifier
.. _bpy.types.WarpModifier:

*************
Warp Modifier
*************

The *Warp* modifier can be used to warp parts of a mesh to a new location in
a very flexible way, by using two objects to select the "from" and "to" regions.

.. figure:: /images/modeling_modifiers_deform_warp_example.png
   :align: center

   A Warp modifier applied to a grid mesh.

This modifier is a bit tricky to understand at first.
It requires two points, specified by the two target objects' origins.
The "from" point designates a point in space that is pulled toward the "to" point.
It is akin to using
the :doc:`Proportional Editing </editors/3dview/controls/proportional_editing>` in Edit Mode.


Options
=======

.. figure:: /images/modeling_modifiers_deform_warp_panel.png
   :align: right
   :width: 300px

   The Warp modifier.

Object From
   The object defining the origin transformation of the warp.

Object To
   The object defining the destination transformation of the warp.

Preserve Volume
   Enables volume preservation when rotating one of the transforms.

Strength
   Sets how strong the effect is.

Vertex Group
   The name of a vertex group which is used to control the influence of the modifier.
   If left empty, the modifier affects all vertices equally.

   :bl-icon:`arrow_leftright` Invert
      Inverts the influence of the selected vertex group, meaning that the group
      now represents vertices that will not be deformed by the modifier.

      The setting reverses the weight values of the group.


Falloff
-------

Falloff Type
   Sets the way the strength of the warp change as it goes from the center of the transform to the *Radius* value.
   See :doc:`Proportional Editing </editors/3dview/controls/proportional_editing>`
   for descriptions of the falloff types.

Radius
   Sets the distance from the transforms that can be warped by the transform handles.


Texture
-------

Texture
   You can finely control which vertices are affected by the warp,
   and to what extent, using a texture.

See :ref:`common masking options <modifiers-common-options-masking>` for a complete reference.


Usage
=====

The *Warp* modifier can be awkward to use sometimes, and its use case is rather small,
but there are a few still. For example, it can be used to have
an interactive :doc:`Proportional Editing </editors/3dview/controls/proportional_editing>`
that can be used for animations.

Another way to use this modifier is similar to
the :doc:`Deform Modifier </modeling/modifiers/deform/mesh_deform>`.
This allows you to deform parts of the mesh without having to make a vertex group.


Examples
========

.. figure:: /images/modeling_modifiers_deform_warp_example-curve-falloff.png
   :align: center

   Warp Modifier with a custom falloff curve.
