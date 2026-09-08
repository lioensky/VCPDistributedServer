.. highlight:: rst

*******************
Writing Style Guide
*******************

Primary Goals
=============

The main goals for this manual are as follows:

User Focused
   The manual is written for people educated in computer graphics, who understand the basics of 3D and/or know other
   3D software. While some areas of computer graphics are highly technical, this manual shall be kept understandable
   by non-technical users.
Complete
   The manual provides detailed functional description of all features, tools and options in Blender. While there is a
   canonical source of truth for each of Blender's key areas, this does not mean we have to document every small
   detail. The manual should provide information on what a feature is, how to use it, and its purpose. More background
   information should be provided when necessary to give deeper understanding of a 3D pipeline.
Concise
   Computer graphics is an incredibly interesting field. There are many rules, exceptions to those rules, and
   interesting details. However, expanding into details can add unnecessary content; therefore, keep the text concise
   and relevant to the end user.
Maintainable
   Keep in mind that Blender has frequent releases, so try to write content that will not have to be redone the moment
   some small change is made. This also helps a small documentation community maintain the manual.


Content Guidelines
==================

In order to maintain a consistent writing style within the manual, please keep this page in mind and only deviate from
it when you have a good reason to do so. If in doubt, check with the documentation team on Blender Chat.

Rules of thumb:

- Spell checking is *strongly* recommended.
- Use American English (e.g: modeling and not :abbr:`modelling`, color and not :abbr:`colour`) also for formatting
  numbers (e.g: 2,718.28 and not 2 718,28).
- Take care about grammar, appropriate wording and use simple English.
- Keep sentences short and clear.
- Including why or how an option might be useful is a good idea.
- If you are unsure about how a feature works, ask someone else or find out who developed it and ask them.
- RST files should wrap at column 120. No lines of text should exceed that length.

To be avoided:

- Avoid writing in the first person perspective, about yourself, or about your own opinions.
- Avoid `weasel words <https://en.wikipedia.org/wiki/Weasel_word>`__ and being unnecessarily vague, e.g:

  | "Reloading the file will probably fix the problem"
  | "Most people do not use this option because ..."
- Avoid including specific details such as:

  | "Blender has 23 different kinds of modifiers."
  | "Enabling previews adds 65536 bytes to the size of each blend-file (unless it is compressed)."

  These details are not useful for users and become quickly outdated.
- Avoid documenting bugs.

  Blender often has hundreds of bugs fixed between releases, so the manual cannot be expected to keep up.

  Issues that are known to the developers and are not going to be resolved before the next release can be documented
  as *Known Limitations*.
  In some cases, it may be best to include them in the :doc:`troubleshooting </troubleshooting/index>` section.
- Avoid product placements, e.g. unnecessarily promoting software or hardware brands. Keep content vendor-neutral
  where possible.
- Avoid technical explanations about the mathematical/algorithmic implementation of a feature if there is a simpler
  way to explain it.

  (E.g. explaining how mesh smoothing algorithms work is unnecessary, but the blending types of a Mix node do need a
  mathematical explanation.)
- Avoid repetition of large portions of text. Simply explain it once, and from then on refer to that explanation.

  For general terminology, consider defining a ``:term:`` in the :doc:`glossary </glossary/index>`.
- Avoid listing every option in a menu, such as frame rates.

  Their contents may be summarized or simply omitted. Such lists are only showing what is already *obvious* in the
  interface and end up being a lot of text to read and maintain.
- Avoid documenting changes in Blender between releases, that is what the release notes are for. We only need to
  document the current state of Blender.
- Unless the unit a value is measured in is obscure and unpredictable, there is no need to mention it.
- Do not simply copy the tooltips from Blender.

  People will come to the manual to learn *more* than is provided by the UI. As a last resort you can add comment
  (which is not shown in the HTML page, but useful for other editors)::

     .. TODO how does this tool work? ask Joe Blogg.


Glossary
--------

This section is specifically about the :doc:`Glossary </glossary/index>` section,
where we define common terms in Blender and computer graphics.

Rules of thumb:

- Define the term before providing any further information.
- Avoid using constructs such as "it is" or "xyz is" before the definition.
- Avoid repeating the term immediately or using it in the definition.
- Avoid adding terms not found in Blender's interface or the manual.
- Avoid overly long entries.
  If an explanation of a complex term is needed, supplement with external links.
- Avoid duplicating documentation;
  if explaining the term is the primary focus of another section of the manual
  (e.g. if the term is the name of a tool),
  either just link to that section, or avoid creating a glossary entry entirely.
- URL references are to be added at the end, formatted as follows, e.g::

     See also `OpenGL <https://en.wikipedia.org/wiki/OpenGL>`__ on Wikipedia.


Examples
^^^^^^^^

This entry::

   Displacement Mapping
      Uses a grayscale heightmap, like Bump Mapping,
      but the image is used to physically move the vertices of the mesh at render time.
      This is of course only useful if the mesh has large amounts of vertices.

Would be written like this instead, putting a definition first::

   Displacement Mapping
      Distorts vertices with an image.
      Similar to Bump Mapping, but operates on the mesh's geometry.
      The mesh must have enough geometry.

----

This entry::

   Doppler Effect
      The Doppler effect is the change in pitch that occurs
      when a sound has a velocity relative to the listener.

Would be written more like this, avoiding the immediate repetition of the term::

   Doppler Effect
      Perceived change in pitch that occurs
      when the source of a sound is moving relative to the listener.

----

This entry::

   Curve
      It is a class of objects.
      In Blender there are Bézier curves and NURBS curves.

Would be written more like this, avoiding the "it is"::

   Curve
      A line interpolated between Control Vertices.
      Common types include Bézier and NURBS.
