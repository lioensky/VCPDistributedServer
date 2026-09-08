
*********************
Open Shading Language
*********************

`Open Shading Language (OSL) <https://github.com/AcademySoftwareFoundation/OpenShadingLanguage>`__
is a programmable shading system developed for advanced rendering engines.
It allows technical artists and developers to write custom shader code using a C-like scripting language.

In Blender, OSL can be used within Cycles to define custom surface, volume, and displacement shaders.
This gives users full control over shading behavior, enabling procedural effects, advanced lighting models,
and custom geometry-based material logic that may not be possible with built-in shader nodes alone.

Unlike node-based materials, OSL shaders are authored as text scripts using Blender's internal
:doc:`Text Editor </editors/text_editor>` or loaded from external `.osl` or `.oso` files.
These scripts are then compiled and used in the Shader Editor
through the :doc:`Script Node </render/shader_nodes/utilities/script>`.

.. tip::

   OSL is especially useful for generating procedural textures, custom BRDFs, or implementing research prototypes.
   It also allows sharing shaders across compatible rendering applications that support the OSL standard.


.. _osl-usage:

Usage
=====

To use Open Shading Language (OSL) in Blender, follow these steps:

#. **Enable OSL Rendering**

   In the :menuselection:`Render Properties` enable
   :ref:`Open Shading Language <bpy.types.CyclesRenderSettings.shading_system>`.

#. **Add a Script Node**

   In the Shader Editor add :doc:`Script Node </render/shader_nodes/utilities/script>` then in the node's properties:

   - Set the *Mode* to *Internal* to use a Blender text data-block, or
   - Set it to *External* to load a shader file from disk (either `.osl` or compiled `.oso`).

   For the internal mode, create a new text data-block in the Text Editor,
   then write or paste your OSL code there.

   Blender will compile the OSL source file automatically.
   If the source is `.osl`, it will be compiled into `.oso` bytecode.
   Compilation errors will be shown in the system console.

#. **Use Shader Outputs**

   Once compiled, the node's outputs will reflect the ``output`` parameters defined in the OSL code.
   These outputs can be connected to any part of the material node tree.


Writing Shaders
===============

For more details on how to write shaders, see the
`OSL Documentation <https://open-shading-language.readthedocs.io/en/latest/>`__.

Here is a simple example:

.. code-block:: cpp

   shader simple_material(
       color Diffuse_Color = color(0.6, 0.8, 0.6),
       float Noise_Factor = 0.5,
       output closure color BSDF = diffuse(N))
   {
       color material_color = Diffuse_Color * mix(1.0, noise(P * 10.0), Noise_Factor);
       BSDF = material_color * diffuse(N);
   }


Closures
========

OSL is different from, for example, RSL or GLSL, in that it does not have a light loop.
There is no access to lights in the scene,
and the material must be built from closures that are implemented in the renderer itself.
This is more limited, but also makes it possible for the renderer to do optimizations and
ensure all shaders can be importance sampled.

The available closures in Cycles correspond to the shader nodes and their sockets;
for more details on what they do and the meaning of the parameters,
see the :doc:`shader nodes manual </render/shader_nodes/shader/index>`.

.. seealso::

   Documentation on OSL's `built-in closures
   <https://open-shading-language.readthedocs.io/en/latest/stdlib.html#material-closures>`__.


BSDF
----

- ``diffuse(N)``
- ``oren_nayar(N, roughness)``
- ``diffuse_ramp(N, colors[8])``
- ``phong_ramp(N, exponent, colors[8])``
- ``diffuse_toon(N, size, smooth)``
- ``glossy_toon(N, size, smooth)``
- ``translucent(N)``
- ``reflection(N)``
- ``refraction(N, ior)``
- ``transparent()``
- ``microfacet_ggx(N, roughness)``
- ``microfacet_ggx_aniso(N, T, ax, ay)``
- ``microfacet_ggx_refraction(N, roughness, ior)``
- ``microfacet_beckmann(N, roughness)``
- ``microfacet_beckmann_aniso(N, T, ax, ay)``
- ``microfacet_beckmann_refraction(N, roughness, ior)``
- ``ashikhmin_shirley(N, T, ax, ay)``
- ``ashikhmin_velvet(N, roughness)``


Hair
----

- ``hair_reflection(N, roughnessu, roughnessv, T, offset)``
- ``hair_transmission(N, roughnessu, roughnessv, T, offset)``
- ``principled_hair(N, absorption, roughness, radial_roughness, coat, offset, IOR)``


BSSRDF
------

Used to simulate subsurface scattering.

.. function:: bssrdf(method, N, radius, albedo)

   :type method: string
   :arg method:
      Rendering method to simulate subsurface scattering.

      - ``burley``:
        An approximation to physically-based volume scattering.
        This method is less accurate than ``random_walk`` however,
        in some situations this method will resolve noise faster.
      - ``random_walk_skin``:
        Provides accurate results for thin and curved objects.
        Random Walk uses true volumetric scattering inside the mesh,
        which means that it works best for closed meshes.
        Overlapping faces and holes in the mesh can cause problems.
      - ``random_walk``:
        Behaves similarly to ``random_walk_skin`` but modulates
        the *Radius* based on the *Color*, *Anisotropy*, and *IOR*.
        This method thereby attempts to retain greater surface detail and color
        than ``random_walk_skin``.
   :type N: vector
   :arg N: Normal vector of the surface point being shaded.
   :type radius: vector
   :arg radius:
      Average distance that light scatters below the surface.
      Higher radius gives a softer appearance, as light bleeds into shadows and through the object.
      The scattering distance is specified separately for the RGB channels,
      to render materials such as skin where red light scatters deeper.
      The X, Y and Z values are mapped to the R, G and B values, respectively.
   :type albedo: color
   :arg albedo:
      Color of the surface, or physically speaking, the probability that light is reflected for each wavelength.


