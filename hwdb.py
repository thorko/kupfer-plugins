__kupfer_name__ = _("HwDB")
__kupfer_actions__ = ("HwDB", )
__description__ = _("Search hwdb")
__version__ = "2018-6"
__author__ = "thorko"

from kupfer.objects import Action, TextLeaf, Leaf, RunnableLeaf, Source
from kupfer import utils, plugin_support, config
import pprint

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

    def wants_context(self):
        return True

    def activate_multiple(self, leav, iobjs):
        for app in iobjs:
            app.run(leav)

    def activate(self, leaf, iobj, ctx):
        self.activate_multiple(leaf.object, (iobj, ))

    def item_types(self):
        yield TextLeaf

    def get_description(self):
        return _("Search hwdb in browser")

    def get_icon_name(self):
        return "view-bank"

    def requires_object(self):
        return True

    def object_types(self):
        yield RunnableLeaf

    def object_source(self, for_item=None):
        return _GetActions()

class _GetActions (Source):
    def __init__(self):
        super().__init__(name=_("Actions"))

    def get_items(self):
        yield Search()
        yield Host()

class Search (RunnableLeaf):
    def __init__(self):
        super().__init__(name=_("Search"))

    def run(self, leaf):
        browser_type = __kupfer_settings__["browser_type"]
        searchhwdb = [browser_type, 'https://nannyfe.prod.denic.de/search?Search=Search&searchpattern=%s' % leaf]
        utils.spawn_async(searchhwdb)

    def item_types(self):
        yield TextLeaf

    def get_icon_name(self):
        return "edit-find"

class Host (RunnableLeaf):
    def __init__(self):
        super().__init__(name=_("Host"))

    def run(self, leaf):
        browser_type = __kupfer_settings__["browser_type"]
        searchhwdb = [browser_type, 'https://nannyfe.prod.denic.de/host/%s' % leaf]
        utils.spawn_async(searchhwdb)

    def item_types(self):
        yield TextLeaf

    def get_icon_name(self):
        return "node"
