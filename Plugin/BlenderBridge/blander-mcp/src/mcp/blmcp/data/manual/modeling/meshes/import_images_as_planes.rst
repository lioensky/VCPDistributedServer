.. _bpy.ops.image.import_as_mesh_planes:

**********
Mesh Plane
**********

.. reference::

   :Menu:      :menuselection:`3D Viewport --> Add --> Image --> Mesh Plane`

The *Mesh Plane* operator automates the process of creating a plane,
sizing it to match the aspect ratio of the selected image, and applying a material with the image as a texture.
The plane, material, and texture are named based on the image filename.

This tool supports importing single images, multiple images, or image sequences/movie clips:

- **Single Image**: Creates one plane with the image applied as a texture.
- **Multiple Images**: Generates multiple planes, either stacked or spaced apart.
- **Image Sequence/Movie Clip**: Creates a single plane with the animated sequence applied.


Properties
==========

The current import settings can be saved as an :ref:`Operator Preset <ui-presets>`.


Options
-------

Relative Paths
   Stores the image file path relative to the currently open blend-file.
   See :ref:`files-blend-relative_paths`.

Force Reload
   Reloads the image file if it already exists as an image data-block.

Detect Image Sequences
   Imports sequentially numbered images as an animated
   :ref:`image sequence <image-sequence>` instead of separate planes.
   The frame range of the sequence is automatically set (which can be adjusted later).


Material
--------

A material is automatically created for the plane to display the imported image. The following shader options are
available:

Shader
   The type of node shader to use.

   :Principled:
      Uses a :doc:`Principled BSDF </render/shader_nodes/shader/principled>` shader.
      The imported image is linked to the *Base Color* input.
   :Shadeless:
      Creates a material that does not respond to lighting.
      Uses a mix of Diffuse and Emission shaders controlled by a Light Path node.
   :Emission:
      Similar to *Principled*, but links the image texture to the *Emission* input instead of *Base Color*.

      Emission Strength
         Adjusts the intensity of emission.

Render Method
   Controls the blending and the compatibility with certain features.
   See :ref:`Material Settings <bpy.types.Material.surface_render_method>` for more information.

   :Dithered:
      Allows for grayscale hashed transparency, and compatible with render passes and raytracing.
      Also know as deferred rendering.

      When using *Dithered* render method, the materials are rendered in layers.
      Each layer can only transmit (e.g. refract) light emitted from previous layers.
      If no intersection with the layers below exists, the transmissive BSDFs will fallback to light probes.
   :Blended:
      Allows the colored transparency, but incompatible with render passes and raytracing.
      Also known as forward rendering.

      Show Backface
         Displays the backface of transparent areas.

Backface Culling
   Hides the plane's backface.

Overwrite Material
   If an imported image shares a name with an existing material, Blender appends a number to differentiate it.
   Enabling this option forces the new material to overwrite the existing one.


Texture
-------

.. note::

   For a detailed explanation of each option, see :doc:`Image Texture Node </render/shader_nodes/textures/image>`.

Interpolation
   Defines how the image is scaled when displayed on the plane.

Extension
   Determines how the image is extrapolated beyond its original boundaries.

Alpha
   Enables transparency using the image's alpha channel.

Auto Refresh
   Automatically updates images in the viewport when the frame changes.


Transform
---------

Imported planes are positioned at the 3D Cursor's location. Multiple planes can be offset using the *Offset Planes*
option.

Size Mode
   Determines how the plane's size is set:

   :Absolute:
      The plane's height is explicitly defined in *Height*, with width adjusted to maintain aspect ratio.
      Example: An image of 800 × 600 pixels with a height of 1 m results in a width of 1.33 m.

      Height
         Sets the height of the plane.

   :Scale to Camera Frame:
      The plane is sized relative to the active camera.

      Scale
         Method to scale the plane with the camera frame.

         :Fit:
            Scales the plane to fit inside the camera frame while preserving aspect ratio.
         :Fill:
            Scales the plane to fill the entire camera frame, possibly cropping some areas.

   :Pixels per Inch:
      Determines the plane's size using the *Definition* value, measured in pixels per inch.
      Example: With a 600 DPI setting, an 800 × 600 px image results in a plane size of ~0.0339 × 0.0254 m.

      Definition
         Sets the number of pixels per inch.

   :Pixels per Blender Unit:
      Uses *Definition* to define pixels per Blender Unit.
      Example: With a setting of 600, an 800 × 600 px image results in a plane size of 1.33 × 1 BU.

      Definition
         Sets pixels per Blender Unit.

Align
   Specifies the plane's rotation upon import.

   :Z- (Down), Y-, X-, Z+ (Up), Y+, X+:
      Rotates the plane to align with the selected axis.
   :Face Camera:
      Directly faces the camera.
   :Camera's Main Axis:
      Aligns the plane to a major axis facing the camera view direction.

Track Camera :guilabel:`Face Camera` :guilabel:`Camera's Main Axis`
   Adds a :doc:`Locked Track </animation/constraints/tracking/locked_track>` constraint,
   ensuring the plane always faces the camera.
Offset Planes
   Offsets multiple planes instead of stacking them.

Offset Direction
   Specifies the axis along which multiple planes are spaced.

Distance
   Defines the spacing between planes.
