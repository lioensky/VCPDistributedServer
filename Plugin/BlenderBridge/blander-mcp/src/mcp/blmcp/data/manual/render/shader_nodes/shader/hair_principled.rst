.. _bpy.types.ShaderNodeBsdfHairPrincipled:

********************
Principled Hair BSDF
********************

.. figure:: /images/node-types_ShaderNodeBsdfHairPrincipled.webp
   :align: right
   :alt: Principled Hair BSDF node under Melanin concentration.

:guilabel:`Cycles Only`

The *Principled Hair* :abbr:`BSDF (Bidirectional Scattering Distribution Function)` is a physically-based,
easy-to-use shader for rendering hair and fur.

.. tip::

   Realistic hair should have a minimum of variance between each strand.
   The shader allows for this by specifying two values, *Random Color*
   and *Random Roughness*, which remap the specified Melanin/Roughness values to
   the range :math:`Color/Roughness \pm Randomization\%`.


Inputs
======

Common
------

Color
   The RGB color of the strand. Only used in Direct coloring.

   .. hint::

      The chosen color is converted to an absorption coefficient with
      the following formula (section 4.2 of [CBTB16]_):

      .. math::

         \sigma_{a} = \frac{\ln(Color)}
         {\left(5.969 - 0.215\beta_{N} + 2.532\beta_{N}^{2} -
         10.73\beta_{N}^{3} + 5.574\beta_{N}^{4} + 0.245\beta_{N}^{5}\right)^{2}}

      where :math:`\beta_{N}` is the radial roughness of the hair after applying randomization (if specified).

   .. figure:: /images/render_shader-nodes_shader_hair-principled_demo-color.jpg
      :align: center

      Coloring hair using the Direct coloring parametrization. (The numbers on top are the RGB values.)

Melanin
   Absolute quantity of pigment.
   Range :math:`[0, 1]` equivalent to :math:`[0\%, 100\%]`.

   .. hint::

      This is a linear mapping to the underlying exponential function:

      .. math::

         melanin\_qty = -\ln(\max(1.0 - Melanin, 0.0001))

   .. figure:: /images/render_shader-nodes_shader_hair-principled_demo-melanin.jpg
      :align: center

      Melanin.

Melanin Redness
   Ratio of pheomelanin to eumelanin.
   Range :math:`[0, 1]` equivalent to :math:`[0\%, 100\%]`.

   .. hint::

      The ratio formula is: :math:`eumelanin = Melanin×(1.0-MelaninRedness)`,
      :math:`pheomelanin = Melanin×MelaninRedness`.

      The resulting quantities are converted (after randomization, if specified)
      to absorption concentration via the following formula
      (section 6.1 of [EFHLA11]_, adjusted for the range :math:`[0, 1]`):

      .. math::

         \sigma_{a} =
         eumelanin   × \left[\begin{matrix} 0.506 \\ 0.841 \\ 1.653 \\ \end{matrix}\right] +
         pheomelanin × \left[\begin{matrix} 0.343 \\ 0.733 \\ 1.924 \\ \end{matrix}\right]

   .. figure:: /images/render_shader-nodes_shader_hair-principled_demo-melanin-redness.jpg
      :align: center

      Melanin Redness.

Tint
   Color used for dyeing the hair after applying the melanin pigment.
   It is not subject to randomization.
   It can be disabled by setting the color to white.

   .. hint::

      This is converted via the Color mapping above and added to
      the absorption coefficient of the melanin concentration.

   .. figure:: /images/render_shader-nodes_shader_hair-principled_demo-tint.jpg
      :align: center

      Tint, using Melanin 0.1 and the corresponding RGB values.

Absorption Coefficient
   Attenuation coefficient :math:`\sigma`.

IOR
   Index of refraction (:term:`IOR`) defining how much the ray changes direction.
   At 1.0 rays pass straight through like in a transparent material;
   higher values give more refraction.
   Default value is :math:`1.55`.
Offset
   Tilts the glint of the hair by increasing the angle of the scales of
   the hair's cuticle with respect to the hair shaft.
   Human hair usually has low values.
Random Color
   For each strand, vary the melanin concentration by :math:`RandomFactor`.
   Range :math:`[0, 1]` equivalent to :math:`[0\%, 100\%]` of
   the initial melanin concentration.

   .. hint::

      The melanin concentration is multiplied by :math:`randomFactor`,
      where :math:`randomFactor = 1.0 + 2.0×(Random - 0.5) × RandomColor`.

   .. figure:: /images/render_shader-nodes_shader_hair-principled_demo-random-color.jpg
      :align: center

      Random Color.

Random Roughness
   For each strand, vary both Roughness values by :math:`RandomFactor`.
   Range :math:`[0, 1]` equivalent to :math:`[0\%, 100\%]` of
   the initial roughness values.

   .. hint::

      The applied formula is the same one as for *Random Color*.

   .. figure:: /images/render_shader-nodes_shader_hair-principled_demo-random-roughness.jpg
      :align: center

      Random Roughness.

