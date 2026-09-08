.. _bpy.ops.mesh.intersect_boolean:

*******************
Intersect (Boolean)
*******************

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Face --> Intersect (Boolean)`

Performs Boolean operations between the selected and unselected geometry.

.. figure:: /images/modeling_meshes_editing_face_intersect-boolean_example.png

   Selecting a sphere and performing an Intersection, Union, and Difference
   with a cube.

.. tip::

   Hide geometry by pressing :kbd:`H` to exclude it from the operation,
   then :kbd:`Alt-H` afterwards to unhide it again.

.. seealso::

   The :doc:`/modeling/modifiers/generate/booleans` can perform these same operations
   non-destructively between different mesh objects.

The :ref:`bpy.ops.screen.redo_last` panel offers the following options:

Boolean Operation
   :Intersect:
      Only keep the volume that's inside both the selected and the unselected geometry.
   :Union:
      Remove the interior faces between the selected and the unselected geometry.
   :Difference:
      Cut the selected geometry out of the unselected geometry, then remove the selected geometry.

Solver
   Algorithm used to perform the Boolean operation.

   :Float:
      Uses a simple solver which offers good performance but lacks support for overlapping geometry.

      Merge Threshold
         Tolerance for close faces to be considered touching.
         It may be useful to increase this when some intersections aren't detected that should be and
         when extra geometry is being created because edges aren't detected as overlapping.

         .. warning::

            A threshold approaching the size of faces may cause very slow calculation.
            In general, keep this value small.

   :Exact:
      Uses a complex solver which offers the best results and has full
      support for overlapping geometry, but is much slower.

Swap
   When using *Difference*, cut the unselected geometry out of the selected geometry instead
   of the other way around.

Self Intersection
   Correctly handle self-intersection in the participating geometry, at the cost of performance.
