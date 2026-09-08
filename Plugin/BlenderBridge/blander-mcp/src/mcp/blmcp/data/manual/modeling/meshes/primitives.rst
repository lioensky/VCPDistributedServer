
***************
Mesh Primitives
***************

.. reference::

   :Mode:      Object Mode, Edit Mode
   :Menu:      :menuselection:`Add --> Mesh`
   :Shortcut:  :kbd:`Shift-A`

Meshes are the most common object type used in 3D scenes.
Blender provides a variety of built-in mesh primitives that serve as starting points for modeling.
These primitives can be added in both Object Mode and Edit Mode, where they appear at the location of the 3D Cursor.

.. figure:: /images/modeling_meshes_primitives_all.png

   Blender's standard mesh primitives.

.. tip::

   Planar meshes like *Plane*, *Circle*, and *Grid* can become three-dimensional
   by moving vertices out of their original plane.

.. note::

   Additional primitives can be enabled through add-on extensions.
   See :doc:`Get Extensions </editors/preferences/extensions>` for more information.


Common Options
==============

These options can be specified in the :ref:`bpy.ops.screen.redo_last` panel,
which appears when the object is created.
Options included in more than one primitive are:

Generate UVs
   Generates a default UV unwrapping of new geometry.
   This will be defined in the first UV layer (which will get added if needed).
Align to View, Location, Rotation
   See :ref:`Common Object Options <object-common-options>`.


.. _bpy.ops.mesh.primitive_plane_add:

Plane
=====

The standard plane is a single quad face composed of four vertices, four edges, and one face.
It lies flat and has no thickness, making it a purely two-dimensional object.

Planes are commonly used to represent surfaces such as floors, walls, tabletops, or mirrors.
They are also frequently used as emitter objects, camera backgrounds, or for projection mapping.

Size
   Sets the width and height of the plane (the full extent from edge to edge).

.. seealso::

   :ref:`Mesh Plane <bpy.ops.image.import_as_mesh_planes>` allows importing an image as a textured plane.
   The plane's dimensions are automatically scaled to match the image's aspect ratio.

.. tip::

   Planes are useful as a starting point for modeling panels, ceilings, cloth simulations, or sculpting surfaces.
   Apply modifiers like *Subdivision Surface* or *Displace* to turn a flat plane into complex geometry.

.. toctree::
   :hidden:

   import_images_as_planes.rst


.. _bpy.ops.mesh.primitive_cube_add:

Cube
====

Adds a standard cube mesh composed of six quad faces, eight vertices, and twelve edges.
This is one of the most basic and frequently used primitives in modeling,
serving as a starting point for creating boxes, crates, buildings, or sculpting bases.

Size
   Sets the total width, height, and depth of the cube (i.e., the full diameter along each axis).
   A size of 2 creates a cube that spans from -1 to +1 on all axes.

.. tip::

   The cube is ideal for hard-surface modeling and is commonly used as a base for applying
   modifiers such as *Subdivision Surface*, *Boolean*, or *Bevel*.


.. _bpy.ops.mesh.primitive_circle_add:

Circle
======

Adds a flat, 2D ring of vertices forming a polygonal approximation of a circle.
This primitive is useful as a starting point for cylindrical objects, holes, pipe ends,
or extrusion-based modeling workflows.

Vertices
   Number of vertices used to define the perimeter of the circle.
   Higher values result in a smoother shape.
Fill Type
   Sets how the center of the circle is filled:

   :Triangle Fan: Fills the circle with triangular faces sharing a central vertex.
   :N-gon: Fills the center with a single N-gon face.
   :Nothing: Leaves the circle unfilled; only the perimeter vertices are created.
Radius
   Distance from the center to the outer edge of the circle.


.. _bpy.ops.mesh.primitive_uv_sphere_add:

UV Sphere
=========

A UV sphere is composed of quad faces arranged in horizontal rings and vertical segments,
with triangle fans at the poles. This structure mirrors how textures are typically mapped
in 2D (hence the name "UV" sphere), making it well-suited for texturing.

It resembles lines of latitude and longitude on a globe, which also makes it useful for
planetary models or spherical shapes with pole-to-pole UV seams.

Segments
   Number of vertical segments (longitudinal divisions).
   These are like meridians on a globe, running from the north to south pole.
Rings
   Number of horizontal segments (latitudinal divisions).
   These are like parallels on a globe, stacked from top to bottom.

   .. note::

      Rings correspond to face loops, not edge loops, so the actual number of visible edge loops is one less.

Radius
   Distance from the center to the outer surface of the sphere.

.. tip::

   For clean shading, enable *Smooth Shading* and apply a *Subdivision Surface* modifier.


.. _bpy.ops.mesh.primitive_ico_sphere_add:

Icosphere
=========

An icosphere is a sphere built from equilateral triangles
and has a more uniform distribution of vertices compared to a UV sphere.
This makes it ideal for sculpting, simulations, or applications where topological regularity is important.

It is created by recursively subdividing the faces of an icosahedron, which is a polyhedron with 20 triangular faces.

