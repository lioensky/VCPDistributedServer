********
Clamping
********

.. reference::

   :Panel:     :menuselection:`Render --> Clamping`


Surface
=======

.. _bpy.types.SceneEEVEE.clamp_surface_direct:

Direct Light
   This option limits the maximum light intensity a surface can reflect.
   It reduces :term:`Aliasing` noise and :term:`Fireflies` at the cost of accuracy.
   Setting this option to 0.0 disables clamping altogether.
   Lower values have a greater effect on the resulting image than higher values.

.. _bpy.types.SceneEEVEE.clamp_surface_indirect:

Indirect Light
   Similar to **Direct Light** but limits the maximum light intensity reflected using ray-tracing and light-probes.
   This also limits the intensity of the world lighting since it is considered as indirect light.

.. note::

    These options provide a way to limit :term:`Fireflies` and :term:`Aliasing`
    of highly reflective surfaces and dense volumes.
    However, note that as you clamp out such values, other bright lights will be dimmed as well.

    Care must be taken when using this setting to find a balance between mitigating fireflies and
    losing intentionally bright parts.


Volume
======

.. _bpy.types.SceneEEVEE.clamp_volume_direct:

Direct Light
   The same as *Surface Direct Light* but for volume direct lighting.

.. _bpy.types.SceneEEVEE.clamp_volume_indirect:

Indirect Light
   The same as *Surface Direct Light* but for volume indirect lighting.
