Utilities (bpy.utils)
=====================

.. module:: bpy.utils

This module contains utility functions specific to blender but
not associated with blenders internal data.

.. toctree::
   :maxdepth: 1
   :caption: Submodules

   bpy.utils.previews.rst
   bpy.utils.units.rst

.. function:: blend_paths(*, absolute=False, packed=False, local=False)

   Returns a list of paths to external files referenced by the loaded .blend file.

   :param absolute: When true the paths returned are made absolute.
   :type absolute: bool
   :param packed: When true include file paths for packed data.
   :type packed: bool
   :param local: When true skip linked library paths.
   :type local: bool
   :return: path list.
   :rtype: list[str]


.. function:: escape_identifier(string)

   Simple string escaping function used for animation paths.

   :param string: text
   :type string: str
   :return: The escaped string.
   :rtype: str


.. function:: flip_name(name, *, strip_digits=False)

   Flip a name between left/right sides, useful for 
   mirroring bone names.

   :param name: Bone name to flip.
   :type name: str
   :param strip_digits: Whether to remove ``.###`` suffix.
   :type strip_digits: bool
   :return: The flipped name.
   :rtype: str


.. function:: unescape_identifier(string)

   Simple string un-escape function used for animation paths.
   This performs the reverse of :func:`escape_identifier`.

   :param string: text
   :type string: str
   :return: The un-escaped string.
   :rtype: str


.. function:: register_class(cls)

   Register a subclass of a Blender type class.

   :param cls: Registerable Blender class type.
   :type cls: type[:class:`bpy.types.Panel` | :class:`bpy.types.UIList` | :class:`bpy.types.Menu` | :class:`bpy.types.Header` | :class:`bpy.types.Operator` | :class:`bpy.types.KeyingSetInfo` | :class:`bpy.types.RenderEngine` | :class:`bpy.types.AssetShelf` | :class:`bpy.types.FileHandler` | :class:`bpy.types.PropertyGroup` | :class:`bpy.types.AddonPreferences` | :class:`bpy.types.NodeTree` | :class:`bpy.types.Node` | :class:`bpy.types.NodeSocket` | :class:`bpy.types.Gizmo` | :class:`bpy.types.GizmoGroup`]

   :raises ValueError:
      if the class is not a subclass of a registerable blender class.

   .. note::

      If the class has a *register* class method it will be called
      before registration.


.. function:: register_cli_command(id, execute)

   Register a command, accessible via the (``-c`` / ``--command``) command-line argument.

   :param id: The command identifier (must pass an ``str.isidentifier`` check).

      If the ``id`` is already registered, a warning is printed and the command is inaccessible to prevent accidents invoking the wrong command.
   :type id: str
   :param execute: Callback, taking a single list of strings and returns an int.
      The arguments are built from all command-line arguments following the command id.
      The return value should be 0 for success, 1 on failure (specific error codes from the ``os`` module can also be used).
   :type execute: Callable[[list[str]], int]
   :return: The command handle which can be passed to :func:`unregister_cli_command`.

      This uses Python's capsule type however the result should be considered an opaque handle only used for unregistering.
   :rtype: Any


   **Custom Commands**

   Registering commands makes it possible to conveniently expose command line
   functionality via commands passed to (``-c`` / ``--command``).

   .. literalinclude:: ./examples/bpy.utils.register_cli_command.0.py
      :lines: 8-


   **Using Python Argument Parsing**

   This example shows how the Python ``argparse`` module can be used with a custom command.

   Using ``argparse`` is generally recommended as it has many useful utilities and
   generates a ``--help`` message for your command.

   .. literalinclude:: ./examples/bpy.utils.register_cli_command.1.py
      :lines: 10-


.. function:: unregister_cli_command(handle)

   Unregister a CLI command.

   :param handle: The return value of :func:`register_cli_command`.
   :type handle: Any


.. function:: resource_path(type, *, major=bpy.app.version[0], minor=bpy.app.version[1])

   Return the base path for storing system files.

   :param type: The resource type.
   :type type: Literal['USER', 'LOCAL', 'SYSTEM']
   :param major: major version, defaults to current.
   :type major: int
   :param minor: minor version, defaults to current.
   :type minor: int
   :return: the resource path (not necessarily existing).
   :rtype: str


.. function:: unregister_class(cls)

   Unload the Python class from blender.

   :param cls: Blender type class, 
      see :func:`bpy.utils.register_class` for classes which can 
      be registered.
   :type cls: type[:class:`bpy.types.Panel` | :class:`bpy.types.UIList` | :class:`bpy.types.Menu` | :class:`bpy.types.Header` | :class:`bpy.types.Operator` | :class:`bpy.types.KeyingSetInfo` | :class:`bpy.types.RenderEngine` | :class:`bpy.types.AssetShelf` | :class:`bpy.types.FileHandler` | :class:`bpy.types.PropertyGroup` | :class:`bpy.types.AddonPreferences` | :class:`bpy.types.NodeTree` | :class:`bpy.types.Node` | :class:`bpy.types.NodeSocket` | :class:`bpy.types.Gizmo` | :class:`bpy.types.GizmoGroup`]

   .. note::

      If the class has an *unregister* class method it will be called
      before unregistering.


