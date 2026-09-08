Math Types & Utilities (mathutils)
==================================

.. module:: mathutils

This module provides access to math operations.

.. note::

   Classes, methods and attributes that accept vectors also accept other numeric sequences,
   such as tuples, lists.

The :mod:`mathutils` module provides the following classes:

- :class:`Color`,
- :class:`Euler`,
- :class:`Matrix`,
- :class:`Quaternion`,
- :class:`Vector`,

.. toctree::
   :maxdepth: 1
   :caption: Submodules

   mathutils.geometry.rst
   mathutils.bvhtree.rst
   mathutils.kdtree.rst
   mathutils.interpolate.rst
   mathutils.noise.rst


.. literalinclude:: ./examples/mathutils.0.py

.. class:: Color(rgb=(0.0, 0.0, 0.0), /)

   This object gives access to Colors in Blender.

   Most colors returned by Blender APIs are in scene linear color space, as defined by the OpenColorIO configuration. The notable exception is user interface theming colors, which are in sRGB color space.

   :param rgb: (red, green, blue) color values where (0, 0, 0) is black & (1, 1, 1) is white.
   :type rgb: Sequence[float]


   .. literalinclude:: ./examples/mathutils.Color.0.py

   .. method:: copy()
   
      Returns a copy of this color.
   
      :return: A copy of the color.
      :rtype: :class:`Color`
   
      .. note:: use this to get a copy of a wrapped color with
         no reference to the original data.


   .. method:: freeze()
   
      Make this object immutable.
   
      After this the object can be hashed, used in dictionaries & sets.
   
      :return: An instance of this object.
      :rtype: Self


   .. method:: from_aces_to_scene_linear()
   
      Convert from ACES2065-1 linear to scene linear color space.
   
      :return: A color in scene linear color space.
      :rtype: :class:`Color`


   .. method:: from_acescg_to_scene_linear()
   
      Convert from ACEScg linear to scene linear color space.
   
      :return: A color in scene linear color space.
      :rtype: :class:`Color`


   .. method:: from_rec2020_linear_to_scene_linear()
   
      Convert from Rec.2020 linear color space to scene linear color space.
   
      :return: A color in scene linear color space.
      :rtype: :class:`Color`


   .. method:: from_rec709_linear_to_scene_linear()
   
      Convert from Rec.709 linear color space to scene linear color space.
   
      :return: A color in scene linear color space.
      :rtype: :class:`Color`


   .. method:: from_scene_linear_to_aces()
   
      Convert from scene linear to ACES2065-1 linear color space.
   
      :return: A color in ACES2065-1 linear color space.
      :rtype: :class:`Color`


   .. method:: from_scene_linear_to_acescg()
   
      Convert from scene linear to ACEScg linear color space.
   
      :return: A color in ACEScg linear color space.
      :rtype: :class:`Color`


   .. method:: from_scene_linear_to_rec2020_linear()
   
      Convert from scene linear to Rec.2020 linear color space.
   
      :return: A color in Rec.2020 linear color space.
      :rtype: :class:`Color`


   .. method:: from_scene_linear_to_rec709_linear()
   
      Convert from scene linear to Rec.709 linear color space.
   
      :return: A color in Rec.709 linear color space.
      :rtype: :class:`Color`


   .. method:: from_scene_linear_to_srgb()
   
      Convert from scene linear to sRGB color space.
   
      :return: A color in sRGB color space.
      :rtype: :class:`Color`


   .. method:: from_scene_linear_to_xyz_d65()
   
      Convert from scene linear to CIE XYZ (Illuminant D65) color space.
   
      :return: A color in XYZ color space.
      :rtype: :class:`Color`


   .. method:: from_srgb_to_scene_linear()
   
      Convert from sRGB to scene linear color space.
   
      :return: A color in scene linear color space.
      :rtype: :class:`Color`


   .. method:: from_xyz_d65_to_scene_linear()
   
      Convert from CIE XYZ (Illuminant D65) to scene linear color space.
   
      :return: A color in scene linear color space.
      :rtype: :class:`Color`


   .. attribute:: b

      Blue color channel.
      
      :type: float


   .. attribute:: g

      Green color channel.
      
      :type: float


   .. attribute:: h

      HSV Hue component in [0, 1].
      
      :type: float


   .. attribute:: hsv

      HSV Values in [0, 1].
      
      :type: tuple[float, float, float]


   .. attribute:: is_frozen

      True when this object has been frozen (read-only).
      
      :type: bool


   .. attribute:: is_valid

      True when the owner of this data is valid.
      
      :type: bool


   .. attribute:: is_wrapped

      True when this object wraps external data (read-only).
      
      :type: bool


   .. attribute:: owner

      The item this is wrapping or None (read-only).
      
      :type: Any


   .. attribute:: r

      Red color channel.
      
      :type: float


   .. attribute:: s

      HSV Saturation component in [0, 1].
      
      :type: float


   .. attribute:: v

      HSV Value component in [0, 1].
      
      :type: float




.. class:: Euler(angles=(0.0, 0.0, 0.0), order='XYZ', /)

   This object gives access to Eulers in Blender.

   .. seealso:: `Euler angles <https://en.wikipedia.org/wiki/Euler_angles>`__ on Wikipedia.

   :param angles: (X, Y, Z) angles in radians.
   :type angles: Sequence[float]
   :param order: Euler rotation order.
   :type order: Literal['XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX']


   .. literalinclude:: ./examples/mathutils.Euler.0.py

   .. method:: copy()
   
      Returns a copy of this euler.
   
      :return: A copy of the euler.
      :rtype: :class:`Euler`
   
      .. note:: use this to get a copy of a wrapped euler with
         no reference to the original data.


   .. method:: freeze()
   
      Make this object immutable.
   
      After this the object can be hashed, used in dictionaries & sets.
   
      :return: An instance of this object.
      :rtype: Self


   .. method:: make_compatible(other, /)
   
      Make this euler compatible with another,
      so interpolating between them works as intended.
   
      :param other: Other euler rotation.
      :type other: :class:`Euler`
   
      .. note:: the rotation order is not taken into account for this function.


   .. method:: rotate(other, /)
   
      Rotates the euler by another mathutils value.
   
      :param other: rotation component of mathutils value
      :type other: :class:`Euler` | :class:`Quaternion` | :class:`Matrix`


   .. method:: rotate_axis(axis, angle, /)
   
      Rotates the euler a certain amount, wrapping the result to produce
      a unique euler rotation (no 720 degree pitches).
   
      :param axis: An axis string.
      :type axis: Literal['X', 'Y', 'Z']
      :param angle: angle in radians.
      :type angle: float


   .. method:: to_matrix()
   
      Return a matrix representation of the euler.
   
      :return: A 3x3 rotation matrix representation of the euler.
      :rtype: :class:`Matrix`


   .. method:: to_quaternion()
   
      Return a quaternion representation of the euler.
   
      :return: Quaternion representation of the euler.
      :rtype: :class:`Quaternion`


   .. method:: zero()
   
      Set all values to zero.


   .. attribute:: is_frozen

      True when this object has been frozen (read-only).
      
      :type: bool


   .. attribute:: is_valid

      True when the owner of this data is valid.
      
      :type: bool


   .. attribute:: is_wrapped

      True when this object wraps external data (read-only).
      
      :type: bool


   .. attribute:: order

      Euler rotation order.
      
      :type: Literal['XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX']


   .. attribute:: owner

      The item this is wrapping or None (read-only).
      
      :type: Any


   .. attribute:: x

      Euler axis angle in radians.
      
      :type: float


   .. attribute:: y

      Euler axis angle in radians.
      
      :type: float


   .. attribute:: z

      Euler axis angle in radians.
      
      :type: float




