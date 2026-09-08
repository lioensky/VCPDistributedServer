
********
Vertices
********

.. reference::

   :Mode:      Object Mode
   :Panel:     :menuselection:`Properties --> Object Properties --> Instancing`

*Instance Vertices* allows you to replicate child objects
at the location of every vertex of the parent object.

.. note::

   The relative :doc:`Object Origin </scene_layout/object/origin>` position
   of the parent and child objects determines offset instanced geometry from parent vertex.

Align to Vertex Normal
   Rotates all instanced objects according to the corresponding vertex normals of the parent mesh.

   To change the axis of direction of the instanced objects,
   select the child object and change the :ref:`Tracking Axis <bpy.types.Object.track_axis>`.

There are actually two approaches to modeling using instanced vertices.
They can be used as an arranging tool,
allowing you to model geometrical arrangements of objects (e.g. the columns of a Greek temple,
the trees in a garden, the desks in a classroom).
The object can be of any object type which Blender supports.
The second approach is to use them to model an object starting from a single part of it
(e.g. the spikes in a club, the thorns of a sea-urchin, the tiles in a wall, the petals in a flower).

.. note:: Download Example Blend-File

   You can download a file with the examples described on this page.
   In `this blend <https://archive.blender.org/wiki/2015/index.php/File:Manual-2.5-DupliVerts-Examples.blend>`__,
   the first example, a monkey parented to a circle is on layer 1;
   while a tentacle parented to an icosphere is on layer 2.


Usage
=====

Instanced Vertices as an Arranging Tool
---------------------------------------

All you need is a base object (e.g. the *tree* or the *column*)
and a pattern mesh with its vertices following the pattern you have in mind. In this section,
we will use a simple scene for the following part. We will be using a monkey head located at
the origin of the coordinate system as our base object and a circle at the same location as
our parent mesh.

.. list-table::

   * - .. figure:: /images/scene-layout_object_properties_instancing_verts_monkey-before.png
          :width: 320px

          A monkey head and a circle.

     - .. figure:: /images/scene-layout_object_properties_instancing_verts_monkey-after.png
          :width: 320px

          Instanced monkeys on Vertices.

First, in *Object Mode*, select the base object
and :kbd:`Shift-LMB` to add the circle to the selection (order is very important here),
and :kbd:`Ctrl-P` or :menuselection:`Object --> Parent --> Object`
to parent the base object to the circle.
Now, the circle is the parent of the monkey; if you move the circle, the monkey will follow it.

With only the circle selected, enable *Instancing Vertices*;
a monkey head should be placed at every vertex of the circle.

The original monkey head at the center and the parent mesh are still shown in the 3D Viewport but
neither will be rendered. If the placement and rotation of your monkey head are odd,
you might need to clear its rotation :kbd:`Alt-R`, scale :kbd:`Alt-S`,
location :kbd:`Alt-G`, and origin :menuselection:`Object --> Clear --> Origin`.


Rearranging
^^^^^^^^^^^

If you now select the base object and modify it in either Object or Edit Mode,
all changes will also affect the shape of all instanced objects.
You can also select the parent mesh to modify the arrangement of the instances;
adding vertices will also add more base objects.

Note that the base objects will inherit changes made to the parent mesh in Object Mode,
but not in Edit Mode. So scaling the circle up in Object Mode will enlarge the monkey head,
while scaling the circle up in Edit Mode will only increase the distance between the base objects.


Orientation
^^^^^^^^^^^

The orientation of the base objects can be controlled by
enabling *Align to Vertex Normal* in the *Instancing* panel.
This will rotate all base objects according to the vertex normals of the parent mesh.

To change the orientation of the instanced objects,
select the base object and change the :ref:`Tracking Axis <bpy.types.Object.track_axis>`.

.. list-table:: Output of various orientations.

   * - .. figure:: /images/scene-layout_object_properties_instancing_verts_orientation.png
          :width: 320px

          Orientation enabled, orientation +Y.

     - .. figure:: /images/scene-layout_object_properties_instancing_verts_negy.png
          :width: 320px

          Negative Y.

   * - .. figure:: /images/scene-layout_object_properties_instancing_verts_posx.png
          :width: 320px

          Positive X.

     - .. figure:: /images/scene-layout_object_properties_instancing_verts_posz.png
          :width: 320px

          Positive Z, up X.

.. note::

   The axes of an object can be made visible in
   the :menuselection:`Properties --> Object Properties --> Viewport Display` panel.
   To display the vertex normals of the parent mesh,
   enter *Edit Mode* and enable this visualization in
   the :menuselection:`Display & Shading --> Viewport Overlays --> Normals`
   where you can also resize the displayed normals as necessary.


Instanced Vertices as a Modeling Tool
-------------------------------------

Very interesting models can be made using *Instancing Vertices* and a standard primitive.
In this example, a simple tentacle was made by extruding a cube a couple of times.
The tentacle object was then parented to an icosphere.
With *Align to Vertex Normal* enabled for the parent mesh (the icosphere),
the orientation of the base object (the tentacle)
was adapted to the vertex normals of the parent mesh
(in this case the tentacle was rotated -90° about the X axis in Edit Mode).

.. list-table::

   * - .. figure:: /images/scene-layout_object_properties_instancing_verts_tentacle.png

          A simple tentacle set to smooth.

     - .. figure:: /images/scene-layout_object_properties_instancing_verts_norot.png

          Tentacles instanced onto the parent mesh.

     - .. figure:: /images/scene-layout_object_properties_instancing_verts_rot.png

          *Align to Vertex Normal* enabled to align instanced geometry.

As in the previous example, the shape and proportions of the arrangement can now be tweaked.

To turn all instanced geometry into real objects,
select the icosphere and :ref:`bpy.ops.object.duplicates_make_real`.
To make the icosphere and the tentacle a single object,
make sure they are all selected and go to :menuselection:`Object --> Join`, :kbd:`Ctrl-J`.

.. seealso::

   Other duplication methods are listed :doc:`here </scene_layout/object/editing/duplicate>`.
