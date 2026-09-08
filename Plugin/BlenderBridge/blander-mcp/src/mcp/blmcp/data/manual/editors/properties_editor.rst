.. index:: Editors; Properties
.. _bpy.types.SpaceProperties:

*****************
Properties Editor
*****************

.. figure:: /images/editors_properties-editor_interface.png
   :align: right

   The Properties editor.

The Properties editor displays settings for the active scene, object, material, and other data types.
It provides access to a wide range of context-sensitive properties used throughout Blender.


Navigation Bar
==============

Properties are grouped into tabs, shown as a vertical list of icons in the Navigation Bar region of the editor.

The Navigation Bar can be flipped to the left or right of the editor by :kbd:`RMB` on the region and selecting
:menuselection:`Navigation Bar --> Flip to Left/Right`.

To hide the Navigation Bar, :kbd:`RMB` on the region and select :menuselection:`Navigation Bar --> Hide`.
Use the region toggle icon as described in :ref:`bpy.ops.screen.region_blend`.


.. _properties-tool-tab:

Active Tool and Workspace Settings
----------------------------------

This first tab contains settings for the active :doc:`tool </editors/3dview/toolbar/index>` (in the 3D Viewport)
and the current :doc:`workspace </interface/window_system/workspaces>`.


Scene
-----

Tabs related to the active scene:

.. _properties-render-tab:

- Render: :doc:`EEVEE </render/eevee/index>`,
  :doc:`Cycles </render/cycles/render_settings/index>`, or
  :doc:`Workbench </render/workbench/index>` settings.
- :doc:`Output </render/output/index>`
- :doc:`View Layer </render/layers/index>`
- :doc:`Scene </scene_layout/scene/properties>`
- :doc:`World </render/lights/world>`


Collection
----------

Settings for the active :ref:`Collection <scene-layout_collections_collections_tab>`.


.. _properties-data-tabs:

Object
------

Tabs related to the active object. Some are only shown for certain object types.

- :doc:`Object </scene_layout/object/properties/index>`
- :doc:`Modifiers </modeling/modifiers/index>` (or :doc:`Grease Pencil Modifiers </grease_pencil/modifiers/index>`)
- :doc:`Effects </grease_pencil/visual_effects/index>`
- :doc:`Particles </physics/particles/index>`
- :doc:`Physics </physics/index>`
- :doc:`Object Constraints </animation/constraints/index>`


Object Data
-----------

The *Object Data* tab name remains constant, but its icon changes depending on the object type.

.. rubric:: Geometry Objects

- :doc:`Mesh </modeling/meshes/properties/object_data>`
- :doc:`Curve </modeling/curves/properties/index>`
- :doc:`Surface </modeling/surfaces/properties/index>`
- :doc:`Text </modeling/texts/properties>`
- :doc:`Metaball </modeling/metas/properties>`
- :doc:`Grease Pencil </grease_pencil/properties/index>`

.. rubric:: Rigging and Deformation Objects

- :doc:`Armature </animation/armatures/properties/index>`

  - :doc:`Bone </animation/armatures/bones/properties/index>`
  - :doc:`Bone Constraints </animation/armatures/posing/bone_constraints/index>`

- :doc:`Lattice </animation/lattice>`

.. rubric:: Other Object Types

- :doc:`Empty </modeling/empties>`
- :doc:`Speaker </render/output/audio/speaker>`
- :doc:`Camera </render/cameras>`
- :doc:`Light </render/lights/light_object>`
- :doc:`Light Probe </render/eevee/light_probes/index>`


Object Shading
--------------

Tabs related to an object's visual appearance. Shown only when relevant.

- :doc:`Material </render/materials/index>`
- :doc:`Texture </render/materials/legacy_textures/index>`


Strips
------

Tabs related to video editing strips. Shown only when relevant.

- :doc:`Strip Modifiers </video_editing/edit/montage/strip_modifiers>`
- :doc:`Strip Properties </video_editing/edit/montage/strips/strip_properties>`


.. _bpy.types.SpaceProperties.show_properties:

Visible Tabs
------------

Allows hiding specific tabs in the Properties editor.

This is especially useful for tailoring the editor to specific workflows. For example:
- In the *Video Editing* workspace, you may hide object and shading tabs to reduce clutter.
- In the *Modeling* workspace, you may hide strip-related tabs that are not relevant.

Hidden tabs can be restored at any time using this filter list.


Header
======

.. figure:: /images/editors_properties-editor_top.png

   The header of the Properties editor.

.. _bpy.types.SpaceProperties.search_filter:

Display Filter :kbd:`Ctrl-F`
   Use this to search for properties by name. Matching properties remain visible; others are grayed out.
   The editor also highlights the first match and switches to the relevant tab automatically.

   Start a search with :kbd:`Ctrl-F`, and clear it with :kbd:`Alt-F`.

Data Context Path
   Displays the name and icon of the current data-block (e.g. Object, Material, Scene), along with its hierarchical
   path within the data structure.
   Example: *Cube* (Object) --> *Mesh* --> *Material*

.. _bpy.ops.buttons.toggle_pin:

Toggle Pin ID
   Click the pin icon to lock the editor to the current data-block, preventing it from changing when the selection
   updates. Click again to unlock and return to context-based display.


Options
-------

These options are accessible from the :menuselection:`Options` popover in the top-right corner of the editor.

.. _bpy.types.SpaceProperties.outliner_sync:

Sync with Outliner
   Controls whether clicking icons in the :doc:`Outliner </editors/outliner/introduction>` changes the active tab.

   :Always: Always follow the clicked Outliner icon.
   :Never: Ignore Outliner interaction.
   :Auto: Only follow when the Properties editor shares a border with the Outliner.