.. class:: Matrix(rows=Matrix.Identity(4), /)

   This object gives access to Matrices in Blender, supporting square and rectangular
   matrices from 2x2 up to 4x4.

   :param rows: Sequence of rows.
   :type rows: Sequence[Sequence[float]]


   .. literalinclude:: ./examples/mathutils.Matrix.0.py

   .. classmethod:: Diagonal(vector, /)
   
      Create a diagonal (scaling) matrix using the values from the vector.
   
      :param vector: The vector of values for the diagonal.
      :type vector: Sequence[float]
      :return: A diagonal matrix.
      :rtype: :class:`Matrix`


   .. classmethod:: Identity(size, /)
   
      Create an identity matrix.
   
      :param size: The size of the identity matrix to construct [2, 4].
      :type size: int
      :return: A new identity matrix.
      :rtype: :class:`Matrix`


   .. classmethod:: LocRotScale(location, rotation, scale, /)
   
      Create a matrix combining translation, rotation and scale,
      acting as the inverse of the decompose() method.
   
      Any of the inputs may be replaced with None if not needed.
   
      :param location: The translation component.
      :type location: Sequence[float] | None
      :param rotation: The rotation component as a 3x3 matrix, quaternion, euler or None for no rotation.
      :type rotation: :class:`Matrix` | :class:`Quaternion` | :class:`Euler` | None
      :param scale: The scale component.
      :type scale: Sequence[float] | None
      :return: Combined transformation as a 4x4 matrix. 
      :rtype: :class:`Matrix`


      .. literalinclude:: ./examples/mathutils.Matrix.LocRotScale.0.py


   .. classmethod:: OrthoProjection(axis, size, /)
   
      Create a matrix to represent an orthographic projection.
   
      :param axis: An axis string,
         where a single axis is for a 2D matrix.
         Or a vector for an arbitrary axis
      :type axis: Literal['X', 'Y', 'XY', 'XZ', 'YZ'] | Sequence[float]
      :param size: The size of the projection matrix to construct [2, 4].
      :type size: int
      :return: A new projection matrix.
      :rtype: :class:`Matrix`


   .. classmethod:: Rotation(angle, size, axis, /)
   
      Create a matrix representing a rotation.
   
      :param angle: The angle of rotation desired, in radians.
      :type angle: float
      :param size: The size of the rotation matrix to construct [2, 4].
      :type size: int
      :param axis: an axis string or a 3D Vector Object
         (optional when size is 2).
      :type axis: Literal['X', 'Y', 'Z'] | Sequence[float]
      :return: A new rotation matrix.
      :rtype: :class:`Matrix`


   .. classmethod:: Scale(factor, size, axis, /)
   
      Create a matrix representing a scaling.
   
      :param factor: The factor of scaling to apply.
      :type factor: float
      :param size: The size of the scale matrix to construct [2, 4].
      :type size: int
      :param axis: Direction to influence scale. (optional).
      :type axis: Sequence[float]
      :return: A new scale matrix.
      :rtype: :class:`Matrix`


   .. classmethod:: Shear(plane, size, factor, /)
   
      Create a matrix to represent a shear transformation.
   
      :param plane: An axis string,
         where a single axis is for a 2D matrix only.
      :type plane: Literal['X', 'Y', 'XY', 'XZ', 'YZ']
      :param size: The size of the shear matrix to construct [2, 4].
      :type size: int
      :param factor: The factor of shear to apply. For a 2 *size* matrix use a single float. For a 3 or 4 *size* matrix pass a pair of floats corresponding with the *plane* axis.
      :type factor: float | Sequence[float]
      :return: A new shear matrix.
      :rtype: :class:`Matrix`


   .. classmethod:: Translation(vector, /)
   
      Create a matrix representing a translation.
   
      :param vector: The translation vector.
      :type vector: Sequence[float]
      :return: An identity matrix with a translation.
      :rtype: :class:`Matrix`


   .. method:: adjugate()
   
      Set the matrix to its adjugate.
   
      :raises ValueError: if the matrix cannot be adjugated.
   
      .. seealso:: `Adjugate matrix <https://en.wikipedia.org/wiki/Adjugate_matrix>`__ on Wikipedia.


   .. method:: adjugated()
   
      Return an adjugated copy of the matrix.
   
      :return: the adjugated matrix.
      :rtype: :class:`Matrix`
      :raises ValueError: if the matrix cannot be adjugated


   .. method:: copy()
   
      Returns a copy of this matrix.
   
      :return: A copy of the matrix.
      :rtype: :class:`Matrix`


   .. method:: decompose()
   
      Return the translation, rotation, and scale components of this 4x4 matrix.
   
      :return: Tuple of translation, rotation, and scale.
      :rtype: tuple[:class:`Vector`, :class:`Quaternion`, :class:`Vector`]


   .. method:: determinant()
   
      Return the determinant of a matrix.
   
      :return: Return the determinant of a matrix.
      :rtype: float
   
      .. seealso:: `Determinant <https://en.wikipedia.org/wiki/Determinant>`__ on Wikipedia.


   .. method:: freeze()
   
      Make this object immutable.
   
      After this the object can be hashed, used in dictionaries & sets.
   
      :return: An instance of this object.
      :rtype: Self


   .. method:: identity()
   
      Set the matrix to the identity matrix.
   
      .. note:: An object with a location and rotation of zero, and a scale of one
         will have an identity matrix.
   
      .. seealso:: `Identity matrix <https://en.wikipedia.org/wiki/Identity_matrix>`__ on Wikipedia.


   .. method:: invert(fallback=None, /)
   
      Set the matrix to its inverse.
   
      :param fallback: Set the matrix to this value when the inverse cannot be calculated
         (instead of raising a :exc:`ValueError` exception).
      :type fallback: :class:`Matrix` | None
   
      .. seealso:: `Inverse matrix <https://en.wikipedia.org/wiki/Inverse_matrix>`__ on Wikipedia.


   .. method:: invert_safe()
   
      Set the matrix to its inverse, will never error.
      If degenerated (e.g. zero scale on an axis), add some epsilon to its diagonal, to get an invertible one.
      If tweaked matrix is still degenerated, set to the identity matrix instead.
   
      .. seealso:: `Inverse Matrix <https://en.wikipedia.org/wiki/Inverse_matrix>`__ on Wikipedia.


   .. method:: inverted(fallback=None, /)
   
      Return an inverted copy of the matrix.
   
      :param fallback: return this when the inverse can't be calculated
         (instead of raising a :exc:`ValueError`).
      :type fallback: Any
      :return: The inverted matrix or fallback when given.
      :rtype: :class:`Matrix` | Any


   .. method:: inverted_safe()
   
      Return an inverted copy of the matrix, will never error.
      If degenerated (e.g. zero scale on an axis), add some epsilon to its diagonal, to get an invertible one.
      If tweaked matrix is still degenerated, return the identity matrix instead.
   
      :return: the inverted matrix.
      :rtype: :class:`Matrix`


   .. method:: lerp(other, factor, /)
   
      Returns the interpolation of two matrices. Uses polar decomposition, see "Matrix Animation and Polar Decomposition", Shoemake and Duff, 1992.
   
      :param other: value to interpolate with.
      :type other: :class:`Matrix`
      :param factor: The interpolation value in [0.0, 1.0].
      :type factor: float
      :return: The interpolated matrix.
      :rtype: :class:`Matrix`


   .. method:: normalize()
   
      Normalize each of the matrix columns (3x3 and 4x4 only).
   
      .. note:: for 4x4 matrices, the 4th column (translation) is left untouched.


   .. method:: normalized()
   
      Return a column normalized matrix (3x3 and 4x4 only).
   
      :return: a column normalized matrix
      :rtype: :class:`Matrix`
   
      .. note:: for 4x4 matrices, the 4th column (translation) is left untouched.


   .. method:: resize_4x4()
   
      Resize the matrix to 4x4.


   .. method:: rotate(other, /)
   
      Rotates the matrix by another mathutils value.
   
      .. note:: The matrix must be 3x3.
   
      .. note:: If any of the columns are not unit length this may not have desired results.
   
      :param other: rotation component of mathutils value
      :type other: :class:`Euler` | :class:`Quaternion` | :class:`Matrix`


   .. method:: to_2x2()
   
      Return a 2x2 copy of this matrix.
   
      :return: a new matrix.
      :rtype: :class:`Matrix`


   .. method:: to_3x3()
   
      Return a 3x3 copy of this matrix.
   
      :return: a new matrix.
      :rtype: :class:`Matrix`


   .. method:: to_4x4()
   
      Return a 4x4 copy of this matrix.
   
      :return: a new matrix.
      :rtype: :class:`Matrix`


   .. method:: to_euler(order='XYZ', euler_compat=None, /)
   
      Return an Euler representation of the rotation matrix
      (3x3 or 4x4 matrix only).
   
      :param order: A rotation order string.
      :type order: Literal['XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX']
      :param euler_compat: Optional euler argument the new euler will be made
         compatible with (no axis flipping between them).
         Useful for converting a series of matrices to animation curves.
      :type euler_compat: :class:`Euler` | None
      :return: Euler representation of the matrix.
      :rtype: :class:`Euler`


   .. method:: to_quaternion()
   
      Return a quaternion representation of the rotation matrix.
   
      :return: Quaternion representation of the rotation matrix.
      :rtype: :class:`Quaternion`


   .. method:: to_scale()
   
      Return the scale part of a 3x3 or 4x4 matrix.
   
      :return: Return the scale of a matrix.
      :rtype: :class:`Vector`
   
      .. note:: This method does not return a negative scale on any axis because it is not possible to obtain this data from the matrix alone.


   .. method:: to_translation()
   
      Return the translation part of a 4x4 matrix.
   
      :return: Return the translation of a matrix.
      :rtype: :class:`Vector`


   .. method:: transpose()
   
      Set the matrix to its transpose.
   
      .. seealso:: `Transpose <https://en.wikipedia.org/wiki/Transpose>`__ on Wikipedia.


   .. method:: transposed()
   
      Return a new, transposed matrix.
   
      :return: a transposed matrix
      :rtype: :class:`Matrix`


   .. method:: zero()
   
      Set all the matrix values to zero.


   .. attribute:: col

      Access the matrix by columns (read-only).
      
      :type: :class:`MatrixAccess`


   .. attribute:: is_frozen

      True when this object has been frozen (read-only).
      
      :type: bool


   .. attribute:: is_identity

      True if this is an identity matrix (read-only).
      
      :type: bool


   .. attribute:: is_negative

      True if this matrix results in a negative scale, 3x3 and 4x4 only, (read-only).
      
      :type: bool


   .. attribute:: is_orthogonal

      True if this matrix is orthogonal, 3x3 and 4x4 only, (read-only).
      
      :type: bool


   .. attribute:: is_orthogonal_axis_vectors

      True if this matrix has orthogonal axis vectors, 3x3 and 4x4 only, (read-only).
      
      :type: bool


   .. attribute:: is_valid

      True when the owner of this data is valid.
      
      :type: bool


   .. attribute:: is_wrapped

      True when this object wraps external data (read-only).
      
      :type: bool


   .. attribute:: median_scale

      The average scale applied to each axis (read-only).
      
      :type: float


   .. attribute:: owner

      The item this is wrapping or None (read-only).
      
      :type: Any


   .. attribute:: row

      Access the matrix by rows (default), (read-only).
      
      :type: :class:`MatrixAccess`


   .. attribute:: translation

      The translation component of the matrix.
      
      :type: :class:`Vector`




