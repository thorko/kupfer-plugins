__kupfer_name__ = _("AmazonPrime")
__kupfer_actions__ = ("AmazonPrime", )
__description__ = _("Search Amazon Prime")
__version__ = "2018-3"
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


class AmazonPrime (Action):
    def __init__(self):
        Action.__init__(self, _("AmazonPrime"))

    def activate(self, leaf):
        browser_type = __kupfer_settings__["browser_type"]
        searchamazon = [browser_type, 'https://www.amazon.de/s/ref=nb_sb_noss_2?__mk_de_DE=%%C3%%85M%%C3%%85%%C5%%BD%%C3%%95%%C3%%91&url=search-alias%%3Dinstant-video&field-keywords=%s' % leaf.object]
        utils.spawn_async(searchamazon)

    def item_types(self):
        yield TextLeaf

    def get_description(self):
        return _("Search amazon prime with your browser")

    def get_icon_name(self):
        return "amazonprime"

