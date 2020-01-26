__kupfer_name__ = _("MovieTrailer")
__kupfer_actions__ = ("MovieTrailer", )
__description__ = _("Search MovieTrailer")
__version__ = "2020-1"
__author__ = "thorko"

import http.client
import urllib.parse
from kupfer.objects import Action, TextLeaf
from kupfer import utils, plugin_support, config

_ALTERNATIVES = (
        "german",
        "english",
        "spanish",
)

__kupfer_settings__ = plugin_support.PluginSettings(
        {
            "key": "language",
            "label": _("Your language for the trailer"),
            "type": str,
            "value": "german",
            "alternatives": _ALTERNATIVES,
        }
)

class MovieTrailer (Action):
    def __init__(self):
        Action.__init__(self, _("Trailer"))

    def activate(self, leaf):
        language = __kupfer_settings__["language"]
        query_url = "https://www.youtube.com/results?search_query=" + leaf.object + "+trailer+" + language
        utils.show_url(query_url)

    def item_types(self):
        yield TextLeaf

    def get_description(self):
        return __description__

    def get_icon_name(self):
        return "visibility"
