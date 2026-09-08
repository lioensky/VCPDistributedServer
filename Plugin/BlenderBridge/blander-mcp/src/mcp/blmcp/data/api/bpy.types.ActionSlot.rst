ActionSlot(bpy_struct)
======================

.. currentmodule:: bpy.types


Action Slots organize animation data within an action. Each action has slots with specific animation
data. An animated data-block specifies an action and a slot, determining the animation data it uses.
See the `Blender Manual <https://docs.blender.org/manual/en/5.1/animation/actions.html#action-slots>`_
for how Action Slots are used, or the
`technical documentation <https://developer.blender.org/docs/features/animation/>`_
for details on the animation system's architecture.

Create & Access an Action Slot
++++++++++++++++++++++++++++++

To get started with Action Slots, you can easily create them by inserting a keyframe on an object. When you do this,
Blender automatically creates an Action & Slot for that data-block.

.. literalinclude:: ./examples/bpy.types.ActionSlot.1.py
   :lines: 16-


Manually Create an Action Slot
++++++++++++++++++++++++++++++
If required you can also manually create Action Slots on an Action. Note the ``target_id_type``
that matches the data-block type. Identifiers start with a prefix based on the ID type,
e.g. "OB" for objects, followed by the name. There can be identifiers like ``OBSuzanne``
and ``MESuzanne`` and the name (``Suzanne``) can be shared between them. This is intentional,
so that the slots and the datablocks can have the same name.

.. literalinclude:: ./examples/bpy.types.ActionSlot.2.py
   :lines: 11-


Explicitly Assigning Action Slots
+++++++++++++++++++++++++++++++++
An action slot is compatible with a data-block if the slot's ``target_id_type`` matches the data-block's type.
If there are multiple slots on the Action, and you want to just pick the first one that's
compatible, use the following code. ``anim_data.action_suitable_slots`` can be used `after` the
Action has been assigned; it is a list of action slots of that Action, but only the ones that
are actually compatible with the owner of anim_data (in this case, Suzanne).

.. literalinclude:: ./examples/bpy.types.ActionSlot.3.py
   :lines: 11-


Finding Action Slot Users
+++++++++++++++++++++++++

To return a list of the data-blocks that are animated by a specific slot of an Action,
use the ``users()`` method of the ActionSlot.

.. literalinclude:: ./examples/bpy.types.ActionSlot.4.py
   :lines: 9-

base class --- :class:`bpy_struct`

