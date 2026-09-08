
*******************************
Troubleshooting Linux -- NVIDIA
*******************************

.. include:: ../common/introduction.rst
   :start-line: 1

On Linux, graphics drivers are usually installed as a package by your Linux distribution. Installing the latest
drivers is typically done by upgrading packages or the distribution as a whole. Some distributions provide multiple
packages for multiple drivers versions, giving you the choice to install newer versions.

For NVIDIA, there are open source (Nouveau) and closed source (by NVIDIA) graphics drivers. Blender functions best
with the closed source drivers as they are more optimized and complete. Linux graphics drivers can be downloaded from
NVIDIA's website, however in most cases the ones from your Linux distribution are fine and make things easier.
Manually downloading drivers is mostly useful to get the very latest version, for example for a GPU that was only
recently released.

Note, drivers before 550 do not support Vulkan!

`NVIDIA Website <https://www.nvidia.com/Download/index.aspx>`__

.. include:: ../common/laptops.rst
   :start-line: 1
.. include:: ../common/other.rst
   :start-line: 1