.. class:: MatrixAccess

   An indexable type for accessing matrix rows or columns as :class:`Vector` types.



.. class:: Quaternion(seq=(1.0, 0.0, 0.0, 0.0), angle=0.0, /)

   This object gives access to Quaternions in Blender.

   :param seq: A (w, x, y, z) quaternion, a 3D exponential map vector,
      or a 3D axis vector (when *angle* is also provided).
   :type seq: Sequence[float]
   :param angle: rotation angle, in radians
   :type angle: float

   The constructor takes arguments in various forms:

   (), *no args*
      Create an identity quaternion
   (*wxyz*)
      Create a quaternion from a ``(w, x, y, z)`` vector.
   (*exponential_map*)
      Create a quaternion from a 3d exponential map vector.

      .. seealso:: :meth:`to_exponential_map`
   (*axis, angle*)
      Create a quaternion representing a rotation of *angle* radians over *axis*.

      .. seealso:: :meth:`to_axis_angle`


   .. literalinclude:: ./examples/mathutils.Quaternion.0.py

   .. method:: conjugate()
   
      Set the quaternion to its conjugate (negate x, y, z).


   .. method:: conjugated()
   
      Return a new conjugated quaternion.
   
      :return: a new quaternion.
      :rtype: :class:`Quaternion`


   .. method:: copy()
   
      Returns a copy of this quaternion.
   
      :return: A copy of the quaternion.
      :rtype: :class:`Quaternion`
   
      .. note:: use this to get a copy of a wrapped quaternion with
         no reference to the original data.


   .. method:: cross(other, /)
   
      Return the cross product of this quaternion and another.
   
      :param other: The other quaternion to perform the cross product with.
      :type other: :class:`Quaternion`
      :return: The cross product.
      :rtype: :class:`Quaternion`


   .. method:: dot(other, /)
   
      Return the dot product of this quaternion and another.
   
      :param other: The other quaternion to perform the dot product with.
      :type other: :class:`Quaternion`
      :return: The dot product.
      :rtype: float


   .. method:: freeze()
   
      Make this object immutable.
   
      After this the object can be hashed, used in dictionaries & sets.
   
      :return: An instance of this object.
      :rtype: Self


   .. method:: identity()
   
      Set the quaternion to an identity quaternion.


   .. method:: invert()
   
      Set the quaternion to its inverse.


   .. method:: inverted()
   
      Return a new, inverted quaternion.
   
      :return: the inverted value.
      :rtype: :class:`Quaternion`


   .. method:: make_compatible(other, /)
   
      Make this quaternion compatible with another,
      so interpolating between them works as intended.
   
      :param other: The reference quaternion to make this one compatible with.
      :type other: :class:`Quaternion`


   .. method:: negate()
   
      Set the quaternion to its negative.


   .. method:: normalize()
   
      Normalize the quaternion.


   .. method:: normalized()
   
      Return a new normalized quaternion.
   
      :return: a normalized copy.
      :rtype: :class:`Quaternion`


   .. method:: rotate(other, /)
   
      Rotates the quaternion by another mathutils value.
   
      :param other: rotation component of mathutils value
      :type other: :class:`Euler` | :class:`Quaternion` | :class:`Matrix`


   .. method:: rotation_difference(other, /)
   
      Returns a quaternion representing the rotational difference.
   
      :param other: second quaternion.
      :type other: :class:`Quaternion`
      :return: the rotational difference between the two quat rotations.
      :rtype: :class:`Quaternion`


   .. method:: slerp(other, factor, /)
   
      Returns the interpolation of two quaternions.
   
      :param other: value to interpolate with.
      :type other: :class:`Quaternion`
      :param factor: The interpolation value in [0.0, 1.0].
      :type factor: float
      :return: The interpolated rotation.
      :rtype: :class:`Quaternion`


   .. method:: to_axis_angle()
   
      Return the axis, angle representation of the quaternion.
   
      :return: Axis, angle.
      :rtype: tuple[:class:`Vector`, float]


   .. method:: to_euler(order='XYZ', euler_compat=None, /)
   
      Return Euler representation of the quaternion.
   
      :param order: Rotation order.
      :type order: Literal['XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX']
      :param euler_compat: Optional euler argument the new euler will be made
         compatible with (no axis flipping between them).
         Useful for converting a series of quaternions to animation curves.
      :type euler_compat: :class:`Euler` | None
      :return: Euler representation of the quaternion.
      :rtype: :class:`Euler`


   .. method:: to_exponential_map()
   
      Return the exponential map representation of the quaternion.
   
      This representation consists of the rotation axis multiplied by the rotation angle.
      Such a representation is useful for interpolation between multiple orientations.
   
      :return: 3D exponential map.
      :rtype: :class:`Vector`
   
      To convert back to a quaternion, pass it to the :class:`Quaternion` constructor.


   .. method:: to_matrix()
   
      Return a matrix representation of the quaternion.
   
      :return: A 3x3 rotation matrix representation of the quaternion.
      :rtype: :class:`Matrix`


   .. method:: to_swing_twist(axis, /)
   
      Split the rotation into a swing quaternion with the specified
      axis fixed at zero, and the remaining twist rotation angle.
   
      :param axis: Twist axis as a string.
      :type axis: Literal['X', 'Y', 'Z']
      :return: Swing, twist angle.
      :rtype: tuple[:class:`Quaternion`, float]


   .. attribute:: angle

      Angle of the quaternion.
      
      :type: float


   .. attribute:: axis

      Quaternion axis as a vector.
      
      :type: :class:`Vector`


   .. attribute:: is_frozen

      True when this object has been frozen (read-only).
      
      :type: bool


   .. attribute:: is_valid

      True when the owner of this data is valid.
      
      :type: bool


   .. attribute:: is_wrapped

      True when this object wraps external data (read-only).
      
      :type: bool


   .. attribute:: magnitude

      Size of the quaternion (read-only).
      
      :type: float


   .. attribute:: owner

      The item this is wrapping or None (read-only).
      
      :type: Any


   .. attribute:: w

      Quaternion component value.
      
      :type: float


   .. attribute:: x

      Quaternion component value.
      
      :type: float


   .. attribute:: y

      Quaternion component value.
      
      :type: float


   .. attribute:: z

      Quaternion component value.
      
      :type: float




