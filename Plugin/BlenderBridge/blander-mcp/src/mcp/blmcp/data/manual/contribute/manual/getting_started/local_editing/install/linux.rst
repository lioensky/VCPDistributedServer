.. highlight:: sh

*********************
Installation on Linux
*********************

This guide covers the following topics:

#. `Installing Dependencies`_
#. `Downloading the Repository`_
#. `Setting up the Build Environment`_


Installing Dependencies
=======================

Below are listed the installation commands for popular Linux distributions.

For the appropriate system, run the command in a terminal:

Debian/Ubuntu::

   sudo apt-get install python3 python3-pip git git-lfs
   git lfs install --skip-repo

Redhat/Fedora::

   sudo dnf install python python-pip git git-lfs
   git lfs install --skip-repo

Arch Linux::

   sudo pacman -S python python-pip git git-lfs
   git lfs install --skip-repo


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

   This avoids interfering with the system Python installation, following `PEP 668
   <https://peps.python.org/pep-0668/>`__

   The Sphinx command is available at::

      .venv/bin/sphinx-build
