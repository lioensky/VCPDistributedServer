
*****
Plane
*****

.. reference::

   :Mode:      Sculpt Mode
   :Brush:     :menuselection:`Sidebar --> Tool --> Brush Settings --> Advanced --> Brush Type`

Moves vertices toward or away from the brush plane along its normal direction.

The *Plane* brush flattens geometry to a virtual plane
or raises the surface relative to it, depending on brush settings.
The *Height* and *Depth* parameters control the range of influence above and below the plane,
allowing precise shaping of flat surfaces or plateaus.


Brush Settings
==============

General
-------

.. note::

   More info at :ref:`sculpt-tool-settings-brush-settings-general` brush settings
   and on :ref:`sculpt-tool-settings-brush-settings-advanced` brush settings.


Unique
------

Height
   Determines the range of influence of the brush above the brush plane.
   Increasing the height affects vertices farther above the plane.

Depth
   Determines the range of influence of the brush below the brush plane.
   Increasing the depth affects vertices farther below the plane.

Inversion Mode
   Determines the behavior of the brush when inverted.

   Invert Displacement
      When inverted, the brush displaces vertices away from the brush plane, resulting in increased contrast.
   Swap Height and Depth
      When inverted, the roles of the *Height* and *Depth* parameters are exchanged.

      For example, if *Height* is set to 0.7 and *Depth* to 0.3, inverting the brush causes the roles of these
      parameters to be exchanged, resulting in an effective *Height* of 0.3 and *Depth* of 0.7.

Stabilize Normal
   Controls the stability of the brush plane's orientation. The normal of the plane is averaged over the last few
   stroke steps, with the number of steps and blending factor determined by the parameter's value.

   When set to 0, the brush reacts immediately to changes in the in surface orientation.

   When set to 1, the plane's orientation remains constant throughout the stroke.

   Intermediate values provide a gradual transition between these behaviors, resulting in a weighted moving average of
   plane normals.

Stabilize Plane
   Controls the stability of the brush plane's position. Similar to *Stabilize Normal*, it works by averaging the
   position over the previous stroke steps.

   Each position is calculated as the interpolated between the unstabilized position and its projection onto the plane
   of the previous stroke step.
