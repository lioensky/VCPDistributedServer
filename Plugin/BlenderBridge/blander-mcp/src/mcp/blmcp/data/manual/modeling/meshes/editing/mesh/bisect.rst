.. _bpy.ops.mesh.bisect:
.. _tool-mesh-bisect:

******
Bisect
******

.. reference::

   :Mode:      Edit Mode
   :Tool:      :menuselection:`Toolbar --> Knife --> Bisect`
   :Menu:      :menuselection:`Mesh --> Bisect`

The Bisect tool cuts the selected geometry in two using an infinitely large plane.

Usage
=====

Orient the view so that the cutting plane will appear as a line (for example, the Top view
when cutting the mesh into left and right halves). Then activate the tool and drag the cutting
line using :kbd:`LMB`. While dragging, the following shortcuts are available (also shown in
the :doc:`status bar </interface/window_system/status_bar>`):

Move :kbd:`Spacebar`
   Changes the location of the line.
Snap :kbd:`Ctrl`
   Constrains the rotation of the line to 15 degree intervals.
Flip :kbd:`F`
   Changes which side of the plane is seen as the "outer" side. This is later used with the
   *Fill* and *Clear Inner/Outer* options.


Options
=======

After dragging the line, a yellow arrow shows the direction towards the "outer" side,
and the following options are available in the :ref:`bpy.ops.screen.redo_last` panel:

Plane Point, Plane Normal
   The plane can be numerically adjusted for precise values.
Fill
   Create new faces along the cutting plane to cover up any holes left by *Clear Inner/Outer*.
   Materials, UV coordinates, and Color Attributes are assigned based on the surrounding geometry.
Clear Inner/Outer
   Delete any geometry on the "inner"/"outer" side of the cutting plane. Note that this also
   affects geometry that was not originally selected.
Axis Threshold
   Any vertices closer to the cutting plane than this threshold will be reused.
   For the rest of the mesh, new vertices and edges are created.

Examples
========

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_mesh_bisect_example.png
          :width: 300px

          Example of a common use of bisect.

     - .. figure:: /images/modeling_meshes_editing_mesh_bisect_uv.jpg
          :width: 320px

          Example of bisect with the *Fill* option enabled.
