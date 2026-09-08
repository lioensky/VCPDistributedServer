
*****
Apply
*****

.. reference::

   :Mode:      Object Mode
   :Menu:      :menuselection:`Object --> Apply`
   :Shortcut:  :kbd:`Ctrl-A`

These operations lets you apply several transformations to the selected objects.
The object transformation coordinates are transferred to the object data.
If the objects have hierarchical descendants, it also applies those transformations to their children.


.. _bpy.ops.object.transform_apply:

Transforms
==========

.. reference::

   :Mode:      Object Mode
   :Menu:      :menuselection:`Object --> Apply --> Location / Rotation / Scale / Rotation & Scale`

Applying transforms resets an object's *Location*, *Rotation*, or *Scale* values
while visually keeping the object in place.
In practice, this means:

- The object's origin is moved to the global origin (for location).
- Rotation values are cleared to zero.
- Scale values are reset to 1.0.

The geometry itself is adjusted so that the object continues to appear unchanged in the 3D Viewport
and final render.

For simple cases you may not notice a difference,
but applying transforms can affect how modifiers, constraints, and parenting behave,
since they often depend on an object's transform values.

.. warning:: Armature Objects

   Applying transforms to armatures is supported, but it does **not** affect pose locations,
   animation curves, or constraints.
   It is recommended to apply transforms before rigging and animation.

.. important::

   When applying transforms to an object that shares Object Data with other objects,
   the data must first be made a :ref:`Single User <data-system-datablock-make-single-user>`.
   Blender will prompt you to confirm this action.


Options
-------

Location
   Apply (set) the location of the selection.
   This will make Blender consider the current location to be equivalent to 0 in each plane
   i.e. the selection will not move, the current location will be considered to be the "default location".
   The object origin will be set to actual (0, 0, 0) (where the colored axis lines intersect in each view).
Rotation
   Apply (set) the rotation of the selection.
   This will make Blender consider the current rotation to be equivalent to 0 degrees in each plane
   i.e. the selection will not rotated, the current rotation will be considered to be the "default rotation".
Scale
   Apply (set) the scale of the selection.
   This will make Blender consider the current scale to be equivalent to 0 in each plane
   i.e. the selection will not scaled, the current scale will be considered to be the "default scale".
Rotation & Scale
   Apply (set) the rotation and scale of the selection. Do the above two applications simultaneously.
Apply Properties
   Modify properties such as curve vertex radius, font size and bone envelope
   according to the applied transformation. (Found in the :ref:`bpy.ops.screen.redo_last` panel)


.. _bpy.ops.object.transforms_to_deltas:

Transforms to Deltas
====================

.. reference::

   :Mode:      Object Mode
   :Menu:      :menuselection:`Object --> Apply --> Location / Rotation / Scale to Deltas`

Converts the object's primary transforms (*Location*, *Rotation*, *Scale*) into
:ref:`Delta Transforms <bpy.types.Object.delta>`.
Any existing delta transforms will be added to the new values.

This allows you to "bake" the current transforms into the delta channels, while leaving the primary
transform channels free for new adjustments or keyframes.

Available options:

- **Location to Deltas** -- Converts the object's location to *Delta Location*.
- **Rotation to Deltas** -- Converts the object's rotation to *Delta Rotation*.
- **Scale to Deltas** -- Converts the object's scale to *Delta Scale*.
- **All Transforms to Deltas** -- Converts all three at once.


Options
-------

Reset Values
   Clear primary transform values after transferring to deltas.

   Clears the primary transform values after transferring them to deltas.
   When enabled, the object's main *Location*, *Rotation*, and *Scale* are reset
   (e.g. to 0 for location/rotation and 1 for scale), while the appearance remains unchanged
   because the deltas now contain the previous values.


.. _bpy.ops.object.anim_transforms_to_deltas:

Animated Transform to Deltas
============================

.. reference::

   :Mode:      Object Mode
   :Menu:      :menuselection:`Object --> Apply --> Animated Transform to Deltas`

