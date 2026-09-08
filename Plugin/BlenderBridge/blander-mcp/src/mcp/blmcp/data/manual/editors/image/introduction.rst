.. index:: Editors; Image Editor

************
Introduction
************

The Image Editor lets you create, view, and edit images,
as well as see render results and intermediate
:doc:`Compositor </compositing/introduction>` output.

.. figure:: /images/editors_image_introduction_main.png

   Image Editor with a test grid texture.


Toolbar
=======

Sample
   Used to sample the color of one or more pixels in the image.
   As long as you hold :kbd:`LMB`, the footer will show the following:

   - X and Y coordinates of the mouse cursor.
   - Color in RGBA.
   - Color in RGB after :doc:`/render/color_management/index`.
   - Color in HSV.
   - Luminance.

   Sample Size
      The dimensions of the square used to sample underlying pixels.
      If larger than 1, the resulting sample is an average of all underlying pixels.

Annotate
   See :doc:`Annotations </interface/annotate_tool>` for more information.


Header
======

Mode
   :View: Displays images.
   :Paint: :doc:`/sculpt_paint/texture_paint/index`.
   :Mask: :doc:`/movie_clip/masking/index`.

View
   Tools for controlling how the content is displayed in the editor.
   See :doc:`/editors/image/navigating`.

Image
   Tools for opening and manipulating images. Shows an asterisk if the image
   has unsaved changes. See :doc:`/editors/image/editing`.

Image
   A :ref:`data-block menu <ui-data-block>` used for selecting images.
   Once an image is selected, the :doc:`Image tab </editors/image/image_settings>`
   appears in the Sidebar region.

   Apart from loading existing images, you can also create new ones:

   .. figure:: /images/editors_image_image-settings_generated-new-image.png

      The pop-over that's displayed when clicking "New Image" in the header.

   The *Tiled* option creates an image with support for
   :doc:`/modeling/meshes/uv/workflows/udims`. For the other options, see
   :ref:`Generated Images <image-generated>`.

   In addition to images, the data-block selector includes the following items:

   - Render Result: displays renders. When this item is selected, the *Slot*,
     *View Layer*, and *Render Pass* selectors become available (see below).
   - Viewer Node: displays the image that's fed into the
     :doc:`/compositing/types/output/viewer` in the Compositor.

Image Pin
   Prevents the Image Editor from automatically switching to the texture of
   the selected object. (This switching only happens if the 3D Viewport is
   in :doc:`Texture Paint </sculpt_paint/texture_paint/introduction>` mode).

.. _bpy.types.SpaceImageEditor.show_sequencer_scene:

Show Sequencer Scene
   This toggle is only visible on the Render Result if a :doc:`Sequencer Scene </video_editing/sequencer_scene>`
   exists, and it differs from the active scene in the window. After rendering, its state is chosen automatically from
   the render type. 

Slot
   The render slot to view (and render to). You can create new renders without
   losing previous ones by selecting an empty slot before rendering. Afterwards,
   you compare them by pressing :kbd:`J` and :kbd:`Alt-J` to cycle forwards and backwards.
   Alternatively, you can use the number keys :kbd:`1`, :kbd:`2`, :kbd:`3` etc.
   to select the slot with the corresponding number.

   Slots can be renamed by double clicking their name in the Image panel in the Sidebar.

View Layer
   The :doc:`View Layer </render/layers/introduction>` to display.

Render Pass
   The :doc:`Render Pass </render/layers/passes>` to display.

.. _bpy.types.SpaceImageEditor.show_gizmo:

Viewport Gizmos
   Lets you show/hide all gizmos using the toggle button, or specific gizmos using
   the drop-down arrow.

   .. _bpy.types.SpaceImageEditor.show_gizmo_navigate:

   Navigate
      Enable/disable the gizmos used to pan or zoom the 2D viewport.
      See :ref:`Navigation Gizmos <editors-image-navigate-gizmos>` for more information.

.. _bpy.types.SpaceImageEditor.display_channels:

Display Channels
   Select which color channels are displayed.

   :Color & Alpha:
      Enables transparency and shows a checkerboard behind the image.
   :Color:
      Disables transparency.
   :Alpha:
      Displays the alpha channel as a grayscale image. White areas are opaque,
      black areas are transparent.
   :Z-Buffer:
      Displays the depth from the camera, from Clip Start to Clip End,
      as specified in the :doc:`Camera settings </render/cameras>`.
   :Red, Green, Blue:
      Single color channel visualized as a grayscale image.


Asset Shelf Region
==================

Depending on the current mode, the asset shelf may be available, providing quick access to assets
for this specific mode (for example brush assets in *Paint* mode).

See :ref:`ui-region-asset_shelf` for more information.


Main View
=========

Holding :kbd:`RMB` will sample the image just like the Sample tool,
except it will always sample only one pixel.