.. function:: keyconfig_init()

   Initialize and refresh key configurations, called from the Blender
   window manager on startup and refresh.

.. function:: keyconfig_set(filepath, *, report=None)

   Load and activate a key configuration from a file.
   
   :param filepath: The file path to the key configuration preset.
   :type filepath: str
   :param report: An optional callable for reporting errors.
   :type report: Callable[[set[str], str], None] | None

.. function:: load_scripts(*, reload_scripts=False, refresh_scripts=False, extensions=True)

   Load scripts and run each modules register function.
   
   :param reload_scripts: Causes all scripts to have their unregister method
      called before loading.
   :type reload_scripts: bool
   :param refresh_scripts: only load scripts which are not already loaded
      as modules.
   :type refresh_scripts: bool
   :param extensions: Loads additional scripts (add-ons & app-templates).
   :type extensions: bool

.. function:: modules_from_path(path, loaded_modules)

   Load all modules in a path and return them as a list.
   
   :param path: this path is scanned for scripts and packages.
   :type path: str
   :param loaded_modules: already loaded module names, files matching these
      names will be ignored.
   :type loaded_modules: set[str]
   :return: all loaded modules.
   :rtype: list[ModuleType]

.. function:: preset_find(name, preset_path, *, display_name=False, ext='.py')

   Search for a preset by name.
   
   :param name: The preset name.
   :type name: str
   :param preset_path: The preset subdirectory (e.g. ``"keyconfig"``).
   :type preset_path: str
   :param display_name: When True, search by display name instead of filename.
   :type display_name: bool
   :param ext: The file extension for the preset.
   :type ext: str
   :return: The file path of the preset or None if not found.
   :rtype: str | None

.. function:: preset_paths(subdir)

   Returns a list of paths for a specific preset.
   
   :param subdir: preset subdirectory (must not be an absolute path).
   :type subdir: str
   :return: Script paths.
   :rtype: list[str]

.. function:: refresh_script_paths()

   Run this after creating new script paths to update sys.path

.. function:: app_template_paths(*, path=None)

   Returns valid application template paths.
   
   :param path: Optional subdir.
   :type path: str | None
   :return: App template paths.
   :rtype: Iterator[str]

.. function:: time_from_frame(frame, *, fps=None, fps_base=None)

   Returns the time from a frame number.
   
   If *fps* and *fps_base* are not given the current scene is used.
   
   :param frame: number.
   :type frame: int | float
   :param fps: Frames per second, if not given the current scene is used.
   :type fps: float | None
   :param fps_base: Frames per second base, if not given the current scene is used.
   :type fps_base: float | None
   :return: the time in seconds.
   :rtype: datetime.timedelta

.. function:: register_manual_map(manual_hook)

   Register a function to provide manual URL mappings.
   
   :param manual_hook: A callable that returns ``(prefix, mapping)``
      where *mapping* is a sequence of ``(pattern, url)`` pairs.
   :type manual_hook: Callable[[], tuple[str, list[tuple[str, str]]]]

.. function:: unregister_manual_map(manual_hook)

   Unregister a previously registered manual map hook.
   
   :param manual_hook: The hook function to remove.
   :type manual_hook: Callable[[], tuple[str, list[tuple[str, str]]]]

.. function:: register_preset_path(path)

   Register a preset search path.
   
   :param path: preset directory (must be an absolute path).
   
      This path must contain a "presets" subdirectory which will typically contain presets for add-ons.
   
      You may call ``bpy.utils.register_preset_path(os.path.dirname(__file__))`` from an add-ons ``__init__.py`` file.
      When the ``__init__.py`` is in the same location as a ``presets`` directory.
      For example an operators preset would be located under: ``presets/operator/{operator.id}/``
      where ``operator.id`` is the ``bl_idname`` of the operator.
   :type path: str
   :return: success
   :rtype: bool

.. function:: unregister_preset_path(path)

   Unregister a preset search path.
   
   :param path: preset directory (must be an absolute path).
   
      This must match the registered path exactly.
   :type path: str
   :return: success
   :rtype: bool

.. function:: register_classes_factory(classes)

   Utility function to create register and unregister functions
   which simply registers and unregisters a sequence of classes.
   
   :param classes: Sequence of classes to register and unregister.
   :type classes: Sequence[type]
   :return: register and unregister functions.
   :rtype: tuple[Callable[[], None], Callable[[], None]]

.. function:: register_submodule_factory(module_name, submodule_names)

   Utility function to create register and unregister functions
   which simply load submodules,
   calling their register & unregister functions.
   
   .. note::
   
      Modules are registered in the order given,
      unregistered in reverse order.
   
   :param module_name: The module name, typically ``__name__``.
   :type module_name: str
   :param submodule_names: List of submodule names to load and unload.
   :type submodule_names: list[str]
   :return: register and unregister functions.
   :rtype: tuple[Callable[[], None], Callable[[], None]]

