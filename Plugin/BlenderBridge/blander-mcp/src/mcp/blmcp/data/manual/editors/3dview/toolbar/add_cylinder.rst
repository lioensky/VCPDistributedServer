.. _tool-add-cylinder:

************
Add Cylinder
************

.. reference::

   :Mode:      Object Mode and Edit Mode
   :Tool:      :menuselection:`Toolbar --> Add Cylinder`

Interactively add a :ref:`cylinder mesh object <bpy.ops.mesh.primitive_cylinder_add>`.


Usage
=====

First define the base of the object by dragging with :kbd:`LMB`.
Next, release :kbd:`LMB` and move the mouse to define the height of the object.
Finally, click :kbd:`LMB` to confirm the shape of the object.

You can use the following hotkeys to temporarily change a setting
(for as long as the key is held):

.. list-table::
   :widths: 10 90

   * - :kbd:`Ctrl`
     - Toggles snapping.
   * - :kbd:`Alt`
     - Toggles the *Origin* setting.
   * - :kbd:`Shift`
     - Toggles the *Aspect* setting.


Tool Settings
=============

Depth
   The initial depth (from the screen into the scene) used when placing the object.

   :Surface: Start placing on the surface under the mouse cursor. If there is no surface, this does the
             same as *Cursor Plane*.
   :Cursor Plane: Start placing on a plane that goes through the :doc:`3D Cursor </editors/3dview/3d_cursor>`
                  and is aligned according to the *Orientation* and *Plane Axis*.
   :Cursor View: Start placing on a plane that goes through the 3D Cursor and is aligned to the view.

Orientation
   The new object's orientation -- a set of three axes, out of which *Plane Axis* chooses one.

   :Surface: The object uses the normal orientation of the surface under the mouse cursor.
             If there is no surface, this does the same as *Default*.
   :Default: The object uses the default :doc:`/editors/3dview/controls/orientation`.

Snap To
   The target to use while :doc:`/editors/3dview/controls/snapping`.

   :Geometry: Snap to all types of geometry (vertices, edges, and faces).
   :Default: Snap to the target defined in the global snapping options.

Plane Axis
   Which of the three *Orientation* axes (X, Y or Z) is "up" for the object.
   The object's base will be perpendicular to this axis.

Auto Axis
   Rather than using the *Orientation* axis indicated by *Plane Axis*,
   use the one that's closest to the viewport's viewing direction
   (when not hovering over a surface).


.. rubric:: Base

Origin
   How the base is defined.

   :Edge: The base is defined from one corner to the opposing corner.
   :Center: The base is defined from the centerpoint to a corner.

Aspect
   Whether the base has a free or fixed aspect ratio.

   :Free: The width and depth of the base can be chosen independently.
   :Fixed: The width and depth of the base are forced to be equal.


.. rubric:: Height

Origin
   How the height is defined.

   :Edge: The base becomes the bottom, after which you define the top.
   :Center: The base becomes the center, after which you define the top.

Aspect
   Whether the side of the bounding box has a free or fixed aspect ratio.

   :Free: The height can be chosen independently of the base.
   :Fixed: The height is forced to be equal to the largest side of the base.

Vertices
   The number of vertices in the caps.

Cap Fill Type
   Set how the caps will be filled.

   :Triangle Fan: Fill with triangular faces which share a vertex in the middle.
   :N-gon: Fill each ring with an :term:`N-gon`.
   :Nothing: Do not fill. Creates only the outer rings of vertices.
