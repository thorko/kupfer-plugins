__kupfer_name__ = _("SSH yakuake")
__kupfer_sources__ = ("SSHSession", )
__kupfer_actions__ = ("Connect", )
__description__ = _("Open SSH Session in yakuake")
__version__ = "2018-2"
__author__ = "thorko"

import subprocess
import os
from kupfer.objects import Source, Action, TextLeaf
from kupfer import utils, plugin_support


__kupfer_settings__ = plugin_support.PluginSettings(
        {
            "key": "config_file",
            "label": _("Your ssh host file"),
            "type": str,
            "value": "~/sshhosts"
        }
)
class SSHSession (Source):
    source_use_cache = False
    source_user_reloadable = True
    def __init__(self):
        super().__init__(_("SSH"))
        self.mark_for_update()

    def finalize(self):
        pass

    def is_dynamic(self):
        return True

    def get_items(self):
        series = {}
        ssh_config = os.path.expanduser(__kupfer_settings__['config_file'])
        file = open(ssh_config, "r")
        for x in file.readlines():
            series[x.strip("\n")] = x.strip("\n")

        return[Host(value, key) for key, value in series.items()]

    def provides(self):
        yield TextLeaf

    def get_gicon(self):
        return "view-presentation"
    
    def description(self):
        return __description__

    def get_icon_name(self):
        return "view-presentation"

class Host (TextLeaf):
    def __init__(self, value, key):
        TextLeaf.__init__(self, value, name=key)

    def get_icon_name(self):
        return "path-reverse"

class Connect (Action):
    def __init__(self):
        Action.__init__(self, _("connect..."))

    def activate(self, leaf):
        new_cmd = ['qdbus', 'org.kde.yakuake', '/yakuake/sessions', 'org.kde.yakuake.addSession']
        run_cmd = ['qdbus', 'org.kde.yakuake', '/yakuake/sessions', 'runCommand', 'ssh %s' % leaf.object]
        open_cmd = ['qdbus', 'org.kde.yakuake', '/yakuake/window', 'org.kde.yakuake.toggleWindowState']
        utils.spawn_async(new_cmd)
        utils.spawn_async(open_cmd)
        utils.spawn_async(run_cmd)

    def item_types(self):
        yield TextLeaf

    def get_description(self):
        return _("Open ssh session in your yakuake")

    def get_icon_name(self):
        return "applications-internet"

