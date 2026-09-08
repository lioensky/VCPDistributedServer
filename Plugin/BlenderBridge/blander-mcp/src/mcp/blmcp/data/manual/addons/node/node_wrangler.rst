
*************
Node Wrangler
*************

Node Wrangler provides various tools that help you to work with nodes quickly and efficiently.

While many of this add-on's functions work in all supported node editors (Compositor, Shader, Geometry Nodes,
and Texture Nodes) some functions only work in specific node editors, and some functions work differently per
editor.
Functions that only work in specific editors are marked with labels (:guilabel:`Compositor`, :guilabel:`Shader`,
:guilabel:`Geometry Nodes`, :guilabel:`Texture Nodes`). Functions without labels should work for all node editors.


Enabling Add-on
===============

#. Open Blender and go to :doc:`/editors/preferences/addons` section of the :doc:`/editors/preferences/index`.
#. Search "Node Wrangler" and check the *Enable Add-on* checkbox.


Usage
=====

Use the panel in Sidebar of the node editor or press :kbd:`Shift-W` to bring up the quick access menu. You can also
look up the shortcut list in the add-on preferences panel.

.. figure:: /images/addons_node_node-wrangler_menu.png

   You can access most functions from the sidebar panel or quick access menu.


Description
===========

Lazy Connect
------------

.. reference::

   :Shortcut:  :kbd:`Alt-RMB`-drag, :kbd:`Shift-Alt-RMB`-drag

Connect two nodes without even clicking the sockets. Just drag the cursor from one node to another while
holding :kbd:`Alt-RMB`.
It will select the nodes nearest the start and end points of the drag for connection, so you don't even have
to click on the nodes.

.. figure:: /images/addons_node_node-wrangler_lazy-connect.png

   Selection can be lazy.

It tries to connect the best-matched sockets possible, based on their names, types, and whether they are
open or not.

For a more precise connection, you can alternatively use :kbd:`Shift-Alt-RMB`. It brings up menus of
available inputs and outputs before connection, so you can select the exact sockets to connect.
It's especially useful when working with a large node tree since you can make connections without
frequently zooming in and out.


Lazy Mix
--------

.. reference::

   :Shortcut:  :kbd:`Shift-Ctrl-RMB`-drag

Connect the outputs of two nodes into an appropriate "mix" type of node. This is the "lazy" way of selecting
nodes and executing the *Mix* function from `Merge with Automatic Type Detection`_.


Merge
-----

.. reference::

   :Menu:   :menuselection:`Node Wrangler --> Merge Selected Nodes`

Connect outputs of the selected nodes into a "mix" type of node (Mix, Math, Z-Combine, Alpha Over, Mix Shader, Add
Shader, Join Geometry).

.. note::

   Merge currently does not support outputs of Integer, String, or Boolean types from Geometry Nodes.

There are automatic and manual ways of merging. The automatic ways let the add-on determine which "mix" node
to use based on the types of outputs to merge. The manual ways let you decide and force connections even if the
types of outputs and the "mix" node are not compatible.

.. note::

   Generally, the modifier part of the shortcut signifies the type of "mix" node you want to use (:kbd:`Ctrl`
   for automatic detection, :kbd:`Ctrl-Alt` for the Mix node, and :kbd:`Shift-Ctrl` for the Math node),
   the non-modifier part signifies the mode of "mix" node you want to set (:kbd:`NumpadPlus` for add,
   :kbd:`NumpadMinus` for subtract, :kbd:`NumpadSlash` for divide, and :kbd:`NumpadAsterisk` for multiply).


Merge with Automatic Type Detection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The automatic merge functions determine the type of "mix" node to use based on the types of outputs to merge. If
it has a Color output, it will use the Mix node. It will use the Math node if both outputs are of Value type.
Add Shader, Mix Shader, and Join Geometry nodes will also be used for specific cases.

Modes
   Add :kbd:`Ctrl-=`, :kbd:`Ctrl-NumpadPlus`
      Merge into Mix or Math nodes, then set blend mode or math operation as Add. If the outputs are Shaders,
      it will use Add Shader node instead.
   Multiply :kbd:`Ctrl-8`, :kbd:`Ctrl-NumpadAsterisk`
      Merge into Mix or Math nodes, then set blend mode or math operation as Multiply.
   Subtract :kbd:`Ctrl-Minus`, :kbd:`Ctrl-NumpadMinus`
      Merge into Mix or Math nodes, then set blend mode or math operation as Subtract.
   Divide :kbd:`Ctrl-Slash`, :kbd:`Ctrl-NumpadSlash`
      Merge into Mix or Math nodes, then set blend mode or math operation as Divide.
   Mix :kbd:`Ctrl-0`, :kbd:`Ctrl-Numpad0`
      Merge into Mix node, then set blend mode as Mix. If the outputs are Shaders, it will use Mix Shader node
      instead. If the outputs are Geometry, it will use Join Geometry node.


