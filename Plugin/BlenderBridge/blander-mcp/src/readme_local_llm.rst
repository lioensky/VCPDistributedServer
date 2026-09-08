#########
Local LLM
#########

Prerequisites
=============

- This repository.
- `LLAMA.cpp <https://github.com/ggml-org/llama.cpp>`__ (version 8218 or newer).
- Blender 5.1.


Components
==========

Before going into details, here are the components which will need to run
with a brief explanation of what they do.

``llama.cpp`` (external project)
   Runs the LLM model.

``chat_client``: ``./chat_client/chat_client.py``
   A simple text mode chat client that connects ``llama.cpp`` to ``blender_mcp``.

``blender_mcp``: ``./mcp/``
   The MCP server that provides tools and connects the ``chat_client`` to ``blender_mcp_addon``.

``blender_mcp_addon``: ``./addon/``
   The Blender MCP add-on which connects Blender to the ``blender_mcp`` server.

``blender``: (external project)
   An instance of Blender running ``blender_mcp_addon``,
   this can run in background or with a GUI.

   For the purpose of this document, we assume a graphical session.


Setup
=====

Using ``virtualenv`` is optional but assumed in the instructions below.

Create & Activate a Virtual Environment:
   .. code-block::

      virtualenv .venv -p python
      source .venv/bin/activate

Install Requirements & Blender MCP:
   .. code-block::

      pip install -r mcp/requirements.txt
      pip install -e mcp

   Check that ``blender-mcp`` runs (it will do nothing, press Ctrl-C to exit).

Build the Blender Extension:
   .. code-block::

      blender -c extension build --source-dir ./addon/blender_mcp_addon
      blender -c extension install-file blender_mcp_addon-0.1.0.zip --repo=user_default

Download a Model via LLAMA.cpp:
   .. code-block::

      # This will download AND run the model, running afterwards will use the cache.

      # These are just examples.
      export HF_REPO="HeYujie/Qwen3.5-35B-A3B-abliterated-GGUF"
      export HF_FILE="Qwen3.5-35B-A3B-abliterated-Q8_0.gguf"

      llama-server --jinja --hf-repo $HF_REPO --hf-file $HF_FILE

   You can visit ``http://127.0.0.1:8080/`` to check this is working.


Usage
=====

There are two ways you can interact with the chat:
text mode client & the LLAMA.CPP web UI.

The web UI currently gives a much nicer experience with feedback while it's processing.
The text client is mainly useful for tests.


Text Mode Client
----------------

Ensure the ``llama-server`` is running:
   .. code-block::

      llama-server --jinja --hf-repo $HF_REPO --hf-file $HF_FILE

Run the chat client:
   Activate the virtual-environment (if you haven't already).

   .. code-block::

      python chat_client/chat_client.py openai --api-url http://localhost:8080

   Note that this will start ``blender-mcp``.

Run Blender:
   Ensure "Online Access" is enabled.

   In the Add-on preferences, check the "MCP Bridge Server" is running,
   if not - start it.


LLAMA.CPP Web UI
----------------

Ensure the ``llama-server`` is running:
   .. code-block::

      llama-server --jinja --hf-repo $HF_REPO --hf-file $HF_FILE

Run ``blender-mcp`` with HTTP enabled:
   Activate the virtual-environment (if you haven't already).

   .. code-block::

      blender-mcp --transport http --port 9191

Connect LLAMA.CPP to ``blender-mcp``:
   - Open ``http://127.0.0.1:8080/`` in a web browser - you should see a chat prompt.
   - Click on the "Cog" icon at the top right.
   - Click on the "MCP" section in the settings.
   - Click on the "Add New Server" button.
   - Enter ``http://127.0.0.1:9191/`` for the "Server URL".
   - Click on "Update", you should see server instructions, tools ... etc.
   - Enable the MCP server (a switch at the top right).

     NOTE: for each new chat, you will need to enable ``blender-mcp`` from the web UI.

Run Blender:
   Ensure "Online Access" is enabled.

   In the Add-on preferences, check the "MCP Bridge Server" is running,
   if not - start it.
