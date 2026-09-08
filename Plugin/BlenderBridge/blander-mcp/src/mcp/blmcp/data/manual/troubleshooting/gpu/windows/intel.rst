
********************************
Troubleshooting Windows -- Intel
********************************

.. include:: ../common/introduction.rst
   :start-line: 1

On Windows, drivers are provided by the graphics card manufacturer (Intel). Windows Update automatically installs
graphics drivers, or your computer manufacturer may provide its own version of the graphics drivers.

However, these are not always the latest version or may have been corrupted in some way. We recommend always using
the official drivers.

`Download Latest Intel Drivers <https://www.intel.com/content/www/us/en/support/products/80939/graphics.html>`__

.. include:: ../common/laptops.rst
   :start-line: 1


Compatibility
=============

In some cases, Blender may crash on startup. Running Blender in compatibility mode can help in fixing this issue. To
enable compatibility mode, :kbd:`RMB` on the Blender executable and select :menuselection:`Properties -->
Compatibility` and enable :menuselection:`Run this program in compatibility mode`. Confirm the changes with *Apply*.

.. include:: ../common/other.rst
   :start-line: 1


Legacy Intel HD 4000/5000
=========================

When running on Intel 3rd, 4th or 5th gen iGPUs, the latest Intel driver will crash on startup. In order to start
Blender try to install a previous version of the driver. Drivers that are known to work are:

- 20.19.15.4835
- 20.19.15.4963
- 20.19.15.5063

Drivers that are known to fail are:

- 20.19.15.5126
- 20.19.15.5144
- 20.19.15.5166
- 20.19.15.5171

`Download older Intel Drivers <https://www.intel.com/content/www/us/en/support/articles/000089377/graphics.html>`__
