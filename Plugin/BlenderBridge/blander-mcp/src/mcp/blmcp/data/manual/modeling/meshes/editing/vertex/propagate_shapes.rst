.. _bpy.ops.mesh.shape_propagate_to_all:

*******************
Propagate to Shapes
*******************

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Vertex --> Propagate to Shapes`

Applies the current positions of the selected vertices to all other
:doc:`shape keys </animation/shape_keys/introduction>` on the object.
This allows edits made in *Edit Mode* to be consistently transferred across every shape key.

This is useful for:

- Correcting vertex positions that should be the same in all shape keys.
- Fixing topology issues or small modeling mistakes without manually editing each shape key.
- Ensuring consistent base structure across shape key variations.

.. warning::

   - This action **overwrites** the affected vertex positions in all shape keys.
     Use with caution if some shape keys require unique deformations for those vertices.
   - It is generally best applied to structural corrections that must be shared
     (e.g. moving an eyelid edge loop slightly higher in all expressions).
