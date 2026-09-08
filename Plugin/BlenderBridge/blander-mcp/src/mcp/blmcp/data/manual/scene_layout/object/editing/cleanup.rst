
********
Clean Up
********

Clean Vertex Group Weights
==========================

.. reference::

   :Mode:      Object Mode
   :Menu:      :menuselection:`Object --> Clean Up --> Clean Vertex Group Weights`

Clean Vertex Group Weights unassigns vertices from
:doc:`Vertex Groups </modeling/meshes/properties/vertex_groups/index>`
whose weights are below the *Limit*. Removes weights below a given threshold.
This tool is useful for clearing your weight groups of very low (or zero) weights.

In the example shown, a cutoff value of 0.2 is used (see operator options below)
so all blue parts are cleaned out.

Note, the images use the *Show Zero weights* Active option
so that unreferenced Weights are shown in Black.

.. figure:: /images/sculpt-paint_weight-paint_editing_clean-example.png

   Clean example.

Subset
   Restrict the tool to a subset.
   See above :ref:`The Subset Option <sculpt-paint_weight-paint_editing_subset>` for how subsets are defined.
Limit
   This is the minimum weight value that will be kept in the group.
   Weights below this value will be removed from the group.
Keep Single
   Ensure that the *Clean Vertex Group Weights* tool will not create completely unreferenced vertices
   (which are vertices that are not assigned to any vertex group), so each vertex will
   keep at least one weight, even if it is below the limit value!


Limit Total Vertex Groups
=========================

.. reference::

   :Mode:      Object Mode
   :Menu:      :menuselection:`Object --> Clean Up --> Limit Total Vertex Groups`

Reduce the number of weight groups per vertex to the specified Limit.
The tool removes lowest weights first until the limit is reached.

.. hint::

   The tool can only work reasonably when more than one weight group is selected.

Subset
   Restrict the tool to a subset.
   See above :ref:`The Subset Option <sculpt-paint_weight-paint_editing_subset>` for how subsets are defined.
Limit
   Maximum number of weights allowed on each vertex.


.. _bpy.ops.object.material_slot_remove_unused:

Remove Unused Material Slots
============================

.. reference::

   :Mode:      Object Mode
   :Menu:      :menuselection:`Object --> Clean Up --> Remove Unused Material Slots`

Removes unused :ref:`material slots <bpy.types.MaterialSlot>`.
