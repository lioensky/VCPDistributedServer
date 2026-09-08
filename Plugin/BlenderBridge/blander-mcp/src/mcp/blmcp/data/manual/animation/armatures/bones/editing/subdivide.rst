.. _bpy.ops.armature.subdivide:

*********
Subdivide
*********

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Armature --> Subdivide`

You can subdivide bones, to get two or more bones where there was just one bone.
The tool will subdivide all selected bones, preserving the existing relationships:
the bones created from a subdivision always form a connected chain of bones.

To create an arbitrary number of bones from each selected bone
in the Subdivide Multi :ref:`bpy.ops.screen.redo_last` panel.

Number of Cuts
   Specifies the number of cuts. As in mesh editing,
   if you set *n* cuts, you will get *n* + 1 bones for each selected bone.

.. list-table:: Subdivision example.

   * - .. figure:: /images/animation_armatures_bones_editing_subdivide_example-1.png

          An armature with one selected bone, just before multi-subdivision.

     - .. figure:: /images/animation_armatures_bones_editing_subdivide_example-2.png

          The selected bone has been "cut" two times, giving three sub-bones.
