__kupfer_name__ = _("Internet Search")
__kupfer_actions__ = ("InternetSearch", "Site")
__description__ = _("Search the internet with results shown in browser")
__version__ = "2017-1"
__author__ = "thorko"

import http.client
import urllib.parse

from kupfer.objects import Action, TextLeaf
from kupfer import utils, plugin_support, config

_ALTERNATIVES = (
        "Google",
        "DuckDuckGo",
        "Startpage",
        "Bing",
        "Qwant",
)

URLS = {
        "Google" : "https://www.google.com/search",
        "DuckDuckGo" : "https://duckduckgo.com",
        "Startpage" : "https://www.startpage.com/do/search",
        "Bing" : "https://www.bing.com/search",
        "Qwant" : "https://www.qwant.com/",
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

class InternetSearch (Action):
    def __init__(self):
        Action.__init__(self, _("Internet Search"))

    def activate(self, leaf):
        engine = __kupfer_settings__["search_engine"]
        query_url = URLS[engine] + "?" + urllib.parse.urlencode({"q": leaf.object})
        utils.show_url(query_url)

    def item_types(self):
        yield TextLeaf

    def get_description(self):
        return _("Search the web with google.com")

    def get_icon_name(self):
        return "edit-find"

class Site(Action):
    def __init__(self):
        Action.__init__(self, _("Open Site"))

    def activate(self, leaf):
        query_url = "http://" + leaf.object
        utils.show_url(query_url)

    def item_types(self):
        yield TextLeaf

    def get_description(self):
        return _("open the url in browser")

    def get_icon_name(self):
        return "applications-internet"
