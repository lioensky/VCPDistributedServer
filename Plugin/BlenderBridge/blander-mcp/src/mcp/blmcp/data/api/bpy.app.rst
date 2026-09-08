Application Data (bpy.app)
==========================

.. module:: bpy.app

This module contains application values that remain unchanged during runtime.

.. toctree::
   :maxdepth: 1
   :caption: Submodules

   bpy.app.handlers.rst
   bpy.app.translations.rst
   bpy.app.icons.rst
   bpy.app.timers.rst

.. data:: autoexec_fail

   Boolean, True when auto-execution of scripts failed (read-only).
   
   :type: bool


.. data:: autoexec_fail_message

   String, message describing the auto-execution failure (read-only).
   
   :type: str


.. data:: autoexec_fail_quiet

   Boolean, True when auto-execution failure should be quiet, set after the warning is shown once for the current blend file (read-only).
   
   :type: bool


.. data:: binary_path

   The location of Blender's executable, useful for utilities that open new instances. Read-only unless Blender is built as a Python module - in this case the value is an empty string which script authors may point to a Blender binary.
   
   :type: str


.. data:: cachedir

   String, the cache directory used by blender (read-only).
   
   If the parent of the cache folder (i.e. the part of the path that is not Blender-specific) does not exist, returns None.
   
   :type: str | None


.. data:: debug

   Boolean, for debug info (started with ``--debug`` / ``--debug-*`` matching this attribute name).
   
   :type: bool


.. data:: debug_depsgraph

   Boolean, for debug info (started with ``--debug`` / ``--debug-*`` matching this attribute name).
   
   :type: bool


.. data:: debug_depsgraph_build

   Boolean, for debug info (started with ``--debug`` / ``--debug-*`` matching this attribute name).
   
   :type: bool


.. data:: debug_depsgraph_eval

   Boolean, for debug info (started with ``--debug`` / ``--debug-*`` matching this attribute name).
   
   :type: bool


.. data:: debug_depsgraph_pretty

   Boolean, for debug info (started with ``--debug`` / ``--debug-*`` matching this attribute name).
   
   :type: bool


.. data:: debug_depsgraph_tag

   Boolean, for debug info (started with ``--debug`` / ``--debug-*`` matching this attribute name).
   
   :type: bool


.. data:: debug_depsgraph_time

   Boolean, for debug info (started with ``--debug`` / ``--debug-*`` matching this attribute name).
   
   :type: bool


.. data:: debug_events

   Boolean, for debug info (started with ``--debug`` / ``--debug-*`` matching this attribute name).
   
   :type: bool


.. data:: debug_freestyle

   Boolean, for debug info (started with ``--debug`` / ``--debug-*`` matching this attribute name).
   
   :type: bool


.. data:: debug_handlers

   Boolean, for debug info (started with ``--debug`` / ``--debug-*`` matching this attribute name).
   
   :type: bool


.. data:: debug_io

   Boolean, for debug info (started with ``--debug`` / ``--debug-*`` matching this attribute name).
   
   :type: bool


.. data:: debug_python

   Boolean, for debug info (started with ``--debug`` / ``--debug-*`` matching this attribute name).
   
   :type: bool


.. data:: debug_simdata

   Boolean, for debug info (started with ``--debug`` / ``--debug-*`` matching this attribute name).
   
   :type: bool


.. data:: debug_value

   Integer value which can be set to non-zero values for testing purposes.
   
   :type: int


.. data:: debug_wm

   Boolean, for debug info (started with ``--debug`` / ``--debug-*`` matching this attribute name).
   
   :type: bool


.. data:: driver_namespace

   Dictionary for drivers namespace, editable in-place, reset on file load (read-only).
   
   :type: dict[str, Any]


   File Loading & Order of Initialization
      Since drivers may be evaluated immediately after loading a blend-file it is necessary
      to ensure the driver name-space is initialized beforehand.

      This can be done by registering text data-blocks to execute on startup,
      which executes the scripts before drivers are evaluated.
      See *Text -> Register* from Blender's text editor.

      .. hint::

         You may prefer to use external files instead of Blender's text-blocks.
         This can be done using a text-block which executes an external file.

         This example runs ``driver_namespace.py`` located in the same directory as the text-blocks blend-file:

         .. code-block::

            import os
            import bpy
            blend_dir = os.path.normpath(os.path.join(__file__, "..", ".."))
            bpy.utils.execfile(os.path.join(blend_dir, "driver_namespace.py"))

         Using ``__file__`` ensures the text resolves to the expected path even when library-linked from another file.

      Other methods of populating the drivers name-space can be made to work but tend to be error prone:

      Using The ``--python`` command line argument to populate name-space often fails to achieve the desired goal
      because the initial evaluation will lookup a function that doesn't exist yet,
      marking the driver as invalid - preventing further evaluation.

      Populating the driver name-space before the blend-file loads also doesn't work
      since opening a file clears the name-space.

      It is possible to run a script via the ``--python`` command line argument, before the blend file.
      This can register a load-post handler (:mod:`bpy.app.handlers.load_post`) that initializes the name-space.
      While this works for background tasks it has the downside that opening the file from the file selector
      won't setup the name-space.


.. data:: online_access

   Boolean, true when internet access is allowed by Blender & 3rd party scripts (read-only).
   
   :type: bool


.. data:: online_access_override

   Boolean, true when internet access preference is overridden by the command line (read-only).
   
   :type: bool


.. data:: python_args

   Leading arguments to use when calling Python directly (via ``sys.executable``). These arguments match settings Blender uses to ensure Python runs with a compatible environment (read-only).
   
   :type: tuple[str, ...]