.. class:: ActionSlot(bpy_struct)

   Identifier for a set of channels in this Action, that can be used by a data-block to specify what it gets animated by

   .. data:: active

      Whether this is the active slot, can be set by assigning to action.slots.active (default False, readonly)

      :type: bool

   .. data:: handle

      Number specific to this Slot, unique within the Action.
      This is used, for example, on a ActionKeyframeStrip to look up the ActionChannelbag for this Slot
      
      (in [-inf, inf], default 0, readonly)

      :type: int

   .. attribute:: identifier

      Used when connecting an Action to a data-block, to find the correct slot handle. This is the display name, prefixed by two characters determined by the slot's ID type (default "", never None)

      :type: str

   .. attribute:: name_display

      Name of the slot, for display in the user interface. This name combined with the slot's data-block type is unique within its Action (default "", never None)

      :type: str

   .. attribute:: select

      Selection state of the slot (default False)

      :type: bool

   .. attribute:: show_expanded

      Expanded state of the slot (default False)

      :type: bool

   .. attribute:: target_id_type

      Type of data-block that this slot is intended to animate; can be set when 'UNSPECIFIED' but is otherwise read-only (default ``'UNSPECIFIED'``)

      - ``ACTION``
        Action.
      - ``ARMATURE``
        Armature.
      - ``BRUSH``
        Brush.
      - ``CACHEFILE``
        Cache File.
      - ``CAMERA``
        Camera.
      - ``COLLECTION``
        Collection.
      - ``CURVE``
        Curve.
      - ``CURVES``
        Curves.
      - ``FONT``
        Font.
      - ``GREASEPENCIL``
        Grease Pencil.
      - ``GREASEPENCIL_V3``
        Grease Pencil v3.
      - ``IMAGE``
        Image.
      - ``KEY``
        Key.
      - ``LATTICE``
        Lattice.
      - ``LIBRARY``
        Library.
      - ``LIGHT``
        Light.
      - ``LIGHT_PROBE``
        Light Probe.
      - ``LINESTYLE``
        Line Style.
      - ``MASK``
        Mask.
      - ``MATERIAL``
        Material.
      - ``MESH``
        Mesh.
      - ``META``
        Metaball.
      - ``MOVIECLIP``
        Movie Clip.
      - ``NODETREE``
        Node Tree.
      - ``OBJECT``
        Object.
      - ``PAINTCURVE``
        Paint Curve.
      - ``PALETTE``
        Palette.
      - ``PARTICLE``
        Particle.
      - ``POINTCLOUD``
        Point Cloud.
      - ``SCENE``
        Scene.
      - ``SCREEN``
        Screen.
      - ``SOUND``
        Sound.
      - ``SPEAKER``
        Speaker.
      - ``TEXT``
        Text.
      - ``TEXTURE``
        Texture.
      - ``VOLUME``
        Volume.
      - ``WINDOWMANAGER``
        Window Manager.
      - ``WORKSPACE``
        Workspace.
      - ``WORLD``
        World.
      - ``UNSPECIFIED``
        Unspecified -- Not yet specified. When this slot is first assigned to a data-block, this will be set to the type of that data-block.

      :type: Literal['ACTION', 'ARMATURE', 'BRUSH', 'CACHEFILE', 'CAMERA', 'COLLECTION', 'CURVE', 'CURVES', 'FONT', 'GREASEPENCIL', 'GREASEPENCIL_V3', 'IMAGE', 'KEY', 'LATTICE', 'LIBRARY', 'LIGHT', 'LIGHT_PROBE', 'LINESTYLE', 'MASK', 'MATERIAL', 'MESH', 'META', 'MOVIECLIP', 'NODETREE', 'OBJECT', 'PAINTCURVE', 'PALETTE', 'PARTICLE', 'POINTCLOUD', 'SCENE', 'SCREEN', 'SOUND', 'SPEAKER', 'TEXT', 'TEXTURE', 'VOLUME', 'WINDOWMANAGER', 'WORKSPACE', 'WORLD', 'UNSPECIFIED']

   .. data:: target_id_type_icon

      (in [-inf, inf], default 0, readonly)

      :type: int

   .. method:: users()

      Return the data-blocks that are animated by this slot of this action

      :return: users
      :rtype: :class:`bpy_prop_collection`\ [:class:`ID`]

   .. method:: duplicate()

      Duplicate this slot, including all the animation data associated with it

      :return: Duplicated Slot, The slot created by duplicating this one
      :rtype: :class:`ActionSlot`

   .. classmethod:: bl_rna_get_subclass(id, default=None, /)
   
      :param id: The RNA type identifier.
      :type id: str
      :param default: The value to return when not found.
      :type default: :class:`bpy.types.Struct` | None
      :return: The RNA type or default when not found.
      :rtype: :class:`bpy.types.Struct`


   .. classmethod:: bl_rna_get_subclass_py(id, default=None, /)
   
      :param id: The RNA type identifier.
      :type id: str
      :param default: The value to return when not found.
      :type default: type | None
      :return: The class or default when not found.
      :rtype: type


Inherited Properties
--------------------

.. hlist::
   :columns: 2

   - :class:`bpy_struct.id_data`

Inherited Functions
-------------------

.. hlist::
   :columns: 2

   - :class:`bpy_struct.as_pointer`
   - :class:`bpy_struct.driver_add`
   - :class:`bpy_struct.driver_remove`
   - :class:`bpy_struct.get`
   - :class:`bpy_struct.id_properties_clear`
   - :class:`bpy_struct.id_properties_ensure`
   - :class:`bpy_struct.id_properties_ui`
   - :class:`bpy_struct.is_property_hidden`
   - :class:`bpy_struct.is_property_overridable_library`
   - :class:`bpy_struct.is_property_readonly`
   - :class:`bpy_struct.is_property_set`
   - :class:`bpy_struct.items`
   - :class:`bpy_struct.keyframe_delete`
   - :class:`bpy_struct.keyframe_insert`
   - :class:`bpy_struct.keys`
   - :class:`bpy_struct.path_from_id`
   - :class:`bpy_struct.path_from_module`
   - :class:`bpy_struct.path_resolve`
   - :class:`bpy_struct.pop`
   - :class:`bpy_struct.property_overridable_library_set`
   - :class:`bpy_struct.property_unset`
   - :class:`bpy_struct.rna_ancestors`
   - :class:`bpy_struct.type_recast`
   - :class:`bpy_struct.values`

References
----------

.. hlist::
   :columns: 2

   - :class:`Action.slots`
   - :class:`ActionChannelbag.slot`
   - :class:`ActionChannelbags.new`
   - :class:`ActionConstraint.action_slot`
   - :class:`ActionConstraint.action_suitable_slots`
   - :class:`ActionKeyframeStrip.channelbag`
   - :class:`ActionKeyframeStrip.key_insert`
   - :class:`ActionSlot.duplicate`
   - :class:`ActionSlots.active`
   - :class:`ActionSlots.new`
   - :class:`ActionSlots.remove`
   - :class:`AnimData.action_slot`
   - :class:`AnimData.action_suitable_slots`
   - :class:`NlaStrip.action_slot`
   - :class:`NlaStrip.action_suitable_slots`

