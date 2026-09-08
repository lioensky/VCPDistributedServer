
**************
Onion Skinning
**************

Onion Skinning show ghosts of the keyframes before and after the current frame allowing animators
to make decisions in the animation sequence.

The main switch to show/hide Onion Skinning is in the :ref:`Viewport Overlays <3dview-overlay-grease-pencil>`,
but Grease Pencil Onion Skinning is per-layer and the visibility can be toggle in the layer list.
See :doc:`2D Layers </grease_pencil/properties/layers>` for more information.

.. figure:: /images/grease-pencil_properties_onion-skinning_panel.png
   :align: right

   Onion Skinning panel.


Options
=======

.. _bpy.types.GreasePencil.onion_mode:

Mode
   :Keyframes: Shows Keyframes in the range determined by the *Before*/*After* settings.
   :Frames: Shows Frames in the range determined by the *Before*/*After* settings.
   :Selected: Shows only on the manually selected keyframes in the Dope Sheet.

.. _bpy.types.GreasePencil.onion_factor:

Opacity
   Control the opacity of the ghost frames.

.. _bpy.types.GreasePencil.onion_keyframe_type:

Filter by Type
   Filters what type of frames to show in the Onion Skinning range.

.. _bpy.types.GreasePencil.ghost_before_range:
.. _bpy.types.GreasePencil.ghost_after_range:

Keyframes Before/After
   Sets how many frames or keyframes, depending on the *Mode*, to show before and after the current frame.


Custom Colors
=============

.. _bpy.types.GreasePencil.before_color:
.. _bpy.types.GreasePencil.after_color:

Before/After
   Color to use before and after the current frame on ghost frames.


Display
=======

.. _bpy.types.GreasePencil.use_onion_fade:

Fade
   Opacity of the ghosts frames decrease the further away from the current frame.

.. _bpy.types.GreasePencil.use_onion_loop:

Show Start Frame
   Help working on loop animations showing the first keyframe/frame
   as ghost when you are on the last frame of your animation.

.. figure:: /images/grease-pencil_properties_onion-skinning_example.png

   An example of Onion Skinning activated.
