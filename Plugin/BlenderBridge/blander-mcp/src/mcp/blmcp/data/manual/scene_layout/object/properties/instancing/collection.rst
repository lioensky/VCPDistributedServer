
**********
Collection
**********

.. reference::

   :Mode:      Object Mode
   :Panel:     :menuselection:`Properties --> Object Properties --> Instancing --> Collection`

*Instance Collections* allows you to create an instance of a collection for each instance of another object.
Collections may contain animations, objects with physics simulations and even other nested collections.


Basic Usage
===========

Create a Collection:
   - Create a new collection (this can be done via the Outliner).
   - Link the objects that need to be instanced as part of the newly created collection.
Create a new Collection Instance:
   - :menuselection:`Add --> Collection Instance`

At this point, an instance of the collection and an :doc:`empty object </modeling/empties>` will appear.
You can duplicate the empty, and the *Instance Collections* settings will be preserved for each empty.
This way, you can get multiple copies of linked data very easily.


Collections and Dynamic Linking
===============================

See :doc:`Appending and Linking </files/linked_libraries/index>`
to understand how to dynamically link data from another blend-file into the current file.
You can dynamically link collections from one blend-file to another.
When you do so, the linked collection does not appear anywhere in your scene
until you create an object controlling where the collection instance appears.


Making an Instanced Collection Real
===================================

If you want to make further edits on an instanced collection select the *Instance Collection*.
Then call :ref:`bpy.ops.object.duplicates_make_real` to convert
the collection into regular objects that can be transformed and animated normally.

.. note::

   Note that if the instanced collection was linked from an external file, the Object Data
   (mesh, materials, textures, transforms) will also still be linked from the original collection.
   However, the various object's parent-child relationships do not carry over.
