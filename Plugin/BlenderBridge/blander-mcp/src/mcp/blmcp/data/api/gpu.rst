GPU Module (gpu)
================

.. module:: gpu

This module provides Python wrappers for the GPU implementation in Blender.
Some higher level functions can be found in the :mod:`gpu_extras` module.

.. toctree::
   :maxdepth: 1
   :caption: Submodules

   gpu.types.rst
   gpu.matrix.rst
   gpu.select.rst
   gpu.shader.rst
   gpu.state.rst
   gpu.texture.rst
   gpu.platform.rst
   gpu.capabilities.rst


Geometry Batches
++++++++++++++++

Geometry is drawn in batches.
A batch contains the necessary data to perform the drawing.
That includes an obligatory *Vertex Buffer* and an optional *Index Buffer*,
each of which is described in more detail in the following sections.
A batch also defines a draw type.
Typical draw types are ``POINTS``, ``LINES`` and ``TRIS``.
The draw type determines how the data will be interpreted and drawn.

Vertex Buffers
++++++++++++++

A *Vertex Buffer Object* (VBO) (:class:`gpu.types.GPUVertBuf`)
is an array that contains the vertex attributes needed for drawing using a specific shader.
Typical vertex attributes are *location*, *normal*, *color*, and *uv*.
Every vertex buffer has a *Vertex Format* (:class:`gpu.types.GPUVertFormat`)
and a length corresponding to the number of vertices in the buffer.
A vertex format describes the attributes stored per vertex and their types.

The following code demonstrates the creation of a vertex buffer that contains 6 vertices.
For each vertex 2 attributes will be stored: The position and the normal.

.. code-block:: python

   import gpu
   vertex_positions = [(0, 0, 0), ...]
   vertex_normals = [(0, 0, 1), ...]

   fmt = gpu.types.GPUVertFormat()
   fmt.attr_add(id="pos", comp_type='F32', len=3, fetch_mode='FLOAT')
   fmt.attr_add(id="normal", comp_type='F32', len=3, fetch_mode='FLOAT')

   vbo = gpu.types.GPUVertBuf(len=6, format=fmt)
   vbo.attr_fill(id="pos", data=vertex_positions)
   vbo.attr_fill(id="normal", data=vertex_normals)

This vertex buffer could be used to draw 6 points, 3 separate lines, 5 consecutive lines, 2 separate triangles, ...
E.g. in the case of lines, each two consecutive vertices define a line.
The type that will actually be drawn is determined when the batch is created later.

Index Buffers
+++++++++++++

Often triangles and lines share one or more vertices.
With only a vertex buffer one would have to store all attributes for the these vertices multiple times.
This is very inefficient because in a connected triangle mesh every vertex is used 6 times on average.
A more efficient approach would be to use an *Index Buffer* (IBO) (:class:`gpu.types.GPUIndexBuf`),
sometimes referred to as *Element Buffer*.
An *Index Buffer* is an array that references vertices based on their index in the vertex buffer.

For instance, to draw a rectangle composed of two triangles, one could use an index buffer.

.. code-block:: python

   positions = (
       (-1,  1), (1,  1),
       (-1, -1), (1, -1))

   indices = ((0, 1, 2), (2, 1, 3))

   ibo = gpu.types.GPUIndexBuf(type='TRIS', seq=indices)

Here the first tuple in ``indices`` describes which vertices should be used for the first triangle
(same for the second tuple).
Note how the diagonal vertices 1 and 2 are shared between both triangles.

Shaders
+++++++

A shader is a program that runs on the GPU (written in GLSL in our case).
There are multiple types of shaders.
The most important ones are *Vertex Shaders* and *Fragment Shaders*.
Typically multiple shaders are linked together into a *Program*.
However, in the Blender Python API the term *Shader* refers to an OpenGL Program.
Every :class:`gpu.types.GPUShader` consists of a vertex shader, a fragment shader and an optional geometry shader.
For common drawing tasks there are some built-in shaders accessible from :class:`gpu.shader.from_builtin`
with an identifier such as ``UNIFORM_COLOR`` or ``FLAT_COLOR``. There are specific builtin shaders for
drawing triangles, lines and points.

Every shader defines a set of attributes and uniforms that have to be set in order to use the shader.
Attributes are properties that are set using a vertex buffer and can be different for individual vertices.
Uniforms are properties that are constant per draw call.
They can be set using the ``shader.uniform_*`` functions after the shader has been bound.

