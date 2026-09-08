
*****************
Selecting Objects
*****************

Selection determines which elements will be the target of our actions.
Selections work on the current scene visible objects.
Blender has advanced selection methods. Both in *Object Mode* and in *Edit Mode*.


.. _object-active:

Selections and the Active Object
================================

Blender distinguishes between two different states of selection:

.. figure:: /images/scene-layout_object_selecting_color.png

   Active object in yellow, selected object in orange, and unselected object in black.

In *Object Mode* the last (de)selected item is called the "Active Object"
and is outlined in yellow (the others are orange).
There is at most one active object at any time.

Many actions in Blender use the active object as a reference (for example linking operations).
If you already have a selection and need to make a different object the active one,
simply reselect it with :kbd:`Shift-LMB`.

All other selected objects are just selected. You can select any number of objects.
In order to change a property or to perform an operation on all selected objects (bones, and sequencer strips)
hold :kbd:`Alt`, while confirming.


.. _object-select-menu:

Select Menu
===========

.. _bpy.ops.object.select_all:

All
---

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`Select --> All`
   :Shortcut:  :kbd:`A`

Select all selectable objects.


None
----

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`Select --> None`
   :Shortcut:  :kbd:`Alt-A`

Deselect all objects, but the active object stays the same.


Invert
------

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`Select --> Invert`
   :Shortcut:  :kbd:`Ctrl-I`

Toggle the selection state of all visible objects.


Box Select
----------

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`Select --> Box Select`
   :Shortcut:  :kbd:`B`

Interactive :ref:`box selection <tool-select-box>`.


Circle Select
-------------

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`Select --> Circle Select`
   :Shortcut:  :kbd:`C`

Interactive :ref:`circle selection <tool-select-circle>`.


Lasso Select
------------

.. reference::

   :Mode:      All modes
   :Menu:      :menuselection:`Select --> Lasso Select`
   :Shortcut:  :kbd:`Ctrl-Alt-LMB`

See :ref:`tool-select-lasso`.


.. _bpy.ops.object.select_camera:

Select Active Camera
--------------------

.. reference::

   :Mode:      Object Mode
   :Menu:      :menuselection:`Select --> Select Active Camera`

Selects the active camera, this is especially handy in complex scene.


.. _bpy.ops.object.select_mirror:

Select Mirror
-------------

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`Select --> Select Mirror`

Select the Mirror objects of the selected object,
based on their names, e.g. "sword.L" and "sword.R".


.. _bpy.ops.object.select_random:

Select Random
-------------

.. reference::

   :Mode:      Object Mode
   :Menu:      :menuselection:`Select --> Select Random`

Randomly selects unselected objects based on percentage probability.
The percentage can be modified in the *Adjust Last Operation* panel.
It is important to note that the percentage is the likelihood of
an unselected object being selected and not the percentage amount of objects
that will be selected.


.. _bpy.ops.object.select_more:
.. _bpy.ops.object.select_less:
.. _bpy.ops.object.select_hierarchy:

Select More/Less
----------------

.. reference::

   :Mode:      Object Mode
   :Menu:      :menuselection:`Select --> More/Less`
   :Shortcut:  :kbd:`Ctrl-NumpadPlus`, :kbd:`Ctrl-NumpadMinus`

Their purpose, based on the hierarchical.

More
   Expand the selection to the immediate parent and children of the selected objects.
Less
   Contrast the selection, deselect objects at the boundaries of parent/child relationships.
Parent
   Deselects the currently selected objects and selects their immediate parents.
Child
   Deselects the currently selected objects and selects their immediate children.
Extend Parent
   Extends the selection to the immediate parents of the currently selected objects.
Extend Child
   Extends the selection to the immediate children of the currently selected objects.


.. _bpy.ops.object.select_by_type:

Select All by Type
------------------

.. reference::

   :Mode:      Object Mode
   :Menu:      :menuselection:`Select --> Select All by Type`

With this tool, it becomes possible to select objects of a certain type in one go.
For a description of all object types see :doc:`Object Types </scene_layout/object/types>`.


.. _bpy.ops.object.select_grouped:

Select Grouped
--------------

.. reference::

   :Mode:      Object Mode
   :Menu:      :menuselection:`Select --> Select Grouped`
   :Shortcut:  :kbd:`Shift-G`

There are two ways to organize the objects in relation to one another.
The first one is *parenting*, and the second is simple *grouping*.
These relationships to an artist's advantage by selecting members of respective families or groups.
*Select Grouped* uses the active object as a basis to select all others.

Children
   Selects all hierarchical descendants of the active object.
Immediate Children
   Selects all direct children of the active object.
Parent
   Selects the parent of this object if it has one.
Siblings
   Select objects that have the same parent as the active object.
   This can also be used to select all root level objects (objects with no parents).
Type
   Select objects that are the same type as the active one.
Collection
   Select all objects that are in the same collection as the active one.
   If the active object belongs to more than one collection,
   a list will pop up so that you can choose which collection to select.
Object Hooks
   Every hook that belongs to the active object.
Pass
   Select objects assigned to the same :doc:`Render Pass </render/layers/passes>`.
Color
   Select objects with same :ref:`Object Color <bpy.types.Object.color>`.
Keying Set
   Select objects included in the active :doc:`Keying Set </animation/keyframes/keying_sets>`.
Light Type
   Select matching light types.


.. _bpy.ops.object.select_linked:

Select Linked
-------------

.. reference::

   :Mode:      Object Mode
   :Menu:      :menuselection:`Select --> Select Linked`
   :Shortcut:  :kbd:`Shift-L`

Selects all objects which share a common data-block with the active object.
*Select Linked* uses the active object as a basis to select all others.

Object Data
   Selects every object that is linked to the same Object Data, i.e.
   the data-block that specifies the type (mesh, curve, etc.) and the build
   (constitutive elements like vertices, control vertices, and where they are in space) of the object.
Material
   Selects every object that is linked to the same material data-block.
Instanced Collection
   Select every object that is linked to the instanced collection.
Texture
   Selects every object that is linked to the same texture data-block.
Particle System
   Selects all objects that use the same *Particle System*.
Library
   Selects all objects that are in the same :doc:`Library </files/linked_libraries/index>`.
Library (Object Data)
   Selects all objects that are in the same :doc:`Library </files/linked_libraries/index>`
   and limited to *Object Data*.


.. _bpy.ops.object.select_pattern:

Select Pattern
--------------

.. reference::

   :Mode:      Object Mode
   :Menu:      :menuselection:`Select --> Select Pattern...`

Selects all elements whose name matches a given pattern.
Supported wild-cards: ``*`` matches everything, ``?`` matches any single character,
``[abc]`` matches characters in ``abc``, and ``[!abc]`` match any character not in ``abc``.
As an example ``*house*`` matches any name that contains ``house``,
while ``floor*`` matches any name starting with ``floor``.

Case Sensitive
   The matching can be chosen to be case sensitive or not.
Extend
   When *Extend* checkbox is checked the selection is extended instead of generating a new one.
