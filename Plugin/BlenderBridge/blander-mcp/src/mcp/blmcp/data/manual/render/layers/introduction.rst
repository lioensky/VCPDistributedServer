.. _bpy.ops.scene.view_layer:
.. _bpy.types.ViewLayer:

************
Introduction
************

View Layers allow you to separate a render into multiple layers, which can then be composited together.
This is useful for rendering scene elements independently—such as characters, lighting variations, or background
elements—without duplicating the entire scene or re-rendering everything after each change.

For example, you can:

- Apply different compositing effects to foreground and background elements.
- Render characters separately from the environment for post-processing.
- Generate multiple lighting passes without modifying the original scene setup.

View Layers also improve performance and flexibility during iteration by letting you re-render only the layers
that have changed.

.. figure:: /images/scene-layout_view-layers_introduction_collections.png

   View Layers and collections.

Each View Layer references a combination of :doc:`Collections </scene_layout/collections/introduction>`,
which define the visibility, selectability, and contribution of scene objects in the final render.
Multiple View Layers can use the same or different collections, allowing for tailored layer setups.


Selecting View Layers
=====================

At the top of the *View Layer Properties* tab is a list of all View Layers in the active scene.

.. figure:: /images/render_layers_introduction_list.png

   View Layers list.

.. _bpy.types.ViewLayer.name:

Name
   The name of the active View Layer. Click to edit.

.. _bpy.ops.scene.view_layer_add:

Add View Layer
   Adds a new View Layer to the scene.

   - **New**: Adds an empty View Layer.
   - **Copy Settings**: Duplicates the current View Layer, including collection visibility and overrides.
   - **Blank**: Adds a new View Layer with all collections disabled.

.. _bpy.ops.scene.view_layer_remove:

Remove View Layer
   Deletes the selected View Layer from the scene.

   .. note::

      Each scene must contain at least one View Layer.


Usage
=====

Visibility Management
---------------------

Each :doc:`Scene </scene_layout/scene/introduction>` consists of one or more
:doc:`Collections </scene_layout/collections/collections>`.
Collections can be enabled or disabled per View Layer, allowing you to control what appears in each layer's render.

This makes it easy to separate lighting, characters, props, or effects into their own passes.

Collection visibility for each View Layer can be adjusted in the :ref:`Outliner
<editors-outliner-editing-collections>` or :ref:`Collection View Layer Properties <bpy.types.LayerCollection>`.

.. figure:: /images/scene-layout_view-layers_introduction_outliner.png

   View Layer collections in the Outliner.

From the Outliner, you can:

- Enable or disable collections per View Layer.
- Set holdout and indirect-only options (Cycles only).
- Manage what objects contribute to the render or compositing.


Rendering & Compositing
-----------------------

When a scene is rendered, each View Layer is available in the
:doc:`Compositor </compositing/introduction>` using they :doc:`/compositing/types/input/scene/render_layers`.
This allows you to process each layer independently, combining or adjusting them to create the final output.

Each View Layer can output multiple :doc:`Render Passes </render/layers/passes>` including:

- Combined (final image)
- Diffuse, Glossy, Transmission components
- Shadow, Mist, Ambient Occlusion
- Cryptomatte and Object/Material/ID Masks
- Data passes like Normal, UV, and Depth

These passes make it possible to perform detailed color grading,
masking, relighting, and other post-processing operations in a non-destructive workflow.