Subdivisions
   Number of recursive subdivision steps.
   Each step splits every triangle into four new triangles, increasing the mesh resolution exponentially.

   - Subdivision Level 1 creates the base icosahedron.
   - Higher levels smooth the surface and increase vertex count.

   .. warning::

      Subdividing an icosphere quickly increases the vertex count.
      For example, 10 subdivisions generate over 5 million triangles and may crash Blender.
Radius
   Distance from the center to the outer surface of the sphere.

.. tip::

   Icospheres are often used in simulations, particle emitters,
   and sculpting workflows where uniformity and triangle-only topology are beneficial.


.. _bpy.ops.mesh.primitive_cylinder_add:

Cylinder
========

Creates a cylindrical mesh composed of two circular ends and vertical faces.
This shape is commonly used to model objects like handles, rods, pillars, and barrels.

Vertices
   Number of vertices used to define the circular ends.
   Higher values result in a smoother circular profile.
Radius
   Radius of the cylinder's circular ends, measured from the center to the perimeter.
Depth
   Height of the cylinder along the Z axis.
Cap Fill Type
   Determines how the top and bottom of the cylinder are filled:

   :Nothing:
      No end caps are added. Only the side faces are created, forming a tube.
      Useful for modeling pipes or hollow containers.
   :N-gon:
      Each end is filled with a single N-gon face.
   :Triangle Fan:
      Each end is filled with triangular faces sharing a central vertex.


.. _bpy.ops.mesh.primitive_cone_add:

Cone
====

Creates a cone- or pyramid-shaped mesh. Useful for modeling objects like spikes, traffic cones, or wizard hats.
You can also create frustums (truncated cones) or simple pyramids by adjusting the top radius.

Vertices
   Number of vertices used to define the circular base (or polygon base in the case of a pyramid).
   Higher values produce smoother curves.
Radius 1
   Radius of the base of the cone (bottom circle).
Radius 2
   Radius of the tip (top circle). A value of 0 creates a standard cone with a pointed tip.
   Non-zero values result in a frustum shape.
Depth
   Height of the cone along the Z axis.
Cap Fill Type
   Determines how the base of the cone is filled:

   :Nothing:
      No bottom cap is added. Only the side faces are created.
      Useful for creating open containers or hollow cones.
   :N-gon: Fills the base with a single N-gon face.
   :Triangle Fan: Fills the base with triangular faces sharing a central vertex.

.. tip::

   To create a pyramid, set *Vertices* to 4 and use *N-gon* or *Triangle Fan* as the cap type.
   Adjust *Radius 2* to 0 to keep the top pointed.


.. _bpy.ops.mesh.primitive_torus_add:

Torus
=====

A doughnut-shaped primitive created by rotating a circle around an axis.
This shape is commonly used for rings, pipes, and stylized details.

Operator Presets
   Saved torus settings that can be reused.
   These are stored as Python scripts in the presets directory.
Major Segments
   Number of segments that make up the main circular ring of the torus.
   Think of this as the number of steps in the spin operation around the central axis.
Minor Segments
   Number of segments making up the circular cross-section of the torus.
   Each segment is rotated around the main ring.
Dimensions Mode
   Selects the method used to define the shape and size of the torus:

   :Major/Minor:
      Define the torus using the radius of the main ring and the radius of the cross-sectional circle.
   :Exterior/Interior:
      Define the torus using the total outer radius and the radius of the central hole.

Major Radius :guilabel:`Major/Minor`
   Distance from the center of the torus to the center of the cross section.
Minor Radius :guilabel:`Major/Minor`
   Radius of the cross-sectional circle (thickness of the ring).
Exterior Radius :guilabel:`Exterior/Interior`
   Total radius from the center of the torus to its outer edge.
Interior Radius :guilabel:`Exterior/Interior`
   Radius of the hole at the center of the torus.


.. _bpy.ops.mesh.primitive_grid_add:

Grid
====

A regular grid composed of quadrilateral faces, useful as a base for landscapes, cloth, or organic surfaces.
You can increase the number of subdivisions to create a more detailed mesh suitable for sculpting or simulation.

X Subdivisions
   Number of face spans along the X axis.
Y Subdivisions
   Number of face spans along the Y axis.
Size
   Sets the width and height of the plane (the full extent from edge to edge).


.. _bpy.ops.mesh.primitive_monkey_add:

Monkey
======

Adds a stylized monkey head mesh named "Suzanne".
Suzanne is a gift from old NaN to the community and
remains in Blender as a playful "Easter egg" and is widely recognized as Blender's mascot.

This primitive is commonly used for testing materials, lighting setups, and modifiers such as
:term:`Subdivision Surface`.

It serves a similar purpose to well-known test models like the
`Utah Teapot <https://en.wikipedia.org/wiki/Utah_teapot>`__ or the
`Stanford Bunny <https://en.wikipedia.org/wiki/Stanford_Bunny>`__.

Size
   Controls the overall scale of the mesh.
