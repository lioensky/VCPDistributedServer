.. _objects-types:

************
Object Types
************

.. reference::

   :Mode:      Object Mode
   :Menu:      :menuselection:`Add`
   :Shortcut:  :kbd:`Shift-A`

New objects can be created with the *Add* menu in the 3D Viewport's header.

:doc:`Mesh </modeling/meshes/introduction>`
   Objects composed of vertices, edges and polygonal faces
   and can be edited extensively with Blender's mesh editing tools.
   See :doc:`Mesh Primitives </modeling/meshes/primitives>`.
:doc:`Curve </modeling/curves/introduction>`
   Mathematically defined objects which can be manipulated with control handles
   or control points (instead of vertices), to edit their length and curvature.
   See :doc:`Curves Primitives </modeling/curves/primitives>`.
:doc:`Surface </modeling/surfaces/introduction>`
   Mathematically defined patches that are manipulated with control points.
   These are useful for simple rounded forms and organic landscapes.
   See :doc:`Surfaces Primitives </modeling/surfaces/primitives>`.
:doc:`Metaball </modeling/metas/introduction>`
   Objects formed by a mathematical function (with no vertices or control points)
   defining the 3D volume in which the object exists. Meta objects have a liquid-like quality
   where when two or more metaballs are brought together,
   they merge by smoothly rounding out the connection, appearing as one unified object.
   See :doc:`Meta Primitives </modeling/metas/primitives>`.
:doc:`Text </modeling/texts/introduction>`
   Create a two-dimensional representation of a text.
:doc:`Volume </modeling/volumes/introduction>`
   Container for OpenVDB files that is generated
   by other software or Blender's :doc:`Fluid Simulator </physics/fluid/index>`.
:doc:`Grease Pencil </grease_pencil/introduction>`
   Objects created by drawing strokes.
   See :doc:`Grease Pencil Primitives </grease_pencil/primitives>`

:doc:`Armature </animation/armatures/index>`
   Used for rigging 3D models to make them pose-able and animatable.
:doc:`Lattice </animation/lattice>`
   Non-renderable wireframes commonly used for the deformation of other objects
   with help of the :doc:`Lattice Modifier </modeling/modifiers/deform/lattice>`.

:doc:`Empty </modeling/empties>`
   Null objects that are simple visual transform nodes that do not render.
   They are useful for controlling the position or movement of other objects.
:ref:`Image <bpy.types.Object.empty_image>`
   Empty objects that display images in the 3D Viewport.
   These images can be used to aid artists in modeling or animating.

   Image Plane
      Adds a :ref:`mesh plane <bpy.ops.mesh.primitive_plane_add>` with materials and texture from an image file.
      The dimensions of the plane are calculated to match the aspect of the image file.

:doc:`Light </render/lights/light_object>`
   Empty objects that emit light and are used for lighting the scene in renders.
:doc:`Light Probe </render/eevee/light_probes/index>`
   Used by the EEVEE render engine to record lighting information for indirect lighting.

:doc:`Camera </render/cameras>`
   This is the virtual camera that is used to determine what appears in the render.

:doc:`Speaker </render/output/audio/speaker>`
   Empty objects that bring a source of sound to the scene.

:doc:`Force Field </physics/forces/force_fields/index>`
   Empty objects that give simulations external forces, creating movement,
   and are represented in the 3D Viewport as small control objects.

:doc:`Collection Instance </scene_layout/object/properties/instancing/collection>`
   Lets you select from a list of existing collections. Once selected, an empty object will be created,
   with an instance of the selected collection (collection instancing active).


.. _object-common-options:

Common Options
==============

You can change the options of the object in the :ref:`bpy.ops.screen.redo_last` panel
just after creating it:

Type
   You can change the type of some objects after their creation with a selector.
Radius/Size
   Sets the starting size.
Align
   Rotates the new object so that it is aligned in one of the following manners:

   :World:
      Aligns the object to the global space axes, i.e. the object's front faces the negative Y axis (default).
   :View:
      Aligns the object to the view space axes, i.e. the object's front faces the viewport's point of view.
   :3D Cursor:
      Aligns the object to match the rotation of the :doc:`3D Cursor </editors/3dview/3d_cursor>`.
Location
   Objects are placed, by default, at the position of the 3D Cursor.
   These values let you place the object in an other position.
Rotation
   Values let you rotate the object so that default rotation is overridden.
