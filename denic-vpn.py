__kupfer_name__ = _("VPN Denic")
__kupfer_sources__ = ("VPN",)
__description__ = _("handle VPN connections")
__version__ = "2018-9"
__author__ = "thorko"

from kupfer.objects import Source, RunnableLeaf, TextLeaf
from kupfer import utils, plugin_support, config

class VPN (Source):
    def __init__(self):
        super().__init__(_("VPN denic"))

    def initialize(self):
        pass

    def finalize(self):
        pass

    def get_items(self):
        yield Start()
        yield Stop()
        yield Restart()

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
        vpnstart=["/usr/local/bin/vpnconnect.sh", "start"]
        utils.spawn_async(vpnstart)

    def get_icon_name(self):
        return "im-user-online"


class Stop (RunnableLeaf):
    def __init__(self):
        super().__init__(name=_("Stop"))

    def run(self):
        vpnstop=["/usr/local/bin/vpnconnect.sh", "stop"]
        utils.spawn_async(vpnstop)

    def get_icon_name(self):
        return "im-kick-user"

class Restart (RunnableLeaf):
    def __init__(self):
        super().__init__(name=_("Restart"))

    def run(self):
        vpnrestart=["/usr/local/bin/vpnconnect.sh", "stop", "&&", "/usr/local/bin/vpnconnect.sh", "start"]
        utils.spawn_async(vpnrestart)

    def get_icon_name(self):
        return "im-user-away"
