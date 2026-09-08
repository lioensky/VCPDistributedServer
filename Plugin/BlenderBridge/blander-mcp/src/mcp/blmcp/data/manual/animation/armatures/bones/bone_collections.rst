
.. _bone-collections:

****************
Bone Collections
****************

:term:`Bone Collections <Bone Collection>` group the bones of an
:term:`Armature` into named collections. The armature is the owner of these
collections, so they are available in all modes. Bone Collections are identified
by their name, which are unique within the Armature.
Bone Collections can be nested inside other Bone Collections to create an organized hierarchy for complex rigs.

In the text below, "collection" is understood to refer to "bone collection";
:term:`Scene Collections <Collection>` are not described here.

Bone Collections can be managed via :ref:`the Armature and Bone property panels <bpy.types.BoneCollection>`.


Visibility
==========

Bone Collections can be shown & hidden via the list in the Armature properties,
as well as via the list in the Bone properties. Bone visibility is determined by
the visibility of its collections, its own 'solo' and 'hidden' properties:

- If the bone itself is marked as 'hidden', it is invisible regardless of the
  bone collections.
- If a parent collection is hidden, child collections will also be hidden; same is true for soloed collections.
- A bone is visible when it is contained in any visible collection.
- If a collection is soloed, it will be visible regardless of the collection's 'hidden' property.
- A bone that is not assigned to any bone collection is visible; otherwise it
  would be impossible to select it & assign it to a collection.


.. _bone_collections_library_overrides:

Library Overrides
=================

Bone collections can be added using library overrides. For this to work, both
the armature Object and the Armature itself need to be overridden.

Limitations
-----------

There are a few limitations when it comes to bone collections & overrides:

- Only bone collections that are local to the current blend file can be edited.
- Bone collections that already existed on the linked-in Armature are read-only,
  and only their visibility can be toggled. Those visibility changes won't be
  saved, though.
- Custom properties of overridden bone collections cannot be edited in the
  properties panel. Python access is fine; this is just a current limitation of
  Blender's UI code.


How It Works
------------

Bone collections added via overrides are 'anchored' to the preceding
collection, by name. Here is an example. The *italic* collections are defined on
the linked Armature in ``armature.blend``. The **bold** ones are added by
overrides in ``armature_shot_47.blend``.

- *FK Controls*
- *IK Controls*
- **Left Pinky** (anchored to "IK Controls")
- **Right Pinky** (anchored to "Left Pinky")

Now if the Armature in ``armature.blend`` gets updated with two more collections
it might look like this:

- *FK Controls*
- *IK Controls*
- *Face Controls*
- *Face Detail Controls*

After reloading ``armature_shot_47.blend``, it will look like this:

- *FK Controls*
- *IK Controls*
- **Left Pinky** (still anchored to "IK Controls")
- **Right Pinky** (still anchored to "Left Pinky")
- *Face Controls*
- *Face Detail Controls*


.. _bpy.types.armature.layers:

Some history
============

Bone Collections were introduced in Blender 4.0, as a replacement for armature
layers and bone groups. Bone Collections are owned by the Armature, so they are
available in all modes. To contrast, bone groups were stored on the object's
pose, and thus were not available in armature edit mode.
