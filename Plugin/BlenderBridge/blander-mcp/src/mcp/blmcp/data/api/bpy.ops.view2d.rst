View2D Operators
================

.. module:: bpy.ops.view2d

.. function:: edge_pan(*, inside_padding=1.0, outside_padding=0.0, speed_ramp=1.0, max_speed=500.0, delay=1.0, zoom_influence=0.0)

   Pan the view when the mouse is held at an edge

   :param inside_padding: Inside Padding, Inside distance in UI units from the edge of the region within which to start panning (in [0, 100], optional)
   :type inside_padding: float
   :param outside_padding: Outside Padding, Outside distance in UI units from the edge of the region at which to stop panning (in [0, 100], optional)
   :type outside_padding: float
   :param speed_ramp: Speed Ramp, Width of the zone in UI units where speed increases with distance from the edge (in [0, 100], optional)
   :type speed_ramp: float
   :param max_speed: Max Speed, Maximum speed in UI units per second (in [0, 10000], optional)
   :type max_speed: float
   :param delay: Delay, Delay in seconds before maximum speed is reached (in [0, 10], optional)
   :type delay: float
   :param zoom_influence: Zoom Influence, Influence of the zoom factor on scroll speed (in [0, 1], optional)
   :type zoom_influence: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: pan(*, deltax=0, deltay=0)

   Pan the view

   :param deltax: Delta X, (in [-inf, inf], optional)
   :type deltax: int
   :param deltay: Delta Y, (in [-inf, inf], optional)
   :type deltay: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: reset()

   Reset the view

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: scroll_down(*, deltax=0, deltay=0, page=False)

   Scroll the view down

   :param deltax: Delta X, (in [-inf, inf], optional)
   :type deltax: int
   :param deltay: Delta Y, (in [-inf, inf], optional)
   :type deltay: int
   :param page: Page, Scroll down one page (optional)
   :type page: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: scroll_left(*, deltax=0, deltay=0)

   Scroll the view left

   :param deltax: Delta X, (in [-inf, inf], optional)
   :type deltax: int
   :param deltay: Delta Y, (in [-inf, inf], optional)
   :type deltay: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: scroll_right(*, deltax=0, deltay=0)

   Scroll the view right

   :param deltax: Delta X, (in [-inf, inf], optional)
   :type deltax: int
   :param deltay: Delta Y, (in [-inf, inf], optional)
   :type deltay: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: scroll_up(*, deltax=0, deltay=0, page=False)

   Scroll the view up

   :param deltax: Delta X, (in [-inf, inf], optional)
   :type deltax: int
   :param deltay: Delta Y, (in [-inf, inf], optional)
   :type deltay: int
   :param page: Page, Scroll up one page (optional)
   :type page: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: scroller_activate()

   Scroll view by mouse click and drag

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: smoothview(*, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :param xmin: X Min, (in [-inf, inf], optional)
   :type xmin: int
   :param xmax: X Max, (in [-inf, inf], optional)
   :type xmax: int
   :param ymin: Y Min, (in [-inf, inf], optional)
   :type ymin: int
   :param ymax: Y Max, (in [-inf, inf], optional)
   :type ymax: int
   :param wait_for_input: Wait for Input, (optional)
   :type wait_for_input: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: zoom(*, deltax=0.0, deltay=0.0, use_cursor_init=True)

   Zoom in/out the view

   :param deltax: Delta X, (in [-inf, inf], optional)
   :type deltax: float
   :param deltay: Delta Y, (in [-inf, inf], optional)
   :type deltay: float
   :param use_cursor_init: Use Mouse Position, Allow the initial mouse position to be used (optional)
   :type use_cursor_init: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: zoom_border(*, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, zoom_out=False)

   Zoom in the view to the nearest item contained in the border

   :param xmin: X Min, (in [-inf, inf], optional)
   :type xmin: int
   :param xmax: X Max, (in [-inf, inf], optional)
   :type xmax: int
   :param ymin: Y Min, (in [-inf, inf], optional)
   :type ymin: int
   :param ymax: Y Max, (in [-inf, inf], optional)
   :type ymax: int
   :param wait_for_input: Wait for Input, (optional)
   :type wait_for_input: bool
   :param zoom_out: Zoom Out, (optional)
   :type zoom_out: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: zoom_in(*, zoomfacx=0.0, zoomfacy=0.0)

   Zoom in the view

   :param zoomfacx: Zoom Factor X, (in [-inf, inf], optional)
   :type zoomfacx: float
   :param zoomfacy: Zoom Factor Y, (in [-inf, inf], optional)
   :type zoomfacy: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: zoom_out(*, zoomfacx=0.0, zoomfacy=0.0)

   Zoom out the view

   :param zoomfacx: Zoom Factor X, (in [-inf, inf], optional)
   :type zoomfacx: float
   :param zoomfacy: Zoom Factor Y, (in [-inf, inf], optional)
   :type zoomfacy: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

