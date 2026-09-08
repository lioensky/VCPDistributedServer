
*****
Faces
*****

.. reference::

   :Mode:      Object Mode
   :Panel:     :menuselection:`Properties --> Object Properties --> Instancing`

*Instancing Faces* is the capability to replicate an object on each face of a parent object.
One of the best ways to explain this is through an example illustration.

Scale
   Scales each instance according to the size of its corresponding face.

   Inherit Scale
      Scale the instance faces objects.

*Make Instance Face* tool converts linked objects (that share mesh data) into instanced faces.
This tool creates the parent object (instancer) with faces where the objects were,
then it uses *Instancing Faces* to put instances at the location of every created face.

You can go back from *Instancing Faces* to multiple linked objects using
:ref:`bpy.ops.object.duplicates_make_real`.

.. seealso:: Example blend-file

   Download the blend-file used for the examples on this page
   `here <https://archive.blender.org/wiki/2015/index.php/File:Manual-2.5-Duplifaces-Example01.blend>`__.


Basic Usage
===========

In this example we will use a UV sphere with an extruded "north pole" as our base object and
a cube as our parent mesh. To parent the sphere to the cube, in *Object Mode*,
first :kbd:`LMB` select the sphere, then :kbd:`Shift-LMB` select the cube
(order is very important here), and finally :kbd:`Ctrl-P` to parent.

.. list-table::

   * - .. figure:: /images/scene-layout_object_properties_instancing_faces_cube-before.png
          :width: 320px

          A cube and a sphere.

     - .. figure:: /images/scene-layout_object_properties_instancing_faces_cube-after.png
          :width: 320px

          Instancing Faces applied to the cube.

Next, in the :menuselection:`Properties --> Object Properties --> Instancing`,
select *Faces*. The sphere is instanced, one for each face of the cube.

.. note:: Inherited properties

   The location, orientation, and scale of the instanced child(ren) matches that of the faces of the parent.
   So, if several objects are parented to the cube, they will all be instanced once for each face on the cube.
   If the cube is subdivided, every child will be instanced for each face on the cube.

Both the parent object and original are displayed as editable "templates" in 3D Viewport,
but neither is rendered.


Scale
=====

.. list-table::

   * - .. figure:: /images/scene-layout_object_properties_instancing_faces_scale-enabled.png
          :width: 320px

          Scale enabled.

     - .. figure:: /images/scene-layout_object_properties_instancing_faces_scale-changed.png
          :width: 320px

          Top face of cube scaled down.

By enabling *Scale* for the parent object,
the scale of the child objects will be adapted to the size of each face in the parent object.

Thus, by rescaling the face of the parent object,
the size of the instanced object will change accordingly.


Limitations/Considerations
==========================

The positioning of the instanced geometry relative to the face is dependent upon the position
of the child objects relative to the instancer's origin. This can lead to some visual artifacts
in the 3D Viewport as the geometry of the original objects overlaps or intersects with
the instanced geometry.
One workaround is to move the origin of the instancer mesh off of the plane of the faces.

If the geometry of the children is not symmetrical then the orientation of the face
(as determined by the order of its vertices) could matter. As of 2.70 Blender does not have
tools which allow you to adjust the ordering of the vertices on a face.

However, there is a workflow that lets you control for this. Make a single square and
enable the *Instancing Faces* so you can see the instanced geometry in the 3D Viewport.
If the orientation is not what you want, rotate the face until it is how you want.
Typically you want to do the rotation in Edit Mode, not Object Mode,
but this is not a hard rule.

Once you have the orientation correct,
Duplicate the face and move the duplicate where you want it.
Repeat this process until you have enough faces.
Since it is common for these faces to butt up against one another,
your geometry will have lots of duplicate vertices.
Use the *Merge by Distance* button in the Tools panel.


.. rubric:: Demo Video

`A short video illustrating this workflow <https://www.youtube.com/watch?v=diI8xJ9oo_8>`__
