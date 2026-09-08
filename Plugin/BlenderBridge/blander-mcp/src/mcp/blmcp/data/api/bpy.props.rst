Property Definitions (bpy.props)
================================

.. module:: bpy.props

This module defines properties to extend Blender's internal data. The result of these functions is used to assign properties to classes registered with Blender and can't be used directly.

.. note:: All parameters to these functions must be passed as keywords.


Assigning to Existing Classes
+++++++++++++++++++++++++++++

Custom properties can be added to any subclass of an :class:`ID`,
:class:`Bone` and :class:`PoseBone`.

These properties can be animated, accessed by the user interface and Python
like Blender's existing properties.

.. warning::

   Access to these properties might happen in threaded context, on a per-data-block level.
   This has to be carefully considered when using accessors or update callbacks.

   Typically, these callbacks should not affect any other data that the one owned by their data-block.
   When accessing external non-Blender data, thread safety mechanisms should be considered.

.. literalinclude:: ./examples/bpy.props.0.py
   :lines: 21-


Operator Example
++++++++++++++++

A common use of custom properties is for Python based :class:`Operator`
classes. Test this code by running it in the text editor, or by clicking the
button in the 3D Viewport's Tools panel. The latter will show the properties
in the Redo panel and allow you to change them.

.. literalinclude:: ./examples/bpy.props.1.py
   :lines: 11-


PropertyGroup Example
+++++++++++++++++++++

PropertyGroups can be used for collecting custom settings into one value
to avoid many individual settings mixed in together.

.. literalinclude:: ./examples/bpy.props.2.py
   :lines: 9-


Collection Example
++++++++++++++++++

Custom properties can be added to any subclass of an :class:`ID`,
:class:`Bone` and :class:`PoseBone`.

.. literalinclude:: ./examples/bpy.props.3.py
   :lines: 9-


Update Example
++++++++++++++

It can be useful to perform an action when a property is changed and can be
used to update other properties or synchronize with external data.

All properties define update functions except for CollectionProperty.

.. warning::

   Remember that these callbacks may be executed in threaded context.

.. warning::

   If the property belongs to an Operator, the update callback's first
   parameter will be an OperatorProperties instance, rather than an instance
   of the operator itself. This means you can't access other internal functions
   of the operator, only its other properties.

.. literalinclude:: ./examples/bpy.props.4.py
   :lines: 23-


Getter/Setter Example
+++++++++++++++++++++

Accessor functions can be used for boolean, int, float, string and enum properties.

If ``get`` or ``set`` callbacks are defined, the property will not be stored in the ID properties
automatically. Instead, the ``get`` and ``set`` functions will be called when the property
is respectively read or written from the API, and are responsible to handle the data storage.

Note that:

- It is illegal to define a ``set`` callback without a matching ``get`` one.
- When a ``get`` callback is defined but no ``set`` one, the property is read-only.

``get_transform`` and ``set_transform`` can be used when the returned value needs to be modified,
but the default internal storage is still used. They can only transform the value before it is
set or returned, but do not control how/where that data is stored.

.. note::

   It is possible to define both ``get``/``set`` and ``get_transform``/``set_transform`` callbacks
   for the same property. In practice however, this should rarely be needed, as most 'transform'
   operation can also happen within a ``get``/``set`` callback.

.. warning::

   Remember that these callbacks may be executed in threaded context.

