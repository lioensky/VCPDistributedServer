Noise Utilities (mathutils.noise)
=================================

.. module:: mathutils.noise

The Blender noise module.

.. function:: cell(position, /)

   Returns cell noise value at the specified position.

   :param position: The position to evaluate the cell noise at.
   :type position: :class:`mathutils.Vector`
   :return: The cell noise value.
   :rtype: float


.. function:: cell_vector(position, /)

   Returns cell noise vector at the specified position.

   :param position: The position to evaluate the cell noise at.
   :type position: :class:`mathutils.Vector`
   :return: The cell noise vector.
   :rtype: :class:`mathutils.Vector`


.. function:: fractal(position, H, lacunarity, octaves, /, *, noise_basis='PERLIN_ORIGINAL')

   Returns the fractal Brownian motion (fBm) noise value from the noise basis at the specified position.

   :param position: The position to evaluate the selected noise function.
   :type position: :class:`mathutils.Vector`
   :param H: The fractal increment parameter.
   :type H: float
   :param lacunarity: The gap between successive frequencies.
   :type lacunarity: float
   :param octaves: The number of different noise frequencies used.
   :type octaves: float
   :param noise_basis: A noise basis string.
   :type noise_basis: Literal['BLENDER', 'PERLIN_ORIGINAL', 'PERLIN_NEW', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2F1', 'VORONOI_CRACKLE', 'CELLNOISE']
   :return: The fractal Brownian motion noise value.
   :rtype: float


.. function:: hetero_terrain(position, H, lacunarity, octaves, offset, /, *, noise_basis='PERLIN_ORIGINAL')

   Returns the heterogeneous terrain value from the noise basis at the specified position.

   :param position: The position to evaluate the selected noise function.
   :type position: :class:`mathutils.Vector`
   :param H: The fractal dimension of the roughest areas.
   :type H: float
   :param lacunarity: The gap between successive frequencies.
   :type lacunarity: float
   :param octaves: The number of different noise frequencies used.
   :type octaves: float
   :param offset: The height of the terrain above 'sea level'.
   :type offset: float
   :param noise_basis: A noise basis string.
   :type noise_basis: Literal['BLENDER', 'PERLIN_ORIGINAL', 'PERLIN_NEW', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2F1', 'VORONOI_CRACKLE', 'CELLNOISE']
   :return: The heterogeneous terrain value.
   :rtype: float


.. function:: hybrid_multi_fractal(position, H, lacunarity, octaves, offset, gain, /, *, noise_basis='PERLIN_ORIGINAL')

   Returns hybrid multifractal value from the noise basis at the specified position.

   :param position: The position to evaluate the selected noise function.
   :type position: :class:`mathutils.Vector`
   :param H: The fractal dimension of the roughest areas.
   :type H: float
   :param lacunarity: The gap between successive frequencies.
   :type lacunarity: float
   :param octaves: The number of different noise frequencies used.
   :type octaves: float
   :param offset: The height of the terrain above 'sea level'.
   :type offset: float
   :param gain: Scaling applied to the values.
   :type gain: float
   :param noise_basis: A noise basis string.
   :type noise_basis: Literal['BLENDER', 'PERLIN_ORIGINAL', 'PERLIN_NEW', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2F1', 'VORONOI_CRACKLE', 'CELLNOISE']
   :return: The hybrid multifractal value.
   :rtype: float


.. function:: multi_fractal(position, H, lacunarity, octaves, /, *, noise_basis='PERLIN_ORIGINAL')

   Returns multifractal noise value from the noise basis at the specified position.

   :param position: The position to evaluate the selected noise function.
   :type position: :class:`mathutils.Vector`
   :param H: Determines the highest fractal dimension.
   :type H: float
   :param lacunarity: The gap between successive frequencies.
   :type lacunarity: float
   :param octaves: The number of different noise frequencies used.
   :type octaves: float
   :param noise_basis: A noise basis string.
   :type noise_basis: Literal['BLENDER', 'PERLIN_ORIGINAL', 'PERLIN_NEW', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2F1', 'VORONOI_CRACKLE', 'CELLNOISE']
   :return: The multifractal noise value.
   :rtype: float


.. function:: noise(position, /, *, noise_basis='PERLIN_ORIGINAL')

   Returns noise value from the noise basis at the position specified.

   :param position: The position to evaluate the selected noise function.
   :type position: :class:`mathutils.Vector`
   :param noise_basis: A noise basis string.
   :type noise_basis: Literal['BLENDER', 'PERLIN_ORIGINAL', 'PERLIN_NEW', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2F1', 'VORONOI_CRACKLE', 'CELLNOISE']
   :return: The noise value.
   :rtype: float


.. function:: noise_vector(position, /, *, noise_basis='PERLIN_ORIGINAL')

   Returns the noise vector from the noise basis at the specified position.

   :param position: The position to evaluate the selected noise function.
   :type position: :class:`mathutils.Vector`
   :param noise_basis: A noise basis string.
   :type noise_basis: Literal['BLENDER', 'PERLIN_ORIGINAL', 'PERLIN_NEW', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2F1', 'VORONOI_CRACKLE', 'CELLNOISE']
   :return: The noise vector.
   :rtype: :class:`mathutils.Vector`


.. function:: random()

   Returns a random number in the range [0, 1).

   :return: The random number.
   :rtype: float


.. function:: random_unit_vector(*, size=3)

   Returns a unit vector with random entries.

   :param size: The size of the vector to be produced, in the range [2, 4].
   :type size: int
   :return: The random unit vector.
   :rtype: :class:`mathutils.Vector`


.. function:: random_vector(*, size=3)

   Returns a vector with random entries in the range (-1, 1).

   :param size: The size of the vector to be produced, must be 2 or greater.
   :type size: int
   :return: The random vector.
   :rtype: :class:`mathutils.Vector`


.. function:: ridged_multi_fractal(position, H, lacunarity, octaves, offset, gain, /, *, noise_basis='PERLIN_ORIGINAL')

   Returns ridged multifractal value from the noise basis at the specified position.

   :param position: The position to evaluate the selected noise function.
   :type position: :class:`mathutils.Vector`
   :param H: The fractal dimension of the roughest areas.
   :type H: float
   :param lacunarity: The gap between successive frequencies.
   :type lacunarity: float
   :param octaves: The number of different noise frequencies used.
   :type octaves: float
   :param offset: The height of the terrain above 'sea level'.
   :type offset: float
   :param gain: Scaling applied to the values.
   :type gain: float
   :param noise_basis: A noise basis string.
   :type noise_basis: Literal['BLENDER', 'PERLIN_ORIGINAL', 'PERLIN_NEW', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2F1', 'VORONOI_CRACKLE', 'CELLNOISE']
   :return: The ridged multifractal value.
   :rtype: float


.. function:: seed_set(seed, /)

   Sets the random seed used for random_unit_vector, random_vector, and random.

   :param seed: Seed used for the random generator.
      When seed is zero, the current time will be used instead.
   :type seed: int


.. function:: turbulence(position, octaves, hard, /, *, noise_basis='PERLIN_ORIGINAL', amplitude_scale=0.5, frequency_scale=2.0)

   Returns the turbulence value from the noise basis at the specified position.

   :param position: The position to evaluate the selected noise function.
   :type position: :class:`mathutils.Vector`
   :param octaves: The number of different noise frequencies used.
   :type octaves: int
   :param hard: Specifies whether returned turbulence is hard (sharp transitions) or soft (smooth transitions).
   :type hard: bool
   :param noise_basis: A noise basis string.
   :type noise_basis: Literal['BLENDER', 'PERLIN_ORIGINAL', 'PERLIN_NEW', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2F1', 'VORONOI_CRACKLE', 'CELLNOISE']
   :param amplitude_scale: The amplitude scaling factor.
   :type amplitude_scale: float
   :param frequency_scale: The frequency scaling factor.
   :type frequency_scale: float
   :return: The turbulence value.
   :rtype: float


.. function:: turbulence_vector(position, octaves, hard, /, *, noise_basis='PERLIN_ORIGINAL', amplitude_scale=0.5, frequency_scale=2.0)

   Returns the turbulence vector from the noise basis at the specified position.

   :param position: The position to evaluate the selected noise function.
   :type position: :class:`mathutils.Vector`
   :param octaves: The number of different noise frequencies used.
   :type octaves: int
   :param hard: Specifies whether returned turbulence is hard (sharp transitions) or soft (smooth transitions).
   :type hard: bool
   :param noise_basis: A noise basis string.
   :type noise_basis: Literal['BLENDER', 'PERLIN_ORIGINAL', 'PERLIN_NEW', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2F1', 'VORONOI_CRACKLE', 'CELLNOISE']
   :param amplitude_scale: The amplitude scaling factor.
   :type amplitude_scale: float
   :param frequency_scale: The frequency scaling factor.
   :type frequency_scale: float
   :return: The turbulence vector.
   :rtype: :class:`mathutils.Vector`


.. function:: variable_lacunarity(position, distortion, /, *, noise_type1='PERLIN_ORIGINAL', noise_type2='PERLIN_ORIGINAL')

   Returns variable lacunarity noise value, a distorted variety of noise, from noise type 1 distorted by noise type 2 at the specified position.

   :param position: The position to evaluate the selected noise function.
   :type position: :class:`mathutils.Vector`
   :param distortion: The amount of distortion.
   :type distortion: float
   :param noise_type1: A noise type string.
   :type noise_type1: Literal['BLENDER', 'PERLIN_ORIGINAL', 'PERLIN_NEW', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2F1', 'VORONOI_CRACKLE', 'CELLNOISE']
   :param noise_type2: A noise type string.
   :type noise_type2: Literal['BLENDER', 'PERLIN_ORIGINAL', 'PERLIN_NEW', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2F1', 'VORONOI_CRACKLE', 'CELLNOISE']
   :return: The variable lacunarity noise value.
   :rtype: float


.. function:: voronoi(position, /, *, distance_metric='DISTANCE', exponent=2.5)

   Returns a list of distances to the four closest features and their locations.

   :param position: The position to evaluate the selected noise function.
   :type position: :class:`mathutils.Vector`
   :param distance_metric: A distance metric string.
   :type distance_metric: Literal['DISTANCE', 'DISTANCE_SQUARED', 'MANHATTAN', 'CHEBYCHEV', 'MINKOVSKY', 'MINKOVSKY_HALF', 'MINKOVSKY_FOUR']
   :param exponent: The exponent for Minkowski distance metric.
   :type exponent: float
   :return: A list of distances to the four closest features and their locations.
   :rtype: list[list[float] | list[:class:`mathutils.Vector`]]


