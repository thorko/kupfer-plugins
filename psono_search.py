__kupfer_name__ = _("Psono Search")
__kupfer_actions__ = ("PsonoSearch", "Site")
__description__ = _("Search the psono password manager")
__version__ = "2022-1"
__author__ = "thorko"


import http.client
import urllib.parse

from kupfer.objects import Action, TextLeaf
from kupfer import utils, plugin_support, config


class PsonoSearch (Action):
    def __init__(self):
        Action.__init__(self, _("Psono Search"))

    def activate(self, leaf):
        query_url = "https://pw.thorko.de/#!/datastore/search/" + leaf.object
        utils.show_url(query_url)

    def item_types(self):
        yield TextLeaf

    def get_description(self):
        return _("Search your passwords")

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
