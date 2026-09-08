
***********************
Common Modifier Options
***********************

Some options are commonly used by many modifiers, and share the same behavior across all of those.
In particular, many offer ways to precisely mask and weight their effect on a vertex basis
(using either vertex groups and/or textures).


.. _modifiers-common-options-masking:

Vertex Group
============

.. figure:: /images/modeling_modifiers_common-options_vertex-group.png
   :align: right

   Typical modifier Vertex Group options.

:doc:`Vertex Groups </modeling/meshes/properties/vertex_groups/introduction>` are an easy way to control
which vertices are affected by a modifier, and to which extent (using their weights).
They are available when modifying meshes or lattices.

.. tip::

   Vertex groups can also be edited and even animated using
   the :ref:`Vertex Weight modifiers <bpy.types.VertexWeightEditModifier>`.

Vertex Group
   The vertex group name.

   .. warning::

      The group is referenced by its name. That means that if you rename it, the link to the renamed vertex group
      will be lost by all modifiers using it (their field will turn red),
      and you'll have to select the proper group again in all of them.

   :bl-icon:`arrow_leftright` Invert
      Inverts the influence of the selected vertex group, meaning that the group
      now represents vertices that will not be deformed by the modifier.

      The setting reverses the weight values of the group.
      Only available in some modifiers.


Texture
=======

.. figure:: /images/modeling_modifiers_common-options_texture.png
   :align: right

   Typical modifier Texture options.

Those options allow to use any kind of image (including parametric ones) to control the modifier's effect.
Most of the time, only the value (grayscale) of the texture is used,
but in some cases (like with some modes of the :ref:`Displace modifier <bpy.types.DisplaceModifier>`),
the whole RGB color components might be exploited.

.. tip::

   Textures can be animated (either using videos, or by animating the mapping coordinates...).

Texture
   The :doc:`texture data-block </render/materials/legacy_textures/introduction>` to use.

   .. tip::

      Clicking on :bl-icon:`properties` (properties icon) takes you directly
      to the selected texture's settings in the *Texture Properties* tab.

Texture Coordinates
   The texture's coordinates to get each vertex' value:

   UV
      Take texture coordinates from face UV coordinates.

      UV Map
         The :term:`UV Map` from which to take texture coordinates. If the object has no
         UV coordinates, it falls back to the *Local* coordinate system. If this field is blank,
         but there is a UV map available (e.g. just after adding the first UV map to the mesh),
         the currently active UV map will be used.

      .. note::

         Since UV coordinates are specified per face, the UV texture coordinate system currently determines the UV
         coordinate for each vertex from the first face encountered which uses that vertex.
         Any other faces using that vertex are ignored.

         This may lead to artifacts if the mesh has non-contiguous UV coordinates.

   Object
      Take the texture coordinates from another object's coordinate system.

      Object
         The object from which to take texture coordinates.
         Moving the object will therefore alter the coordinates of the texture mapping.

         If this field is blank, it falls back to the *Local* coordinate system.

      .. note::

         Moving the original object will **also** result in a texture coordinate update.
         As such, if you need to maintain a displacement coordinate system while moving the modified object,
         consider :ref:`parenting <bpy.ops.object.parent_set>` the coordinate object to the modified object.

   Global
      Take the texture coordinates from the global coordinate system.
   Local
      Take the texture coordinates from the object's local coordinate system.

Use Channel
   Which channel to use as value source
   (only available with a few modifiers currently, others follow the *Intensity* behavior,
   unless otherwise specified).

   Intensity
      The average of the RGB channels (if RGB(1.0, 0.0, 0.0) value is 0.33).
   Red/Green/Blue/Alpha
      One of the color channels' values.
   Hue
      The hue from the HSV color model
      (i.e; the color in the standard wheel, e.g. blue has a higher hue value than yellow).
   Saturation
      The saturation from the HSV color model (e.g. the value for pure red is 1.0, for gray is 0.0).
   Value
      The value from the HSV color model.

   .. note::

      All of the channels above are gamma corrected, except for *Intensity*.
