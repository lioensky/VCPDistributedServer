.. index:: Grease Pencil Visual Effects

************
Introduction
************

.. reference::

   :Panel:     :menuselection:`Properties --> Visual Effects`

Grease Pencil has a special set of viewport real-time visual effects that can be apply to the object.

These effects treat the object as if it was just an image, for that reason they
have effect on the whole object and cannot limit their influence
on certain parts like layers, materials or vertex group as with modifiers.
Also unlike modifiers, they can not be applied to the object.

Their main purpose is to have a quick way to apply visual effects on your drawings
like blurring, pixelation, wave distortion, among others.

.. note::

   Visual Effects best fit for quick viewport visualization. You can use it for final renders
   but if you want more precision with effects it is still recommended to use
   the :doc:`Compositor </compositing/introduction>`.


Interface
=========

.. figure:: /images/grease-pencil_visual-effects_introduction_interface.png

   Panel layout (Blur effect as an example).

The visual effects panels and interface are similar to modifiers.
Each effect shares the same basic interface components similar to modifiers for meshes.

See :ref:`Modifiers Interface <bpy.types.Modifier.show>` for more information.
