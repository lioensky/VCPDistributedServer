.. index:: Nodes; Compositing Nodes

************
Introduction
************

Compositing Nodes allow you to assemble and enhance an image (or movie). Using composition nodes,
you can glue two pieces of footage together and colorize the whole sequence all at once.
You can enhance the colors of a single image or an entire movie clip in a static manner or
in a dynamic way that changes over time (as the clip progresses). In this way,
you use composition nodes to both assemble video clips together and enhance them.

.. note:: Term: Image

   The term *Image* may refer to a single picture, a picture in
   a numbered sequence of images, or a frame of a movie clip.
   The Compositor processes one image at a time, no matter what kind of input you provide.

To process your image, you use nodes to import the image into Blender, change it,
optionally merge it with other images, and finally, save it.

.. figure:: /images/compositing_types_distort_map-uv_example-2.png

   An example of a composition.

.. figure:: /images/compositing_types_color_hue-saturation_example.jpg

   An example of color correction.


Getting Started
===============

To begin compositing, open the *Compositor* and create a new node tree
by clicking the :ref:`New <bpy.ops.node.new_compositing_node_group>` button in the header.
This adds a compositing node tree data block to the scene, which can then be reused
across different scenes or linked/appended from other blend-files.

.. important::

   To make the render engine actually use the compositing node tree (or disable compositing),
   the :ref:`Compositing Pipeline <bpy.types.RenderSettings.use_compositing>`
   option must be enabled in the output's *Post Processing* properties.

Once a node tree is created, you will see your first basic setup.
From here you can add and connect many types of
:doc:`Compositing Nodes </compositing/index>` in a node graph layout
to build effects ranging from simple color corrections to complex composites.

.. note::

   General concepts and controls for working with nodes are described in
   the :doc:`Nodes </interface/controls/nodes/index>` reference.


Examples
========

You can do just about anything with images using nodes.

Raw footage from a foreground actor in front of a blue screen,
or a rendered object doing something, can be layered on top of a background.
Composite both together, and you have composited footage.

You can change the mood of an image:

- To make an image 'feel' colder, a blue tinge is added.
- To convey a flashback or memory, the image may be softened.
- To convey hatred and frustration, add a red tinge or enhance the red.
- A startling event may be sharpened and contrast-enhanced.
- To convey a happy feeling add yellow (equal parts red and green, no blue).
- Dust and airborne dirt are often added as a cloud texture over the image to give a little more realism.


Saving your Composite Image
===========================

The *Render* button renders a single frame or image.
Save your image using :ref:`Save Image <bpy.ops.image.save>`.
The image will be saved using the image format settings on the Render panel.

To save a sequence of images, for example,
if you input a movie clip or used a Time node with each frame in its own file,
use the *Animation* button and its settings. If you might want to later overlay them,
be sure to use an image format that supports an Alpha channel (such as ``PNG``).
If you might want to later arrange them front to back or create a depth of field effect,
use a format that supports a Z-depth channel (such as ``EXR``).

To save a composition as a movie clip (all frames in a single file),
use an ``AVI`` or ``QuickTime`` format, and use the *Animation* button and its settings.
