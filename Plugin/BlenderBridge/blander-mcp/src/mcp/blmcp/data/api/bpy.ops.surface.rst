Surface Operators
=================

.. module:: bpy.ops.surface

.. function:: primitive_nurbs_surface_circle_add(*, radius=1.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Construct a NURBS surface circle

   :param radius: Radius, (in [0, inf], optional)
   :type radius: float
   :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object (optional)
   :type enter_editmode: bool
   :param align: Align, The alignment of the new object (optional)

      - ``WORLD``
        World -- Align the new object to the world.
      - ``VIEW``
        View -- Align the new object to the view.
      - ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: Literal['WORLD', 'VIEW', 'CURSOR']
   :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type rotation: :class:`mathutils.Euler` | Sequence[float]
   :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type scale: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: primitive_nurbs_surface_curve_add(*, radius=1.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Construct a NURBS surface curve

   :param radius: Radius, (in [0, inf], optional)
   :type radius: float
   :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object (optional)
   :type enter_editmode: bool
   :param align: Align, The alignment of the new object (optional)

      - ``WORLD``
        World -- Align the new object to the world.
      - ``VIEW``
        View -- Align the new object to the view.
      - ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: Literal['WORLD', 'VIEW', 'CURSOR']
   :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type rotation: :class:`mathutils.Euler` | Sequence[float]
   :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type scale: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: primitive_nurbs_surface_cylinder_add(*, radius=1.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Construct a NURBS surface cylinder

   :param radius: Radius, (in [0, inf], optional)
   :type radius: float
   :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object (optional)
   :type enter_editmode: bool
   :param align: Align, The alignment of the new object (optional)

      - ``WORLD``
        World -- Align the new object to the world.
      - ``VIEW``
        View -- Align the new object to the view.
      - ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: Literal['WORLD', 'VIEW', 'CURSOR']
   :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type rotation: :class:`mathutils.Euler` | Sequence[float]
   :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type scale: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: primitive_nurbs_surface_sphere_add(*, radius=1.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Construct a NURBS surface sphere

   :param radius: Radius, (in [0, inf], optional)
   :type radius: float
   :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object (optional)
   :type enter_editmode: bool
   :param align: Align, The alignment of the new object (optional)

      - ``WORLD``
        World -- Align the new object to the world.
      - ``VIEW``
        View -- Align the new object to the view.
      - ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: Literal['WORLD', 'VIEW', 'CURSOR']
   :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type rotation: :class:`mathutils.Euler` | Sequence[float]
   :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type scale: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: primitive_nurbs_surface_surface_add(*, radius=1.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Construct a NURBS surface patch

   :param radius: Radius, (in [0, inf], optional)
   :type radius: float
   :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object (optional)
   :type enter_editmode: bool
   :param align: Align, The alignment of the new object (optional)

      - ``WORLD``
        World -- Align the new object to the world.
      - ``VIEW``
        View -- Align the new object to the view.
      - ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: Literal['WORLD', 'VIEW', 'CURSOR']
   :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type rotation: :class:`mathutils.Euler` | Sequence[float]
   :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type scale: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: primitive_nurbs_surface_torus_add(*, radius=1.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Construct a NURBS surface torus

   :param radius: Radius, (in [0, inf], optional)
   :type radius: float
   :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object (optional)
   :type enter_editmode: bool
   :param align: Align, The alignment of the new object (optional)

      - ``WORLD``
        World -- Align the new object to the world.
      - ``VIEW``
        View -- Align the new object to the view.
      - ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: Literal['WORLD', 'VIEW', 'CURSOR']
   :param location: Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type location: :class:`mathutils.Vector` | Sequence[float]
   :param rotation: Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type rotation: :class:`mathutils.Euler` | Sequence[float]
   :param scale: Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
   :type scale: :class:`mathutils.Vector` | Sequence[float]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

