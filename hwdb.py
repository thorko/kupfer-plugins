__kupfer_name__ = _("HwDB")
__kupfer_actions__ = ("HwDB", )
__description__ = _("Search hwdb")
__version__ = "2018-6"
__author__ = "thorko"

from kupfer.objects import Action, TextLeaf
from kupfer import utils, plugin_support, config
import re

_ALTERNATIVES = (
        "google-chrome-stable",
        "chromium",
        "firefox",
        "vivaldi-stable",
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


class HwDB (Action):
    def __init__(self):
        Action.__init__(self, _("HwDB"))

    def activate(self, leaf):
        browser_type = __kupfer_settings__["browser_type"]
        p = re.compile("^x")
        r = p.match(leaf.object)
        if r != None:
            searchhwdb = [browser_type, 'https://nannyfe.prod.denic.de/search?Search=Search&searchpattern=%s' % leaf.object]
        else:
            searchhwdb = [browser_type, 'https://nannyfe.prod.denic.de/host/%s' % leaf.object]
        utils.spawn_async(searchhwdb)

    def item_types(self):
        yield TextLeaf

    def get_description(self):
        return _("Search hwdb in browser")

    def get_icon_name(self):
        return "hwdb"

