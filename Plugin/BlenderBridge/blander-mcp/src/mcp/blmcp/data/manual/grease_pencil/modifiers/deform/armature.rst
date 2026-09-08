.. index:: Grease Pencil Modifiers; Armature Modifier
.. _bpy.types.GreasePencilArmatureModifier:

*****************
Armature Modifier
*****************

The *Armature* Modifier is used for building skeletal systems for animating
the poses of characters and anything else which needs to be posed.

By adding an armature to an object,
this object can be deformed accurately so that geometry does not have to be animated by hand.

.. seealso::

   For more details on armatures usage, see the :doc:`armature section </animation/armatures/index>`.

.. seealso::

   This documentation refers to the Armature Modifier specific to the Grease Pencil object.
   For uses with other object types refer to the general :doc:`/modeling/modifiers/deform/armature`.


Options
=======

.. figure:: /images/grease-pencil_modifiers_deform_armature_panel.png
   :align: right

   The Armature modifier.

Object
   The name of the armature object used by this modifier.

Vertex Group
   The name of a vertex group of the object, the weights of which will be used to determine the influence of this
   Armature Modifier's result when mixing it with the results from other *Armature* ones.

   Only meaningful when having at least two of these modifiers on the same object,
   with *Multi Modifier* activated.

   :bl-icon:`arrow_leftright` Invert
      Inverts the influence set by the vertex group defined in previous setting
      (i.e. reverses the weight values of this group).

Bind to
   Vertex Groups
      When enabled, bones of a given name will deform points which belong to
      :doc:`vertex groups </modeling/meshes/properties/vertex_groups/index>` of the same name.
      E.g. a bone named "forearm", will only affect the points in the "forearm" vertex group.

      The influence of one bone on a given point is controlled by the weight of this point in the relevant group.
      A much more precise method than *Bone Envelopes*, but also generally longer to set up.
   Bone Envelopes
      When enabled, bones will deform points or control points near them,
      defined by each bone's envelope radius and distance.
      Enable/Disable bone :ref:`envelopes <armature-bones-envelope>` defining the deformation
      (i.e. bones deform points in their neighborhood).
