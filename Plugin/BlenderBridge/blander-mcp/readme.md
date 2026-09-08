# Blender MCP

## Overview

A lightweight MCP (Model Context Protocol) server for Blender.
It offers a natural language interface with Blender's Python API,
improving access to documentation, and allowing users to explore
and understand complex setups.

Read the documentation at [blender.org/lab/mcp-server](https://www.blender.org/lab/mcp-server/)

----

The project is deliberately small, maintainable, and does no more than
necessary. It has two components that communicate over a TCP socket:

- A **Blender add-on** that runs inside Blender and executes requests.
- An **MCP server** that runs as a separate process, launched by the
  MCP client (e.g. [Llama.cpp](https://projects.blender.org/lab/blender_mcp/wiki/Llama.cpp)).

The data flow is:
```
MCP Client  ⇐ MCP/stdio ⇒  blender-mcp  ⇐ TCP socket ⇒  Blender Add-on
```


## Blender Add-on

Located in ``addon/blender_mcp_addon/``.

A Blender extension that allows the MCP server to communicate with a
running Blender instance. It must be installed and enabled for any of
the MCP tools to work.

The add-on provides a preferences panel for configuring the host, port,
and an optional auto-start setting.

### Functionality Overview

Note that this is intended to be a fairly minimal add-on.

Connectivity
   - Auto-start (optional), is non-blocking any issues can be viewed from the preferences.
   - Configurable polling intervals (active and idle rates) from preferences to avoid excessive overhead.
   - Client timeout protection - stalled connections are evicted.
   - Start/stop operators accessible from the preferences panel.
   - Deferred responses are supported only by the interactive add-on server;
     background mode requires requests to complete synchronously and rejects deferred results.




## MCP Server

Located in ``mcp/blmcp/``, installed as a Python package with the
entry point ``blender-mcp``.

An MCP client launches this process and communicates with it over
stdio. The server connects to the add-on's TCP socket to relay
requests to Blender.

``mcp/blmcp/data/``
   Data files bundled with the package.

   - ``prompts.yml`` provides instructions sent to the LLM at
     connection time.
   - ``api/`` contains Blender Python API reference in RST format.
   - ``manual/`` contains Blender user manual excerpts in RST format.

``mcp/blmcp/tools/``
   Each tool is a single module, auto-discovered at startup.
   Modules ending in ``_toolcode`` contain code that runs inside
   Blender (sent to the addon for execution) and are skipped during
   discovery.

``mcp/blmcp/tools_helpers/``
   Shared utilities used by tools. Tools should not import from each
   other; shared logic lives here instead.


### Tools
- ``execute_blender_code``
   - Execute Python code in the connected Blender instance.
- ``execute_blender_code_for_cli``
   - Execute Python code in a background Blender process.
- ``get_blendfile_summary_datablocks``
   - Return a summary of the blend file: data-block counts, active workspace,
   and render engine.
- ``get_blendfile_summary_datablocks_for_cli``
   - Return a data-block summary by opening *blend_file* in background
   Blender.
- ``get_blendfile_summary_missing_files``
   - Report external file references that are missing from disk (images,
   libraries, fonts, sounds, movie clips, caches, sequences).
- ``get_blendfile_summary_missing_files_for_cli``
   - Report missing file references by opening *blend_file* in background
   Blender.
- ``get_blendfile_summary_of_linked_libraries``
   - Return a tree of directly and indirectly linked library files.
- ``get_blendfile_summary_of_linked_libraries_for_cli``
   - Return linked-library info by opening *blend_file* in background
   Blender.
- ``get_blendfile_summary_path_info``
   - Simple/fast access to the blend file's path, save status, age, and
   backups.
- ``get_blendfile_summary_path_info_for_cli``
   - Return path info by opening *blend_file* in background Blender.
- ``get_blendfile_summary_usage_guess``
   - Guess the primary use-cases of the current blend file (scored 0-100 with
   certainty).
- ``get_blendfile_summary_usage_guess_for_cli``
   - Guess use-cases by opening *blend_file* in background Blender.
- ``get_object_detail_summary``
   - Return a structured summary of the object identified by *name*.
- ``get_objects_summary``
   - Return the scene's collection hierarchy and their objects.
- ``get_python_api_docs``
   - Return the Blender Python API docs for *identifier*, or list modules
   matching a trailing-``*`` discovery pattern.
- ``get_screenshot_of_area_as_image``
   - Take a screenshot of a single Blender area and return it as a PNG image.
- ``get_screenshot_of_window_as_image``
   - Take a screenshot of the entire Blender window and return it as a PNG
   image.
- ``get_screenshot_of_window_as_json``
   - Return a JSON description of the Blender window layout, areas, active
   object, and selection.
- ``jump_to_tab_by_name``
   - Switch the active workspace tab to *name*.
- ``jump_to_tab_by_space_type``
   - Switch to a workspace whose main area matches *space_type*.
- ``jump_to_view3d_object_by_name``
   - Move the 3D viewport to focus on an object by *name*.
- ``jump_to_view3d_object_data_by_name``
   - Move the 3D viewport to the object whose data block matches *name*.
- ``render_thumbnail_to_path``
   - Render a small, low-quality thumbnail to *output_path* (temporarily
   overrides settings).
- ``render_viewport_to_path``
   - Render the current scene to *output_path* using current render settings.