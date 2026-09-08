
*******
Network
*******

.. Since adding extensions we have had many reports that accessing extensions fails.
   practically all of them relate to Python making outgoing SSL connections which
   can be blocked for all sorts of reasons.

   Common issues should be documented here.


403 Error Accessing Extensions
==============================

On systems or networks that use an additional layer of SSL management:
it's possible Blender's connection to ``https://extensions.blender.org`` is blocked.

In this case the problem can't be resolved in Blender's side,
it's up the system administrators to allow a connection to ``extensions.blender.org``.

See: `this report <https://projects.blender.org/blender/blender/issues/129681>`__.
