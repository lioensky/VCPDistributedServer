.. index:: Grease Pencil Modifiers; Lattice Modifier
.. _bpy.types.GreasePencilLatticeModifier:

****************
Lattice Modifier
****************

The Lattice modifier deforms the base object according to
the shape of a :doc:`Lattice </animation/lattice>` object.

.. tip::

   A Lattice Modifier can quickly be added to selected objects by selecting them all,
   then selecting the lattice object last and pressing :kbd:`Ctrl-P` and choosing *Lattice Deform*.
   This will both add Lattice Modifiers to the selected objects and parent them to the lattice.

.. seealso::

   This documentation refers to the Lattice Modifier specific to the Grease Pencil object.
   For uses with other object types refer to the general :doc:`/modeling/modifiers/deform/lattice`.


Options
=======

.. figure:: /images/grease-pencil_modifiers_deform_lattice_panel.png
   :align: right

   Lattice Modifier.

Object
   The :doc:`Lattice </animation/lattice>` object with which to deform the base object.

Strength
   A factor to control blending between original and deformed points positions.


Influence
---------

See :ref:`grease-pencil-modifier-influence-filters`.


Example
=======

.. list-table:: Lattice modifier example.

   * - .. figure:: /images/grease-pencil_modifiers_deform_lattice_original.png
          :width: 320px

          Original model.

     - .. figure:: /images/grease-pencil_modifiers_deform_lattice_edit.png
          :width: 320px

          After lattice editing.
