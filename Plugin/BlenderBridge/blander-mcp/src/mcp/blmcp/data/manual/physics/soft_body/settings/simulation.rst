
**********
Simulation
**********

.. _bpy.types.SoftBodySettings.speed:

Speed
   You can control the internal timing of the soft body system with this value.
   It sets the correlation between frame rate and tempo of the simulation.
   A free falling body should cover a distance of about five meters after
   one second and travel at a speed of ten meters per seconds.

   You can adjust the scale of your scene and simulation with this correlation.
   If you render with 25 frames per second, you will have to set *Speed* to 1.3.
