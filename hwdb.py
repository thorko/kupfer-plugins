__kupfer_name__ = _("HWDB")
__kupfer_actions__ = ("Hwdb", )
__description__ = _("get info from hwdb")
__version__ = "2018-2"
__author__ = "thorko"

from kupfer.objects import Action, Leaf, TextLeaf
from kupfer import icons, uiutils
from kupfer import utils
import subprocess

class Hwdb (Action):
    def __init__(self):
        Action.__init__(self, _("hwdb"))

    def wants_context(self):
        return True

    def activate(self, leaf, ctx):
        cmd = ['ssh x10734 "hwdb ip" | grep %s' % leaf.object]
        info = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)

        # display result
        uiutils.show_text_result(info.decode("utf-8"), title=_("HWDB"), ctx=ctx)

    def item_types(self):
        yield TextLeaf

    def get_description(self):
        return _("Get information from hwdb")

    def get_icon_name(self):
        return "applications-internet"

