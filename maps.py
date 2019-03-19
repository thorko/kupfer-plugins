__kupfer_name__ = _("Google Maps")
__kupfer_actions__ = ("GoogleMaps", )
__description__ = _("Search address in gmaps")
__version__ = "2019-3"
__author__ = "thorko"

import http.client
import urllib.parse

from kupfer.objects import Action, TextLeaf
from kupfer import utils, plugin_support, config

_ALTERNATIVES = (
        "Google",
)

URLS = { 
        "Google" : "https://www.google.com/maps/place/",
}

__kupfer_settings__ = plugin_support.PluginSettings(
        {
            "key": "search_engine",
            "label": _("Your search engine"),
            "type": str,
            "value": "Google",
            "alternatives": _ALTERNATIVES,
        }
)

class GoogleMaps (Action):
    def __init__(self):
        Action.__init__(self, _("Maps"))

    def activate(self, leaf):
        engine = __kupfer_settings__["search_engine"]
        query_url = URLS[engine] + "?" + urllib.parse.urlencode({"q": leaf.object})
        utils.show_url(query_url)

    def item_types(self):
        yield TextLeaf

    def get_description(self):
        return _("Search address with gmaps")

    def get_icon_name(self):
        return "edit-find"

