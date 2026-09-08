.. _bpy.ops.object.duplicate_move_linked:

****************
Duplicate Linked
****************

.. reference::

   :Mode:      Object Mode
   :Menu:      :menuselection:`Object --> Duplicate Linked`
   :Shortcut:  :kbd:`Alt-D`

You also have the choice of creating a *Linked Duplicate* rather than a *Duplicate*;
this is called a deep link. This will create a new object with **all** of its data linked to
the original object. If you modify one of the linked objects in *Edit Mode*,
all linked copies are modified. Transform properties (object data-blocks) still remain copies,
not links, so you still can rotate, scale, and move freely without affecting the other copies.
Reference the `Examples`_ for the discussions below.

If the original object was animated, the duplicate will link to the same :ref:`Action <bpy.types.Action>`.
This means that, even though each object has separate transform properties,
they will be set to the same values by the animation system.
If this is not desired, make the action a single-user copy in the
:doc:`Action </editors/dope_sheet/modes/action>` or
:doc:`NLA Editor </editors/nla/introduction>`.

Linked
   In the *Duplicate Objects* :ref:`bpy.ops.screen.redo_last` panel the *Linked* checkbox is checked
   unlike with *Duplicate*.

.. hint::

   If you want to make changes to an object in the new linked duplicate independently of
   the original object, you will have to manually make the object a "single-user" copy
   by :kbd:`LMB` the number in the *Object Data* panel of the Properties. (See :ref:`ui-data-block`.)

.. seealso::

   :ref:`bpy.ops.object.make_single_user` for unlinking data-blocks.


Examples
========

.. figure:: /images/scene-layout_object_editing_duplicate-linked_example.png

   The Cube object was linked duplicated.

The object ``Cube`` was linked duplicated, using :kbd:`Alt-D`.
Though both these cubes are separate objects with unique names:
``Cube`` and ``Cube.001``, the single mesh named ``Cube``, is shared by both.

- As a mesh is edited in *Edit Mode* in one object, the same occurs in
  the other cube as well. The mesh data are links, not copies.
- In contrast, if one of these two cubes is rotated or scaled in *Object Mode*,
  the other remains unchanged. The transform properties are copied, not linked.
- As in the previous example, the newly created cube has inherited
  the material of the original cube. The material properties are linked, not copied.

A common table has a top and four legs. Model one leg, and then make linked duplicates
three times for each of the remaining legs. If you later make a change to the mesh,
all the legs will still match. Linked duplicates also apply to a set of drinking glasses,
wheels on a car... anywhere there is repetition or symmetry.

.. seealso:: Linked Library Duplication

   :doc:`Linked Libraries </files/linked_libraries/index>` are also a form of duplication.
   Any object or data-block in other blend-files can be reused in the current file.

.. hint::

   If you want transform properties (i.e. object data-blocks) to be "linked",
   see the page on :doc:`parenting </scene_layout/object/editing/parent>`.