Converts existing animation keyframes from the object's primary transforms
(*Location*, *Rotation*, *Scale*) into :ref:`Delta Transforms <bpy.types.Object.delta>`.

This means that the animation data is moved from the main transform channels
to the corresponding delta channels, leaving the main transforms unchanged at their current values.


.. _bpy.ops.object.visual_transform_apply:

Visual Transform
================

.. reference::

   :Mode:      Object Mode
   :Menu:      :menuselection:`Object --> Apply --> Visual Transform`

Apply the result of each selected object's constraints to that object's own transformation.
This will make the objects keep their location, rotation, and scale even if their
constraints are disabled or deleted.


Visual Geometry as Mesh
=======================

.. reference::

   :Mode:      Object Mode
   :Menu:      :menuselection:`Object --> Apply --> Visual Geometry to Mesh`

Apply the visual state of all selected objects (modifiers, shape keys, hooks, etc.) to object data.
This is a way to freeze all object data into static meshes, as well as converts non-mesh types to mesh.

For details, see the :ref:`object-convert-to` mesh.


.. _bpy.ops.object.visual_geometry_to_objects:

Visual Geometry to Objects
==========================

.. reference::

   :Mode:      Object Mode
   :Menu:      :menuselection:`Object --> Apply --> Visual Geometry to Objects`

Creates new objects from the evaluated geometry of the active object,
including the effects of all modifiers, constraints, and instancing.

This operator is similar to :ref:`Make Instances Real <bpy.ops.object.duplicates_make_real>`,
but with several key differences:

- Instanced geometry is **not** realized. Instead, shared data is preserved between objects that use it.
- The original object is **not removed or modified**,
  avoiding unintended disruptions to relationships with other objects.
- Instancing hierarchies are preserved by creating new objects
  and collections that reflect the evaluated structure.

This operator is useful for extracting visible results of geometry nodes, modifiers, or instancing setups
without permanently modifying the original scene structure.

.. note::

   Instance attributes (e.g. custom per-instance data) are currently **not** preserved.


.. _bpy.ops.object.duplicates_make_real:

Make Instances Real
===================

.. reference::

   :Mode:      Object Mode
   :Menu:      :menuselection:`Object --> Apply --> Make Instances Real`

*Make Instances Real* creates a new object for each
:doc:`instance </scene_layout/object/properties/instancing/index>` generated by the selected ones,
and removes any direct instancing from those.

In the end, each instance becomes a real object.

.. warning::

   This applies to both direct (from verts or faces...) and indirect (from particle system...) instancing.
   In case you have tens of thousands of instances (from particles for example),
   this can significantly slow down Blender, which does not always deal well with that many objects in a scene.


Options
-------

By default, new objects will be added to the same collection as the one containing their instancer,
without keeping any hierarchy relationships. This behavior can be altered with the following options.

Parent
   If *Keep Hierarchy* is not set, parents all the generated objects to the former instancer.

   Otherwise, parents all the generated objects *which are not already parented* to their respective instancer,
   or its matching new copy (this is important in case of recursive instancing, see the note below).

Keep Hierarchy
   Preserves internal hierarchies (i.e. parent relationships) in the newly generated objects.

.. tip::

   Usually, to get a new hierarchy as close as possible from the instancing one,
   you'll want to enable both of these options.

.. note::

   Preserving relationships in recursive instancing cases (instancers instancing other instancer objects, etc.)
   is only supported to some extent currently.

   Simple cases (like an empty instancing a collection containing instances of some other collections)
   will usually work, but more complex cases will fail to fully reproduce the whole instancing hierarchy.


.. _bpy.ops.object.parent_inverse_apply:

Parent Inverse
==============

.. reference::

   :Mode:      Object Mode
   :Menu:      :menuselection:`Object --> Apply --> Parent Inverse`

Applies the object's :ref:`parent-inverse-matrix` transform to the object data.