.. note::

   It is important to note that GLSL sources are reinterpreted to MSL (Metal Shading Language)
   on Apple operating systems.
   This uses a small compatibility layer that does not cover the whole GLSL language specification.
   Here is a list of differences to keep in mind when targeting compatibility with Apple platforms:

   - The only matrix constructors available are:

      - diagonal scalar (example: ``mat2(1)``)
      - all scalars (example: ``mat2(1, 0, 0, 1)``)
      - column vector (example: ``mat2(vec2(1,0), vec2(0,1))``)
      - reshape constructors work only for square matrices (example: ``mat3(mat4(1))``)

   - ``vertex``, ``fragment`` and ``kernel`` are reserved keywords.
   - all types and keywords defined by the
     `MSL specification <https://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf>`__
     are reserved keywords and should not be used.


Batch Creation
++++++++++++++

Batches can be created by first manually creating VBOs and IBOs.
However, it is recommended to use the :class:`gpu_extras.batch.batch_for_shader` function.
It makes sure that all the vertex attributes necessary for a specific shader are provided.
Consequently, the shader has to be passed to the function as well.
When using this function one rarely has to care about the vertex format, VBOs and IBOs created in the background.
This is still something one should know when drawing stuff though.

Since batches can be drawn multiple times, they should be cached and reused whenever possible.

Offscreen Rendering
+++++++++++++++++++

What one can see on the screen after rendering is called the *Front Buffer*.
When draw calls are issued, batches are drawn on a *Back Buffer* that will only be displayed
when all drawing is done and the current back buffer will become the new front buffer.
Sometimes, one might want to draw the batches into a distinct buffer that could be used as
texture to display on another object or to be saved as image on disk.
This is called Offscreen Rendering.
In Blender Offscreen Rendering is done using the :class:`gpu.types.GPUOffScreen` type.

.. warning::

   :class:`gpu.types.GPUOffScreen` objects are bound to the OpenGL context they have been created in.
   This means that once Blender discards this context (i.e. the window is closed),
   the offscreen instance will be freed.

Examples
++++++++

To try these examples, just copy them into Blender's text editor and execute them.
To keep the examples relatively small, they just register a draw function that can't easily be removed anymore.
Blender has to be restarted in order to delete the draw handlers.

3D Points with Single Color

.. literalinclude:: ./examples/gpu.1.py
   :lines: 147-


Triangle with Custom Shader
---------------------------

.. literalinclude:: ./examples/gpu.2.py
   :lines: 5-


Wireframe Cube using Index Buffer
---------------------------------

.. literalinclude:: ./examples/gpu.3.py
   :lines: 5-


Mesh with Random Vertex Colors
------------------------------

.. literalinclude:: ./examples/gpu.4.py
   :lines: 5-


2D Rectangle
------------

.. literalinclude:: ./examples/gpu.5.py
   :lines: 5-


2D Image
--------

To use this example you have to provide an image that should be displayed.

.. literalinclude:: ./examples/gpu.6.py
   :lines: 7-


Generate a texture using Offscreen Rendering
--------------------------------------------

#. Create an :class:`gpu.types.GPUOffScreen` object.
#. Draw some circles into it.
#. Make a new shader for drawing a planar texture in 3D.
#. Draw the generated texture using the new shader.

.. literalinclude:: ./examples/gpu.7.py
   :lines: 10-


Copy Off-screen Rendering result back to RAM
--------------------------------------------

This will create a new image with the given name.
If it already exists, it will override the existing one.

Currently almost all of the execution time is spent in the last line.
In the future this will hopefully be solved by implementing the Python buffer protocol
for :class:`gpu.types.Buffer` and :class:`bpy.types.Image.pixels` (aka ``bpy_prop_array``).

.. literalinclude:: ./examples/gpu.8.py
   :lines: 12-


Rendering the 3D View into a Texture
------------------------------------

The scene has to have a camera for this example to work.
You could also make this independent of a specific camera,
but Blender does not expose good functions to create view and projection matrices yet.

.. literalinclude:: ./examples/gpu.9.py
   :lines: 9-


Custom Shader for dotted 3D Line
--------------------------------

In this example the arc length (distance to the first point on the line) is calculated in every vertex.
Between the vertex and fragment shader that value is automatically interpolated
for all points that will be visible on the screen.
In the fragment shader the ``sin`` of the arc length is calculated.
Based on the result a decision is made on whether the fragment should be drawn or not.

.. literalinclude:: ./examples/gpu.10.py
   :lines: 11-


Custom compute shader (using image store) and vertex/fragment shader
--------------------------------------------------------------------

This is an example of how to use a custom compute shader
to write to a texture and then use that texture in a vertex/fragment shader.
The expected result is a 2x2 plane (size of the default cube),
which changes color from a green-black gradient to a green-red gradient,
based on current time.

.. literalinclude:: ./examples/gpu.11.py
   :lines: 11-

