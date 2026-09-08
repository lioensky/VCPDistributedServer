.. _bpy.types.ShaderNodeScript:

***********
Script Node
***********

:guilabel:`Cycles Only`

.. figure:: /images/node-types_ShaderNodeScript.webp
   :align: right
   :alt: Script Node.

The *Script Node* allows you to load and use custom shaders written in
:doc:`Open Shading Language (OSL) </render/cycles/osl/index>` within the Cycles renderer.
This node acts as a bridge between OSL shader code and the node-based material system in Blender.

Each Script node represents a single OSL shader, with its inputs
and outputs defined by the parameters in the shader script.
These shaders can be stored directly within the blend-file or referenced externally.

This feature is ideal for technical artists and shader developers
who need fine-grained control over shading behavior beyond what the standard shader nodes provide.

.. note::

   The Script node is only evaluated if
   :ref:`Open Shading Language <bpy.types.CyclesRenderSettings.shading_system>` is enabled.

.. tip::

   For use in production, we suggest to use a node group to wrap shader script nodes,
   and link that into other blend-files.
   This makes it easier to make changes to the node afterwards as sockets are added or removed,
   without having to update the script nodes in all files.


Properties
==========

Mode
   How to link to OSL shaders.

   :Internal:
      A text data-block is used to store the OSL shader, and the OSO bytecode is stored in the node itself.
      This is useful for distributing a blend-file with everything packed into it.

      .. _bpy.ops.node.shader_script_update:

      :bl-icon:`file_refresh` Script Node Update
         Reloads the text file data-block, creating new inputs and outputs if needed.

   :External:
      Used to specify a ``.osl`` file from a drive,
      and this will then be automatically compiled into a ``.oso`` file in the same directory.
      It is also possible to specify a path to a ``.oso`` file, which will then be used directly,
      with compilation done manually by the user. The third option is to specify just the module name,
      which will be looked up in the shader search path.

      The shader search path is located in the same place as the scripts or configuration path, under:

      .. rubric:: **Linux:**
      .. parsed-literal:: $HOME/.config/blender/|BLENDER_VERSION|/shaders/
      .. rubric:: **Windows:**
      .. parsed-literal:: C:\\Users\\$user\\AppData\\Roaming\\Blender Foundation\\Blender\\\ |BLENDER_VERSION|\\shaders\\
      .. rubric:: **macOS:**
      .. parsed-literal:: /Users/$USER/Library/Application Support/Blender/|BLENDER_VERSION|/shaders/
