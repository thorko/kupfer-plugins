__kupfer_name__ = _("Psono")
__kupfer_actions__ = ("PsonoPass", )
__description__ = _("Copy password to clipboard (copyq)")
__version__ = "2020-7"
__author__ = "thorko"

import subprocess
import json
from kupfer.objects import Action, TextLeaf, Source, TextSource, Leaf
from kupfer import utils, icons, plugin_support, kupferstring

class PsonoPass (Action):
    def __init__(self):
        Action.__init__(self, _("psono"))

    def is_factory(self):
        return True

    def activate(self, leaf):
        return SearchPass(leaf.object)

    def item_types(self):
        yield TextLeaf

    def get_description(self):
        return _("search for password")

    def get_icon_name(self):
        return "edit-find"


class SearchPass (TextSource):
    def __init__(self, text):
        TextSource.__init__(self, _("search password"))
        self.text = text

    def get_text_items(self, text):
        command = ("psoco search -js '%s'" % self.text)
        p1 = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        out, ignored_err = p1.communicate()
        d = json.loads(out)
        for l in d:
            yield PassEntry(l['match']['name'], l['match']['name'], l['match']['id'])

class PassEntry (Leaf):
    def __init__(self, obj, name, pwid):
        self.pwid = pwid
        Leaf.__init__(self, obj, name)

    def get_actions(self):
        yield CopyPass()
        yield CopyUser()

    def get_icon_name(self):
        return "dialog-password"

class CopyUser(Action):
    def __init__(self):
        Action.__init__(self, _("Copy Username"))

    def activate(self, leaf):
        command = ("psoco user %s" % leaf.pwid)
        p1 = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        out, ignored_err = p1.communicate()
        utils.spawn_async(['copyq', 'add', out.decode("utf-8").strip('\n')])

    def get_icon_name(self):
        return "edit-copy"

    def get_description(self):
        return _("Copy username to clipboard")

class CopyPass (Action):
    def __init__(self):
        Action.__init__(self, _("Copy Password"))

    def activate(self, leaf):
        command = ("psoco pwd %s" % leaf.pwid)
        p1 = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        out, ignored_err = p1.communicate()
        utils.spawn_async(['copyq', 'add', out.decode("utf-8").strip('\n')])

    def get_description(self):
        return _("Copy password to clipboard")

    def get_icon_name(self):
        return "edit-copy"

    def item_types(self):
        yield TextLeaf
