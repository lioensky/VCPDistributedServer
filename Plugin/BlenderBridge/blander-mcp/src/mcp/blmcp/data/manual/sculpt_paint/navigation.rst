
*************************
Navigating in Paint Modes
*************************

There are different preferences for navigating the 3D Viewport in Blender.
For painting and sculpting specific workflows it is recommended to use any of the following methods.

Center View to Mouse :kbd:`Alt MMB`
   Center the View on the surface directly under the mouse position.
   This way the rotation point of the viewport can be manually changed to any point you wish to orbit around.

Center on Last Stroke :kbd:`NumpadPeriod`
   Center the View on the average position of the last stroke.

Various preferences can also make navigation more convenient.
These can be found in the "Navigation" tab of the preferences.

Orbit Method = Trackball
   Tumble the view based on the mouse position in your 3D Viewport while rotating.
   This makes it very easy to tilt the viewport freely,
   instead of having the Z axis of the viewport locked.

.. Needs a visual example to make it easier to understand.

:ref:`Zoom to Mouse Position <bpy.types.PreferencesInput.use_zoom_to_mouse>`
   Use the mouse position to zoom towards and rotate around the surface that is pointed at.
   This can be an alternative to the repeated manual use of the Center View to Mouse operator.

   The disadvantage is that this navigation preference can lead to accidental navigation
   around backfacing geometry or very distant geometry.

.. Needs a visual reference of where to find both.