Merge Using Mix Node
^^^^^^^^^^^^^^^^^^^^

.. reference::

   :Menu:   :menuselection:`Node Wrangler --> Merge Selected Nodes --> Use Mix Nodes`

Use the Mix nodes for merging, regardless of the selected nodes. You can choose the mode of the node via the menu.
You can quickly set some operations by using corresponding shortcuts.

- Add: :kbd:`Ctrl-Alt-=`, :kbd:`Ctrl-Alt-=`
- Subtract: :kbd:`Ctrl-Alt-Minus`, :kbd:`Ctrl-Alt-NumpadMinus`
- Multiply: :kbd:`Ctrl-Alt-8`, :kbd:`Ctrl-Alt-NumpadAsterisk`
- Divide: :kbd:`Ctrl-Alt-Slash`, :kbd:`Ctrl-Alt-NumpadSlash`


Merge Using Math Node
^^^^^^^^^^^^^^^^^^^^^

.. reference::

   :Menu:   :menuselection:`Node Wrangler --> Merge Selected Nodes --> Use Math Nodes`

Use the Math nodes for merging, regardless of the selected nodes. You can choose the mode of the node via the menu.
You can quickly set some operations by using corresponding shortcuts.

- Add: :kbd:`Shift-Ctrl-=`, :kbd:`Shift-Ctrl-=`
- Subtract: :kbd:`Shift-Ctrl-Minus`, :kbd:`Shift-Ctrl-NumpadMinus`
- Multiply: :kbd:`Shift-Ctrl-8`, :kbd:`Shift-Ctrl-NumpadAsterisk`
- Divide: :kbd:`Shift-Ctrl-Slash`, :kbd:`Shift-Ctrl-NumpadSlash`
- Greater than: :kbd:`Ctrl-Comma`
- Less than: :kbd:`Ctrl-Period`


Merge Using Z-Combine Node
^^^^^^^^^^^^^^^^^^^^^^^^^^

:guilabel:`Compositor`

.. reference::

   :Menu:   :menuselection:`Node Wrangler --> Merge Selected Nodes --> Use Z-Combine Nodes`
   :Shortcut:  :kbd:`Ctrl-NumpadPeriod`

Use the Z-Combine nodes for merging. If possible, Image and Z-Depth outputs will be linked. If the current
node editor is not Compositor, this will execute the *Mix* function from the automatic merge.


Merge Using Alpha Over Node
^^^^^^^^^^^^^^^^^^^^^^^^^^^

:guilabel:`Compositor`

.. reference::

   :Menu:   :menuselection:`Node Wrangler --> Merge Selected Nodes --> Use Alpha Over Nodes`
   :Shortcut:  :kbd:`Ctrl-Alt-0`

Use the Alpha Over nodes for merging. If the current node editor is not Compositor, this will execute the *Mix*
function from the automatic merge.


Batch Change Blend Mode / Math Operation
----------------------------------------

.. reference::

   :Menu:   :menuselection:`Node Wrangler --> Batch Change`

Change the blend mode or math operation of the selected Mix and Math nodes at once.
You can use :kbd:`Alt-Up` or :kbd:`Alt-Down` to cycle through previous or next blend modes or math operations.
You can also quickly set some operations by using corresponding shortcuts.

- Add: :kbd:`Alt-=`, :kbd:`Alt-=`
- Subtract: :kbd:`Alt-Minus`, :kbd:`Alt-NumpadMinus`
- Multiply: :kbd:`Alt-8`, :kbd:`Alt-NumpadAsterisk`
- Divide: :kbd:`Alt-Slash`, :kbd:`Alt-NumpadSlash`
- Greater than: :kbd:`Alt-Comma`
- Less than: :kbd:`Alt-Period`

Change Mix Factor
-----------------

.. reference::

   :Shortcut:
      :kbd:`Alt-Left`, :kbd:`Shift-Alt-Left`, :kbd:`Alt-Right`, :kbd:`Shift-Alt-Right`,
      :kbd:`Shift-Ctrl-Alt-Left`, :kbd:`Shift-Ctrl-Alt-0`, :kbd:`Shift-Ctrl-Alt-Right`, :kbd:`Shift-Ctrl-Alt-1`

Change the Factor value of the selected Mix and Mix Shader nodes with shortcuts.

