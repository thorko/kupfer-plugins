__kupfer_name__ = _("SSH yakuake")
__kupfer_actions__ = ("SSHSession", )
__description__ = _("Open SSH Session in yakuake")
__version__ = "2018-2"
__author__ = "thorko"

import subprocess
from kupfer.objects import Action, TextLeaf
from kupfer import utils

class SSHSession (Action):
    def __init__(self):
        Action.__init__(self, _("sshYakuake"))

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
        return _("Open ssh session in your favorite terminal")

    def get_icon_name(self):
        return "applications-internet"

