.. _bpy.types.Scene.gravity:

*******
Gravity
*******

.. reference::

   :Panel:     :menuselection:`Scene --> Gravity`

Gravity is a global setting that is applied to all physics systems in a scene.
It can be found in the scene tab.
This value is generally fine left at its default, -9.810 on the Z axis,
which is the force of gravity in the real world.
Changing this value would simulate a lower or higher force of gravity.
Gravity denoted g, measurement *m* × *s*\ :sup:`-2`.

Gravity is applied in the same way to all physics systems.

Gravity is practically the same around the entirety of planet *Earth*.
For rendering scenes on The Moon, use -1.622 *m* × *s*\ :sup:`-2` on the Z axis.
Another popular gravity value might be for Mars which
has a gravitation acceleration of -3.69 *m* × *s*\ :sup:`-2` on the Z Axis.

.. note::

   The gravity value per physics system can be scaled down in the *Field Weights* tab.