Volume
------

- ``henyey_greenstein(g)``
- ``absorption()``


Other
-----

- ``emission()``
- ``ambient_occlusion()``
- ``holdout()``
- ``background()``


Attributes
==========

Geometry attributes can be read through the ``getattribute()`` function.
This includes UV maps, color attributes and any attributes output from geometry nodes.

The following built-in attributes are available through ``getattribute()`` as well.

``geom:generated``
   Automatically generated texture coordinates, from non-deformed mesh.
``geom:uv``
   Default render UV map.
``geom:tangent``
   Default tangent vector along surface, in object space.
``geom:undisplaced``
   Position before displacement, in object space.
``geom:dupli_generated``
   For instances, generated coordinate from instancer object.
``geom:dupli_uv``
   For instances, UV coordinate from instancer object.
``geom:trianglevertices``
   Three vertex coordinates of the triangle.
``geom:numpolyvertices``
   Number of vertices in the polygon (always returns three currently).
``geom:polyvertices``
   Vertex coordinates array of the polygon (always three vertices currently).
``geom:name``
   Name of the object.
``geom:is_smooth``
   Is mesh face smooth or flat shaded.
``geom:is_curve``
   Is object a curve or not.
``geom:curve_intercept``
   0..1 coordinate for point along the curve, from root to tip.
``geom:curve_thickness``
   Thickness of the curve in object space.
``geom:curve_length``
   Length of the curve in object space.
``geom:curve_tangent_normal``
   Tangent Normal of the strand.
``geom:is_point``
   Is point in a point cloud or not.
``geom:point_radius``
   Radius of point in point cloud.
``geom:point_position``
   Center position of point in point cloud.
``geom:point_random``
   Random number, different for every point in point cloud.
``path:ray_length``
   Ray distance since last hit.
``object:random``
   Random number, different for every object instance.
``object:index``
   Object unique instance index.
``object:location``
   Object location.
``material:index``
   Material unique index number.
``particle:index``
   Particle unique instance number.
``particle:age``
   Particle age in frames.
``particle:lifetime``
   Total lifespan of particle in frames.
``particle:location``
   Location of the particle.
``particle:size``
   Size of the particle.
``particle:velocity``
   Velocity of the particle.
``particle:angular_velocity``
   Angular velocity of the particle.


.. _render-shader-nodes-osl-trace:

Trace
=====

:guilabel:`CPU Only`

We support the ``trace(point pos, vector dir, ...)`` function,
to trace rays from the OSL shader. The "shade" parameter is not supported currently,
but attributes can be retrieved from the object that was hit using the
``getmessage("trace", ..)`` function. See the OSL specification for details on how to use this.

This function cannot be used instead of lighting;
the main purpose is to allow shaders to "probe" nearby geometry,
for example to apply a projected texture that can be blocked by geometry,
apply more "wear" to exposed geometry, or make other ambient occlusion-like effects.


Metadata
========

Metadata on parameters controls how they are displayed in the user interface.
The following metadata entries are supported:

``[[ string label = "My Label" ]]``
   Custom display name of the parameter in the user interface.

``[[ string widget = "null" ]]``
   Hides the parameter from the user interface.

``[[ string widget = "boolean" ]]`` or ``[[ string widget = "checkbox" ]]``
   Displays an integer parameter as a boolean checkbox.

``[[ string widget = "filename" ]]``
   Displays the parameter as a file path selector.

``[[ string widget = "mapper", string options = "left:0|right:1" ]]``
   Displays an integer parameter as an enumerated menu.
   The *options* string defines a list of label-value pairs separated by ``|``.

``[[ string vecsemantics = "POINT" ]]``
   Marks a vector parameter as a translation input (position vector).

``[[ string vecsemantics = "NORMAL" ]]``
   Marks a vector parameter as a normal input (direction vector).

``[[ string unit = "radians" ]]``
   Marks a float parameter as an angle input, displayed in radians.

``[[ string unit = "m" ]]``
   Marks a float parameter as a distance input, displayed in meters.

``[[ string unit = "mm" ]]``
   Marks a float parameter as a distance input, displayed in millimeters.

``[[ string unit = "s" ]]`` or ``[[ string unit = "sec" ]]``
   Marks a float parameter as a time input, displayed in seconds.


Limitations
===========

.. important::

   OSL is not supported with GPU rendering unless using the OptiX backend.

Some OSL features are not available when using the OptiX backend. Examples include:

- Memory usage reductions offered by features like on-demand texture loading and
   mip-mapping are not available.
- Texture lookups require OSL to be able to determine a constant image file path for each
   texture call.
- Some noise functions are not available. Examples include *Cell*, *Simplex*, and *Gabor*.
- The :ref:`trace <render-shader-nodes-osl-trace>` function is not functional.
  As a result of this, the :ref:`Ambient Occlusion <bpy.types.ShaderNodeAmbientOcclusion>`
  and :ref:`Bevel <bpy.types.ShaderNodeBevel>` nodes do not work.
