.. _ui-data-block:

***************
Data-Block Menu
***************

Lets you select a :doc:`Data-Block </files/data_blocks>` (such as a material)
in order to link it to something else (such as an object).

.. figure:: /images/interface_controls_templates_data-block_menu.png
   :align: right

   A data-block menu with a search field.

Type
   Shows an icon indicating the data-block type. Clicking the image or the down arrow opens the popup menu.
   Dragging the image lets you apply the data-block to something else. (For example, you can drag a
   material onto an object in the 3D Viewport to :doc:`assign </render/materials/assignment>` it.
   Dragging onto :ref:`ui-data-id` fields is also possible.)

   List
      A list of data-blocks available in the current blend-file, or a link to select an item from.
      The menu may show a preview besides the items and
      a search field to search the items in the list by name.

      .. note::

         Data-blocks with names that begin with ``.`` are hidden from the list, unless a string
         that also starts with ``.`` is entered into the search field, or the
         :ref:`Show Hidden Files/Data-Blocks <bpy.types.PreferencesFilePaths.show_hidden_files_datablocks>`
         user preference is enabled.

Name
   Displays, and allows :ref:`editing <data-system-datablock-name-and-rename>` of, the name of the selected
   data-block.
User Count
   Displays the number of :term:`users <Data User>` of the data (if there's more than one user).
   Clicking it will create a single-user copy.

   As an example, if three separate objects referenced the same material, the material's user count would be 3.
   Changing the material would affect all three objects. If you now selected an object and clicked the user count,
   the object would receive its very own copy of the material, which can be modified independently of the original
   that's still used by the other two.

Fake User (shield icon)
   If a data-block has no :term:`real users <Real User>`, it'll normally be cleaned up
   (deleted) when saving the blend-file. To prevent this, you can give it a fake user;
   that way, it's guaranteed to "survive." Data-blocks with a fake user have an "F"
   prefix in the drop-down list.

   The :doc:`Outliner </editors/outliner/introduction>` can show an overview of all data-blocks
   without real users in the blend-file. Simply change its Display Mode to Orphan Data.
New/Add (files icon)
   Creates a new data-block (or duplicates the current one) and selects it.
Open File (folder icon)
   Opens the :doc:`File Browser </editors/file_browser>`, for importing an image for example.
Unpack File (bin icon)
   :ref:`Unpack <pack-unpack-data>` the file packed into the current blend-file to an external one.
:bl-icon:`x` (Unlink Data-block)
   Clears the link. :kbd:`Shift-LMB` to set the users to zero
   allowing the data to be fully deleted from the blend-file.

Sometimes there is a :ref:`list <ui-list-view>` of applied data-blocks
(such as a list of materials used on the object).

.. seealso::

   Data-blocks are discussed further in the :doc:`Data System chapter </files/data_blocks>`.


Preview
=======

.. figure:: /images/interface_controls_templates_data-block_preview.png
   :align: right

   A Data-Block menu with preview.

Some data-block menus have large preview images in their drop-down
instead of just icons and names.

.. container:: lead

   .. clear


.. rename to selector?

.. _ui-data-id:

Data ID
=======

.. figure:: /images/interface_controls_templates_data-block_data-id.png
   :align: right

   A Data ID field.

A Data ID field is similar to a Data Block Menu, but is only for selecting
(and not for other features like creating new data or managing users).

It can show the following elements:

Type
   The icon on the left specifies the accepted data-block type.
Name
   The text field functions as a search field by matching elements in the list.
   Press :kbd:`Tab` to auto-complete names up to the level where a match is found.
   If more than one match exists, you have to continue typing.
   If you type an invalid name, the value will remain unchanged.
List
   Lets you select the data-block directly.
Eyedropper
   In some Data IDs there is an :ref:`ui-eyedropper`
   available through the pipette icon on the right side.
:bl-icon:`x` (Clear Button String)
   Click the :bl-icon:`x` button on the right to clear the reference.


ID Sub-Data
-----------

Related types of ID sub-data may become available to select,
depending on the data-block type and its intended usage.

.. figure:: /images/interface_controls_templates_data-block_subids.png

   Sub-data Example.

Vertex Group
   If the selected Object in the *Target* field is a mesh or a lattice,
   an additional field may be displayed to select one of its vertex groups.
Bone
   If the selected Object in the *Target* field is an armature,
   an additional field may be displayed to select one of its bones.

   Head/Tail
      Once a bone is selected, a numeric field may become available for specifying a point
      along the bone.
      A value of **0.0** corresponds to the bone's head, while a value of **1.0** corresponds to its tail.
      Any values between these will result in linear interpolation (so a value of **0.5** matches
      the bone's center).

      Use B-Bone Shape
         If the bone is a :doc:`bendy bone </animation/armatures/bones/properties/bendy_bones>`,
         clicking on this button will make the point follow the curvature of the B-spline between head and tail,
         rather than simply going in a straight line.