- Increase Factor by 0.1: :kbd:`Alt-Right`
- Decrease Factor by 0.1: :kbd:`Alt-Left`
- Increase Factor by 0.01: :kbd:`Shift-Alt-Right`
- Decrease Factor by 0.01: :kbd:`Shift-Alt-Left`
- Set Factor to 0.0: :kbd:`Shift-Ctrl-Alt-Left`, :kbd:`Shift-Ctrl-Alt-0`
- Set Factor to 1.0: :kbd:`Shift-Ctrl-Alt-Right`, :kbd:`Shift-Ctrl-Alt-1`


Delete Unused Nodes
-------------------

.. reference::

   :Menu:   :menuselection:`Node Wrangler --> Delete Unused Nodes`
   :Shortcut:  :kbd:`Alt-X`

Clean up your node tree. Delete all nodes that don't contribute to the final result.


Swap Links
----------

.. reference::

   :Menu:   :menuselection:`Node Wrangler --> Swap Links`
   :Shortcut:  :kbd:`Alt-S`

When two nodes are selected, this swaps each other's output link.
Note that some output connections can be lost if the two nodes have a different number of connected
outputs.

With one node selected, if the node has one linked input, it cycles the link through the available input
sockets. If the node has two linked inputs, it swaps those two links. If there are more than two inputs linked,
it swaps the two inputs with matching types (the Mix node's two Color inputs, for example).

.. figure:: /images/addons_node_node-wrangler_swap_links.png

   Swap works differently depending on the selected nodes and their links.


Reset Backdrop
--------------

:guilabel:`Compositor`

.. reference::

   :Menu:   :menuselection:`Node Wrangler --> Reset Backdrop`
   :Shortcut:  :kbd:`Z`

Reset the position and scale of the backdrop.


Add Attribute Node
------------------

:guilabel:`Shader`

.. reference::

   :Menu:      :menuselection:`Header --> Add --> Input --> Attributes`

Add an Attribute node with the selected attribute.


Preview Node Output
-------------------

:guilabel:`Shader` :guilabel:`Geometry Nodes`

.. reference::

   :Shortcut:  :kbd:`Shift-Ctrl-LMB` for :guilabel:`Shader`, :kbd:`Shift-Alt-LMB` for :guilabel:`Geometry Nodes`

Connect an output of the selected node to the final output of the node tree (the Material Output or World Output
for Shader, the final Group Output for Geometry Nodes) to preview its output in the viewport.
You can cycle through the available outputs by clicking it again while holding the modifier keys.

.. seealso::

   While in Shader, any output can be connected to the final output, in Geometry Nodes, only Geometry outputs
   can be connected to the final output.
   To preview other types of outputs in Geometry Nodes,
   use its own :doc:`Viewer Node </modeling/geometry_nodes/output/viewer>`.

.. seealso::

   Also check out *Connect to Output*. It is a similar function but has different behaviors.
   It also works in all node editors.


Join Nodes
----------

.. reference::

   :Menu:   :menuselection:`Node Wrangler --> Join Nodes`
   :Shortcut:  :kbd:`Shift-P`

See :ref:`bpy.ops.node.join`.


Reload Images
-------------

:guilabel:`Compositor` :guilabel:`Shader` :guilabel:`Texture Nodes`

.. reference::

   :Menu:   :menuselection:`Node Wrangler --> Reload Images`
   :Shortcut:  :kbd:`Alt-R`

Reload all of the images used in the node tree. This lets you reload the images without using the Image Editor.


Copy Settings
-------------

.. reference::

   :Menu:   :menuselection:`Node Wrangler --> Copy to Selected --> Settings from Active`
   :Shortcut:  :kbd:`Shift-C`

Copy the settings of the active node to all selected nodes of the same type.


Reset Nodes
-----------

.. reference::

   :Shortcut:  :kbd:`Backspace`

Revert the settings of the selected nodes to default while maintaining connections.


Copy Label
----------

.. reference::

   :Menu:   :menuselection:`Node Wrangler --> Copy to Selected --> Copy Label`
   :Shortcut:  :kbd:`Shift-V`, :kbd:`Shift-C`

Copy custom labels to all of the selected nodes. You can copy them from the active node (:kbd:`Shift-V`),
from the nodes that are linked to the selected ones, or from the names of the sockets that the selected nodes
are linked to.
:kbd:`Shift-C` will bring up a submenu with all available options.


Clear Label
-----------

.. reference::

   :Menu:   :menuselection:`Node Wrangler --> Clear Label`
   :Shortcut:  :kbd:`Alt-L`

Clear the custom labels of selected nodes and revert them back to their default node names.


Modify Labels
-------------

.. reference::

   :Menu:   :menuselection:`Node Wrangler --> Modify Labels`
   :Shortcut:  :kbd:`Shift-Alt-L`

Batch rename the custom labels of selected nodes. You can add text to the beginning and the end and replace parts
of the text.


Add Texture Setup
-----------------

:guilabel:`Shader`

.. reference::

   :Menu:   :menuselection:`Node Wrangler --> Add Texture Setup`
   :Shortcut:  :kbd:`Ctrl-T`

Add a setup of a texture node, Texture Coordinate, and Mapping nodes to any shader node.
If you select a texture node, it will only add the Texture Coordinate and Mapping nodes.
For a background shader it will add an Environment Texture node.


Add Principled Texture Setup
----------------------------

:guilabel:`Shader`

.. reference::

   :Menu:   :menuselection:`Node Wrangler --> Add Principled Setup`
   :Shortcut:  :kbd:`Shift-Ctrl-T`

Add a principled texture setup from the selected texture files. Select a Principled BSDF node,
select *Add Principled Setup* from the quick access menu (or press :kbd:`Shift-Ctrl-T`), and select texture files.
It automates the process of adding Image Texture nodes, loading images, selecting the appropriate Color Space,
and connecting their outputs to the Principled BSDF node.

It detects the type of textures by looking at their file names. You can edit the tags used for this matching
process in the add-on preferences.

.. figure:: /images/addons_node_node-wrangler_swap_pbr-setup.jpg

   Setting up these textures can take dozens of clicks, even with Node Wrangler's other tools.
   With Principled Texture Setup, you can reduce that to a few clicks.


Add Reroutes to Outputs
-----------------------

.. reference::

   :Menu:   :menuselection:`Node Wrangler --> Add Reroutes`
   :Shortcut:  :kbd:`Slash`

Add reroute nodes to each output of the selected nodes.


Link Active to Selected
-----------------------

.. reference::

   :Menu:   :menuselection:`Node Wrangler --> Link Active to Selected`
   :Shortcut:  :kbd:`Backslash`

Link the active node to the selected nodes based on various criteria.

To All Selected
   Link the active node to all selected nodes. (:kbd:`K`) You can force it to replace existing links.
   (:kbd:`Shift-K`)

Use Node Name/Label
   Link only to the selected nodes that have the same label as the active node. (:kbd:`'`) You can force it to
   replace existing links. (:kbd:`Shift-'`)

Use Outputs Names
   Link only when the name of the outputs matches the name or label of the selected nodes. (:kbd:`;`) You can
   force it to replace existing links. (:kbd:`Shift-;`) This is handy for replacing sources at the same time.
   (For example, connecting outputs from Render Layer to image (multi-layer EXR) in Compositor.)


Align Nodes
-----------

.. reference::

   :Menu:   :menuselection:`Node Wrangler --> Align Nodes`
   :Shortcut:  :kbd:`Shift-=`

Align the selected nodes horizontally or vertically. The effect is similar to scaling nodes on an axis
(:kbd:`S X 0` or :kbd:`S Y 0`), but it places the nodes at an even distance.


Select within Frame (Parent/Children)
-------------------------------------

- :kbd:`]` -- Select all direct child nodes of the selected frame.
- :kbd:`[` -- Select the direct parent frame node of the selected nodes.


Detach Outputs
--------------

.. reference::

   :Menu:   :menuselection:`Node Wrangler --> Detach Outputs`
   :Shortcut:  :kbd:`Shift-Alt-D`

Detach the selected node's outputs while leaving linked inputs intact.


.. _bpy.ops.node.add_image:

Add Multiple Images
-------------------

:guilabel:`Compositor` :guilabel:`Shader`

.. reference::

   :Menu:      :menuselection:`Add --> Input` for :guilabel:`Compositor`,
               or :menuselection:`Add --> Texture` for :guilabel:`Shader`

Select multiple images and add a node for each image.
(Useful for importing multiple render passes or renders for image stacking.)


.. _bpy.ops.node.nw_add_sequence:

Add Image Sequence
------------------

:guilabel:`Compositor` :guilabel:`Shader`

.. reference::

   :Menu:      :menuselection:`Add --> Input Add Image Sequence` for :guilabel:`Compositor`,
               or :menuselection:`Add --> Texture Add Image Sequence` for :guilabel:`Shader`

Add an Image Sequence by only selecting one image from a sequence of image files. It will automatically detect
the length of the sequence and set the node appropriately.

Relative Path
   Sets the file path to be relative to the currently opened blend-file.
   See :ref:`files-blend-relative_paths`.
Start Frame
   Global starting frame of the movie/sequence, assuming first picture has a #1.

.. reference::

   :Category: Node
   :Description: Various tools to enhance and speed up node-based workflow.
   :Location: :menuselection:`Node editor --> Sidebar` or see the shortcuts of individual tools.
   :File: node_wrangler.py
   :Author: Bartek Skorupa, Greg Zaal, Sebastian Koenig, Christian Brinkmann, Florian Meyer
   :License: GPL
   :Note: This add-on is bundled with Blender.
