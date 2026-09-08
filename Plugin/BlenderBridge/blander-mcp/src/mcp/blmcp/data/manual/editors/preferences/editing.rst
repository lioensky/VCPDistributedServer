.. _bpy.types.PreferencesEdit:

*******
Editing
*******

These preferences control how several tools will interact with your input.

.. figure:: /images/editors_preferences_section_editing.webp


Objects
=======

New Objects
-----------

.. _bpy.types.PreferencesEdit.material_link:

Link Materials To
   To understand this option properly, you need to understand how Blender works with Objects.
   Almost everything in Blender is organized in a hierarchy of data-blocks.
   A data-block can be thought of as containers for certain pieces of information. For example,
   the Object data-block contains information about the Object's location, rotation, and scale
   while the associated linked Object Data's data-block contains information about the mesh.

   .. figure:: /images/editors_preferences_editing_data-blocks-hierarchy.png

      Example for a mesh.

   A material may be linked in two different ways:

   :Object Data:
      Any created material will be created as part of the Object Data's data-block.
   :Object:
      Any created material will be created as part of the Object's data-block.

   .. figure:: /images/editors_preferences_editing_data-blocks-link.png

      A material linked to Object Data (left) and Object (right).

   .. seealso::

      :doc:`Read more about Blender's Data System </files/index>`.

.. _bpy.types.PreferencesEdit.object_align:

Align to
   :World:
      New objects align with world coordinates.
   :View:
      New object align with view coordinates.
   :3D Cursor:
      New objects align to the 3D cursor's orientation.

.. _bpy.types.PreferencesEdit.use_enter_edit_mode:

Enter Edit Mode
   If selected, Edit Mode is automatically activated when you create a new object.

.. _bpy.types.PreferencesEdit.collection_instance_empty_size:

Instance Empty Size
   The display size for empties when
   a new :doc:`collection instance </scene_layout/object/properties/instancing/collection>` is created.


.. _bpy.types.PreferencesEdit.use_duplicate:

Copy on Duplicate
-----------------

The checkboxes define what data is copied with a duplicated object and
what data remains linked. Any boxes that are checked will have their data copied along with
the duplication of the object. Any boxes that are not checked will instead have their data linked
from the source object that was duplicated.

For example, if you have *Mesh* checked,
then a full copy of the mesh data is created with the new object,
and each mesh will behave independently of the duplicate.
If you leave the mesh box unchecked then when you change the mesh of one object,
the change will be mirrored in the duplicate object.

The same rules apply to each of the checkboxes in the data-block list.


3D Cursor
=========

.. _bpy.types.PreferencesEdit.use_mouse_depth_cursor:

Cursor -- Surface Project
   When placing the cursor by clicking,
   the cursor is projected onto the surface under the cursor.

.. _bpy.types.PreferencesEdit.use_cursor_lock_adjust:

Cursor -- Lock Adjust
   When the viewport is locked to the cursor,
   moving the cursor avoids the view *jumping* based on the new offset.


Annotations
===========

.. _bpy.types.PreferencesEdit.grease_pencil_default_color:

Default Color
   The default color for new Annotate layers.

.. _bpy.types.PreferencesEdit.grease_pencil_eraser_radius:

Eraser Radius
   The size of the eraser used with the Annotate Tool.

.. seealso::

   :doc:`Read more about Annotations </interface/annotate_tool>`.


.. _bpy.types.PreferencesView.use_weight_color_range:

Weight Paint
============

*Mesh skin weighting* is used to control how much a bone deforms the mesh of a character.
To visualize and paint these weights, Blender uses a color ramp (from blue to green, and from yellow to red).
Enabling the checkbox will enable an alternate map using a ramp starting with an empty range.
Now you can create your custom map using the common color ramp options.
For detailed information see the :doc:`Color ramps </interface/controls/templates/color_ramp>` page.


Grease Pencil
=============

.. _bpy.types.PreferencesEdit.grease_pencil_manhattan_distance:

Manhattan
   The minimum number of pixels the mouse should have moved either
   horizontally or vertically before the movement is recorded.
   Decreasing this should work better for curvy lines.

.. _bpy.types.PreferencesEdit.grease_pencil_euclidean_distance:

Euclidean
   The minimum distance that mouse has to travel before movement is recorded.

.. seealso::

   :doc:`Read more about Grease Pencil </grease_pencil/index>`.


Text Editor
===========

.. _bpy.types.PreferencesEdit.use_text_edit_auto_close:

Auto Close Character Pairs
   Automatically insert the corresponding character to close an expression
   when typing characters such as quotes, brackets, braces, or parentheses.


.. _preferences-editing-node-editor:

Node Editor
===========

.. _bpy.types.PreferencesEdit.node_use_insert_offset:

Auto-Offset
   Automatically offset the following or previous nodes in a chain when inserting a new node.
   See :ref:`editors-nodes-usage-auto-offset` for more information.

   .. _bpy.types.PreferencesEdit.node_margin:

   Auto-offset Margin
      Margin to use for :ref:`offsetting nodes <editors-nodes-usage-auto-offset>`.


Miscellaneous
=============

.. _bpy.types.PreferencesEdit.sculpt_paint_overlay_color:

Sculpt Overlay Color
   Defines a color to be used in the inner part of
   the brushes circle when in Sculpt Mode, and it is placed as an overlay to the brush,
   representing the focal point of the brush influence.
   The overlay color is visible only when the overlay visibility is selected
   (clicking at the *eye* to set its visibility), and the transparency of the overlay is
   controlled by the alpha slider located at the :menuselection:`Tool tab --> Display panel` in the Sidebar.
