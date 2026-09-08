
*********************************
Grease Pencil Material Properties
*********************************

.. _gp-material-slots:

Material Slots
==============

.. figure:: /images/grease-pencil_materials_introduction_slots-panel.png
   :align: right

   Grease Pencil material slots panel.

Next to the material name there are three icons buttons that control common properties of the material:

.. _bpy.types.MaterialGPencilStyle.ghost:

:bl-icon:`onionskin_on` /:bl-icon:`onionskin_off` (Show/Hide in Ghosts)
   Toggle the use of the material for :doc:`Onion Skinning </grease_pencil/properties/onion_skinning>`.

.. _bpy.types.MaterialGPencilStyle.hide:

:bl-icon:`hide_off` / :bl-icon:`hide_on` (Hide/Show Material)
   Toggle whether the active material is the only one that can be edited and is visible.

.. _bpy.types.MaterialGPencilStyle.lock:

:bl-icon:`unlocked` / :bl-icon:`locked` (Lock/Unlock Material)
   Toggle whether the active material is the only one that can be edited.


Specials
--------

.. _bpy.ops.grease_pencil.material_reveal:

Show All
   Turns on the visibility of every material in the list.

.. _bpy.ops.grease_pencil.material_hide:

Hide Others
   Turns off the visibility of every material in the list except the active one.

.. _bpy.ops.grease_pencil.material_lock_all:

Lock All
   Locks editing of all the materials in the list.

.. _bpy.ops.grease_pencil.material_unlock_all:

Unlock All
   Unlocks editing of all the materials in the list.

.. _bpy.ops.grease_pencil.material_lock_unselected:

Lock Unselected
   Locks all materials not used in the selected strokes.

.. _bpy.ops.grease_pencil.material_lock_unused:

Lock Unused
   Locks and hides all unused materials.

.. _bpy.ops.grease_pencil.material_copy_to_object:

Copy Material to Selected
   Copy the active material to the selected Grease Pencil object.

Copy All Materials to Selected
   Copy all materials to the selected Grease Pencil object.

Remove Unused Slots
   Remove all unused materials.


Lock & Visibility Controls
--------------------------

.. _bpy.ops.grease_pencil.material_isolate:

:bl-icon:`locked` (Isolate Material)
    Toggle whether the active material is the only one that can be edited.
:bl-icon:`restrict_view_on` (Isolate Material)
    Toggle whether the active material is the only one that can be edited and is visible.


.. _gp-material-surface:

Surface
=======

.. figure:: /images/grease-pencil_materials_properties_panel.png
   :align: right

   Shader panel with only Stroke component activated.


.. _bpy.types.MaterialGPencilStyle.show_stroke:

Stroke
------

When enabled, the shader use the stroke component.
The *Stroke* component controls how to render the edit lines.

.. _bpy.types.MaterialGPencilStyle.mode:

Line Type
   Defines how to display or distribute the output material over the stroke.

   :Line:
      Connects every points in the strokes showing a continuous line.
   :Dots:
      Use a disk shape at each point in the stroke.
      The dots are not connected.
   :Squares:
      Use a square shape at each point in the stroke.
      The squares are not connected.

.. _bpy.types.MaterialGPencilStyle.stroke_style:

Style
   The type of the material.

   :Solid:
      Use a solid color.
   :Texture:
      Use an image texture.

      Image
         The image data-block used as an image source.

      Blend
         Texture and Base Color mixing amount.

      UV Factor
         The image size along the stroke.

.. _bpy.types.MaterialGPencilStyle.color:

Base Color
   The base color of the stroke.

.. _bpy.types.MaterialGPencilStyle.use_stroke_holdout:

Holdout
   Removes the color from strokes underneath the current by using it as a mask.

.. _bpy.types.MaterialGPencilStyle.alignment_mode:

Alignment
   Defines how to align the *Dots* and *Squares* along the drawing path and with the object's rotation.

   :Path:
      Aligns to the drawing path and the object's rotation.
   :Object:
      Aligns to the object's rotation; ignoring the drawing path.
   :Fixed:
      Aligns to the screen space; ignoring the drawing path and the object's rotation.

