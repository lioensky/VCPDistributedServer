Operators (bpy.ops)
===================

.. module:: bpy.ops


Calling Operators
-----------------

Provides Python access to calling operators, this includes operators written in
C++, Python or macros.

Only keyword arguments can be used to pass operator properties.

Operators don't have return values as you might expect,
instead they return a set() which is made up of:
``{'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'}``.
Common return values are ``{'FINISHED'}`` and ``{'CANCELLED'}``, the latter
meaning that the operator execution was aborted without making any changes or
saving an undo history entry.

If operator was cancelled but there wasn't any reports from it with ``{'ERROR'}`` type,
it will just return ``{'CANCELLED'}`` without raising any exceptions.
However, if there are error reports, a ``RuntimeError`` will be raised
after the operator finishes execution, including all error report messages,
regardless of the return status (even if it was ``{'FINISHED'}``).

Calling an operator in the wrong context will raise a ``RuntimeError``,
there is a poll() method to avoid this problem.

Note that the operator ID (bl_idname) in this example is ``mesh.subdivide``,
``bpy.ops`` is just the access path for Python.


Keywords and Positional Arguments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For calling operators keywords are used for operator properties and
positional arguments are used to define how the operator is called.

There are 2 optional positional arguments (documented in detail below).

.. code-block:: python

   bpy.ops.test.operator(execution_context, undo)

- execution_context - ``str`` (enum).
- undo - ``bool`` type.


Each of these arguments is optional, but must be given in the order above.

.. literalinclude:: ./examples/bpy.ops.0.py
   :lines: 48-


Overriding Context
------------------

It is possible to override context members that the operator sees, so that they
act on specified rather than the selected or active data, or to execute an
operator in the different part of the user interface.

The context overrides are passed in as keyword arguments,
with keywords matching the context member names in ``bpy.context``.
For example to override ``bpy.context.active_object``,
you would pass ``active_object=object`` to :class:`bpy.types.Context.temp_override`.

.. note::

   You will nearly always want to use a copy of the actual current context as basis
   (otherwise, you'll have to find and gather all needed data yourself).

.. note::

   Context members are names which Blender uses for data access,
   overrides do not extend to overriding methods or any Python specific functionality.

.. literalinclude:: ./examples/bpy.ops.1.py
   :lines: 25-


.. _operator-execution_context:

Execution Context
-----------------

When calling an operator you may want to pass the execution context.

This determines the context that is given for the operator to run in, and whether
invoke() is called or only execute().

``EXEC_DEFAULT`` is used by default, running only the ``execute()`` method, but you may
want the operator to take user interaction with ``INVOKE_DEFAULT`` which will also
call invoke() if existing.

The execution context is one of:

- ``INVOKE_DEFAULT``
- ``INVOKE_REGION_WIN``
- ``INVOKE_REGION_CHANNELS``
- ``INVOKE_REGION_PREVIEW``
- ``INVOKE_AREA``
- ``INVOKE_SCREEN``
- ``EXEC_DEFAULT``
- ``EXEC_REGION_WIN``
- ``EXEC_REGION_CHANNELS``
- ``EXEC_REGION_PREVIEW``
- ``EXEC_AREA``
- ``EXEC_SCREEN``

.. literalinclude:: ./examples/bpy.ops.2.py
   :lines: 32-


It is also possible to run an operator in a particular part of the user
interface. For this we need to pass the window, area and sometimes a region.

.. literalinclude:: ./examples/bpy.ops.3.py
   :lines: 6-

.. toctree::
   :caption: Submodules
   :maxdepth: 1
   :glob:

   bpy.ops.*

