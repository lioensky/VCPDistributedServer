
****************
Shape Keys Panel
****************

.. reference::

   :Editor:    Properties
   :Mode:      All modes
   :Panel:     :menuselection:`Object Data --> Shape Keys`

.. figure:: /images/animation_shape-keys_shape-keys-panel_basis.png
   :align: right
   :width: 296px

   Shape Keys panel.


The *Shape Keys* panel is used to create, organize, and manage shape keys.
It presents a tree view where shape keys can be reordered by click-dragging.

.. container:: lead

   .. clear

.. _bpy.types.Object.active_shape_key_index:

Shape Key element

   .. _bpy.types.ShapeKey.frame:

   Value/Frame (number)
      In Relative mode: Value is the current influence of the shape key used for blending between
      the shape (value=1.0) and its reference key (value=0.0). The reference key is usually the Basis shape.
      The weight of the blend can be extrapolated above 1.0 and below 0.0.

      In Absolute mode: Value is the *Evaluation Time* at which the shape will have maximum influence.

   .. _bpy.types.ShapeKey.mute:

   :bl-icon:`checkbox_hlt` / :bl-icon:`checkbox_dehlt` Mute
      If unchecked, the shape key will not be taken into consideration when
      mixing the shape key stack into the result visible in the 3D Viewport.

   .. _bpy.types.ShapeKey.lock_shape:

   :bl-icon:`unlocked` / :bl-icon:`locked` Lock Shape
      Shape keys can be locked to protect them from accidental modification due to inadvertently
      selecting the wrong key for editing in the list. Most common sculpt and edit mode operators
      and tools that move vertices abort with an error if the active shape key is locked.

      .. note::

         Operators that always modify all shape keys in exactly the same way, like
         :ref:`Apply Object Transforms <bpy.ops.object.transform_apply>`, don't check shape key locks.
         Neither currently do most edit mode operators that modify topology, because the topology is
         expected to usually be finalized before shape keys are created.

Shape Key Specials
   .. _bpy.ops.object.shape_key_add:

   New Combined
      Add a new shape key with the current deformed shape of the object.
      This differs from the :bl-icon:`add` button of the list, as that one always copies
      the Basis shape independently of the current mix.

   .. _bpy.ops.object.shape_key_copy:

   Duplicate
      Creates a copy of the active shape key.

   .. _bpy.ops.object.join_shapes:

   New from Objects
      Add the vertex positions of selected objects as new shape keys,
      or update existing shape keys with matching names.

      To use, select the object(s) to copy shape data *from*,
      then the target object to copy shape data *to*, and perform the operation.

   New from Objects Flipped
      Creates new shape keys from selected objects while mirroring the vertex positions
      across the local X axis. This is typically used when creating symmetrical shape keys
      (for example, generating a *Left Smile* from a *Right Smile* shape).

      The operation requires the topology of all involved meshes to match.

   .. _bpy.ops.object.update_shapes:

   Update from Objects
      Updates existing shape keys of the active object with the vertex positions of
      selected objects that have shape keys with matching names.

      To use, select the object(s) to update shape data *from*, then the target object to
      update *into*, and perform the operation.

   Update from Objects Flipped
      Similar to *Update from Objects*, but applies a mirrored update across the local X axis.
      This is useful for updating symmetrical shape keys when working with mirrored geometry
      or pose-corrective shapes.

   .. _bpy.ops.object.shape_key_mirror:

   Flip
      If your mesh is symmetrical, in *Object Mode*, you can mirror the shape keys on the X axis.

      This will not work unless the mesh vertices are perfectly symmetrical.
      Use the :menuselection:`Mesh --> Symmetrize` tool in *Edit Mode*.

   Flip (Topology)
      Same as *Mirror Shape Key* though it detects the mirrored vertices based on the topology of the mesh.
      The mesh vertices do not have to be perfectly symmetrical for this action to work.

  .. _bpy.ops.object.shape_key_make_basis:

   Make Basis
      Makes the selected shape key the new *Basis* shape key. The vertex positions of the
      active shape key are applied to the base mesh, and all other shape keys are adjusted
      relative to this new basis.

      This operation is useful when a corrective or edited shape key should become the
      default shape of the mesh instead of the original basis.

   Apply All
      Saves the current visible shape to the mesh data and deletes all Shape Keys.

   .. _bpy.ops.object.shape_key_remove:

   Delete All
      Removes all Shape Keys and any effect that they had on the mesh.

   .. .. _bpy.ops.object.shape_key_transfer:

   .. Transfer Shape Key
   ..    Transfer the active shape key from a different object regardless of its current influence.

   ..    To use, select the object to copy from, then the object to copy into, then perform the operation.

