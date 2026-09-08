Application Translations (bpy.app.translations)
===============================================

.. module:: bpy.app.translations

This object contains some data/methods regarding internationalization in Blender, and allows every py script
to feature translations for its own UI messages.


Introduction
------------

.. warning::

   Most of this object should only be useful if you actually manipulate i18n stuff from Python.
   If you are a regular add-on, you should only bother about :const:`contexts` member,
   and the :func:`register`/:func:`unregister` functions! The :func:`pgettext` family of functions
   should only be used in rare, specific cases (like e.g. complex "composited" UI strings...).

To add translations to your Python script, you must define a dictionary formatted like that:
``{locale: {msg_key: msg_translation, ...}, ...}`` where:

- locale is either a lang ISO code (e.g. ``fr``), a lang+country code (e.g. ``pt_BR``),
  a lang+variant code (e.g. ``sr@latin``), or a full code (e.g. ``uz_UZ@cyrilic``).
- msg_key is a tuple (context, org message) - use, as much as possible, the predefined :const:`contexts`.
- msg_translation is the translated message in given language!

Then, call ``bpy.app.translations.register(__name__, your_dict)`` in your ``register()`` function, and
``bpy.app.translations.unregister(__name__)`` in your ``unregister()`` one.

The ``Manage UI translations`` add-on has several functions to help you collect strings to translate, and
generate the needed Python code (the translation dictionary), as well as optional intermediary po files
if you want some... See
`How to Translate Blender <https://developer.blender.org/docs/handbook/translating/translator_guide/>`_ and
`Using i18n in Blender Code <https://developer.blender.org/docs/handbook/translating/developer_guide/>`_
for more info.

Module References
-----------------

.. literalinclude:: ./examples/bpy.app.translations.0.py
   :lines: 35-

.. data:: locale

   The actual locale currently in use (will always return an empty string when Blender is built without internationalization support).


.. data:: locales

   All locales currently known by Blender (i.e. available as translations).


.. data:: contexts_C_to_py

   A readonly dict mapping contexts' C-identifiers to their py-identifiers.


.. data:: contexts

   Constant value bpy.app.translations.contexts(default_real=None, default='*', operator_default='Operator', ui_events_keymaps='UI_Events_KeyMaps', plural='Plural', countable='Countable', id_action='Action', id_armature='Armature', no_translation='Do not translate', id_brush='Brush', id_cachefile='CacheFile', id_camera='Camera', id_collection='Collection', id_curves='Curves', id_curve='Curve', id_fs_linestyle='FreestyleLineStyle', id_gpencil='GPencil', id_id='ID', id_image='Image', id_lattice='Lattice', id_library='Library', id_light='Light', id_lightprobe='LightProbe', id_mask='Mask', id_material='Material', id_mesh='Mesh', id_metaball='Metaball', id_movieclip='MovieClip', id_nodetree='NodeTree', id_object='Object', id_paintcurve='PaintCurve', id_palette='Palette', id_particlesettings='ParticleSettings', id_pointcloud='PointCloud', id_scene='Scene', id_screen='Screen', id_sequence='Sequence', id_shapekey='Key', id_simulation='Simulation', id_sound='Sound', id_speaker='Speaker', id_text='Text', id_texture='Texture', id_vfont='VFont', id_volume='Volume', id_windowmanager='WindowManager', id_workspace='WorkSpace', id_world='World', editor_filebrowser='File browser', editor_python_console='Python console', editor_preferences='Preferences', editor_view3d='View3D', amount='Amount', color='Color', constraint='Constraint', modifier='Modifier', navigation='Navigation', render_layer='Render Layer', time='Time', unit='Unit')

.. method:: locale_explode(locale)

   Return all components and their combinations of the given ISO locale string.

   >>> bpy.app.translations.locale_explode("sr_RS@latin")
   ("sr", "RS", "latin", "sr_RS", "sr@latin")

   For non-complete locales, missing elements will be None.

   :param locale: The ISO locale string to explode.
   :type locale: str
   :return: A tuple ``(language, country, variant, language_country, language@variant)``.
   :rtype: tuple[str | None, str | None, str | None, str | None, str | None]


