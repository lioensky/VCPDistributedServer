bpy_extras submodule (bpy_extras.asset_utils)
=============================================

.. module:: bpy_extras.asset_utils

Helpers for asset management tasks.

.. class:: AssetBrowserPanel

   Mixin class for panels that should only show in the asset browser.

   .. classmethod:: asset_browser_panel_poll(context)

      Check if the panel should be shown in the asset browser.
      
      :param context: The context.
      :type context: :class:`bpy.types.Context`
      :return: True when the panel should be visible.
      :rtype: bool

   .. classmethod:: poll(context)

      Poll for asset browser visibility.
      
      :param context: The context.
      :type context: :class:`bpy.types.Context`
      :return: True when the panel should be visible.
      :rtype: bool



.. class:: AssetMetaDataPanel

   Mixin class for panels that display asset metadata in the asset browser.

   .. classmethod:: poll(context)

      Poll for asset browser with active asset metadata.
      
      :param context: The context.
      :type context: :class:`bpy.types.Context`
      :return: True when the asset browser has active asset data.
      :rtype: bool



.. class:: SpaceAssetInfo

   Utility class for checking if a space is an asset browser.

   .. classmethod:: is_asset_browser(space_data)

      Check if the given space is an asset browser.
      
      :param space_data: The space to check.
      :type space_data: :class:`bpy.types.Space`
      :return: True when the space is an asset browser.
      :rtype: bool

   .. classmethod:: is_asset_browser_poll(context)

      Poll whether the active space is an asset browser.
      
      :param context: The context.
      :type context: :class:`bpy.types.Context`
      :return: True when the active space is an asset browser.
      :rtype: bool