.. _bpy.types.Key.use_relative:

Relative
   Set the shape keys to *Relative* or *Absolute*.
   See :ref:`animation-shapekeys-relative-vs-absolute`.

.. _bpy.types.Object.show_only_shape_key:

Shape Key Lock (pin icon)
   Show the active shape in the 3D Viewport without blending.
   *Shape Key Lock* gets automatically enabled while the object is in *Edit Mode*.

.. _bpy.types.Object.use_shape_key_edit_mode:

Shape Key Edit Mode (edit mode icon)
   If enabled, when entering *Edit Mode* the active shape key will **not** take maximum influence as is default.
   Instead, the current blend of shape keys will be visible and can be edited from that state.

.. _bpy.types.Object.add_rest_position_attribute:

Add Rest Position
   Creates an :doc:`Attribute </modeling/geometry_nodes/attributes_reference>` in the vertex domain called
   ``rest_position`` which is a copy of the ``position`` attribute before shape keys and modifiers are evaluated.
   Only mesh objects support this option.


Relative Shape Keys
===================

.. figure:: /images/animation_shape-keys_shape-keys-panel_relative.png
   :align: right
   :width: 296px

   Relative Shape Keys options.

See :ref:`animation-shapekeys-relative-vs-absolute`.

With relative shape keys, the value shown for each shape in the list represents
the current weight or influence of that shape in the current *Mix*.

.. container:: lead

   .. clear

.. _bpy.ops.object.shape_key_clear:

:bl-icon:`x` (Clear Shape Keys)
   Set all influence values, or weights, to zero.
   Useful to quickly guarantee that the result shown in the 3D Viewport is not affected by shapes.

.. _bpy.types.ShapeKey.value:

Value
   The weight of the blend between the shape key and its reference key (usually the Basis shape).

   A value of 0.0 denotes 100% influence of the reference key and 1.0 of the shape key.

.. _bpy.types.ShapeKey.slider_min:
.. _bpy.types.ShapeKey.slider_max:

Range
   Minimum and maximum range for the influence value of the active shape key.
   Blender can extrapolate results when the *Value* goes lower than 0.0 or above 1.0.

.. _bpy.types.ShapeKey.vertex_group:

Vertex Group
   Limit the active shape key deformation to a vertex group.
   Useful to break down a complex shape into components by assigning temporary vertex groups
   to the complex shape and copying the result into new simpler shapes.

.. _bpy.types.ShapeKey.relative_key:

Relative To
   Select the shape key to deform from. This is called the *Reference Key* for that shape.

.. note::

   Rather than storing offsets directly, internally relative keys are stored as snapshots of the mesh shape.
   The relative deformation offsets are computed by subtracting *Reference Key* from that snapshot.

   Therefore, replacing the *Reference Key* has the effect of subtracting the difference between the new
   and old reference from the relative deformation of the current key.

Absolute Shape Keys
===================

.. figure:: /images/animation_shape-keys_shape-keys-panel_absolute.png
   :align: right
   :width: 296px

   Absolute Shape Keys options.

See :ref:`animation-shapekeys-relative-vs-absolute`.

With absolute shape keys, the value shown for each shape in the list represents
the *Evaluation Time* at which that shape key will be active.

.. container:: lead

   .. clear

.. _bpy.ops.object.shape_key_retime:

Re-Time Shape Keys (clock icon)
   Absolute shape keys are timed, by order in the list, at a constant interval.
   This button resets the timing for the keys. Useful if keys were removed or re-ordered.

.. _bpy.types.ShapeKey.interpolation:

Interpolation
   Controls the interpolation between shape keys.

   Linear, Cardinal, Catmull-Rom, B-Spline

   .. _fig-interpolation-type:

   .. figure:: /images/animation_shape-keys_shape-keys-panel_interpolation-types.png

      Different types of interpolation.

      The red line represents interpolated values between keys (black dots).

.. _bpy.types.Key.eval_time:

Evaluation Time
   Controls the shape key influence. Scrub to see the effect of the current configuration.
   Typically, this property is keyed for animation or rigged with a driver.
