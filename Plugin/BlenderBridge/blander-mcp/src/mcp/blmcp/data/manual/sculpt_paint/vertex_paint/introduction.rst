
************
Introduction
************

Vertex Painting is a simple way of painting color onto an object, by directly
manipulating the color of vertices, rather than textures, and is fairly straightforward.
Vertex Painting stores the color information as a
:ref:`Color Attribute <modeling-meshes-properties-object_data-color-attributes>`
which can be used by different render engines.

Color attribute's can be managed in the pallette pop-over in the middle of the header.

.. figure:: /images/sculpt-paint_vertex-paint_introduction_mode-menu.png

   Vertex Painting Mode.

When a vertex is painted, the color of the vertex is modified according to
the settings of the brush. The color of all visible planes and edges attached to
the vertex are then modified with a gradient to the color of the other connected vertices.
Note that the color of occluded faces is not modified.

.. seealso::

   :doc:`Dynamic Paint </physics/dynamic_paint/introduction>`
   can create Color Attribute information while using physics or animation.


Viewing Color Attributes
========================

Color Attributes can be used in a material node tree using the :doc:`/render/shader_nodes/input/vertex_color`.

Color Attributes can be viewed in the 3D viewport using the Workbench render engine.
To use such feature, set the 3D Viewport to :ref:`Solid Shading <3dview-shading-solid>`
and select the *Attribute* Color option.
