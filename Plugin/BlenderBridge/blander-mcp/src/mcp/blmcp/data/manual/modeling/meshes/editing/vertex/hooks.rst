.. _bpy.ops.object.hook:

*****
Hooks
*****

This menu works with the :doc:`/modeling/modifiers/deform/hooks`, which "parents" a set of vertices
to an external object. Transforming that object will then also transform those vertices.

The opposite operation -- parenting an external object to a vertex -- can be achieved using
:doc:`/modeling/meshes/editing/vertex/make_vertex_parent`.



.. _bpy.ops.object.hook_add_newob:

Hook to New Object
==================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Vertex --> Hooks --> Hook to New Object`
   :Shortcut:  :kbd:`Ctrl-H`

Creates an :doc:`Empty </modeling/empties>` at the average position of the selected vertices,
then adds a Hook modifier that attaches the vertices to this Empty.

If no vertices are selected, the active
:doc:`Vertex Group </modeling/meshes/properties/vertex_groups/introduction>` is used instead.


.. _bpy.ops.object.hook_add_selob:

Hook to Selected Object
=======================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Vertex --> Hooks --> Hook to Selected Object`
   :Shortcut:  :kbd:`Ctrl-H`

Adds a Hook modifier that attaches the selected vertices to the selected object (that is
not the currently active mesh). If no vertices are selected, the active Vertex Group is used instead.

To select another object while in Edit Mode, either click it in the
:doc:`Outliner </editors/outliner/introduction>` or click it with :kbd:`Ctrl-LMB` in the 3D Viewport.


Hook to Selected Object Bone
============================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Vertex --> Hooks --> Hook to Selected Object Bone`
   :Shortcut:  :kbd:`Ctrl-H`

Adds a Hook modifier that attaches the selected vertices to the selected bone.
If no vertices are selected, the active Vertex Group is used instead.

To select the bone of another object while in Edit Mode, click it with :kbd:`Ctrl-LMB`
in the 3D Viewport.

.. tip::

   Attaching vertices to a bone is more commonly done using the
   :doc:`/modeling/modifiers/deform/armature`.


Assign to Hook
==============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Vertex --> Hooks --> Assign to Hook`
   :Shortcut:  :kbd:`Ctrl-H`

Adds the selected vertices to an existing Hook modifier (as chosen from the menu)
and removes the unselected vertices from it.

Vertices can be assigned to multiple hooks at the same time.


.. _bpy.ops.object.hook_remove:

Remove Hook
===========

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Vertex --> Hooks --> Remove Hook`
   :Shortcut:  :kbd:`Ctrl-H`

Removes a Hook modifier (as chosen from the menu) from the mesh.


Select Hook
===========

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Vertex --> Hooks --> Select Hook`
   :Shortcut:  :kbd:`Ctrl-H`

Selects the vertices that are assigned to a particular Hook modifier (as chosen from the menu).


Reset Hook
==========

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Vertex --> Hooks --> Reset Hook`
   :Shortcut:  :kbd:`Ctrl-H`

Each Hook modifier stores a rest transformation for the "parent" object where the hooked
vertices stay in their original place. Clicking *Reset Hook* updates this rest transformation
to the parent object's current transformation (meaning the vertices will return to their original location).


Recenter Hook
=============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Vertex --> Hooks --> Recenter Hook`
   :Shortcut:  :kbd:`Ctrl-H`

Sets the center of a particular Hook modifier (as chosen from the menu) to the position of the
:doc:`/editors/3dview/3d_cursor`. This is the centerpoint for calculating the *Falloff* distance
of the modifier.

The center is shown in the 3D Viewport as a black dot, and is connected to the "parent" object
with a dashed black line.
