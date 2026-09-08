
*******
Texture
*******

Assigns a texture to the Freestyle stroke.

.. figure:: /images/render_freestyle_parameter-editor_line-style_texture_tab.png
   :align: center
   :width: 50%

   Line Style: Texture.

.. _bpy.types.FreestyleLineStyle.use_nodes:

Use Nodes
   In Cycles textures are defined by means of shader `Nodes`_.

.. _bpy.types.FreestyleLineStyle.texture_spacing:

Spacing Along Stroke
   Allows to set the "pace" of textures mapped along the length of strokes.

Go to Linestyle Textures
   A shortcut to the line style texture properties in the other *Textures* tab of the Properties.
   Make sure to first enable *Use Nodes*.


Nodes
=====

UV Along Stroke Node
--------------------

.. figure:: /images/node-types_ShaderNodeUVAlongStroke.webp
   :align: right

   UV Along Stroke Node.

The *UV Along Stroke* input node is maps textures along the stroke length,
making it possible to mimic pencil, paintbrush, and other art medium marks.

.. note::

   These UV maps become available only during the Freestyle rendering process.
   Hence, the UV Along Stroke node cannot be replaced by the conventional UV Map input node
   which takes an existing UV map already defined as part of mesh data.


Inputs
^^^^^^

This node has no inputs.


Properties
^^^^^^^^^^

Use Tips
   Allows to use lower quarters of a texture image for the head and tail tips of a stroke,
   while the upper half for the stroke body.


Outputs
^^^^^^^

UV
   UV maps defined along strokes.


Line Style Output Node
----------------------

.. figure:: /images/node-types_ShaderNodeOutputLineStyle.webp
   :align: right

   Line Style Output Node.

The *Line Style Output* node specifies how to mix the texture information
into the base color of line styles.


Inputs
^^^^^^

Color
   Color input for the texture.
Color Factor
   Standard mix factor of the *Color* value.
Alpha
   Alpha input for the texture.
Alpha Factor
   Standard mix factor of the *Alpha* value.


Properties
^^^^^^^^^^

Mix
   The Blend mode can be selected in the select menu.
   See :term:`Color Blend Modes` for details on each blending mode.
Clamp
   Limit the highest color value to not exceed 1.0.


Outputs
^^^^^^^

This node has no outputs.


Example
=======

The image below shows a typical shader node tree that maps a floral texture image along strokes.
The UV Along Stroke input node retrieves UV maps defined by Freestyle along generated strokes, and
passes them to the Vector input channel of the Image Texture node.
A texture image is selected in the Image Texture node,
and its color is inputted to the Alpha channel of the Line Style Output node.
Since the Alpha Factor is set to one, the texture image replaces the base alpha transparency of the active line style
(shown in the Freestyle Line Style panel).
On the other hand, the Mix blend mode is selected in the Line Style Output node with the Color Factor set to zero,
so that the gradient line color specified in the active line style is applied along strokes.

.. figure:: /images/render_freestyle_parameter-editor_line-style_texture_uv-along-stroke-example.png

   Example of Line Style Nodes
   (`blend-file
   <https://archive.blender.org/wiki/2015/index.php/File:Blender_272_textured_strokes_in_cycles.blend>`__).

It is noted that the texture image ``FS_floral_brush.png``
shown in the screen capture is an example of Freestyle brush images with tips.
Specifically, the upper half of the image is used as a seamless horizontal tile of the stroke body.
Whereas the parts in the lower half are tips (stroke caps) at both ends of the stroke.