.. _bpy.types.MaterialGPencilStyle.alignment_rotation:

Rotation
   Rotates the points of *Dot* and *Square* strokes.

   .. note::

      The *Rotation* option is limited to a range of -90 to 90 degrees.

.. _bpy.types.MaterialGPencilStyle.use_overlap_strokes:

Self Overlap
   Disables stencil and overlap self-intersections with alpha materials.

.. list-table:: Samples of different material strokes mode types and styles.

   * - .. figure:: /images/grease-pencil_materials_properties_stroke-solid-line.png
          :width: 130px

          Mode Type: Line, Style: Solid.

     - .. figure:: /images/grease-pencil_materials_properties_stroke-texture-line.png
          :width: 130px

          Mode Type: Line, Style: Texture.

     - .. figure:: /images/grease-pencil_materials_properties_stroke-solid-dot.png
          :width: 130px

          Mode Type: Dot, Style: Solid.

     - .. figure:: /images/grease-pencil_materials_properties_stroke-texture-dot.png
          :width: 130px

          Mode Type: Dot, Style: Texture.


.. _bpy.types.MaterialGPencilStyle.show_fill:

Fill
----

When enabled, the shader use the fill component.
The *Fill* component control how to render the filled areas determined by closed edit lines.

.. _bpy.types.MaterialGPencilStyle.fill_style:

Style
   The type of material.

   :Solid:
      Use solid color.
   :Gradient:
      Use a color gradient.

      .. _bpy.types.MaterialGPencilStyle.gradient_type:

      Gradient Type
         :Linear: Mix the colors along a single axis.
         :Radial: Mix the colors radiating from a center point.

   :Texture:
      Use an image texture.

      .. _bpy.types.MaterialGPencilStyle.fill_image:

      Image
         The image data-block used as an image source.

   .. list-table:: Samples of different material fill styles.

      * - .. figure:: /images/grease-pencil_materials_properties_fill-solid.png
             :width: 130px

             Style: Solid.

        - .. figure:: /images/grease-pencil_materials_properties_fill-gradient.png
             :width: 130px

             Style: Gradient (Linear).

        - .. figure:: /images/grease-pencil_materials_properties_fill-gradient-radial.png
             :width: 130px

             Style: Gradient (Radial).

        - .. figure:: /images/grease-pencil_materials_properties_fill-texture.png
             :width: 130px

             Style: Texture.

.. _bpy.types.MaterialGPencilStyle.fill_color:

Base Color
   The base color of the fill.

.. _bpy.types.MaterialGPencilStyle.mix_color:

Secondary Color :guilabel:`Gradient`
   The secondary color.

.. _bpy.types.MaterialGPencilStyle.use_fill_holdout:

Holdout
   Removes the color from strokes underneath the current by using it as a mask.

.. _bpy.types.MaterialGPencilStyle.mix_factor:

Blend :guilabel:`Gradient / Texture`
   The amount that the *Secondary Color* (for *Gradient Style*) or image texture (for Texture Style) mixes with the
   *Base Color*.

.. _bpy.types.MaterialGPencilStyle.flip:

Flip Colors :guilabel:`Gradient`
   Flips the gradient, inverting the Base Color and *Secondary Color*.

.. _bpy.types.MaterialGPencilStyle.texture_offset:

Location X, Y :guilabel:`Gradient / Texture`
   Shifts the position of gradient or image texture.

.. _bpy.types.MaterialGPencilStyle.texture_angle:

Rotation :guilabel:`Gradient / Texture`
   Rotates the gradient or image texture.

.. _bpy.types.MaterialGPencilStyle.texture_scale:

Scale X, Y :guilabel:`Gradient / Texture`
   Scales the gradient or image texture.

.. _bpy.types.MaterialGPencilStyle.texture_clamp:

Clip Image :guilabel:`Texture`
   When enabled, show one image instance only (do not repeat).


.. _gp-material-settings:

Settings
========

.. _bpy.types.MaterialGPencilStyle.pass_index:

Pass Index
   This index can be used with some modifiers to restrict changes to only a certain material.
   See :doc:`Modifiers </grease_pencil/modifiers/introduction>` for more information.
