.. highlight:: sh

******************
Editing the Manual
******************

You can modify the manual by editing local text files. These files are kept in sync with those online via a
repository, based on this the server will update the online manual.

The manual is written in the `reStructuredText
<https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`__ (RST) markup language and can be edited
using a plain text editor. For a local preview, you convert (build) the manual source files from RST into HTML web
pages.


Update
======

Firstly, make sure that your local copy of the manual is up to date with the online repository using::

   make update


Writing
=======

You can now edit the documentation files, which are the ``.rst`` files inside the ``manual`` folder using a text
editor of your choice.

Be sure to check the :doc:`/contribute/manual/guides/writing_guide` for conventions and
:doc:`/contribute/manual/guides/markup_guide` to learn how to write in the reStructuredText markup language.

Happy writing!


Bigger Changes
--------------

If you are going to add or overhaul a section, be sure to check carefully that it does not already exist. In some
places, the docs are so disorganized that sections may be duplicated or in a strange location. In the case that you
find a duplicate or out of place section, `create an issue
<https://projects.blender.org/blender/documentation/issues/new>`__ explaining the issue, and optionally include a
revision (actual changes).

Before you make any edits that are not simple and plainly justified (for example, moving folders around), you should
verify with a manual maintainer that your contribution is along the community's vision for the manual. This ensures
the best use of your time and good will as it is otherwise possible that, for some reason, your changes will conflict
and be rejected or need time-consuming review. For example, another person may be already working on the section you
wish to change, the section may be scheduled for deletion or to be updated according to a planned change to Blender.

:ref:`Communicating <contribute-contact>` early and frequently is the key to have a productive environment, to not
waste people's effort and to attain a better Blender manual as a result.

..
   Communication is a very important step in community development.
   Manual maintainers and the general community can also point to areas that are in need of big or small changes.


Getting Help/Answers
--------------------

If you are in doubt about functionality that you wish to document, you should pose your questions to the Blender
developers responsible for that area or ask at the unofficial user support channel in the ``#docs`` or
``#blender-coders`` channel in :ref:`blender-chat`.

Blender itself has a system of module owners with developer and artist members who are responsible for the design and
maintenance of the assigned Blender areas. See the `module pages
<https://projects.blender.org/blender/blender/wiki>`__ for more information.


Preview
=======

To view your changes, build the manual :doc:`as instructed </contribute/manual/getting_started/local_editing/build>`.
Keep in mind that you can also build only the chapter you just edited to view it quickly.
Open the generated ``.html`` files inside the ``build/html`` folder using your web browser,
or refresh the page if you have it open already.


Upload
======

When you are happy with your changes, you can upload them, so that they will be in the online manual. At first, this
is done by submitting patches so that someone can review your changes and give you feedback. After, you can commit
your changes directly. This process is described in detail in the next section.
