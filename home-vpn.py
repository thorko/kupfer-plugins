__kupfer_name__ = _("HomeVPN")
__kupfer_sources__ = ("HomeVPN",)
__description__ = _("handle VPN connections")
__version__ = "2018-9"
__author__ = "thorko"

from kupfer.objects import Source, RunnableLeaf, TextLeaf
from kupfer import utils, plugin_support, config

class HomeVPN (Source):
    def __init__(self):
        super().__init__(_("HomeVPN"))

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
        vpnstart=["sudo", "systemctl", "start", "tinc@work"]
        utils.spawn_async(vpnstart)

    def get_icon_name(self):
        return "im-user-online"


class Stop (RunnableLeaf):
    def __init__(self):
        super().__init__(name=_("Stop"))

    def run(self):
        vpnstop=["sudo", "systemctl", "stop", "tinc@work"]
        utils.spawn_async(vpnstop)

    def get_icon_name(self):
        return "im-kick-user"