.. method:: pgettext(msgid, msgctxt=None)

   Try to translate the given msgid (with optional msgctxt).

   .. note::
      The ``(msgid, msgctxt)`` parameters order has been switched compared to gettext function, to allow
      single-parameter calls (context then defaults to BLT_I18NCONTEXT_DEFAULT).

   .. note::
      You should really rarely need to use this function in regular addon code, as all translation should be
      handled by Blender internal code. The only exceptions are strings containing formatting (like "File: %r"),
      but you should rather use :func:`pgettext_iface`/:func:`pgettext_tip` in those cases!

   .. note::
      Does nothing when Blender is built without internationalization support (hence always returns ``msgid``).

   :param msgid: The string to translate.
   :type msgid: str
   :param msgctxt: The translation context (defaults to BLT_I18NCONTEXT_DEFAULT).
   :type msgctxt: str | None
   :return: The translated string (or msgid if no translation was found).
   :rtype: str


.. method:: pgettext_data(msgid, msgctxt=None)

   Try to translate the given msgid (with optional msgctxt), if new data name's translation is enabled.

   .. note::
      See :func:`pgettext` notes.

   :param msgid: The string to translate.
   :type msgid: str
   :param msgctxt: The translation context (defaults to BLT_I18NCONTEXT_DEFAULT).
   :type msgctxt: str | None
   :return: The translated string (or ``msgid`` if no translation was found).
   :rtype: str


.. method:: pgettext_iface(msgid, msgctxt=None)

   Try to translate the given msgid (with optional msgctxt), if labels' translation is enabled.

   .. note::
      See :func:`pgettext` notes.

   :param msgid: The string to translate.
   :type msgid: str
   :param msgctxt: The translation context (defaults to BLT_I18NCONTEXT_DEFAULT).
   :type msgctxt: str | None
   :return: The translated string (or msgid if no translation was found).
   :rtype: str


.. method:: pgettext_n(msgid, msgctxt=None)

   Extract the given msgid to translation files. This is a no-op function that will only mark the string to extract, but not perform the actual translation.

   .. note::
      See :func:`pgettext` notes.

   :param msgid: The string to extract.
   :type msgid: str
   :param msgctxt: The translation context (defaults to BLT_I18NCONTEXT_DEFAULT).
   :type msgctxt: str | None
   :return: The original string.
   :rtype: str


.. method:: pgettext_rpt(msgid, msgctxt=None)

   Try to translate the given msgid (with optional msgctxt), if reports' translation is enabled.

   .. note::
      See :func:`pgettext` notes.

   :param msgid: The string to translate.
   :type msgid: str
   :param msgctxt: The translation context (defaults to BLT_I18NCONTEXT_DEFAULT).
   :type msgctxt: str | None
   :return: The translated string (or msgid if no translation was found).
   :rtype: str


.. method:: pgettext_tip(msgid, msgctxt=None)

   Try to translate the given msgid (with optional msgctxt), if tooltips' translation is enabled.

   .. note::
      See :func:`pgettext` notes.

   :param msgid: The string to translate.
   :type msgid: str
   :param msgctxt: The translation context (defaults to BLT_I18NCONTEXT_DEFAULT).
   :type msgctxt: str | None
   :return: The translated string (or msgid if no translation was found).
   :rtype: str


.. method:: register(module_name, translations_dict)

   Registers an addon's UI translations.

   .. note::
      Does nothing when Blender is built without internationalization support.

   :param module_name: The name identifying the addon.
   :type module_name: str
   :param translations_dict: A dictionary built like that:
      ``{locale: {msg_key: msg_translation, ...}, ...}``
   :type translations_dict: dict[str, dict[tuple[str, str], str]]


.. method:: unregister(module_name)

   Unregisters an addon's UI translations.

   .. note::
      Does nothing when Blender is built without internationalization support.

   :param module_name: The name identifying the addon.
   :type module_name: str


