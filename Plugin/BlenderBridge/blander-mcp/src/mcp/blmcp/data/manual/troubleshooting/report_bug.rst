
***************
Reporting a Bug
***************

The best way to help the Blender team to fix a bug is to report the bug using the proper process.

Before Reporting
================

Before reporting a bug, some basic steps should be taken to ensure that you are reporting a real issue.

- Ensure you have installed Blender according to the guidance in this manual under
  :doc:`/getting_started/installing/index`.
- Follow the steps in this Troubleshooting section first, starting with loading factory settings. Many crashes and
  errors may be caused by bad settings or add-ons that have not been updated to work with the newest release of
  Blender.

.. admonition:: Registration Required

   If this is your first time using one of the Blender Projects sites, you will be required to register a new Blender
   ID before you can file a bug report. The screen will guide you through the process.


Report from within Blender
==========================

It is recommended to initiate your bug report from within Blender. Doing so allows Blender to automatically populate
a number of fields in the bug report template including your computer configuration, operating system, and specific
Blender build.

To initiate a bug report:

- Select :menuselection:`Topbar --> Help --> Report a Bug` from the menu.  This will open your default web browser to
  the bug reporting page on blender.org with some of your information prepopulated.
- Give the bug a clear, easy-to-understand title - try to avoid long run-on sentences.
- Enter details about the steps to reproduce the bug. Bugs that are not consistently reproducible may be more
  difficult to track down, so provide any additional information that you can.  Make sure to fill in the **Short
  description of error** and the **Exact steps for others to reproduce the error** sections.
- Attach any pictures if you feel they will help the developers understand the issue more clearly. Videos can also be
  attached, but please only do so if it is absolutely required to show the issue.
- If a crash occurs, attach a crash log as discussed below: `Attaching a Crash Log`_.


.. note::
    If Blender crashes before fully starting, this process will not work for you. In that case, you will need to
    manually `Report on the Web`_.

Report on the Web
=================

The process here is similar to reporting from within Blender, with the added step of specifying details about your
computer.

To initiate a bug report:

- Open the bug reporting template on `projects.blender.org
  <https://projects.blender.org/blender/blender/issues/new?template=.gitea/issue_template/bug.yaml>`__.
- Give the bug a clear, easy-to-understand title - try to avoid long run-on sentences.
- Specify details about your computer and operating system in the **System Information** and **Blender Version**
  sections.
- Enter details about the steps to reproduce the bug. Bugs that are not consistently reproducible may be more
  difficult to track down, so provide any additional information that you can.  Make sure to fill in the **Short
  description of error** and the **Exact steps for others to reproduce the error** sections.
- Attach any pictures if you feel they will help the developers understand the issue more clearly. Videos can also be
  attached, but please only do so if it is absolutely required to show the issue.
- If a crash occurs, attach a crash log as discussed below: `Attaching a Crash Log`_.

Attaching a Crash Log
=====================

Attaching a crash log to your bug report (in the case of a hard crash) may help the development team to identify the
problem more easily. Follow the directions in :doc:`Crashes <crash>` to locate the text file and upload it to the bug
report.