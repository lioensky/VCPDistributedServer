.. index:: Editors; Shader Editor

*************
Shader Editor
*************

The Shader Editor is used to edit materials which are used for :doc:`rendering </render/index>`.
Materials used by Cycles and EEVEE are defined using a node tree.
Therefore, the main window of the Shader editor is a :doc:`node editor </interface/controls/nodes/index>`.

.. figure:: /images/editors_shader-editor_main.png

   Shader Editor with the default material node tree.

A list of all :doc:`shader nodes </render/shader_nodes/index>` is available in the rendering section.


Header
======

.. _bpy.types.SpaceNodeEditor.shader_type:

Shader Type
   The type of data whose shader nodes are being edited:

   :Object:
      Edit shader nodes for the active object's :doc:`Material </render/materials/index>`.
   :World:
      Edit shader nodes for the :doc:`World background </render/lights/world>`.
   :Line Style:
      Edit shader nodes for Freestyle :doc:`Line Styles </render/freestyle/view_layer/line_style/index>`

Use Nodes :guilabel:`Line Style`
   Use shader nodes to define the texture for the freestyle line style.

Slot
   The *Slot* menu can be used to select
   the active :ref:`material slot <bpy.types.MaterialSlot>` on the active object.
   The material selector to the right of it can change the material that is in the selected slot.
:bl-icon:`unpinned` / :bl-icon:`pinned` Pinned
   Keeps the current material selection visible in the Shader editor
   even when another object or material is selected elsewhere.


Sidebar
=======

Options
-------

The Options panel in the Sidebar region contains the same :doc:`settings </render/materials/settings>`
that are also available in the Material tab in the Properties.
They differ depending on the selected render engine.
The settings are duplicated to make it possible to edit the entire material from the Shader editor.
