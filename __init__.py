# __init__.py

import octoprint.plugin
from octoprint.server.util.flask import restricted_access
from octoprint.server import user_permission

class FilamentManagerPlugin(octoprint.plugin.StartupPlugin,
                            octoprint.plugin.TemplatePlugin,
                            octoprint.plugin.SettingsPlugin,
                            octoprint.plugin.AssetPlugin):

    def on_after_startup(self):
        self._logger.info("Filament Manager Plugin initialized")

    def get_settings_defaults(self):
        return dict(
            filaments=[]
        )

    def get_template_configs(self):
        return [
            dict(type="sidebar", name="Filament Manager", icon="fa-cube", custom_bindings=True),
        ]

    def get_assets(self):
        return dict(
            js=["js/scripts.js"],
            css=["css/styles.css"]
        )

    def get_custom_bindings(self):
        return dict(
            type="settings",
            template="filament_manager_settings.jinja2",
            custom_bindings=True
        )

    @restricted_access
    def on_api_get(self, request):
        return self._settings.get(["filaments"])

    @restricted_access
    def on_api_post(self, request):
        data = request.json
        filaments = self._settings.get(["filaments"])
        filaments.append(data)
        self._settings.set(["filaments"], filaments)
        self._settings.save()
        return {"success": True}

    @restricted_access
    def on_api_delete(self, request):
        data = request.json
        filaments = self._settings.get(["filaments"])
        filaments = [f for f in filaments if f["name"] != data["name"]]
        self._settings.set(["filaments"], filaments)
        self._settings.save()
        return {"success": True}

__plugin_name__ = "Filament Manager"
__plugin_version__ = "0.1.0"
__plugin_description__ = "Manage filaments used in your prints"
__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = FilamentManagerPlugin()

