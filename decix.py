__kupfer_name__ = _("DE-CIX")
__kupfer_sources__ = ("WORK",)
__description__ = _("handle DE-CIX work")
__version__ = "2018-9"
__author__ = "thorko"

from kupfer.objects import Source, RunnableLeaf, TextLeaf
from kupfer import utils, plugin_support, config

class WORK (Source):
    def __init__(self):
        super().__init__(_("DE-CIX WORK"))

    def initialize(self):
        pass

    def finalize(self):
        pass

    def get_items(self):
        yield Start()
        yield Stop()

    def provides(self):
        yield RunnableLeaf

    def description(self):
        return __description__

    def get_icon_name(self):
        return "im-user"

class Start (RunnableLeaf):
    def __init__(self):
        super().__init__(name=_("Start"))

    def run(self):
        vpnstart=["/usr/bin/nmcli", "con", "up", "de-cix"]
        timecalc=["/home/thorko/bin/work.sh", "start"]
        utils.spawn_async(vpnstart)
        utils.spawn_async(timecalc)

    def get_icon_name(self):
        return "im-user-online"


class Stop (RunnableLeaf):
    def __init__(self):
        super().__init__(name=_("Stop"))

    def run(self):
        vpnstop=["/usr/bin/nmcli", "con", "down", "de-cix"]
        timecalc=["/home/thorko/bin/work.sh", "stop"]
        utils.spawn_async(vpnstop)
        utils.spawn_async(timecalc)

    def get_icon_name(self):
        return "im-kick-user"
