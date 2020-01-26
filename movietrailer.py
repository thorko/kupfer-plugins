__kupfer_name__ = _("MovieTrailer")
__kupfer_actions__ = ("MovieTrailer", )
__description__ = _("Search MovieTrailer")
__version__ = "2020-1"
__author__ = "thorko"

import http.client
import urllib.parse
from kupfer.objects import Action, TextLeaf
from kupfer import utils, plugin_support, config

class MovieTrailer (Action):
    def __init__(self):
        Action.__init__(self, _("Trailer"))

    def activate(self, leaf):
        query_url = "https://www.youtube.com/results?search_query=" + leaf.object + "+trailer+german"
        utils.show_url(query_url)

    def item_types(self):
        yield TextLeaf

    def get_description(self):
        return __description__

    def get_icon_name(self):
        return "visibility"
