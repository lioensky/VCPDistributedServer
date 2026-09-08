
************
Force Fields
************

Field Weights
=============

.. reference::

   :Panel:     :menuselection:`Particle System --> Field Weights`

The Field Weight panel allows you to control how much influence each type of external force field, or effector,
has on the particle system. Force fields are external forces that give dynamic system's motion.
The force fields types are detailed on the :doc:`Force Field Page </physics/forces/force_fields/index>`.

Effector Group
   Limit effectors to a specified group. Only effectors in this group will have an effect on the current system.
Gravity
   Control how much the Global Gravity has an effect on the system.
All
   Scale all of the effector weights.


Force Fields Settings
=====================

.. reference::

   :Panel:     :menuselection:`Particle System --> Force Fields Settings`

The Force Field Settings panel allows you to make each individual act as a force field,
allowing them to affect other dynamic systems, or even, each other.

Self Effect
   Causes the particle force fields to have an effect on other particles within the same system.
Effector Amount
   Set how many of the particles act as force fields. 0 means all of them are effectors.

You can give particle systems up to two force fields. By default they do not have any.
Choose an effector type from the selector to enable them.
Settings are described in the :ref:`Common Settings section <force-field-common-settings>`.
