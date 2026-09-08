.. index:: Geometry Nodes; Bake
.. _bpy.types.GeometryNodeBake:

*********
Bake Node
*********

.. figure:: /images/node-types_GeometryNodeBake.webp
   :align: right
   :alt: Bake node.

The *Bake* node allows saving and loading intermediate geometries.
This node bakes parts of the node tree for better performance.

The data format used to store geometry data is not considered to be an import/export format.
Volume objects, however, are saved using the OpenVDB file format which can be used interoperably.

.. important::

   - It's not guaranteed that data written with one Blender version can be read by another Blender version.


Inputs
======

Geometry
   Standard geometry input, which is used as the default bake item.
   More bake items can be added by dragging sockets into the blank socket or in the *Bake Items* panel.
   Items can be renamed by :kbd:`Ctrl-LMB` on the socket name or in the nodes *Properties* panel.


Bake Items
==========

.. reference::

   :Editor:    Geometry Node Editor
   :Panel:     :menuselection:`Sidebar --> Node --> Bake Items`

The *Bake Items* panel is used to manage the input sockets
of the node thus also managing what data is baked.

.. _bpy.types.GeometryNodeBake.active_index:

Bake Items List
   Used to manage the inputs and outputs of the bake node.
   Items can be added, removed, renamed, and sorted.

Socket Type
   The data (:ref:`bpy.types.NodeLink`) of the input/output.

Attribute Domain
   The :ref:`attribute domain <attribute-domains>` used to evaluate the input field on.

Is Attribute
   Bake item is an attribute stored on a geometry.


Properties
==========

.. note::

   Some properties can only be edited in the Properties panel
   (:menuselection:`Sidebar --> Node --> Properties`).

Bake Mode
   The *Bake* node can calculate the geometry of a single frame or an animation.

   :Animation:
      Bakes the geometry data for multiple frames.
      By default the scene frame range is used, however, a *Custom Range* can also be defined.
   :Still: Bakes the geometry data of the current frame.

Bake
   Performs all necessary geometry calculations and saves the data on disk or packed into the .blend file.

   Pack/Unpack
      Packs or unpacks already baked data. When unpacking, there are different options to control where the data will
      be stored. The options are the same as for the :ref:`Unpack Resources <bpy.ops.file.unpack_all>` operator.

   :bl-icon:`trash` Delete Geometry Node Bake
      Deletes the bake data.

Bake Target
   Specifies where the baked data should be stored.

   :Inherit from Modifier:
      The setting is copied from the modifier that contains the bake node. This is the default.
   :Packed:
      The baked data is packed into the .blend file. So no separate file is necessary.
   :Disk:
      The baked data is stored in a separate directory on disk.

Custom Path
   Specify a path where the baked data should be stored manually.

   Bake Path
      Location on disk where the baked data is stored.
      Note, this path is also used for :doc:`simulation zones </modeling/geometry_nodes/simulation/simulation_zone>`.

Custom Range :guilabel:`Animation`
   Override the simulation frame range from the scene.

Start, End
   The start and end frame numbers for the custom range.


Outputs
=======

For each input, the same output is added to act as a pass through.

Geometry
   Standard geometry output, which is used as the default bake item.
   More bake items can be added by dragging sockets into the blank socket or in the *Bake Items* panel.
   Items can be renamed by :kbd:`Ctrl-LMB` on the socket name or in the nodes *Properties* panel.
