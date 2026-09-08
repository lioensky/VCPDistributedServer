************
Introduction
************

Vertex Groups can potentially have a very large number of associated vertices
and thus a large number of weights (one weight per assigned vertex).
*Weight Painting* is a method to maintain large amounts of weight information
in a very intuitive way.

It is primarily used for rigging meshes, where the vertex groups are used to
define the relative bone influences on the mesh. But we use it also for
controlling particle emission, hair density, many modifiers, shape keys, etc.

.. figure:: /images/sculpt-paint_weight-paint_introduction_example.jpg

   Vertex group in Weight Paint Mode.

You can enter Weight Paint Mode from the Mode selector :kbd:`Ctrl-Tab`.
The selected mesh object is displayed slightly shaded with a rainbow color spectrum.
The color visualizes the weights associated to each vertex in the active vertex group.
By default *blue* means unweighted and *red* means fully weighted.

You can assign weights to the vertices of the object by painting on it with weight brushes.
Starting to paint on a mesh automatically adds weights to the active vertex group
(a new vertex group is created if needed).

Vertex Groups can be managed in the pallette pop-over in the middle of the header.


The Weighting Color Code
========================

Weights are visualized by a gradient using a cold/hot color system,
such that areas of low value (with weights close to 0.0) are displayed as blue (cold)
and areas of high value (with weights close to 1.0) are displayed as red (hot).
And all in-between values are displayed as rainbow colors (blue, green, yellow, orange, red).

.. figure:: /images/sculpt-paint_weight-paint_introduction_color-code.png

   The color spectrum and their respective weights.

In addition to the above described color code, Blender has a special visual notation
(as an option) for unreferenced vertices: They are displayed as black.
Thus you can see the referenced areas (displayed as cold/hot colors) and
the unreferenced areas (in black) at the same time.
This is most useful when you look for weighting errors.
See :ref:`Viewport Overlays <3dview-overlay-weight-paint>`.

.. figure:: /images/sculpt-paint_weight-paint_introduction_color-code-black.png

   Unreferenced vertices example.

.. note::

   You can customize the colors in the weight gradient by enabling
   :ref:`Custom Weight Paint Range <bpy.types.PreferencesView.use_weight_color_range>` in the *Editing* tab
   of the *Preferences*.


Normalized Weight Workflow
==========================

In order to be used for things like deformation, weights usually have to be normalized,
so that all deforming weights assigned to a single vertex add up to 1.
The *Armature* modifier in Blender does this automatically, so it is technically not necessary to
ensure that weights are normalized at the painting stage.

However, while more complicated, working with normalized weights has certain advantages,
because it allows use of certain tools designed for them, and because when weights are normalized,
understanding the final influence of the current group does not require knowing weights in
other groups on the same vertex.

These tools are provided to aid working with normalized weights:

Normalize All
   In order to start working with normalized weights it is first necessary to normalize the existing weights.
   The :ref:`Normalize All <bpy.ops.object.vertex_group_normalize_all>` tool can be used for that.
   Make sure to select the right mode and disable *Lock Active*.

Auto Normalize
   Once the weights are initially normalized,
   the :ref:`Auto Normalize <bpy.types.ToolSettings.use_auto_normalize>` option
   can be enabled to automatically maintain normalization as you paint.
   This also tells certain tools that the weights are supposed to be already normalized.

Vertex group locking
   Any vertex group can be locked to prevent changes to it. This can be done via
   the lock icon in the vertex group list, or using bone selection and
   the :ref:`locks pie menu <bpy.ops.object.vertex_group_lock>`.

   This setting prevents accidental edits to groups. However,
   since it is also respected by *Auto Normalize*, in the normalized weight workflow
   it has a more significant meaning of locking the current influence of chosen bones,
   so that when you paint other bones, the weight is redistributed only between the unlocked groups.

   In locations affected by multiple bones, this allows more precise tweaking and re-balancing of
   weights by temporarily focusing on a subset of bones. This can also be aided by
   the :ref:`Lock Relative <bpy.types.ToolSettings.use_auto_normalize>` option, which displays unlocked groups as
   though re-normalized with the locked groups deleted, thus making it appear as if the locked groups did not even
   exist.

Multi-Paint
   Finally, the :ref:`Multi-Paint <bpy.types.ToolSettings.use_auto_normalize>` option allows treating
   multiple selected bones as if they were one bone, so that the painting operations change
   the combined weight, preserving the ratio within the group. Combined with locking,
   this allows balancing between one set of bones versus the rest, excluding a third set
   that has its influence not affected in any way due to locks.

   Technically, this option does not require the normalized workflow, but since non-normalized
   weights can add to more than 1, the weight display behaves best with *Auto Normalize* enabled.

.. tip::

   For example, when dealing with a bone loop, e.g. mouth or an eye, selecting the loop with
   *Multi-Paint* exposes the falloff between the loop as a whole and surrounding bones,
   while locking the surrounding bones and using *Lock Relative* displays the falloff between bones
   within the loop. Thus the complex two-dimensional falloff of each bone can be viewed and
   edited as two independent one-dimensional gradients.
