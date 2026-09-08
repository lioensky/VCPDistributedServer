.. index:: Editors
.. _bpy.types.Space:
.. _bpy.ops.screen.space_type_set_or_cycle:

###########
  Editors
###########

Blender provides a number of different editors for displaying and modifying different aspects of data.
An Editor is contained inside an :doc:`Area </interface/window_system/areas>`
which determines its size and placement within the Blender window.
Every area may contain any type of editor.

The *Editor Type* selector, the first button at the left side of a header,
allows you to change the Editor in that area.
It is also possible to open the same Editor type in different areas at the same time.

See :doc:`User Interface </interface/index>` for documentation on the general interface.

.. figure:: /images/editors_index_menu.png
   :align: center

   The Editor Type selector.


General
=======

.. toctree::
   :maxdepth: 1

   3dview/index.rst
   image/index.rst
   uv/index.rst
   compositor.rst
   texture_node/index.rst
   geometry_node.rst
   shader_editor.rst
   video_sequencer/index.rst
   clip/index.rst


Animation
=========

.. toctree::
   :maxdepth: 1

   dope_sheet/index.rst
   timeline.rst
   graph_editor/index.rst
   drivers_editor.rst
   nla/index.rst


Scripting
=========

.. toctree::
   :maxdepth: 1

   text_editor.rst
   python_console.rst
   info_editor.rst


Data
====

.. toctree::
   :maxdepth: 1

   outliner/index.rst
   properties_editor.rst
   file_browser.rst
   asset_browser.rst
   spreadsheet.rst
   preferences/index.rst
