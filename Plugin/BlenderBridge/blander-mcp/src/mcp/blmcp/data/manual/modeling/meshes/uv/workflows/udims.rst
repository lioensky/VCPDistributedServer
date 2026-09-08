
*****
UDIMs
*****

Using UV maps can have one disadvantage, they consist of one texture for the entire mesh.
Most of the time this is sufficient but the disadvantage is that the texture is one resolution for the entire mesh.
This causes issues if you have a very large mesh with geometry of different importance.
When using a singular texture, the resolution might be too low to cover larger UV islands
while being inefficient for smaller, less important islands.

UDIM offers a solution to this by being able to spread UV islands across several different textures.
UDIM which stands for U DIMension is based on a tile system
where each tile is a different texture in the overall UDIM texture array.
Basically each tile consists of its own UV space (0-1, 1-2, 2-3) and have its own image assigned to that tile.
Tiles are managed in the `UDIM Tiles`_ panel where they can have a generated image assigned to them.
Generally, you create several textures of different resolutions;
for example, you may have a 4k resolution texture for the major details,
and 2k and/or 1k textures for less important details.

The UDIM array consists of one main tile, this tile is given the index number of ``1001``.
The next tile that gets added will be ``1002`` and will be placed to the right of the main tile.
The overall UDIM array is ten tiles wide, so tiles ``1001`` through ``1010`` are created on the first row.
After ten tiles a new row of tiles is started above the main tile; so ``1011`` will be place directly above ``1001``.


Workflow
========

To start using a UDIM workflow, you should unwrap a mesh as you would for any other UV map.
After that you should decide how many textures you want to split your UV map into.
This will be different for every mesh and workflow but a good minimum is 3: one 4k, one 2k, and one 1k image.
Then create the desired textures to match how many textures you want.

After this it is the same process of moving UVs to the appropriate tile
and scaling and managing them like any other UV map.
See :doc:`/modeling/meshes/uv/workflows/layout` for information on laying out UVs.

When the UVs are correctly set up across the multiple UV islands it is time to add proper textures the UDIM array.
Currently, existing textures cannot be added to a tile,
to fill a tile with an existing texture you first must:

#. Create the desired tiles.
#. Save the image.
#. Replace the saved image file with the desire texture by deleting the file
   and replacing it with a new image file, keeping the old file name.
   Or by opening the image in another application and modifying the contents of the image.

Other than using a third-party application to edit the UDIM texture it is possible to paint on UDIM textures.
This works for either 2D Painting or :doc:`3D Painting </sculpt_paint/texture_paint/index>`.


File Substitution Tokens
========================

Substitution tokens are special sequences of characters in a filename
that can be replaced with more meaningful and context aware information.
In this case, tokens are identified by being text wrapped in angle bracket characters.

This substitution is used while load loading or saving an image
to automatically identify the tile associated with a particular texture in the UDIM array.

The following tokens are supported:

- ``<UDIM>``: A 4-digit notation calculated as ``1001 + u-tile + v-tile * 10``.
- ``<UVTILE>``: A notation defined as ``u(u-tile + 1)_v(v-tile + 1)``.

Examples:

- ``monster-basecolor.<UDIM>.png`` will load/save files like ``monster-basecolor.1021.png`` etc.
- ``monster-basecolor.<UVTILE>.png`` will load/save files like ``monster-basecolor.u1_v3.png`` etc.


.. _bpy.ops.image.tile:
.. _bpy.types.UDIMTiles:

UDIM Tiles
==========

.. reference::

   :Editor:    Image Editor, UV Editor
   :Mode:      All Modes
   :Panel:     :menuselection:`Sidebar --> Image --> UDIM Tiles`

In this panel UDIM tiles are managed;
new tiles can be added, tiles can be removed, or tiles can filled with a generated texture.

UDIM Tile List
   List all UDIM tiles associated with the main index (``1000`` tile).
   Double clicking on the tile name allows you to alter the tiles *Label*.

:bl-icon:`add` Add Tile
   Adds new UDIM tiles to the group.

   Number
      The starting tile index number.
      UDIMs must start with the ``1001`` tile and typically increase in incremental order.
   Count
      The number of tiles to add.
   Label
      An optional label can be used instead of the index number.
      These labels are shown in the 2D Viewport.
   Fill
      Occupy the UDIM tile with a generated image; see *Fill Tile* below.

:bl-icon:`remove` Remove Tile
   Deletes the selected UDIM tile from the group.
   If this tile is not saved and contains data, that data will be lost.

Fill Tile
   Occupy the UDIM tile with a :ref:`Generated Image <image-generated>`.

   .. warning::

      If a tile is not filled, it will not be saved with the image.
