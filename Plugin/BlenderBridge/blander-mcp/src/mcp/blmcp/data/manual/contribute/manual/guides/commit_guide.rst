

*****************
Commit Guidelines
*****************

Access to directly submit changes is limited to people with commit access to the repository. Once you are provided
with commit access you can start committing directly instead of creating a patch file.

You can make commits from your Git client or using the Git command line tool. The following command will create a
commit and send it to the central repository::

   git commit -m "This is what I did"
   git push

If you leave out ``-m "message"``, you will be prompted to type the message in a text editor.

.. tip::

   You should make sure you are always on the latest revision before committing. You may not be able to commit
   directly if there are conflicting changes in the latest revision.

   To avoid this update your local repository before committing (run ``make update``).

.. seealso::

   `Blender's Git usage guide <https://developer.blender.org/docs/handbook/contributing/using_git/>`__

.. seealso::

   See `release branch <https://developer.blender.org/docs/handbook/release_process/release_branch/>`__ for
   documentation on how to make commits to a specific release branch and how to create merge commits.

.. _contribute-commit-good-message:

Writing a Good Commit Message
=============================

When making changes to the manual that directly relate to a specific commit (change) in Blender, it is helpful to make
the title of the commit the same as the commit made to Blender. It is requested that you include the commit hash of
the commit made to the Blender source code.

For example, the commit `rBM8473 <https://developer.blender.org/rBM8473>`__ includes a descriptive indicative of the
changes made along with the hash ``rBa71d2b260170``. The hash can be extracted from the URL provided in the
Documentation task for a specific upcoming release.

----

Other more general changes do not have to follow the above policy however, it is still important to make the
description clear about what changes you made and why. It can be helpful to prefix the commit title with a prefix word
such as ``Cleanup:`` or ``Fix:`` when you are making general cleanups or fixes respectively.

Writing good commit messages helps administrators keep track of changes made and ensures all new features are properly
documented.
