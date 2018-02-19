__kupfer_name__ = _("SSH terminator")
__kupfer_actions__ = ("SshTerminator", )
__description__ = _("Open SSH Session in terminator")
__version__ = "2018-2"
__author__ = "thorko"

from kupfer.objects import Action, TextLeaf
from kupfer import utils

class SshTerminator (Action):
    def __init__(self):
        Action.__init__(self, _("SshTerminator"))

    def activate(self, leaf):
        run_cmd = ['terminator', '-m', '--new-tab', '-e', 'ssh %s' % leaf.object]
        utils.spawn_async(run_cmd)

    def item_types(self):
        yield TextLeaf

    def get_description(self):
        return _("Open ssh session in terminator")

    def get_icon_name(self):
        return "applications-internet"

