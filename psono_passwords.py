__kupfer_name__ = _("Psono Passwords")
__kupfer_actions__ = ("PsonoPasswords", )
__description__ = _("Search Psono Passwords")
__version__ = "2020-7"
__author__ = "thorko"

import os
from kupfer.objects import Action, TextLeaf, Source
from kupfer import utils, plugin_support, config

class PsonoPasswords (Action)
    def __init__(self):
        Action.__init__(self, _("Search for password")

    def is_factory(self):
        return True

    def activate(self, leaf):
        return Search(leaf.object)

    def item_type(self):
        yield TextLeaf

    def description(self):
        return __description__

    def get_icon_name(self):
        return "edit-find"

class Search (Source):
    def __init__(self):
        Source.__init__(self, name=_('Results for "%s"') % query)
        self.query = query

    def repr_key(self):
        return self.query

    def get_items(self):
        c = ("pwc %s" % self.query)
        p1 = subprocess.Popen(c, shell=True, stdout=subprocess.PIPE)

        def get_locate_output(proc, offset=0):
            out, ignored_err = proc.communicate()
            return (ConstructFileLeaf(kupferstring.fromlocale(f))
                    for f in out.split(b'\n')[offset:-1])

        for F in get_locate_output(p1, 0):
            yield F