.. function:: register_tool(tool_cls, *, after=None, separator=False, group=False)

   Register a tool in the toolbar.
   
   :param tool_cls: A tool subclass.
   :type tool_cls: type[:class:`bpy.types.WorkSpaceTool`]
   :param after: Optional identifiers this tool will be added after.
   :type after: Sequence[str] | set[str] | None
   :param separator: When true, add a separator before this tool.
   :type separator: bool
   :param group: When true, add a new nested group of tools.
   :type group: bool

.. function:: make_rna_paths(struct_name, prop_name, enum_name)

   Create RNA "paths" from given names.
   
   :param struct_name: Name of a RNA struct (like e.g. "Scene").
   :type struct_name: str
   :param prop_name: Name of a RNA struct's property.
   :type prop_name: str
   :param enum_name: Name of a RNA enum identifier.
   :type enum_name: str
   :return: A triple of three "RNA paths"
      (most_complete_path, "struct.prop", "struct.prop:'enum'").
      If no enum_name is given, the third element will always be empty.
   :rtype: tuple[str, str, str]

.. function:: manual_map()

   Yield manual URL mappings from all registered hooks.
   
   :return: An iterator of ``(prefix, mapping)`` pairs.
   :rtype: Iterator[tuple[str, list[tuple[str, str]]]]

.. function:: manual_language_code(default='en')

   :param default: The fallback language code to use when the current language is unavailable.
   :type default: str
   :return:
      The language code used for user manual URL component based on the current language user-preference,
      falling back to the ``default`` when unavailable.
   :rtype: str

.. function:: script_path_user()

   Return the user script path or None.
   
   :return: The user script path, or None if not found.
   :rtype: str | None

.. function:: extension_path_user(package, *, path='', create=False)

   Return a user writable directory associated with an extension.
   
   .. note::
   
      This allows each extension to have its own user directory to store files.
   
      The location of the extension it self is not a suitable place to store files
      because it is cleared each upgrade and the users may not have write permissions
      to the repository (typically "System" repositories).
   
   :param package: The ``__package__`` of the extension.
   :type package: str
   :param path: Optional subdirectory.
   :type path: str
   :param create: Treat the path as a directory and create it if its not existing.
   :type create: bool
   :return: a path.
   :rtype: str

.. function:: script_paths(*, subdir=None, user_pref=True, check_all=False, use_user=True, use_system_environment=True)

   Returns a list of valid script paths.
   
   :param subdir: Optional subdir.
   :type subdir: str | None
   :param user_pref: Include the user preference script paths.
   :type user_pref: bool
   :param check_all: Include local, user and system paths rather just the paths Blender uses.
   :type check_all: bool
   :param use_user: Include user paths
   :type use_user: bool
   :param use_system_environment: Include BLENDER_SYSTEM_SCRIPTS variable path
   :type use_system_environment: bool
   :return: script paths.
   :rtype: list[str]

.. function:: smpte_from_frame(frame, *, fps=None, fps_base=None)

   Returns an SMPTE formatted string from the *frame*:
   ``HH:MM:SS:FF``.
   
   If *fps* and *fps_base* are not given the current scene is used.
   
   :param frame: frame number.
   :type frame: int | float
   :param fps: Frames per second, if not given the current scene is used.
   :type fps: float | None
   :param fps_base: Frames per second base, if not given the current scene is used.
   :type fps_base: float | None
   :return: the frame string.
   :rtype: str

.. function:: smpte_from_seconds(time, *, fps=None, fps_base=None)

   Returns an SMPTE formatted string from the *time*:
   ``HH:MM:SS:FF``.
   
   If *fps* and *fps_base* are not given the current scene is used.
   
   :param time: time in seconds.
   :type time: int | float | datetime.timedelta
   :param fps: Frames per second, if not given the current scene is used.
   :type fps: float | None
   :param fps_base: Frames per second base, if not given the current scene is used.
   :type fps_base: float | None
   :return: the frame string.
   :rtype: str

.. function:: unregister_tool(tool_cls)

   Unregister a previously registered tool.
   
   :param tool_cls: The tool class to unregister.
   :type tool_cls: type[:class:`bpy.types.WorkSpaceTool`]

.. function:: user_resource(resource_type, *, path='', create=False)

   Return a user resource path (normally from the users home directory).
   
   :param resource_type: The resource type.
   :type resource_type: Literal['DATAFILES', 'CONFIG', 'SCRIPTS', 'EXTENSIONS']
   :param path: Optional subdirectory.
   :type path: str
   :param create: Treat the path as a directory and create it if its not existing.
   :type create: bool
   :return: a path.
   :rtype: str

.. function:: execfile(filepath, *, mod=None)

   Execute a file path as a Python script.
   
   :param filepath: Path of the script to execute.
   :type filepath: str
   :param mod: Optional cached module, the result of a previous execution.
   :type mod: ModuleType | None
   :return: The module which can be passed back in as ``mod``.
   :rtype: ModuleType

.. function:: expose_bundled_modules()

   For Blender as a Python module, add bundled VFX library python bindings
   to ``sys.path``. These may be used instead of dedicated packages, to ensure
   the libraries are compatible with Blender.