.. warning::

   Take care when accessing other properties in these callbacks, as it can easily trigger
   complex issues, such as infinite loops (if e.g. two properties try to also set the other
   property's value in their own ``set`` callback), or unexpected side effects due to changes
   in data, caused e.g. by an ``update`` callback.

.. literalinclude:: ./examples/bpy.props.5.py
   :lines: 38-

.. function:: BoolProperty(*, name="", description="", translation_context="*", default=False, options={'ANIMATABLE'}, override=set(), tags=set(), subtype='NONE', update=None, get=None, set=None, get_transform=None, set_transform=None)

   Returns a new boolean property definition.

   :param name: Name used in the user interface.
   :type name: str
   :param description: Text used for the tooltip and api documentation.
   :type description: str
   :param translation_context: Text used as context to disambiguate translations.
   :type translation_context: str
   :param default: The default value for this property.
   :type default: bool
   :param options: Enumerator in :ref:`rna_enum_property_flag_items`.
   :type options: set[str]
   :param override: Enumerator in :ref:`rna_enum_property_override_flag_items`.
   :type override: set[str]
   :param tags: Enumerator of tags that are defined by parent class.
   :type tags: set[str]
   :param subtype: Enumerator in :ref:`rna_enum_property_subtype_number_items`.
   :type subtype: str
   :param update: Function to be called when this value is modified,
      This function must take 2 values (self, context) and return None.
      *Warning* there are no safety checks to avoid infinite recursion.
   :type update: Callable[[:class:`bpy.types.bpy_struct`, :class:`bpy.types.Context`], None] | None
   :param get: Function to be called when this value is 'read', and the default,
      system-defined storage is not used for this property.
      This function must take 1 value (self) and return the value of the property.

      .. note:: Defining this callback without a matching ``set`` one will make the property read-only (even if ``READ_ONLY`` option is not set).
   :type get: Callable[[:class:`bpy.types.bpy_struct`], bool] | None
   :param set: Function to be called when this value is 'written', and the default,
      system-defined storage is not used for this property.
      This function must take 2 values (self, value) and return None.

      .. note:: Defining this callback without a matching ``get`` one is invalid.
   :type set: Callable[[:class:`bpy.types.bpy_struct`, bool], None] | None
   :param get_transform: Function to be called when this value is 'read',
      if some additional processing must be performed on the stored value.
      This function must take three arguments (self, the stored value,
      and a boolean indicating if the property is currently set),
      and return the final, transformed value of the property.

      .. note:: The callback is responsible to ensure that value limits of the property (min/max, length...) are respected. Otherwise a ValueError exception is raised.

   :type get_transform: Callable[[:class:`bpy.types.bpy_struct`, bool, bool], bool] | None
   :param set_transform: Function to be called when this value is 'written',
      if some additional processing must be performed on the given value before storing it.
      This function must take four arguments (self, the given value to store,
      the currently stored value ('raw' value, without any ``get_transform`` applied to it),
      and a boolean indicating if the property is currently set),
      and return the final, transformed value of the property.

      .. note:: The callback is responsible to ensure that value limits (min/max, length...) are respected. Otherwise a ValueError exception is raised.

   :type set_transform: Callable[[:class:`bpy.types.bpy_struct`, bool, bool, bool], bool] | None
   :return: Opaque type used for registration.
   :rtype: :class:`_PropertyDeferred`


.. function:: BoolVectorProperty(*, name="", description="", translation_context="*", default=(False, False, False), options={'ANIMATABLE'}, override=set(), tags=set(), subtype='NONE', size=3, update=None, get=None, set=None, get_transform=None, set_transform=None)

   Returns a new vector boolean property definition.

   :param name: Name used in the user interface.
   :type name: str
   :param description: Text used for the tooltip and api documentation.
   :type description: str
   :param translation_context: Text used as context to disambiguate translations.
   :type translation_context: str
   :param default: sequence of booleans the length of *size*.
   :type default: Sequence[bool]
   :param options: Enumerator in :ref:`rna_enum_property_flag_items`.
   :type options: set[str]
   :param override: Enumerator in :ref:`rna_enum_property_override_flag_items`.
   :type override: set[str]
   :param tags: Enumerator of tags that are defined by parent class.
   :type tags: set[str]
   :param subtype: Enumerator in :ref:`rna_enum_property_subtype_number_array_items`.
   :type subtype: str
   :param size: Vector dimensions in [1, 32]. An int sequence can be used to define multi-dimension arrays.
   :type size: int | Sequence[int]
   :param update: Function to be called when this value is modified,
      This function must take 2 values (self, context) and return None.
      *Warning* there are no safety checks to avoid infinite recursion.
   :type update: Callable[[:class:`bpy.types.bpy_struct`, :class:`bpy.types.Context`], None] | None
   :param get: Function to be called when this value is 'read', and the default,
      system-defined storage is not used for this property.
      This function must take 1 value (self) and return the value of the property.

      .. note:: Defining this callback without a matching ``set`` one will make the property read-only (even if ``READ_ONLY`` option is not set).
   :type get: Callable[[:class:`bpy.types.bpy_struct`], Sequence[bool]] | None
   :param set: Function to be called when this value is 'written', and the default,
      system-defined storage is not used for this property.
      This function must take 2 values (self, value) and return None.

      .. note:: Defining this callback without a matching ``get`` one is invalid.
   :type set: Callable[[:class:`bpy.types.bpy_struct`, tuple[bool, ...]], None] | None
   :param get_transform: Function to be called when this value is 'read',
      if some additional processing must be performed on the stored value.
      This function must take three arguments (self, the stored value,
      and a boolean indicating if the property is currently set),
      and return the final, transformed value of the property.

      .. note:: The callback is responsible to ensure that value limits of the property (min/max, length...) are respected. Otherwise a ValueError exception is raised.

   :type get_transform: Callable[[:class:`bpy.types.bpy_struct`, Sequence[bool], bool], Sequence[bool]] | None
   :param set_transform: Function to be called when this value is 'written',
      if some additional processing must be performed on the given value before storing it.
      This function must take four arguments (self, the given value to store,
      the currently stored value ('raw' value, without any ``get_transform`` applied to it),
      and a boolean indicating if the property is currently set),
      and return the final, transformed value of the property.

      .. note:: The callback is responsible to ensure that value limits (min/max, length...) are respected. Otherwise a ValueError exception is raised.

   :type set_transform: Callable[[:class:`bpy.types.bpy_struct`, Sequence[bool], Sequence[bool], bool], Sequence[bool]] | None
   :return: Opaque type used for registration.
   :rtype: :class:`_PropertyDeferred`


.. function:: CollectionProperty(type, *, name="", description="", translation_context="*", options={'ANIMATABLE'}, override=set(), tags=set())

   Returns a new collection property definition.

   :param type: A subclass of a property group.
   :type type: type[:class:`bpy.types.PropertyGroup`]
   :param name: Name used in the user interface.
   :type name: str
   :param description: Text used for the tooltip and api documentation.
   :type description: str
   :param translation_context: Text used as context to disambiguate translations.
   :type translation_context: str
   :param options: Enumerator in :ref:`rna_enum_property_flag_items`.
   :type options: set[str]
   :param override: Enumerator in :ref:`rna_enum_property_override_flag_collection_items`.
   :type override: set[str]
   :param tags: Enumerator of tags that are defined by parent class.
   :type tags: set[str]
   :return: Opaque type used for registration.
   :rtype: :class:`_PropertyDeferred`


.. function:: EnumProperty(items, *, name="", description="", translation_context="*", default=None, options={'ANIMATABLE'}, override=set(), tags=set(), update=None, get=None, set=None, get_transform=None, set_transform=None)

   Returns a new enumerator property definition.

   :param items: sequence of enum items formatted:
      ``[(identifier, name, description, icon, number), ...]``.

      The first three elements of the tuples are mandatory.

      :identifier: The identifier is used for Python access.
         An empty identifier means that the item is a separator
      :name: Name for the interface.
      :description: Used for documentation and tooltips.
      :icon: An icon string identifier or integer icon value
         (e.g. returned by :class:`bpy.types.UILayout.icon`)
      :number: Unique value used as the identifier for this item (stored in file data).
         Use when the identifier may need to change. If the *ENUM_FLAG* option is used,
         the values are bit-masks and should be powers of two.

      When an item only contains 4 items they define ``(identifier, name, description, number)``.

      Separators may be added using either None (nameless separator),
      or a regular item tuple with an empty identifier string, in which case the name,
      if non-empty, will be displayed in the UI above the separator line.
      For dynamic values a callback can be passed which returns a list in
      the same format as the static list.
      This function must take 2 arguments ``(self, context)``, **context may be None**.

      .. warning::

         There is a known bug with using a callback,
         Python must keep a reference to the strings returned by the callback or Blender
         will misbehave or even crash.
   :type items: Iterable[tuple[str, str, str] | tuple[str, str, str, int] | tuple[str, str, str, str | int, int] | None] | Callable[[:class:`bpy.types.bpy_struct`, :class:`bpy.types.Context` | None], Iterable[tuple[str, str, str] | tuple[str, str, str, int] | tuple[str, str, str, str | int, int] | None]]
   :param name: Name used in the user interface.
   :type name: str
   :param description: Text used for the tooltip and api documentation.
   :type description: str
   :param translation_context: Text used as context to disambiguate translations.
   :type translation_context: str
   :param default: The default value for this enum, a string from the identifiers used in *items*, or integer matching an item number.
      If the *ENUM_FLAG* option is used this must be a set of such string identifiers instead.
      WARNING: Strings cannot be specified for dynamic enums
      (i.e. if a callback function is given as *items* parameter).
   :type default: str | int | set[str] | None
   :param options: Enumerator in :ref:`rna_enum_property_flag_enum_items`.
   :type options: set[str]
   :param override: Enumerator in :ref:`rna_enum_property_override_flag_items`.
   :type override: set[str]
   :param tags: Enumerator of tags that are defined by parent class.
   :type tags: set[str]
   :param update: Function to be called when this value is modified,
      This function must take 2 values (self, context) and return None.
      *Warning* there are no safety checks to avoid infinite recursion.
   :type update: Callable[[:class:`bpy.types.bpy_struct`, :class:`bpy.types.Context`], None] | None
   :param get: Function to be called when this value is 'read', and the default,
      system-defined storage is not used for this property.
      This function must take 1 value (self) and return the value of the property.

      .. note:: Defining this callback without a matching ``set`` one will make the property read-only (even if ``READ_ONLY`` option is not set).
   :type get: Callable[[:class:`bpy.types.bpy_struct`], int] | None
   :param set: Function to be called when this value is 'written', and the default,
      system-defined storage is not used for this property.
      This function must take 2 values (self, value) and return None.

      .. note:: Defining this callback without a matching ``get`` one is invalid.
   :type set: Callable[[:class:`bpy.types.bpy_struct`, int], None] | None
   :param get_transform: Function to be called when this value is 'read',
      if some additional processing must be performed on the stored value.
      This function must take three arguments (self, the stored value,
      and a boolean indicating if the property is currently set),
      and return the final, transformed value of the property.

      .. note:: The callback is responsible to ensure that value limits of the property (min/max, length...) are respected. Otherwise a ValueError exception is raised.

   :type get_transform: Callable[[:class:`bpy.types.bpy_struct`, int, bool], int] | None
   :param set_transform: Function to be called when this value is 'written',
      if some additional processing must be performed on the given value before storing it.
      This function must take four arguments (self, the given value to store,
      the currently stored value ('raw' value, without any ``get_transform`` applied to it),
      and a boolean indicating if the property is currently set),
      and return the final, transformed value of the property.

      .. note:: The callback is responsible to ensure that value limits (min/max, length...) are respected. Otherwise a ValueError exception is raised.

   :type set_transform: Callable[[:class:`bpy.types.bpy_struct`, int, int, bool], int] | None
   :return: Opaque type used for registration.
   :rtype: :class:`_PropertyDeferred`


.. function:: FloatProperty(*, name="", description="", translation_context="*", default=0.0, min=-3.402823e+38, max=3.402823e+38, soft_min=-3.402823e+38, soft_max=3.402823e+38, step=3, precision=2, options={'ANIMATABLE'}, override=set(), tags=set(), subtype='NONE', unit='NONE', update=None, get=None, set=None, get_transform=None, set_transform=None)

   Returns a new float (single precision) property definition.

   :param name: Name used in the user interface.
   :type name: str
   :param description: Text used for the tooltip and api documentation.
   :type description: str
   :param translation_context: Text used as context to disambiguate translations.
   :type translation_context: str
   :param default: The default value for this property.
   :type default: float
   :param min: Hard minimum, trying to assign a value below will silently assign this minimum instead.
   :type min: float
   :param max: Hard maximum, trying to assign a value above will silently assign this maximum instead.
   :type max: float
   :param soft_min: Soft minimum (>= *min*), user won't be able to drag the widget below this value in the UI.
   :type soft_min: float
   :param soft_max: Soft maximum (<= *max*), user won't be able to drag the widget above this value in the UI.
   :type soft_max: float
   :param step: Step of increment/decrement in UI, in [1, 100], defaults to 3 (WARNING: actual value is /100).
   :type step: float
   :param precision: Maximum number of decimal digits to display, in [0, 6]. Fraction is automatically hidden for exact integer values of fields with unit 'NONE' or 'TIME' (frame count) and step divisible by 100.
   :type precision: int
   :param options: Enumerator in :ref:`rna_enum_property_flag_items`.
   :type options: set[str]
   :param override: Enumerator in :ref:`rna_enum_property_override_flag_items`.
   :type override: set[str]
   :param tags: Enumerator of tags that are defined by parent class.
   :type tags: set[str]
   :param subtype: Enumerator in :ref:`rna_enum_property_subtype_number_items`.
   :type subtype: str
   :param unit: Enumerator in :ref:`rna_enum_property_unit_items`.
   :type unit: str
   :param update: Function to be called when this value is modified,
      This function must take 2 values (self, context) and return None.
      *Warning* there are no safety checks to avoid infinite recursion.
   :type update: Callable[[:class:`bpy.types.bpy_struct`, :class:`bpy.types.Context`], None] | None
   :param get: Function to be called when this value is 'read', and the default,
      system-defined storage is not used for this property.
      This function must take 1 value (self) and return the value of the property.

      .. note:: Defining this callback without a matching ``set`` one will make the property read-only (even if ``READ_ONLY`` option is not set).
   :type get: Callable[[:class:`bpy.types.bpy_struct`], float] | None
   :param set: Function to be called when this value is 'written', and the default,
      system-defined storage is not used for this property.
      This function must take 2 values (self, value) and return None.

      .. note:: Defining this callback without a matching ``get`` one is invalid.
   :type set: Callable[[:class:`bpy.types.bpy_struct`, float], None] | None
   :param get_transform: Function to be called when this value is 'read',
      if some additional processing must be performed on the stored value.
      This function must take three arguments (self, the stored value,
      and a boolean indicating if the property is currently set),
      and return the final, transformed value of the property.

      .. note:: The callback is responsible to ensure that value limits of the property (min/max, length...) are respected. Otherwise a ValueError exception is raised.

   :type get_transform: Callable[[:class:`bpy.types.bpy_struct`, float, bool], float] | None
   :param set_transform: Function to be called when this value is 'written',
      if some additional processing must be performed on the given value before storing it.
      This function must take four arguments (self, the given value to store,
      the currently stored value ('raw' value, without any ``get_transform`` applied to it),
      and a boolean indicating if the property is currently set),
      and return the final, transformed value of the property.

      .. note:: The callback is responsible to ensure that value limits (min/max, length...) are respected. Otherwise a ValueError exception is raised.

   :type set_transform: Callable[[:class:`bpy.types.bpy_struct`, float, float, bool], float] | None
   :return: Opaque type used for registration.
   :rtype: :class:`_PropertyDeferred`


.. function:: FloatVectorProperty(*, name="", description="", translation_context="*", default=(0.0, 0.0, 0.0), min=-sys.float_info.max, max=sys.float_info.max, soft_min=-sys.float_info.max, soft_max=sys.float_info.max, step=3, precision=2, options={'ANIMATABLE'}, override=set(), tags=set(), subtype='NONE', unit='NONE', size=3, update=None, get=None, set=None, get_transform=None, set_transform=None)

   Returns a new vector float property definition.

   :param name: Name used in the user interface.
   :type name: str
   :param description: Text used for the tooltip and api documentation.
   :type description: str
   :param translation_context: Text used as context to disambiguate translations.
   :type translation_context: str
   :param default: Sequence of floats the length of *size*.
   :type default: Sequence[float]
   :param min: Hard minimum, trying to assign a value below will silently assign this minimum instead.
   :type min: float
   :param max: Hard maximum, trying to assign a value above will silently assign this maximum instead.
   :type max: float
   :param soft_min: Soft minimum (>= *min*), user won't be able to drag the widget below this value in the UI.
   :type soft_min: float
   :param soft_max: Soft maximum (<= *max*), user won't be able to drag the widget above this value in the UI.
   :type soft_max: float
   :param step: Step of increment/decrement in UI, in [1, 100], defaults to 3 (WARNING: actual value is /100).
   :type step: float
   :param precision: Maximum number of decimal digits to display, in [0, 6]. Fraction is automatically hidden for exact integer values of fields with unit 'NONE' or 'TIME' (frame count) and step divisible by 100.
   :type precision: int
   :param options: Enumerator in :ref:`rna_enum_property_flag_items`.
   :type options: set[str]
   :param override: Enumerator in :ref:`rna_enum_property_override_flag_items`.
   :type override: set[str]
   :param tags: Enumerator of tags that are defined by parent class.
   :type tags: set[str]
   :param subtype: Enumerator in :ref:`rna_enum_property_subtype_number_array_items`.
   :type subtype: str
   :param unit: Enumerator in :ref:`rna_enum_property_unit_items`.
   :type unit: str
   :param size: Vector dimensions in [1, 32]. An int sequence can be used to define multi-dimension arrays.
   :type size: int | Sequence[int]
   :param update: Function to be called when this value is modified,
      This function must take 2 values (self, context) and return None.
      *Warning* there are no safety checks to avoid infinite recursion.
   :type update: Callable[[:class:`bpy.types.bpy_struct`, :class:`bpy.types.Context`], None] | None
   :param get: Function to be called when this value is 'read', and the default,
      system-defined storage is not used for this property.
      This function must take 1 value (self) and return the value of the property.

      .. note:: Defining this callback without a matching ``set`` one will make the property read-only (even if ``READ_ONLY`` option is not set).
   :type get: Callable[[:class:`bpy.types.bpy_struct`], Sequence[float]] | None
   :param set: Function to be called when this value is 'written', and the default,
      system-defined storage is not used for this property.
      This function must take 2 values (self, value) and return None.

      .. note:: Defining this callback without a matching ``get`` one is invalid.
   :type set: Callable[[:class:`bpy.types.bpy_struct`, tuple[float, ...]], None] | None
   :param get_transform: Function to be called when this value is 'read',
      if some additional processing must be performed on the stored value.
      This function must take three arguments (self, the stored value,
      and a boolean indicating if the property is currently set),
      and return the final, transformed value of the property.

      .. note:: The callback is responsible to ensure that value limits of the property (min/max, length...) are respected. Otherwise a ValueError exception is raised.

   :type get_transform: Callable[[:class:`bpy.types.bpy_struct`, Sequence[float], bool], Sequence[float]] | None
   :param set_transform: Function to be called when this value is 'written',
      if some additional processing must be performed on the given value before storing it.
      This function must take four arguments (self, the given value to store,
      the currently stored value ('raw' value, without any ``get_transform`` applied to it),
      and a boolean indicating if the property is currently set),
      and return the final, transformed value of the property.

      .. note:: The callback is responsible to ensure that value limits (min/max, length...) are respected. Otherwise a ValueError exception is raised.

   :type set_transform: Callable[[:class:`bpy.types.bpy_struct`, Sequence[float], Sequence[float], bool], Sequence[float]] | None
   :return: Opaque type used for registration.
   :rtype: :class:`_PropertyDeferred`


.. function:: IntProperty(*, name="", description="", translation_context="*", default=0, min=-2**31, max=2**31-1, soft_min=-2**31, soft_max=2**31-1, step=1, options={'ANIMATABLE'}, override=set(), tags=set(), subtype='NONE', update=None, get=None, set=None, get_transform=None, set_transform=None)

   Returns a new int property definition.

   :param name: Name used in the user interface.
   :type name: str
   :param description: Text used for the tooltip and api documentation.
   :type description: str
   :param translation_context: Text used as context to disambiguate translations.
   :type translation_context: str
   :param default: The default value for this property.
   :type default: int
   :param min: Hard minimum, trying to assign a value below will silently assign this minimum instead.
   :type min: int
   :param max: Hard maximum, trying to assign a value above will silently assign this maximum instead.
   :type max: int
   :param soft_min: Soft minimum (>= *min*), user won't be able to drag the widget below this value in the UI.
   :type soft_min: int
   :param soft_max: Soft maximum (<= *max*), user won't be able to drag the widget above this value in the UI.
   :type soft_max: int
   :param step: Step of increment/decrement in UI, in [1, 100], defaults to 1 (WARNING: unused currently!).
   :type step: int
   :param options: Enumerator in :ref:`rna_enum_property_flag_items`.
   :type options: set[str]
   :param override: Enumerator in :ref:`rna_enum_property_override_flag_items`.
   :type override: set[str]
   :param tags: Enumerator of tags that are defined by parent class.
   :type tags: set[str]
   :param subtype: Enumerator in :ref:`rna_enum_property_subtype_number_items`.
   :type subtype: str
   :param update: Function to be called when this value is modified,
      This function must take 2 values (self, context) and return None.
      *Warning* there are no safety checks to avoid infinite recursion.
   :type update: Callable[[:class:`bpy.types.bpy_struct`, :class:`bpy.types.Context`], None] | None
   :param get: Function to be called when this value is 'read', and the default,
      system-defined storage is not used for this property.
      This function must take 1 value (self) and return the value of the property.

      .. note:: Defining this callback without a matching ``set`` one will make the property read-only (even if ``READ_ONLY`` option is not set).
   :type get: Callable[[:class:`bpy.types.bpy_struct`], int] | None
   :param set: Function to be called when this value is 'written', and the default,
      system-defined storage is not used for this property.
      This function must take 2 values (self, value) and return None.

      .. note:: Defining this callback without a matching ``get`` one is invalid.
   :type set: Callable[[:class:`bpy.types.bpy_struct`, int], None] | None
   :param get_transform: Function to be called when this value is 'read',
      if some additional processing must be performed on the stored value.
      This function must take three arguments (self, the stored value,
      and a boolean indicating if the property is currently set),
      and return the final, transformed value of the property.

      .. note:: The callback is responsible to ensure that value limits of the property (min/max, length...) are respected. Otherwise a ValueError exception is raised.

   :type get_transform: Callable[[:class:`bpy.types.bpy_struct`, int, bool], int] | None
   :param set_transform: Function to be called when this value is 'written',
      if some additional processing must be performed on the given value before storing it.
      This function must take four arguments (self, the given value to store,
      the currently stored value ('raw' value, without any ``get_transform`` applied to it),
      and a boolean indicating if the property is currently set),
      and return the final, transformed value of the property.

      .. note:: The callback is responsible to ensure that value limits (min/max, length...) are respected. Otherwise a ValueError exception is raised.

   :type set_transform: Callable[[:class:`bpy.types.bpy_struct`, int, int, bool], int] | None
   :return: Opaque type used for registration.
   :rtype: :class:`_PropertyDeferred`


.. function:: IntVectorProperty(*, name="", description="", translation_context="*", default=(0, 0, 0), min=-2**31, max=2**31-1, soft_min=-2**31, soft_max=2**31-1, step=1, options={'ANIMATABLE'}, override=set(), tags=set(), subtype='NONE', size=3, update=None, get=None, set=None, get_transform=None, set_transform=None)

   Returns a new vector int property definition.

   :param name: Name used in the user interface.
   :type name: str
   :param description: Text used for the tooltip and api documentation.
   :type description: str
   :param translation_context: Text used as context to disambiguate translations.
   :type translation_context: str
   :param default: sequence of ints the length of *size*.
   :type default: Sequence[int]
   :param min: Hard minimum, trying to assign a value below will silently assign this minimum instead.
   :type min: int
   :param max: Hard maximum, trying to assign a value above will silently assign this maximum instead.
   :type max: int
   :param soft_min: Soft minimum (>= *min*), user won't be able to drag the widget below this value in the UI.
   :type soft_min: int
   :param soft_max: Soft maximum (<= *max*), user won't be able to drag the widget above this value in the UI.
   :type soft_max: int
   :param step: Step of increment/decrement in UI, in [1, 100], defaults to 1 (WARNING: unused currently!).
   :type step: int
   :param options: Enumerator in :ref:`rna_enum_property_flag_items`.
   :type options: set[str]
   :param override: Enumerator in :ref:`rna_enum_property_override_flag_items`.
   :type override: set[str]
   :param tags: Enumerator of tags that are defined by parent class.
   :type tags: set[str]
   :param subtype: Enumerator in :ref:`rna_enum_property_subtype_number_array_items`.
   :type subtype: str
   :param size: Vector dimensions in [1, 32]. An int sequence can be used to define multi-dimension arrays.
   :type size: int | Sequence[int]
   :param update: Function to be called when this value is modified,
      This function must take 2 values (self, context) and return None.
      *Warning* there are no safety checks to avoid infinite recursion.
   :type update: Callable[[:class:`bpy.types.bpy_struct`, :class:`bpy.types.Context`], None] | None
   :param get: Function to be called when this value is 'read', and the default,
      system-defined storage is not used for this property.
      This function must take 1 value (self) and return the value of the property.

      .. note:: Defining this callback without a matching ``set`` one will make the property read-only (even if ``READ_ONLY`` option is not set).
   :type get: Callable[[:class:`bpy.types.bpy_struct`], Sequence[int]] | None
   :param set: Function to be called when this value is 'written', and the default,
      system-defined storage is not used for this property.
      This function must take 2 values (self, value) and return None.

      .. note:: Defining this callback without a matching ``get`` one is invalid.
   :type set: Callable[[:class:`bpy.types.bpy_struct`, tuple[int, ...]], None] | None
   :param get_transform: Function to be called when this value is 'read',
      if some additional processing must be performed on the stored value.
      This function must take three arguments (self, the stored value,
      and a boolean indicating if the property is currently set),
      and return the final, transformed value of the property.

      .. note:: The callback is responsible to ensure that value limits of the property (min/max, length...) are respected. Otherwise a ValueError exception is raised.

   :type get_transform: Callable[[:class:`bpy.types.bpy_struct`, Sequence[int], bool], Sequence[int]] | None
   :param set_transform: Function to be called when this value is 'written',
      if some additional processing must be performed on the given value before storing it.
      This function must take four arguments (self, the given value to store,
      the currently stored value ('raw' value, without any ``get_transform`` applied to it),
      and a boolean indicating if the property is currently set),
      and return the final, transformed value of the property.

      .. note:: The callback is responsible to ensure that value limits (min/max, length...) are respected. Otherwise a ValueError exception is raised.

   :type set_transform: Callable[[:class:`bpy.types.bpy_struct`, Sequence[int], Sequence[int], bool], Sequence[int]] | None
   :return: Opaque type used for registration.
   :rtype: :class:`_PropertyDeferred`


.. function:: PointerProperty(type, *, name="", description="", translation_context="*", options={'ANIMATABLE'}, override=set(), tags=set(), poll=None, update=None)

   Returns a new pointer property definition.

   :param type: A subclass of PropertyGroup or ID.
   :type type: type[:class:`bpy.types.PropertyGroup` | :class:`bpy.types.ID`]
   :param name: Name used in the user interface.
   :type name: str
   :param description: Text used for the tooltip and api documentation.
   :type description: str
   :param translation_context: Text used as context to disambiguate translations.
   :type translation_context: str
   :param options: Enumerator in :ref:`rna_enum_property_flag_items`.
   :type options: set[str]
   :param override: Enumerator in :ref:`rna_enum_property_override_flag_items`.
   :type override: set[str]
   :param tags: Enumerator of tags that are defined by parent class.
   :type tags: set[str]
   :param poll: Function that determines whether an item is valid for this property.
      The function must take 2 values (self, object) and return a boolean.

      .. note:: The return value will be checked only when assigning an item from the UI, but it is still possible to assign an "invalid" item to the property directly.

   :type poll: Callable[[:class:`bpy.types.bpy_struct`, :class:`bpy.types.ID`], bool] | None
   :param update: Function to be called when this value is modified,
      This function must take 2 values (self, context) and return None.
      *Warning* there are no safety checks to avoid infinite recursion.
   :type update: Callable[[:class:`bpy.types.bpy_struct`, :class:`bpy.types.Context`], None] | None
   :return: Opaque type used for registration.
   :rtype: :class:`_PropertyDeferred`

.. note:: Pointer properties do not support storing references to embedded IDs (e.g. :class:`bpy.types.Scene.collection`, :class:`bpy.types.Material.node_tree`).
   These should exclusively be referenced and accessed through their owner ID (e.g. the scene or material).


.. function:: RemoveProperty(cls, attr)

   Removes a dynamically defined property.

   :param cls: The class containing the property (must be a positional argument).
   :type cls: type[:class:`bpy.types.bpy_struct`]
   :param attr: Property name (must be passed as a keyword).
   :type attr: str

   .. note::

      Typically this function doesn't need to be accessed directly.
      Instead use ``del cls.attr``


.. function:: StringProperty(*, name="", description="", translation_context="*", default="", maxlen=0, options={'ANIMATABLE'}, override=set(), tags=set(), subtype='NONE', update=None, get=None, set=None, get_transform=None, set_transform=None, search=None, search_options={'SUGGESTION'})

   Returns a new string property definition.

   :param name: Name used in the user interface.
   :type name: str
   :param description: Text used for the tooltip and api documentation.
   :type description: str
   :param translation_context: Text used as context to disambiguate translations.
   :type translation_context: str
   :param default: initializer string.
   :type default: str
   :param maxlen: maximum length of the string.
   :type maxlen: int
   :param options: Enumerator in :ref:`rna_enum_property_flag_items`.
   :type options: set[str]
   :param override: Enumerator in :ref:`rna_enum_property_override_flag_items`.
   :type override: set[str]
   :param tags: Enumerator of tags that are defined by parent class.
   :type tags: set[str]
   :param subtype: Enumerator in :ref:`rna_enum_property_subtype_string_items`.
   :type subtype: str
   :param update: Function to be called when this value is modified,
      This function must take 2 values (self, context) and return None.
      *Warning* there are no safety checks to avoid infinite recursion.
   :type update: Callable[[:class:`bpy.types.bpy_struct`, :class:`bpy.types.Context`], None] | None
   :param get: Function to be called when this value is 'read', and the default,
      system-defined storage is not used for this property.
      This function must take 1 value (self) and return the value of the property.

      .. note:: Defining this callback without a matching ``set`` one will make the property read-only (even if ``READ_ONLY`` option is not set).
   :type get: Callable[[:class:`bpy.types.bpy_struct`], str] | None
   :param set: Function to be called when this value is 'written', and the default,
      system-defined storage is not used for this property.
      This function must take 2 values (self, value) and return None.

      .. note:: Defining this callback without a matching ``get`` one is invalid.
   :type set: Callable[[:class:`bpy.types.bpy_struct`, str], None] | None
   :param get_transform: Function to be called when this value is 'read',
      if some additional processing must be performed on the stored value.
      This function must take three arguments (self, the stored value,
      and a boolean indicating if the property is currently set),
      and return the final, transformed value of the property.

      .. note:: The callback is responsible to ensure that value limits of the property (min/max, length...) are respected. Otherwise a ValueError exception is raised.

   :type get_transform: Callable[[:class:`bpy.types.bpy_struct`, str, bool], str] | None
   :param set_transform: Function to be called when this value is 'written',
      if some additional processing must be performed on the given value before storing it.
      This function must take four arguments (self, the given value to store,
      the currently stored value ('raw' value, without any ``get_transform`` applied to it),
      and a boolean indicating if the property is currently set),
      and return the final, transformed value of the property.

      .. note:: The callback is responsible to ensure that value limits (min/max, length...) are respected. Otherwise a ValueError exception is raised.

   :type set_transform: Callable[[:class:`bpy.types.bpy_struct`, str, str, bool], str] | None
   :param search: Function to be called to show candidates for this string (shown in the UI).
      This function must take 3 values (self, context, edit_text)
      and return a sequence, iterator or generator where each item must be:

      - A single string (representing a candidate to display).
      - A tuple-pair of strings, where the first is a candidate and the second
        is additional information about the candidate.
   :type search: Callable[[:class:`bpy.types.bpy_struct`, :class:`bpy.types.Context`, str], Iterable[str | tuple[str, str]]] | None
   :param search_options: Set of strings in:

      - 'SORT' sorts the resulting items.
      - 'SUGGESTION' lets the user enter values not found in search candidates.
        **WARNING** disabling this flag causes the search callback to run on redraw,
        so only disable this flag if it's not likely to cause performance issues.

   :type search_options: set[str]
   :return: Opaque type used for registration.
   :rtype: :class:`_PropertyDeferred`


.. class:: _PropertyDeferred

   Intermediate storage for properties before registration.
   
   .. note::
   
      This is not part of the stable API and may change between releases.

   .. attribute:: function

      Undocumented, consider `contributing <https://developer.blender.org/>`__.


   .. attribute:: keywords

      Undocumented, consider `contributing <https://developer.blender.org/>`__.




