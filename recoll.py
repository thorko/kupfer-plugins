__kupfer_name__ = _("Recoll search documents")
__kupfer_actions__ = ("RecollIndex", )
__description__ = _("Search in recollindex")
__version__ = "2017-1"
__author__ = "thorko"

from kupfer.obj import Action, TextLeaf
from kupfer import launch
from kupfer.support import pretty

class RecollIndex (Action):
    def __init__(self):
        Action.__init__(self, _("Recollindex Search"))

    def activate(self, leaf):
        search_cmd = ["recoll", "-q", leaf.object]
        launch.spawn_async(search_cmd)

    def item_types(self):
        yield TextLeaf

    def get_description(self):
        return _("Search in your recollindex")

    def get_icon_name(self):
        return "recoll"
