
*****
Usage
*****

Relations Management
====================

.. figure:: /images/editors_outliner_usage_relations.png
   :align: right

   Linking objects to a collection.

Objects and collections can be reorganized, linked, or parented directly in the *Outliner* using drag-and-drop
operations. This provides an intuitive way to manage scene hierarchies and relationships.


Moving and Linking
------------------

- **Move:**
  Drag an object or collection onto another collection to move it there.

- **Link:**
  Drag an object (or collection) while holding :kbd:`Ctrl` and drop it onto a collection
  to link it instead of moving it.
  This allows the same object or collection to be part of multiple parent collections at once.


Parenting
---------

- **Parent to Object:**
  Drag an object onto another object to make it a child of that object.
  Hold :kbd:`Alt` while dropping to *not* keep the transform relationship (i.e. the child retains its world position).

- **Clear Parent:**
  Drag the child object out of its parent hierarchy to remove the parent relationship.
  Hold :kbd:`Alt` while dropping to clear the parent while preserving the parent's transform on the child.

- **Parent Across Collections:**
  To parent an object that resides in a different collection, hold :kbd:`Shift` while dragging.

See :ref:`bpy.types.Object.parent` for more information on parenting and transformation inheritance.

.. note::

   Drag-and-drop operations apply to the entire current selection.
   If some selected data-blocks are incompatible with the operation, they are left unchanged.


Modifiers, Constraints, and Visual Effects
==========================================

You can manage :doc:`Modifiers </modeling/modifiers/index>`, :doc:`Constraints </animation/constraints/index>`, and
:doc:`Visual Effects </grease_pencil/visual_effects/index>` from the Outliner in a couple of ways:

- You can drag and drop individual items to change their order within the :ref:`stack <modifier-stack>` or to copy
  them to another object.
- You can drag and drop the group item (e.g. *Modifiers*) to copy the whole stack to another object.
  The target object's existing stack will be replaced.
- You can apply and delete items using the context menu.


Drag & Dropping to 3D Viewport
==============================

Dragging an object from the Outliner to the :doc:`3D Viewport </editors/3dview/index>`
creates a :doc:`duplicate </scene_layout/object/editing/duplicate>` -- a new object with its own copy
of the underlying object data.

Dragging object data from the Outliner to the 3D Viewport creates a
:doc:`linked duplicate </scene_layout/object/editing/duplicate_linked>` -- a new object that references
the same underlying object data.
