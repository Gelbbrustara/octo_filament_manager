# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
import sqlite3

class FilamentManagerPlugin(octoprint.plugin.StartupPlugin,
                            octoprint.plugin.TemplatePlugin,
                            octoprint.plugin.SettingsPlugin):

    def on_after_startup(self):
        self._logger.info("Filament Manager Plugin started")

    def get_settings_defaults(self):
        return dict(
            filament_data=[]
        )

    def get_template_configs(self):
        return [
            dict(type="navbar", custom_bindings=False),
            dict(type="settings", custom_bindings=False)
        ]

    def on_settings_save(self, data):
        octoprint.plugin.SettingsPlugin.on_settings_save(self, data)
        # Custom save logic here

__plugin_name__ = "Filament Manager"
__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = FilamentManagerPlugin()
