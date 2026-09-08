.. index:: Modifiers; Modeling Modifiers
.. index:: Modeling Modifiers

************
Introduction
************

Modifiers are automatic operations that affect an object's geometry in a non-destructive way.
With modifiers, you can perform many effects automatically that would otherwise be too tedious to do manually
(such as subdivision surfaces) and without affecting the base geometry of your object.

They work by changing how an object is displayed and rendered, but not the geometry which you can edit directly.
You can add several modifiers to a single object to form `The Modifier Stack`_
and *Apply* a modifier if you wish to make its changes permanent.

They can be added to the active object using the :ref:`bpy.ops.object.modifier_add` operator,
the "Add Modifier" button at the top of Modifiers tab in the :doc:`/editors/properties_editor`,
or using :kbd:`Shift-A` in the same tab.
New modifiers are always added at the bottom of the :ref:`stack <modifier-stack>` (i.e. will be applied last).

There are many built-in modifiers but Blender also allows users
to make their own modifiers through :doc:`/modeling/geometry_nodes/index`.


Categories
==========

There are four categories of built-in modifiers:

Edit
   Similar to the *Deform*  modifiers (see below),
   however, they usually do not directly affect the geometry of the object,
   but some other data, such as vertex groups.
Generate
   Constructive/destructive modifiers that will affect the whole :term:`Topology` of the mesh.
   They can change the general appearance of the object, or add new geometry to it...
Deform
   Unlike *Generate* ones above, these modifiers only change the shape of an object, without altering its topology.
Simulate
   Represent :doc:`physics simulations </physics/index>`. In most cases, they are automatically added to
   the modifiers stack whenever a *Particle System* or *Physics* simulation is enabled. Their only role is to define
   the position in the modifier stack from which is taken the base data for the simulation they represent.
   As such, they typically have no properties, and are controlled by settings exposed in
   separate sections of the :doc:`/editors/properties_editor`.

You will also notice a category called "Hair",
this category comes from a bundled :term:`Asset Library` that is distributed with Blender.
See :doc:`/modeling/geometry_nodes/hair/index` for more information.

Users can make their own categories by making geometry node groups :term:`assets <Asset>`
and assigning them to a :term:`Asset Catalog`. This catalog name will be the category name.
If a user creates a catalog with the same name as one of the built-in categories
the node group will be added to the bottom of the corresponding menu.

Node Groups that are non-assets or that do not belong to a category will be available in the "Unassigned" sub-menu.

.. note::

   Geometry Node Groups must have the :ref:`Modifier <bpy.types.GeometryNodeTree.is_modifier>`
   property enabled for the node group to show up in the Add Modifier menu.


.. _bpy.types.Modifier.show:

Interface
=========

Each modifier's interface shares the same basic components, see Fig. :ref:`fig-modifiers-panel-layout`.

.. _fig-modifiers-panel-layout:

.. figure:: /images/modeling_modifiers_introduction_panel-layout.png
   :align: center

   Panel layout (Subdivision Surface as an example).

At the top is the panel header.
The icons each represent different settings for the modifier (left to right):

:bl-icon:`rightarrow` / :bl-icon:`downarrow_hlt` Expand
   Collapse modifier to show only the header and not its options.

Type
   An icon as a quick visual reference of the modifier's type.

.. _bpy.types.Modifier.name:

Name
   Every modifier has a unique name per object. Two modifiers on one object must have unique names,
   but two modifiers on different objects can have the same name. The default name is based on the modifier type.

.. _bpy.types.Modifier.show_on_cage:

:bl-icon:`mesh_data` On Cage :guilabel:`Meshes`
   Depends on the previous setting, if enabled, the modified geometry can also be edited directly,
   instead of the original one.

   .. warning::

      While it shows edited items in their final, modified positions, you are still editing original data.

      In situations where the positions diverge it can lead to confusing behavior,
      so you may wish to disable it in those cases.

      It's also worth noting that some features don't use the cage positions including:

      - Snap targets, such as snapping to vertex.
      - The transform gizmo uses the original positions.

.. _bpy.types.Modifier.use_apply_on_spline:

:bl-icon:`surface_data` Apply On Spline :guilabel:`Curves` :guilabel:`Surfaces` :guilabel:`Text`
   Apply the whole modifier stack up to and including that one on the curve or surface control points,
   instead of their tessellated geometry.

   .. note::

      By default, curves, texts and surfaces are always converted to mesh-like geometry
      before that the modifier stack is evaluated on them.

.. _bpy.types.Modifier.show_in_editmode:

:bl-icon:`editmode_hlt` Edit Mode
   Display the modified geometry in Edit Mode, as well as the original geometry which you can edit.

.. _bpy.types.Modifier.show_viewport:

:bl-icon:`restrict_view_off` / :bl-icon:`restrict_view_on` Realtime
   Toggle visibility of the modifier's effect in the 3D Viewport.

.. _bpy.types.Modifier.show_render:

