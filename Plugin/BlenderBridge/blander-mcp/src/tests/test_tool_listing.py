# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Checks that the MCP server exposes the expected tool listing.
"""

__all__ = ()

import asyncio
import os
import sys
import unittest

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# Root of the repository.
_REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Complete expected tool listing.
# When a tool is added, changed, or removed this must be updated.
# Run with `--update` to regenerate from a live server query.

# BEGIN: EXPECTED_TOOLS
EXPECTED_TOOLS = [
    {
        "name": "action_list",
        "description": "\n"
        "Return all Actions stored in the current Blender file.\n"
        "\n"
        "Each entry in ``actions`` contains:\n"
        "\n"
        "- ``name``          \u2014 action name\n"
        "- ``frame_start``   \u2014 first frame of the action's time range\n"
        "- ``frame_end``     \u2014 last frame of the action's time range\n"
        "- ``fcurve_count``  \u2014 total number of F-Curves (0 = empty action)\n"
        "- ``slots``         \u2014 list of slot names for new-style actions\n"
        "  (Blender 4.4+); empty list for legacy single-slot actions\n"
        "\n"
        "Results are sorted alphabetically by action name.\n"
        "\n"
        "Use ``armature_action_apply`` to assign one of these actions to an\n"
        "armature object.\n",
        "inputSchema": {
            "properties": {},
            "title": "action_listArguments",
            "type": "object"
        }
    },
    {
        "name": "armature_action_apply",
        "description": "\n"
        "Assign an existing Action to an Armature object so that the bones\n"
        "animate according to the Action's F-Curves.\n"
        "\n"
        "``armature_name`` must be an object of type ``ARMATURE`` in the\n"
        "scene.\n"
        "\n"
        "``action_name`` must already exist in ``bpy.data.actions``.  Use\n"
        "``action_list`` to discover available actions.\n"
        "\n"
        "Works with both legacy (single-slot) and the new slot-based actions\n"
        "introduced in Blender 4.4.\n"
        "\n"
        "Returns ``frame_start`` and ``frame_end`` \u2014 the time range of the\n"
        "applied action \u2014 so you can adjust the scene's frame range if needed.\n"
        "\n"
        "To animate an IK target after applying the action, create an Empty\n"
        "object and use ``object_keyframe_insert`` with ``location`` to\n"
        "keyframe its position at each key frame.\n",
        "inputSchema": {
            "properties": {
                "armature_name": {
                    "title": "Armature Name",
                    "type": "string"
                },
                "action_name": {
                    "title": "Action Name",
                    "type": "string"
                }
            },
            "required": [
                "armature_name",
                "action_name"
            ],
            "title": "armature_action_applyArguments",
            "type": "object"
        }
    },
    {
        "name": "asset_import",
        "description": "\n"
        "Import a 3D asset file into the current Blender scene.\n"
        "\n"
        "``filepath`` must be an absolute path to an existing file.\n"
        "\n"
        "Supported formats:\n"
        "\n"
        "- ``\"FBX\"``   \u2014 Autodesk FBX (``*.fbx``)\n"
        "- ``\"GLTF\"``  \u2014 GL Transmission Format (``*.gltf``, ``*.glb``)\n"
        "- ``\"OBJ\"``   \u2014 Wavefront OBJ (``*.obj``)\n"
        "\n"
        "``format`` overrides automatic detection; leave empty to detect\n"
        "from the file extension.\n"
        "\n"
        "Returns ``imported_objects`` \u2014 a list of the object names added\n"
        "to the scene by this import.  If the import adds no objects (e.g.\n"
        "the file is empty) the list is empty but ``status`` is still\n"
        "``\"ok\"``.\n"
        "\n"
        "Requires the corresponding Blender extension to be installed and\n"
        "enabled (FBX, GLTF, or the built-in OBJ importer).\n",
        "inputSchema": {
            "properties": {
                "filepath": {
                    "title": "Filepath",
                    "type": "string"
                },
                "format": {
                    "default": "",
                    "title": "Format",
                    "type": "string"
                }
            },
            "required": [
                "filepath"
            ],
            "title": "asset_importArguments",
            "type": "object"
        }
    },
    {
        "name": "blend_library_link",
        "description": "\n"
        "Link an object or collection from another ``.blend`` file into the\n"
        "current scene using Blender's **Library Link** mechanism.\n"
        "\n"
        "Linked assets remain read-only and are associated with the source\n"
        "file.  They appear in the Outliner with the external-link indicator\n"
        "(``obj.library`` is set).\n"
        "\n"
        "``filepath`` \u2014 absolute path to the source ``.blend`` file.\n"
        "\n"
        "``asset_type`` \u2014 ``\"OBJECT\"`` to link a single object, or\n"
        "``\"COLLECTION\"`` to link a whole collection.\n"
        "\n"
        "``asset_name`` \u2014 exact name of the object or collection inside the\n"
        "source file.  If the name is not found the error response includes\n"
        "``current_state.available_assets`` listing what is in the file, so\n"
        "you can retry with a correct name.\n"
        "\n"
        "Returns ``linked_objects`` \u2014 the names of objects added to the\n"
        "scene.  For ``asset_type=\"COLLECTION\"`` this includes all objects\n"
        "belonging to the linked collection.\n",
        "inputSchema": {
            "properties": {
                "filepath": {
                    "title": "Filepath",
                    "type": "string"
                },
                "asset_type": {
                    "title": "Asset Type",
                    "type": "string"
                },
                "asset_name": {
                    "title": "Asset Name",
                    "type": "string"
                }
            },
            "required": [
                "filepath",
                "asset_type",
                "asset_name"
            ],
            "title": "blend_library_linkArguments",
            "type": "object"
        }
    },
    {
        "name": "camera_target_track",
        "description": "\n"
        "Set up (or update) a Track-To constraint on a camera so it always\n"
        "looks at an Empty target object, and optionally insert a keyframe on\n"
        "the target's position.\n"
        "\n"
        "**Camera selection**\n"
        "- ``camera_name`` \u2014 name of a ``CAMERA`` object in the scene.\n"
        "  Leave empty to use the active scene camera.\n"
        "\n"
        "**Target Empty**\n"
        "- ``target_name`` \u2014 name of the Empty to use as the look-at point.\n"
        "  If the object does not exist it is created automatically.\n"
        "  Defaults to ``\"{camera_name}_Target\"``.\n"
        "- ``target_location`` \u2014 ``[x, y, z]`` world-space position to move\n"
        "  the target to. Omit to keep the target where it is.\n"
        "\n"
        "**Keyframing**\n"
        "- ``frame`` \u2014 frame number at which to insert a keyframe on the\n"
        "  target's ``location`` channel. Requires ``target_location``.\n"
        "  Pass ``-1`` (default) to skip keyframing.\n"
        "- ``interpolation`` \u2014 ``\"BEZIER\"`` (default), ``\"LINEAR\"``, or\n"
        "  ``\"CONSTANT\"``.\n"
        "\n"
        "**Constraint details**\n"
        "The Track-To constraint uses ``track_axis = TRACK_NEGATIVE_Z``\n"
        "(camera looks along its \u2212Z axis) and ``up_axis = UP_Y``.\n"
        "Calling this tool twice with the same target does not duplicate\n"
        "the constraint.\n"
        "\n"
        "To animate camera position, use ``object_keyframe_insert`` with\n"
        "the camera's name and the ``location`` channel.\n"
        "Use ``object_fcurve_list`` to verify written keyframes.\n",
        "inputSchema": {
            "properties": {
                "camera_name": {
                    "default": "",
                    "title": "Camera Name",
                    "type": "string"
                },
                "target_name": {
                    "default": "",
                    "title": "Target Name",
                    "type": "string"
                },
                "target_location": {
                    "anyOf": [
                        {
                            "items": {
                                "type": "number"
                            },
                            "type": "array"
                        },
                        {
                            "type": "null"
                        }
                    ],
                    "default": None,
                    "title": "Target Location"
                },
                "frame": {
                    "default": -1,
                    "title": "Frame",
                    "type": "integer"
                },
                "interpolation": {
                    "default": "BEZIER",
                    "title": "Interpolation",
                    "type": "string"
                }
            },
            "title": "camera_target_trackArguments",
            "type": "object"
        }
    },
    {
        "name": "execute_blender_code",
        "description": "\n"
        "Execute Python code in the connected Blender instance.\n"
        "\n"
        "The code runs in Blender's Python environment with full access to ``bpy``.\n"
        "To return data, assign a JSON-serialisable dict to a variable named ``result``.\n"
        "Deferred completion via ``check_is_finished`` is only supported by the\n"
        "interactive addon server, and is rejected in background mode.\n",
        "inputSchema": {
            "properties": {
                "code": {
                    "title": "Code",
                    "type": "string"
                }
            },
            "required": [
                "code"
            ],
            "title": "execute_blender_codeArguments",
            "type": "object"
        }
    },
    {
        "name": "execute_blender_code_for_cli",
        "description": "\n"
        "Execute Python code in a background Blender process.\n"
        "\n"
        "Opens *blend_file* with ``blender --background`` and runs *code*.\n"
        "Assign a dict to ``result`` to return data.\n",
        "inputSchema": {
            "properties": {
                "blend_file": {
                    "title": "Blend File",
                    "type": "string"
                },
                "code": {
                    "title": "Code",
                    "type": "string"
                }
            },
            "required": [
                "blend_file",
                "code"
            ],
            "title": "execute_blender_code_for_cliArguments",
            "type": "object"
        }
    },
    {
        "name": "geonodes_apply_preset",
        "description": "\n"
        "Add a Geometry Nodes modifier with a pre-built node graph to an object.\n"
        "\n"
        "``preset`` selects the graph template:\n"
        "\n"
        "- ``\"wave\"``           \u2014 Sine-wave Z-displacement driven by vertex\n"
        "  X position. Exposed inputs: ``Amplitude`` (default 0.3),\n"
        "  ``Frequency`` (default 2.0), ``Phase`` (default 0.0).\n"
        "- ``\"noise_displace\"`` \u2014 Random Z-displacement from a noise texture.\n"
        "  Exposed inputs: ``Strength`` (default 0.5),\n"
        "  ``Scale`` (default 2.0).\n"
        "\n"
        "``modifier_name`` sets the modifier display name (defaults to a\n"
        "title-cased version of the preset name).\n"
        "\n"
        "If a NODES modifier with the same name already exists its node\n"
        "tree is replaced. Call ``geonodes_query`` to inspect the result,\n"
        "and ``geonodes_node_set`` / ``geonodes_node_keyframe`` to adjust\n"
        "parameters.\n",
        "inputSchema": {
            "properties": {
                "object_name": {
                    "title": "Object Name",
                    "type": "string"
                },
                "preset": {
                    "title": "Preset",
                    "type": "string"
                },
                "modifier_name": {
                    "default": "",
                    "title": "Modifier Name",
                    "type": "string"
                }
            },
            "required": [
                "object_name",
                "preset"
            ],
            "title": "geonodes_apply_presetArguments",
            "type": "object"
        }
    },
    {
        "name": "geonodes_node_keyframe",
        "description": "\n"
        "Insert a keyframe for a node input socket in a Geometry Nodes graph.\n"
        "\n"
        "Sets ``value`` on the socket's ``default_value`` and inserts a\n"
        "keyframe at ``frame``.  The keyframe is stored in the node tree's\n"
        "animation data and will appear in the Graph Editor under the node\n"
        "tree name.\n"
        "\n"
        "``interpolation`` is one of ``\"BEZIER\"`` (default), ``\"LINEAR\"``,\n"
        "or ``\"CONSTANT\"``.\n"
        "\n"
        "Only scalar (float / int / bool) socket types are supported. For\n"
        "vector inputs use ``execute_blender_code``.\n"
        "\n"
        "Use ``geonodes_query`` to find node and input names.\n",
        "inputSchema": {
            "properties": {
                "object_name": {
                    "title": "Object Name",
                    "type": "string"
                },
                "node_name": {
                    "title": "Node Name",
                    "type": "string"
                },
                "input_name": {
                    "title": "Input Name",
                    "type": "string"
                },
                "frame": {
                    "title": "Frame",
                    "type": "integer"
                },
                "value": {
                    "title": "Value",
                    "type": "number"
                },
                "interpolation": {
                    "default": "BEZIER",
                    "title": "Interpolation",
                    "type": "string"
                }
            },
            "required": [
                "object_name",
                "node_name",
                "input_name",
                "frame",
                "value"
            ],
            "title": "geonodes_node_keyframeArguments",
            "type": "object"
        }
    },
    {
        "name": "geonodes_node_set",
        "description": "\n"
        "Set the ``default_value`` of a node input socket in a Geometry Nodes\n"
        "graph.\n"
        "\n"
        "``node_name`` is the display name of the node as returned by\n"
        "``geonodes_query`` (e.g. ``\"Multiply Frequency\"``).\n"
        "\n"
        "``input_name`` is the socket label (e.g. ``\"Value\"``,\n"
        "``\"Scale\"``, ``\"Strength\"``).\n"
        "\n"
        "``value`` is a scalar float; Blender automatically coerces it for\n"
        "integer or boolean socket types. For vector or geometry sockets\n"
        "use ``execute_blender_code``.\n"
        "\n"
        "Returns ``old_value`` and ``new_value`` so you can verify the\n"
        "change.\n",
        "inputSchema": {
            "properties": {
                "object_name": {
                    "title": "Object Name",
                    "type": "string"
                },
                "node_name": {
                    "title": "Node Name",
                    "type": "string"
                },
                "input_name": {
                    "title": "Input Name",
                    "type": "string"
                },
                "value": {
                    "title": "Value",
                    "type": "number"
                }
            },
            "required": [
                "object_name",
                "node_name",
                "input_name",
                "value"
            ],
            "title": "geonodes_node_setArguments",
            "type": "object"
        }
    },
    {
        "name": "geonodes_query",
        "description": "\n"
        "Return the node graph structure of a Geometry Nodes modifier.\n"
        "\n"
        "``modifier_name`` selects which NODES modifier to inspect. If\n"
        "empty the first NODES modifier on the object is used.\n"
        "\n"
        "Returns ``nodes`` \u2014 a list of node dicts, each with:\n"
        "\n"
        "- ``name``        \u2014 node display name\n"
        "- ``bl_idname``   \u2014 Blender node type identifier\n"
        "- ``location``    \u2014 ``[x, y]`` in the node editor\n"
        "- ``inputs``      \u2014 list of input sockets with ``name``,\n"
        "  ``type``, ``is_linked``, and (when not linked)\n"
        "  ``default_value``\n"
        "\n"
        "Use ``geonodes_apply_preset`` to create a Geometry Nodes modifier\n"
        "with a ready-made node graph.\n",
        "inputSchema": {
            "properties": {
                "object_name": {
                    "title": "Object Name",
                    "type": "string"
                },
                "modifier_name": {
                    "default": "",
                    "title": "Modifier Name",
                    "type": "string"
                }
            },
            "required": [
                "object_name"
            ],
            "title": "geonodes_queryArguments",
            "type": "object"
        }
    },
    {
        "name": "get_blendfile_summary_datablocks",
        "description": "\n"
        "Return a summary of the blend file: data-block counts, active workspace, and render engine.\n",
        "inputSchema": {
            "properties": {},
            "title": "get_blendfile_summary_datablocksArguments",
            "type": "object"
        }
    },
    {
        "name": "get_blendfile_summary_datablocks_for_cli",
        "description": "\n"
        "Return a data-block summary by opening *blend_file* in background Blender.\n",
        "inputSchema": {
            "properties": {
                "blend_file": {
                    "title": "Blend File",
                    "type": "string"
                }
            },
            "required": [
                "blend_file"
            ],
            "title": "get_blendfile_summary_datablocks_for_cliArguments",
            "type": "object"
        }
    },
    {
        "name": "get_blendfile_summary_missing_files",
        "description": "\n"
        "Report external file references that are missing from disk\n"
        "(images, libraries, fonts, sounds, movie clips, caches, sequences).\n",
        "inputSchema": {
            "properties": {},
            "title": "get_blendfile_summary_missing_filesArguments",
            "type": "object"
        }
    },
    {
        "name": "get_blendfile_summary_missing_files_for_cli",
        "description": "\n"
        "Report missing file references by opening *blend_file* in background Blender.\n",
        "inputSchema": {
            "properties": {
                "blend_file": {
                    "title": "Blend File",
                    "type": "string"
                }
            },
            "required": [
                "blend_file"
            ],
            "title": "get_blendfile_summary_missing_files_for_cliArguments",
            "type": "object"
        }
    },
    {
        "name": "get_blendfile_summary_of_linked_libraries",
        "description": "\n"
        "Return a tree of directly and indirectly linked library files.\n",
        "inputSchema": {
            "properties": {},
            "title": "get_blendfile_summary_of_linked_librariesArguments",
            "type": "object"
        }
    },
    {
        "name": "get_blendfile_summary_of_linked_libraries_for_cli",
        "description": "\n"
        "Return linked-library info by opening *blend_file* in background Blender.\n",
        "inputSchema": {
            "properties": {
                "blend_file": {
                    "title": "Blend File",
                    "type": "string"
                }
            },
            "required": [
                "blend_file"
            ],
            "title": "get_blendfile_summary_of_linked_libraries_for_cliArguments",
            "type": "object"
        }
    },
    {
        "name": "get_blendfile_summary_path_info",
        "description": "\n"
        "Simple/fast access to the blend file's path, save status, age, and backups.\n",
        "inputSchema": {
            "properties": {},
            "title": "get_blendfile_summary_path_infoArguments",
            "type": "object"
        }
    },
    {
        "name": "get_blendfile_summary_path_info_for_cli",
        "description": "\n"
        "Return path info by opening *blend_file* in background Blender.\n",
        "inputSchema": {
            "properties": {
                "blend_file": {
                    "title": "Blend File",
                    "type": "string"
                }
            },
            "required": [
                "blend_file"
            ],
            "title": "get_blendfile_summary_path_info_for_cliArguments",
            "type": "object"
        }
    },
    {
        "name": "get_blendfile_summary_usage_guess",
        "description": "\n"
        "Guess the primary use-cases of the current blend file (scored 0-100 with certainty).\n",
        "inputSchema": {
            "properties": {},
            "title": "get_blendfile_summary_usage_guessArguments",
            "type": "object"
        }
    },
    {
        "name": "get_blendfile_summary_usage_guess_for_cli",
        "description": "\n"
        "Guess use-cases by opening *blend_file* in background Blender.\n",
        "inputSchema": {
            "properties": {
                "blend_file": {
                    "title": "Blend File",
                    "type": "string"
                }
            },
            "required": [
                "blend_file"
            ],
            "title": "get_blendfile_summary_usage_guess_for_cliArguments",
            "type": "object"
        }
    },
    {
        "name": "get_object_detail_summary",
        "description": "\n"
        "Return a structured summary of the object identified by *name*.\n"
        "\n"
        "Includes type, transforms, parent, children, modifiers, constraints,\n"
        "materials, visibility, data-block name, and collections.\n",
        "inputSchema": {
            "properties": {
                "name": {
                    "title": "Name",
                    "type": "string"
                }
            },
            "required": [
                "name"
            ],
            "title": "get_object_detail_summaryArguments",
            "type": "object"
        }
    },
    {
        "name": "get_objects_summary",
        "description": "\n"
        "Return the scene's collection hierarchy and their objects.\n"
        "\n"
        "Each collection lists its objects (name, type, parent, data name,\n"
        "selection, visibility) and nested child collections.\n",
        "inputSchema": {
            "properties": {},
            "title": "get_objects_summaryArguments",
            "type": "object"
        }
    },
    {
        "name": "get_python_api_docs",
        "description": "\n"
        "Return the Blender Python API docs for *identifier*, or list\n"
        "modules matching a trailing-``*`` discovery pattern.\n"
        "\n"
        "*identifier* should be a fully-qualified Python name (e.g.\n"
        "``bpy.app`` or ``bpy.types.Scene.frame_current``).\n"
        "The trailing-``*`` forms are supported as discovery entry-points:\n"
        "\n"
        "- ``*`` enumerates the top-level modules (``bpy``, ``bmesh``,\n"
        "  ``mathutils``, ``gpu``, ...).\n"
        "- ``X.*`` enumerates the direct-child identifiers under the\n"
        "  *X* namespace (``bpy.*`` -> ``bpy.app``, ``bpy.context``, ...).\n"
        "\n"
        "Both return a ``namespace`` response even when ``X.rst`` would\n"
        "otherwise resolve to ``exact``; the ``.*`` form lets an agent\n"
        "force the child listing.\n"
        "\n"
        "The response always carries ``kind``, ``found``, and ``identifier``.\n"
        "The remaining keys depend on ``kind``:\n"
        "\n"
        "- ``\"exact\"`` (``found=True``): ``<identifier>.rst`` was read.\n"
        "  Extra keys: ``content`` (RST text), ``examples``. When the\n"
        "  file exceeds 32 KB, ``content`` is replaced with a dot-point\n"
        "  summary of the file's top-level definitions (prefixed by a\n"
        "  header noting the truncation) and ``examples`` is empty -\n"
        "  re-query individual members for their rendered blocks.\n"
        "- ``\"namespace\"`` (``found=True``):\n"
        "  no ``<identifier>.rst`` but ``<identifier>.<child>.rst`` siblings exist.\n"
        "  Extra key: ``submodules`` (list of child identifiers).\n"
        "- ``\"definition\"`` (``found=True``):\n"
        "  *identifier* is defined inside a parent RST\n"
        "  (e.g. ``bpy.props.IntProperty`` lives in ``bpy.props.rst``).\n"
        "  Extra keys: ``content`` (rendered block), ``examples``.\n"
        "- ``\"partial\"`` (``found=False``):\n"
        "  the parent RST was located but the trailing component isn't defined in it.\n"
        "  Extra keys:\n"
        "  - ``parent`` the identifier whose RST was loaded.\n"
        "  - ``available`` top-level definitions in that RST.\n"
        "  - ``submodules`` sibling identifiers ``<parent>.<child>`` with their own RSTs,\n"
        "    filtered to those whose last component contains every character of the missing tail.\n"
        "\n"
        "  For a toctree landing page like ``bpy.types`` ``available`` is empty and ``submodules``\n"
        "  is the near-miss list; for a self-contained module like ``bpy.props`` it's the reverse.\n"
        "- ``\"suggestions\"`` (``found=False``):\n"
        "  no direct match, but *identifier* appears as a component of other files.\n"
        "  Extra key: ``suggestions`` (list of full identifiers).\n"
        "- ``\"missing\"`` (``found=False``): nothing matched.\n"
        "\n"
        "``examples`` (present on the ``exact`` and ``definition`` kinds)\n"
        "is a list of ``{path, content}`` entries referenced from this documentation.\n",
        "inputSchema": {
            "properties": {
                "identifier": {
                    "title": "Identifier",
                    "type": "string"
                }
            },
            "required": [
                "identifier"
            ],
            "title": "get_python_api_docsArguments",
            "type": "object"
        }
    },
    {
        "name": "get_scene_state",
        "description": "\n"
        "Return the current scene's timeline parameters and a flat list of\n"
        "all objects with their name, type, and world-space location.\n"
        "\n"
        "Includes ``frame_start``, ``frame_end``, ``frame_current``, and\n"
        "``fps`` so the AI can plan keyframe placement without a separate\n"
        "query. Works in both background and interactive Blender sessions.\n"
        "\n"
        "Call this at the start of any animation workflow to understand\n"
        "the scene layout and timeline before issuing further tool calls.\n",
        "inputSchema": {
            "properties": {},
            "title": "get_scene_stateArguments",
            "type": "object"
        }
    },
    {
        "name": "get_screenshot_of_area_as_image",
        "description": "\n"
        "Take a screenshot of a single Blender area and return it as a PNG image.\n"
        "\n"
        "*area_ui_type* matches the area's ``ui_type``.\n"
        "\n"
        "*size_limit_in_bytes* caps the image size in bytes.\n"
        "Zero (the default) uses the MCP message size limit.\n",
        "inputSchema": {
            "properties": {
                "area_ui_type": {
                    "enum": [
                        "VIEW_3D",
                        "IMAGE_EDITOR",
                        "UV",
                        "ShaderNodeTree",
                        "CompositorNodeTree",
                        "GeometryNodeTree",
                        "TextureNodeTree",
                        "SEQUENCE_EDITOR",
                        "CLIP_EDITOR",
                        "DOPESHEET_EDITOR",
                        "GRAPH_EDITOR",
                        "NLA_EDITOR",
                        "TEXT_EDITOR",
                        "CONSOLE",
                        "INFO",
                        "TOPBAR",
                        "STATUSBAR",
                        "OUTLINER",
                        "PROPERTIES",
                        "FILE_BROWSER",
                        "SPREADSHEET",
                        "PREFERENCES"
                    ],
                    "title": "Area Ui Type",
                    "type": "string"
                },
                "size_limit_in_bytes": {
                    "default": 0,
                    "title": "Size Limit In Bytes",
                    "type": "integer"
                }
            },
            "required": [
                "area_ui_type"
            ],
            "title": "get_screenshot_of_area_as_imageArguments",
            "type": "object"
        }
    },
    {
        "name": "get_screenshot_of_window_as_image",
        "description": "\n"
        "Take a screenshot of the entire Blender window and return it as a PNG image.\n"
        "\n"
        "*size_limit_in_bytes* caps the image size in bytes.\n"
        "Zero (the default) uses the MCP message size limit.\n",
        "inputSchema": {
            "properties": {
                "size_limit_in_bytes": {
                    "default": 0,
                    "title": "Size Limit In Bytes",
                    "type": "integer"
                }
            },
            "title": "get_screenshot_of_window_as_imageArguments",
            "type": "object"
        }
    },
    {
        "name": "get_screenshot_of_window_as_json",
        "description": "\n"
        "Return a JSON description of the Blender window layout, areas, active object, and selection.\n",
        "inputSchema": {
            "properties": {},
            "title": "get_screenshot_of_window_as_jsonArguments",
            "type": "object"
        }
    },
    {
        "name": "gp_layer_create",
        "description": "\n"
        "Add a new layer to an existing Grease Pencil object.\n"
        "\n"
        "``object_name`` must refer to a ``GREASEPENCIL`` type object\n"
        "already in the scene (use ``gp_object_create`` to create one).\n"
        "``layer_name`` is the display name of the new layer.\n"
        "\n"
        "Returns an error if the object is not found or is not a\n"
        "Grease Pencil object. Duplicate layer names are allowed by\n"
        "Blender and are not treated as errors.\n",
        "inputSchema": {
            "properties": {
                "object_name": {
                    "title": "Object Name",
                    "type": "string"
                },
                "layer_name": {
                    "default": "Layer",
                    "title": "Layer Name",
                    "type": "string"
                }
            },
            "required": [
                "object_name"
            ],
            "title": "gp_layer_createArguments",
            "type": "object"
        }
    },
    {
        "name": "gp_layer_delete",
        "description": "\n"
        "Remove a layer from a Grease Pencil object.\n"
        "\n"
        "All strokes and keyframes stored on the layer are permanently\n"
        "deleted. Use ``gp_layers_list`` first to verify the layer name.\n"
        "\n"
        "Returns an error if the object or layer is not found.\n",
        "inputSchema": {
            "properties": {
                "object_name": {
                    "title": "Object Name",
                    "type": "string"
                },
                "layer_name": {
                    "title": "Layer Name",
                    "type": "string"
                }
            },
            "required": [
                "object_name",
                "layer_name"
            ],
            "title": "gp_layer_deleteArguments",
            "type": "object"
        }
    },
    {
        "name": "gp_layer_keyframes_list",
        "description": "\n"
        "Return all opacity keyframes on a Grease Pencil layer, sorted by frame.\n"
        "\n"
        "Each entry in ``keyframes`` contains:\n"
        "\n"
        "- ``frame``: the scene frame number (integer).\n"
        "- ``opacity``: the opacity value at that frame (float, 0.0\u20131.0).\n"
        "\n"
        "Returns an empty ``keyframes`` list if no opacity keyframes have\n"
        "been set on this layer yet.\n"
        "\n"
        "Use ``gp_layer_opacity_set`` to insert keyframes, then call\n"
        "this tool to verify the animation curve before rendering.\n"
        "\n"
        "Returns an error if the object or layer is not found.\n",
        "inputSchema": {
            "properties": {
                "object_name": {
                    "title": "Object Name",
                    "type": "string"
                },
                "layer_name": {
                    "title": "Layer Name",
                    "type": "string"
                }
            },
            "required": [
                "object_name",
                "layer_name"
            ],
            "title": "gp_layer_keyframes_listArguments",
            "type": "object"
        }
    },
    {
        "name": "gp_layer_opacity_set",
        "description": "\n"
        "Set the opacity of a Grease Pencil layer and insert a keyframe.\n"
        "\n"
        "``opacity`` must be in ``[0.0, 1.0]``: ``0.0`` is fully\n"
        "transparent, ``1.0`` is fully opaque.\n"
        "\n"
        "The keyframe is inserted at ``frame`` in the scene timeline.\n"
        "If a keyframe already exists at that frame it is overwritten.\n"
        "\n"
        "Call this multiple times with different ``frame`` values to\n"
        "build an opacity animation.  Use ``gp_layer_keyframes_list``\n"
        "afterwards to verify the inserted keyframes.\n"
        "\n"
        "Returns an error if the object or layer is not found, or if\n"
        "``opacity`` is outside ``[0.0, 1.0]``.\n",
        "inputSchema": {
            "properties": {
                "object_name": {
                    "title": "Object Name",
                    "type": "string"
                },
                "layer_name": {
                    "title": "Layer Name",
                    "type": "string"
                },
                "frame": {
                    "title": "Frame",
                    "type": "integer"
                },
                "opacity": {
                    "title": "Opacity",
                    "type": "number"
                }
            },
            "required": [
                "object_name",
                "layer_name",
                "frame",
                "opacity"
            ],
            "title": "gp_layer_opacity_setArguments",
            "type": "object"
        }
    },
    {
        "name": "gp_layers_list",
        "description": "\n"
        "Return all layers on a Grease Pencil object in their stack order.\n"
        "\n"
        "Each layer entry contains ``name``, ``opacity``, and ``hide``.\n"
        "Layers are listed top-to-bottom as they appear in Blender's\n"
        "layer panel (index 0 = topmost layer).\n"
        "\n"
        "Returns an error if the object is not found or is not a\n"
        "Grease Pencil object.\n",
        "inputSchema": {
            "properties": {
                "object_name": {
                    "title": "Object Name",
                    "type": "string"
                }
            },
            "required": [
                "object_name"
            ],
            "title": "gp_layers_listArguments",
            "type": "object"
        }
    },
    {
        "name": "gp_material_assign",
        "description": "\n"
        "Assign a Grease Pencil material to a GP object's material slots.\n"
        "\n"
        "If the material is already in a slot on ``object_name``, the\n"
        "existing ``slot_index`` is returned without creating a duplicate.\n"
        "Otherwise the material is appended to the end of the slot list.\n"
        "\n"
        "The returned ``slot_index`` (0-based) is the value to pass as\n"
        "``material_index`` when calling ``gp_stroke_draw`` or\n"
        "``gp_shape_draw``.\n"
        "\n"
        "Returns an error if the object is not found, is not a Grease\n"
        "Pencil object, or the material does not exist or is not a GP\n"
        "material (use ``gp_material_create`` to make one).\n",
        "inputSchema": {
            "properties": {
                "object_name": {
                    "title": "Object Name",
                    "type": "string"
                },
                "material_name": {
                    "title": "Material Name",
                    "type": "string"
                }
            },
            "required": [
                "object_name",
                "material_name"
            ],
            "title": "gp_material_assignArguments",
            "type": "object"
        }
    },
    {
        "name": "gp_material_create",
        "description": "\n"
        "Create a Grease Pencil material with stroke and fill colors (GPv3).\n"
        "\n"
        "Colors are RGBA lists with values in ``[0.0, 1.0]``:\n"
        "\n"
        "- ``stroke_color``: outline color, default opaque black\n"
        "  ``[0.0, 0.0, 0.0, 1.0]``.\n"
        "- ``fill_color``: interior fill color, default fully transparent\n"
        "  ``[1.0, 1.0, 1.0, 0.0]``.  Set alpha ``> 0`` to make fill\n"
        "  visible.\n"
        "\n"
        "Blender uses **linear** color space internally; the values you\n"
        "provide are treated as linear, not sRGB.  Pure black\n"
        "``[0, 0, 0, 1]`` and pure white ``[1, 1, 1, 1]`` are\n"
        "unaffected; intermediate colors will appear slightly different\n"
        "from sRGB equivalents.\n"
        "\n"
        "After creation, assign the material to a GP object with\n"
        "``gp_material_assign``, then reference it by slot index when\n"
        "drawing strokes via ``gp_stroke_draw`` or ``gp_shape_draw``.\n"
        "\n"
        "The returned ``name`` is the actual name Blender assigned\n"
        "(may differ if a material with that name already exists).\n",
        "inputSchema": {
            "properties": {
                "name": {
                    "default": "GPMaterial",
                    "title": "Name",
                    "type": "string"
                },
                "stroke_color": {
                    "default": [
                        0.0,
                        0.0,
                        0.0,
                        1.0
                    ],
                    "items": {
                        "type": "number"
                    },
                    "title": "Stroke Color",
                    "type": "array"
                },
                "fill_color": {
                    "default": [
                        1.0,
                        1.0,
                        1.0,
                        0.0
                    ],
                    "items": {
                        "type": "number"
                    },
                    "title": "Fill Color",
                    "type": "array"
                }
            },
            "title": "gp_material_createArguments",
            "type": "object"
        }
    },
    {
        "name": "gp_object_create",
        "description": "\n"
        "Create a new Grease Pencil object in the active scene.\n"
        "\n"
        "Blender deduplicates names automatically: if an object named\n"
        "``name`` already exists, the new object receives a ``.001`` suffix\n"
        "(or the next available number). The returned ``name`` field always\n"
        "reflects the actual name assigned by Blender.\n"
        "\n"
        "The object is linked to the scene's root collection.\n"
        "Call ``gp_layer_create`` next to add at least one drawing layer.\n",
        "inputSchema": {
            "properties": {
                "name": {
                    "default": "GreasePencil",
                    "title": "Name",
                    "type": "string"
                }
            },
            "title": "gp_object_createArguments",
            "type": "object"
        }
    },
    {
        "name": "gp_shape_draw",
        "description": "\n"
        "Draw a predefined geometric shape on a Grease Pencil layer (GPv3).\n"
        "\n"
        "``shape`` must be one of ``\"line\"``, ``\"rect\"``, or ``\"circle\"``.\n"
        "\n"
        "For ``\"line\"``: a straight stroke from ``(x1, y1, z1)`` to\n"
        "``(x2, y2, z2)``.  ``points_count`` sets the number of evenly\n"
        "spaced points along the line (minimum 2, default 2).\n"
        "\n"
        "For ``\"rect\"``: a closed rectangle centred at ``(cx, cy, cz)``\n"
        "in the XZ plane. ``width`` is the total X-extent; ``height`` is\n"
        "the total Z-extent. Both default to ``2.0``.\n"
        "\n"
        "For ``\"circle\"``: a polygon approximation of a circle centred\n"
        "at ``(cx, cy, cz)`` in the XZ plane. ``radius`` controls size\n"
        "(default ``1.0``); ``segments`` controls smoothness (default\n"
        "``32``).\n"
        "\n"
        "For freeform polylines or paths, use ``gp_stroke_draw`` instead.\n"
        "\n"
        "``mode`` controls existing strokes on the frame:\n"
        "\n"
        "- ``\"replace\"``: clears all strokes before drawing.\n"
        "- ``\"append\"``: adds the shape alongside existing strokes.\n"
        "\n"
        "``stroke_radius`` is the point radius in object-space units\n"
        "(controls stroke thickness, default ``0.01``).\n"
        "``material_index`` selects the GP material slot (0-based).\n"
        "\n"
        "Returns an error if the object, layer, shape, or mode is invalid.\n",
        "inputSchema": {
            "properties": {
                "object_name": {
                    "title": "Object Name",
                    "type": "string"
                },
                "layer_name": {
                    "title": "Layer Name",
                    "type": "string"
                },
                "frame": {
                    "title": "Frame",
                    "type": "integer"
                },
                "shape": {
                    "title": "Shape",
                    "type": "string"
                },
                "cx": {
                    "default": 0.0,
                    "title": "Cx",
                    "type": "number"
                },
                "cy": {
                    "default": 0.0,
                    "title": "Cy",
                    "type": "number"
                },
                "cz": {
                    "default": 0.0,
                    "title": "Cz",
                    "type": "number"
                },
                "radius": {
                    "default": 1.0,
                    "title": "Radius",
                    "type": "number"
                },
                "width": {
                    "default": 2.0,
                    "title": "Width",
                    "type": "number"
                },
                "height": {
                    "default": 2.0,
                    "title": "Height",
                    "type": "number"
                },
                "segments": {
                    "default": 32,
                    "title": "Segments",
                    "type": "integer"
                },
                "mode": {
                    "default": "replace",
                    "title": "Mode",
                    "type": "string"
                },
                "stroke_radius": {
                    "default": 0.01,
                    "title": "Stroke Radius",
                    "type": "number"
                },
                "material_index": {
                    "default": 0,
                    "title": "Material Index",
                    "type": "integer"
                },
                "x1": {
                    "default": 0.0,
                    "title": "X1",
                    "type": "number"
                },
                "y1": {
                    "default": 0.0,
                    "title": "Y1",
                    "type": "number"
                },
                "z1": {
                    "default": 0.0,
                    "title": "Z1",
                    "type": "number"
                },
                "x2": {
                    "default": 1.0,
                    "title": "X2",
                    "type": "number"
                },
                "y2": {
                    "default": 0.0,
                    "title": "Y2",
                    "type": "number"
                },
                "z2": {
                    "default": 0.0,
                    "title": "Z2",
                    "type": "number"
                },
                "points_count": {
                    "default": 2,
                    "title": "Points Count",
                    "type": "integer"
                }
            },
            "required": [
                "object_name",
                "layer_name",
                "frame",
                "shape"
            ],
            "title": "gp_shape_drawArguments",
            "type": "object"
        }
    },
    {
        "name": "gp_stroke_draw",
        "description": "\n"
        "Draw a stroke on a Grease Pencil layer at the given frame (GPv3).\n"
        "\n"
        "``points`` is a list of ``[x, y, z]`` coordinates defining the\n"
        "stroke path. Provide two points for a straight line; three or more\n"
        "for a curve or polyline. Blender uses a right-hand coordinate system:\n"
        "X right, Y into the screen, Z up. For 2D animation draw in the XZ\n"
        "plane (Y = 0) and place the camera along -Y.\n"
        "\n"
        "``mode`` controls existing strokes on that frame:\n"
        "\n"
        "- ``\"replace\"``: clears all existing strokes before drawing.\n"
        "- ``\"append\"``: adds the new stroke alongside existing ones.\n"
        "\n"
        "``stroke_radius`` is the point radius in object-space units; it\n"
        "controls stroke thickness (default ``0.01``).\n"
        "\n"
        "``material_index`` selects the GP material slot (0-based).\n"
        "\n"
        "The frame is created automatically if it does not exist.\n"
        "Returns an error if the object, layer, mode, or points are invalid.\n",
        "inputSchema": {
            "properties": {
                "object_name": {
                    "title": "Object Name",
                    "type": "string"
                },
                "layer_name": {
                    "title": "Layer Name",
                    "type": "string"
                },
                "frame": {
                    "title": "Frame",
                    "type": "integer"
                },
                "points": {
                    "items": {
                        "items": {
                            "type": "number"
                        },
                        "type": "array"
                    },
                    "title": "Points",
                    "type": "array"
                },
                "mode": {
                    "default": "replace",
                    "title": "Mode",
                    "type": "string"
                },
                "stroke_radius": {
                    "default": 0.01,
                    "title": "Stroke Radius",
                    "type": "number"
                },
                "material_index": {
                    "default": 0,
                    "title": "Material Index",
                    "type": "integer"
                }
            },
            "required": [
                "object_name",
                "layer_name",
                "frame",
                "points"
            ],
            "title": "gp_stroke_drawArguments",
            "type": "object"
        }
    },
    {
        "name": "jump_to_tab_by_name",
        "description": "\n"
        "Switch the active workspace tab to *name*.\n",
        "inputSchema": {
            "properties": {
                "name": {
                    "title": "Name",
                    "type": "string"
                }
            },
            "required": [
                "name"
            ],
            "title": "jump_to_tab_by_nameArguments",
            "type": "object"
        }
    },
    {
        "name": "jump_to_tab_by_space_type",
        "description": "\n"
        "Switch to a workspace whose main area matches *space_type*.\n"
        "\n"
        "If *allow_edits* is True and no matching workspace exists, a new one\n"
        "is created by duplicating the current workspace.\n",
        "inputSchema": {
            "properties": {
                "space_type": {
                    "title": "Space Type",
                    "type": "string"
                },
                "allow_edits": {
                    "default": False,
                    "title": "Allow Edits",
                    "type": "boolean"
                }
            },
            "required": [
                "space_type"
            ],
            "title": "jump_to_tab_by_space_typeArguments",
            "type": "object"
        }
    },
    {
        "name": "jump_to_view3d_object_by_name",
        "description": "\n"
        "Move the 3D viewport to focus on an object by *name*.\n"
        "\n"
        "If *allow_edits* is True the object may be un-hidden and its\n"
        "collections enabled to make it visible.\n",
        "inputSchema": {
            "properties": {
                "name": {
                    "title": "Name",
                    "type": "string"
                },
                "allow_edits": {
                    "default": False,
                    "title": "Allow Edits",
                    "type": "boolean"
                }
            },
            "required": [
                "name"
            ],
            "title": "jump_to_view3d_object_by_nameArguments",
            "type": "object"
        }
    },
    {
        "name": "jump_to_view3d_object_data_by_name",
        "description": "\n"
        "Move the 3D viewport to the object whose data block matches *name*.\n"
        "\n"
        "If *allow_edits* is True the object may be un-hidden and its\n"
        "collections enabled to make it visible.\n",
        "inputSchema": {
            "properties": {
                "name": {
                    "title": "Name",
                    "type": "string"
                },
                "allow_edits": {
                    "default": False,
                    "title": "Allow Edits",
                    "type": "boolean"
                }
            },
            "required": [
                "name"
            ],
            "title": "jump_to_view3d_object_data_by_nameArguments",
            "type": "object"
        }
    },
    {
        "name": "material_list",
        "description": "\n"
        "Return all materials stored in the current Blender file with their\n"
        "basic shading properties.\n"
        "\n"
        "Each entry in ``materials`` contains:\n"
        "\n"
        "- ``name``             \u2014 material name\n"
        "- ``use_nodes``        \u2014 whether node-based shading is enabled\n"
        "- ``is_grease_pencil`` \u2014 True for GP / annotation materials\n"
        "- ``diffuse_color``    \u2014 ``[R, G, B, A]`` from the material's\n"
        "  base diffuse colour (always present)\n"
        "\n"
        "When ``use_nodes`` is True and a **Principled BSDF** node is found:\n"
        "\n"
        "- ``base_color``       \u2014 ``[R, G, B, A]`` from the Base Color input\n"
        "- ``metallic``         \u2014 float 0\u20131\n"
        "- ``roughness``        \u2014 float 0\u20131\n"
        "\n"
        "For Grease Pencil materials (when ``include_grease_pencil=True``):\n"
        "\n"
        "- ``stroke_color``     \u2014 ``[R, G, B, A]``\n"
        "- ``fill_color``       \u2014 ``[R, G, B, A]``\n"
        "- ``show_stroke``      \u2014 bool\n"
        "- ``show_fill``        \u2014 bool\n"
        "\n"
        "Results are sorted alphabetically by material name.\n",
        "inputSchema": {
            "properties": {
                "include_grease_pencil": {
                    "default": False,
                    "title": "Include Grease Pencil",
                    "type": "boolean"
                }
            },
            "title": "material_listArguments",
            "type": "object"
        }
    },
    {
        "name": "mesh_primitive_add",
        "description": "\n"
        "Create a basic 3D mesh primitive in the active scene.\n"
        "\n"
        "``primitive_type`` selects the geometry to create. Supported values:\n"
        "\n"
        "- ``\"CUBE\"``     \u2014 2\u00d72\u00d72 cube centred at *location*\n"
        "- ``\"SPHERE\"``   \u2014 UV sphere with radius 1 at *location*\n"
        "- ``\"PLANE\"``    \u2014 2\u00d72 plane at *location*\n"
        "- ``\"CYLINDER\"`` \u2014 cylinder with radius 1 and height 2 at *location*\n"
        "\n"
        "``name`` sets the object (and mesh data) name. If omitted Blender\n"
        "assigns a default name such as ``\"Cube\"``, ``\"Sphere\"``, etc.\n"
        "Blender automatically appends ``.001`` suffixes when a name is\n"
        "already taken; the returned ``name`` always reflects the actual name.\n"
        "\n"
        "``location`` is ``[x, y, z]`` in world space (default ``[0, 0, 0]``).\n"
        "\n"
        "After creation, use ``get_object_detail_summary`` to inspect the\n"
        "object, or ``get_scene_state`` to list all scene objects.\n",
        "inputSchema": {
            "properties": {
                "primitive_type": {
                    "title": "Primitive Type",
                    "type": "string"
                },
                "name": {
                    "default": "",
                    "title": "Name",
                    "type": "string"
                },
                "location": {
                    "anyOf": [
                        {
                            "items": {
                                "type": "number"
                            },
                            "type": "array"
                        },
                        {
                            "type": "null"
                        }
                    ],
                    "default": None,
                    "title": "Location"
                }
            },
            "required": [
                "primitive_type"
            ],
            "title": "mesh_primitive_addArguments",
            "type": "object"
        }
    },
    {
        "name": "object_driver_add",
        "description": "\n"
        "Add (or update) a scripted driver on a property of a scene object.\n"
        "\n"
        "A *driver* is a Python expression that controls a property value\n"
        "at every frame, enabling procedural animation without manual\n"
        "keyframing.\n"
        "\n"
        "**Parameters**\n"
        "\n"
        "- ``data_path``  \u2014 property channel to drive. Common values:\n"
        "  ``\"location\"``, ``\"rotation_euler\"``, ``\"scale\"``.\n"
        "- ``index``      \u2014 array component: ``0`` = X, ``1`` = Y, ``2`` = Z.\n"
        "  Use ``-1`` for scalar (non-array) properties.\n"
        "- ``expression`` \u2014 Python expression string evaluated each frame.\n"
        "  The variable ``frame`` contains the current scene frame number.\n"
        "  Maths functions (``sin``, ``cos``, ``pi``, etc.) are available\n"
        "  without imports.\n"
        "\n"
        "**Examples**\n"
        "\n"
        "- Oscillate Z position: ``data_path=\"location\", index=2,``\n"
        "  ``expression=\"sin(frame/10)\"``\n"
        "- Constant rotation: ``data_path=\"rotation_euler\", index=2,``\n"
        "  ``expression=\"frame * 0.1\"``\n"
        "\n"
        "If a driver already exists at the given ``data_path`` / ``index``\n"
        "it is updated in place (``action`` field returns ``\"updated\"``).\n"
        "\n"
        "Use ``object_driver_list`` to read back and verify drivers.\n",
        "inputSchema": {
            "properties": {
                "object_name": {
                    "title": "Object Name",
                    "type": "string"
                },
                "data_path": {
                    "title": "Data Path",
                    "type": "string"
                },
                "index": {
                    "title": "Index",
                    "type": "integer"
                },
                "expression": {
                    "title": "Expression",
                    "type": "string"
                }
            },
            "required": [
                "object_name",
                "data_path",
                "index",
                "expression"
            ],
            "title": "object_driver_addArguments",
            "type": "object"
        }
    },
    {
        "name": "object_driver_list",
        "description": "\n"
        "List all drivers attached to a scene object.\n"
        "\n"
        "Returns a ``drivers`` list sorted by ``data_path`` then ``index``.\n"
        "Each entry contains:\n"
        "\n"
        "- ``data_path``   \u2014 the driven property (e.g. ``\"location\"``)\n"
        "- ``index``       \u2014 array component (0/1/2 for X/Y/Z, -1 for scalar)\n"
        "- ``driver_type`` \u2014 ``\"SCRIPTED\"`` for expression drivers,\n"
        "  ``\"AVERAGE\"`` / ``\"SUM\"`` / ``\"MIN\"`` / ``\"MAX\"`` for\n"
        "  variable-based drivers\n"
        "- ``expression``  \u2014 the formula string (non-empty for\n"
        "  ``\"SCRIPTED\"`` type only)\n"
        "- ``is_valid``    \u2014 ``false`` if Blender flagged the driver as\n"
        "  invalid (e.g. syntax error in expression)\n"
        "\n"
        "If the object has no drivers, ``drivers`` is an empty list.\n"
        "\n"
        "Use ``object_driver_add`` to add or update drivers.\n",
        "inputSchema": {
            "properties": {
                "object_name": {
                    "title": "Object Name",
                    "type": "string"
                }
            },
            "required": [
                "object_name"
            ],
            "title": "object_driver_listArguments",
            "type": "object"
        }
    },
    {
        "name": "object_fcurve_list",
        "description": "\n"
        "Read F-Curve keyframe data for a transform property of a scene object.\n"
        "\n"
        "``data_path`` selects the channel to query:\n"
        "\n"
        "- ``\"location\"``       \u2014 XYZ world-space position\n"
        "- ``\"rotation_euler\"`` \u2014 XYZ Euler rotation in radians\n"
        "- ``\"scale\"``          \u2014 XYZ scale factors\n"
        "\n"
        "Returns a ``curves`` list with one entry per axis (``array_index``\n"
        "0/1/2 for X/Y/Z). Each entry contains a sorted ``keyframes`` list\n"
        "of ``{\"frame\", \"value\", \"interpolation\"}`` dicts.\n"
        "\n"
        "If the object has no animation data or no keyframes for the\n"
        "requested path, ``curves`` is an empty list (not an error).\n"
        "\n"
        "Use ``object_keyframe_insert`` to add keyframes.\n",
        "inputSchema": {
            "properties": {
                "object_name": {
                    "title": "Object Name",
                    "type": "string"
                },
                "data_path": {
                    "title": "Data Path",
                    "type": "string"
                }
            },
            "required": [
                "object_name",
                "data_path"
            ],
            "title": "object_fcurve_listArguments",
            "type": "object"
        }
    },
    {
        "name": "object_keyframe_insert",
        "description": "\n"
        "Insert transform keyframes on a scene object at the given frame.\n"
        "\n"
        "At least one of ``location``, ``rotation``, or ``scale`` must be\n"
        "provided.\n"
        "\n"
        "- ``location``  \u2014 ``[x, y, z]`` in world space\n"
        "- ``rotation``  \u2014 ``[x, y, z]`` Euler angles in **radians**\n"
        "  (uses the object's ``rotation_euler`` channel)\n"
        "- ``scale``     \u2014 ``[x, y, z]`` scale factors (1.0 = unchanged)\n"
        "- ``interpolation`` \u2014 keyframe interpolation mode for the new\n"
        "  keyframe points: ``\"BEZIER\"`` (default), ``\"LINEAR\"``,\n"
        "  or ``\"CONSTANT\"``\n"
        "\n"
        "Only the properties explicitly provided receive a keyframe; others\n"
        "are left untouched. The returned ``inserted`` list names which\n"
        "data-paths were keyed (e.g. ``[\"location\", \"rotation_euler\"]``).\n"
        "\n"
        "Use ``object_fcurve_list`` to verify the written keyframes.\n",
        "inputSchema": {
            "properties": {
                "object_name": {
                    "title": "Object Name",
                    "type": "string"
                },
                "frame": {
                    "title": "Frame",
                    "type": "integer"
                },
                "location": {
                    "anyOf": [
                        {
                            "items": {
                                "type": "number"
                            },
                            "type": "array"
                        },
                        {
                            "type": "null"
                        }
                    ],
                    "default": None,
                    "title": "Location"
                },
                "rotation": {
                    "anyOf": [
                        {
                            "items": {
                                "type": "number"
                            },
                            "type": "array"
                        },
                        {
                            "type": "null"
                        }
                    ],
                    "default": None,
                    "title": "Rotation"
                },
                "scale": {
                    "anyOf": [
                        {
                            "items": {
                                "type": "number"
                            },
                            "type": "array"
                        },
                        {
                            "type": "null"
                        }
                    ],
                    "default": None,
                    "title": "Scale"
                },
                "interpolation": {
                    "default": "BEZIER",
                    "title": "Interpolation",
                    "type": "string"
                }
            },
            "required": [
                "object_name",
                "frame"
            ],
            "title": "object_keyframe_insertArguments",
            "type": "object"
        }
    },
    {
        "name": "object_material_assign",
        "description": "\n"
        "Assign an existing material to a scene object's material slot.\n"
        "\n"
        "``material_name`` must already exist in ``bpy.data.materials``.\n"
        "Use ``material_list`` to find available materials.\n"
        "\n"
        "``slot_index`` controls which slot receives the material:\n"
        "\n"
        "- ``-1`` (default) \u2014 append a new slot and assign the material there.\n"
        "- ``0, 1, \u2026``      \u2014 overwrite the material at that slot index.\n"
        "\n"
        "Returns ``slot_index`` (the final slot index used), ``action``\n"
        "(``\"appended\"`` or ``\"assigned\"``), and ``total_slots`` after the\n"
        "operation.\n"
        "\n"
        "Use ``object_material_list`` to verify the result.\n",
        "inputSchema": {
            "properties": {
                "object_name": {
                    "title": "Object Name",
                    "type": "string"
                },
                "material_name": {
                    "title": "Material Name",
                    "type": "string"
                },
                "slot_index": {
                    "default": -1,
                    "title": "Slot Index",
                    "type": "integer"
                }
            },
            "required": [
                "object_name",
                "material_name"
            ],
            "title": "object_material_assignArguments",
            "type": "object"
        }
    },
    {
        "name": "object_material_list",
        "description": "\n"
        "Return the material slots of a scene object.\n"
        "\n"
        "Each entry in ``slots`` contains:\n"
        "\n"
        "- ``index``           \u2014 slot index (0-based)\n"
        "- ``material_name``   \u2014 material name, or ``null`` if the slot is empty\n"
        "- ``is_active``       \u2014 True for the currently active slot\n"
        "\n"
        "``active_material_index`` is the index of the active slot.\n"
        "\n"
        "Use ``material_list`` to see all available materials in the scene.\n"
        "Use ``object_material_assign`` (REQ-15) to assign a material to a slot.\n",
        "inputSchema": {
            "properties": {
                "object_name": {
                    "title": "Object Name",
                    "type": "string"
                }
            },
            "required": [
                "object_name"
            ],
            "title": "object_material_listArguments",
            "type": "object"
        }
    },
    {
        "name": "object_modifier_add",
        "description": "\n"
        "Add a modifier to a scene object and optionally configure its parameters.\n"
        "\n"
        "``modifier_type`` is the Blender modifier type string (uppercase).\n"
        "Common values:\n"
        "\n"
        "- ``\"SUBSURF\"``   \u2014 Subdivision Surface (params: ``levels``,\n"
        "  ``render_levels``, ``subdivision_type``)\n"
        "- ``\"WAVE\"``      \u2014 Wave deform (params: ``height``, ``width``,\n"
        "  ``speed``, ``use_x``, ``use_y``)\n"
        "- ``\"SOLIDIFY\"``  \u2014 Solidify (params: ``thickness``, ``offset``)\n"
        "- ``\"BEVEL\"``     \u2014 Bevel (params: ``width``, ``segments``)\n"
        "- ``\"ARRAY\"``     \u2014 Array (params: ``count``, ``relative_offset_displace``)\n"
        "- ``\"MIRROR\"``    \u2014 Mirror (params: ``use_axis``)\n"
        "- ``\"DECIMATE\"``  \u2014 Decimate (params: ``ratio``)\n"
        "\n"
        "``name`` sets the modifier's display name. Defaults to a\n"
        "capitalised form of ``modifier_type``.\n"
        "\n"
        "``params`` is a dict of modifier-specific attribute names and\n"
        "values (e.g. ``{\"levels\": 2}``). Unknown or read-only keys are\n"
        "silently skipped and reported in ``failed_params``.\n"
        "\n"
        "Use ``object_modifiers_list`` to inspect the modifier after creation.\n"
        "Use ``get_object_detail_summary`` to confirm the modifier appears\n"
        "in the object's modifier stack.\n",
        "inputSchema": {
            "properties": {
                "object_name": {
                    "title": "Object Name",
                    "type": "string"
                },
                "modifier_type": {
                    "title": "Modifier Type",
                    "type": "string"
                },
                "name": {
                    "default": "",
                    "title": "Name",
                    "type": "string"
                },
                "params": {
                    "anyOf": [
                        {
                            "additionalProperties": True,
                            "type": "object"
                        },
                        {
                            "type": "null"
                        }
                    ],
                    "default": None,
                    "title": "Params"
                }
            },
            "required": [
                "object_name",
                "modifier_type"
            ],
            "title": "object_modifier_addArguments",
            "type": "object"
        }
    },
    {
        "name": "object_modifiers_list",
        "description": "\n"
        "List all modifiers on a scene object together with their parameters.\n"
        "\n"
        "Returns a ``modifiers`` list. Each entry contains:\n"
        "\n"
        "- ``name``          \u2014 modifier display name\n"
        "- ``type``          \u2014 modifier type string (e.g. ``\"SUBSURF\"``)\n"
        "- ``show_viewport`` \u2014 whether the modifier is visible in the viewport\n"
        "- ``show_render``   \u2014 whether the modifier is applied at render time\n"
        "- ``params``        \u2014 dict of the modifier's current attribute values\n"
        "  (booleans, integers, floats, strings, and enums only)\n"
        "\n"
        "If the object has no modifiers, ``modifiers`` is an empty list.\n"
        "\n"
        "Use ``object_modifier_add`` to add modifiers to the object.\n"
        "Use ``get_object_detail_summary`` for a higher-level overview.\n",
        "inputSchema": {
            "properties": {
                "object_name": {
                    "title": "Object Name",
                    "type": "string"
                }
            },
            "required": [
                "object_name"
            ],
            "title": "object_modifiers_listArguments",
            "type": "object"
        }
    },
    {
        "name": "ping",
        "description": "\n"
        "Verify that Blender is online and return its version string.\n"
        "\n"
        "Call this before other tools to confirm the Blender addon is running.\n"
        "Returns an error if the connection to Blender cannot be established.\n",
        "inputSchema": {
            "properties": {},
            "title": "pingArguments",
            "type": "object"
        }
    },
    {
        "name": "render_animation",
        "description": "\n"
        "Render a frame sequence and write a video file (H.264 / MPEG-4).\n"
        "\n"
        "``output_path`` sets the destination.  Absolute paths are used\n"
        "as-is; relative paths are placed inside Blender's temp directory.\n"
        "The file extension should be ``.mp4``.\n"
        "\n"
        "Optional overrides (all default to current scene settings):\n"
        "\n"
        "- ``frame_start`` / ``frame_end``: inclusive frame range to render.\n"
        "  Both default to ``scene.frame_start`` / ``scene.frame_end``.\n"
        "- ``width`` / ``height``: render resolution in pixels.\n"
        "  Internally sets ``resolution_percentage = 100``.\n"
        "- ``fps``: frames-per-second.  Overrides ``scene.render.fps`` and\n"
        "  sets ``fps_base`` to 1.\n"
        "\n"
        "Video encoding uses H.264 in an MPEG-4 container with no audio.\n"
        "On Blender 5.1+, ``image_settings.media_type = 'VIDEO'`` is used;\n"
        "older builds fall back to ``file_format = 'FFMPEG'``.\n"
        "All settings are restored after the render.\n"
        "\n"
        "Returns ``filepath``, ``frame_start``, ``frame_end``, ``width``,\n"
        "``height``, and ``fps`` in the success result.\n",
        "inputSchema": {
            "properties": {
                "output_path": {
                    "title": "Output Path",
                    "type": "string"
                },
                "frame_start": {
                    "anyOf": [
                        {
                            "type": "integer"
                        },
                        {
                            "type": "null"
                        }
                    ],
                    "default": None,
                    "title": "Frame Start"
                },
                "frame_end": {
                    "anyOf": [
                        {
                            "type": "integer"
                        },
                        {
                            "type": "null"
                        }
                    ],
                    "default": None,
                    "title": "Frame End"
                },
                "width": {
                    "anyOf": [
                        {
                            "type": "integer"
                        },
                        {
                            "type": "null"
                        }
                    ],
                    "default": None,
                    "title": "Width"
                },
                "height": {
                    "anyOf": [
                        {
                            "type": "integer"
                        },
                        {
                            "type": "null"
                        }
                    ],
                    "default": None,
                    "title": "Height"
                },
                "fps": {
                    "anyOf": [
                        {
                            "type": "integer"
                        },
                        {
                            "type": "null"
                        }
                    ],
                    "default": None,
                    "title": "Fps"
                }
            },
            "required": [
                "output_path"
            ],
            "title": "render_animationArguments",
            "type": "object"
        }
    },
    {
        "name": "render_frame",
        "description": "\n"
        "Render a single frame of the current scene to an image file.\n"
        "\n"
        "``output_path`` sets the destination. Absolute paths are used\n"
        "as-is; relative paths are placed inside Blender's temp directory.\n"
        "\n"
        "Optional overrides (all default to the current scene settings):\n"
        "\n"
        "- ``frame``: scene frame number to render (``None`` = current frame).\n"
        "- ``width`` / ``height``: render resolution in pixels; both default\n"
        "  to the scene resolution.  If only one is provided the other keeps\n"
        "  the scene value.  Set ``resolution_percentage`` to 100 internally\n"
        "  so the values are exact.\n"
        "- ``fps``: frames-per-second; overrides ``scene.render.fps`` and\n"
        "  sets ``fps_base`` to 1.\n"
        "\n"
        "All overrides are temporary and are restored after the render.\n"
        "\n"
        "Returns ``filepath``, ``frame``, ``width``, ``height``, and ``fps``\n"
        "in the success result.  Returns an error if Blender's render\n"
        "operator raises a ``RuntimeError``.\n",
        "inputSchema": {
            "properties": {
                "output_path": {
                    "title": "Output Path",
                    "type": "string"
                },
                "frame": {
                    "anyOf": [
                        {
                            "type": "integer"
                        },
                        {
                            "type": "null"
                        }
                    ],
                    "default": None,
                    "title": "Frame"
                },
                "width": {
                    "anyOf": [
                        {
                            "type": "integer"
                        },
                        {
                            "type": "null"
                        }
                    ],
                    "default": None,
                    "title": "Width"
                },
                "height": {
                    "anyOf": [
                        {
                            "type": "integer"
                        },
                        {
                            "type": "null"
                        }
                    ],
                    "default": None,
                    "title": "Height"
                },
                "fps": {
                    "anyOf": [
                        {
                            "type": "integer"
                        },
                        {
                            "type": "null"
                        }
                    ],
                    "default": None,
                    "title": "Fps"
                }
            },
            "required": [
                "output_path"
            ],
            "title": "render_frameArguments",
            "type": "object"
        }
    },
    {
        "name": "render_thumbnail_to_path",
        "description": "\n"
        "Render a small, low-quality thumbnail to *output_path* (temporarily overrides settings).\n",
        "inputSchema": {
            "properties": {
                "output_path": {
                    "title": "Output Path",
                    "type": "string"
                }
            },
            "required": [
                "output_path"
            ],
            "title": "render_thumbnail_to_pathArguments",
            "type": "object"
        }
    },
    {
        "name": "render_viewport_to_path",
        "description": "\n"
        "Render the current scene to *output_path* using current render settings.\n",
        "inputSchema": {
            "properties": {
                "output_path": {
                    "title": "Output Path",
                    "type": "string"
                }
            },
            "required": [
                "output_path"
            ],
            "title": "render_viewport_to_pathArguments",
            "type": "object"
        }
    },
    {
        "name": "search_api_docs",
        "description": "\n"
        "Full-text search over the bundled Blender Python API reference.\n"
        "\n"
        "Returns a ranked list of hits. Each hit has:\n"
        "\n"
        "- ``path``: file path relative to the bundled docs.\n"
        "- ``text``: the matching paragraph plus ``context``\n"
        "  paragraphs on either side.\n"
        "- ``breadcrumb``: the section path containing the hit\n"
        "  (``Section > Sub-section > ...``).\n"
        "- ``index``: the hit's position in the result list.\n"
        "- ``score``: a relevance score; higher is better.\n"
        "\n"
        "The query is tokenised on whitespace and matched\n"
        "case-insensitively. Every token must appear somewhere in\n"
        "the paragraph body, the file path, or an enclosing section\n"
        "title - in any order. Common English stop-words (``the``,\n"
        "``a``, ``how``, ``to``, ...) are dropped, so natural\n"
        "phrasings like ``\"how to bake\"`` work as expected. Regular\n"
        "expressions are not supported.\n"
        "\n"
        "Use ``context`` to pull more surrounding paragraphs into\n"
        "each hit (symmetric, default 0). Use ``index`` with the\n"
        "position of a previous hit (same query) to get that hit\n"
        "alone with its text widened to its enclosing section.\n"
        "\n"
        "Read-only; consults bundled RST files only.\n",
        "inputSchema": {
            "properties": {
                "query": {
                    "title": "Query",
                    "type": "string"
                },
                "max_results": {
                    "default": 20,
                    "title": "Max Results",
                    "type": "integer"
                },
                "context": {
                    "default": 0,
                    "title": "Context",
                    "type": "integer"
                },
                "index": {
                    "anyOf": [
                        {
                            "type": "integer"
                        },
                        {
                            "type": "null"
                        }
                    ],
                    "default": None,
                    "title": "Index"
                }
            },
            "required": [
                "query"
            ],
            "title": "search_api_docsArguments",
            "type": "object"
        }
    },
    {
        "name": "search_manual_docs",
        "description": "\n"
        "Full-text search over the bundled Blender user manual.\n"
        "\n"
        "Returns a ranked list of hits. Each hit has:\n"
        "\n"
        "- ``path``: file path relative to the bundled docs.\n"
        "- ``text``: the matching paragraph plus ``context``\n"
        "  paragraphs on either side.\n"
        "- ``breadcrumb``: the section path containing the hit\n"
        "  (``Section > Sub-section > ...``).\n"
        "- ``index``: the hit's position in the result list.\n"
        "- ``score``: a relevance score; higher is better.\n"
        "\n"
        "The query is tokenised on whitespace and matched\n"
        "case-insensitively. Every token must appear somewhere in\n"
        "the paragraph body, the file path, or an enclosing section\n"
        "title - in any order. Common English stop-words (``the``,\n"
        "``a``, ``how``, ``to``, ...) are dropped, so natural\n"
        "phrasings like ``\"how to bake\"`` work as expected. Regular\n"
        "expressions are not supported.\n"
        "\n"
        "Use ``context`` to pull more surrounding paragraphs into\n"
        "each hit (symmetric, default 0). Use ``index`` with the\n"
        "position of a previous hit (same query) to get that hit\n"
        "alone with its text widened to its enclosing section.\n"
        "\n"
        "Read-only; consults bundled RST files only.\n",
        "inputSchema": {
            "properties": {
                "query": {
                    "title": "Query",
                    "type": "string"
                },
                "max_results": {
                    "default": 20,
                    "title": "Max Results",
                    "type": "integer"
                },
                "context": {
                    "default": 0,
                    "title": "Context",
                    "type": "integer"
                },
                "index": {
                    "anyOf": [
                        {
                            "type": "integer"
                        },
                        {
                            "type": "null"
                        }
                    ],
                    "default": None,
                    "title": "Index"
                }
            },
            "required": [
                "query"
            ],
            "title": "search_manual_docsArguments",
            "type": "object"
        }
    }
]
# END: EXPECTED_TOOLS


def _list_tools() -> list[dict[str, object]]:
    """
    Starts the MCP server and returns the full tool listing.
    """

    # Async is required because the MCP client SDK is async-only.
    async def _run() -> list[dict[str, object]]:
        env = os.environ.copy()
        env["PYTHONPATH"] = os.path.join(_REPO_DIR, "mcp")
        params = StdioServerParameters(
            command=sys.executable,
            args=["-m", "blmcp"],
            env=env,
        )
        async with stdio_client(params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                result = await session.list_tools()
                return [
                    {
                        "name": t.name,
                        "description": t.description,
                        "inputSchema": t.inputSchema,
                    }
                    for t in result.tools
                ]

    return asyncio.run(_run())


class TestToolListing(unittest.TestCase):
    """
    Checks that the live tool listing matches the frozen snapshot.
    """

    _tools: list[dict[str, object]]

    @classmethod
    def setUpClass(cls) -> None:
        cls._tools = _list_tools()

    def test_tools_match_expected(self) -> None:
        """
        Checks that the live tool listing exactly matches ``EXPECTED_TOOLS``.
        """
        self.assertEqual(self._tools, EXPECTED_TOOLS)


def _update_expected_tools() -> None:
    """
    Re-generates the ``EXPECTED_TOOLS`` block from a live server query.
    """
    import json
    import subprocess

    filepath = os.path.abspath(__file__)
    with open(filepath, "r", encoding="utf-8") as fh:
        source = fh.read()
    begin = source.index("# BEGIN: EXPECTED_TOOLS\n") + len("# BEGIN: EXPECTED_TOOLS\n")
    end = source.index("# END: EXPECTED_TOOLS\n")
    formatted = json.dumps(_list_tools(), indent=4)
    formatted = (
        formatted.replace(": true", ": True")
        .replace(": false", ": False")
        .replace(": null", ": None")
    )
    formatted = formatted.replace("\\n", '\\n"\n"')
    # Also handles the `\n"` case (no trailing empty string).
    formatted = formatted.replace('\\n"\n""', '\\n"')
    formatted = "EXPECTED_TOOLS = " + formatted + "\n"
    with open(filepath, "w", encoding="utf-8") as fh:
        fh.write(source[:begin] + formatted + source[end:])
    subprocess.check_call(["autopep8", "--in-place", filepath])


if __name__ == "__main__":
    if "--update" in sys.argv:
        sys.argv.remove("--update")
        _update_expected_tools()
    else:
        unittest.main()
