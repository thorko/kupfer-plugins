__kupfer_name__ = _("Netflix")
__kupfer_actions__ = ("Netflix", )
__description__ = _("Search Netflix")
__version__ = "2018-9"
__author__ = "thorko"

from kupfer.objects import Action, TextLeaf
from kupfer import utils, plugin_support, config

_ALTERNATIVES = (
        "google-chrome-stable",
        "chromium",
        "firefox",
        "vivaldi",
)

__kupfer_settings__ = plugin_support.PluginSettings(
        {
            "key" : "browser_type",
            "label": _("Your browser to use"),
            "type": str,
            "value": "google-chrome-stable",
            "alternatives": _ALTERNATIVES,
        }
)


class Netflix (Action):
    def __init__(self):
        Action.__init__(self, _("Netflix"))

    def activate(self, leaf):
        browser_type = __kupfer_settings__["browser_type"]
        searchnetflix = [browser_type, 'https://www.netflix.com/search?q=%s' % leaf.object]
        utils.spawn_async(searchnetflix)

    def item_types(self):
        yield TextLeaf

    def get_description(self):
        return _("Search netflix with your browser")

    def get_icon_name(self):
        return "netflix"

