.. highlight:: sh

*************
Pull Requests
*************

This page describes the tools used for code contribution and review.

Reviews are a key measure to assure changes are of a good quality. They help preventing bugs, design consistencies, or
potential maintenance problems. And having your work reviewed also generally keeps you on your toes.

.. note::

   Writers who have been given commit access can commit to the main repository without needing to fork the repository.

   See :doc:`/contribute/manual/guides/commit_guide` if this applies to you.


One Time Setup
==============

This assumes you have the Blender manual repository already checked out on your computer, following the :doc:`install
instructions </contribute/manual/getting_started/local_editing/install/index>`.


Fork
----

#. Go to Blender repository and click the Fork button.
#. Confirm the fork with the default settings.
#. Now you will have to add your personal fork as a remote in your local git repository.
   Click *SSH* to see the correct URL, and then add it like this::

      git remote add me git@git.blender.org:<USERNAME>/blender-manual.git

.. note::

   In order to push to the fork repository, you need an SSH key. If you don't already have the file
   ``~/.ssh/id_rsa.pub``, there's a simple command to generate such keys which works on Linux, macOS, and in Git Bash
   on Windows::

      ssh-keygen

   This command will generate a private key id_rsa and a public key id_rsa.pub in ``~/.ssh``. The private key must
   never be shown or sent to anyone else to avoid compromising your account, but the public key is safe to share.

   The contents of ``~/.ssh/id_rsa.pub`` can be copied and pasted into the `account settings on projects.blender.org
   <https://projects.blender.org/user/settings/keys>`__, after clicking "Add Key". Any name for the SSH key is ok.


Workflow
========

The workflow for working with pull requests can be found in the
`Blender Developer's Documentation <https://developer.blender.org/docs/handbook/contributing/pull_requests/>`__.

Note, some text in the above guideline is focused on the main Blender repository, however, the workflow is the same
for any Blender project.


Guidelines for Reviewers
========================

- The pull request text should be usable as the git commit message (see the :ref:`guidelines
  <contribute-commit-good-message>` for details).
- Be explicit when some changes are to be addressed before committing, without the need for a review iteration.
- If the pull request is not approved the author is expected to make another iteration.
- If the change needs agreement on the design task first, put the pull request on hold by adding a ``WIP:`` prefix in
  the title, indicating the author considers the pull request not ready to be merged. No review is expected unless the
  author specifically asks for it.
- Writers are expected to reply to pull requests in 3 working days.
- Add relevant modules/projects to the labels.
- Encourage new writes to do review, it's a good way to learn and important to grow the project.


Tips
====

- To get the patch file, add .patch to the end of the URL of the pull request. Example::

     https://projects.blender.org/blender/blender-manual/pulls/104892.patch

- Checkout a pull request into a detached head (not leaving behind a branch). Example::

     git fetch -q origin +refs/pull/104892/head: ; git checkout -qf FETCH_HEAD