.. class:: Vector(seq=(0.0, 0.0, 0.0), /)

   This object gives access to Vectors in Blender.

   :param seq: Components of the vector, must be a sequence of at least two.
   :type seq: Sequence[float]


   .. literalinclude:: ./examples/mathutils.Vector.0.py

   .. classmethod:: Fill(size, fill=0.0, /)
   
      Create a vector of length size with all values set to fill.
   
      :param size: The length of the vector to be created.
      :type size: int
      :param fill: The value used to fill the vector.
      :type fill: float
      :return: A new vector.
      :rtype: :class:`Vector`


   .. classmethod:: Linspace(start, stop, size, /)
   
      Create a vector of the specified size which is filled with linearly spaced values between start and stop values.
   
      :param start: The start of the range used to fill the vector.
      :type start: float
      :param stop: The end of the range used to fill the vector.
      :type stop: float
      :param size: The size of the vector to be created.
      :type size: int
      :return: A new vector.
      :rtype: :class:`Vector`


   .. classmethod:: Range(start, stop, step=1, /)
   
      Create a vector filled with a range of values.
   
      This method can also be called with a single argument, in which case the argument is interpreted as ``stop`` and ``start`` defaults to 0.
   
      :param start: The start of the range used to fill the vector.
      :type start: int
      :param stop: The end of the range used to fill the vector.
      :type stop: int
      :param step: The step between successive values in the vector.
      :type step: int
      :return: A new vector.
      :rtype: :class:`Vector`


   .. classmethod:: Repeat(vector, size, /)
   
      Create a vector by repeating the values in vector until the required size is reached.
   
      :param vector: The vector to draw values from.
      :type vector: :class:`Vector`
      :param size: The size of the vector to be created.
      :type size: int
      :return: A new vector.
      :rtype: :class:`Vector`


   .. method:: angle(other, fallback=None, /)
   
      Return the angle between two vectors.
   
      .. note:: For 4D vectors, only the x, y, z components are used.
   
      :param other: another vector to compare the angle with
      :type other: :class:`Vector`
      :param fallback: return this when the angle can't be calculated (zero length vector),
         (instead of raising a :exc:`ValueError`).
      :type fallback: Any
      :return: angle in radians or fallback when given
      :rtype: float | Any


   .. method:: angle_signed(other, fallback=None, /)
   
      Return the signed angle between two 2D vectors (clockwise is positive).
   
      :param other: another vector to compare the angle with
      :type other: :class:`Vector`
      :param fallback: return this when the angle can't be calculated (zero length vector),
         (instead of raising a :exc:`ValueError`).
      :type fallback: Any
      :return: angle in radians or fallback when given
      :rtype: float | Any


   .. method:: copy()
   
      Returns a copy of this vector.
   
      :return: A copy of the vector.
      :rtype: :class:`Vector`
   
      .. note:: use this to get a copy of a wrapped vector with
         no reference to the original data.


   .. method:: cross(other, /)
   
      Return the cross product of this vector and another.
   
      :param other: The other vector to perform the cross product with.
      :type other: :class:`Vector`
      :return: The cross product as a vector or a float when 2D vectors are used.
      :rtype: :class:`Vector` | float
   
      .. note:: both vectors must be 2D or 3D


   .. method:: dot(other, /)
   
      Return the dot product of this vector and another.
   
      :param other: The other vector to perform the dot product with.
      :type other: :class:`Vector`
      :return: The dot product.
      :rtype: float


   .. method:: freeze()
   
      Make this object immutable.
   
      After this the object can be hashed, used in dictionaries & sets.
   
      :return: An instance of this object.
      :rtype: Self


   .. method:: lerp(other, factor, /)
   
      Returns the interpolation of two vectors.
   
      :param other: value to interpolate with.
      :type other: :class:`Vector`
      :param factor: The interpolation value in [0.0, 1.0].
      :type factor: float
      :return: The interpolated vector.
      :rtype: :class:`Vector`


   .. method:: negate()
   
      Set all values to their negative.


   .. method:: normalize()
   
      Normalize the vector, making the length of the vector always 1.0.
   
      .. warning:: Normalizing a vector where all values are zero has no effect.
   
      .. note:: For 4D vectors, only the x, y, z components are normalized;
         the w component is left untouched.
         The resulting 4D vector may not have unit length.


   .. method:: normalized()
   
      Return a new, normalized vector.
   
      .. note:: For 4D vectors, only the x, y, z components are normalized;
         the w component is left untouched.
         The resulting 4D vector may not have unit length.
   
      :return: a normalized copy of the vector
      :rtype: :class:`Vector`


   .. method:: orthogonal()
   
      Return a perpendicular vector.
   
      :return: a new vector 90 degrees from this vector.
      :rtype: :class:`Vector`
   
      .. note:: the axis is undefined, only use when any orthogonal vector is acceptable.


   .. method:: project(other, /)
   
      Return the projection of this vector onto the *other*.
   
      :param other: second vector.
      :type other: :class:`Vector`
      :return: the parallel projection vector
      :rtype: :class:`Vector`


   .. method:: reflect(mirror, /)
   
      Return the reflection vector from the *mirror* argument.
   
      :param mirror: This vector could be a normal from the reflecting surface.
      :type mirror: :class:`Vector`
      :return: The reflected vector matching the size of this vector.
      :rtype: :class:`Vector`


   .. method:: resize(size, /)
   
      Resize the vector to have size number of elements.
   
      :param size: The new size of the vector.
      :type size: int


   .. method:: resize_2d()
   
      Resize the vector to 2D (x, y).


   .. method:: resize_3d()
   
      Resize the vector to 3D (x, y, z).


   .. method:: resize_4d()
   
      Resize the vector to 4D (x, y, z, w).


   .. method:: resized(size, /)
   
      Return a resized copy of the vector with size number of elements.
   
      :param size: The new size of the vector.
      :type size: int
      :return: A new vector.
      :rtype: :class:`Vector`


   .. method:: rotate(other, /)
   
      Rotate the vector by a rotation value.
   
      .. note:: 2D vectors are a special case that can only be rotated by a 2x2 matrix.
   
      :param other: rotation component of mathutils value
      :type other: :class:`Euler` | :class:`Quaternion` | :class:`Matrix`


   .. method:: rotation_difference(other, /)
   
      Returns a quaternion representing the rotational difference between this
      vector and another.
   
      :param other: second vector.
      :type other: :class:`Vector`
      :return: the rotational difference between the two vectors.
      :rtype: :class:`Quaternion`
   
      .. note:: 2D vectors raise an :exc:`AttributeError`.


   .. method:: slerp(other, factor, fallback=None, /)
   
      Returns the interpolation of two non-zero vectors (spherical coordinates).
   
      :param other: value to interpolate with.
      :type other: :class:`Vector`
      :param factor: The interpolation value typically in [0.0, 1.0].
      :type factor: float
      :param fallback: return this when the vector can't be calculated (zero length vector or direct opposites),
         (instead of raising a :exc:`ValueError`).
      :type fallback: Any
      :return: The interpolated vector.
      :rtype: :class:`Vector`


   .. method:: to_2d()
   
      Return a 2d copy of the vector.
   
      :return: a new vector
      :rtype: :class:`Vector`


   .. method:: to_3d()
   
      Return a 3d copy of the vector.
   
      :return: a new vector
      :rtype: :class:`Vector`


   .. method:: to_4d()
   
      Return a 4d copy of the vector.
   
      :return: a new vector
      :rtype: :class:`Vector`


   .. method:: to_track_quat(track='Z', up='Y', /)
   
      Return a quaternion rotation from the vector and the track and up axis.
   
      :param track: Track axis string.
      :type track: Literal['X', 'Y', 'Z', '-X', '-Y', '-Z']
      :param up: Up axis string.
      :type up: Literal['X', 'Y', 'Z']
      :return: rotation from the vector and the track and up axis.
      :rtype: :class:`Quaternion`


   .. method:: to_tuple(precision=-1, /)
   
      Return this vector as a tuple with a given precision.
   
      :param precision: The number to round the value to in [-1, 21].
      :type precision: int
      :return: the values of the vector rounded by *precision*
      :rtype: tuple[float, ...]


   .. method:: zero()
   
      Set all values to zero.


   .. attribute:: is_frozen

      True when this object has been frozen (read-only).
      
      :type: bool


   .. attribute:: is_valid

      True when the owner of this data is valid.
      
      :type: bool


   .. attribute:: is_wrapped

      True when this object wraps external data (read-only).
      
      :type: bool


   .. attribute:: length

      Vector Length.
      
      :type: float


   .. attribute:: length_squared

      Vector length squared (v.dot(v)).
      
      :type: float


   .. attribute:: magnitude

      Vector Length.
      
      :type: float


   .. attribute:: owner

      The item this is wrapping or None (read-only).
      
      :type: Any


   .. attribute:: w

      Vector W axis (4D Vectors only).
      
      :type: float


   .. attribute:: ww

      :type: :class:`Vector`


   .. attribute:: www

      :type: :class:`Vector`


   .. attribute:: wwww

      :type: :class:`Vector`


   .. attribute:: wwwx

      :type: :class:`Vector`


   .. attribute:: wwwy

      :type: :class:`Vector`


   .. attribute:: wwwz

      :type: :class:`Vector`


   .. attribute:: wwx

      :type: :class:`Vector`


   .. attribute:: wwxw

      :type: :class:`Vector`


   .. attribute:: wwxx

      :type: :class:`Vector`


   .. attribute:: wwxy

      :type: :class:`Vector`


   .. attribute:: wwxz

      :type: :class:`Vector`


   .. attribute:: wwy

      :type: :class:`Vector`


   .. attribute:: wwyw

      :type: :class:`Vector`


   .. attribute:: wwyx

      :type: :class:`Vector`


   .. attribute:: wwyy

      :type: :class:`Vector`


   .. attribute:: wwyz

      :type: :class:`Vector`


   .. attribute:: wwz

      :type: :class:`Vector`


   .. attribute:: wwzw

      :type: :class:`Vector`


   .. attribute:: wwzx

      :type: :class:`Vector`


   .. attribute:: wwzy

      :type: :class:`Vector`


   .. attribute:: wwzz

      :type: :class:`Vector`


   .. attribute:: wx

      :type: :class:`Vector`


   .. attribute:: wxw

      :type: :class:`Vector`


   .. attribute:: wxww

      :type: :class:`Vector`


   .. attribute:: wxwx

      :type: :class:`Vector`


   .. attribute:: wxwy

      :type: :class:`Vector`


   .. attribute:: wxwz

      :type: :class:`Vector`


   .. attribute:: wxx

      :type: :class:`Vector`


   .. attribute:: wxxw

      :type: :class:`Vector`


   .. attribute:: wxxx

      :type: :class:`Vector`


   .. attribute:: wxxy

      :type: :class:`Vector`


   .. attribute:: wxxz

      :type: :class:`Vector`


   .. attribute:: wxy

      :type: :class:`Vector`


   .. attribute:: wxyw

      :type: :class:`Vector`


   .. attribute:: wxyx

      :type: :class:`Vector`


   .. attribute:: wxyy

      :type: :class:`Vector`


   .. attribute:: wxyz

      :type: :class:`Vector`


   .. attribute:: wxz

      :type: :class:`Vector`


   .. attribute:: wxzw

      :type: :class:`Vector`


   .. attribute:: wxzx

      :type: :class:`Vector`


   .. attribute:: wxzy

      :type: :class:`Vector`


   .. attribute:: wxzz

      :type: :class:`Vector`


   .. attribute:: wy

      :type: :class:`Vector`


   .. attribute:: wyw

      :type: :class:`Vector`


   .. attribute:: wyww

      :type: :class:`Vector`


   .. attribute:: wywx

      :type: :class:`Vector`


   .. attribute:: wywy

      :type: :class:`Vector`


   .. attribute:: wywz

      :type: :class:`Vector`


   .. attribute:: wyx

      :type: :class:`Vector`


   .. attribute:: wyxw

      :type: :class:`Vector`


   .. attribute:: wyxx

      :type: :class:`Vector`


   .. attribute:: wyxy

      :type: :class:`Vector`


   .. attribute:: wyxz

      :type: :class:`Vector`


   .. attribute:: wyy

      :type: :class:`Vector`


   .. attribute:: wyyw

      :type: :class:`Vector`


   .. attribute:: wyyx

      :type: :class:`Vector`


   .. attribute:: wyyy

      :type: :class:`Vector`


   .. attribute:: wyyz

      :type: :class:`Vector`


   .. attribute:: wyz

      :type: :class:`Vector`


   .. attribute:: wyzw

      :type: :class:`Vector`


   .. attribute:: wyzx

      :type: :class:`Vector`


   .. attribute:: wyzy

      :type: :class:`Vector`


   .. attribute:: wyzz

      :type: :class:`Vector`


   .. attribute:: wz

      :type: :class:`Vector`


   .. attribute:: wzw

      :type: :class:`Vector`


   .. attribute:: wzww

      :type: :class:`Vector`


   .. attribute:: wzwx

      :type: :class:`Vector`


   .. attribute:: wzwy

      :type: :class:`Vector`


   .. attribute:: wzwz

      :type: :class:`Vector`


   .. attribute:: wzx

      :type: :class:`Vector`


   .. attribute:: wzxw

      :type: :class:`Vector`


   .. attribute:: wzxx

      :type: :class:`Vector`


   .. attribute:: wzxy

      :type: :class:`Vector`


   .. attribute:: wzxz

      :type: :class:`Vector`


   .. attribute:: wzy

      :type: :class:`Vector`


   .. attribute:: wzyw

      :type: :class:`Vector`


   .. attribute:: wzyx

      :type: :class:`Vector`


   .. attribute:: wzyy

      :type: :class:`Vector`


   .. attribute:: wzyz

      :type: :class:`Vector`


   .. attribute:: wzz

      :type: :class:`Vector`


   .. attribute:: wzzw

      :type: :class:`Vector`


   .. attribute:: wzzx

      :type: :class:`Vector`


   .. attribute:: wzzy

      :type: :class:`Vector`


   .. attribute:: wzzz

      :type: :class:`Vector`


   .. attribute:: x

      Vector X axis.
      
      :type: float


   .. attribute:: xw

      :type: :class:`Vector`


   .. attribute:: xww

      :type: :class:`Vector`


   .. attribute:: xwww

      :type: :class:`Vector`


   .. attribute:: xwwx

      :type: :class:`Vector`


   .. attribute:: xwwy

      :type: :class:`Vector`


   .. attribute:: xwwz

      :type: :class:`Vector`


   .. attribute:: xwx

      :type: :class:`Vector`


   .. attribute:: xwxw

      :type: :class:`Vector`


   .. attribute:: xwxx

      :type: :class:`Vector`


   .. attribute:: xwxy

      :type: :class:`Vector`


   .. attribute:: xwxz

      :type: :class:`Vector`


   .. attribute:: xwy

      :type: :class:`Vector`


   .. attribute:: xwyw

      :type: :class:`Vector`


   .. attribute:: xwyx

      :type: :class:`Vector`


   .. attribute:: xwyy

      :type: :class:`Vector`


   .. attribute:: xwyz

      :type: :class:`Vector`


   .. attribute:: xwz

      :type: :class:`Vector`


   .. attribute:: xwzw

      :type: :class:`Vector`


   .. attribute:: xwzx

      :type: :class:`Vector`


   .. attribute:: xwzy

      :type: :class:`Vector`


   .. attribute:: xwzz

      :type: :class:`Vector`


   .. attribute:: xx

      :type: :class:`Vector`


   .. attribute:: xxw

      :type: :class:`Vector`


   .. attribute:: xxww

      :type: :class:`Vector`


   .. attribute:: xxwx

      :type: :class:`Vector`


   .. attribute:: xxwy

      :type: :class:`Vector`


   .. attribute:: xxwz

      :type: :class:`Vector`


   .. attribute:: xxx

      :type: :class:`Vector`


   .. attribute:: xxxw

      :type: :class:`Vector`


   .. attribute:: xxxx

      :type: :class:`Vector`


   .. attribute:: xxxy

      :type: :class:`Vector`


   .. attribute:: xxxz

      :type: :class:`Vector`


   .. attribute:: xxy

      :type: :class:`Vector`


   .. attribute:: xxyw

      :type: :class:`Vector`


   .. attribute:: xxyx

      :type: :class:`Vector`


   .. attribute:: xxyy

      :type: :class:`Vector`


   .. attribute:: xxyz

      :type: :class:`Vector`


   .. attribute:: xxz

      :type: :class:`Vector`


   .. attribute:: xxzw

      :type: :class:`Vector`


   .. attribute:: xxzx

      :type: :class:`Vector`


   .. attribute:: xxzy

      :type: :class:`Vector`


   .. attribute:: xxzz

      :type: :class:`Vector`


   .. attribute:: xy

      :type: :class:`Vector`


   .. attribute:: xyw

      :type: :class:`Vector`


   .. attribute:: xyww

      :type: :class:`Vector`


   .. attribute:: xywx

      :type: :class:`Vector`


   .. attribute:: xywy

      :type: :class:`Vector`


   .. attribute:: xywz

      :type: :class:`Vector`


   .. attribute:: xyx

      :type: :class:`Vector`


   .. attribute:: xyxw

      :type: :class:`Vector`


   .. attribute:: xyxx

      :type: :class:`Vector`


   .. attribute:: xyxy

      :type: :class:`Vector`


   .. attribute:: xyxz

      :type: :class:`Vector`


   .. attribute:: xyy

      :type: :class:`Vector`


   .. attribute:: xyyw

      :type: :class:`Vector`


   .. attribute:: xyyx

      :type: :class:`Vector`


   .. attribute:: xyyy

      :type: :class:`Vector`


   .. attribute:: xyyz

      :type: :class:`Vector`


   .. attribute:: xyz

      :type: :class:`Vector`


   .. attribute:: xyzw

      :type: :class:`Vector`


   .. attribute:: xyzx

      :type: :class:`Vector`


   .. attribute:: xyzy

      :type: :class:`Vector`


   .. attribute:: xyzz

      :type: :class:`Vector`


   .. attribute:: xz

      :type: :class:`Vector`


   .. attribute:: xzw

      :type: :class:`Vector`


   .. attribute:: xzww

      :type: :class:`Vector`


   .. attribute:: xzwx

      :type: :class:`Vector`


   .. attribute:: xzwy

      :type: :class:`Vector`


   .. attribute:: xzwz

      :type: :class:`Vector`


   .. attribute:: xzx

      :type: :class:`Vector`


   .. attribute:: xzxw

      :type: :class:`Vector`


   .. attribute:: xzxx

      :type: :class:`Vector`


   .. attribute:: xzxy

      :type: :class:`Vector`


   .. attribute:: xzxz

      :type: :class:`Vector`


   .. attribute:: xzy

      :type: :class:`Vector`


   .. attribute:: xzyw

      :type: :class:`Vector`


   .. attribute:: xzyx

      :type: :class:`Vector`


   .. attribute:: xzyy

      :type: :class:`Vector`


   .. attribute:: xzyz

      :type: :class:`Vector`


   .. attribute:: xzz

      :type: :class:`Vector`


   .. attribute:: xzzw

      :type: :class:`Vector`


   .. attribute:: xzzx

      :type: :class:`Vector`


   .. attribute:: xzzy

      :type: :class:`Vector`


   .. attribute:: xzzz

      :type: :class:`Vector`


   .. attribute:: y

      Vector Y axis.
      
      :type: float


   .. attribute:: yw

      :type: :class:`Vector`


   .. attribute:: yww

      :type: :class:`Vector`


   .. attribute:: ywww

      :type: :class:`Vector`


   .. attribute:: ywwx

      :type: :class:`Vector`


   .. attribute:: ywwy

      :type: :class:`Vector`


   .. attribute:: ywwz

      :type: :class:`Vector`


   .. attribute:: ywx

      :type: :class:`Vector`


   .. attribute:: ywxw

      :type: :class:`Vector`


   .. attribute:: ywxx

      :type: :class:`Vector`


   .. attribute:: ywxy

      :type: :class:`Vector`


   .. attribute:: ywxz

      :type: :class:`Vector`


   .. attribute:: ywy

      :type: :class:`Vector`


   .. attribute:: ywyw

      :type: :class:`Vector`


   .. attribute:: ywyx

      :type: :class:`Vector`


   .. attribute:: ywyy

      :type: :class:`Vector`


   .. attribute:: ywyz

      :type: :class:`Vector`


   .. attribute:: ywz

      :type: :class:`Vector`


   .. attribute:: ywzw

      :type: :class:`Vector`


   .. attribute:: ywzx

      :type: :class:`Vector`


   .. attribute:: ywzy

      :type: :class:`Vector`


   .. attribute:: ywzz

      :type: :class:`Vector`


   .. attribute:: yx

      :type: :class:`Vector`


   .. attribute:: yxw

      :type: :class:`Vector`


   .. attribute:: yxww

      :type: :class:`Vector`


   .. attribute:: yxwx

      :type: :class:`Vector`


   .. attribute:: yxwy

      :type: :class:`Vector`


   .. attribute:: yxwz

      :type: :class:`Vector`


   .. attribute:: yxx

      :type: :class:`Vector`


   .. attribute:: yxxw

      :type: :class:`Vector`


   .. attribute:: yxxx

      :type: :class:`Vector`


   .. attribute:: yxxy

      :type: :class:`Vector`


   .. attribute:: yxxz

      :type: :class:`Vector`


   .. attribute:: yxy

      :type: :class:`Vector`


   .. attribute:: yxyw

      :type: :class:`Vector`


   .. attribute:: yxyx

      :type: :class:`Vector`


   .. attribute:: yxyy

      :type: :class:`Vector`


   .. attribute:: yxyz

      :type: :class:`Vector`


   .. attribute:: yxz

      :type: :class:`Vector`


   .. attribute:: yxzw

      :type: :class:`Vector`


   .. attribute:: yxzx

      :type: :class:`Vector`


   .. attribute:: yxzy

      :type: :class:`Vector`


   .. attribute:: yxzz

      :type: :class:`Vector`


   .. attribute:: yy

      :type: :class:`Vector`


   .. attribute:: yyw

      :type: :class:`Vector`


   .. attribute:: yyww

      :type: :class:`Vector`


   .. attribute:: yywx

      :type: :class:`Vector`


   .. attribute:: yywy

      :type: :class:`Vector`


   .. attribute:: yywz

      :type: :class:`Vector`


   .. attribute:: yyx

      :type: :class:`Vector`


   .. attribute:: yyxw

      :type: :class:`Vector`


   .. attribute:: yyxx

      :type: :class:`Vector`


   .. attribute:: yyxy

      :type: :class:`Vector`


   .. attribute:: yyxz

      :type: :class:`Vector`


   .. attribute:: yyy

      :type: :class:`Vector`


   .. attribute:: yyyw

      :type: :class:`Vector`


   .. attribute:: yyyx

      :type: :class:`Vector`


   .. attribute:: yyyy

      :type: :class:`Vector`


   .. attribute:: yyyz

      :type: :class:`Vector`


   .. attribute:: yyz

      :type: :class:`Vector`


   .. attribute:: yyzw

      :type: :class:`Vector`


   .. attribute:: yyzx

      :type: :class:`Vector`


   .. attribute:: yyzy

      :type: :class:`Vector`


   .. attribute:: yyzz

      :type: :class:`Vector`


   .. attribute:: yz

      :type: :class:`Vector`


   .. attribute:: yzw

      :type: :class:`Vector`


   .. attribute:: yzww

      :type: :class:`Vector`


   .. attribute:: yzwx

      :type: :class:`Vector`


   .. attribute:: yzwy

      :type: :class:`Vector`


   .. attribute:: yzwz

      :type: :class:`Vector`


   .. attribute:: yzx

      :type: :class:`Vector`


   .. attribute:: yzxw

      :type: :class:`Vector`


   .. attribute:: yzxx

      :type: :class:`Vector`


   .. attribute:: yzxy

      :type: :class:`Vector`


   .. attribute:: yzxz

      :type: :class:`Vector`


   .. attribute:: yzy

      :type: :class:`Vector`


   .. attribute:: yzyw

      :type: :class:`Vector`


   .. attribute:: yzyx

      :type: :class:`Vector`


   .. attribute:: yzyy

      :type: :class:`Vector`


   .. attribute:: yzyz

      :type: :class:`Vector`


   .. attribute:: yzz

      :type: :class:`Vector`


   .. attribute:: yzzw

      :type: :class:`Vector`


   .. attribute:: yzzx

      :type: :class:`Vector`


   .. attribute:: yzzy

      :type: :class:`Vector`


   .. attribute:: yzzz

      :type: :class:`Vector`


   .. attribute:: z

      Vector Z axis (3D Vectors only).
      
      :type: float


   .. attribute:: zw

      :type: :class:`Vector`


   .. attribute:: zww

      :type: :class:`Vector`


   .. attribute:: zwww

      :type: :class:`Vector`


   .. attribute:: zwwx

      :type: :class:`Vector`


   .. attribute:: zwwy

      :type: :class:`Vector`


   .. attribute:: zwwz

      :type: :class:`Vector`


   .. attribute:: zwx

      :type: :class:`Vector`


   .. attribute:: zwxw

      :type: :class:`Vector`


   .. attribute:: zwxx

      :type: :class:`Vector`


   .. attribute:: zwxy

      :type: :class:`Vector`


   .. attribute:: zwxz

      :type: :class:`Vector`


   .. attribute:: zwy

      :type: :class:`Vector`


   .. attribute:: zwyw

      :type: :class:`Vector`


   .. attribute:: zwyx

      :type: :class:`Vector`


   .. attribute:: zwyy

      :type: :class:`Vector`


   .. attribute:: zwyz

      :type: :class:`Vector`


   .. attribute:: zwz

      :type: :class:`Vector`


   .. attribute:: zwzw

      :type: :class:`Vector`


   .. attribute:: zwzx

      :type: :class:`Vector`


   .. attribute:: zwzy

      :type: :class:`Vector`


   .. attribute:: zwzz

      :type: :class:`Vector`


   .. attribute:: zx

      :type: :class:`Vector`


   .. attribute:: zxw

      :type: :class:`Vector`


   .. attribute:: zxww

      :type: :class:`Vector`


   .. attribute:: zxwx

      :type: :class:`Vector`


   .. attribute:: zxwy

      :type: :class:`Vector`


   .. attribute:: zxwz

      :type: :class:`Vector`


   .. attribute:: zxx

      :type: :class:`Vector`


   .. attribute:: zxxw

      :type: :class:`Vector`


   .. attribute:: zxxx

      :type: :class:`Vector`


   .. attribute:: zxxy

      :type: :class:`Vector`


   .. attribute:: zxxz

      :type: :class:`Vector`


   .. attribute:: zxy

      :type: :class:`Vector`


   .. attribute:: zxyw

      :type: :class:`Vector`


   .. attribute:: zxyx

      :type: :class:`Vector`


   .. attribute:: zxyy

      :type: :class:`Vector`


   .. attribute:: zxyz

      :type: :class:`Vector`


   .. attribute:: zxz

      :type: :class:`Vector`


   .. attribute:: zxzw

      :type: :class:`Vector`


   .. attribute:: zxzx

      :type: :class:`Vector`


   .. attribute:: zxzy

      :type: :class:`Vector`


   .. attribute:: zxzz

      :type: :class:`Vector`


   .. attribute:: zy

      :type: :class:`Vector`


   .. attribute:: zyw

      :type: :class:`Vector`


   .. attribute:: zyww

      :type: :class:`Vector`


   .. attribute:: zywx

      :type: :class:`Vector`


   .. attribute:: zywy

      :type: :class:`Vector`


   .. attribute:: zywz

      :type: :class:`Vector`


   .. attribute:: zyx

      :type: :class:`Vector`


   .. attribute:: zyxw

      :type: :class:`Vector`


   .. attribute:: zyxx

      :type: :class:`Vector`


   .. attribute:: zyxy

      :type: :class:`Vector`


   .. attribute:: zyxz

      :type: :class:`Vector`


   .. attribute:: zyy

      :type: :class:`Vector`


   .. attribute:: zyyw

      :type: :class:`Vector`


   .. attribute:: zyyx

      :type: :class:`Vector`


   .. attribute:: zyyy

      :type: :class:`Vector`


   .. attribute:: zyyz

      :type: :class:`Vector`


   .. attribute:: zyz

      :type: :class:`Vector`


   .. attribute:: zyzw

      :type: :class:`Vector`


   .. attribute:: zyzx

      :type: :class:`Vector`


   .. attribute:: zyzy

      :type: :class:`Vector`


   .. attribute:: zyzz

      :type: :class:`Vector`


   .. attribute:: zz

      :type: :class:`Vector`


   .. attribute:: zzw

      :type: :class:`Vector`


   .. attribute:: zzww

      :type: :class:`Vector`


   .. attribute:: zzwx

      :type: :class:`Vector`


   .. attribute:: zzwy

      :type: :class:`Vector`


   .. attribute:: zzwz

      :type: :class:`Vector`


   .. attribute:: zzx

      :type: :class:`Vector`


   .. attribute:: zzxw

      :type: :class:`Vector`


   .. attribute:: zzxx

      :type: :class:`Vector`


   .. attribute:: zzxy

      :type: :class:`Vector`


   .. attribute:: zzxz

      :type: :class:`Vector`


   .. attribute:: zzy

      :type: :class:`Vector`


   .. attribute:: zzyw

      :type: :class:`Vector`


   .. attribute:: zzyx

      :type: :class:`Vector`


   .. attribute:: zzyy

      :type: :class:`Vector`


   .. attribute:: zzyz

      :type: :class:`Vector`


   .. attribute:: zzz

      :type: :class:`Vector`


   .. attribute:: zzzw

      :type: :class:`Vector`


   .. attribute:: zzzx

      :type: :class:`Vector`


   .. attribute:: zzzy

      :type: :class:`Vector`


   .. attribute:: zzzz

      :type: :class:`Vector`




