
****************
Viewport Display
****************

.. reference::

   :Mode:      Object Mode
   :Panel:     :menuselection:`Properties --> Object Properties --> Viewport Display`

This panel lets you configure display options for the 3D Viewport.

.. figure:: /images/scene-layout_object_properties_display_panel.png

   Viewport Display panel.

.. _bpy.types.Object.show:

Show
   Name
      Displays the object's name in the 3D Viewport.
   Axes
      Displays an object similar to an empty that shows the object's orientation.
   Wireframe
      Displays the object's wireframe on top of the solid display.
   All Edges
      Displays all wireframe edges. This overrides the
      :ref:`wireframe threshold <bpy.types.View3DOverlay.wireframe_threshold>`
      that you can set in the 3D Viewport's overlay settings.

   .. _bpy.types.Object.show_texture_space:

   Texture Space
      Displays the object's :term:`Texture Space` in the 3D Viewport..
      The texture space overlay can be disabled for all objects using the
      :ref:`Extras Overlay <bpy.types.View3DOverlay.show_extras>`.
   Shadow
      Allows the object to cast shadows in the viewport.

   .. _bpy.types.Object.show_in_front:

   In Front
      Makes the object display in front of others. Unsupported for instanced objects.
      Limited support in the *Material Preview* and *Rendered* shading modes
      (works for e.g. armatures, but not for meshes).

.. _bpy.types.Object.display_type:

Display As
   Lets you display the object with less detail, going from removing the textures to
   only showing a bounding box. This can be useful if you have a high-poly object
   that is slowing down the viewport.

.. _bpy.types.Object.color:

Color
   The object's color in the *Wireframe* and *Solid* viewport shading modes.
   Used when the viewport's :ref:`(Wire) Color <viewport_shading_solid_color>`
   shading option is set to *Object*.

.. _bpy.types.Object.show_bounds:
.. _bpy.types.Object.display_bounds_type:

Bounds
   Displays a bounding shape around an object. You can choose between different
   primitive shapes that might be closer to what the original object looks like.
