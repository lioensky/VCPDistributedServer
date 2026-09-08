
*********
UV Layout
*********

.. reference::

   :Category:  Import-Export
   :Menu:      :menuselection:`UV Editor --> UV --> Export UV Layout`


Enabling Add-on
===============

This add-on is enabled by default. In case it is not:

#. Open Blender and go to :doc:`/editors/preferences/addons` section of the :doc:`/editors/preferences/index`.
#. Search "UV Layout" and check the *Enable Add-on* checkbox.


Usage
=====

This add-on allows you to export a UV map as an image:
(:menuselection:`UV Editor --> UV --> Export UV Layout`)
It allows you to export to ``PNG``, ``EPS``, or ``SVG`` format.
The desired UV faces must be selected in the 3D View, not the UV Editor.

The image will be lines defining the UV edges that are within the default grid of the UV Editor.
Edges outside this boundary, even if selected, will not be shown in the saved graphic.

You can then bring this image into your favorite painting program, 
and use it as a transparent reference guide to create a texture.
Then export that image and load it back into Blender as part of a material set-up.
For using images as textures, see the page on
:doc:`Image Textures </render/materials/legacy_textures/types/image_movie>`.

.. list-table::

   * - .. figure:: /images/addons_import-export_mesh-uv-layout_uv-editor.png
          :width: 320px

          A UV layout in the UV Editor.

     - .. figure:: /images/addons_import-export_mesh-uv-layout_export.png
          :width: 320px

          A UV layout in a paint program.


Properties
==========

.. figure:: /images/addons_import-export_mesh-uv-layout_export-panel.png

   Export options.

All UVs
   Export all UVs rather than only what is selected in the 3D View.
Export Tiles
   Choose whether to export only the [0,1] range, or all UV tiles
Modified
   Export UVs from the mesh with all its modifiers evaluated.
Format
   Image file format to save to (``.png``, ``.eps``, ``.svg``).
Size
   The size of the exported image in pixels.
Fill Opacity
   Set the opacity of the fill.
