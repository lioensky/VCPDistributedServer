.. _extensions-create_repo-dynamic:

****************************************
Creating a Dynamic Extensions Repository
****************************************

A dynamic repository allows you to serve a smaller JSON file with only the latest version
of the extensions which are compatible with the query parameters.
This is only relevant for repositories which contain multiple version of multiple extensions.

For small or personal repositories it is simpler and recommended to use
:doc:`static repositories <static_repository>` instead.

Listing
=======

To setup a dynamic extensions repository, follow the steps for :doc:`static repositories <static_repository>`,
since the format and the listing are the same.

Query Parameters
================

When Blender fetches the extensions listing it passes the following arguments to make sure only
compatible extensions are listed:

- ``platform``
- ``blender_version``

These arguments are passed as parameters to the server via a query URL:

   :URL: ``https://extensions.blender.org/api/v1/extensions/``
   :query URL: ``https://extensions.blender.org/api/v1/extensions/?blender_version=4.2.0&platform=linux-x64``


Access Token
============

Some repositories may require authentication. The user can specify an ``access token`` for a repository,
which is passed along with the API request from Blender.

This is passed to the servers via an Authorization header:

.. code-block:: sh

   curl -i https://extensions.blender.org/api/v1/extensions/ \
        -H "Accept: application/json" \
        -H "Authorization: Bearer abc29832befb92983423abcaef93001"
