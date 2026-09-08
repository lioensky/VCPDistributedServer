.. _glossary:

############
  Glossary
############

.. For writing style guide, see: :doc:`/contribute/manual/guides/writing_guide`
   If you add new entries, keep the alphabetical sorting!

This page lists definitions for terms used in Blender and this manual.

.. glossary::
   :sorted:

   Active
      When many items are selected, the last selected item will be the active one.
      Used in situations where the interface only shows options for one item at a time.

      See also :ref:`selection states <object-active>`.

   :doc:`Action </animation/actions>`
      Blender's container for animation data.  In Blender, animatable :term:`data-blocks <Data-Block>` do not store
      their own animation data, but instead store their animation data an actions.

   Action Safe
      Area of the screen visible on most devices. Place content inside it to ensure it does not get cut off.

   Aliasing
      Rendering artifacts in the form of jagged lines.

   Alpha Channel
      Additional channel in an image for transparency.

      Straight Alpha
         Method where RGBA channels are stored as (R, G, B, A)
         channels, with the RGB channels unaffected by the alpha channel.
         This is the alpha type used by paint programs such as Photoshop or Gimp,
         and used in common file formats like PNG, BMP or TARGA.
         So, image textures or output for the web are usually straight alpha.

      Premultiplied Alpha
         Method where RGBA channels are stored as (R × A, G × A, B × A, A),
         with the alpha multiplied into the RGB channel.

         This is the natural output of render engines, with the RGB channels representing the amount
         of light that comes toward the viewer, and alpha representing how much of the light from
         the background is blocked. The OpenEXR file format uses this alpha type. So, intermediate files
         for rendering and compositing are often stored as premultiplied alpha.

      Conversion (Straight/Premultiplied) Alpha
         Conversion between the two alpha types is not a simple operation and can involve data loss,
         as both alpha types can represent data that the other cannot, though it is often subtle.

         Straight alpha can be considered to be an RGB color image with a separate alpha mask.
         In areas where this mask is fully transparent, there can still be colors in the RGB channels.
         On conversion to premultiplied alpha, this mask is *applied* and the colors in such areas
         become black and are lost.

         Premultiplied alpha, on the other hand, can represent renders that are both emitting light
         and letting through light from the background. For example, a transparent fire render might
         be emitting light, but also letting through all light from objects behind it.
         On converting to straight alpha, this effect is lost.

      Channel Packed
         A separate image map is stored for each color and alpha channel.
         Channel packing is commonly used by game engines to save memory and to optimize memory access.

   Ambient Light
      The light that comes from the surrounding environment as a whole.

   Ambient Occlusion
      A ratio of how much :term:`Ambient Light` a surface point would be likely to receive.
      If a surface point is under a foot or table,
      it will end up much darker than the top of someone's head or the tabletop.

   Animation
      Simulation of motion.

   Anti-Aliasing
      Is the technique of minimizing :term:`Aliasing`, by e.g. rendering multiple samples per pixel.

   Armature
      An :term:`Object` consisting of :term:`Bones <Bone>`. Used to :term:`Rig` characters, props, etc.

   Asset
      Curated data-blocks that are meant for reuse, usually contained in an :term:`Asset Library`.
      See also :doc:`Asset Libraries </files/asset_libraries/introduction>`.

      Note that there are other meanings of the word "asset" -- sometimes this
      is used more generically, and refers to any "useful thing", like images,
      models, materials, and more.

   Asset Catalog
      Container for assets, similar to what a directory is for files.
      See also :doc:`/files/asset_libraries/catalogs`.

   Asset Library
      Directory on drive, registered in the list of asset libraries in the preferences.
      See also :doc:`Asset Libraries </files/asset_libraries/introduction>` and :term:`Current File Asset Library`.

   Asset Metadata
      Asset-related information, such as its :term:`catalog <Asset Catalog>`,
      description, author, preview, and tags. See :ref:`editing-asset-metadata`.

   Attribute
      A generic term to describe data stored per-element in a geometry data-block.

   Current File Asset Library
      Asset library that is not a directory on drive, but only reflects the assets in
      the current blend-file. This library is available regardless of the location of
      the blend-file. See :ref:`asset-library-current-file`.

   Axis
      A reference line which defines coordinates along one cardinal direction in n-dimensional space.

   Axis Angle
      Rotation method where X, Y, and Z correspond to the axis definition,
      while W corresponds to the angle around that axis, in radians.

   Baking
      The process of computing and storing the result of a potentially
      time-consuming calculation so as to avoid needing to calculate it again.

   Bevel
      The operation to chamfer or bevel edges of an object.

   Bone
      The building block of an :term:`Armature`. Made up of a :term:`Head`,
      :term:`Tail` and :term:`Roll Angle` which define a set of local axes and a
      point of rotation at the Head. Also see :term:`Pose Bone`.

   Bone Collection
      Collection of :term:`bones <Bone>` of an :term:`Armature`, identified by
      its name. Bone collections can be used to organize bones and toggle their
      visibility. See :ref:`bone-collections`.

   Boolean
      A type of logic dealing with binary true/false states.

      See also :doc:`Boolean Modifier </modeling/modifiers/generate/booleans>`.

   Bounding Box
      The box that encloses the shape of an object. The box is aligned with the local space of the object.

   Bump Mapping
      Technique for simulating slight variations in surface height using a grayscale "heightmap" texture.

   Bézier
      A computer graphics technique for generating and representing curves.

   Bit Depth
      The exponent value (with base two) for how many colors can be represented within a single color channel.
      A higher bit depth will allow more possible colors, reducing banding, and increasing precision.
      Yet a higher bit depth will increase memory usage exponentially.

   BVH
   Bounding Volume Hierarchy
      A hierarchical structure of geometric objects.

      See also `Bounding Volume Hierarchy <https://en.wikipedia.org/wiki/Bounding_volume_hierarchy>`__ on Wikipedia.

   Caustics
      The optical phenomenon of light concentration focused by specular reflections or refracting objects.
      In example observable on light passing through a glass of water onto a table or
      the pattern at the bottom of a swimming pool.

      In rendering this refers to diffuse reflected light paths after a glossy or refraction bounce.

      See also `Caustics <https://en.wikipedia.org/wiki/Caustic_(optics)>`__ on Wikipedia.

   Child
      An :term:`Object` that is affected by its :term:`Parent`.

   Chromaticities
      The coordinates of the :term:`Primaries` on the CIE 1931 xy chromaticity diagram.

   Chroma
   Chrominance
      In general, a resulting image color decomposition, where its (*L* or *Y*) luminance channel is separated.
      There are two different contexts whereas this term is used:

      Video Systems
         Refers to the general color decomposition resulting in *Y* (Luminance) and *C* (Chrominance) channels,
         whereas the chrominance is represented by: U = ( Blue minus Luminance ) and V = ( Red minus Luminance ).
      Matte Compositing
         Refers to a point in the color gamut surrounded by a mixture of a determined spectrum of its RGB
         neighboring colors. This point is called *Chroma key* and this key (a chosen color) is used to create
         an *Alpha Mask*. The total amount of gamut space for this chrominance point is defined by users
         in a circular or square-shaped format.

   Clamp
   Clamping
      Limits a variable to a range. The values over or under the range are set
      to the constant values of the range's minimum or maximum.

   Collection
      A device for organizing objects. See also :doc:`Collections </scene_layout/collections/collections>`.

   Blend Modes
   Color Blend Modes
      Methods for blending two colors together.

      See also `Blend Modes <https://docs.krita.org/en/reference_manual/blending_modes.html>`__ on Krita docs.

   Color Gamut
      A gamut traditionally refers to the volume of color a particular color model/space can cover.
      In many instances, it is illustrated via a 2D model using CIE Yxy coordinates.

   Color Model
      A mechanism for representing colors as numbers.

      RGB
         An additive system where three primaries; red, green, and blue are combined to make other colors.
      HSV
         Three values often considered as more intuitive (human perception) than the RGB system.
         In this model, colors are represented as :term:`Hue`, :term:`Saturation`, and :term:`Value`.
      HSL
         Similar to *HSV* except the colors are represented as
         :term:`Hue`, :term:`Saturation`, and :term:`Luminance`.
      YUV
         Luminance-Chrominance standard used in broadcasting analog PAL (European) video.
      YCbCr
         Luminance-ChannelBlue-ChannelRed component video for digital broadcast use,
         whose standards have been updated for HDTV and commonly referred to as the HDMI format for component video.

   Color Space
      A color space is a coordinate system in which a vector represents a color value.
      The definition of a color space specifies three things:

      - The exact color of each of the :term:`Primaries`.
      - The :term:`White Point`.
      - A transfer function (also called a tone response curve).

      The color spaces available in Blender depend on the active :ref:`OCIO config <ocio-config>`.
      The default supported color spaces are described in detail at
      :ref:`Default OpenColorIO Configuration <ocio-config-default-color-spaces>`.

      Linear
         A linear color space means that the numerical values of the color channels are directly proportional
         to light intensity. This is the most physically accurate representation of color and is used internally
         for rendering, shading, and compositing to ensure correct blending and lighting calculations.

      sRGB
         A widely used display-referred color space that uses the Rec.709 :term:`Primaries` and a D65 white point.
         It applies an approximate 2.2 gamma transfer function to better match human perception of brightness.
         sRGB is the standard for monitors, images, and the web, making it the most common format for saving
         or displaying images outside of Blender.

      - Linear color space is recommended for internal work, such as rendering and compositing.
      - sRGB is typically used for output images intended for screens and general distribution.
      - Wide gamut and high dynamic range workflows may use other color spaces, such as ACES, depending on
        the active OCIO configuration.

   Concave Face
      Face in which one vertex is inside a triangle formed by other vertices of the face.

      See also `Convex and concave polygons <https://en.wikipedia.org/wiki/Convex_and_concave_polygons>`__
      on Wikipedia.

   Constraint
      A way of controlling one :term:`Object` with data from another.

   Convex Face
      Face where, if lines were drawn from each vertex to every other vertex,
      all lines would remain in the face. Opposite of a :term:`Concave Face`.

   Coplanar
      Refers to any set of elements that are all aligned to the same 2D plane in 3D space.

   Crease
      Property of an :term:`Edge`. Used to define the sharpness of edges in :term:`Subdivision Surface` meshes.

   Curve
      A type of object defined in terms of a line interpolated between Control Vertices.
      Available types of curves include :term:`Bézier`, :term:`NURBS` and Poly.

   Curve Segment
      The part of a curve connecting two adjacent control points.

   Cyclic
      Often referring to an object being circular. This term is often associated with :term:`Curve`.

   Data-Block
      Data-blocks are the named items in Blender that serve as the base unit of
      data in a blend file, and which can be linked into other blend files. Some
      examples of data-blocks are objects, materials, armatures, meshes,
      node-trees, and actions.

   Data User
      An existing Blender object, which is using its own data, or
      linked data (data owned and controlled by another Blender object).

   DOF
   Depth of Field
      The distance in front of and behind the subject which appears to be in focus. For any given lens setting,
      there is only one distance at which a subject is precisely in focus, but focus falls off gradually on either
      side of that distance, so there is a region in which the blurring is tolerable. This region is greater behind
      the point of focus than it is in front, as the angle of the light rays change more rapidly;
      they approach being parallel with increasing distance.

   DPI
   Dots Per Inch
      A physical measurement for the number of individual dots that can be placed in a line span of one inch.

      This term typically applies to printing however it is often used loosely to mean :term:`PPI`.

      See also:

      - :ref:`Pixel Density support for image formats <files-media-image_formats>`
      - :ref:`Pixel Density support for render output <render-output-pixel-density-panel>`

   Dielectric Material
      A material for real world objects that are electrical insulators such as plastics, wood, glass, etc.
      Essentially this summarizes any material that is solid and non metallic.

   Diffuse Light
      Even, directed light coming off a surface.
      For most things, diffuse light is the main lighting we see.
      Diffuse light comes from a specific direction or location and creates shading.
      Surfaces facing towards the light source will be brighter,
      while surfaces facing away from the light source will be darker.

   Directional Light
      The light that has a specific direction, but no location.
      It seems to come from an infinitely far away source, like the sun.
      Surfaces facing the light are illuminated more than surfaces facing away, but their location does not matter.
      A directional light illuminates all objects in the scene, no matter where they are.

   Displacement Mapping
      A method for distorting vertices based on an image or texture.
      Similar to :term:`Bump Mapping`, but instead operates on the mesh's actual geometry.
      This relies on the mesh having enough geometry to represent details in the image.

   Display Referenced
      Refers to an image whose :term:`Luminance` channel is limited to a certain range of values (usually 0-1).
      The reason it is called display referenced is because a display cannot display an infinite range of values.
      So, the term :term:`Scene Referenced` must go through a transfer function to be converted
      from one to the other.

   Double Buffer
      Technique for rendering and displaying content on the screen.
      Blender uses two buffers (images) to render the interface,
      the content of one buffer is displayed while rendering occurs on the other buffer.
      When rendering is complete, the buffers are switched.

   Edge
      Straight segment (line) that connects two :term:`Vertices <Vertex>`, and can be part of a :term:`Face`.

   Edge Loop
      Chain of :term:`Edges <Edge>` belonging to consecutive :term:`Quads <Quad>`.
      An edge loop ends at a pole or a boundary. Otherwise, it is cyclic.

   Edge Ring
      Path of all :term:`Edges <Edge>` along a :term:`Face Loop` that share two faces belonging to that loop.

   Elastic
      Objects that are able to spontaneously return to their original shape
      after all outside forces are removed from the object.

   Elasticity
      The amount a material is elastic versus inelastic.

   Empty
      An :term:`Object` without any :term:`Vertices`, :term:`Edges <Edge>` or :term:`Faces <Face>`.

   Euler
   Euler Rotation
      Rotation method where rotations are applied to each of the X, Y, Z axes in a specific order.

      Euler orders in Blender are most intuitive when read backwards: *XYZ Euler* is similar to rotating
      around *Local Z* using the *Rotate* tool in the 3D Viewport, followed by *Local Y* and then *Local X*.

   Face
      Mesh element that defines a piece of surface. It consists of three or more :term:`Edges <Edge>`.

   Face Loop
      Chain of consecutive :term:`Quads <Quad>`. A face loop stops at a :term:`Triangle` or :term:`N-gon`
      (which do not belong to the loop), or at a boundary. Otherwise, it is cyclic.

   Face Normal
      The normalized vector perpendicular to the plane that a :term:`Face` lies in. Each face has its own normal.

   Fake User
      A special :term:`Data User`, a program construct that is
      used to mark an object (e.g. material) to be saved in a blend-file,
      even when no :term:`Real User` is using the object.
      Objects that are not used by any Data User are not included in saved blend-files.

   F-Curve
      A curve that holds the animation values of a specific property.

   Field of View
      The area in which objects are visible to the camera. Also see :term:`Focal Length <Focal Length>`.

   Fireflies
      Rendering artifacts encountered with path tracing resulting from
      improbable samples that contribute very high values to pixels.

   Focal Length
      The distance required by a lens to focus collimated light.
      Defines the magnification power of a lens. Also see :term:`Field of View <Field of View>`.

   FK
   Forward Kinematics
      The process of determining the movement of interconnected segments or bones of
      a body or model in the order from the parent bones to the child bones.
      Using forward kinematics on a hierarchically structured object, you can move
      the upper arm then the lower arm and hand go along with the movement.
      Without forward kinematics the lower arm and hand would disconnect from
      upper arm and would move independently in space.

      See also :term:`Inverse Kinematics`.

   Frame Types
      In video compression, a frame can be compressed by several different algorithms.
      These algorithms are known as *picture types* or *frame types*
      and there are three major types: **I**, **P**, and **B** frames.

      I‑frames
         The least compressible but don't require other video frames to decode.
      P‑frames
         Use data from previous frames to decompress and are more compressible than I‑frames.
      B‑frames
         Use both previous and forward frames for data reference to get the highest amount of compression.

   Gamma
      An operation used to adjust the brightness of an image.

      See also `Gamma correction <https://en.wikipedia.org/wiki/Gamma_correction>`__ on Wikipedia.

   Geodesic
      Relating to the shortest possible path between two points on a curved surface.

   Geometric Center
      The mean average of the positions of all vertices making up the object.

   Gimbal
      A pivoted support that allows the rotation of an object about a single axis.

      See also `Gimbal <https://en.wikipedia.org/wiki/Gimbal>`__ on Wikipedia.

   Gimbal Lock
      The limitation where axes of rotation can become aligned,
      losing the ability to rotate on an axis (typically associated with :term:`Euler Rotation`).

      - See also `Gimbal lock <https://en.wikipedia.org/wiki/Gimbal_lock>`__ on Wikipedia.
      - See also `Gimbal lock <https://blender.stackexchange.com/questions/469>`__ on Stack Exchange.

   Global Illumination
      A superset of :term:`Radiosity` and ray tracing. The goal is to compute all possible light interactions
      in a given scene, and thus, obtain a truly photorealistic image.
      All combinations of diffuse and specular reflections and transmissions must be accounted for.
      Effects such as color bleeding and caustics must be included in a global illumination simulation.

   Global Space
      See :term:`World Space`.

   Glossy Map
      See :term:`Roughness Map`.

   Head
      A subcomponent of a :term:`Bone`. The point of rotation for the bone
      has X, Y, and Z coordinates measured in the :term:`Local Space` of the :term:`Armature` object.
      Used in conjunction with the :term:`Tail` to define the local Y axis of the bone
      in :term:`Pose Mode`. The larger of the two ends when displayed as an :term:`Octahedron`.

   HDRI
   High Dynamic Range Image
      A set of techniques that allow a far greater dynamic range of exposures than normal digital imaging techniques.
      The intention is to accurately represent the wide range of intensity levels found in real scenes,
      ranging from direct sunlight to the deepest shadows.

      See also `HDRI <https://en.wikipedia.org/wiki/HDRI>`__ on Wikipedia.

   Hue
      A shade of light out of the color spectrum.

   IOR
   Index of Refraction
      A property of transparent materials.
      When a light ray travels through the same volume it follows a straight path.
      However, if it passes from one transparent volume to another, it bends.
      The angle by which the ray is bent can be determined by the IOR of the materials of both volumes.

   Interpolation
      The process of calculating new data between points of known value, like :term:`Keyframes <Keyframe>`.

   IK
   Inverse Kinematics
      The process of determining the movement of interconnected segments or bones of
      a body or model in the order from the child bones to the parent bones.
      Using inverse kinematics on a hierarchically structured object, you can move
      the hand then the upper and lower arm will automatically follow that movement.
      Without inverse kinematics the hand would come off the model
      and would move independently in space.

      See also :term:`Forward Kinematics`.

   Keyframe
      A frame in an animated sequence drawn or otherwise constructed directly by the animator.
      In classical animation, when all frames were drawn by animators,
      the senior artist would draw these frames, leaving the "in between" frames to an apprentice.
      Now, the animator creates only the first and last frames of a simple sequence (keyframes);
      the computer fills in the gap.

   Keyframing
      Inserting :term:`Keyframes <Keyframe>` to build an animated sequence.

   Lattice
      A type of object consisting of a non-renderable three-dimensional grid of vertices.

      See also :doc:`Lattice Modifier </modeling/modifiers/deform/lattice>`.

   Light Bounces
      Refers to the reflection or transmission of a light ray upon interaction with a material.
      See also :doc:`Light Paths </render/cycles/render_settings/light_paths>`.

   Local Space
      A 3D coordinate system that originates (for Objects) at the :term:`Object Origin`.
      or (for Bones) at the :term:`Head` of the :term:`Bone`.

      Compare to :term:`World Space`.

   Luminance
      The intensity of light either in an image/model channel,
      or emitted from a surface per square unit in a given direction.

   Manifold
      Manifold meshes, also called 'water-tight' meshes, define a closed non-self-intersecting volume
      (see also :term:`Non-manifold`). A manifold mesh is a mesh in which the structure of the connected
      faces in a closed volume will always point the normals (and their surfaces) to the outside
      or to the inside of the mesh without any overlaps. If you recalculate those normals,
      they will always point at a predictable direction (to the outside or to the inside of the volume).
      When working with non-closed volumes, a manifold mesh is a mesh in which
      the normals will always define two different and non-consecutive surfaces.
      A manifold mesh will always define an even number of non-overlapped surfaces.

   MatCap
      Stands for "material capture", using an image to represent a complete material
      including lighting and reflections.

   Matte
   Mask
      A grayscale image used to include or exclude parts of an image.
      A matte is applied as an :term:`Alpha Channel`,
      or it is used as a mix factor when applying :term:`Color Blend Modes`.

   Mesh
      Type of object consisting of :term:`Vertices <Vertex>`, :term:`Edges <Edge>` and :term:`Faces <Face>`.

   Micropolygons
      A polygon roughly the size of a pixel or smaller.

   MIP
   Mip-map
   Mip-mapping
      'MIP' is an acronym of the Latin phrase 'multum in parvo', meaning 'much in little'.
      Mip-maps are progressively lower resolution representations of an image,
      generally reduced by half squared interpolations using :term:`Anti-Aliasing`.
      Mip-mapping is the process used to calculate lower resolutions of
      the same image, reducing memory usage to help speed visualization, but increasing
      memory usage for calculations and allocation. Mip-mapping is also a process
      used to create small anti-aliased samples of an image used for texturing.
      The mip-mapping calculations are made by CPUs, but modern graphic processors
      can be selected for this task and are way faster.

   MIS
   Multiple Importance Sampling
      A process of estimating the direction of light rays to improve sampling quality.

      See :ref:`render-cycles-reducing-noise-mis` and
      also `Importance sampling <https://en.wikipedia.org/wiki/Importance_sampling>`__ on Wikipedia.

   Modifiers
      A non-destructive operation that is applied on top of some sort of data.

   Motion Blur
      The phenomenon that occurs when we perceive a rapidly moving object.
      The object appears to be blurred because of our persistence of vision.
      Simulating motion blur makes computer animation appear more realistic.

   Multisampling
      Rendering multiple samples per pixel, for :term:`Anti-Aliasing`.

   N-gon
      A :term:`Face` that contains more than four :term:`Vertices <Vertex>`.

   NDOF
   3D Mouse
      A general term used to describe a 3D mouse, or any input devices which supports
      more degrees of freedom than a conventional 2D input device, see: :ref:`hardware-ndof`.

   Nonlinear Animation
      Animation technique that allows the animator to edit motions as a whole,
      not just the individual keys. Nonlinear animation allows you to combine,
      mix, and blend different motions to create entirely new animations.

   Non-manifold
      Non-Manifold meshes essentially define geometry which cannot exist in the real world.
      This kind of geometry is not suitable for several types of operations,
      especially those where knowing the volume (inside/outside) of the object is important
      (refraction, fluids, Boolean operations, or 3D printing, to name a few).
      A non-manifold mesh is a mesh in which the structure of
      a non-overlapped surface (based on its connected faces) will not determine
      the inside or the outside of a volume based on its normals, defining
      a single surface for both sides, but ended with flipped normals.
      When working with non-closed volumes, a non-manifold mesh will always
      determine at least one discontinuity in the normal directions, either
      by an inversion of a connected loop, or by an odd number of surfaces.
      A non-manifold mesh will always define an odd number of surfaces.

      There are several types of non-manifold geometry:

      - Some borders and holes (edges with only a single connected face), as faces have no thickness.
      - Edges and vertices not belonging to any face (wire).
      - Edges connected to three or more faces (interior faces).
      - Vertices belonging to faces that are not adjoining (e.g. two cones sharing the vertex at the apex).

      See also: :ref:`Select Non-Manifold <bpy.ops.mesh.select_non_manifold>` tool.

      .. TODO: Images would be useful here.

   Normal
      The normalized vector perpendicular to a surface.

      Normals can be assigned to vertices,
      faces and modulated across a surface using :term:`Normal Mapping`.

      See also `Normals <https://en.wikipedia.org/wiki/Normal_(geometry)>`__ on Wikipedia.

   Normal Mapping
      Is similar to :term:`Bump Mapping`, but instead of the image being a grayscale heightmap,
      the colors define in which direction the normal should be shifted,
      the three color channels being mapped to the three directions X, Y and Z.
      This allows more detail and control over the effect.

   NURBS
   Non-uniform Rational Basis Spline
      A computer graphics technique for generating and representing curves and surfaces.

   Object
      Container for a type (mesh, curve, surface, meta-ball, text, armature,
      lattice, empty, camera, light) and basic 3D transform data (:term:`Object Origin`).

   Object Center
   Object Origin
      A reference point used to position, rotate, and scale an :term:`Object`
      and to define its :term:`Local Space` coordinates.

   Octahedron
      An eight-sided figure commonly used to depict the :term:`Bones <Bone>` of an :term:`Armature`.

   OpenGL
      The graphics system used by Blender (and many other graphics applications)
      for rendering 3D graphics, often taking advantage of hardware acceleration.

      See also `OpenGL <https://en.wikipedia.org/wiki/OpenGL>`__ on Wikipedia.

   Operator
      An executable action that is completed the moment they're initiated.
      See :doc:`/interface/operators` as described in the user interface section.

   Overscan
      The term used to describe the situation.
      when not all of a televised image is present on a viewing screen.

      See also `Overscan <https://en.wikipedia.org/wiki/Overscan>`__ on Wikipedia.

   Panel
      A user interface element that contains buttons.
      Panels are collapsible to hide there contents and can often be rearranged.
      See :ref:`bpy.types.Panel` as described in the user interface section.

   Parent
      An :term:`Object` that affects its :term:`Child` objects.

   Parenting
      Creating a :term:`Parent`-:term:`Child` relationship between two :term:`objects <Object>`.

   Particle System
      Technique that simulates certain kinds of fuzzy phenomena,
      which are otherwise very hard to reproduce with conventional rendering techniques.
      Common examples include fire, explosions, smoke, sparks, falling leaves, clouds, fog, snow, dust,
      meteor tails, stars, and galaxies, or abstract visual effects like glowing trails, magic spells.
      Also used for things like fur, grass or hair.

   Phong
      Local illumination model that can produce a certain degree of realism in three-dimensional
      objects by combining three elements: diffuse, specular and ambient for each considered point on a surface.
      It has several assumptions -- all lights are points, only surface geometry is considered,
      only local modeling of diffuse and specular, specular color is the same as light color,
      ambient is a global constant.

   Pivot Point
      The pivot point is the point in space around which all
      rotation, scaling and mirror transformations are centered.

      See also the :doc:`Pivot Point </editors/3dview/controls/pivot_point/index>` docs.

   Pixel
      The smallest unit of information in a 2D raster image,
      representing a single color made up of red, green, and blue channels.
      If the image has an :term:`Alpha Channel`, the pixel will contain a corresponding fourth channel.

   Point Cloud
      A list of points in 3D space.

   Pole
      :term:`Vertex` where three, five, or more edges meet.
      A vertex connected to one, two, or four edges is not a pole.

   Pose Bone
      Pose-specific properties of a :term:`Bone`, such as its location /
      rotation / scale relative to the :term:`Armature`'s rest pose. Its
      properties are stored on the :term:`Object`, and thus can be different for
      each user of the Armature. The Pose Bone also stores constraints.

   Pose Mode
      Used for :term:`Posing`, :term:`Keyframing`, :term:`Weight Painting`,
      :term:`Constraining <Constraint>` and :term:`Parenting` the :term:`Bones <Bone>` of an :term:`Armature`.

   Posing
      Moving, Rotating and Scaling the :term:`Pose Bones <Pose Bone>` of an
      :term:`Armature` to achieve an aesthetically pleasing pose for a
      character.

   PPI
   Pixels Per Inch
      A physical measurement for the number of individual pixels that can be placed in a line span of one inch.

      This term is sometimes used interchangeably with :term:`DPI`.

      .. seealso::

         - :ref:`Pixel Density support for image formats <files-media-image_formats>`
         - :ref:`Pixel Density support for render output <render-output-pixel-density-panel>`

   Premultiplied Alpha
      See :term:`Alpha Channel`.

   Primaries
      In color theory, primaries (often known as primary colors) are the abstract lights,
      using an absolute model, that make up a :term:`Color Space`.

   Primitive
      A basic object that can be used as a basis for modeling more complicated objects.

   Procedural Texture
      Computer generated (generic) textures that can be configured via different parameters.

   Projection
      In computer graphics, there are two common camera projections used.

      Perspective
         A *perspective* view is geometrically constructed by taking a scene in 3D and placing an observer
         at point *O*. The 2D perspective scene is built by placing a plane (e.g. a sheet of paper)
         where the 2D scene is to be rendered in front of point *O*, perpendicular to the viewing direction.
         For each point *P* in the 3D scene a *PO* line is drawn, passing by *O* and *P*.
         The intersection point *S* between this *PO* line and the plane is the perspective projection
         of that point. By projecting all points *P* of the scene you get a perspective view.
      Orthographic
         In an *orthographic* projection,
         you have a viewing direction but not a viewing point *O*. The line is then drawn
         through point *P* so that it is parallel to the viewing direction. The intersection
         *S* between the line and the plane is the orthographic projection of the point *P*.
         By projecting all points *P* of the scene you get the orthographic view.

   Proxy
      For video editing, a proxy is a smaller version of the original file,
      typically using an optimized video codec and lower resolution version (faster to load)
      that stands in for the main image or video.

      When proxies are built, editing functions like scrubbing and scrolling and compositing is much
      faster but gives lower resolution and slightly imprecise result.

   Quad
   Quadrilateral
   Quadrangle
      :term:`Face` that contains exactly four :term:`Vertices <Vertex>`.

   Quaternion
   Quaternion Rotation
      Rotation method where rotations are defined by four values (X, Y, Z, and W).
      X, Y, and Z also define an :term:`Axis`, and W an angle,
      but it is quite different from :term:`Axis Angle`.

      Quaternion values can be interpreted geometrically as defining a point on a unit
      sphere in 4D space. Moving along any *great circle* of the sphere represents rotating
      around a fixed axis, with one full circle matching two full rotations.

   Radiosity
      A global lighting method
      that calculates patterns of light and shadow for rendering graphics images from three-dimensional models.
      One of the many different tools which can simulate diffuse lighting in Blender.

      See also
      `Radiosity (computer graphics) <https://en.wikipedia.org/wiki/Radiosity_%28computer_graphics%29>`__
      on Wikipedia.

   Random Seed
   Seed
      Blender uses pseudo random number generators, which produce numbers that appear to be random,
      but given the same initial condition, they will always produce the exact same sequence of numbers.

      This is a critical feature to get reproducible and/or stable effects
      (otherwise e.g. your hair simulation would change every time you re-run it,
      without any way to control the outcome).

      The **seed** is a number that represents the initial condition of a random generator,
      if you change its seed, it will produce a new sequence of pseudo-random numbers.

      See also `Random seed <https://en.wikipedia.org/wiki/Random_seed>`__ on Wikipedia.

   Ray Tracing
      Rendering technique that works by tracing the path taken by a ray of light through the scene,
      and calculating reflection, refraction, or absorption of the ray whenever it intersects
      an object in the world. More accurate than :term:`Scanline`, but much slower.

   Real User
      A Blender object, which is a :term:`Data User`.
      Opposite of :term:`Fake User`, which is only a program construct.

   Refraction
      The change in direction of a wave due to a change in velocity.
      It happens when waves travel from a medium with a given :term:`Index of Refraction`
      to a medium with another. At the boundary between the media, the wave changes direction;
      its wavelength increases or decreases but frequency remains constant.

   Render
      The process of computationally generating a 2D image from 3D geometry.

   Resource
      External files such as images, sounds, fonts and volumes files that can be packed into a blend-file.

   Rest Pose
      The initial transformations of a bone or whole Armature. Can also be called a default pose.
      Defined in Armature Edit Mode by the head, tail, and roll of each bone.
      Any constraint or driver-induced transformation is NOT part of the rest pose.

   RGB
      A color model based on the traditional primary colors, Red/Green/Blue.
      RGB colors are also directly broadcasted to most computer monitors.

   Rig
      A system of relationships that determine how something moves. The act of building of such a system.

   Roll
   Roll Angle
      The orientation of the local X and Z axes of a :term:`Bone`.
      Has no effect on the local Y axis as local Y is determined by the location of
      the :term:`Head` and :term:`Tail`.

   Rolling Shutter
      In real CMOS cameras the sensor is read out with scanlines
      and hence different scanlines are sampled at a different moment in time.
      This, for example, make vertical straight lines being curved when doing a horizontal camera pan.
      See also `Rolling Shutter <https://en.wikipedia.org/wiki/Rolling_shutter>`__ on Wikipedia.

   Roughness Map
      A grayscale texture that defines how rough or smooth the surface of a material is.
      This may also be known as a :term:`Glossy Map`.

   Saturation
      Also known as colorfulness, saturation is the quantity of hue in the color
      (from desaturated -- a shade of gray -- to saturated -- brighter colors).

   Scanline
      Rendering technique. Much faster than :term:`Ray Tracing`,
      but allows fewer effects, such as reflections, refractions, motion blur and focal blur.

   Scene Referenced
      An image whose :term:`Luminance` channel is not limited.

      See also :term:`Display Referenced`.

   Blender Session
   Session
      The timespan of a Blender instance. The session begins with starting an instance of Blender
      and ends with closing it.

      In some cases, loading a new file may be considered beginning a new
      session. If so, the documentation should mention that.

   Shading
      Process of altering the color of an object/surface in the 3D scene,
      based on its angle to lights and its distance from lights to create a photorealistic effect.

   Smoothing
      Defines how :term:`Faces <Face>` are shaded. Faces can be either solid (faces are rendered flat)
      or smooth (faces are smoothed by interpolating the normal on every point of the face).

   Specular Light
      A light which is reflected precisely, like a mirror.
      Also used to refer to highlights on reflective objects.

   Straight Alpha
      See :term:`Alpha Channel`.

   SSS
   Subsurface Scattering
      Mechanism of light transport in which light penetrates the surface of a translucent object,
      is scattered by interacting with the material, and exits the surface at a different point.
      All non-metallic materials are translucent to some degree. In particular, materials such as marble, skin,
      and milk are extremely difficult to simulate realistically without taking subsurface scattering into account.

   Subdividing
      Technique for adding more geometry to a mesh.
      It creates new vertices on subdivided edges, new edges between subdivisions and new faces based on new edges.
      If new edges cross a new vertex is created at their crossing point.

   Subdiv
   Subdivision Surface
      A method of creating smooth higher poly surfaces which can take a low polygon mesh as input.

      See also
      `Catmull-Clark subdivision surface <https://en.wikipedia.org/wiki/Catmull%E2%80%93Clark_subdivision_surface>`__
      on Wikipedia.

   Swing
   Swing and Twist
      Refers to decomposition of an arbitrary rotation into a sequence of two single axis rotations:
      a *swing* rotation that aims a chosen axis in its final direction using the shortest possible rotation path,
      followed by a *twist* rotation around that axis.

      This decomposition is available through :ref:`Driver Variables <drivers-variables-rotation-modes>`
      and inputs of the :doc:`Transformation constraint </animation/constraints/transform/transformation>`.
      The :doc:`Damped Track constraint </animation/constraints/tracking/damped_track>` produces
      a pure *swing* rotation.

      In the :term:`Quaternion` representation the *swing* rotation always has 0 as the X/Y/Z component
      corresponding to the selected axis, while *twist* always has 0 as the other two components.

   Tail
      A subcomponent of a :term:`Bone`. Has X, Y and Z coordinates measured in the :term:`Local Space`
      of the armature object. Used in conjunction with the :term:`Head`
      to define the local Y axis of a bone in :term:`Pose Mode`.
      The smaller of the two ends when displayed as an :term:`Octahedron`.

   Tangent
      A line that intersects a surface at exactly one point,
      a tangent is perpendicular to a :term:`Normal <Face Normal>`.

   Tessellation
      The tiling of a plane using one or more geometric shapes usually resulting in :term:`Micropolygons`.

   Texture
      Specifies visual patterns on surfaces and simulates physical surface structure.

   Texture Space
      The bounding box to use when using *Generated* mapping to add a :term:`Texture` to an image.

   Timecode
      A coded signal on videotape or film giving information about the frame number and time the frame was recorded.
      Timecodes are used to sync media between different recording devices, including both audio and video.

   Title Safe
      Area of the screen visible on all devices.
      Place text and graphics inside this area to make sure they do not get cut off.

   Topology
      The arrangement of *Vertices*, *Edges*, and *Faces* which define the shape of a mesh.
      See :term:`Vertex`, :term:`Edge`, and :term:`Face`.

   Transform
   Transformation
      The combination of location, rotation, and scale.
      Can be expressed in :term:`World Space` or :term:`Local Space`.

   Transformation Matrix
      A matrix that is used to represent the :term:`Transformation` of an item.

   Triangle
      :term:`Face` with exactly three :term:`Vertices <Vertex>`.

   UV Map
      Defines a relation between the surface of a mesh and a 2D texture.
      In detail, each face of the mesh is mapped to a corresponding face on the texture.
      It is possible and often common practice to map several faces of the mesh to
      the same or overlapping areas of the texture.

   Value
      The brightness of the color (dark to light).

   Vertex
   Vertices
      A point in 3D space containing a location.
      Vertices are the terminating points of :term:`Edges <Edge>`.

   Vertex Group
      Collection of :term:`Vertices <Vertex>`.
      Vertex groups are useful for limiting operations to specific areas of a mesh.

   Voxel
      A cubic 3D equivalent to the square 2D pixel.
      The name is a combination of the terms "Volumetric" and ":term:`Pixel <Pixel>`".
      Used to store smoke and fire data from physics simulations.

   Walk Cycle
      In animation, a walk cycle is a character that has just the walking function animated.
      Later on in the animation process, the character is placed in an environment
      and the rest of the functions are animated.

   Weight Painting
      Assigning :term:`Vertices` to a :term:`Vertex Group` with a weight of 0.0 - 1.0.

   White Point
      A reference value for white light when all primaries of a color model are combined evenly.

      A white point is defined by a set of `CIE illuminates <https://en.wikipedia.org/wiki/Standard_illuminant>`__
      which correspond to a color temperature.
      For example, D65 corresponds to 6500 K light and D70 corresponding to 7000 K.

   World Space
      A 3D coordinate system that originates at a point at the origin of the world.
      Compare to :term:`Local Space`.

   Z-buffer
      Raster-based storage of the distance measurement between the camera and the surface points.
      Surface points which are in front of the camera have a positive Z value and
      points behind have negative values. The Z-depth map can be visualized as a grayscale image.
