.. highlight:: sh

*********************
Installation on macOS
*********************

This guide covers the following topics:

#. `Installing Dependencies`_
#. `Downloading the Repository`_
#. `Setting up the Build Environment`_

.. note::

   This guide relies heavily on command-line tools. It assumes you are the least familiar with the macOS Terminal
   application.


Installing Dependencies
=======================

Install those packages or make sure you have them in your system.

- `PIP <https://pip.pypa.io/en/latest/installing/>`__
- `Git <https://git-scm.com/download/mac>`__
- `Git LFS <https://git-lfs.com>`__

When using `Homebrew <https://brew.sh>`__, run the following commands in the terminal::

   python3 -m ensurepip
   brew install git git-lfs
   git lfs install


Downloading the Repository
==========================

Simply check out the Blender Manual's repository using::

   cd ~
   git clone https://projects.blender.org/blender/blender-manual.git

The repository will now be downloaded which may take a few minutes depending on your internet connection.


Setting up the Build Environment
================================

- Open a Terminal window.
- Enter the ``blender-manual`` folder which was just added by ``git clone``::

     cd ~/blender-manual

- Install dependencies::

     make setup

.. note::

   Every now and then you need to re-run this command, to make sure dependencies are up to date.

.. tip::

   ``make setup`` automatically creates a virtual environment using these commands::

      python3 -m venv .venv
      .venv/bin/pip install -r requirements.txt

   This avoids interfering with the system Python installation, following `PEP 668 <https://peps.python.org/pep-0668/>`__

   The Sphinx command is available at::

      .venv/bin/sphinx-build
