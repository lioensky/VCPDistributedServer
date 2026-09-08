
******
Baking
******

Baking allows saving and loading intermediate geometries.
Baking parts of the node tree can be used for better performance.

The data format used to store geometry data is not considered to be an import/export format.
Volume objects, however, are saved using the OpenVDB file format which can be used interoperably.

Data can be baked using two methods:

- :doc:`/modeling/geometry_nodes/geometry/operations/bake` -- used to bake any portion of the node tree.
- :ref:`Simulation Zone Baking <geometry_nodes-simulation-baking>` --
  used to bake animations where the result of one geometry state can influence the next state.

Data is not stored to disk until the :ref:`Bake <bpy.ops.object.geometry_node_bake_single>` operation is ran.

.. important::

   - Blend-files must be saved to a disk before data can be baked.
   - It's not guaranteed that data written with one Blender version can be read by another Blender version.


.. _bpy.ops.object.geometry_node_bake_single:

Bake Geometry Node
==================

Bakes the simulations and bake nodes in all modifiers for the selected objects.

.. tip::

   When data is baked the number of baked frames is displayed above the simulation zone or bake nodes.


.. _bpy.types.NodesModifierDataBlock:

Data-Block References
=====================

.. reference::

   :Editor:    Geometry Node Editor
   :Panel:     :menuselection:`Sidebar --> Node --> Data-Block References`

Baked geometries that reference other data-blocks such as materials are listed here.

This panel allows changing these references after the data has been baked.

.. note::

   Currently only material data-blocks are supported.
