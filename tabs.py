__kupfer_name__ = _("SearchTabs")
__kupfer_actions__ = ("SearchTabs", "TabActivation", )
__description__ = _("Browser Tabs")
__version__ = "2021.4"
__author__ = "Thorsten Mueller"

import subprocess
from time import sleep
from kupfer.objects import Leaf, Action, TextSource, TextLeaf

class SearchTabs(Action):
    def __init__(self):
        Action.__init__(self, _("SearchTabs"))

    def is_factory(self):
        return True

    def activate(self, leaf):
        command = ("brotab index")
        p1 = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        sleep(2)
        return TabLeaf(leaf.object)

    def item_types(self):
        yield TextLeaf

    def get_description(self):
        return _("Tabs")

    def get_icon_name(self):
        return "web-browser"

class TabLeaf(TextSource):
    def __init__(self, query):
        TextSource.__init__(self, name=_("Results for '%s'") % query)
        self.text = query

    def get_text_items(self, text):
        command = ("brotab search '%s'" % self.text)
        p1 = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        out, ignored_err = p1.communicate()
        for t in out.split(b'\n'):
            if t != b'':
                k = t.decode('UTF-8').split('\t')
                yield TabEntry(k[0], k[1], k[0])

class TabEntry (Leaf):
    def __init__(self, obj, name, tabid):
        self.tabid = tabid
        Leaf.__init__(self, obj, name)

    def get_actions(self):
        yield TabActivation()

    def get_icon_name(self):
        return "web-browser"


class TabActivation(Action):
    def __init__(self):
        super().__init__(_("Activate Tab"))

    def activate(self, leaf):
        command = ("brotab activate %s" % leaf.tabid)
        p1 = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        out, ignored_err = p1.communicate()

    def get_icon_name(self):
        return "go-jump"
