
**************
Working Limits
**************

.. Note to editors:
   Please excuse the complicated Python scripts on this page,
   this is not something we do frequently in this manual,
   Its just for such explicit technical details,
   its useful to be able to validate its correct (or adjust the information shown).
   -- ideasman42


Space
=====

While object positions, vertex locations are not clamped, larger values become increasingly imprecise.
To get an idea of the precision you can work with using different scales.
Here's a table of scales and their associated accuracy:

.. # Python script used to generate the values below
   import ctypes
   from sys import platform as _platform
   _libm = ctypes.cdll.LoadLibrary('libm.so.6')
   _funcname_f = 'nextafterf'
   _nextafterf = getattr(_libm, _funcname_f)
   _nextafterf.restype = ctypes.c_float
   _nextafterf.argtypes = [ctypes.c_float, ctypes.c_float]
   i = 10
   while i < 10000000:
      delta = _nextafterf(i, i + 1) - i
      print(":{scale:,}: 1/{div:,}\\ :sup:`th`".format(scale=i, div=int(1 / delta)))
      i = i * 10


:10: 1/1,048,576\ :sup:`th`
:100: 1/131,072\ :sup:`th`
:1,000: 1/16,384\ :sup:`th`
:10,000: 1/1,024\ :sup:`th`
:100,000: 1/128\ :sup:`th`
:1,000,000: 1/16\ :sup:`th`

.. hint::

   For a rough rule of thumb, values within -5,000/+5,000 are typically reliable (range of 10,000).
   Internally *single precision* floating-point calculations are used.


Time
====

.. # Python script used to generate the values below
   from datetime import timedelta
   maxframe = 1048574
   for fps in (24, 25, 30, 60):
      seconds = maxframe / fps
      print(":%d fps: %d hours, %d minutes." %
            (fps, seconds // 3600, seconds % 3600 // 60))

The maximum number of frames for each scene is currently 1,048,574, and allows for continuous shots for durations of:

:24 fps: 12 hours, 8 minutes.
:25 fps: 11 hours, 39 minutes.
:30 fps: 9 hours, 42 minutes.
:60 fps: 4 hours, 51 minutes.

.. note::

   In practice, a finished work is typically composed of output from many scenes.
   So this limit does not prevent you from creating longer works.


Text Fields
===========

Fixed strings are used internally, and while it is not useful to list all limits, here are some common limits.
*Used for data-block names, modifiers, vertex groups, UV layers...*

:directory: 767
:file-name: 255
:file-path: 1023
:identifier: 63

.. note::

   Multi-byte encoding means some Unicode characters use more than a single ASCII character.