Random
   Random number source. If no node is connected here, it is automatically
   instanced with the value obtained from :menuselection:`Hair Info --> Random`.


Chiang Model
------------

The Chiang model is based on a Gaussian distribution with separate roughness
along and orthogonal to the hair.

Roughness
   Specify how much the glints are smoothed in the direction of the hair shaft.
   Too low values will smoothen the hair to the point of looking almost metallic,
   making glints look like :term:`Fireflies`; while setting it too high will result in a Lambertian look.

   .. figure:: /images/render_shader-nodes_shader_hair-principled_demo-roughness.jpg
      :align: center

      Roughness.

Radial Roughness
   Specify how much the glints are smoothed in the direction of the hair normal.
   Too low values will concentrate the glint;
   while setting it too high will spread the light across the width of the strand.

   .. hint::

      Mathematically, this parameter is mapped to the logistic distribution's
      scale factor :math:`s` (section 4.1 of [CBTB16]_).

.. figure:: /images/render_shader-nodes_shader_hair-principled_demo-radial-roughness.jpg
   :align: center

   Radial Roughness.

Coat
   Simulate a shiny coat of fur, by reducing the Roughness to the given factor
   only for the first light bounce (diffuse).
   Range :math:`[0, 1]` equivalent to a reduction of :math:`[0\%, 100\%]` of the original Roughness.

   .. figure:: /images/render_shader-nodes_shader_hair-principled_demo-coat.jpg
      :align: center

      Coat.


Huang Model
-----------

The Huang model is based on microfacet based reflection and transmission,
and supports elliptically shaped hair.

Aspect Ratio
   The ratio of the minor axis to the major axis of an elliptical cross-section.
   Recommended values are 0.8~1 for Asian hair, 0.65~0.9 for Caucasian hair, 0.5~0.65 for
   African hair. The major axis is aligned with the curve normal, which can be created
   with geometry nodes, but is not supported in legacy particle hair.

Roughness
   Microfacet roughness for reflection and transmission.

Reflection
   Optional factor for modulating the first light bounce off the hair surface.
   The color of this component is always white. Keep this 1.0 for physical correctness.
Transmission
   Optional factor for modulating the transmission component. Picks up the color of the
   pigment inside the hair. Keep this 1.0 for physical correctness.
Secondary Reflection
   Optional factor for modulating the component which is transmitted into the hair,
   reflected off the backside of the hair and then transmitted out of the hair. This
   component is oriented approximately around the incoming direction, and picks up the
   color of the pigment inside the hair. Keep this 1.0 for physical correctness


Properties
==========

Color Parametrization
   The shader provides three different ways, or *parametrizations*, to color the hair strands.

   :Direct Coloring:
      Choose the desired RGB color and the shader will approximate
      the necessary *absorption coefficient* (below).

   :Melanin Concentration:
      This mode defines the color as the quantity and
      ratio of the pigments which are commonly found in hair and fur,
      *eumelanin* (prevalent in brown-black hair) and *pheomelanin* (red hair).
      The quantity is specified in the *Melanin* input, and the ratio between them in *Melanin Redness*.
      Increasing concentrations darken the hair (the following are with *Melanin Redness* :math:`1`):

      - White (Melanin :math:`0`)
      - Blonde (Melanin :math:`0.25`)
      - Reddish (Melanin :math:`0.5`)
      - Brown (Melanin :math:`0.75`)
      - Black (Melanin :math:`1`)

      Additionally, the *Tint* inputs allows to dye the hair with the desired color.

   :Absorption Coefficient:
      Specifies the attenuation coefficient :math:`\sigma_{a}`, as applied by the `Beer-Lambert law
      <https://en.wikipedia.org/wiki/Beer%E2%80%93Lambert_law#Expression_with_attenuation_coefficient>`__.
      This mode is intended mainly for technical users who want to use coefficients from the literature
      without any sort of conversion.


Outputs
=======

BSDF
   Standard shader output.


References
==========

This shader is an implementation of the papers by Chiang et al. [CBTB16]_ and Huang et al. [HHH22]_.

.. [CBTB16] Chiang, M. J. , Bitterli, B. , Tappan, C. and Burley, B. (2016),
   A Practical and Controllable Hair and Fur Model for Production Path Tracing. Computer Graphics Forum, 35: 275-283.
   `doi:10.1111/cgf.12830 <https://doi.org/10.1111/cgf.12830>`__

.. [EFHLA11] d'Eon, E. , Francois, G. , Hill, M. , Letteri, J. and Aubry, J. (2011),
   An Energy‐Conserving Hair Reflectance Model. Computer Graphics Forum, 30: 1181-1187.
   `doi:10.1111/j.1467-8659.2011.01976.x <https://doi.org/10.1111/j.1467-8659.2011.01976.x>`__

.. [HHH22] Huang W., Hullin M.B. Hanika J. (2022),
   A Microfacet-based Hair Scattering Model. Computer Graphics Forum, 41: 79-91.
   `doi:10.1111/cgf.14588 <https://doi.org/10.1111/cgf.14588>`__