:bl-icon:`restrict_render_off` / :bl-icon:`restrict_render_on` Render
   Toggle visibility of the modifier's effect in the render.

   .. note::

      The *Square*, *Triangle* and *Surface* icons may not be available,
      depending on the type of object and modifier.

.. _bpy.ops.object.modifier_apply:

Extras
   Apply :kbd:`Ctrl-A`
      Makes the modifier "real": converts the object's geometry to match the applied modifier's results,
      and deletes the modifier.

      When applying a modifier to an object that shares Object Data between multiple objects,
      the object must first be made a :ref:`Single User <data-system-datablock-make-single-user>`
      which can be performed by confirming the pop-up message.

      .. warning::

         Applying a modifier that is not first in the stack will ignore the stack order
         (it will be applied as if it was the first one), and may produce undesired results.

   .. _bpy.ops.object.modifier_apply_as_shapekey:

   Apply as Shape Key
      Stores the result of that modifier in a new relative :doc:`shape key </animation/shape_keys/introduction>`
      and then deletes the modifier from the modifier stack.
      This is only available with modifiers that do not affect the topology (typically, *Deform* modifiers only).

      .. note::

         Even though it should work with any geometry type that supports shape keys,
         currently it will only work with meshes.

   Save as Shape Key
      Stores the result of that modifier in a new relative :doc:`shape key </animation/shape_keys/introduction>`
      and keeps the modifier in the modifier stack.
      This is only available with modifiers that do not affect the topology (typically, *Deform* modifiers only).

   .. _bpy.ops.object.modifier_copy:

   Duplicate :kbd:`Shift-D`
      Creates a duplicate of the modifier just below current one in the stack.

   .. _bpy.ops.object.modifier_copy_to_selected:

   Copy to Selected
      Copies the modifier from the :term:`Active` object to all selected objects.

   .. _bpy.ops.object.modifier_move_to_index:

   Move to First/Last
      Moves the modifier to the first or last position in the modifier stack.

   .. _bpy.types.Modifier.use_pin_to_last:

   Pin to Last
      Keeps the modifier at the end of the modifier stack.
      When a modifier is pinned, a pin icon will be displayed on the right side of the panel's header.
   Move to Nodes
      Converts the existing :doc:`/modeling/modifiers/geometry_nodes`
      node tree to a group node to be reused in other node trees.
      See :ref:`bpy.ops.object.geometry_nodes_move_to_nodes` for more information.

      This operator is only available for the Geometry Nodes Modifier.

.. _bpy.ops.object.modifier_remove:

Delete :kbd:`X`, :kbd:`Delete`
   Delete the modifier.

:bl-icon:`grip` (Move)
   Move the modifier up/down in the :ref:`stack <modifier-stack>`,
   changing the evaluation order of the modifiers.

   A modifier is not movable if :ref:`Pin to Last <bpy.types.Modifier.use_pin_to_last>` is enabled.

Below this header, all of the options unique to each modifier will be displayed.

.. tip::

   Use :kbd:`Alt` to affect all selected objects at once
   when performing operators such as add, apply, remove, and move to index.

   See :ref:`3dview-multi-object-mode` for more information.


.. _modifier-stack:

The Modifier Stack
------------------

Modifiers are a series of non-destructive operations which can be applied on top of an object's geometry.
You can be apply them in almost any order.
This kind of functionality is often referred to as a "modifier stack"
and is also found in several other 3D applications.

In a modifier stack, the order in which modifiers are applied has an effect on the result.
Therefore the modifiers can be re-arranged by clicking :bl-icon:`grip` (grip icon) in the top right,
and moving the selected modifier up or down.
For example, the image below shows :doc:`Subdivision Surface </modeling/modifiers/generate/subdivision_surface>`
and :doc:`Mirror </modeling/modifiers/generate/mirror>` modifiers that have switched places.

.. list-table:: Modifier Stack example.

   * - .. figure:: /images/modeling_modifiers_introduction_mirror-subdiv2.png
          :width: 320px

          The Mirror modifier is the last item in the stack and
          the result looks like two surfaces.

     - .. figure:: /images/modeling_modifiers_introduction_mirror-subdiv1.png
          :width: 320px

          The Subdivision Surface modifier is the last
          item in the stack and the result is a single merged surface.

Modifiers are calculated from top to bottom in the stack.
In this example, the desired result (on right) is achieved by first mirroring the object,
and then calculating the subdivision surface.


.. _modifier-stack-active:

Active Modifier
^^^^^^^^^^^^^^^

A modifier in the stack can be selected to mark in as :term:`Active`,
the active modifier displays an outline around the modifier's panel.
To set an active modifier, select an area of the modifier's panel background,
the modifier's icon, or, select a modifier in the :doc:`/editors/outliner/index`.

The active modifier is used by the :doc:`/editors/geometry_node`
to determine which node group is being modified.


Example
=======

.. figure:: /images/modeling_modifiers_introduction_stack-example-3.png

   In this example a simple subdivided cube has been transformed into a rather complex object using
   a stack of modifiers.

`Download example file <https://archive.blender.org/wiki/2015/index.php/File:25-Manual-Modifiers-example.blend>`__.
