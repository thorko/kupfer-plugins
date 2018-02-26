__kupfer_name__ = _("HWDB")
__kupfer_actions__ = ("Hwdb", )
__description__ = _("get info from hwdb")
__version__ = "2018-2"
__author__ = "thorko"

import gi
gi.require_version('Notify', '0.7')

from kupfer.objects import Action, Leaf, TextLeaf
from kupfer import icons, uiutils
from kupfer import utils
import subprocess
from gi.repository import Notify

class Hwdb (Action):
    def __init__(self):
        Action.__init__(self, _("hwdb"))

    def wants_context(self):
        return True

    def activate(self, leaf, ctx):
        #cmd = ['ssh x10734 "hwdb ip" | grep "%s"' % leaf.object]
        cmd = ['ssh', 'x10734', 'hwdb', 'ip', '|', 'grep', '"%s"' % leaf.object]
        #info = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
        info = ""
        p = subprocess.Popen(cmd,stdout=subprocess.PIPE)
        for line in p.stdout.readlines():
            info += line.decode("utf-8")

        Notify.init("HWDB info")
        if len(info): 
            result = info
        else:
            result = "No information available"

        # display notification window
        note = Notify.Notification.new(leaf.object, result)
        note.set_timeout(6000)
        note.show()


    def item_types(self):
        yield TextLeaf

    def get_description(self):
        return _("Get information from hwdb")

    def get_icon_name(self):
        return "edit-find"

