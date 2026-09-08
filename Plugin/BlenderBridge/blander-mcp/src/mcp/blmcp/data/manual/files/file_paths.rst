
**********
File Paths
**********

.. _files-path_templates:

Path Templates
==============

Path templates substitute *template expressions* (written ``{abcd}``, where
"abcd" is a *variable* name) in a filepath when the path is used.

For example, if the currently open blend file is ``dance.blend`` and the render
output path is set to this:

.. code-block:: text

   //my_render_dir/{blend_name}.png

Then when rendering, Blender will treat the path as:

.. code-block:: text

   //my_render_dir/dance.png

With ``{blend_name}`` getting replaced by the ``dance`` from ``dance.blend``.

This substitution happens internally at time of use (e.g. while rendering), so
the template syntax will remain as-is in the path field.

.. note::

   Currently path templates are only supported for the **render output path** in
   Scene properties and the output paths in the compositor's **File Output
   node**. More filepaths will support templates in future releases.


Available Variables
-------------------

The following variables are currently available in template expressions.

Available in all paths that support template expressions:

:``blend_name``: The currently open blend file's name (without the .blend).
:``blend_dir``: Path up to (but not including) the currently open blend file.
:``blend_name_lib``: Like ``blend_name``, except that for path properties on
    library-linked data-blocks it will be the name of the library blend file
    that the data-block comes from.
:``blend_dir_lib``: Like ``blend_dir``, except that for path properties on
    library-linked data-blocks it will be the path to the library blend file
    that the data-block comes from.

Available only in render output paths (including in the compositor File Output node):

:``fps``: The frames per second of the current scene.
:``resolution_x / resolution_y``: The x and y resolution of the rendered image.
    This factors in the resolution scale as well, so if the scene resolution is
    1000x600 and the scale is 50%, then ``resolution_x`` and ``resolution_y``
    will be 500 and 300, respectively.
:``scene_name``: Name of the current scene.
:``camera_name``: Name of the current render camera.

Available only in path properties on a node:

:``node_name``: The name of the node that the path property is on.


Syntax
------

A basic template expression simply wraps a variable name with curly braces:

.. code-block:: text

   dance_{fps}.png


.. _files-path_templates-specifiers:

Format Specifiers
^^^^^^^^^^^^^^^^^

Template expressions can also include a format specifier.
Format specifiers instruct Blender how to format the substituted value.
They are written after a separating colon, like this:

.. code-block:: text

   dance_{fps:FORMAT}.png

Format specifiers currently can only be used with variables that represent
numerical values, not string values. The available format specifiers are:

- ``dance_{fps:###}.png``: format as an integer with at least 3 digits.
- ``dance_{fps:.###}.png``: format as a floating point number with exactly 3
  digits after the decimal point.
- ``dance_{fps:###.##}.png``: format as a floating point number with at least 3
  digits for the integer part and exactly 2 digits for the fractional part.

In all cases, the number of hash symbols (``#``) indicates the desired number of
digits.

For example, if the fps is 29.97, then:

- ``dance_{fps:###}.png`` -> ``dance_030.png``
- ``dance_{fps:.###}.png`` -> ``dance_29.970.png``
- ``dance_{fps:###.##}.png`` ->  -> ``dance_029.97.png``

Note that the values are properly rounded for the given number of digits.

If no format specification is given, default formatting for the named variable
is used (e.g. floating point for fps, integer for resolution).


Escape Sequences
----------------

Because ``{`` and ``}`` are used for template expressions in paths that support
them, when a literal ``{`` or ``}`` is desired in such a path they must be
escaped by writing them double:

- ``{{`` translates to a single ``{`` in the final path.
- ``}}`` translates to a single ``}`` in the final path.

For example:

- ``my_weird}}_{{path.png`` -> ``my_weird}_{path.png``
- ``//my_render_{{dir}}/{blend_name}.png`` -> ``//my_render_{dir}/dance.png``
- ``//my_render_dir/{{{blend_name}}}.png`` -> ``//my_render_dir/{dance}.png``


Errors
------

Paths that support templates can have template errors, which prevent the
path from being processed.

For example, in the following path:

.. code-block:: text

   //my_render_dir/{blend_name.png

The expression ``{blend_name`` isn't properly closed, which will result in an
error.

When there are template errors in a path, the path field will be highlighted red
in the UI:

.. figure:: /images/files_file_paths-invalid_path_template.png

Hovering over the path field will pop up a tooltip that contains a list of the
template errors encountered in that path:

.. figure:: /images/files_file_paths-invalid_path_template_tooltip.png

.. note::

   Depending on the path, template errors may prevent certain actions. For
   example, if there are errors in the render output path, then rendering an
   animation will fail with an error message indicating the path errors.
