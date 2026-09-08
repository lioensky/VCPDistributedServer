.. _bpy.ops.armature.split:

*****
Split
*****

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Armature --> Split`
   :Shortcut:  :kbd:`Y`

The *Split* operator disconnects selected bones from the rest of the armature,
creating a new, unconnected bone chain.

This is useful for restructuring rigs, separating limbs, or preparing bone chains to be transformed independently.

.. note::

   This operator only affects bone connectivity; the bones remain within the same armature object.
   To move the split bone chain to a separate object, use :ref:`bpy.ops.armature.separate`.
