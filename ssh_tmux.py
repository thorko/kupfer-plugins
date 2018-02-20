__kupfer_name__ = _("SSH tmux")
__kupfer_actions__ = ("SshTmux", )
__description__ = _("Open SSH Session in tmux")
__version__ = "2018-2"
__author__ = "thorko"

from kupfer.objects import Action, TextLeaf
from kupfer import utils

class SshTmux (Action):
    def __init__(self):
        Action.__init__(self, _("tmux"))

    def activate(self, leaf):
        tmux_cmd = ['tmux', 'new-window', '-n', leaf.object, 'ssh %s' % leaf.object]
        utils.spawn_async(tmux_cmd)

    def item_types(self):
        yield TextLeaf

    def get_description(self):
        return _("Open ssh session in your favorite terminal")

    def get_icon_name(self):
        return "applications-internet"

