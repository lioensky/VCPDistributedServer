*************
Light Linking
*************

.. _bpy.types.Object.light_linking:

With light linking, you can set up lights that only illuminate specific objects in the scene.
Shadow linking additionally gives control over which objects block the light (cast shadows).

This adds more artistic control by breaking the laws of physics. For example, you could
have a rim light that *only* illuminates a character in a scene (light linking) and is
not blocked by any objects in the scene (shadow linking).


Setup
=====

- Select the light or emissive mesh object and go to the
  :ref:`Cycles Shading panel <render-cycles-object-light-linking-settings>` or
  :ref:`EEVEE Shading panel <render-eevee-object-light-linking-settings>`.
- Create a new light/shadow linking collection.
- Drag & drop objects or collections from the :doc:`Outliner </editors/outliner/introduction>`
  onto the list.

You can also use the :doc:`/scene_layout/object/editing/link_transfer/link_data` menu for this:
select the objects, add the light to the selection, press :kbd:`Ctrl-L`, and choose
:menuselection:`Link Receivers/Blockers to Emitter`.

.. note::
  Emissive mesh objects only support light linking with Cycles.

  :doc:`Grease Pencil </grease_pencil/introduction>` objects don't support light linking at all.

Multiple light objects can use the same linking collection. They can also use an existing scene collection,
but in general, it's recommended to create dedicated linking collections so you can change these
without affecting the scene layout.


Include & Exclude
=================

Light receiver/blocker objects can be set to be either included or excluded.
The behavior is as follows:

- If only included objects are specified, the light only affects those objects.
- If only excluded objects are specified, the light affects all objects in the scene except those specified.
- If both included and excluded objects are specified, the light affects only included objects minus the excluded
  objects. This can be used to for example set a character collection to be included, and then exclude specific
  objects part of the character.


Performance
===========

Sampling for light linking is most efficient with the :ref:`light tree
<bpy.types.CyclesRenderSettings.use_light_tree>` enabled, where a specialized acceleration structure is built for
light linking.

When using shadow linking, renders can be slower and trace additional rays,
as direct and indirect lighting take different paths.
