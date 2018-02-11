__kupfer_name__ = _("SSHSession")
__kupfer_actions__ = ("SSHSession", )
__description__ = _("Open SSH Session in your favorite terminal")
__version__ = "2018-2"
__author__ = "thorko"

import http.client
import urllib.parse

from kupfer.objects import Action, TextLeaf
from kupfer import utils

class SSHSession (Action):
    def __init__(self):
        Action.__init__(self, _("SSHSession"))

    def activate(self, leaf):
        search_url = "https://www.google.com/search"
        query_url = search_url + "?" + urllib.parse.urlencode({"q": leaf.object})
        utils.show_url(query_url)

    def item_types(self):
        yield TextLeaf

    def get_description(self):
        return _("Search the web with google.com")

    def get_icon_name(self):
        return "edit-find"

