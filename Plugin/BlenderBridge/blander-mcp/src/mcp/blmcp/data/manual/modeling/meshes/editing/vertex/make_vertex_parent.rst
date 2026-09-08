.. _bpy.ops.object.vertex_parent_set:

******************
Make Vertex Parent
******************

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Vertex --> Make Vertex Parent`
   :Shortcut:  :kbd:`Ctrl-P`

Parents the selected objects to the selected vertex or triplet of vertices.

If one vertex is selected, the objects will start following its location.
If three vertices are selected, the objects will follow the centerpoint of the resulting
triangle and rotate together with that triangle. (No triangular face needs to exist.)

While in Edit Mode, the child objects can be selected by clicking them in the
:doc:`Outliner </editors/outliner/introduction>` or pressing :kbd:`Ctrl-LMB` on them
in the 3D Viewport. If Blender switches back to Object Mode at this point, make sure that
:menuselection:`Edit --> Lock Object Modes` is enabled in the topbar.

.. seealso::

   - :doc:`Parenting overview </scene_layout/object/editing/parent>`
   - :doc:`/modeling/meshes/editing/vertex/hooks` -- for the opposite operation, "parenting" vertices to objects.
