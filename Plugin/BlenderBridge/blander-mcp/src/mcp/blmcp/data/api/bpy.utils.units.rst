bpy.utils submodule (bpy.utils.units)
=====================================

.. module:: bpy.utils.units

This module contains some data/methods regarding units handling.

.. data:: categories

   Constant value bpy.utils.units.categories(NONE='NONE', LENGTH='LENGTH', AREA='AREA', VOLUME='VOLUME', MASS='MASS', ROTATION='ROTATION', TIME='TIME', TIME_ABSOLUTE='TIME_ABSOLUTE', VELOCITY='VELOCITY', ACCELERATION='ACCELERATION', CAMERA='CAMERA', POWER='POWER', TEMPERATURE='TEMPERATURE', WAVELENGTH='WAVELENGTH', COLOR_TEMPERATURE='COLOR_TEMPERATURE', FREQUENCY='FREQUENCY')

.. data:: systems

   Constant value bpy.utils.units.systems(NONE='NONE', METRIC='METRIC', IMPERIAL='IMPERIAL')

.. function:: to_string(unit_system, unit_category, value, *, precision=3, split_unit=False, compatible_unit=False)

   Convert a given input float value into a string with units.

   :param unit_system: The unit system, from :attr:`bpy.utils.units.systems`.
   :type unit_system: str
   :param unit_category: The category of data we are converting (length, area, rotation, etc.),
      from :attr:`bpy.utils.units.categories`.
   :type unit_category: str
   :param value: The value to convert to a string.
   :type value: float
   :param precision: Number of digits after the decimal point.
   :type precision: int
   :param split_unit: Whether to use several units if needed (1m1cm), or always only one (1.01m).
   :type split_unit: bool
   :param compatible_unit: Whether to use keyboard-friendly units (1m2) or nicer UTF8 ones (1m²).
   :type compatible_unit: bool
   :return: The converted string.
   :rtype: str
   :raises ValueError: if conversion fails to generate a valid Python string.


.. function:: to_value(unit_system, unit_category, str_input, *, str_ref_unit=None)

   Convert a given input string into a float value.

   :param unit_system: The unit system, from :attr:`bpy.utils.units.systems`.
   :type unit_system: str
   :param unit_category: The category of data we are converting (length, area, rotation, etc.),
      from :attr:`bpy.utils.units.categories`.
   :type unit_category: str
   :param str_input: The string to convert to a float value.
   :type str_input: str
   :param str_ref_unit: A reference string from which to extract a default unit, if none is found in ``str_input``.
   :type str_ref_unit: str | None
   :return: The converted/interpreted value.
   :rtype: float
   :raises ValueError: if conversion fails to generate a valid Python float value.


