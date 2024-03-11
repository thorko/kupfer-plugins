__kupfer_name__ = _("dict.cc")
__kupfer_actions__ = ("DictccSearch", )
__description__ = _("Translate from german to english with dict.cc")
__version__ = "2018-3"
__author__ = "thorko"

import http.client
import urllib.parse

from kupfer.obj import Action, TextLeaf
from kupfer import launch

class DictccSearch (Action):
    def __init__(self):
        Action.__init__(self, _("dict.cc"))

    def activate(self, leaf):
        search_url = "https://www.dict.cc/"
        query_url = search_url + "?" + urllib.parse.urlencode({"s": leaf.object})
        launch.show_url(query_url)

    def item_types(self):
        yield TextLeaf

    def get_description(self):
        return _("Translate from germant to english with dict.cc")

    def get_icon_name(self):
        return "dictcc"
