
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  Blender |BLENDER_VERSION_LABEL| Reference Manual
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Welcome to the manual for `Blender <https://www.blender.org>`__,
the free and open source 3D creation suite.

.. see #64071 for why we don't use ':download:'

.. only:: builder_html

   This site can be used offline:

   - `Download the manual as web pages (HTML) <blender_manual_html.zip>`__
   - `Download the manual in an e-book format (EPUB) <blender_manual_epub.zip>`__


Getting Started
===============

.. only:: builder_html and (not singlehtml)

   .. container:: toc-cards

      .. container:: card

         :doc:`/getting_started/about/index`

      .. container:: card

         :doc:`/getting_started/installing/index`

      .. container:: card

         :doc:`/getting_started/configuration/index`

      .. container:: card

         :doc:`/getting_started/help`

.. container:: global-index-toc

   .. toctree::
      :caption: Getting Started
      :maxdepth: 1

      getting_started/about/index.rst
      getting_started/installing/index.rst
      getting_started/configuration/index.rst
      getting_started/help.rst


Sections
========

.. only:: builder_html and (not singlehtml)

   .. container:: toc-cards

      .. container:: card

         .. figure:: /images/index_interface.jpg
            :target: interface/index.html

         :doc:`/interface/index`
            An introduction to Blender's window system, widgets and tools.

      .. container:: card

         .. figure:: /images/index_editors.jpg
            :target: editors/index.html

         :doc:`/editors/index`
            Overview of the interface and functionality of all editors.

      .. container:: card

         .. figure:: /images/index_scene.jpg
            :target: scene_layout/index.html

         :doc:`/scene_layout/index`
            Objects and their organization into scenes, view layers and collections.

      .. container:: card

         .. figure:: /images/index_modeling.jpg
            :target: modeling/index.html

         :doc:`/modeling/index`
            Meshes, curves, metaballs, text, modeling tools, and modifiers.

      .. container:: card

         .. figure:: /images/index_painting.jpg
            :target: sculpt_paint/index.html

         :doc:`/sculpt_paint/index`
            Sculpting, texture painting and vertex painting.

      .. container:: card

         .. figure:: /images/index_grease-pencil.jpg
            :target: grease_pencil/index.html

         :doc:`/grease_pencil/index`
            2D drawing and animation with Grease Pencil.

      .. container:: card

         .. figure:: /images/index_animation.jpg
            :target: animation/index.html

         :doc:`/animation/index`
            Keyframes, drivers, constraints, armatures and shape keys.

      .. container:: card

         .. figure:: /images/index_physics.jpg
            :target: physics/index.html

         :doc:`/physics/index`
            Physics simulations, particle systems and dynamic paint.

      .. container:: card

         .. figure:: /images/index_render.jpg
            :target: render/index.html

         :doc:`/render/index`
            Rendering and shading with EEVEE, Cycles and Freestyle.

      .. container:: card

         .. figure:: /images/index_compositing.jpg
            :target: compositing/index.html

         :doc:`/compositing/index`
            Post-processing with the compositing nodes.

      .. container:: card

         .. figure:: /images/index_movie-clip.jpg
            :target: movie_clip/index.html

         :doc:`/movie_clip/index`
            Video motion tracking & masking.

      .. container:: card

         .. figure:: /images/index_sequencer.jpg
            :target: video_editing/index.html

         :doc:`/video_editing/index`
            Video editing with the sequencer.

      .. container:: card

         :doc:`/files/index`
            Data-block management and the structure of blend-files.

      .. container:: card

         :doc:`/addons/index`
            Additional functionality available as add-ons.

      .. container:: card

         :doc:`/advanced/index`
            Python scripting, how to write add-ons and a reference for command-line arguments.

      .. container:: card

         :doc:`/troubleshooting/index`
            Solving crashes, graphics issues and Python errors, recovering data and reporting bugs.

      .. container:: card

         :doc:`Glossary </glossary/index>`
            A list of terms and definitions used in Blender and this manual.

      .. container:: card

         :ref:`Manual Index <genindex>`
            A list of terms linked to the Glossary.

.. container:: global-index-toc

   .. toctree::
      :caption: Sections
      :maxdepth: 2

      interface/index.rst
      editors/index.rst
      scene_layout/index.rst
      modeling/index.rst
      sculpt_paint/index.rst
      grease_pencil/index.rst
      animation/index.rst
      physics/index.rst
      render/index.rst
      compositing/index.rst
      movie_clip/index.rst
      video_editing/index.rst
      files/index.rst
      addons/index.rst
      advanced/index.rst
      troubleshooting/index.rst
      glossary/index.rst
      Manual Index <genindex.rst>


Get Involved
============

Help write Blender's future! ✏️ Contribute to the Blender Manual and share your knowledge with creators worldwide.
No matter your expertise, your contributions can make Blender easier to learn and use for everyone.
Join the team and :ref:`start documenting Blender <about-user-contribute>` today!

.. rubric:: Translations

Help bring Blender to the world! 🌍
Join the translation effort to make the Blender accessible in more languages.

- :doc:`Translate Blender's UI </contribute/translate_blender>`
- :doc:`Translate Blender's User Manual  </contribute/translate_manual/index>`

.. just so this is included in the toc (not user visible).

.. toctree::
   :caption: Get Involved
   :maxdepth: 1
   :hidden:

   contribute/manual/index.rst
   contribute/translate_blender.rst
   contribute/translate_manual/index.rst
