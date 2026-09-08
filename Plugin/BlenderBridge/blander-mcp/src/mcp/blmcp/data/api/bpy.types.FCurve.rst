FCurve(bpy_struct)
==================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: FCurve(bpy_struct)

   F-Curve defining values of a period of time

   .. attribute:: array_index

      Index to the specific property affected by F-Curve if applicable (in [0, inf], default 0)

      :type: int

   .. attribute:: auto_smoothing

      Algorithm used to compute automatic handles (default ``'NONE'``)

      :type: Literal[:ref:`rna_enum_fcurve_auto_smoothing_items`]

   .. attribute:: color

      Color of the F-Curve in the Graph Editor (array of 3 items, in [0, 1], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. attribute:: color_mode

      Method used to determine color of F-Curve in Graph Editor (default ``'AUTO_RAINBOW'``)

      - ``AUTO_RAINBOW``
        Auto Rainbow -- Cycle through the rainbow, trying to give each curve a unique color.
      - ``AUTO_RGB``
        Auto XYZ to RGB -- Use axis colors for transform and color properties, and auto-rainbow for the rest.
      - ``AUTO_YRGB``
        Auto WXYZ to YRGB -- Use WXYZ axis colors for quaternion/axis-angle rotations, XYZ axis colors for other transform and color properties, and auto-rainbow for the rest.
      - ``CUSTOM``
        User Defined -- Use custom hand-picked color for F-Curve.

      :type: Literal['AUTO_RAINBOW', 'AUTO_RGB', 'AUTO_YRGB', 'CUSTOM']

   .. attribute:: data_path

      RNA Path to property affected by F-Curve (default "", never None)

      :type: str

   .. data:: driver

      Channel Driver (only set for Driver F-Curves) (readonly)

      :type: :class:`Driver` | None

   .. attribute:: extrapolation

      Method used for evaluating value of F-Curve outside first and last keyframes (default ``'CONSTANT'``)

      - ``CONSTANT``
        Constant -- Hold values of endpoint keyframes.
      - ``LINEAR``
        Linear -- Use slope of curve leading in/out of endpoint keyframes.

      :type: Literal['CONSTANT', 'LINEAR']

   .. attribute:: group

      Action Group that this F-Curve belongs to

      :type: :class:`ActionGroup` | None

   .. attribute:: hide

      F-Curve and its keyframes are hidden in the Graph Editor graphs (default True)

      :type: bool

   .. data:: is_empty

      True if the curve contributes no animation due to lack of keyframes or useful modifiers, and should be deleted (default False, readonly)

      :type: bool

   .. attribute:: is_valid

      False when F-Curve could not be evaluated in past, so should be skipped when evaluating (default True)

      :type: bool

   .. data:: keyframe_points

      User-editable keyframes (default None, readonly)

      :type: :class:`FCurveKeyframePoints`\ [:class:`Keyframe`]

   .. attribute:: lock

      F-Curve's settings cannot be edited (default False)

      :type: bool

   .. data:: modifiers

      Modifiers affecting the shape of the F-Curve (default None, readonly)

      :type: :class:`FCurveModifiers`\ [:class:`FModifier`]

   .. attribute:: mute

      Disable F-Curve evaluation (default False)

      :type: bool

   .. data:: sampled_points

      Sampled animation data (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`FCurveSample`]

   .. attribute:: select

      F-Curve is selected for editing (default False)

      :type: bool

   .. method:: evaluate(frame)

      Evaluate F-Curve

      :param frame: Frame, Evaluate F-Curve at given frame (in [-inf, inf])
      :type frame: float
      :return: Value, Value of F-Curve specific frame (in [-inf, inf])
      :rtype: float

   .. method:: update()

      Ensure keyframes are sorted in chronological order and handles are set correctly


   .. method:: range()

      Get the time extents for F-Curve

      :return: Range, Min/Max values (array of 2 items, in [-inf, inf])
      :rtype: :class:`mathutils.Vector`

   .. method:: update_autoflags(data)

      Update FCurve flags set automatically from affected property (currently, integer/discrete flags set when the property is not a float)

      :param data: Data, Data containing the property controlled by given FCurve (never None)
      :type data: :class:`AnyType` | None

   .. method:: convert_to_samples(start, end)

      Convert current FCurve from keyframes to sample points, if necessary

      :param start: Start Frame, (in [-1048574, 1048574])
      :type start: int
      :param end: End Frame, (in [-1048574, 1048574])
      :type end: int

   .. method:: convert_to_keyframes(start, end)

      Convert current FCurve from sample points to keyframes (linear interpolation), if necessary

      :param start: Start Frame, (in [-1048574, 1048574])
      :type start: int
      :param end: End Frame, (in [-1048574, 1048574])
      :type end: int

   .. method:: bake(start, end, *, step=1.0, remove='IN_RANGE')

      Place keys at even intervals on the existing curve.

      :param start: Start Frame, Frame at which to start baking (in [-1048574, 1048574])
      :type start: int
      :param end: End Frame, Frame at which to end baking (inclusive) (in [-1048574, 1048574])
      :type end: int
      :param step: Step, At which interval to add keys (in [0.01, inf], optional)
      :type step: float
      :param remove: Remove Options, Choose which keys should be automatically removed by the bake (optional)

         - ``NONE``
           None -- Keep all keys.
         - ``IN_RANGE``
           In Range -- Remove all keys within the defined range.
         - ``OUT_RANGE``
           Outside Range -- Remove all keys outside the defined range.
         - ``ALL``
           All -- Remove all existing keys.
      :type remove: Literal['NONE', 'IN_RANGE', 'OUT_RANGE', 'ALL']

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

   - :mod:`bpy.context.active_editable_fcurve`
   - :mod:`bpy.context.editable_fcurves`
   - :mod:`bpy.context.selected_editable_fcurves`
   - :mod:`bpy.context.selected_visible_fcurves`
   - :mod:`bpy.context.visible_fcurves`
   - :class:`Action.fcurve_ensure_for_datablock`
   - :class:`ActionChannelbag.fcurves`
   - :class:`ActionChannelbagFCurves.ensure`
   - :class:`ActionChannelbagFCurves.find`
   - :class:`ActionChannelbagFCurves.new`
   - :class:`ActionChannelbagFCurves.new_from_fcurve`
   - :class:`ActionChannelbagFCurves.new_from_fcurve`
   - :class:`ActionChannelbagFCurves.remove`
   - :class:`ActionGroup.channels`
   - :class:`AnimData.drivers`
   - :class:`AnimDataDrivers.find`
   - :class:`AnimDataDrivers.from_existing`
   - :class:`AnimDataDrivers.from_existing`
   - :class:`AnimDataDrivers.new`
   - :class:`AnimDataDrivers.remove`
   - :class:`NlaStrip.fcurves`
   - :class:`NlaStripFCurves.find`

