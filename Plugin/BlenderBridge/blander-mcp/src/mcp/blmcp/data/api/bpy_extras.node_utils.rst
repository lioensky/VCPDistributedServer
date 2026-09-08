bpy_extras submodule (bpy_extras.node_utils)
============================================

.. module:: bpy_extras.node_utils

.. function:: connect_sockets(input, output)

   Connect sockets in a node tree.
   
   This is useful because the links created through the normal Python API are
   invalid when one of the sockets is a virtual socket (grayed out sockets in
   Group Input and Group Output nodes).
   
   It replaces node_tree.links.new(input, output)
   
   :param input: The input socket.
   :type input: :class:`bpy.types.NodeSocket`
   :param output: The output socket.
   :type output: :class:`bpy.types.NodeSocket`

.. function:: find_base_socket_type(socket)

   Find the base class of the socket.
   
   Sockets can have a subtype such as NodeSocketFloatFactor,
   but only the base type is allowed, e.g. NodeSocketFloat
   
   :param socket: The socket to find the base type for.
   :type socket: :class:`bpy.types.NodeSocket`
   :return: The base socket type identifier.
   :rtype: str

.. function:: find_node_input(node, name)

   Find a node input socket by name.
   
   Note that names are not unique, returns the first match.
   
   :param node: The node to search.
   :type node: :class:`bpy.types.Node`
   :param name: The name of the input socket.
   :type name: str
   :return: The input socket or None if not found.
   :rtype: :class:`bpy.types.NodeSocket` | None

