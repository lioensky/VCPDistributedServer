.. _bpy.types.NodeSocket:
.. _bpy.types.NodeTree:

**********
Node Parts
**********

All nodes in Blender are based on a similar construction.
This applies to :ref:`any type of node <tab-node-tree-types>`.
These parts include the title, sockets, properties and more.

.. figure:: /images/interface_controls_nodes_parts_overview.png


.. _interface-nodes-parts-title:

Title
=====

The title shows the name/type of the node;
it can be overridden by changing the node's :ref:`Label <bpy.types.Node.label>`.
On the left side of the title is the *collapse* toggle
which can be used to collapse the node. This can also be done with :kbd:`H`.

.. figure:: /images/interface_controls_nodes_parts_collapsed.png

   How a node appears when collapsed.


.. _interface-nodes-parts-preview:

Preview
-------

Previews are an overlay that shows a small image above the node displaying the node result.
Not all nodes support previews, but the ones that do can be toggled using
the :bl-icon:`hide_off`/:bl-icon:`hide_on` icons in the top right-hand corner of the node next to the title.

Previews can be disabled for the whole node tree by using
:ref:`Previews <bpy.types.SpaceNodeOverlay.show_previews>` overlay toggle.


.. _bpy.types.NodeLink:

Sockets
=======

Sockets are input and output values for the node.
They appear as little colored circles on either side of the node.
Unused sockets can be hidden with :kbd:`Ctrl-H`.

Each socket is color-coded depending on what type of data it handles.

.. figure:: /images/interface_controls_nodes_parts_sockets.png

.. rubric:: Built-in

Shader (bright green)
   Used for shaders in :doc:`Cycles </render/cycles/index>` and :doc:`EEVEE </render/eevee/index>`.
Geometry (Sea Green)
   Used in :doc:`Geometry Nodes </modeling/geometry_nodes/index>`.
Menu (Dark Gray)
   Used for enum style inputs that show a dropdown menu or radio button in the UI.
Bundle (dark turquoise)
   Represents a generic bundle of multiple data types.
   Bundles can contain several values (e.g., geometry, vectors, or colors) grouped together,
   allowing compact data transfer between nodes.
Closure (light brown)
   Used in :doc:`Shader Nodes </render/shader_nodes/index>` and :doc:`Geometry Nodes </modeling/geometry_nodes/index>`
   for logical or procedural encapsulation.
   A closure can store and pass groups of node inputs and logic, enabling reusable "callable" node behaviors.

.. rubric:: Data

Boolean (light pink)
   Used to pass a true or false value.
Color (yellow)
   Indicates that the socket accepts/produces color information.
   The colors may or may not have an alpha component depending on the node tree type.
Float (light gray)
   Indicates that the socket accepts/produces floating-point numbers.
Integer (lime green)
   Used to pass an integer value (a number without a fractional component).
String (light blue)
   Used to pass a text value.
Vector (dark blue)
   Represents vector data such as coordinates and normals. Vectors can have 2, 3, or 4 components:

   - **2D**: Shows and uses only X and Y components.
   - **3D**: Includes X, Y, and Z components.
   - **4D**: Includes X, Y, Z, and W components.
Rotation (pink)
   Indicates a rotation/quaternion.
Matrix (dark pink)
   Indicates a 4×4 matrix of float values, it is often used to represent a :term:`Transformation Matrix`.

.. rubric:: Data-Blocks

Collection (white)
   Used to pass a collection data-block.
Object (orange)
   Used to pass an object data-block.
Material (salmon)
   Used to pass a material data-block.
Texture (pink)
   Used to pass a texture data-block.
Image (apricot)
   Used to pass an image data-block.
Font (brown)
   Used to pass an font data-block.


.. _interface-controls-nodes-socket_shape:

Socket Shape
------------

Data sockets can have different shapes, indicating the data structure use to transport data.
The data structure determines how values are passed and interpreted.
More complex structures allow passing multiple values through a single connection.

Auto
   Automatically detects a good structure type based on how the socket is used.
Dynamic (Circle)
   Socket can work with multiple types of structures.
Single (Square)
   These sockets expects a single value, they are represented by a circular socket shape.
Fields (Diamond)
   Represents a value that can vary per element (e.g. per point, edge, or face).
   You can think of a field as a "value map", similar to how the brightness of pixels
   in a grayscale image represents varying values across space.

   If a single value is connected to a field socket,
   it is implicitly broadcast all elements receive the same value.

   Fields can have the following appearance:

   - **Diamond**: The socket can accept a field input, or it outputs a field. A constant single
     value can be connected to these sockets, but then the output will often not  vary per element.

   - **Diamond with Dot** : The socket can be a field, but it is currently a single value.
     This is helpful because it allows tracking where single values are calculated,
     instead of a field with many different results.
     It also means that :ref:`socket-inspection` will show the value instead of field input names.

   .. seealso::

      :doc:`Geometry Nodes Fields Documentation </modeling/geometry_nodes/fields>`
Grid (Four Squares)
   Represents a grid data structure, which stores values sampled across a **2D surface** or a **3D volume**.
   Grids can represent data such as image pixels, voxel densities, or other sampled values in space.
   They allow complex operations where values are distributed continuously across space,
   rather than being attached to individual geometry elements.


Inputs
------

The inputs are located on the bottom left side of the node,
and provide the data the node needs to perform its function.
Each input socket, except for the green shader input, when disconnected,
has a default value which can be edited via a color, numeric, or vector interface input.
In the screenshot of the node above, the second color option is set by a color interface input.

Some nodes have special sockets that can accept multiple inputs.
These sockets will have an ellipsis shape rather than a circle to indicate their special behavior.


Outputs
-------

The outputs are located on the top right side of the node,
and can be connected to the input of nodes further down the node tree.


Conversion
----------

Some socket types can be converted to others either implicitly or explicitly.
Implicit conversion happens automatically without the need of a conversion node.
For example, Float sockets and Color sockets can be linked to each other.

Once a socket conversion is made, data may be lost and cannot be retrieved later down the node tree.
Implicit socket conversion can sometimes change the data units as well.
When plugging a *Value* input node into an angle socket, it'll default to use radians
regardless of the scene's :ref:`bpy.types.UnitSettings`.
This happens because the Value node has no unit while the angle input does.

Valid conversions:

- Between color and vector -- mapping between color channels and vector components.
- Between color and float -- the color data is converted to its grayscale equivalent.
- Color/float/vector to Shader -- implicitly converts to color and gives the result of using an Emission node.
- Between float and integer -- integers simply become floats, floats are truncated.
- Between float and vector --  when a float becomes a vector the value is used for each component.
  When a vector becomes a float the average of the components is taken.
- Between float and boolean -- values greater than 0 are true, true maps to 1, and false maps to 0.
- Between rotations and matrices.

Explicit conversion requires the use of a conversion node such as
the :doc:`/render/shader_nodes/color/shader_to_rgb`
or the :doc:`/render/shader_nodes/color/rgb_to_bw` node.
The :doc:`/render/shader_nodes/utilities/math/math` node also contains
some functions to convert between degrees and radians.


.. _bpy.types.NodeSetting:

Properties
==========

Many nodes have settings which can affect the way they interact with inputs and outputs.
Node settings are located below the outputs and above any inputs.

.. figure:: /images/interface_controls_nodes_parts_controls.png

   An example of the controls on the Chroma Key node.