.. data:: render_icon_size

   Reference size for icon renders (read-only).
   
   :type: int


.. data:: render_preview_size

   Reference size for preview renders (read-only).
   
   :type: int


.. data:: tempdir

   String, the temp directory used by blender (read-only).
   
   :type: str


.. data:: use_event_simulate

   Boolean, for application behavior (started with ``--enable-*`` matching this attribute name)
   
   :type: bool


.. data:: use_userpref_skip_save_on_exit

   Boolean, for application behavior (started with ``--enable-*`` matching this attribute name)
   
   :type: bool


.. data:: background

   Boolean, True when blender is running without a user interface (started with -b)
   
   :type: bool


.. data:: factory_startup

   Boolean, True when blender is running with --factory-startup
   
   :type: bool


.. data:: module

   Boolean, True when running Blender as a python module
   
   :type: bool


.. data:: portable

   Boolean, True unless blender was built to reference absolute paths (on UNIX).
   
   :type: bool


.. data:: build_branch

   The branch this blender instance was built from
   
   :type: bytes


.. data:: build_cflags

   C compiler flags
   
   :type: bytes


.. data:: build_commit_date

   The date of the commit this Blender instance was built from
   
   :type: bytes


.. data:: build_commit_time

   The time of the commit this Blender instance was built from
   
   :type: bytes


.. data:: build_cxxflags

   C++ compiler flags
   
   :type: bytes


.. data:: build_date

   The date this Blender instance was built
   
   :type: bytes


.. data:: build_hash

   The commit hash this Blender instance was built with
   
   :type: bytes


.. data:: build_linkflags

   Binary linking flags
   
   :type: bytes


.. data:: build_platform

   The platform this blender instance was built for
   
   :type: bytes


.. data:: build_system

   Build system used
   
   :type: bytes


.. data:: build_time

   The time this Blender instance was built
   
   :type: bytes


.. data:: build_type

   The type of build (Release, Debug)
   
   :type: bytes


.. data:: build_commit_timestamp

   The unix timestamp of the commit this Blender instance was built from
   
   :type: int


.. data:: version_cycle

   The release status of this build alpha/beta/rc/release
   
   :type: str


.. data:: version_string

   The Blender version formatted as a string
   
   :type: str


.. data:: version

   The Blender version as a tuple of 3 numbers (major, minor, micro). eg. (4, 3, 1)
   
   :type: tuple[int, int, int]


.. data:: version_file

   The Blender File version, as a tuple of 3 numbers (major, minor, file sub-version), that will be used to save a .blend file. The last item in this tuple indicates the file sub-version, which is different from the release micro version (the last item of the ``bpy.app.version`` tuple). The file sub-version can be incremented multiple times while a Blender version is under development. This value is, and should be, used for handling compatibility changes between Blender versions
   
   :type: tuple[int, int, int]


.. data:: alembic

   Constant value bpy.app.alembic(supported=False, version=(0, 0, 0), version_string='Unknown')

.. data:: build_options

   Constant value bpy.app.build_options(bullet=False, codec_avi=False, codec_ffmpeg=False, codec_sndfile=False, compositor_cpu=True, cycles=False, cycles_osl=False, freestyle=False, image_cineon=False, image_dds=True, image_hdr=True, image_openexr=False, image_openjpeg=False, image_tiff=True, image_webp=False, input_ndof=False, audaspace=False, international=False, openal=False, opensubdiv=False, sdl=False, coreaudio=False, jack=False, pulseaudio=False, wasapi=False, libmv=False, mod_oceansim=False, mod_remesh=False, io_wavefront_obj=False, io_ply=False, io_stl=False, io_fbx=False, io_gpencil=False, opencolorio=False, openmp=False, openvdb=False, alembic=False, usd=False, fluid=False, xr_openxr=False, potrace=False, pugixml=False, haru=False, experimental_features=False)

.. data:: ffmpeg

   Constant value bpy.app.ffmpeg(supported=False, avcodec_version='Unknown', avcodec_version_string='Unknown', avdevice_version='Unknown', avdevice_version_string='Unknown', avformat_version='Unknown', avformat_version_string='Unknown', avutil_version='Unknown', avutil_version_string='Unknown', swscale_version='Unknown', swscale_version_string='Unknown')

.. data:: ocio

   Constant value bpy.app.ocio(supported=False, version=(0, 0, 0), version_string='Unknown')

.. data:: oiio

   Constant value bpy.app.oiio(supported=True, version=(3, 1, 9), version_string=' 3,  1,  9')

.. data:: opensubdiv

   Constant value bpy.app.opensubdiv(supported=False, version=(0, 0, 0), version_string='Unknown')

.. data:: openvdb

   Constant value bpy.app.openvdb(supported=False, version=(0, 0, 0), version_string='Unknown')

.. data:: sdl

   Constant value bpy.app.sdl(supported=False, version=(0, 0, 0), version_string='Unknown')

.. data:: usd

   Constant value bpy.app.usd(supported=False, version=(0, 0, 0), version_string='Unknown')

.. staticmethod:: help_text(*, all=False)

   Return the help text as a string.

   :param all: Return all arguments, even those which aren't available for the current platform.
   :type all: bool
   :return: Help text.
   :rtype: str


.. staticmethod:: is_job_running(job_type)

   Check whether a job of the given type is running.

   :param job_type: job type in :ref:`rna_enum_wm_job_type_items`.
   :type job_type: str
   :return: Whether a job of the given type is currently running.
   :rtype: bool


.. staticmethod:: memory_usage_undo()

   Get undo memory usage information.

   :return: Memory usage of the undo stack in bytes.
   :rtype: int


