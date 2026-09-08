.. _bpy.types.Bone.color:
.. _bpy.types.EditBone.color:
.. _bpy.types.PoseBone.color:

****************
Viewport Display
****************

.. reference::

   :Mode:      Object, Pose, and Edit Mode
   :Panel:     :menuselection:`Bone --> Viewport Display`

This panel lets you customize the look of your bones.

.. figure:: /images/animation_armatures_bones_properties_display.png

   Viewport Display panel in Object/Pose mode.

.. figure:: /images/animation_armatures_bones_properties_display_editmode.png

   Viewport Display panel in Edit mode.

General
=======

.. _bpy.types.Bone.hide:

Hide
   Hides the bone in the 3D Viewport. When this is unchecked, the bone's
   visibility is determined by the visibility of its :ref:`bone collections <bpy.types.Bone.collections>`.

.. _bpy.types.Bone.display_type:

Display As
   This controls the way the selected bones appear in the 3D Viewport.
   This overrides the :ref:`Display Type <bpy.types.Armature.display_type>` of the armature.

   .. list-table::

      * - .. figure:: /images/animation_armatures_properties_display_octahedral.png
             :width: 320px

             Octahedral bone display.

        - .. figure:: /images/animation_armatures_properties_display_stick.png
             :width: 320px

             Stick bone display.

      * - .. figure:: /images/animation_armatures_properties_display_b-bone.png
             :width: 320px

             B-Bone bone display.

        - .. figure:: /images/animation_armatures_properties_display_envelope.png
             :width: 320px

             Envelope bone display.

   :Armature Defined: Use display mode from armature.
   :Octahedral: Display bones as octahedral shape.
   :Stick: Display bones as simple 2D lines with dots.
   :B-Bone: Display bones as boxes, showing subdivision and B-Splines.
   :Envelope: Display bones as extruded spheres, showing deformation influence volume.
   :Wire: Display bones as thin wires, showing subdivision and B-Splines.

.. _bpy.types.BoneColor.palette:
.. _bpy.types.BoneColor:
.. _bpy.types.ThemeBoneColorSet:

Bone Colors
===========

Bones can be individually colored. You can either choose a color set from the predefined
:ref:`theme <bpy.types.Theme>` list or define a custom one.

.. figure:: /images/animation_armatures_bones_properties_display_custom_colors.png

When selecting *Custom Color Set*, you need to define three colors:
Regular (for when the bone is not selected), Selected, and Active.

You can temporarily disable all the color assignments by unchecking
:ref:`Bone Colors <bpy.types.Armature.show>` in the armature's Viewport Display panel.

Bone Color
   The bone's primary color, affecting both Edit Mode and Pose Mode.

   This color is stored on the armature data-block, so that if you have
   multiple armature objects that share this data-block, they will all use
   the same color.

   .. _bpy.ops.armature.copy_bone_color_to_selected:

   Copy Bone Color to Selected
      Copy the bone color of the :term:`Active` bone to all selected bones.

Pose Bone Color :guilabel:`Pose Mode`
   Lets you optionally override the above *Bone Color* in Pose Mode
   (by setting it to something else than *Default Colors*).

   This color is stored on the :term:`Pose Bone`, meaning it can be different
   in every armature object -- even ones that reference the same data-block.

   Copy Bone Color to Selected
      Copy the bone color of the :term:`Active` bone to all selected bones.


.. _bpy.types.PoseBone.custom_shape:

Custom Shape
============

Apart from custom colors, bones can also have custom shapes (in *Object Mode*
and *Pose Mode*), using another object as a "template."

.. figure:: /images/animation_armatures_bones_properties_display_custom-shape-example.png

   A bone referencing a cone as its Custom Shape.

You can temporarily disable these shapes by unchecking
*Shapes* in the armature's Viewport Display panel.

Custom Object
   Object that defines the custom shape of the selected bone.

Translation X, Y, Z
   Additional translation to apply to the custom shape.

Rotation X, Y, Z
   Additional rotation to apply to the custom shape.

Scale X, Y, Z
   Additional scaling factor to apply to the custom shape.

Override Transform
   A bone that defines the display transform of the custom shape. 
   The shape defined in *Custom Object* will be placed at the location and orientation of that bone.
   This is only visual and does not affect the transform values of this bone.

Affect Gizmo
   The location and orientation of the *Override Transform* bone will be used for transform
   gizmos and for other transform operators in the 3D Viewport.

Use As Pivot
   Transform the bone as if it was a child of the *Override Transform* bone.
   This is useful in special cases, where the mesh is deformed away from the bind pose by
   a separate mechanism, for example :ref:`Shape Keys <animation-shape_keys-index>`.

   .. note::

      While this affects gizmo interaction, it does not change the transform values
      of the bone, or how they are interpolated. As such the interpolation may not
      work as expected.

.. _bpy.types.PoseBone.use_custom_shape_bone_size:

Scale to Bone Length
   Whether the custom shape should be scaled by a factor
   equal to the :ref:`bone's length <bpy.types.EditBone.length>`.

.. _bpy.types.Bone.show_wire:

Wireframe
   When enabled, the bone is displayed in wireframe mode regardless of the viewport's shading mode.

.. _bpy.types.PoseBone.custom_shape_wire_width:

Wire Width
   The line thickness of the wireframe for the custom shape.

.. note::

   - Custom shapes will never be rendered. Like regular bones, they are only visible in the 3D Viewport.
   - The transforms of the template object are ignored. Moving, rotating, or scaling it will have no
     effect on its appearance in the armature.
   - The origin of each instanced shape object is at the :doc:`root </animation/armatures/bones/structure>`
     of the bone.
   - The rotation of each shape object is such that its Y axis lies along the direction of the bone.
   - For best results when :ref:`Scale to Bone Length <bpy.types.PoseBone.use_custom_shape_bone_size>` is enabled,
     make sure the template object is 1 unit in size along its Y axis.
     This will make it perfectly match the size of each bone.
